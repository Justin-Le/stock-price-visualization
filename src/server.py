import os
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(str(np.loadtxt('index.html')))

def make_app():
    root = os.path.dirname(__file__)

    return tornado.web.Application([
        (r"/(.*)", tornado.web.StaticFileHandler,
        {"path": root, "default_filename": "index.html"})
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
