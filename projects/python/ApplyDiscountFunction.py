def apply_discount(price, discount):
    # Check types
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    # Check values
    if price <= 0:
        return "The price should be greater than 0"
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calculate final price
    final_price = price * (1 - discount / 100)
    
    return final_price
