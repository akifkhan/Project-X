#!/usr/bin/env python
"""
A simple crawler for Bloomberg.com that crawls and stores all news articles in Mongo DB.
Akif Khan akif500[at]gmail.com
"""

import links
import DB_connect
from datetime import date, timedelta
from json import JSONDecoder



Days=1

while(Days < 2920):								# 365*8 = 2920 as the website got news only till 2006

	url="http://www.bloomberg.com/archive/news/"										
	d=date.today()-timedelta(days=Days)			# We start extracting data from a date before today due to time zone 
	d=d.strftime('%Y-%m-%d')
	url=url+d+"/"
	list_links = links.get_links(url)			# It gets Articles published on any single day
	
	total_links = len(list_links)				# Total Articles published on a single day
	print "Total articles for date: " 
	print d, " are: ", total_links

	
	#Fetches the Article Details by parsing each article page and then return the Data in JSON Format to be stored in DB 
	
	for index in range(0,total_links):	
		print list_links[index]
		data = links.get_articles(list_links[index])
		data = JSONDecoder().decode(data)
		
		db=DB_connect.mongo_insert(data) # Data inserted in DB

	# After fetching all articles of a particular day the day is increased by one so the date shifts  to a previous day.
	Days = Days+1