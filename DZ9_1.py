import pandas as pd

data = [['Андрей', 12], ['Егор', 15], ['Виктория', 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])
print(df)