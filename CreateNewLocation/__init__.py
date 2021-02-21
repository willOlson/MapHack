import logging
import pymongo
import azure.functions as func




#this is for the initial commit onto the database
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for creating a new location.')

    client = pymongo.MongoClient("mongodb+srv://arnav:barnie@cluster0.uzwam.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    mydb = client["db"]
    entry = mydb["locations"]

    
    nameofProject = req.params.get('Name of Project')
    pictureOfProject = req.params.get('Picture of Project')
    facility= req.params.get('Facility of Project')
    exactlocation= req.params.get('Exact Location of Project')
    longitude= req.params.get('Longitude')
    latitude= req.params.get('Latitude')
    when=req.params.get('When')
    program=req.params.get('Program (Urban Agriculture, Artistry and Craftmanship, Tourism and Hospitality)')
    beneficiaries=req.params.get("Beneficiaries (children, youth at risk, women, PWD, eldery)")
    support=req.params.get("Support Provided by MG to Beneficiaries")
    impact=req.params.get("Impact on Beneficiaries")
    number=req.params.get("Number of Beneficiaries Directly Impacted")
    activities=req.params.get("Activities of Beneficiaries")
    indirect=req.params.get("Indirect Impact on Communities")
    numberofIndirect=req.params.get("Number of Community Members Indirectly Impacted")


    if not nameofProject:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            nameofProject = req_body.get('Name of Project')
            pictureOfProject = req.params.get('Name of Project')
            facility= req_body.get('Facility of Project')
            exactlocation= req_body.get('Exact Location of Project')
            longitude= req_body.get('Longitude')
            latitude= req_body.get('Latitude')
            when=req_body.get('When')
            program=req_body.get('Program (Urban Agriculture, Artistry and Craftmanship, Tourism and Hospitality)')
            beneficiaries=req_body.get("Beneficiaries (children, youth at risk, women, PWD, eldery)")
            support=req_body.get("Support Provided by MG to Beneficiaries")
            impact=req_body.get("Impact on Beneficiaries")
            number=req_body.get("Number of Beneficiaries Directly Impacted")
            activities=req_body.get("Activities of Beneficiaries")
            indirect=req_body.get("Indirect Impact on Communities")
            numberofIndirect=req_body.get("Number of Community Members Indirectly Impacted")

    if nameofProject:
        location ={
        "Name of Project": nameofProject,
        "Picture of Project": pictureOfProject,
        "Facility of Project": facility,
        "Exact Location of Project": exactlocation,
        "Longitude ": longitude,
        "Latitude": latitude,
        "When": when,
        "Program (Urban Agriculture, Artistry and Craftmanship, Tourism and Hospitality)": program,
        "Beneficiaries (children, youth at risk, women, PWD, eldery)": beneficiaries,
        "Support Provided by MG to Beneficiaries": support,
        "Impact on Beneficiaries": impact,
        "Number of Beneficiaries Directly Impacted": number,
        "Activities of Beneficiaries": activities,
        "Indirect Impact on Communities": indirect,
        "Number of Community Members Indirectly Impacted": numberofIndirect
        }
        
        return func.HttpResponse(
             str(entry.insert_one(location).inserted_id),
             status_code=200
        )
    else:
        return func.HttpResponse(
             "Parameters were not given",
             status_code=200
        )
