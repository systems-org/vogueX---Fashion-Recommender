import requests
import json
from flask_login import login_required, current_user
from flask import (
    Blueprint,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
    request,
)

class Shopping:
    def __init__(self):
        self.API_KEY="de711d79731e559c2229268ef91800bdce6db2a1fd6961e05284070cd673775a"
        self.url="https://cloudapi.lykdat.com/v1/global/search"
    
    def shopping_results(self,image_url):
        url = self.url
        payload = {
            "api_key": self.API_KEY ,
            "image_url": image_url,
        }
        response = requests.post(url, data = payload)
        json_response = response.json()
        res = json_response["data"]
        result_groups = res["result_groups"][0]
        similar_products = result_groups["similar_products"]
        results=[]
        for product in similar_products:
            if(product["currency"]== "USD"):
                results.append(product)
        return results


shoppingbp = Blueprint("shoppingbp", __name__, url_prefix="/")

@shoppingbp.route("/shopping-results", methods=["POST"])
# @login_required
def get_shopping_results():
    image_url=request.args.get('image_url')
    s=Shopping()
    result=s.shopping_results(image_url)
    return render_template("shopping.html",user=current_user, shopping_results=result,enumerate=enumerate)