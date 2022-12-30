import json
import requests
import re
import time


def get_json_from_http_post(url: str, post_params: json, headers: dict = None) -> json:
    """
    Requests an API via HTTP post and returns the answer as json object
    :param url: url of the api that should be requested
    :param post_params: params dict to use with e.g. REST APIs
        e.g. {'request': 'search="LED"', 'page': 0, 'size': 100}
    :param headers: dict with additional http headers e.g. auth tokens
    :return: HTTP response parsed into a json object
    """

    # perform a http post, add headers if specified
    if headers is None:
        response = requests.post(url, post_params)
    else:
        response = requests.post(url, post_params, headers=headers)

    # raise Exceptions if any
    response.raise_for_status()

    # return string response as json
    return json.loads(response.text)


def read_file_to_json(filename: str) -> json:
    """
    Reads a json object from a file containing it
    :param filename: relative or full path to the file that contains the json object
    :return: returns the file content as json object
    """

    file = open(filename, mode='r')
    json_object = json.load(file)
    file.close()
    return json_object


def feed_api(url: str, products: json, headers: dict):
    """
    Send list of json objects to api. If an error occurs wait and retry.
    After 5 retries throw exception.
    :param url: url of the api
    :param products: list of json objects
    :param headers: headers to use with api
    """
    
    retries = 5
    wait = 10

    for i in range(retries + 1):
        try:
            get_json_from_http_post(url, json.dumps(products), headers)
            break
        except requests.HTTPError as e:
            if i < retries:
                print(f"Retry in {wait} seconds")
                time.sleep(wait)
            else:
                print("Max retries reached")
                raise e

                
def convert_icecat_to_qsc(filename: str) -> json:
    """
    Convert products to qsc format
    :param filename: relative path to file
    :return: converted json of products in qsc format
    """
    
    icecat_products = read_file_to_json(filename)
    
    converted_products = []
    
    for product in icecat_products:
        # Set header and payload of product
        tmp = {'header': {"id": product.get("id"), "action": "update"},
               'payload': {"title": product.get("title"), "id": product.get("id"), "name": product.get("name")}
              }
        
        # Create empty list to store attributes
        attributes = []
        
        # Iterate through keys in each product and filter out all keys starting with 'attr'
        for key in product:
            if str(key).startswith("attr"):
                key_tokens = key.split('_')

                # generate attribute name
                attr_name = ' '.join(key_tokens[2:])
                # remove multiple spaces
                attr_name = re.sub(' +', ' ', attr_name)

                # Set datatype of attribute. Valid types using the qsc are string, boolean, long, double, date
                data_type = ""
                
                # string
                if key_tokens[1] == 't':
                    data_type = "string"
                # double
                elif key_tokens[1] == 'n' and isinstance(product.get(key), float):
                    data_type = "double"
                # long
                elif key_tokens[1] == 'n' and isinstance(product.get(key), int):
                    data_type = "long"
                # boolean
                elif key_tokens[1] == 'b':
                    data_type = "boolean"

                # If attribute has a known datatype add type
                if data_type:
                    attributes.append({"name": attr_name, "dataType": data_type, "values": [product.get(key)]})
                # If the datatype is not valid don't add type
                else:
                    attributes.append({"name": attr_name, "values": [product.get(key)]})

        # If attributes were found add them to payload
        if bool(attributes):
            tmp['payload'].update({"attributes": attributes})
            
        # Append converted product to list
        converted_products.append(tmp)
        
    return converted_products
