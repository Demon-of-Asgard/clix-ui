import time
import pprint
from definisions.path_definitions import ClixPaths


def main():
    path_obj = ClixPaths({"root": "/"})
    path_obj.add_paths({"home": "/root/home", "manu": "/root/home/manu"})

    pprint.pprint(path_obj.get_paths())

    path_obj.delete_paths(["root",])

    pprint.pprint(path_obj.get_paths())
    
if __name__ == "__main__":
    main()