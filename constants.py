from pathlib import Path

import numpy as np

UNKNOWN_STR = "UNKNOWN"

MAX_NUM_NANS = 8
NAN_PENALTY = 0.01

MAX_CAR_AGE = 50

DATA_PATH = Path("data")
CSV_PREDS_OUT = Path("preds.csv")

TRAIN_PATH = DATA_PATH / "train.csv"
TEST_PATH = DATA_PATH / "test.csv"
USED_CARS_SIMPLIFIED_PATH = DATA_PATH / "sg-used-cars-final-simplified.csv"

MOST_SIMILIAR_TRAIN_PATH = DATA_PATH / "most_similar_train.pkl"
MOST_SIMILIAR_TEST_PATH = DATA_PATH / "most_similar_test.pkl"

CAR_EMBEDDING_MATRIX_PATH = DATA_PATH / "car_embedding_matrix.npy"
TITLE_EMBEDDING_DICT_PATH = DATA_PATH / "title_embedding_dict.npy"

FILLED_PATH = DATA_PATH / "Filled_df"
SIM_REPLACED_TRAIN = FILLED_PATH / "train_sim_filled.csv"
SIM_REPLACED_TEST = FILLED_PATH / "test_sim_filled.csv"
ML_REPLACED_TRAIN = FILLED_PATH / "train_ML_filled.csv"
ML_REPLACED_TEST = FILLED_PATH / "test_ML_filled.csv"

MAKE_MODEL_PATH = DATA_PATH / "Make_model_dictionaries"
MAKE_DICT_PATH = MAKE_MODEL_PATH / "make_dict.pkl"
MAKE_MODEL_BIN_PATH = MAKE_MODEL_PATH / "make_model_bins.pkl"
MAKE_MODEL_DICT_MEAN_PATH = MAKE_MODEL_PATH / "make_dict_mean_norm.pkl"

SCRAPED_PATH = Path("scraped_data")
CAR_CODE_PATH = SCRAPED_PATH / "listing_carcode.csv"
FUEL_TYPE_PATH = SCRAPED_PATH / "listing_id_to_fuel_type.json"


COLS_TO_DROP = [
    "indicative_price",
    "eco_category",
]

CRITICAL_COLS = [
    "title",
    "model",
    "manufactured",
    "transmission",
    "curb_weight",
    "power",
    "engine_cap",
    "no_of_owners",
    "depreciation",
    "coe",
    "road_tax",
    "dereg_value",
    "mileage",
    "omv",
    "arf",
]

STR_COLS = [
    "title",
    "model",
    "description",
    "type_of_vehicle",
    "features",
    "accessories",
]

NUMBER_COLS = [
    "manufactured",
    "road_tax",
    "curb_weight",
    "power",
    "engine_cap",
    "no_of_owners",
    "depreciation",
    "coe",
    "dereg_value",
    "mileage",
    "omv",
    "arf",
]

NOMINAL_TO_REMOVE = [
    "listing_id",
    "title",
    "make",
    "model",
    "description",
    "registered_date",
    "features",
    "accessories",
    "opc_scheme",
]

INFO_COLS = ['title', 'accessories', 'features']

TO_SKIP = {
    "listing_id",
    "description",
    "original_reg_date",
    "reg_date",
    "lifespan",
    "features",
    "accessories",
    "indicative_price",
}

TRANSMISSION_MAP = {"auto": 0, "manual": 1}

VEHICLE_CATEGORIES = [
    {"sports car"},
    {"luxury sedan", "suv"},
    {"others", "mpv", "stationwagon", "mid-sized sedan"},
]

MAKE_MODEL_PRICE_MIN = 8700
MAKE_MODEL_PRICE_MAX = 1_813_887.5
MAKE_MODEL_BINS = [
    20_000,
    30_000,
    40_000,
    50_000,
    55_000,
    60_000,
    65_000,
    70_000,
    75_000,
    80_000,
    85_000,
    90_000,
    95_000,
    100_000,
    110_000,
    120_000,
    130_000,
    140_000,
    150_000,
    175_000,
    200_000,
    250_000,
    300_000,
    400_000,
    600_000,
    900_000,
    1_200_000,
    1_600_000
]

# Grid for RandomSearchCV with RandomForestRegressor
NUM_NA_TRAIN_ITER = 200
K_CROSS_FOLD_NA_TRAIN = 5
RF_REG_RAND_GRID = {
    'n_estimators': list(np.linspace(start=200, stop=2000, num=10, dtype=int)),
    'max_depth': list(np.linspace(start=10, stop=110, num=11, dtype=int)) + [None],
    'max_features': ['auto', 'sqrt'],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}
