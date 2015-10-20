#Tornado Libraries
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task

#Other Libraries
import sqlite3
import json
import requests
import os
import urllib2
#import jsonify
#custom modules
from Database.database import _execute

#QUIZ KEY!!!!
quiz_key = 'cac55dbeb283241bb28547dff9713582abf17aa9e20f7f5d7b17905a'


#Introduction content..

introContent = """
<html>
<body>
<h3> Hey... Welcome to the GDG Devfest Quiz.. You will have 2 minutes to attempt the quiz. No negetive marking.. Just answer as many questions as you can..</h3><br>
<h4> HAPPY QUIZZING</h4>
<form action = "/quiz?key="""+quiz_key+"""">
<input type = "submit" value = "Take Quiz">
</form>
</body>
</html>
"""

#Handlers :-
class MainHandler(RequestHandler):
	def get(self):
		self.write(introContent)
#trial handler for learning..

class trialHandler(RequestHandler):
	def get(self):
		name = self.get_argument('name','')
		self.write('Name : '+name)

# Quiz Handler to generate a randomized quiz from database and serve it as a JSON for Android Application.

class QuizHandler(RequestHandler):
	@asynchronous
	@engine
	def get(self):
		quizKey = self.get_argument('key', '') #Quiz Key to secure our Quiz API	
		if(quizKey==quiz_key):
			dbResult = _execute('select * from questions')
			dbList = []
			for i in dbResult:
				dbList.append(dict(id=i[0],question=i[1],option1=i[2],option2=i[3],option3=i[4],option4=i[5],correctAnswer=i[6]))
			self.write(json.dumps(dict(dbResult=dbList),indent = 4))
		else:
			self.write("Key not matched..")

#Application initialization
application = Application([
	(r"/", MainHandler),
	(r"/quiz", QuizHandler)
], debug = True)

#main init
if __name__ == "__main__":
	port = int(os.environ.get('PORT',5001))
	http_server = HTTPServer(application)
	http_server.listen(port)
	#print 'Listening to port http://127.0.0.1:%d' % port
	IOLoop.current().start()