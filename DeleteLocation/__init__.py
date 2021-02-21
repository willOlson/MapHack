import logging
import pymongo

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for deleting a location.')
    #params have to be able to be searched to be deleted 
    client = pymongo.MongoClient("mongodb+srv://arnav:barnie@cluster0.uzwam.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    mydb = client["db"]
    entry = mydb["locations"]

    
    nameofProject = req.params.get('Name of Project')
    
    if not nameofProject:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            nameofProject = req_body.get('Name of Project')
    #query for the name of the project
    exists=entry.find_one({"Name of Project":nameofProject})
    if exists:
        entry.delete_one({"Name of Project":nameofProject})
        return func.HttpResponse("Deleted",status_code=200)
    else:
        return func.HttpResponse(
             "Their is no data in the database that has that name",
             status_code=200
        )
