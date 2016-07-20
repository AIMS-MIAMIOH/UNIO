import web

import sqlite3

import jsonpickle

import json

import simplejson

urls = ('/singleuser/(.*)', 'getUser',
				'/getAllUsers', 'getAllUsers',
				'/solr/(.*)', 'getSolr')

class getUser:

	def get(self):      
												self.response.headers.add_header('Access-Control-Allow-Origin', '*')

												self.response.headers['Content-Type'] = 'application/json'
				# do something

	def post(self):     
												self.response.headers.add_header('Access-Control-Allow-Origin', '*')
												
												self.response.headers['Content-Type'] = 'application/json'
			# do something

	def options(self):      
												self.response.headers['Access-Control-Allow-Origin'] = '*'
												self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
												self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE'

	def GET(self,userName):
												userName = userName.split('?')[0]
												#userName.replace("%20"," ");
												print "search item-" + userName;


												connection = sqlite3.connect('DOSDATA.sqlite')

												sqlite3.connect("DOSDATA.sqlite", check_same_thread=False)

												cursor = connection.cursor()
												cursor.execute('SELECT * FROM {tn} WHERE {cn}={nameValue}'.\
																				format(tn='dosuser', cn='name', nameValue = "'" + str(userName) + "'"))
												rows = cursor.fetchone()

												#jsonobjectRows = []
												if rows:
														rows ={ 
															'name' : rows[0].encode('utf-8'),
															'Title' : rows[1].encode('utf-8'),
															'Email' : rows[2].encode('utf-8'),
															'Phone' : rows[3].encode('utf-8'),
															'Location' : rows[4].encode('utf-8'),
															'Topic' : rows[5].encode('utf-8'),
															'Image' : rows[6].encode('utf-8'),
														}
												
												jsonobjectRows = json.dumps(rows)
												
												#jsonobjectRows.append(rows)
												#def format(a):
													#return ("\"person\":{{}}").format(a)
												output = "display({})" .format(jsonobjectRows)
												connection.close()
												#return jsonpickle.encode(jsonobjectRows)
												return output

class getSolr:
	def GET(self, query):
		query = query.split('?')[0]

	def GET(self):
		from urllib2 import *
		import simplejson
		connection = urlopen('http://localhost:8983/solr/DOS5/query?'+query+'&wt=json')
		response = simplejson.load(connection)

		print response['response']['numFound'], "documents found."
 
		# Print the name of each document.
 
		for document in response['response']['docs']:
			print "  Author =", document['author']
		



class getAllUsers:
	def GET(self):
		connection = sqlite3.connect('DOSDATA.sqlite')

		sqlite3.connect("DOSDATA.sqlite", check_same_thread=False)

		cursor = connection.cursor()

		cursor.execute("SELECT * FROM dosuser")

		#rows = cursor.fetchone()

		jsonobjectRows = []
		for row in cursor.fetchall():
			jsonobject = {
				'name' : row[0],
				'Title' : row[1],
				'Email' : row[2],
				'Phone' : row[3],
				'Location' : row[4],
				'Topic' : row[5],
			}
			jsonobjectRows.append(jsonobject)
		connection.close()
		return jsonpickle.encode(jsonobjectRows)


app = web.application(urls, globals())
if __name__ == '__main__':
	web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 7724))
	app.run()
