import flask
from flask import *
app = flask.Flask(__name__)
import pickle
model = pickle.load(open('marriage.pkl','rb'))

# main index page route
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    predicted_age_of_marriage = model.predict([[int(request.form['gender']),
                            int(request.form['religion']),
                            int(request.form['caste']),
                            int(request.form['mother_tongue']),
                            int(request.form['country']),
                            float(request.form['height_cms'])
                           ]])
    out=round(predicted_age_of_marriage[0],2)
    return  render_template('index.html',result="You will get married at = {}".format((out)))


if __name__ == "__main__":
    app.run(debug=True)
