import configparser

def add_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    
    name = path.split('\\')[-1]
    files[name] = content

if __name__ == "__main__":
    files = {}
    offsets = {}

    config = configparser.ConfigParser()
    config.read("config.ini")

    # Find all file descriptions in the config file
    for section in config.sections():
        if "path" in config[section].keys():
            add_file(config[section]["path"])
            offsets[section] = config[section]["offset"]

    # Find all functions
    for section in config.sections():
        if "file" in config[section].keys():
            pattern = bytearray.fromhex(config[section]["pattern"])
            file = config[section]["file"]
            function_offset = files[file].find(pattern) + int(offsets[file][2:], 16) # Add to add an offset for each file
            print("[+] {}+{} : {}".format(file, hex(function_offset)[2:], section))

