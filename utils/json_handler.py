import json


class JsonHandler:
    
    @staticmethod
    def load_data(json_file_path):
        with open(json_file_path, "r") as f:
            data = json.load(f)
        return data
    
    
    @staticmethod
    def save_data(data:dict, path: str):
        with open(path, "w") as f:
            json.dump(data, f)
        return data

