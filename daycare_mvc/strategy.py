# strategy.py
from abc import ABC, abstractmethod

# Interface stratégie
class PaymentStrategy(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass

# Stratégie 1 : abonnement standard
class StandardPayment(PaymentStrategy):
    def calculate(self, amount):
        return amount

# Stratégie 2 : abonnement avec réduction
class DiscountPayment(PaymentStrategy):
    def calculate(self, amount):
        return amount * 0.9  # 10% de réduction

# Contexte
class Subscription:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def get_total(self, amount):
        return self.strategy.calculate(amount)

# usage
subscription = Subscription(StandardPayment())
print(subscription.get_total(100))  # 100

subscription.set_strategy(DiscountPayment())
print(subscription.get_total(100))  # 90
