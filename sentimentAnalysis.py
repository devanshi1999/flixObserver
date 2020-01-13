import sys
sys.path.insert(0, '/Users/devanshisingh/desktop/my-work/python/flixObserver/vs')
import vaderSentiment

analyze = vaderSentiment.SentimentIntensityAnalyzer()

def polarity(title,content,stars):
	vs1 = analyze.polarity_scores(content)
	vs2 = analyze.polarity_scores(title)
	if stars!=0:
		if stars>=7:
			if vs1['pos'] - vs1['neg'] > 0 or vs2['pos'] - vs2['neg'] > 0:
				return 1

		elif stars<=3:
			if vs1['pos'] - vs1['neg'] < 0 or vs2['pos'] - vs2['neg'] < 0:
				return -1		
		else:
			return 0
	else:
		if vs1['pos'] - vs1['neg'] > 0 or vs2['pos'] - vs2['neg'] > 0:
			return 1
		elif vs1['pos'] - vs1['neg'] < 0 or vs2['pos'] - vs2['neg'] < 0:
			return -1
		else:
			return 0