import logging
import pymongo

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
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
    exists=entry.find_one({"Name of Project":nameofProject})
    if exists:
        return func.HttpResponse(str(exists),status_code=200)
    else:
        allVals=""
        # you have to use json.dumps(allVals) to turn into json str
        for entry in entry.find():
            allVals+=str(entry)
        return func.HttpResponse(allVals,status_code=200
        )
