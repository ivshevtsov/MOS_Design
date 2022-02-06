import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cp = pd.read_csv('Files/Mism_test.csv')
print(cp['FC_GLO'])
cp.FC_GLO.hist()
cp.FC_GLO.hist()
plt.show()