# Useful util functions to avoid cluttering the main logic files with

def remove_duplicates_from_list(listToPrune: list):
    return list(dict.fromkeys(listToPrune))