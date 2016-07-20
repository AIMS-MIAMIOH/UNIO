import web

import sqlite3

import jsonpickle

urls = ('/trendinglist', 'Topic')

class Topic:
	def GET(self):
		connection = sqlite3.connect('trending.sqlite')

		cursor = connection.cursor()

		sql_query = "SELECT * FROM trendinglist"

		rows = cursor.execute(sql_query)	

		jsonobjectRows = []
		for row in rows:
			jsonobject = {
			  'Topic' : row[0],
			}
			jsonobjectRows.append(jsonobject)
		connection.close()
		return jsonpickle.encode(jsonobjectRows)
		
app = web.application(urls, globals())

if __name__ == '__main__':
  web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 7001))
  app.run()
