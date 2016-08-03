import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Do different home_ownerships apply for more loan_amnt?

data = pd.read_csv('../LoanStats3a.csv')
#index = ['NONE','RENT', 'OWN', 'MORTGAGE', 'OTHER']
#mapping = pd.Series([1,2,3,4,5], index)
#x = data['home_ownership'].map(mapping)
#plt.hist(x.dropna()) 
#
#plt.xlabel("Home Ownership")
#plt.ylabel("No. of Loans")
#plt.title("What Ownerships Borrow the Most?")
#
#axes = plt.gca()
#axes.set_xticks([i for i in range(1,6)])
#axes.set_xticklabels(index)
#
#fig = plt.gcf()
#fig.set_size_inches(10, 10, forward=True)
#fig.savefig('homeownership.png', dpi=100)
#
#plt.show()

#explore relationship for renters, owners, and mortgage holders
df2 = data[['total_acc', 'home_ownership', 'grade','loan_amnt']]
df2 = df2.dropna()
#y = df2['loan_amnt']
#x = df2['total_acc']
#plt.scatter(x,y, marker="o")
#fig = plt.gcf()
#fig.set_size_inches(10, 10, forward=True)
#fig.savefig('totalacc.png', dpi=100)
#axes = plt.gca()
#axes.set_xticks(x)
#axes.set_xticks([i for i in range(1,60)])
#axes.set_ylim([min(y),max(y)])
#axes.set_xlim([0,60])

#plt.hist(x,bins=20)
plt.show()

#grouping attempt
bygroup_loans1 = df2.groupby(['home_ownership', 'grade'])
bygroup_loans2 = df2.groupby(['grade','home_ownership'])
bygroup_loans3 = df2.groupby(['total_acc'])

bygroup_loans3.agg([np.sum, np.mean, np.std, len])


