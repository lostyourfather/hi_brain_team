from edu.edu_handler import *
import sys
import signal



def teardown_handler(signal, frame):
    print("App stoped")
    sys.exit(1)


app = application = falcon.API()
signal.signal(signal.SIGTERM, teardown_handler)
app.add_route('/hacaton_endpoint', EduHandler())