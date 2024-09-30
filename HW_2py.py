# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:12:12 2024

@author: duski
"""

import re
import numpy as np
import pandas as pd

def switch_name(name):
    if name.find(',') == -1:
        return name
        
    last_name, first_name = name.split(", ")
    
    first_parts = first_name.split()
    
    if len(first_parts) > 1:
        first = first_parts[1]
        middle_initial = first_parts[0]
        rearranged = f"{first} {middle_initial} {last_name}"
    else:
        rearranged = f"{first_parts[0]} {last_name}"
    
    return rearranged


def main():
    
    raw_data = "555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\
tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
    TITLE = r"(?:Dr\.|Rev\.|Mr\.|Mrs\.|Ms\.)\s*"
    NAME1 = r"[A-Z][a-z]+,?\s+"
    MIDDLE_I = r"(?:[A-Z][a-z]*\.?\s*)?"
    MIDDLE_I2 = r"(?:[A-Z][a-z]*\.?\s?)"
    NAME2 = r"[A-Z][a-z]+"
    
    name_pattern = r"(?:{title})?{name1}{middle_i}{name2}".format(
        title=TITLE, name1=NAME1, middle_i=MIDDLE_I, name2=NAME2
    )
    
    num_pattern = r"(?:\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}"
    
    nums = np.array(re.findall(num_pattern, raw_data))
    
    names = np.array(re.findall(r"[a-zA-Z., ]{2,}", raw_data))
    
    names = [switch_name(name) for name in names]
    
    print(nums)
        
    HasTitle = [bool(re.search(TITLE, x)) for x in names]
    
    middle_name = [bool(re.search(NAME1 + MIDDLE_I2 + NAME2, x)) for x in names]
    
    print(names)
    
    print(HasTitle)
    
    print(middle_name)
    
if __name__ == "__main__":
    main()