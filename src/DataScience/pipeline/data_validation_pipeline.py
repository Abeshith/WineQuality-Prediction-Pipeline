from src.DataScience.entity.config_entity import (DataValidationConfig)  
from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.data_validation import DataValidation
from src.DataScience import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass 

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f"Starting the {STAGE_NAME}...")
        data_validation_pipeline = DataValidationTrainingPipeline()
        data_validation_pipeline.initiate_data_validation()
        logger.info(f"Completed the {STAGE_NAME}...")
    except Exception as e:
        logger.exception(e)
        raise e