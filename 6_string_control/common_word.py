import re
from collections import defaultdict
from collections import Counter

#Q
#Print out the most common words
#except the forbidden ones.

#There is no case classification, 
# and punctuation (period, comma, etc.) is also ignored.

paragraph = "Bob hit a ball, the hit BALL flew far it was hit"
banned = ["hit"]

#출력값 ball
#####################################


# code 
words = [word for word in re.sub(r'[^\w]', ' ' , paragraph).lower().split( ) if word not in banned]


words = [word for word in re.sub(r'[^\w]', ' ' , paragraph).lower().split( ) if word not in banned]

counts =Counter(words) 

print(counts.most_common(1)[0][0]) // ball
