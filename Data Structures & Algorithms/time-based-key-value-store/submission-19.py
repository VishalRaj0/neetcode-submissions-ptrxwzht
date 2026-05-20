class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        _list = self.store[key]
        if not _list:
            return ""

        i = 0
        j = len(_list) - 1
        res = ""
        while i <= j:
            m = (i + j) // 2
            ts, val = _list[m]
            print(i , j, _list[m])
            res = val
            if ts < timestamp:
                i = m + 1
            elif ts > timestamp:
                j = m - 1
            else:
                return res
        
        if ts > timestamp:
            if m > 0:
                res = _list[m - 1][1]
            else:
                res = ""
        
        return res

        
