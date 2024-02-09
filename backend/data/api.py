import requests
import pandas as pd
from contracts.schema import GenericSchema
from typing import Union, Dict, List
from io import BytesIO
import pyarrow.parquet as pq
import datetime
from aws.client import S3Client


class APICollector:
    def __init__(self, schema, aws):
        self._schema = schema
        self._buffer = None
        self._aws =  aws
        return

    def start(self):
        response = self.getData()
        response = self.extractData(response)
        response = self.transformDf(response)
        response = self.convertToParquet(response)

        if self._buffer is not None:
            file_name = self.filename()
            print(file_name)
            self._aws.upload_file(response, file_name)
            return True


        return False
    
    def getData(self):
        response = requests.get('http://127.0.0.1:8000/get_data').json()
        return response
        
    def extractData(self, response):
        result: List[GenericSchema] = []
        for video_data in response:
            extracted_item = {}
            for key, value_type in self._schema.items():
                item_value = None
                for sub_dict in video_data.values():
                    if key in sub_dict and isinstance(sub_dict[key], value_type):
                        item_value = sub_dict[key]
                        break
                extracted_item[key] = item_value
            result.append(extracted_item)
        return result

    def transformDf(self, response):
        result = pd.DataFrame(response)
        result.to_csv("popular_videos.csv", index=False)

        return result
    
    def convertToParquet(self, response):
        self._buffer = BytesIO()
        try:
            response.to_parquet(self._buffer)
            return self._buffer
        except:
            print("Erro ao transformar em parquet {e}")
            self._buffer = None
            
    def filename(self):
        data_atual = datetime.datetime.now().isoformat()
        match  = data_atual.split(".")
        return f"api/api-response-youtube{match[0]}.parquet"
