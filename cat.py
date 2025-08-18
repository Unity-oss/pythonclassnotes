import time
import os

frames = [
    r"""
  /\_/\  
 ( o.o ) 
 > ^ <   ♪
""",
    r"""
  /\_/\  
 ( -.- ) 
 > ^ <   ♫
""",
    r"""
  /\_/\  
 ( o.o ) 
 > ^ <   ♩
""",
    r"""
  /\_/\  
 ( ^_^ ) 
 > ^ <   ♬
"""
]

while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen
        print(frame)
        time.sleep(0.4)