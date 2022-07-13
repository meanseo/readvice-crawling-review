import re

def remove_html(sentence) :
	sentence = re.sub('(<([^>]+)>)|/n|/t|&nbsp;', '', sentence)
    return sentence