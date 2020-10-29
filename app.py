import os

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def YAM():
    fake_time = [999]
    status = "כשניסים אומר"
    if request.method == "GET":
        if len(request.args.getlist("weeks")) == 0:
            verdict = "..."
            holishit_result = "..."
        else:
            fake_time = request.args.getlist("weeks")
            fake_time = int(fake_time[0])
            time_left = fake_time * 4
            verdict = fake_time*7
            holishit_result = time_left
    return render_template("index.html",
                           status=status,
                           verdict=verdict,
                           holishit_result=holishit_result
                           )


if __name__ == "__main__":
    app.run(debug=False)
