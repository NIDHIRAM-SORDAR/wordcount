from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.

def home_view(request, *args, **kwargs):
	template_name = 'home.html'
	context = {}
	return render(request, template_name, context)

def count_view(request, *args, **kwargs):
	fulltext = request.GET["fulltext"]

	#remove special character from Text
	clean_splited_text = list()
	for line in fulltext.split("\n"):
		clean_splited_text.append(re.sub(r"[^a-zA-Z0-9]+", ' ', line))

	fulltext_cleaned = "".join(clean_splited_text)

	wordlist = fulltext_cleaned.split()
	count = len(wordlist)
	worddict = dict()
	for word in wordlist:
		if word in worddict:
			worddict[word] += 1
		else:
			worddict[word] = 1

	frequent_word = dict()
	for key , value in worddict.items():
		if value >= 3:
			frequent_word[key] = value

	template_name = 'count.html'
	context = {'user_text': fulltext, 'count': count, 'frequent_word': frequent_word }
	return render(request, template_name, context)


def about_view(request, *args, **kwargs):
	template_name = 'about.html'
	context = {}
	return render(request, template_name, context)

