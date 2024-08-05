import pandas as p
import numpy as n
d={"day":[1,2,3,4,5,6,7,8,9,10],
   "steps":[4335,4556,6789,3456,2345,4561,7891,9876,2345,5678]}
dp=p.DataFrame(d)
dp["+1000 steps"]=dp["steps"]+1000
fi=dp[dp["+1000 steps"]>7000]["day"]
print("DataFrame:\n",dp)
print("\n days on which steps were >7000:\n",fi)
