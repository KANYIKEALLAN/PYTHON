date=input("\nEnter Date:")
item_name=input("\nEnter Item Name:")
cost_price=int(input("\nCost Price:"))
transport_cost=int(input("\nTransport Cost:"))

selling_price=int(cost_price + 0.05 * cost_price ) + int(0.02 * transport_cost)
profit_margin=int(selling_price - cost_price)

print(f"\nSelling Price:{selling_price}\n\nprofit:{profit_margin}\n\t\t\n\n***Thanks***\t\t\n\n")




