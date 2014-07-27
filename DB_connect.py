#!/usr/bin/env python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.
Akif Khan akif500[at]gmail.com

"""
from pymongo import MongoClient
import sys


def mongo_insert(data):						#FUCNTION TO INSERT DATA TO MONGO DB
	
	try:

		client = MongoClient('localhost', 27017)
	except:
		print "Database Connection problem:"		
		sys.exit(1)

	db = client.Bloomberg			#database named bloomberg
		
	collection = db.articles		#collection named articles

	try:
		id = db.articles.insert(data)	#Inserting the data in the DB
	except:
		print "Could not make entry to Database"


__name__ == "__main__"
