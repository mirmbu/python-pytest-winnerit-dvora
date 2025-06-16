def calculate_discount(price, discount_price):
    if price <= 0 or discount_price <= 0:
        raise ValueError("Price and discount must be non-negative")
    return price * (1 - discount_price / 100)

