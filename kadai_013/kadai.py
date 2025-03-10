def calc_totalprice(price, tax_rate):
    tax = price * tax_rate / 100
    total_price = price + tax
    return total_price

price = 110
tax_rate = 10

total_price = calc_totalprice(price, tax_rate)
print(f"合計金額：{total_price}円です。")