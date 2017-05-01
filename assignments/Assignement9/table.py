#!/usr/bin/python
'''
import textwrap
import feedparser as fp

feed = fp.parse("http://thehothand.blogspot.com/feeds/posts/default?max-results=100")

f = file('table.txt','w')
f.write("Title\t\t\t\t\t\tClassification")
f.write("\n---------------------------------------------\n")
for i in feed.entries:
	s = i.title
	s = s.encode("utf8")
	f.write(str(textwrap.fill(s,25)))
	f.write ("\n\n")
'''
f=file('class.txt','w')
i=1
while i<101:
	f.write(str(i)+"\n")
	i=i+1
