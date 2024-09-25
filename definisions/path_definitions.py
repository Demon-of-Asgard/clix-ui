import os 
import copy 

class VarMap(object):
    def __init__(self, name:str, value):
        self.name:str = name 
        self.value = value
    
    def set_value(self, new_value):
        self.value = new_value
    
    def get_name(self):
        return self.name 
    
    def get_value(self):
        return self.value 
    
    def __repr__(self):
        return f"variable: {self.name}, value: {self.value}"
    


class ClixPaths(object):
    """Class to hold nesessary path information of clix."""
    def __init__(self, cwd:str):
        """Accepts current working directory as  input. Set other paths relative to cwd"""
        self.__cwd = VarMap("cwd", cwd)
        self.__resource_dir = VarMap(
            "resource_dir", 
            os.path.join(
                self.__cwd.value, 
                "resources"
            )
        )


        self.__category_des = VarMap(
            "category_des", 
            os.path.join(
                self.__cwd.value, self.__resource_dir.value, 
                "available_arxiv_categories.yaml"
            )
        )

       
        self.__path_keys:list = [
            "cwd", "resources", "category_description",
        ]

        self.__all_paths = [
            self.__cwd, self.__resource_dir, self.__resource_dir
        ]


        return None 

    def set_paths(self, to_updated:dict)->tuple:
        """Accepts dictionry of paths as input. Update the values of the """
        err:list = []
        iserr:bool = False
        tobe_updated_keys = to_updated.keys()
        for key in tobe_updated_keys:
            if key not in self.__path_keys:
                err.append(f"UnIdentifiedKeyErr:<{key}>")
                iserr = True
            else:
                for pth in self.__all_paths:
                    if pth.get_name() == key:
                        pth.set_value(to_updated[key])

        return (True if iserr else False, err)

    def get_paths(self)->dict:
        return copy.deepcopy(self.__paths)