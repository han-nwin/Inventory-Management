def calculate_rop(sale_velocity, production_time, shipping_time, processing_time, safety_stock):
    lead_time = production_time + shipping_time + processing_time
    return (sale_velocity * lead_time) + safety_stock

def calculate_shipping_cost(units, shipping_time, method):
    # Define shipping costs per unit for air and sea
    if method == "air":
        cost_per_unit = 2.0  # Example air shipping cost per unit
    elif method == "sea":
        cost_per_unit = 0.8  # Example sea shipping cost per unit
    else:
        cost_per_unit = 1.4  # Average cost for partial (air + sea)
    
    return units * cost_per_unit

def main():
    print("Welcome to the Inventory Management Calculator!")

    # Prompt the user for input data
    sale_velocity = int(input("Enter the sale velocity (units/day): "))
    current_stock = int(input("Enter the current stock level (units): "))
    safety_stock = int(input("Enter the safety stock (units): "))
    production_time = int(input("Enter the production time (days): "))
    processing_time = int(input("Enter the inventory processing time (days): "))

    # Define shipping options and times
    air_shipping_time = 20  # average days for air shipping
    sea_shipping_time = 35  # average days for sea shipping
    partial_shipping_time = (air_shipping_time + sea_shipping_time) // 2  # example blend for partial shipping

    options = [
        ("All Air Shipping", air_shipping_time, "air"),
        ("All Sea Shipping", sea_shipping_time, "sea"),
        ("Partial Air and Sea Shipping", partial_shipping_time, "partial")
    ]

    # Calculate and display ROP and shipping cost for each option
    for option in options:
        name, shipping_time, method = option
        rop = calculate_rop(sale_velocity, production_time, shipping_time, processing_time, safety_stock)
        shipping_cost = calculate_shipping_cost(rop, shipping_time, method)
        days_until_reorder = (current_stock - safety_stock) // sale_velocity
        
        print(f"\n{name}:")
        print(f"  Reorder Point (ROP): {rop} units")
        print(f"  Estimated Shipping Cost: ${shipping_cost:.2f}")
        print(f"  Days Until Reorder (based on current stock): {days_until_reorder} days")

if __name__ == "__main__":
    main()

