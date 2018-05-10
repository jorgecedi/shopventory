dummy_ids = [
    10001,
    10002,
    10003,
    10004,
    10005,
    10006,
    10007,
    10008,
    10009,
    10010,
    10011,
    10012,
    10013,
    10014,
    10015,
    10016,
    10017,
]

interval = 15
currently_loaded_ids = []
minutes = {}

def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]

def load_ids(account_ids_list, minute):
    currently_loaded_ids.extend(account_ids_list)
    account_ids_list_index = 0
    for i in account_ids_list:
        minute_in_interval =  (account_ids_list_index + minute)  % interval
        minutes[minute_in_interval].append(i)
        account_ids_list_index += 1

def unload_ids(account_ids_list):
    for i in minutes:
        for j in account_ids_list:
            # print(j)
            if j in minutes[i]:
                currently_loaded_ids.remove(j)
                minutes[i].remove(j)

def get_account_ids_to_run(account_ids_list, minute):
    # Check for new ids in the given list
    minute = minute % interval
    new_ids = diff(account_ids_list, currently_loaded_ids)
    if( len(new_ids) > 0 ):
        load_ids(new_ids, minute)
    # Check for removed ids in the given list
    removed_ids = diff(currently_loaded_ids, account_ids_list)
    if( len(removed_ids) > 0):
        unload_ids(removed_ids)
    account_ids_to_return = minutes[minute]
    return account_ids_to_return

for i in range(interval):
    minutes[i] = []

for i in range(120):
    print ( "Minuto: %d" % (i) )
    if i == 59:
        dummy_ids = dummy_ids[:3]
    if i == 25:
        more_ids = [
            9999,
            7777,
            8888,
        ]
        dummy_ids.extend(more_ids)
    print (get_account_ids_to_run(dummy_ids, i ))
