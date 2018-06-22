import os

from flask import Flask
import redis
import pickle
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

with open('indexing','rb') as f:
    index=pickle.load(f)


app = Flask(__name__)
db = redis.StrictRedis(host='localhost', port=6379, db=0,decode_responses=True)


@app.route('/')
def main_page():

    return render_template('main_page.html')

@app.route('/result',methods=['GET'])
def result():
	tags = request.args['search_tags']
	i = search(tags)
	ans = query(i)
	return render_template('result.html',values = ans)

def search(tags):
	words = tags.split(' ')
	index_pool = dict(index)
	new_pool = {}
	query_index =[]
	for word in words:
		for qs in index_pool:
			if word in qs:
				new_pool[qs] = index_pool[qs]
		index_pool = dict(new_pool) 
		new_pool = {}
	return index_pool

def query(i):
	answers = {}
	for k,v in i.items():
		r = db.get(v)
		if r:
			answers[k] = r 
	return answers

if __name__ == '__main__':
    app.run()
