import re
re.match()      #Returns first match
re.search()     #Returns 
re.findall()    #Returns a list containing all matches
re.sub()        #Replaces one or many matches w/ a string
re.split()      #Returns a list where string has been split at end of each match
#Creating RegExs
#Goes in single quotes
pattern = ['A-Za-z']  #Set of characters []
pattern = '.'         #Any character      .
pattern = '^x'        #Starts with        ^
pattern = 'x$'        #Ends with          $
pattern = 'x*'   #Zero or more occurences of previous character  *
pattern = 'x+'  #One or more occurences of previous character   +
pattern = '?'   #Zero or one occurences of previous character   ?
pattern = 'x{3}' #Exactly x occurences of previous character                      {}
pattern = 'a|b'       #Either or          |

import itertools
import collections
import math
import random
import string
import os
import sys
import subprocess
import argparse
import datetime
import unittest
import numpy
