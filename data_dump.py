import pymongo
import json
import pandas as pd
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns {df.shape}")

    #Convert dataframe to json to dump records in MongoDB
    df.reset_index(drop = True,inplace = True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #Insert Record to Mongo DB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    