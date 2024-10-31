from typing import (Union, List, Dict, Tuple)

# ---------------- [ class: Item ]
class Item:

    # ---------------- [ func: __init__ ]
    def __init__(
        self,
        title_:str,
        id_:int, 
        value_:Union[str, Dict, List],
    ) -> None:
        """Create a class object from dictioary item. 
        If value is again a Dict type, then the initializer 
        recursively creates a new nested subitem(s)."""

        self.id : int = id_
        self.title : str = title_ 
        self.have_subitem: bool = True 
        self.value:Union[str, Dict, List] = [] 

        if isinstance(value_, dict):
            id: int = 0
            for key, value in value_.items():
                self.value.append(self.create_item(id=id, item={key:value}))
                id += 1
            self.have_subitem = False
        else:
            self.value = value_
    
    # ---------------- [ func: __str__ ]
    def __str__(self)->str:
        return f"({self.__class__}, {self.id}, {self.title})"

    # ---------------- [ func: create_item ]
    def create_item(self, id:int=0, item:dict={}):    
        key = list(item.keys())[0]
        value = item[key]
        return Item(id_=id, title_=key, value_=value) 

    # ---------------- [ func: print_item ]
    def print_item(self, ntab:int=0)->None:
        """Print items and values recursively with intendations to 
        distinguish nested (sub-)items."""

        assert ntab >= 0, "number of tab cannot be negative."
        nt:int = ntab
        if isinstance(self.value, list):
            print(f"{'\t'*ntab}{self.title}: ", end="\n")
        if self.have_subitem:
            print(f"{'\t'*ntab}{self.title}: {self.value}")
        else:
            nt += 1
            if isinstance(self.value, list):
                for next_item in self.value:
                    next_item.print_item(ntab=nt)
    
    # ---------------- [ func: get_item ]
    def get_item(self)->Dict:
        """Reurn id, title, value"""
        return (
            {
                "id": self.id,
                "title" : self.title,
                "value" : self.value
            }
        )
