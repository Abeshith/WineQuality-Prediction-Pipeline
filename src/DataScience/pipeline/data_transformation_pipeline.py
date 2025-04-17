from src.DataScience.entity.config_entity import (DataTransformationConfig)  
from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.data_transformation import DataTransformation
from src.DataScience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as file:
                status = file.read().split(" ")[-1].strip()
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_split_data()
            else:
                raise Exception("Data Validation failed. Cannot proceed with Data Transformation.")
        except Exception as e:
            logger.exception(e)
            raise e
