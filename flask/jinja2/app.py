from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/success/<int:results>")
def results(results):
    return render_template('results.html', res=results)

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/submit", methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method == "POST":
        maths = float(request.form['maths'])
        data = float(request.form['data'])
        algo = float(request.form['algo'])
        total_score = (maths + data + algo ) / 3
    return redirect(url_for('results', results=total_score))


if __name__=="__main__":
    app.run(debug=True)