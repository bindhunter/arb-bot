import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, time_frame):
        self.max_calls = max_calls
        self.time_frame = time_frame
        self.calls = deque()

    def __enter__(self):
        while len(self.calls) >= self.max_calls:
            time_passed = time.time() - self.calls[0]
            if time_passed < self.time_frame:
                time.sleep(self.time_frame - time_passed)
            self.calls.popleft()
        self.calls.append(time.time())

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass