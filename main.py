import yaml as yaml
from pathlib import Path
from src.arxiv_items import Item
from typing import (Union, List, Dict, Tuple)

import flet as ft
from pages import render_category 

def read_yaml(fpath:Union[str, Path])->dict:
    data:dict = {}
    with open(fpath, "r") as f:
        data.update(yaml.load(f, Loader=yaml.FullLoader))
    return data
 

def print_dict(data_dict:dict, carry:int=0, end_line:str="\n")->None:
    last_carry:int = carry
    keys = data_dict.keys()
    carry += 1
    for key, value in data_dict.items():
        if isinstance(value, dict):
            print(f"{'\t'*(carry-1)}{key}: ", end=end_line)
            key2s = list(value.keys())
            value2s:list = []
            for k in key2s:
                if not isinstance(value[k], dict): end_line = "\n"
                else: 
                    end_line = ""
            print_dict(value, carry - 1, end_line)
        else:
            print(f"{'\t'*(carry)}{key}: {value}")



def main(page:ft.Page)->None:
    
    # Read Items and subitems from yaml file
    data = read_yaml(Path("configs") / "available_arxiv_categories.yaml")

    # Create List of Items objects. 
    # Each item in the list may or may not have nested subitems
    items_list = []
    itemid = 0
    for key, value in data.items():
        items_list.append(
            Item(
                id_=itemid,
                title_= key,
                value_=value,
            )
        )

        itemid += 1
    render_category.render_cat_and_subcat(page, items_list=items_list)
    

if __name__ == "__main__":
    ft.app(main)