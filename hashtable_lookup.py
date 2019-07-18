def hashtable_lookup(htable,key):
    for i in hashtable_get_bucket(htable,key):
        if key==i[0]:
            return i[1]
    return None

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,key).append([key,value])
    return htable

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Ellis', 11], ['Francis', 13]], 
         [], 
         [['Bill', 17], ['Zoe', 14]],
         [['Coach', 4]], 
         [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtable_lookup(table, 'Francis')

print hashtable_lookup(table, 'Louis')

print hashtable_lookup(table, 'Zoe')
