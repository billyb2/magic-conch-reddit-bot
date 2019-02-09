import re
import praw
import random
import time

from random import randint

reddit = praw.Reddit(client_id='8vlJDtcIMx4quA',
                     client_secret='CJ8fSzb_s74GNODu2CQQ68WqsaI',
                     user_agent='heroku:python:v0.1 (by /u/WhatsALigma)',
                     username='hailthemagicconchbot',
                     password='1k2R1OWBmcXme6rV2PLmMR6eyGUtpFxF0pH')

previous_id="0"

def commentedAlready(commentid):
		if commentid in previous_id:
			return True
		else:
			return False

	
def search():
	for results in reddit.subreddit('bikinibottomtwitter').comments():	#Grab all the Recent Comments in every subreddit. This will return 100 of the newest comments on Reddit
		global previous_id	#Import the global variable
		
		body = results.body  #Grab the Comment
		body=body.lower()	#Convert the comment to lowercase so we can search it no matter how it was written
		comment_id = results.id  #Get the Comment ID
		
		if commentedAlready(comment_id) == False:  #Check if we already replied to this comment
			previous_id+=comment_id
		elif commentedAlready(comment_id) == True:
			return
 
		
		found=body.find('!conch')
			
		if found != -1: 		#Looks like the comment includes . sad.
			previous_id = comment_id  #Add to our global variable
			
			try:
				randNum=randint(0, 6)
				print("Found a comment!")
				if randNum == 0:
					results.reply('Maybe someday')
				elif randNum == 1:
					results.reply('Nothing')
				elif randNum == 2:
					results.reply('Neither')
				elif randNum == 3:
					results.reply('I don\'t think so')
				elif randNum == 4:
					results.reply('No')
				elif randNum == 5:
					results.reply('Yes')
				elif randNum == 6:
					results.reply('Try asking again')
			except:
				break	#Leave the function if error occurs with replying

while 1:
	search()
	print("Loop complete")
	time.sleep(5)
