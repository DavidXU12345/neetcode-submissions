class TimeMap:

    def __init__(self):
        self.key_to_timestamp_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timestamp_value[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamp_value_list = self.key_to_timestamp_value[key]
        left = 0
        right = len(timestamp_value_list)
        while left < right:
            mid = left + (right - left) // 2
            if timestamp_value_list[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1
        if left == 0:
            return ""
        return timestamp_value_list[left - 1][1]
        
