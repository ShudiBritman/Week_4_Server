



def load_data(file):
    with open(file, "r") as f:
        data = f.read()
    return data
    
    
    
def save_data(data, path: str):
    with open(path, "a") as f:
        f.write(data)
    return data


