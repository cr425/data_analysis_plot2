import pandas as pd
import matplotlib.pyplot as plt

#Do different home_ownerships apply for more loan_amnt?

data = pd.read_csv('LoanStats3a.csv')
index = ['NONE','RENT', 'OWN', 'MORTGAGE', 'OTHER']

mapping = pd.Series([1,2,3,4,5], index)
data['home_ownership_int'] = data['home_ownership'].map(mapping)
home_ownership_int = data['home_ownership_int']

x = home_ownership_int
y = data['loan_amnt']
plt.bar(x,y, width = .2, color = "blue")
plt.xlabel("Home Ownership")
plt.ylabel("Loan Amount")
plt.title("What Ownerships Borrow the Most?")
axes = plt.gca()
axes.set_ylim([min(y),max(y)])
axes.set_xticks([i for i in range(1,6) ])
axes.set_xticklabels(index)

fig = plt.gcf()
fig.set_size_inches(10, 10, forward=True)
fig.savefig('homeownership.png', dpi=100)
