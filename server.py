from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def index(num=3, color="lightblue"):
    return render_template("index.html", num=num, color=color)

@app.route('/play/<int:num>')
def new_index(num, color="lightblue"):
    return render_template("index.html", num=num, color=color)

@app.route('/play/<int:num>/<color>')
def color_index(num, color):
    return render_template("index.html", num=num, color=color)


# @app.route('/<color>')
# def index(color, num=3):
#     return render_template("index.html", num=num, color = color)



if __name__=="__main__":
    app.run(debug=True)

