# python -m pip install "pymongo[srv]"==3.11
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv(override=True) # haetaan ensisijaisesti .env -tiedostosta, sitten vasta ympäristömuuttujista

def connect():
    uri = f"mongodb+srv://{os.getenv("DBUSERNAME")}:{os.getenv("DBPASSWORD")}@cluster0.m52g8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    try:                        
        client = MongoClient(uri) ### LISÄÄ CONNECTION STRINGISI,
                                                           ### HAE SALASANASI .env -TIEDOSTOSTA)
        print("connected to mongo")
        return client
    except:
        print("connection error")

def fetch_new_id(coll):
    ### FUNKTION TULEE PALAUTTAA UUSI id, JOTA KANNASSA EI VIELÄ OLE.
    ### MIKÄLI KANNASSA EI OLE YHTÄÄN DOKUMENTTIA, PALAUTETAAN 0.
    pass #placeholder, (poista)

def fetch_task_by_id(coll,task_id):
    ### FUNKTION TULEE HAKEA task_id -MUUTTUJAN PERUSTEELLA TIETOKANNASTA TASK, JONKA id ON task_id
    ### JA PALAUTTAA LÖYTYNYT TASK
    pass #placeholder, (poista)