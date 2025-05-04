# filepath: doi_checker_gui_project/doi_checker_gui_project/src/doi_checker_may_2025.py
# -*- coding: utf-8 -*-
"""
Created on Sun May 04 19:11 2025
@author: Obrad Vučkovac
@identifier: https://orcid.org/0000-0001-5616-2680
"""
# Function to check if a DOI already exists in the VinaR database

import requests
from requests.structures import CaseInsensitiveDict


def check_doi_exists(doi):
    """
    Check if a DOI already exists in the VinaR database.

    Parameters:
    doi (str): The DOI to check.

    Returns:
    bool: True if the DOI exists, False otherwise.
    """
    # Define the URL for the VinaR API endpoint
    url = "https://vinar.vin.bg.ac.rs/rest/items/find-by-metadata-field"

    headers = CaseInsensitiveDict()  # Case-insensitive dictionary for headers
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    data = {
        "key": "dc.identifier.doi",  # The key for DOI in the VinaR database
        "value": doi,  # The DOI to check
        "language": ""  # Language parameter, not specified
    }
    try:
        # Make a POST request to the VinaR database to check for the DOI
        resp = requests.post(url, headers=headers, json=data)
        if resp.json() == []:
            # If the response is an empty list, the DOI is not a duplicate
            print("DOI nije u repozitorijumu: ", doi)
            return False
        else:
            # If the response contains data, the DOI exists in the VinaR database
            vinar_metadata = resp.json()[0]
            vinar_handle = "https://vinar.vin.bg.ac.rs/" + vinar_metadata['handle']
            print(f"PAŽNJA! Već postoji zapis u VinaR-u sa istim DOI brojem: {vinar_handle}")
            return True
    except requests.exceptions.RequestException as e:
        # Handle any request exceptions
        print("An error occurred:", e)
        return None