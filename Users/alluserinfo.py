import web

import sqlite3

import jsonpickle


urls = ('/users', 'users')

class users:
	def GET(self):
		connection = sqlite3.connect('DOSDATA.sqlite')

		sqlite3.connect("DOSDATA.sqlite", check_same_thread=False)

		cursor = connection.cursor()

		sql_query = "SELECT * FROM dosuser"

		rows = cursor.execute(sql_query)

		jsonobjectRows = []
		for row in rows:
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
  web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 7744))
  app.run()
 