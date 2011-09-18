class NegativeNumberException(Exception):
    pass

class DistanceInMiles:

    def __init__(self, distance, original_format = "miles"):
        if distance < 0:
            raise NegativeNumberException()

        self.original_format = original_format
        self.distance = distance

    def calculate(self):
        if self.original_format is "km":
            return self.distance *1.6
        return self.distance

    @staticmethod
    def calculated_from(distance, format="miles"):
        return DistanceInMiles(distance, format).calculate()

