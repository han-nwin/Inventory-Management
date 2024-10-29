def calculate_rop(sale_velocity, production_time, shipping_time, processing_time, safety_stock):
    lead_time = production_time + shipping_time + processing_time
    return (sale_velocity * lead_time) + safety_stock, lead_time

def calculate_shipping_cost(units, cost):
    return units * cost

def main():
    print("Welcome to the Inventory Management Calculator!")

    # Prompt the user for input data
    sale_velocity = int(input("Enter the sale velocity (units/day): "))
    current_stock = int(input("Enter the current stock level (units): "))
    safety_stock = int(input("Enter the safety stock (units): "))
    production_time = int(input("Enter the production time (days): "))
    processing_time = int(input("Enter the inventory processing time (days): "))

    # Define shipping options and times
    air_shipping_time = int(input("Enter air shipping time (days): "))  # average days for air shipping
    sea_shipping_time = int(input("Enter sea shipping time (days): "))  # average days for sea shipping
    partial_shipping_time = (air_shipping_time + sea_shipping_time) // 2  # example blend for partial shipping

    air_cost = float(input("Enter air shipping unit price ($): "))
    sea_cost = float(input("Enter sea shipping unit price ($): "))
    partial_shipping_cost = (air_cost + sea_cost) / 2

     # Seasonal adjustment for sales spikes
    seasonal_increase = input("Do you expect a 20% increase in sales during the holiday season? (yes/no): ").strip().lower()
    if seasonal_increase == "yes":
        sale_velocity *= 1.2  # Increase sale velocity by 20%

    options = [
        ("All Air Shipping", air_shipping_time, "air", air_cost),
        ("All Sea Shipping", sea_shipping_time, "sea", sea_cost),
        ("Partial Air and Sea Shipping", partial_shipping_time, "partial", partial_shipping_cost)
    ]

    # Calculate and display ROP and shipping cost for each option
    for option in options:
        name, shipping_time, method, ship_cost = option
        rop, lead_time = calculate_rop(sale_velocity, production_time, shipping_time, processing_time, safety_stock)
        shipping_cost = calculate_shipping_cost(rop, ship_cost)
        days_until_reorder = (current_stock - rop) // sale_velocity
        
        print(f"\n{name}:")
        print(f"  Reorder Point (ROP): {rop} units")
        print(f"  Estimated Shipping Cost: ${shipping_cost:.2f}")
        print(f"  Days Until Reorder (based on current stock): {days_until_reorder} days")
        print(f"  Lead Time for {name}: {lead_time} days")

if __name__ == "__main__":
    main()

