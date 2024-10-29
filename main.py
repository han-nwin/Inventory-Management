def calculate_rop(sale_velocity, production_time, shipping_time, processing_time, safety_stock):
    lead_time = production_time + shipping_time + processing_time
    return (sale_velocity * lead_time) + safety_stock, lead_time

def calculate_shipping_cost(units, cost):
    return units * cost

def calculate_order_quantity(sale_velocity, lead_time, safety_stock):
    return (sale_velocity * lead_time) + safety_stock

def main():
    print("Welcome to the Inventory Management Calculator!")

    # Prompt the user for input data
    sale_velocity = int(input("Enter the sale velocity (units/day): "))
    current_stock = int(input("Enter the current stock level (units): "))
    safety_stock = int(input("Enter the safety stock (units): "))
    production_time = int(input("Enter the production time (days): "))

    # Define shipping options and times
    air_shipping_time = int(input("Enter air shipping time (days): "))  # average days for air shipping
    sea_shipping_time = int(input("Enter sea shipping time (days): "))  # average days for sea shipping
    
    air_cost = float(input("Enter air shipping unit price ($): "))
    sea_cost = float(input("Enter sea shipping unit price ($): "))

    processing_time = int(input("Enter the inventory processing time (days): "))

    percent_air = int(input("Enter percentage of inventory by air: "))
    partial_shipping_time = (air_shipping_time*percent_air + sea_shipping_time*(100-percent_air)) // 100  # example blend for partial shipping


    partial_shipping_cost = (air_cost * percent_air + sea_cost * (100 - percent_air)) / 100
    # Seasonal adjustment for sales spikes
    seasonal_increase = input("Do you expect a 20% increase in sales during the holiday season? (yes/no): ").strip().lower()
    if seasonal_increase == "yes":
        sale_velocity *= 1.2  # Increase sale velocity by 20%
    
    partial_name = str(percent_air) + "% Air "  + str(100 - percent_air) + "% Sea"
    options = [
        ("All Air Shipping", air_shipping_time, air_cost),
        ("All Sea Shipping", sea_shipping_time, sea_cost),
        (partial_name, partial_shipping_time, partial_shipping_cost)
    ]

    # Calculate and display ROP, shipping cost, order quantity, and reorder timing for each option
    for name, shipping_time, ship_cost in options:
        rop, lead_time = calculate_rop(sale_velocity, production_time, shipping_time, processing_time, safety_stock)
        shipping_cost = calculate_shipping_cost(rop, ship_cost)
        
        # Calculate order quantity based on the lead time
        order_quantity = calculate_order_quantity(sale_velocity, lead_time, safety_stock)
        
        # Days until reorder depends on method-specific lead time
        days_until_reorder = (current_stock - rop) // sale_velocity
        monthly_cadence = (order_quantity/lead_time) * 30
        print(f"\n{name}:")
        print(f"  Reorder Point (ROP): {rop:.0f} units")
        print(f"  Estimated Shipping Cost: ${shipping_cost:.2f}")
        print(f"  Lead Time for {name}: {lead_time} days")
        print(f"  Minimum Order Quantity to Cover Lead Time: {order_quantity:.0f} units")
        print(f"  Days Until Next Order to Avoid Stockout: {days_until_reorder:.0f} days")
        print("------------------------------------------")
        print("Suggested Cadence and Order Quantity:")
        print(f"Order Quantity = {monthly_cadence:.0f} units every month")
        print("==========================================")

if __name__ == "__main__":
    main()

