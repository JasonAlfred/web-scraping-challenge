import pymongo

def import_mars_data(mars_dict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mars_db = myclient["mars_db"]
    mars_collection = mars_db["mars_collection"]
    x = mars_collection.insert_one(mars_dict)
    return 'Success!'


def retrieve_mars_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    query_results = myclient['mars_db']['mars_collection'].find()

    for x in query_results:
        article_title= x['article_title']
        article_paragraph = x['article_paragraph']
        mars_data_table = x['mars_data_table']
        mars_image = x['mars_image']
        hemisphere_image_urls = x['hemisphere_image_urls'] 
    return (article_title, article_paragraph, mars_data_table, mars_image, hemisphere_image_urls)  