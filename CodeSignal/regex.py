import re

#Starts with capital letter, Ends in .?!, All letters in between can't be .?!
re.match('^[A-Z][^.?!]*[.?!]$', sentence) is not None

#Remove all numbers and replace w/ hashtag
re.sub('[0-9]',"#",inputString)