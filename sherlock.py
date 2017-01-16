import os
from pymongo import MongoClient
import logging
from logging.config import dictConfig
import env_config
import json
from watson_developer_cloud import AlchemyDataNewsV1

dictConfig(env_config.logging_config)
logger = logging.getLogger()

def main():
	try:
		alchemy_api=os.getenv("ALCHEMY_NEWS_API")
		alchemy_url=os.getenv("ALCHEMY_NEWS_URL")
	except:
		logger.error('Could not find AlchemyNews env variables')
	alchemy_data_news = AlchemyDataNewsV1(api_key=alchemy_api)
	results = alchemy_data_news.get_news_documents(start='now-7d', end='now', time_slice='12h')
	print(json.dumps(results, indent=2))


	results = alchemy_data_news.get_news_documents(
	    start='now-2d',
	    end='now',
	    return_fields=['enriched.url.title',
	                   'enriched.url.url',
	                   'enriched.url.author',
	                   'enriched.url.publicationDate'],
	    query_fields={
	        'q.enriched.url.enrichedTitle.entities.entity':
	            '|text=Tesla,type=company|'})
	print(json.dumps(results, indent=2))


if __name__ =="__main__":
	main()