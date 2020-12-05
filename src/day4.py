import pandas as pd
import numpy as np


def hello():
    print("hello world")


hello()
for i in range(1, 10, 1):
    if (i % 2 == 0):
        print(f"i={i},**")
    if (i % 3 == 0):
        print(f"i={i},***")
    if (i % 5 == 0):
        print(f"i={i},*****")
