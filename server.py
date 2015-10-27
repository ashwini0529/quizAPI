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
import urllib
import urllib2
import random
#import jsonify
#custom modules
from Database.database import _execute
import mandrill

html_content = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>GDG VIT DevFest</title>
  <style type="text/css">
  body {margin: 0; padding: 0; min-width: 100%!important;}
  img {height: auto;}
  .content {width: 100%; max-width: 600px;}
  .header {padding: 40px 30px 20px 30px;}
  .innerpadding {padding: 30px 30px 30px 30px;}
  .borderbottom {border-bottom: 1px solid #f2eeed;}
  .subhead {font-size: 15px; color: #ffffff; font-family: sans-serif; letter-spacing: 10px;}
  .h1, .h2, .bodycopy {color: #153643; font-family: sans-serif;}
  .h1 {font-size: 33px; line-height: 38px; font-weight: bold;}
  .h2 {padding: 0 0 15px 0; font-size: 24px; line-height: 28px; font-weight: bold;}
  .bodycopy {font-size: 16px; line-height: 22px;}
  .button {text-align: center; font-size: 18px; font-family: sans-serif; font-weight: bold; padding: 0 30px 0 30px;}
  .button a {color: #ffffff; text-decoration: none;}
  .footer {padding: 20px 30px 15px 30px;}
  .footercopy {font-family: sans-serif; font-size: 14px; color: #ffffff;}
  .footercopy a {color: #ffffff; text-decoration: underline;}

  @media only screen and (max-width: 550px), screen and (max-device-width: 550px) {
  body[yahoo] .hide {display: none!important;}
  body[yahoo] .buttonwrapper {background-color: transparent!important;}
  body[yahoo] .button {padding: 0px!important;}
  body[yahoo] .button a {background-color: #e05443; padding: 15px 15px 13px!important;}
  body[yahoo] .unsubscribe {display: block; margin-top: 20px; padding: 10px 50px; background: #2f3942; border-radius: 5px; text-decoration: none!important; font-weight: bold;}
  }

  /*@media only screen and (min-device-width: 601px) {
    .content {width: 600px !important;}
    .col425 {width: 425px!important;}
    .col380 {width: 380px!important;}
    }*/

  </style>
</head>

<body yahoo bgcolor="#f6f8f1">
<table width="100%" bgcolor="#f6f8f1" border="0" cellpadding="0" cellspacing="0">
<tr>
  <td>
    <!--[if (gte mso 9)|(IE)]>
      <table width="600" align="center" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td>
    <![endif]-->     
    <table bgcolor="#ffffff" class="content" align="center" cellpadding="0" cellspacing="0" border="0">
      <tr>
        <td bgcolor="#c7d8a7" class="header">
          <table width="65" align="left" border="0" cellpadding="0" cellspacing="0">  
            <tr>
              <td height="40" >
                <img class="fix" src="http://www.gdgvitvellore.com/devfest/img/logo.png" width="190" height="62" border="0" alt="" />
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
            <table width="425" align="left" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td>
          <![endif]-->
          <table class="col425" align="left" border="0" cellpadding="0" cellspacing="0" style=" max-width: 425px;">  
            <tr>
              <td height="70">
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td class="subhead" style="padding: 0 0 0 3px;">
                      
                    </td>
                  </tr>
                  <tr>
                    <td class="h1" style="padding: 5px 0 0 0;">
                    
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
                </td>
              </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <tr>
        <td class="innerpadding borderbottom">
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td class="h2">
               INNNOVATE, MAKE THINGS HAPPEN!
              </td>
            </tr>
            <tr>
              <td class="bodycopy">
                Introducing to you the first of its kind at VIT University The Dev Fest, brought to you by the GDG VIT. Sessions on Android, Cloud and Entrepreneurship are the events on order.
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td class="innerpadding borderbottom">
          
          <!--[if (gte mso 9)|(IE)]>
            <table width="380" align="left" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td>
          <![endif]-->
          <table class="col380" align="left" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 380px;">  
            <tr>
              <td>
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td class="bodycopy">
                      Thank You for registering! See You at the Event.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding: 20px 0 0 0;">
                      <table class="buttonwrapper" bgcolor="#e05443" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td class="button" height="45">
                            <a href="http://gdgvitvellore.com/devfest">More Details about the event</a>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
                </td>
              </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <tr>
        <td >
          <img class="fix" src="http://www.gdgvitvellore.com/devfest/img/hero.png" width="100%" border="0" alt="" />
        </td>
      </tr>
      
      <tr>
        <td class="footer" bgcolor="#44525f">
          <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td align="center" class="footercopy">
                &reg; GDG-VIT Vellore, 2015<br/>

              </td>
            </tr>
            <tr>
              <td align="center" style="padding: 20px 0 0 0;">
                <table border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td width="37" style="text-align: center; padding: 0 10px 0 10px;">
                      <a href="http://www.facebook.com/gdgvitvellore">
                        <img src="http://www.gdgvitvellore.com/devfest/img/facebook.png" width="37" height="37" alt="Facebook" border="0" />
                      </a>
                    </td>
                    
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    <!--[if (gte mso 9)|(IE)]>
          </td>
        </tr>
    </table>
    <![endif]-->
    </td>
  </tr>
</table>
</body>
</html>
'''

#QUIZ KEY!!!!
quiz_key = 'cac55dbeb283241bb28547dff9713582abf17aa9e20f7f5d7b17905a'


#Introduction content..

introContent = """
<html>
<body>
<h3> Hey... Welcome to the GDG Devfest Quiz.. You will have 2 minutes to attempt the quiz. No negetive marking.. Just answer as many questions as you can..</h3><br>
<h4> HAPPY QUIZZING</h4>
<form action = "/quiz">
<input type="hidden" value="%s" name="key">
<input type = "submit" value = "Take Quiz">
</form>
</body>
</html>
""" % (quiz_key)

#Handlers :-
class MainHandler(RequestHandler):
	def get(self):
		self.write(introContent)
#trial handler for learning..

class LoginHandler(RequestHandler):
	def post(self):
		regno = self.get_argument('regno','')
		list_regno = _execute("""select * from Login where regno = "{0}" """.format(regno))
		if(len(list_regno)==0):
			self.write('Failure')
		else:
			self.write('Success')



class trialHandler(RequestHandler):
	def get(self):
		number = self.get_argument('number','8098819952')
		to_mail = self.get_argument('mail','shubhodeep9@gmail.com')
		to_name = self.get_argument('name','shubhodeep')
		authkey = "70362AszEUjXo15501cea8"
		message = "Thank you, %s, for your interest. Please check your email for further details." % (to_name)
		sender = "GDGVIT"
		route = "template" 
		values = {
		          'authkey' : authkey,
		          'mobiles' : number,
		          'message' : message,
		          'sender' : sender,
		          'route' : route
		          }
		url = "http://api.msg91.com/sendhttp.php" 
		postdata = urllib.urlencode(values) 
		req = urllib2.Request(url, postdata)
		response = urllib2.urlopen(req)
		output = response.read()
		mandrill_client = mandrill.Mandrill('7YM3ofQU9CGK2AhrzGDMrA')
		message = {
	     'auto_html': None,
	     'auto_text': None,
	     'from_email': 'gdgvitvellore@gmail.com',
	     'from_name': 'GDG-VIT',
	     'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
	     'headers': {'Reply-To': 'gdgvitvellore@gmail.com'},
	     'html': html_content,
	     'important': False,
	     'inline_css': None,
	     'merge': True,
	     'merge_language': 'mailchimp',
	     'merge_vars': [{'rcpt': to_mail,
	                     'vars': [{'content': 'merge2 content', 'name': 'merge2'}]}],
	     'metadata': {'website': 'www.gdgvitvellore.com'},
	     'preserve_recipients': None,
	     'return_path_domain': None,
	     'signing_domain': None,
	     'subject': 'GDG-VIT DevFest',
	     'tags': ['password-resets'],
	     'to': [{'email': to_mail,
	             'name': to_name,
	             'type': 'to'}],
	     'track_clicks': None,
	     'track_opens': None,
	     'tracking_domain': None,
	     'url_strip_qs': None,
	     'view_content_link': None}
		result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
		self.redirect('http://devfest.gdgvitvellore.com')

# Quiz Handler to generate a randomized quiz from database and serve it as a JSON for Android Application.

class QuizHandler(RequestHandler):
	#@asynchronous
	#@engine
	def post(self):
		client = AsyncHTTPClient()
		quizKey = self.get_argument('key', '') #Quiz Key to secure our Quiz API	
		if(quizKey==quiz_key):
			dbResult =_execute('select * from questions')
			dbList = []
			for i in dbResult:
				dbList.append(dict(id=i[0],question=i[1],option1=i[2],option2=i[3],option3=i[4],option4=i[5],correctAnswer=i[6]))
			random.shuffle(dbList)
			self.write(dict(dbResult=dbList))
		else:
			self.write(keyError)

class SubmitHandler(RequestHandler):
	def post(self):
		regno = self.get_argument('regno','')
		score = int(self.get_argument('score',''))
		lis = _execute(""" select * from scores where regno = "{0}" """.format(regno))
		if(len(lis)>0):
			score_old = lis[0][1]
			if(score>score_old):
				_execute(""" update scores set scores = "{0}" where regno = "{1}" """.format(score,regno))
			else:
				score = score_old
		else:
			_execute("""insert into scores (regno,scores) values ("{0}","{1}") """.format(regno,score))
		rank_ord = _execute('select * from scores order by scores desc')
		self.write(str(rank_ord.index((regno,score))+1))

class leaderHandler(RequestHandler):
	def post(self):
		result = _execute('select * from scores order by scores desc')
		out = []
		rank = 1
		for i in result:
			out.append(dict(rank=rank,regno=i[0],scores=i[1]))
			rank = rank+1
		self.write(dict(leader=out))

#Application initialization
application = Application([
	(r"/", MainHandler),
	(r"/quiz", QuizHandler),
	(r"/gdgmsg", trialHandler),
	(r"/login", LoginHandler),
	(r"/submit" , SubmitHandler),
	(r"/leader", leaderHandler)
], debug = True)

#main init
if __name__ == "__main__":
	port = int(os.environ.get('PORT',80))
	http_server = HTTPServer(application)
	http_server.listen(port)
	#print 'Listening to port http://127.0.0.1:%d' % port
	IOLoop.current().start()
