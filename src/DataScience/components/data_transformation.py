from src.DataScience import logger
import pandas as pd
from src.DataScience.entity.config_entity import (DataTransformationConfig)
import os
import pandas as pd
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split_data(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Train and test data split completed.")
        logger.info(f"Train data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")
        
        print(train.shape)
        print(test.shape)
        

