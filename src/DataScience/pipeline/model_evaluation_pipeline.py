from src.DataScience.entity.config_entity import (ModelEvaluationConfig)
from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.model_evaluation import ModelEvaluation
from src.DataScience import logger
from pathlib import Path
import dagshub
dagshub.init(repo_owner='abheshith7', repo_name='WineQuality-Prediction-Pipeline', mlflow=True)

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == "__main__":
    try:
        logger.info(f"Starting the {STAGE_NAME}...")
        model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
        model_evaluation_pipeline.initiate_model_evaluation()
        logger.info(f"Completed the {STAGE_NAME}...")
    except Exception as e:
        logger.exception(e)
        raise e