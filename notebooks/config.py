import os

PROJECT_FOLDER = '../'
DATA_FOLDER = os.path.join(PROJECT_FOLDER, "data")
MODEL_FOLDER = os.path.join(PROJECT_FOLDER, "models")
ARTIFACT_FOLDER = os.path.join(PROJECT_FOLDER, "artifacts")

exp_configs = {
    1: {"param1": 1, "param2": 3, "description":"exp1"},
    2: {"param1": 1, "param2": 3, "description":"exp2"},
    3: {"param1": 1, "param2": 3, "description":"exp3"},
}
