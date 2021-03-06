import os

class ResourceManager:
    def __init__(self):
        self.resources = []
        self.path = os.getcwd()
        self.resource_folder = "res"
        
    """
    def traverseResFolder(self):
        pass #codice che analizza la cartella res e per ogni elemento
             #aggiunge ['key',Resource()] a self.resources
    """
    
    def get_path(self):
        return self.path + "/" + self.resource_folder + "/"
    
    def getResource(self, key):
        
        object_path = self.path + "/" + self.resource_folder + "/" + key
        return object_path               #"full resource absoulute path (value)"
