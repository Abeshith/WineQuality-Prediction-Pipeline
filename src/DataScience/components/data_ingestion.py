## update component to use the new config

from urllib.request import urlretrieve
import urllib.request as request
from src.DataScience import logger
import zipfile, os
from src.DataScience.entity.config_entity import (DataIngestionConfig)  

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.load_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename = self.config.load_data_file
                )
            logger.info(f"File {filename} downloaded with headers: {headers}")
        else:
            logger.info(f"File {self.config.load_data_file} already exists. Skipping download.")

    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.load_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path) 

    