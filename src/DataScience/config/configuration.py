from src.DataScience.constants import *
from src.DataScience.utils.common import read_yaml, create_directories
from src.DataScience.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig)  

## Create the configuration manager class to manage the configuration files
class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_FILE_PATH, 
                       params_filepath = PARAMS_FILE_PATH, 
                       schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)


        create_directories([self.config.artifacts_root])

    ### Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """_summary_

        Returns:
            DataIngestionConfig: _description_
        """
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_URL,
            load_data_file= config.load_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    ### Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        """ Get the data validation configuration
        This method creates the directories for data validation and returns the configuration object.

        Returns:
            DataValidationConfig: _config object for data validation
        """
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        # Create directories for data validation
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = schema
        )
        
        return data_validation_config
    
    ### Data Transformation Configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Get the data transformation configuration

        Returns:
            DataTransformationConfig: _description_
        """
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
         
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )
        return data_transformation_config
    

    ### Model Trainer Configuration
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.Elasticnet
        schema = self.schema.TARGET_COLUMN

        # Create the directories for the artifacts
        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target = schema.name
        )
        return model_trainer_config