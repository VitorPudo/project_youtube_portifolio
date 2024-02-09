from data.api import APICollector
from contracts.schema import YoutubeSchema
from aws.client import S3Client

schema = YoutubeSchema
aws = S3Client()



minha_classe = APICollector(schema, aws).start()

print(minha_classe)