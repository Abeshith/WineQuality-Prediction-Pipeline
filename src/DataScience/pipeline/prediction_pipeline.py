import joblib
import pandas as pd
import os
import numpy as np
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        # Make predictions
        predictions = self.model.predict(data)
        
        return predictions