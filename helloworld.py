import webapp2

class HelloWorldHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello, World!\n\n')

app = webapp2.WSGIApplication([('/', HelloWorldHandler)])
