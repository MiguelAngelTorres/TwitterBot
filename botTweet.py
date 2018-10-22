#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, linecache
from random import randint

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

title1fs=open('Titulo/1fs.txt','r')
title1fp=open('Titulo/1fp.txt','r')
title1ms=open('Titulo/1ms.txt','r')
title1mp=open('Titulo/1mp.txt','r')
title2fs=open('Titulo/2fs.txt','r')
title2fp=open('Titulo/2fp.txt','r')
title2ms=open('Titulo/2ms.txt','r')
title2mp=open('Titulo/2mp.txt','r')
title2n=open('Titulo/2n.txt','r')

desc1fs=open('Sujetos/SF.txt','r')
desc1fp=open('Sujetos/PF.txt','r')
desc1ms=open('Sujetos/SM.txt','r')
desc1mp=open('Sujetos/PM.txt','r')
desc2fs=open('Predicados/PdSF.txt','r')
desc2fp=open('Predicados/PdPF.txt','r')
desc2ms=open('Predicados/PdSM.txt','r')
desc2mp=open('Predicados/PdPM.txt','r')

t1fs=sum(1 for lines in title1fs)
t1fp=sum(1 for lines in title1fp)
t1ms=sum(1 for lines in title1ms)
t1mp=sum(1 for lines in title1mp)
t2fs=sum(1 for lines in title2fs)
t2fp=sum(1 for lines in title2fp)
t2ms=sum(1 for lines in title2ms)
t2mp=sum(1 for lines in title2mp)
t2n=sum(1 for lines in title2n)

t1=t1fs+t1ms+t1fp+t1mp

d1fs=sum(1 for lines in desc1fs)
d1fp=sum(1 for lines in desc1fp)
d1ms=sum(1 for lines in desc1ms)
d1mp=sum(1 for lines in desc1mp)
d2fs=sum(1 for lines in desc2fs)
d2fp=sum(1 for lines in desc2fp)
d2ms=sum(1 for lines in desc2ms)
d2mp=sum(1 for lines in desc2mp)

d1=d1fs+d1ms+d1fp+d1mp

title1fs.close()
title1fp.close()
title1ms.close()
title1mp.close()
title2fs.close()
title2fp.close()
title2ms.close()
title2mp.close()
title2n.close()

desc1fs.close()
desc1fp.close()
desc1ms.close()
desc1mp.close()
desc2fs.close()
desc2fp.close()
desc2ms.close()
desc2mp.close()

while True:
	aux=randint(0,t1-1)
	aux2=randint(0,d1-1)
	
	
	###  Choose title
	if aux < t1fs :
		titulo=linecache.getline('Titulo/1fs.txt', aux).rstrip('\n')
		aux1=randint(0,t2fs+t2n-1)
		if aux1 < t2fs :
			titulo+=' '+linecache.getline('Titulo/2fs.txt', aux1).rstrip('\n')
		else :
			titulo+=' '+linecache.getline('Titulo/2n.txt', aux1-t2fs).rstrip('\n')
	elif aux < t1fp+t1fs :
		titulo=linecache.getline('Titulo/1fp.txt', aux-t1fs).rstrip('\n')
		aux1=randint(0,t2fp+t2n-1)
		if aux1 < t2fp :
			titulo+=' '+linecache.getline('Titulo/2fp.txt', aux1).rstrip('\n')
		else :
			titulo+=' '+linecache.getline('Titulo/2n.txt', aux1-t2fp).rstrip('\n')		
	elif aux < t1fp+t1fs+t1ms :
		titulo=linecache.getline('Titulo/1ms.txt', aux-t1fs-t1fp).rstrip('\n')
		aux1=randint(0,t2ms+t2n-1)
		if aux1 < t2ms :
			titulo+=' '+linecache.getline('Titulo/2ms.txt', aux1).rstrip('\n')
		else :
			titulo+=' '+linecache.getline('Titulo/2n.txt', aux1-t2ms).rstrip('\n')		
	else:
		titulo=linecache.getline('Titulo/1mp.txt', aux-t1fs-t1fp-t1ms).rstrip('\n')
		aux1=randint(0,t2mp+t2n-1)
		if aux1 < t2mp :
			titulo+=' '+linecache.getline('Titulo/2mp.txt', aux1).rstrip('\n')
		else :
			titulo+=' '+linecache.getline('Titulo/2n.txt', aux1-t2mp).rstrip('\n')		
	
	
###  Choose description
	if aux2 < d1fs :
		descrip='Una '+linecache.getline('Sujetos/SF.txt', aux2).rstrip('\n')
		aux3=randint(0,d2fs-1)
		descrip+=' que '+linecache.getline('Predicados/PdSF.txt', aux3).rstrip('\n')
	elif aux2 < d1fp+d1fs :
		descrip='Unas '+linecache.getline('Sujetos/PF.txt', aux2-d1fs).rstrip('\n')	
		aux3=randint(0,d2fp-1)	
		descrip+=' que '+linecache.getline('Predicados/PdPF.txt', aux3).rstrip('\n')
	elif aux2 < d1fp+d1fs+d1ms :
		descrip='Un '+linecache.getline('Sujetos/SM.txt', aux2-d1fs-d1fp).rstrip('\n')	
		aux3=randint(0,d2ms-1)
		descrip+=' que '+linecache.getline('Predicados/PdSM.txt', aux3).rstrip('\n')
	else:
		descrip='Unos '+linecache.getline('Sujetos/PM.txt', aux2-d1fs-d1fp-d1ms).rstrip('\n')
		aux3=randint(0,d2mp-1)	
		descrip+=' que '+linecache.getline('Predicados/PdPM.txt', aux3).rstrip('\n')
	
	api.update_status(titulo+'\n\n'+descrip)
#	print(titulo+'\n\n'+descrip)
#	time.sleep(5)#Tweet every 15 seconds

