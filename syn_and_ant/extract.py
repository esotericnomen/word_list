#!/usr/bin/env python
import urllib2					
import re
from BeautifulSoup import BeautifulSoup		

rstring = "Abandon. Desert, leave, for- \
sake, depart from, quit, give \
up, relinquish, discontinue, ab- \
dicate, renounce, repudiate, for- \
swear, withdraw from, vacate, \
surrender, retract, recant, re- \
tire from, cast off, abjure, cede, \
cease, resign, forego, yield, \
waive, part with, let go, lay \
down, evacuate, drop, deliver \
up. \
\
ANT. Claim, cherish, defend, \
keep, hold, maintain, protect, \
adopt, uphold, advocate, vindi- \
cate, occupy, undertake, prose- \
cute, pursue, follow, seek, \
guard, favor, retain, support, \
assert, haunt. \
Abandon. Desert, leave, for- \
sake, depart from, quit, give \
up, relinquish, discontinue, ab- \
dicate, renounce, repudiate, for- \
swear, withdraw from, vacate, \
surrender, retract, recant, re- \
tire from, cast off, abjure, cede, \
cease, resign, forego, yield, \
waive, part with, let go, lay \
down, evacuate, drop, deliver \
up. \
\
ANT. Claim, cherish, defend, \
keep, hold, maintain, protect, \
adopt, uphold, advocate, vindi- \
cate, occupy, undertake, prose- \
cute, pursue, follow, seek, \
guard, favor, retain, support, \
assert, haunt."

#print rstring
#start = re.search("ANT.(.+?)",rstring)
#print start.group(1)

start = rstring.find('ANT.')
end = rstring.find('.')
print rstring[start:]


#for url in url_list:\
	#start=url.find('?f=') + 3\
	#file_name = url[start:]+".txt"\
	#fd = open(file_name,"w")\
	#lis =[]\
	#try:\
		#response = urllib2.urlopen(url)\
		#html = response.read()\
		#soup = BeautifulSoup(html)\
		#rlist = soup.findAll(attrs={"class" : "wrapco"})\
		#for ul in rlist:\
			#for li in ul.findAll('li'):\
				#if li.find('ul'):\
					#break\
				#lis.append(li)\
	#except:\
		#print "error in opening "+url\
	#for word in lis:\
		#fd.write("%s\n" % (word.text.encode("utf-8")))\
