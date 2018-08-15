from __future__ import print_function
from flask import Flask, request, jsonify, url_for,render_template
from flask_cors import CORS
import sklearn
import numpy as np
from sklearn.externals import joblib

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET','POST'])
def index():
	if request.method == 'POST':
		try:
			print(request.form['length'], request.form['width'])
			length 	= float(request.form["length"])
			width 	= float(request.form["width"])
		except:
			return "Error in parameters"

		clf = joblib.load('models/finalized_model2.pkl')
		ans = clf.predict(np.array([[length, width]]))
		ans = list(ans.astype(np.str))
		print("Prediction:{}".format(ans))
		return jsonify({'prediction': ans})
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run()
