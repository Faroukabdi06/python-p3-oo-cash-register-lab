#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.total = 0
    self.items = []
    self.discount = discount

  def add_item(self,title,price,quantity=1):
    self.last_transaction = {"title": title, "price": price, "quantity": quantity}
    original_quantity = quantity
    cost = price*original_quantity
    self.total += cost
    while quantity >=1:
      self.items.append(title)
      quantity-=1
    return self.total

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      applied_discount = (self.total * self.discount)/100
      self.total-= applied_discount
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    last_transaction = self.last_transaction #{"title": title, "price": price, "quantity": quantity}
    new_quantity = last_transaction["quantity"]
    cost = last_transaction["price"] * new_quantity
    self.total -=cost
    for x in range(new_quantity):
      self.items.remove(last_transaction["title"])
    return self.total



