import numpy as np
import pandas as pd

numbers = np.array([1, 2, 3, 4])
frame = pd.DataFrame({"number": numbers, "square": numbers ** 2})

print(frame)