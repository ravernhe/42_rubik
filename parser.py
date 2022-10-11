class FileParser:

    def __init__(self, file_name=str):
        self.file_name = file_name
        self.map = {'size': 0, 'grid': []}


    def parse(self):
        self.parse_file()
        self.catch_error()
        self.normalized_grid(self.map["size"])

    def normalized_grid(self, size):
        self.map["grid"] = [self.map["grid"][i * size : i * size + size] for i in range(size)]
    
    def parse_file(self):
        try:
            file = open(self.file_name,"r")
        except:
            raise FileNotFoundError(f"File {self.file_name} cannot be oppened.")
        
        lines = file.readlines()
        for line in lines:
            line = line.split("#")[0]
            if line:
                line = line.split()
                if self.map["size"] == 0:
                    if len(line) != 1:
                        raise ValueError("self.map size must specified correctly")
                    if not line[0].isnumeric():
                        raise ValueError("self.map size must be numeric")
                    if int(line[0]) < 2:
                        raise Exception("self.map size cannot be less than 2")
                    self.map["size"] = int(line[0]) 
                else:
                    for x in line:
                        if not x.isnumeric():
                            raise ValueError("self.map must only contain numbers")
                        self.map["grid"].append(int(x))

    def catch_error(self):
        self.map_lenght = self.map["size"] * self.map["size"]
        if len(self.map["grid"]) != self.map_lenght:
            raise Exception("self.map does not match the self.map size specified")
        grid_set = set(self.map["grid"])
        if len(grid_set) != self.map_lenght:
            raise Exception("self.map must not contain duplicates")
        if min(grid_set) != 0 or max(grid_set) != self.map_lenght - 1:
            raise ValueError("self.map values out of range")
