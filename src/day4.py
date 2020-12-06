import numpy as np
import pandas as pd

print(np.array([[1, 2, 3], [2, 3, 4]]))

df = pd.DataFrame()
print(df.shape)


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
