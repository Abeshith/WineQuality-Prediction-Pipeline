from src.DataScience import logger
from src.DataScience.entity.config_entity import (ModelTrainerConfig)
from sklearn.linear_model import ElasticNet
import os, joblib
import pandas as pd
from src.DataScience import logger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        # Load the training and testing data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Separate the features and target variable
        X_train = train_data.drop(columns=[self.config.target], axis=1)
        y_train = train_data[self.config.target]
        X_test = test_data.drop(columns=[self.config.target], axis=1)
        y_test = test_data[self.config.target]

        # Initialize the ElasticNet model
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)

        # Train the model
        model.fit(X_train, y_train)

        # Save the model
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))