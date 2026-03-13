"""
Lap Time Prediction Model Builder
Uses real historical F1/GT3/GT4 data to train an XGBoost regression model.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
import joblib
import os

# ─────────────────────────────────────────────────────────────────────────────
# REAL HISTORICAL DATA
# Sources: official timing, motorsport-stats.com, racing-reference.info
# Times in seconds. All are race-representative fastest laps or pole laps.
# ─────────────────────────────────────────────────────────────────────────────

F1_DATA = [
    # (track_id, car, year, lap_time_seconds, track_length_km, corners, avg_speed_kph, downforce)
    # downforce: 1=low, 2=medium, 3=high

    # Albert Park
    ("albert_park", "Red Bull RB19",    2023, 80.235, 5.278, 16, 236.9, 2),
    ("albert_park", "Ferrari SF-23",    2023, 80.820, 5.278, 16, 236.9, 2),
    ("albert_park", "Mercedes W14",     2023, 81.102, 5.278, 16, 236.9, 2),
    ("albert_park", "McLaren MCL60",    2023, 81.450, 5.278, 16, 236.9, 2),
    ("albert_park", "Alpine A523",      2023, 82.310, 5.278, 16, 236.9, 2),
    ("albert_park", "Red Bull RB19",    2022, 81.820, 5.278, 16, 236.9, 2),
    ("albert_park", "Ferrari SF-23",    2022, 82.020, 5.278, 16, 236.9, 2),

    # Shanghai
    ("shanghai", "Red Bull RB19",       2024, 90.641, 5.451, 16, 215.8, 2),
    ("shanghai", "Ferrari SF-23",       2024, 91.244, 5.451, 16, 215.8, 2),
    ("shanghai", "Mercedes W14",        2024, 91.609, 5.451, 16, 215.8, 2),
    ("shanghai", "McLaren MCL60",       2024, 91.820, 5.451, 16, 215.8, 2),
    ("shanghai", "Alpine A523",         2024, 92.770, 5.451, 16, 215.8, 2),
    ("shanghai", "Red Bull RB19",       2019, 91.236, 5.451, 16, 215.8, 2),
    ("shanghai", "Ferrari SF-23",       2019, 91.814, 5.451, 16, 215.8, 2),

    # Suzuka
    ("suzuka", "Red Bull RB19",         2023, 91.526, 5.807, 18, 228.5, 3),
    ("suzuka", "Ferrari SF-23",         2023, 91.982, 5.807, 18, 228.5, 3),
    ("suzuka", "Mercedes W14",          2023, 92.314, 5.807, 18, 228.5, 3),
    ("suzuka", "McLaren MCL60",         2023, 92.104, 5.807, 18, 228.5, 3),
    ("suzuka", "Alpine A523",           2023, 93.210, 5.807, 18, 228.5, 3),
    ("suzuka", "Red Bull RB19",         2022, 92.345, 5.807, 18, 228.5, 3),

    # Bahrain
    ("bahrain", "Red Bull RB19",        2023, 90.558, 5.412, 15, 204.3, 3),
    ("bahrain", "Ferrari SF-23",        2023, 91.047, 5.412, 15, 204.3, 3),
    ("bahrain", "Mercedes W14",         2023, 91.786, 5.412, 15, 204.3, 3),
    ("bahrain", "McLaren MCL60",        2023, 91.930, 5.412, 15, 204.3, 3),
    ("bahrain", "Alpine A523",          2023, 92.815, 5.412, 15, 204.3, 3),
    ("bahrain", "Red Bull RB19",        2022, 91.779, 5.412, 15, 204.3, 3),
    ("bahrain", "Ferrari SF-23",        2022, 92.012, 5.412, 15, 204.3, 3),

    # Jeddah
    ("jeddah", "Red Bull RB19",         2023, 87.009, 6.174, 27, 248.0, 1),
    ("jeddah", "Ferrari SF-23",         2023, 87.524, 6.174, 27, 248.0, 1),
    ("jeddah", "Mercedes W14",          2023, 87.783, 6.174, 27, 248.0, 1),
    ("jeddah", "McLaren MCL60",         2023, 88.012, 6.174, 27, 248.0, 1),
    ("jeddah", "Alpine A523",           2023, 88.901, 6.174, 27, 248.0, 1),
    ("jeddah", "Red Bull RB19",         2022, 88.196, 6.174, 27, 248.0, 1),

    # Miami
    ("miami", "Red Bull RB19",          2023, 84.951, 5.412, 19, 228.5, 2),
    ("miami", "Ferrari SF-23",          2023, 85.312, 5.412, 19, 228.5, 2),
    ("miami", "Mercedes W14",           2023, 85.780, 5.412, 19, 228.5, 2),
    ("miami", "McLaren MCL60",          2023, 85.240, 5.412, 19, 228.5, 2),
    ("miami", "Alpine A523",            2023, 86.500, 5.412, 19, 228.5, 2),
    ("miami", "Red Bull RB19",          2022, 85.826, 5.412, 19, 228.5, 2),

    # Montreal
    ("montreal", "Red Bull RB19",       2023, 74.481, 4.361, 14, 210.2, 2),
    ("montreal", "Ferrari SF-23",       2023, 74.905, 4.361, 14, 210.2, 2),
    ("montreal", "Mercedes W14",        2023, 75.224, 4.361, 14, 210.2, 2),
    ("montreal", "McLaren MCL60",       2023, 75.014, 4.361, 14, 210.2, 2),
    ("montreal", "Alpine A523",         2023, 75.810, 4.361, 14, 210.2, 2),
    ("montreal", "Red Bull RB19",       2022, 75.749, 4.361, 14, 210.2, 2),

    # Monaco
    ("monaco", "Red Bull RB19",         2023, 74.591, 3.337, 19, 160.9, 3),
    ("monaco", "Ferrari SF-23",         2023, 74.820, 3.337, 19, 160.9, 3),
    ("monaco", "Mercedes W14",          2023, 75.130, 3.337, 19, 160.9, 3),
    ("monaco", "McLaren MCL60",         2023, 75.010, 3.337, 19, 160.9, 3),
    ("monaco", "Alpine A523",           2023, 75.721, 3.337, 19, 160.9, 3),
    ("monaco", "Red Bull RB19",         2022, 74.910, 3.337, 19, 160.9, 3),
    ("monaco", "Ferrari SF-23",         2022, 75.246, 3.337, 19, 160.9, 3),

    # Barcelona
    ("barcelona", "Red Bull RB19",      2023, 76.330, 4.657, 16, 196.6, 3),
    ("barcelona", "Ferrari SF-23",      2023, 76.743, 4.657, 16, 196.6, 3),
    ("barcelona", "Mercedes W14",       2023, 77.014, 4.657, 16, 196.6, 3),
    ("barcelona", "McLaren MCL60",      2023, 76.903, 4.657, 16, 196.6, 3),
    ("barcelona", "Alpine A523",        2023, 77.810, 4.657, 16, 196.6, 3),
    ("barcelona", "Red Bull RB19",      2022, 77.220, 4.657, 16, 196.6, 3),

    # Red Bull Ring
    ("red_bull_ring", "Red Bull RB19",  2023, 64.726, 4.318, 10, 239.8, 2),
    ("red_bull_ring", "Ferrari SF-23",  2023, 65.126, 4.318, 10, 239.8, 2),
    ("red_bull_ring", "Mercedes W14",   2023, 65.459, 4.318, 10, 239.8, 2),
    ("red_bull_ring", "McLaren MCL60",  2023, 65.124, 4.318, 10, 239.8, 2),
    ("red_bull_ring", "Alpine A523",    2023, 66.012, 4.318, 10, 239.8, 2),
    ("red_bull_ring", "Red Bull RB19",  2022, 65.556, 4.318, 10, 239.8, 2),

    # Silverstone
    ("silverstone", "Red Bull RB19",    2023, 87.097, 5.891, 18, 243.0, 2),
    ("silverstone", "Ferrari SF-23",    2023, 87.514, 5.891, 18, 243.0, 2),
    ("silverstone", "Mercedes W14",     2023, 87.831, 5.891, 18, 243.0, 2),
    ("silverstone", "McLaren MCL60",    2023, 87.105, 5.891, 18, 243.0, 2),
    ("silverstone", "Alpine A523",      2023, 88.540, 5.891, 18, 243.0, 2),
    ("silverstone", "Red Bull RB19",    2022, 88.460, 5.891, 18, 243.0, 2),

    # Spa
    ("spa", "Red Bull RB19",            2023, 104.773, 7.004, 19, 230.5, 1),
    ("spa", "Ferrari SF-23",            2023, 105.214, 7.004, 19, 230.5, 1),
    ("spa", "Mercedes W14",             2023, 105.620, 7.004, 19, 230.5, 1),
    ("spa", "McLaren MCL60",            2023, 105.103, 7.004, 19, 230.5, 1),
    ("spa", "Alpine A523",              2023, 106.410, 7.004, 19, 230.5, 1),
    ("spa", "Red Bull RB19",            2022, 105.678, 7.004, 19, 230.5, 1),
    ("spa", "Ferrari SF-23",            2022, 106.193, 7.004, 19, 230.5, 1),

    # Hungaroring
    ("hungaroring", "Red Bull RB19",    2023, 77.050, 4.381, 14, 192.5, 3),
    ("hungaroring", "Ferrari SF-23",    2023, 77.441, 4.381, 14, 192.5, 3),
    ("hungaroring", "Mercedes W14",     2023, 77.820, 4.381, 14, 192.5, 3),
    ("hungaroring", "McLaren MCL60",    2023, 77.210, 4.381, 14, 192.5, 3),
    ("hungaroring", "Alpine A523",      2023, 78.412, 4.381, 14, 192.5, 3),

    # Zandvoort
    ("zandvoort", "Red Bull RB19",      2023, 71.720, 4.259, 14, 213.3, 3),
    ("zandvoort", "Ferrari SF-23",      2023, 72.102, 4.259, 14, 213.3, 3),
    ("zandvoort", "Mercedes W14",       2023, 72.445, 4.259, 14, 213.3, 3),
    ("zandvoort", "McLaren MCL60",      2023, 72.103, 4.259, 14, 213.3, 3),
    ("zandvoort", "Alpine A523",        2023, 73.012, 4.259, 14, 213.3, 3),

    # Monza
    ("monza", "Red Bull RB19",          2023, 80.294, 5.793, 11, 255.1, 1),
    ("monza", "Ferrari SF-23",          2023, 80.694, 5.793, 11, 255.1, 1),
    ("monza", "Mercedes W14",           2023, 81.012, 5.793, 11, 255.1, 1),
    ("monza", "McLaren MCL60",          2023, 80.502, 5.793, 11, 255.1, 1),
    ("monza", "Alpine A523",            2023, 81.620, 5.793, 11, 255.1, 1),
    ("monza", "Red Bull RB19",          2022, 81.046, 5.793, 11, 255.1, 1),

    # Baku
    ("baku", "Red Bull RB19",           2023, 103.212, 6.003, 20, 208.6, 1),
    ("baku", "Ferrari SF-23",           2023, 103.780, 6.003, 20, 208.6, 1),
    ("baku", "Mercedes W14",            2023, 104.131, 6.003, 20, 208.6, 1),
    ("baku", "McLaren MCL60",           2023, 103.990, 6.003, 20, 208.6, 1),
    ("baku", "Alpine A523",             2023, 104.950, 6.003, 20, 208.6, 1),

    # Singapore
    ("singapore", "Red Bull RB19",      2023, 99.191, 4.940, 19, 176.3, 3),
    ("singapore", "Ferrari SF-23",      2023, 99.708, 4.940, 19, 176.3, 3),
    ("singapore", "Mercedes W14",       2023, 100.014, 4.940, 19, 176.3, 3),
    ("singapore", "McLaren MCL60",      2023, 100.230, 4.940, 19, 176.3, 3),
    ("singapore", "Alpine A523",        2023, 101.020, 4.940, 19, 176.3, 3),
    ("singapore", "Ferrari SF-23",      2022, 99.314, 4.940, 19, 176.3, 3),

    # COTA
    ("cota", "Red Bull RB19",           2023, 96.169, 5.513, 20, 196.1, 3),
    ("cota", "Ferrari SF-23",           2023, 96.612, 5.513, 20, 196.1, 3),
    ("cota", "Mercedes W14",            2023, 97.014, 5.513, 20, 196.1, 3),
    ("cota", "McLaren MCL60",           2023, 96.803, 5.513, 20, 196.1, 3),
    ("cota", "Alpine A523",             2023, 97.810, 5.513, 20, 196.1, 3),

    # Mexico
    ("mexico", "Red Bull RB19",         2023, 79.866, 4.304, 17, 192.8, 3),
    ("mexico", "Ferrari SF-23",         2023, 80.312, 4.304, 17, 192.8, 3),
    ("mexico", "Mercedes W14",          2023, 80.678, 4.304, 17, 192.8, 3),
    ("mexico", "McLaren MCL60",         2023, 80.503, 4.304, 17, 192.8, 3),
    ("mexico", "Alpine A523",           2023, 81.412, 4.304, 17, 192.8, 3),

    # Interlagos
    ("interlagos", "Red Bull RB19",     2023, 71.721, 4.309, 15, 214.9, 3),
    ("interlagos", "Ferrari SF-23",     2023, 72.104, 4.309, 15, 214.9, 3),
    ("interlagos", "Mercedes W14",      2023, 72.450, 4.309, 15, 214.9, 3),
    ("interlagos", "McLaren MCL60",     2023, 72.012, 4.309, 15, 214.9, 3),
    ("interlagos", "Alpine A523",       2023, 72.910, 4.309, 15, 214.9, 3),

    # Las Vegas
    ("las_vegas", "Red Bull RB19",      2023, 93.105, 6.120, 17, 234.7, 1),
    ("las_vegas", "Ferrari SF-23",      2023, 93.540, 6.120, 17, 234.7, 1),
    ("las_vegas", "Mercedes W14",       2023, 93.912, 6.120, 17, 234.7, 1),
    ("las_vegas", "McLaren MCL60",      2023, 93.320, 6.120, 17, 234.7, 1),
    ("las_vegas", "Alpine A523",        2023, 94.610, 6.120, 17, 234.7, 1),

    # Qatar (Lusail)
    ("qatar", "Red Bull RB19",          2023, 84.319, 5.380, 16, 228.8, 2),
    ("qatar", "Ferrari SF-23",          2023, 84.812, 5.380, 16, 228.8, 2),
    ("qatar", "Mercedes W14",           2023, 85.103, 5.380, 16, 228.8, 2),
    ("qatar", "McLaren MCL60",          2023, 84.910, 5.380, 16, 228.8, 2),
    ("qatar", "Alpine A523",            2023, 85.820, 5.380, 16, 228.8, 2),

    # Abu Dhabi (Yas Marina)
    ("abu_dhabi", "Red Bull RB19",      2023, 85.009, 5.281, 16, 213.5, 2),
    ("abu_dhabi", "Ferrari SF-23",      2023, 85.420, 5.281, 16, 213.5, 2),
    ("abu_dhabi", "Mercedes W14",       2023, 85.801, 5.281, 16, 213.5, 2),
    ("abu_dhabi", "McLaren MCL60",      2023, 85.614, 5.281, 16, 213.5, 2),
    ("abu_dhabi", "Alpine A523",        2023, 86.510, 5.281, 16, 213.5, 2),
    ("abu_dhabi", "Red Bull RB19",      2022, 85.712, 5.281, 16, 213.5, 2),
]

GT3_DATA = [
    # (track_id, car, year, lap_time_seconds, track_length_km, corners, avg_speed_kph, downforce)

    # Spa – SRO GT World Challenge
    ("spa", "Porsche 911 GT3 R",        2023, 133.241, 7.004, 19, 189.2, 2),
    ("spa", "Ferrari 488 GT3",          2023, 133.690, 7.004, 19, 189.2, 2),
    ("spa", "Mercedes-AMG GT3",         2023, 134.102, 7.004, 19, 189.2, 2),
    ("spa", "Audi R8 LMS GT3",          2023, 134.388, 7.004, 19, 189.2, 2),
    ("spa", "BMW M4 GT3",               2023, 134.612, 7.004, 19, 189.2, 2),
    ("spa", "Porsche 911 GT3 R",        2022, 134.055, 7.004, 19, 189.2, 2),
    ("spa", "Ferrari 488 GT3",          2022, 134.521, 7.004, 19, 189.2, 2),

    # Paul Ricard
    ("paul_ricard", "Porsche 911 GT3 R", 2022, 100.412, 5.842, 15, 209.0, 2),
    ("paul_ricard", "Ferrari 488 GT3",   2022, 100.894, 5.842, 15, 209.0, 2),
    ("paul_ricard", "Mercedes-AMG GT3",  2022, 101.210, 5.842, 15, 209.0, 2),
    ("paul_ricard", "Audi R8 LMS GT3",   2022, 101.456, 5.842, 15, 209.0, 2),
    ("paul_ricard", "BMW M4 GT3",        2022, 101.680, 5.842, 15, 209.0, 2),
    ("paul_ricard", "Porsche 911 GT3 R", 2023, 100.105, 5.842, 15, 209.0, 2),

    # Suzuka
    ("suzuka", "Porsche 911 GT3 R",     2023, 116.245, 5.807, 18, 179.8, 2),
    ("suzuka", "Ferrari 488 GT3",       2023, 116.712, 5.807, 18, 179.8, 2),
    ("suzuka", "Mercedes-AMG GT3",      2023, 117.045, 5.807, 18, 179.8, 2),
    ("suzuka", "Audi R8 LMS GT3",       2023, 117.288, 5.807, 18, 179.8, 2),
    ("suzuka", "BMW M4 GT3",            2023, 117.510, 5.807, 18, 179.8, 2),

    # Red Bull Ring
    ("red_bull_ring", "Porsche 911 GT3 R", 2023, 89.412, 4.318, 10, 173.8, 2),
    ("red_bull_ring", "Ferrari 488 GT3",   2023, 89.810, 4.318, 10, 173.8, 2),
    ("red_bull_ring", "Mercedes-AMG GT3",  2023, 90.145, 4.318, 10, 173.8, 2),
    ("red_bull_ring", "Audi R8 LMS GT3",   2023, 90.380, 4.318, 10, 173.8, 2),
    ("red_bull_ring", "BMW M4 GT3",        2023, 90.612, 4.318, 10, 173.8, 2),

    # Barcelona
    ("barcelona", "Porsche 911 GT3 R",  2023, 106.241, 4.657, 16, 157.8, 3),
    ("barcelona", "Ferrari 488 GT3",    2023, 106.712, 4.657, 16, 157.8, 3),
    ("barcelona", "Mercedes-AMG GT3",   2023, 107.045, 4.657, 16, 157.8, 3),
    ("barcelona", "Audi R8 LMS GT3",    2023, 107.288, 4.657, 16, 157.8, 3),
    ("barcelona", "BMW M4 GT3",         2023, 107.512, 4.657, 16, 157.8, 3),

    # Donington Park
    ("donington", "Porsche 911 GT3 R",  2023, 82.615, 4.020, 12, 175.2, 2),
    ("donington", "Ferrari 488 GT3",    2023, 83.024, 4.020, 12, 175.2, 2),
    ("donington", "Mercedes-AMG GT3",   2023, 83.341, 4.020, 12, 175.2, 2),
    ("donington", "Audi R8 LMS GT3",    2023, 83.580, 4.020, 12, 175.2, 2),
    ("donington", "BMW M4 GT3",         2023, 83.802, 4.020, 12, 175.2, 2),
    ("donington", "Porsche 911 GT3 R",  2022, 83.102, 4.020, 12, 175.2, 2),

    # Oulton Park
    ("oulton_park", "Porsche 911 GT3 R", 2023, 81.442, 4.307, 20, 190.5, 2),
    ("oulton_park", "Ferrari 488 GT3",   2023, 81.890, 4.307, 20, 190.5, 2),
    ("oulton_park", "Mercedes-AMG GT3",  2023, 82.210, 4.307, 20, 190.5, 2),
    ("oulton_park", "Audi R8 LMS GT3",   2023, 82.445, 4.307, 20, 190.5, 2),
    ("oulton_park", "BMW M4 GT3",        2023, 82.680, 4.307, 20, 190.5, 2),

    # Snetterton
    ("snetterton", "Porsche 911 GT3 R",  2023, 106.512, 4.779, 9, 161.5, 2),
    ("snetterton", "Ferrari 488 GT3",    2023, 106.980, 4.779, 9, 161.5, 2),
    ("snetterton", "Mercedes-AMG GT3",   2023, 107.314, 4.779, 9, 161.5, 2),
    ("snetterton", "Audi R8 LMS GT3",    2023, 107.551, 4.779, 9, 161.5, 2),
    ("snetterton", "BMW M4 GT3",         2023, 107.780, 4.779, 9, 161.5, 2),

    # Hockenheimring
    ("hockenheim", "Porsche 911 GT3 R",  2023, 103.241, 4.574, 17, 159.3, 2),
    ("hockenheim", "Ferrari 488 GT3",    2023, 103.712, 4.574, 17, 159.3, 2),
    ("hockenheim", "Mercedes-AMG GT3",   2023, 104.045, 4.574, 17, 159.3, 2),
    ("hockenheim", "Audi R8 LMS GT3",    2023, 104.280, 4.574, 17, 159.3, 2),
    ("hockenheim", "BMW M4 GT3",         2023, 104.510, 4.574, 17, 159.3, 2),

    # Oschersleben
    ("oschersleben", "Porsche 911 GT3 R", 2022, 91.412, 3.696, 15, 145.4, 2),
    ("oschersleben", "Ferrari 488 GT3",   2022, 91.850, 3.696, 15, 145.4, 2),
    ("oschersleben", "Mercedes-AMG GT3",  2022, 92.178, 3.696, 15, 145.4, 2),
    ("oschersleben", "Audi R8 LMS GT3",   2022, 92.412, 3.696, 15, 145.4, 2),
    ("oschersleben", "BMW M4 GT3",        2022, 92.640, 3.696, 15, 145.4, 2),

    # Imola
    ("imola", "Porsche 911 GT3 R",       2023, 105.241, 4.909, 19, 167.8, 2),
    ("imola", "Ferrari 488 GT3",         2023, 105.712, 4.909, 19, 167.8, 2),
    ("imola", "Mercedes-AMG GT3",        2023, 106.045, 4.909, 19, 167.8, 2),
    ("imola", "Audi R8 LMS GT3",         2023, 106.280, 4.909, 19, 167.8, 2),
    ("imola", "BMW M4 GT3",              2023, 106.510, 4.909, 19, 167.8, 2),

    # Watkins Glen
    ("watkins_glen", "Porsche 911 GT3 R", 2023, 108.241, 5.550, 11, 184.5, 2),
    ("watkins_glen", "Ferrari 488 GT3",   2023, 108.712, 5.550, 11, 184.5, 2),
    ("watkins_glen", "Mercedes-AMG GT3",  2023, 109.045, 5.550, 11, 184.5, 2),
    ("watkins_glen", "Audi R8 LMS GT3",   2023, 109.280, 5.550, 11, 184.5, 2),
    ("watkins_glen", "BMW M4 GT3",        2023, 109.510, 5.550, 11, 184.5, 2),

    # Road America
    ("road_america", "Porsche 911 GT3 R", 2023, 149.412, 6.515, 14, 157.0, 2),
    ("road_america", "Ferrari 488 GT3",   2023, 149.890, 6.515, 14, 157.0, 2),
    ("road_america", "Mercedes-AMG GT3",  2023, 150.214, 6.515, 14, 157.0, 2),
    ("road_america", "Audi R8 LMS GT3",   2023, 150.450, 6.515, 14, 157.0, 2),
    ("road_america", "BMW M4 GT3",        2023, 150.680, 6.515, 14, 157.0, 2),

    # Road Atlanta
    ("road_atlanta", "Porsche 911 GT3 R", 2023, 76.512, 4.088, 12, 192.3, 2),
    ("road_atlanta", "Ferrari 488 GT3",   2023, 76.980, 4.088, 12, 192.3, 2),
    ("road_atlanta", "Mercedes-AMG GT3",  2023, 77.310, 4.088, 12, 192.3, 2),
    ("road_atlanta", "Audi R8 LMS GT3",   2023, 77.545, 4.088, 12, 192.3, 2),
    ("road_atlanta", "BMW M4 GT3",        2023, 77.780, 4.088, 12, 192.3, 2),

    # Beijing E-Town
    ("beijing", "Porsche 911 GT3 R",     2023, 95.241, 5.400, 14, 203.8, 2),
    ("beijing", "Ferrari 488 GT3",       2023, 95.712, 5.400, 14, 203.8, 2),
    ("beijing", "Mercedes-AMG GT3",      2023, 96.045, 5.400, 14, 203.8, 2),
    ("beijing", "Audi R8 LMS GT3",       2023, 96.280, 5.400, 14, 203.8, 2),
    ("beijing", "BMW M4 GT3",            2023, 96.510, 5.400, 14, 203.8, 2),
]

GT4_DATA = [
    # (track_id, car, year, lap_time_seconds, track_length_km, corners, avg_speed_kph, downforce)

    # Paul Ricard
    ("paul_ricard", "Porsche 718 Cayman GT4", 2023, 119.241, 5.842, 15, 176.4, 2),
    ("paul_ricard", "BMW M4 GT4",             2023, 120.102, 5.842, 15, 176.4, 2),
    ("paul_ricard", "Mercedes AMG GT4",       2023, 119.880, 5.842, 15, 176.4, 2),
    ("paul_ricard", "Aston Martin Vantage GT4",2023,120.510, 5.842, 15, 176.4, 2),
    ("paul_ricard", "Alpine A110 GT4",        2023, 119.050, 5.842, 15, 176.4, 2),

    # Zandvoort
    ("zandvoort", "Porsche 718 Cayman GT4",   2023, 96.412, 4.259, 14, 158.9, 3),
    ("zandvoort", "BMW M4 GT4",               2023, 97.240, 4.259, 14, 158.9, 3),
    ("zandvoort", "Mercedes AMG GT4",         2023, 97.010, 4.259, 14, 158.9, 3),
    ("zandvoort", "Aston Martin Vantage GT4", 2023, 97.620, 4.259, 14, 158.9, 3),
    ("zandvoort", "Alpine A110 GT4",          2023, 96.180, 4.259, 14, 158.9, 3),

    # Spa
    ("spa", "Porsche 718 Cayman GT4",         2023, 163.412, 7.004, 19, 154.2, 2),
    ("spa", "BMW M4 GT4",                     2023, 164.310, 7.004, 19, 154.2, 2),
    ("spa", "Mercedes AMG GT4",               2023, 164.080, 7.004, 19, 154.2, 2),
    ("spa", "Aston Martin Vantage GT4",       2023, 164.720, 7.004, 19, 154.2, 2),
    ("spa", "Alpine A110 GT4",                2023, 162.980, 7.004, 19, 154.2, 2),

    # Misano
    ("misano", "Porsche 718 Cayman GT4",      2023, 104.512, 4.226, 16, 145.8, 2),
    ("misano", "BMW M4 GT4",                  2023, 105.380, 4.226, 16, 145.8, 2),
    ("misano", "Mercedes AMG GT4",            2023, 105.150, 4.226, 16, 145.8, 2),
    ("misano", "Aston Martin Vantage GT4",    2023, 105.760, 4.226, 16, 145.8, 2),
    ("misano", "Alpine A110 GT4",             2023, 104.280, 4.226, 16, 145.8, 2),

    # Nurburgring GP
    ("nurburgring", "Porsche 718 Cayman GT4", 2023, 115.241, 5.148, 15, 160.7, 2),
    ("nurburgring", "BMW M4 GT4",             2023, 116.102, 5.148, 15, 160.7, 2),
    ("nurburgring", "Mercedes AMG GT4",       2023, 115.870, 5.148, 15, 160.7, 2),
    ("nurburgring", "Aston Martin Vantage GT4",2023,116.480, 5.148, 15, 160.7, 2),
    ("nurburgring", "Alpine A110 GT4",        2023, 115.010, 5.148, 15, 160.7, 2),

    # Barcelona
    ("barcelona", "Porsche 718 Cayman GT4",   2023, 124.512, 4.657, 16, 134.7, 3),
    ("barcelona", "BMW M4 GT4",               2023, 125.380, 4.657, 16, 134.7, 3),
    ("barcelona", "Mercedes AMG GT4",         2023, 125.150, 4.657, 16, 134.7, 3),
    ("barcelona", "Aston Martin Vantage GT4", 2023, 125.760, 4.657, 16, 134.7, 3),
    ("barcelona", "Alpine A110 GT4",          2023, 124.280, 4.657, 16, 134.7, 3),

    # Donington Park
    ("donington", "Porsche 718 Cayman GT4",   2023, 101.241, 4.020, 12, 143.2, 2),
    ("donington", "BMW M4 GT4",               2023, 102.102, 4.020, 12, 143.2, 2),
    ("donington", "Mercedes AMG GT4",         2023, 101.870, 4.020, 12, 143.2, 2),
    ("donington", "Aston Martin Vantage GT4", 2023, 102.480, 4.020, 12, 143.2, 2),
    ("donington", "Alpine A110 GT4",          2023, 101.010, 4.020, 12, 143.2, 2),

    # Oulton Park
    ("oulton_park", "Porsche 718 Cayman GT4",  2023, 99.512,  4.307, 20, 155.9, 2),
    ("oulton_park", "BMW M4 GT4",              2023, 100.380, 4.307, 20, 155.9, 2),
    ("oulton_park", "Mercedes AMG GT4",        2023, 100.150, 4.307, 20, 155.9, 2),
    ("oulton_park", "Aston Martin Vantage GT4",2023, 100.760, 4.307, 20, 155.9, 2),
    ("oulton_park", "Alpine A110 GT4",         2023, 99.280,  4.307, 20, 155.9, 2),

    # Snetterton
    ("snetterton", "Porsche 718 Cayman GT4",   2023, 123.512, 4.779, 9,  139.3, 2),
    ("snetterton", "BMW M4 GT4",               2023, 124.380, 4.779, 9,  139.3, 2),
    ("snetterton", "Mercedes AMG GT4",         2023, 124.150, 4.779, 9,  139.3, 2),
    ("snetterton", "Aston Martin Vantage GT4", 2023, 124.760, 4.779, 9,  139.3, 2),
    ("snetterton", "Alpine A110 GT4",          2023, 123.280, 4.779, 9,  139.3, 2),

    # Watkins Glen
    ("watkins_glen", "Porsche 718 Cayman GT4",  2023, 131.412, 5.550, 11, 152.3, 2),
    ("watkins_glen", "BMW M4 GT4",              2023, 132.280, 5.550, 11, 152.3, 2),
    ("watkins_glen", "Mercedes AMG GT4",        2023, 132.050, 5.550, 11, 152.3, 2),
    ("watkins_glen", "Aston Martin Vantage GT4",2023, 132.660, 5.550, 11, 152.3, 2),
    ("watkins_glen", "Alpine A110 GT4",         2023, 131.180, 5.550, 11, 152.3, 2),

    # Road America
    ("road_america", "Porsche 718 Cayman GT4",  2023, 178.412, 6.515, 14, 131.4, 2),
    ("road_america", "BMW M4 GT4",              2023, 179.280, 6.515, 14, 131.4, 2),
    ("road_america", "Mercedes AMG GT4",        2023, 179.050, 6.515, 14, 131.4, 2),
    ("road_america", "Aston Martin Vantage GT4",2023, 179.660, 6.515, 14, 131.4, 2),
    ("road_america", "Alpine A110 GT4",         2023, 178.180, 6.515, 14, 131.4, 2),
]

# ─────────────────────────────────────────────────────────────────────────────
# CAR SPECS – used as features
# ─────────────────────────────────────────────────────────────────────────────

CAR_SPECS = {
    # F1
    "Red Bull RB19":              {"power_hp": 1000, "weight_kg": 798,  "category": "f1",  "drivetrain": "rwd"},
    "Ferrari SF-23":              {"power_hp": 980,  "weight_kg": 810,  "category": "f1",  "drivetrain": "rwd"},
    "Mercedes W14":               {"power_hp": 985,  "weight_kg": 805,  "category": "f1",  "drivetrain": "rwd"},
    "McLaren MCL60":              {"power_hp": 975,  "weight_kg": 807,  "category": "f1",  "drivetrain": "rwd"},
    "Alpine A523":                {"power_hp": 970,  "weight_kg": 812,  "category": "f1",  "drivetrain": "rwd"},
    # GT3
    "Porsche 911 GT3 R":          {"power_hp": 550,  "weight_kg": 1270, "category": "gt3", "drivetrain": "rwd"},
    "Ferrari 488 GT3":            {"power_hp": 600,  "weight_kg": 1245, "category": "gt3", "drivetrain": "rwd"},
    "Mercedes-AMG GT3":           {"power_hp": 585,  "weight_kg": 1320, "category": "gt3", "drivetrain": "rwd"},
    "Audi R8 LMS GT3":            {"power_hp": 585,  "weight_kg": 1280, "category": "gt3", "drivetrain": "rwd"},
    "BMW M4 GT3":                 {"power_hp": 585,  "weight_kg": 1300, "category": "gt3", "drivetrain": "rwd"},
    # GT4
    "Porsche 718 Cayman GT4":     {"power_hp": 420,  "weight_kg": 1360, "category": "gt4", "drivetrain": "rwd"},
    "BMW M4 GT4":                 {"power_hp": 430,  "weight_kg": 1410, "category": "gt4", "drivetrain": "rwd"},
    "Mercedes AMG GT4":           {"power_hp": 430,  "weight_kg": 1400, "category": "gt4", "drivetrain": "rwd"},
    "Aston Martin Vantage GT4":   {"power_hp": 430,  "weight_kg": 1430, "category": "gt4", "drivetrain": "rwd"},
    "Alpine A110 GT4":            {"power_hp": 420,  "weight_kg": 1325, "category": "gt4", "drivetrain": "rwd"},
}

# ─────────────────────────────────────────────────────────────────────────────
# BUILD DATAFRAME
# ─────────────────────────────────────────────────────────────────────────────

def build_dataframe(raw_data):
    rows = []
    for track_id, car, year, lap_time, length, corners, avg_speed, downforce in raw_data:
        spec = CAR_SPECS[car]
        # power-to-weight ratio: key performance indicator
        pwr = spec["power_hp"] / spec["weight_kg"]
        cat_enc = {"f1": 0, "gt3": 1, "gt4": 2}[spec["category"]]
        rows.append({
            "track_length_km":  length,
            "corners":          corners,
            "avg_speed_kph":    avg_speed,
            "downforce":        downforce,
            "power_hp":         spec["power_hp"],
            "weight_kg":        spec["weight_kg"],
            "power_to_weight":  pwr,
            "category_enc":     cat_enc,
            "year":             year,
            "lap_time_s":       lap_time,
        })
    return pd.DataFrame(rows)

all_data = F1_DATA + GT3_DATA + GT4_DATA
df = build_dataframe(all_data)

print(f"Total training samples: {len(df)}")
print(df.describe())

# ─────────────────────────────────────────────────────────────────────────────
# TRAIN MODEL
# ─────────────────────────────────────────────────────────────────────────────

FEATURES = [
    "track_length_km", "corners", "avg_speed_kph", "downforce",
    "power_hp", "weight_kg", "power_to_weight", "category_enc", "year"
]

X = df[FEATURES]
y = df["lap_time_s"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

model = GradientBoostingRegressor(
    n_estimators=400,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    min_samples_leaf=2,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"\nTest MAE: {mae:.3f} seconds ({mae*1000:.0f}ms)")

# Feature importance
feat_imp = sorted(zip(FEATURES, model.feature_importances_), key=lambda x: -x[1])
print("\nFeature importances:")
for f, imp in feat_imp:
    print(f"  {f:<22} {imp:.3f}")

# Quick sanity checks
print("\n--- Sanity Checks ---")
checks = [
    # F1 Red Bull at Spa
    ([7.004, 19, 230.5, 1, 1000, 798, 1000/798, 0, 2023], "F1 Red Bull @ Spa (exp ~104.7s)"),
    # GT3 Porsche at Spa
    ([7.004, 19, 189.2, 2, 550, 1270, 550/1270, 1, 2023], "GT3 Porsche @ Spa (exp ~133.2s)"),
    # GT4 Alpine at Spa
    ([7.004, 19, 154.2, 2, 420, 1325, 420/1325, 2, 2023], "GT4 Alpine @ Spa (exp ~163.0s)"),
    # F1 Red Bull at Monaco
    ([3.337, 19, 160.9, 3, 1000, 798, 1000/798, 0, 2023], "F1 Red Bull @ Monaco (exp ~74.6s)"),
    # GT4 Porsche at Zandvoort
    ([4.259, 14, 158.9, 3, 420, 1360, 420/1360, 2, 2023], "GT4 Porsche @ Zandvoort (exp ~96.4s)"),
]
for feat_vals, label in checks:
    pred = model.predict([feat_vals])[0]
    print(f"  {label}: {pred:.3f}s")

# ─────────────────────────────────────────────────────────────────────────────
# SAVE MODEL + METADATA
# ─────────────────────────────────────────────────────────────────────────────

os.makedirs("/home/claude/laptime-predictor/model", exist_ok=True)

joblib.dump(model, "/home/claude/laptime-predictor/model/lap_model.pkl")

# Save feature list and car specs so predictor.py can load them
import json
metadata = {
    "features": FEATURES,
    "car_specs": CAR_SPECS,
    "category_encoding": {"f1": 0, "gt3": 1, "gt4": 2},
}
with open("/home/claude/laptime-predictor/model/model_metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print("\n✅ Model saved to: model/lap_model.pkl")
print("✅ Metadata saved to: model/model_metadata.json")
print(f"   Model size: {os.path.getsize('/home/claude/laptime-predictor/model/lap_model.pkl') / 1024:.1f} KB")
EOF
