import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'


import json
# def create_resource():
#     new_emp={
#         'eno':700,
#         'ename':'sukku',
#         'esal':30000,
#         'eaddress':'rajupalem'
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
   
# #create_resource()    

# def delete_resource(id):
#     resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
    
#delete_resource(1) 
def get_resource(id=None):
    data={}   
    if data is not None:
        data={
            'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
    
get_resource()
# def update_resource(id):
#     new_emp={
# #         'id':id,
#         'esal':25000,
#         'eaddress':'Mum'
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# #update_resource(3)
# def Delete_resource(id):
#     new_emp={
#         'id':id,

#     }
#     resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# #Delete_resource(56)
    