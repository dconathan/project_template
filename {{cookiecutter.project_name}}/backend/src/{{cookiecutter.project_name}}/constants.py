import os

PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.dirname(PACKAGE_DIR)
BACKEND_DIR = os.path.dirname(SRC_DIR)
PROJECT_HOME = os.path.dirname(BACKEND_DIR)

MODELS_DIR = os.path.join(BACKEND_DIR, "models")

DATA_DIR = os.path.join(BACKEND_DIR, "data")

