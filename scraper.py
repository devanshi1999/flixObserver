#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import sentimentAnalysis
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def scrape(url):

	fpos=open("positive.txt", "w+")
	fneu=open("neutral.txt", "w+")
	fneg=open("negative.txt", "w+")

	driver = webdriver.PhantomJS(executable_path='/Users/devanshisingh/phantomjs-2.1.1-macosx/bin/phantomjs')
	driver.get(url)
	html = driver.page_source.encode('utf-8')
	pn=0

	response = requests.get(url)

	data = response.text

	soup = BeautifulSoup(data,'html.parser')

	header = soup.find('div',{'class': 'header'})
	div = header.find('div')
	span = div.find('span').text.split()


	if span[0]!='0':
		button = soup.find('button',{'class':'ipl-load-more__button'})
		if button:
			while driver.find_element_by_css_selector('.ipl-load-more__button').value_of_css_property('display')!='none':
				driver.find_element_by_css_selector('.ipl-load-more__button').click()
				time.sleep(2)

		html = driver.page_source.encode('utf-8')
		soup = BeautifulSoup(html, 'lxml')

		reviews = soup.find_all('div',{'class': 'lister-item-content'})

		pos=0
		neg=0
		neu=0
		total = len(reviews)


		for review in reviews:
			rating = review.find('span',{'class': 'rating-other-user-rating'})
			if rating:
				stars = int(rating.find('span').text)
			else:
				stars = 0

			title = review.find('a',{'class':'title'}).text
			contentclass = review.find('div',{'class':'content'})
			content = contentclass.find('div',{'class': ['text show-more__control clickable','text show-more__control']}).text

			opinion = sentimentAnalysis.polarity(title,content,stars)
			if opinion==1:
				if stars==0:
					stars=10
				fpos.write(str(stars)+'⭐️ '+title)
				pos+=1
			elif opinion==0:
				fneu.write(str(stars)+'⭐️ '+title)
				neu+=1
			else:
				fneg.write(str(stars)+'⭐️ '+title)
				neg+=1 

		fpos.close()
		fneg.close()
		fneu.close()

		return [pos,neu,neg,total]
	else:
		return [0,0,0,0]

	