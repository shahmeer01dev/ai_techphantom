import pandas as pd
import matplotlib.pyplot as plt

data = {
    "visitors": [100, 200, 300, 400, 500, 450, 720, 120, 540, 320],
    "sales": [1125, 4400, 9000, 5000, 3400, 6000, 3300, 8000, 3400, 12000]
}

df = pd.DataFrame(data)

plt.plot(df['visitors'], label='Visitors')
plt.plot(df['sales'], label='Sales')

plt.show()

# print(df)

