import functools


class Order:
    def __init__(self, order_num, title_author, quantity, price_per_item):
        self.order_num = order_num
        self.title_author = title_author
        self.quantity = quantity
        self.price_per_item = price_per_item


orders = [
    Order(34587, 'Learning Python, Mark Lutz', 4, 40.95),
    Order(98762, 'Programming Python, Mark Lutz', 5, 56.80),
    Order(77226, 'Head First Python, Paul Barry', 3, 32.95),
    Order(88112, 'Einführung in Python3, Bernd Klein', 3, 24.99)
]

totals = map(lambda order: (order.order_num,
                            (order.quantity*order.price_per_item
                             if order.quantity*order.price_per_item > 10000
                             else order.quantity*order.price_per_item + 10)),
             orders)

print(list(totals))


# Part 2
sublist = [34587,
           ('Learning Python, Mark Lutz', 4, 40.95),
           ('Programming Python, Mark Lutz', 5, 56.80)]
sublist.reverse()
order_number = sublist.pop()


def reducer(acc: list, curr):
    cost = curr[1] * curr[2]
    acc.append((order_number, cost))
    return acc


new_sublist = functools.reduce(reducer, sublist, [])

print(new_sublist)
