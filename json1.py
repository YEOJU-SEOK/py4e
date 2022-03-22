import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

#여기서 load's'가 string이라고 생각
#loads로 dic형식으로 반환
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
