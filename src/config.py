import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATHS = {
    "cigarettes": os.path.join(BASE_DIR, "models", "cigarettes", "cigarettes.pt"),
    "fire": os.path.join(BASE_DIR, "models", "fire", "fire.pt"),
    "flames": os.path.join(BASE_DIR, "models", "flames", "flames.pt"),
    "smoke": os.path.join(BASE_DIR, "models", "smoke", "smoke.pt"),
}

CONF_THRESHOLDS = {
    "cigarettes": 0.5,
    "fire": 0.5,
    "flames": 0.5,
    "smoke": 0.3
}

PRIMARY_MODEL = "smoke"
SECONDARY_MODELS = ["fire", "flames"]
ALWAYS_ON_MODELS = ["cigarettes"]

ALERT_CLASSES = ["fire", "flames"]