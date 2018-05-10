class Scheduler:
    currently_loaded_ids = []
    minutes = {}

    def __init__(self, interval=15):
        self.interval = interval
        for i in range(self.interval):
            self.minutes[i] = []

    def diff(self, first, second):
        second = set(second)
        return [item for item in first if item not in second]

    def load_ids(self, account_ids_list, minute):
        ''' Loads a list of new ids '''
        self.currently_loaded_ids.extend(account_ids_list)
        account_ids_list_index = 0
        for i in account_ids_list:
            minute_in_interval =  (account_ids_list_index + minute)  % self.interval
            self.minutes[minute_in_interval].append(i)
            account_ids_list_index += 1

    def unload_ids(self, account_ids_list):
        ''' Unload removed ids from de system '''
        for i in self.minutes:
            for j in account_ids_list:
                if j in self.minutes[i]:
                    self.currently_loaded_ids.remove(j)
                    self.minutes[i].remove(j)

    def get_account_ids_to_run(self, account_ids_list, minute):
        ''' Obtain the ids to run in a given minute '''

        # Check for new ids in the given list
        minute = minute % self.interval
        new_ids = self.diff(account_ids_list, self.currently_loaded_ids)
        if( len(new_ids) > 0 ):
            self.load_ids(new_ids, minute)

        # Check for removed ids in the given list
        removed_ids = self.diff(self.currently_loaded_ids, account_ids_list)
        if( len(removed_ids) > 0):
            self.unload_ids(removed_ids)

        account_ids_to_return = self.minutes[minute]
        return account_ids_to_return

# A little test
if __name__ == "__main__":
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

    s = Scheduler()
    for minute in range(120):
        print ( "Minute: %d" % (minute) )

        # Loads more ids
        if minute == 25:
            more_ids = [
                9999,
                7777,
                8888,
            ]
            dummy_ids.extend(more_ids)

        # Unload some ids
        if minute == 59:
            dummy_ids = dummy_ids[:3]

        print (s.get_account_ids_to_run(dummy_ids, minute ))
