from flask import Flask, render_template, request

from searchQuery import search

app = Flask(__name__, template_folder='templates')


# with open('SearchBar/index.html', 'r') as f:
#     html_string = f.read()

#
# @app.route("/")
# def index():
#     return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def hello_world():
    # return "hello world"
    if request.method == 'POST':
        query = request.form['searchTerm']
        res = search(query)
        hits = res['hits']['hits']
        time = res['took']
        # aggs = res['aggregations']
        num_results = res['hits']['total']['value']

        return render_template('result.html', query=query, hits=hits, num_results=num_results, time=time)

    if request.method == 'GET':
        return render_template('result.html', init='True')


if __name__ == '__main__':
    app.debug = True
    app.run()
