import pandas as pd
d=pd.DataFrame([[2,5,6],
              [4,6,7],
              [5,7,8]],
              columns=["maths","java","python"])
print(d)
c=d.agg(['sum','min','max','count','mean','std','size'])
print(c)