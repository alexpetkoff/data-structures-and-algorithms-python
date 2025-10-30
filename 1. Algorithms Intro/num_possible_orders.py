def num_possible_orders(num_posts):
    total = 1

    for num in range(2, num_posts + 1):
        total *= num

    return total