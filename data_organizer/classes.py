class Item(object):
    def __init__(
        self, 
        id:int, 
        value:list|dict|str, 
        title:str, 
        is_selected:bool=False,
    )->None:

        self.id:int           = id
        self.title:str        = title 
        self.is_selected:bool = is_selected
        if type(value) == type({}):
            
            self.value:dict | list | str = create_item(item=value)
        else:
            self.value = value

    def on_click(self): self.is_selected = not self.is_selected

    


