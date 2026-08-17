class TimeMap:

    def __init__(self):
        self.events = {} # key = string, value = list of [value, timestamp]



    def set(self, key: str, value: str, timestamp: int) -> None:
        # does the key even exist in the map
        if key not in self.events:
            self.events[key] = []
        # with a non-empty map, we can just append the pairing to our time map
        self.events[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # if key deosnt exist, we can return an empty string
        resres = ""

        # we get the sublist that contains the string value and the timestamp 
        values = self.events.get(key,[])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            middle = (l + r) // 2
            # if our middle timestamp is equal or less to the one we're looking for 
            if values[middle][1] <= timestamp:
                resres = values[middle][0]
                l = middle + 1
            # this is an invalid timestamp (too big)
            else:
                r = middle - 1
        return resres

        
