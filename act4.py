class TripPurse:
    def __init__(self, money):
        self.balance = money

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Trip money cannot be negative.")
        self.__balance = amount

    def pay(self, fare):
        if fare <= 0 or fare > self.balance:
            return False
        self.balance -= fare
        return True


class Journey:
    def __init__(self, student, money):
        self.student = student
        self.purse = TripPurse(money)
        self._legs = []
        self.transport = None

    @property
    def completed_legs(self):
        return len(self._legs)

    def travel(self, transport, distance):
        if distance <= 0:
            return "Distance must be positive. No trip started."

        self.transport = transport
        fare = self.transport.quote_fare(distance)

        if fare == 0 or self.purse.pay(fare):
            self._legs.append(transport)
            return (
                f"{self.student} travels by {transport.name}: "
                f"UGX {fare:,}."
            )

        return f"{self.student}: not enough money for {transport.name}."