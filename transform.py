import glob
import json

import pandas as pd


def get_all_filenames():
    files = glob.glob("raw_data_*.json")
    return files


def transform_one_file(filename):
    results=[]
    with open(filename) as file:
        data = json.load(file)

    for key, value in data.items():
        # key is "Algiers"
        # value is data["Algiers"]
        result = {"city":key,"time":data[key]["time"],"temperature":data[key]["temperature"],"longtitude":data[key]["lon"],"latitude":data[key]["lat"]}
        results.append(result)
    return results
    pass

def merge_all_files_in_pandas_df(files):
        merged_files=[]
        for file in files:
            trans_file= transform_one_file(file)
            merged_files.extend(trans_file)
        
        df = pd.DataFrame(merged_files)
        return df

def drop_duplicates(df_):
    pass

def main():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    print(df)
    # df = drop_duplicates(df)
    df.to_csv("transformed_data.csv", index=False)


main()