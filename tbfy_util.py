from typing import Tuple, Dict

'''
    Utility functions for interacting with TheyBuyForYou JSON tender data
'''

def get_title(tender: Dict) -> str:
    return tender["title"]

def get_description(tender: Dict) -> str:
    return tender["description"]

def get_classification(tender: Dict) -> Tuple:
    '''
        Selects one classification from the tender data. This will either come from the
        tender itself or from the first item in the tender.

        There are multiple schemes available in the data, CPV is just one, so need to retain
        the scheme as well as the classification id.
    '''
    if tender.get("classification"):
        cls = tender["classification"]["id"]
        scheme = tender["classification"]["scheme"]
        return (cls,scheme)

    if not tender.get("items"):
        return (None,None)

    item0 = tender["items"][0]
    if item0.get("classification"):
        cls = item0["classification"]["id"]
        scheme = item0["classification"]["scheme"]
    elif item0.get("additionalClassifications"):
        cls = item0["additionalClassifications"][0]["id"]
        scheme = item0["additionalClassifications"][0]["scheme"]
    else:
        cls = None
        scheme = None

    return (cls,scheme)
