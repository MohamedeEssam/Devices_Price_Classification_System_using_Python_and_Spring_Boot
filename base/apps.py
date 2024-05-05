from django.apps import AppConfig
import pickle
from DevicePriceClassification.settings import MODEL_DIR


def load_pickle(path):
    with open(path, 'rb') as handle:
        loaded_var = pickle.load(handle)
    return loaded_var


class ResbaseConfig(AppConfig):
    name = 'restbase'
    
    
    svm = load_pickle(MODEL_DIR)

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
