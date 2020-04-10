#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i, w in enumerate(weights):
        if w <= limit: # If current weight is not bigger than limit
            i2 = hash_table_retrieve(ht, limit - w)
            if i2 == None: # If (limit - weight) doesn't exist, insert current weight
                hash_table_insert(ht, w, i)
            else: # If does exist, sum of weights equals limit
                return [i, i2]
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
