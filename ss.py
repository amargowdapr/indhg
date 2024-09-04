import pandas as pd
import matplotlib.pyplot as plt

data = {
    "First_name": ["Aryan", "Rohan", "Riya", "Yash", "Siddhant"],
    "Last_name": ["Singh", "Agarwal", "Shah", "Bhatia", "Khanna"],
    "Type": ["Full-Time", "Intern", "Full-Time", "Part-Time", "Full-Time"],
    "Dept": ["Administration", "Technical", "Administration", "Technical", "Management"],
    "YoE": [2,6,8,14,20],
    "Salary": [1000, 1500, 2000, 3500, 4000]
}

df = pd.DataFrame(data)
av=df.pivot_table(index=['Dept', 'Type'], values='Salary', aggfunc='mean')
print("Average Salary from ecah dept: \n", av)
sm=df.pivot_table(index=['Type'], values= 'Salary', aggfunc=['sum', 'mean', 'count'])
sm.columns=['Total Salary', 'Mean Salary', 'Number of Employees']
print("\nSum and Mean of:\n",sm)
St=df.pivot_table(values= 'Salary', index='Type', aggfunc='std')
print("\nStandard Deviation:\n", St)

# Combine YoE and Salary into a single plot
plt.figure(figsize=(8, 6))
plt.plot(df["YoE"], df["Salary"], marker='p', linestyle='dashed', color='blue', label='Salary')
plt.xlabel("Years of Experience (YoE)")
plt.ylabel("Salary")
plt.title("Salary vs. Years of Experience")
plt.legend()
plt.grid(True)
plt.show()