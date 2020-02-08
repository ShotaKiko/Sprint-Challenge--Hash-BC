#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #Will use enumerate to count an iterable and return object
    for index, item in enumerate(weights):
        targetValue = hash_table_retrieve(ht, limit-item)
        #if targetValue is present---
        if targetValue != None:
            if targetValue>index: return(targetValue, index)
            else: 
                return (index, targetValue)
        
        #or if targetValue is NONE
        else:
            hash_table_insert(ht, item, index)
            

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
