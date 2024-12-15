#!/usr/bin/env python3
import argparse
import json
import os

def file_exist_check(path):
    file_path = path;

    if os.path.exists(file_path):
        return True
    else:
        return False

def get_overall_db(pre):
    return pre.split()[1]

# returns r4 numberical value for LowShelf (LSC), Peaking (PK), HighShelf (HSC)
def translate_to_r4_band_type(band_type):
    match band_type:
        case "LSC":
            return 0
        case "PK":
            return 1
        case "HSC":
            return 2
        case _:
            return "Something went wrong here"

# generates a single r4 output band
def translate_to_r4_output_band(band):
    r4_band = {}
    band_split = band.split()
    r4_band["a"] = band_split[5] # Hz
    r4_band["b"] = band_split[-1] # Q
    r4_band["c"] = band_split[8] # gain
    if band_split[2] == "ON":
        r4_band["d"] = 1
    else:
        r4_band["d"] = 0
    r4_band["e"] = translate_to_r4_band_type(band_split[3])
    return r4_band
    


def main():
    # Create and configure the parser
    parser = argparse.ArgumentParser(description="Convert AutoEq ParametricEQ.txt file for use with Hiby R4 PEQ")
    parser.add_argument("--eq", type=str, help="Path to ParametricEQ.txt file",required=True)
    parser.add_argument("--name", type=str, help="Eq name",required=True)
    args = parser.parse_args()
    eq_path = args.eq
    eq_name = args.name

    if file_exist_check(eq_path) == False:
        print(f"The Specific path {eq_path} does not exist")
        exit(1)

    output = {}
    output["b"] = eq_name
    with open(eq_path, "r") as file:
        eq = [line.strip() for line in file]

    # split the overal db from the 10 band eq
    pre = eq[0]
    ten_band_eq = eq[1:11]
    output["c"] = get_overall_db(pre)
    r4_eq_bands = []
    

    for band in ten_band_eq:
        r4_eq_bands.append(translate_to_r4_output_band(band))

    output["a"] = r4_eq_bands
    output_json = json.dumps(output)
    print(output_json)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()