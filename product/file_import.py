import pandas as pd
from .models import Product

# open the csv file
df = pd.read_csv('E:\Supermarket_shelf\Recommended_shelf/final.csv')

for arr in range(len(df)):
    product_id = df.loc[arr, ["Product Id"]].item()
    description = str(df.loc[arr, ["Description"]].item())
    quantity_sum = int(df.loc[arr, ["Sum of Quantity"]].values)
    cost_sum = round(float(df.loc[arr, ["Sum of Total Cost Price"]].values), 2)
    sell_sum = round(float(df.loc[arr, ["Sum of Total Selling Price"]].values), 2)
    profit_rupees = round(float(df.loc[arr, ["Profit Rupees"]].values), 2)
    profit_percentage = round(float(df.loc[arr, ["Profit %"]].values), 2)
    day = str(df.loc[arr, ["Weekday/Weekend/Holiday"]].item())
    # print('id: ', product_id, ' desc: ', description, 'Qunatity: ', quantity_sum, ' Cost: ', cost_sum, ' Sell: ',
    #       sell_sum, ' Rupee: ', profit_rupees, ' Profit: ', profit_percentage, ' Day: ', day)
    Product.objects.create(product_id=product_id, description=description, quantity_sum=quantity_sum, cost_sum=cost_sum,
                           sell_sum=sell_sum, profit_rupees=profit_rupees, profit_percentage=profit_percentage, day=day)
