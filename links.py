#!/usr/bin/env python

"""
Web Mining crawler and Descrepancy Detection Software.

Jabong.com

"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys
import nltk





stopwords_list = ['a','able','about','across','after','all','almost','also','am','among',
	             'an','and','any','are','as','at','be','because','been','but','by','can',
	             'cannot','could','dear','did','do','does','either','else','ever','every',
	             'for','from','get','got','had','has','have','he','her','hers','him','his',
	             'how','however','if','in','i','into','is','it','its','just','least','let',
	             'like','likely','may','me','might','most','must','my','neither','no','nor',
	           	 'not','of','off','often','on','only','or','other','our','own','rather','said',
	             'say','says','she','should','since','so','some','than','that','the','their',
	             'them','then','there','these','they','this','tis','to','too','twas','us',
	             'wants','was','we','were','what','when','where','which','while','who',
	             'whom','why','will','with','would','yet','you','your','style','stylish','beautiful','lovely']

color_list = ["purple","ivory","violet indigo","apricot","transparent","camel","lilac","emerald","cream","silver",
			"brick red","coffee","firozi","green","golden","assorted","rust","pink","turquoise","light grey","olive",
			"navy blue","off white","two tone","aqua blue","grey","peach","nude","sand","pearl","red","copper","champagne",
			"grey milange","bronze","ice blue","brown","mustard", "yellow","multi","maroon","neutral","aqua","camel shade",
			"fuchsia","beige","magenta","charcoal grey","khaki","lemon","ruby","black","lavender","light blue","blue","yellow",
			"antique silver","wine","cherry","white","khakhi","dark grey","antique","mauve","metal","tan","orange"]
count = 1

error=100

def get_articles(url):

	#try:

		html = urlopen(url).read()						# opens the url and fetch HTML
		soup = BeautifulSoup(html, "lxml")				# opens HTML to be parsed
		if  soup.find("span","fs18"):					# checks whether link is live or not
			file =open('skipped_links.csv','a+')
			file.write(url)
		else:	
			name = soup.find("span","fs11 c222").string.strip('\t\n ')
			brand_name = soup.find("span","brand-name fs22 full-width").string.strip('\t\n ')
			name_below_brand = soup.find("span", "mb3 full-width").string.strip('\t\n ')
			
			div_data = soup.find("div",{"class":"product-info c999 fs12 mb20"})
			for a in div_data.findAll("p"):



					description = a.text.strip(' ')

			row = div_data.findAll("tr")
			temp = len(row)
			
			print count
			print url

			print name
			print brand_name
			print name_below_brand
			print description

			name = name.split()
			brand_name = brand_name.split()
			name_below_brand = name_below_brand.split()
			description = description.split()

			

			# Removing stop words 

		#	remove_stopword(description)
			
			details={}

			# 	"DATA IN TABLE"
			
			for i in range(0,temp-2):
				
				cells=row[i].findAll("td", limit=2)
				details[cells[0].string.lower()] = cells[1].string.lower()
			
			print details.keys()

			if 'color' in details.keys():
				color = details['color']
				print color
				print 'lol'
			if 'material' in details.keys():
				material = details['material']
				print 'lol1'
				print material
				
			print "___________________________________________________________________________________________________________\n\n"

			if name == name_below_brand:
				error = error - 10
				print 'no error in name_below_brand'

			if color in color_list:
				if color in name:
					error = error - 10
					print 'error: no color in brand_name'

			else:
				print 'error: UNKNOWN COLOR - color not found in colors list'





	#	except:
			
		#	print "skipped link number:", count
			
		#	file =open('skipped_links.csv','a+')
		#	file.write(url)
		#	pass

def remove_stopword(data):
	
	data = data.encode('utf-8')
	data = data.split()
	desc = ""
	for word in data:
		if word.lower() not in stopwords:
				desc = desc + ' ' + word.lower()

	desc = nltk.word_tokenize(desc)

	#fdisc = nltk.FreqDist(desc)

	#fdisc.freq(colours)
	#print fdisc
	
	#print nltk.pos_tag(data)

	#tagged = nltk.pos_tag(data)
	#propernouns = [word for word,pos in tagged if pos == 'NN']
	#print propernouns



while(1):

	url = raw_input()

	get_articles(url)
	
	count=count+1





























__name__ == "__main__"
