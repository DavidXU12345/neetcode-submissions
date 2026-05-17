class TimeMap:

    def __init__(self):
        self.store: Dict[str, List[(int, str)]] = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        res = ""
        for t, v in values:
            if t <= timestamp:
                res = v
            else:
                break
        return res
        
