# CHAPTER 3.7
import time
randomNumber = int(time.time()) % 26
print(chr(ord('A') + randomNumber))