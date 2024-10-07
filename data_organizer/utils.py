from .classes import Item

def create_item(id:int=0, item:dict={}):    
    key = list(item.keys())[0]
    value = item[key]
    return Item(id=id, title=key, value=value)