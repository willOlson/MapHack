import logging
import pymongo


import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for updating a location.')

    #params have to be able to be searched to be deleted 
    client = pymongo.MongoClient("mongodb+srv://arnav:barnie@cluster0.uzwam.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    mydb = client["db"]
    entry = mydb["locations"]

    #retriving param names in the document 
    nameofProject = req.params.get('Name of Project')

    #the first value will always be the name of the object you want it to change 
        #if it has more than one name then the second name will be the updated name
        #all the params will except the first one will be the updated values in the database
    print(req.params)
    if not nameofProject:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            nameofProject = req_body.get('Name of Project')

    #first i need to check if it is even in the database
    exists =None

    if nameofProject:
        newName =nameofProject.split(',')
        if len(newName) ==2:
            exists=entry.find_one({"Name of Project":newName[0]})
        else:
            exists=entry.find_one({"Name of Project":nameofProject})
    
    if exists:
        #this means the user want to change the name of the project
        if(len(newName)==0):
            #still have errors unable to change the name of project
            newValues=req.params
            newValues["Name of Project"] =newName[1]
            entry.update_one({"Name of Project":newName[0]},{"$set":newValues})
            return func.HttpResponse("Name chnged",status_code=200)
        else:
            entry.update_one({"Name of Project":nameofProject},{"$set":req.params})
            return func.HttpResponse("Other Elments Changed",status_code=200)
            
    else:
        return func.HttpResponse(
             "The item does not exist",
             status_code=200
        )
