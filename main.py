import os
import time
import pprint
import yaml as yaml
import flet as ft
from data_organizer import categories
from data_organizer.utils import (create_item, )

def read_yaml(fpath:str)->dict:
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
    cats_and_subcats:dict = read_yaml(
        os.path.join("clix_pages", "resources", "available_arxiv_categories.yaml")
    )

    id = 0
    item_list:list = []
    for key, value in cats_and_subcats.items():
        item_list.append({key:value})
    # for key, value in data.items():
    #     item_list.append(create_item(id=id, item={key:value}))
    
    for item in item_list:
        categories.render_category_list(page, item)
        # print(item)

    # print_dict(data)
    

if __name__ == "__main__":
    # main()
    ft.app(main)