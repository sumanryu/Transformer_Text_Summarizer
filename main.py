from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = " Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>>>Stage {STAGE_NAME} Started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>Stage {STAGE_NAME} Completed <<<<<<<<<\n\nx=======x")
except Exception as e:
    raise e 