# def calculate_discounted_price(price, discount):              Junior code
#     discounted_price = 0
#     if discount > 0 and discount <=100:
#         discounted_price = price * (1 - discount / 100)
#     elif discount == 0:
#         discounted_price = price
#     else:
#         raise ValueError("Discount should be between 0 and 100")

#     return discounted_price


def calculate_discounted_price(price, discount):  # Senior dev code
    if discount < 0 or discount > 100:
        # Guard clause deployed early to stop any unnessecary logic from being performed
        raise ValueError("Discount should be between 0 and 100")

    if discount == 0:
        return price  # Another guard clause incase the discount is not equal to anything just stop and return price

    return price * (1 - discount / 100)
