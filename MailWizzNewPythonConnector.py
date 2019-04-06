#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json


# In[2]:


INTERNAL_SERVER = "http://localhost:8080"


# In[3]:


def get_subscribers_user_add(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload):
    
    url = "{}/subscribers/user/add".format(INTERNAL_SERVER)
    
    headers = {
        'public-key': PUBLIC_KEY,
        'private-key': PRIVATE_KEY,
        'Content-Type': "application/x-www-form-urlencoded",
        'api-url': API_URL,
        'cache-control': "no-cache",
        'Postman-Token': "b27bb318-7376-4d05-b0de-191cbcfa9dcd"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    
    json_data = json.loads(response.text)
    
    return json_data


# In[4]:


#NTERNAL_SERVER = "http://localhost:8080"
#PUBLIC_KEY = "baa77c704bdcf92fd635c9d757650c405cc70000"
#PRIVATE_KEY = "510d15262bfdd86f91ea3c371268d824a7a24eb9"
#API_URL = "http://mailer46.en-vi-ar.com/api"
#payload = "list=hx786g44lr300&fname=james&lname=smith&email=anthony-custom-fields6%40yahoo.com&city=Beverly%20Hills&state=CA&zip=90210&address=CA&phone1=433454534&phone2=5435345345&ip=111.111.11.11&dsid=35555&undefined="

#get_subscribers_user_add(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload)


# In[ ]:


def get_lists_create(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload):
    
    url = "{}/lists/create".format(INTERNAL_SERVER)
    
    headers = {
        'public-key': PUBLIC_KEY,
        'private-key': PRIVATE_KEY,
        'Content-Type': "application/x-www-form-urlencoded",
        'api-url': API_URL,
        'cache-control': "no-cache",
        'Postman-Token': "b27bb318-7376-4d05-b0de-191cbcfa9dcd"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    
    json_data = json.loads(response.text)
    
    return json_data


# In[ ]:


#INTERNAL_SERVER = "http://localhost:8080"
#PUBLIC_KEY = "67e0747ff750686c8961a6e844b2ab0ad94a24a0"
#PRIVATE_KEY = "81114a2506cef8834e084ced33a77f0b63f64f68"
#API_URL = "http://mailer46.en-vi-ar.com/api"

#payload = "general_name=test%2011&general_description=This%20is%20a%20test%20list%2C%20created%20from%20the%20API.&defaults_from_name=Chris%20Barlow&defaults_from_email=anthony%40gmail.com&defaults_reply_to=anthony%40gmail.com&defaults_subject=testing%20subject&notifications_subscribe=yes&notifications_unsubscribe=yes&notifications_subscribe_to=anthony%40gmail.com&notifications_unsubscribe_to=anthony%40gmail.com&company_name=Chris%20Barlow%20INC&company_country=Costa%20Rica&company_zone=CA&company_address_1=CA&company_address_2=beverly&company_zone_name=zone%20&company_city=REALLY%20BIG%20COMPANY&company_zip_code=11111&general_opt_in=double&undefined="
    
#get_lists_create(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload)


# In[ ]:


def get_lists_show(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload):
    
    url = "{}/lists/show".format(INTERNAL_SERVER)

    payload = ""
    
    headers = {
        'public-key': PUBLIC_KEY,
        'private-key': PRIVATE_KEY,
        'Content-Type': "application/x-www-form-urlencoded",
        'api-url': API_URL,
        'cache-control': "no-cache",
        'Postman-Token': "b27bb318-7376-4d05-b0de-191cbcfa9dcd"
        }

    response = requests.request("GET", url, data=payload, headers=headers)

    json_data = json.loads(response.text)
    
    return json_data


# In[ ]:


#INTERNAL_SERVER = "http://localhost:8080"
#PUBLIC_KEY = "67e0747ff750686c8961a6e844b2ab0ad94a24a0"
#PRIVATE_KEY = "81114a2506cef8834e084ced33a77f0b63f64f68"
#API_URL = "http://mailer46.en-vi-ar.com/api"
#payload = ""
    
#get_lists_show(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload)


# In[ ]:


from flask import Flask, request

app = Flask(__name__)

@app.route("/lists/show", methods=['GET', 'POST'])
def get_lists_show_api():
    
    if request.method == 'GET':

        PUBLIC_KEY = request.args.get("public-key", None)
        PRIVATE_KEY = request.args.get("private-key", None)
        API_URL = request.args.get("api-url", None)
        payload = str(request.__dict__["environ"]["QUERY_STRING"])

        result = get_lists_show(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload)

        return str(result)
    
    else:
        
        PUBLIC_KEY = request.headers["public-key"]
        PRIVATE_KEY = request.headers["private-key"]
        API_URL = request.headers["api-url"]
        payload = str(request.form)
        
        values = list(request.form.values())
        keys = list(request.form.keys())
        
        params_string = ""
        for x, y in zip(values, keys):
            new_pair = "=".join([y,x+"&"])
            params_string = params_string + new_pair
    
        result = get_lists_show(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload=params_string)

        return str(result)
        
        



@app.route("/lists/create", methods=['GET', 'POST'])
def get_lists_create_api():
    
    if request.method == 'GET':

        PUBLIC_KEY = request.args.get("public-key", None)
        PRIVATE_KEY = request.args.get("private-key", None)
        API_URL = request.args.get("api-url", None)
        payload = str(request.__dict__["environ"]["QUERY_STRING"])

        result = get_lists_create(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload)

        return str(result)
    
    else:
                
        PUBLIC_KEY = request.headers["public-key"]
        PRIVATE_KEY = request.headers["private-key"]
        API_URL = request.headers["api-url"]
        payload = str(request.form)
        
        values = list(request.form.values())
        keys = list(request.form.keys())
        
        params_string = ""
        for x, y in zip(values, keys):
            new_pair = "=".join([y,x+"&"])
            params_string = params_string + new_pair
    
        result = get_lists_create(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload=params_string)

        return str(result)



@app.route("/subscribers/user/add", methods=['GET', 'POST'])
def get_subscribers_user_add_api():
    
    if request.method == 'GET':

        PUBLIC_KEY = request.args.get("public-key", None)
        PRIVATE_KEY = request.args.get("private-key", None)
        API_URL = request.args.get("api-url", None)
        payload = str(request.__dict__["environ"]["QUERY_STRING"])

        result = get_subscribers_user_add(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload)

        return str(result)
    
    else:
        
        PUBLIC_KEY = request.headers["public-key"]
        PRIVATE_KEY = request.headers["private-key"]
        API_URL = request.headers["api-url"]
        payload = str(request.form)
        
        values = list(request.form.values())
        keys = list(request.form.keys())
        
        params_string = ""
        for x, y in zip(values, keys):
            new_pair = "=".join([y,x+"&"])
            params_string = params_string + new_pair
    
        result = get_subscribers_user_add(INTERNAL_SERVER, PUBLIC_KEY, PRIVATE_KEY, API_URL, payload=params_string)

        return str(result)


# In[ ]:



if __name__ == '__main__':
    app.run()




