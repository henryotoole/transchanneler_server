import os

# Load the proper config file.
dir_path = os.path.dirname(os.path.realpath(__file__))
cnf_path = dir_path + "/instance/master.cfg"
os.environ['FLASK_CONFIG_TRC'] = cnf_path

print(cnf_path)

import provod
from provod import app

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555)
