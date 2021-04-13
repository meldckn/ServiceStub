"""
Starter code for a basic Python microservice that can respond to HTTP 
requests
"""

import os
import falcon
#from falcon_cors import CORS

# For starting a local server for debugging 
from wsgiref import simple_server

hostName = "localhost"
serverPort = 8000
sampleFile = "level_0501.txt"

def load_txt(filename):
    # Utility function for loading a txt file
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()

class Welcome:
    def __init__(self):
        return

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.text = "<h>Hello world, I'm responding to your GET request</h>"

class Generate:
    def __init__(self):
        return

    def on_post(self, req, resp):
        """ Return a level file [stub for generating a level file]
        """
        txt_str = load_txt(sampleFile)
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = txt_str


# Create WSGI application
# Later, will probably need CORS settings to allow cross-origin requests
app = falcon.App()

# Route URI paths to different handler resources
app.add_route('/', Welcome())
app.add_route('/generate', Generate())

if __name__ == '__main__':
    """ When run as a standalone script rather than as an imported 
        module, start a simple local server for the app. Visit 
        {hostName}:{serverPort}/{route} in your browser or as the 
        request URL in Postman to test responses to different requests.
        Could alternatively use Gunicorn.
    """
    print(f"Serving HTTP on {hostName}:{serverPort}...")
    httpd = simple_server.make_server(hostName, serverPort, app)

    # Respond to requests until process is killed
    httpd.serve_forever()
