'''
Name: Deepanjal Kumar
Date: 10-03-2025
Description: Testing github action pipeline capabilities
'''
from fastapi import FastAPI
from dotenv import load_dotenv
import logging, uvicorn
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='myapp.log', # Log to a file
    filemode='a'           # Append to the log file (default)
)

load_dotenv()
app=FastAPI()

@app.get("/organization/{name}")
async def greetings(name:str):
    '''
    greetings: function to just greet the organization hitting the endpoint
    
    arguments:
        name: name of the organization
    
    return: it will return a json response if successfully executed it will return json response with great string  etc
    
    '''
    try:
        logging.info("[Info]: Successfully greated the organization: {}".format(name))
        return {
            "message":"Greetings : {}".format(name)
        }
    except Exception as e:
        logging.error("[Error]: Failed to great the organization for name :{} error message: {}".format(name, e))
        return {
            "message":"Failed to greet the organization"
        }


@app.get("/")
async def landingpageflow():
    '''
    landingpageflow() -> this function returns the greeting message to fellow user if ran successfully, else please try again message
    
    Arguments:
        None

    

    '''
    try:
        logging.info("[Info]: Greetings fellow users")
        return {
            "message": "Greetings fellow user"
        }
    except Exception as e:
        logging.error("[Error]: Failed to greet the fellow users")
        return {
            "message": "Sorry something went wrong please try again"
        }

'''
We will be using uvicorn for running the server

'''
