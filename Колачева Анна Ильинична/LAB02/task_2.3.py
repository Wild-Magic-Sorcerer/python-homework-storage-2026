#!/usr/bin/env python3

import ast
import math

DELIMITER = "; "

def user_input(text: str) -> str:
    znach = input(text)
    return znach

def parse_value(s: str):
    s_stripped = s.strip()
    
    try:

        return ast.literal_eval(s_stripped)
    
    except (ValueError, SyntaxError):
    
        return s_stripped

def rasbor_po_tipam(list_elem: list) -> dict[type, list]:
    result = {}
    
    for el in list_elem:
        el_type = type(el)
        
        if el_type not in result:
            result[el_type] = []
            
        result[el_type].append(el)
        
    return result

if __name__ == "__main__":
    us_i = user_input(f"Введите последовательность аргументов через '{DELIMITER}':\n")
    
    list_el = [parse_value(i) for i in us_i.split(DELIMITER)]
    
    grouped = rasbor_po_tipam(list_el)

    if int in grouped:
        product = math.prod(grouped[int])
        print(f"Произведение int: {product}")
    
    for t, items in grouped.items():
        print(f"Тип {t.__name__}: {items}")
