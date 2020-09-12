from flask import current_app as app
from flask import render_template
from flask import Flask, redirect
from scrape_mars import mars_dict
from mongo_query import import_mars_data, retrieve_mars_data

#Setup Flask Local Server
app = Flask(__name__)

@app.route('/')
def home():
    """Landing page with scraping action"""
    query_call = mars_dict()
    import_query = import_mars_data(query_call)

    results = retrieve_mars_data()
    return render_template('home.html',
                           title="Mission to Mars",
                           description="U of M Homework",
                           article_title = results[0],
                           article_paragraph = results[1],
                           mars_data_table = results[2],
                           mars_image = results[3],
                           hemisphere_title1 = results[4][0]['title'],
                           hemisphere_url1 = results[4][0]['img_url'],
                           hemisphere_title2 = results[4][1]['title'],
                           hemisphere_url2 = results[4][1]['img_url'],
                           hemisphere_title3 = results[4][2]['title'],
                           hemisphere_url3 = results[4][2]['img_url'],
                           hemisphere_title4 = results[4][3]['title'],
                           hemisphere_url4 = results[4][3]['img_url']
                           )

@app.route('/scrape')
def scrape():
    """URL just to rescrape the data."""
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)