import pandas as pd

df = pd.read_csv("refugee.csv")
df['tag'] = 'refugee'
df.to_csv('ref.csv')

df = pd.read_csv("tourist.csv")
df['tag'] = 'tourist'
df.to_csv('tour.csv')

df = pd.read_csv("student.csv")
df['tag'] = 'student'
df.to_csv('stu.csv')

df = pd.read_csv("employee.csv")
df['tag'] = 'employee'
df.to_csv('emp.csv')
