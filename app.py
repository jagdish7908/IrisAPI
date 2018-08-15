from __future__ import print_function
from flask import Flask, request, jsonify
from flask_cors import CORS
import sklearn
import numpy as np
import os
from sklearn.externals import joblib

app = Flask(__name__)
CORS(app)

@app.route('/home', methods = ['POST'])
def index():
	try:
		print(request.form['length'], request.form['width'])
		length 	= float(request.form["length"])
		width 	= float(request.form["width"])
	except:
		return "Error in parameters"
	ans = clf.predict(np.array([[length, width]]))
	ans = list(ans.astype(np.str))
	print("Prediction:{}".format(ans))
	return jsonify({'prediction': ans})
	# return "Hello from the other side"

if __name__ == '__main__':
	clf = joblib.load('models/finalized_model2.pkl')
	port = int(os.environ.get('PORT', 3000))
	app.run(host='0.0.0.0', port=port, debug=True)
	#sudo lsof -i:port
