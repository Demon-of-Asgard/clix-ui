import copy 
from typing import (List, Dict, Tuple)


class ClixPaths(object):
    """Class to hold nesessary path information of clix."""

    def __init__(self, paths:dict={}):
        """Accepts current working directory as  input. Set other paths relative to cwd"""

        assert isinstance(paths, Dict), f"Unexpeted type {type(paths)} for the <var paths>. Expect {Dict}"
        self.__paths:dict = {}

        for key, value in paths.items():
            self.__paths[key] = value
        return None 



    def add_paths(self, tobe_added:dict)->None:
        """Accepts dictionry of paths as input. Add the values of the 
        self.__paths dictiory"""
        assert isinstance(tobe_added, Dict), f"Unexpeted type {type(tobe_added)} for the <var tobe_added>. Expect {Dict}"

        existing_paths:list = []
        for key, value in tobe_added.items():
            if key not in self.__paths.keys():
                self.__paths[key] = value
            else:
                existing_paths.append(key)
            
        print(
            f"Following paths already exists./n" + \
            f"{existing_paths}./n" + \
            "You may want to use <update_paths> method to update them."
        )

        return 


    def update_paths(self, tobe_updated:dict)->None:
        """Accepts dictionry of paths as input. Update the values of the same"""
        assert isinstance(tobe_updated, Dict), f"Unexpeted type {type(tobe_updated)} for the <var tobe_updated>. Expect {Dict}"
        
        not_existing_paths:list = []
        for key, value in tobe_updated.items():
            if key not in self.__paths.keys():
                self.__paths[key] = value
            else:
                not_existing_paths.append(key)
            
        print(
            f"Following paths does not exist./n" + \
            f"{not_existing_paths}./n" + \
            "You may want to use <add_paths> method to add them."
        )

        return 


    def delete_paths(self, tobe_deleted:list)->None:
        assert isinstance(tobe_deleted, List), f"Unexpeted type {type(tobe_deleted)} for the <var tobe_deleted>. Expect {List}"

        for key in tobe_deleted:
            try:del self.__paths[key] 
            except KeyError: pass
        return


    def get_paths(self)->Dict:
        """Returns a copy of self.__paths"""
        return copy.deepcopy(self.__paths)