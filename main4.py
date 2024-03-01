from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file


app = Flask("JobScrapper")

@app.route("/")
def home():
    # return "<h1>hey there!</h1><a href='/hello'>go to hello</a>"
    return render_template("home.html", name="nico")

db = {
}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # print(keyword)
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs = jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachmen=True)

app.run("0.0.0.0")