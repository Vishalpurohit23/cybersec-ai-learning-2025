week1 = [14, 16, 19, 21, 13, 15, 18]
week2 = [15, 17, 20, 22, 14, 16]
# ask the user and add another day sales in week 2
new_sale = int(input("Enter the sales for the new day in week 2: "))
week2.append(new_sale)
# combine both weeks into one list called sales
sales = week1 + week2
# profit per lemonade
profit_per_lemonade = 1.5
# calculate earning of best and worst day and print them
best_day_earning = max(sales) * profit_per_lemonade
worst_day_earning = min(sales) * profit_per_lemonade
print(f"Best day earning: ${best_day_earning}")
print(f"Worst day earning: ${worst_day_earning}")

total_earning = sum(sales) * profit_per_lemonade
print(f"Total earning: ${total_earning}")
