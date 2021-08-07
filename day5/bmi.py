

class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def get_bmi(self) -> float:
        return float(self.weight) / (self.height ** 2)

    def get_grade(self) -> str:
        bmi = self.get_bmi()
        if bmi >= 30.0:
            return "obese"
        elif bmi >= 25.0:
            return "over"
        elif bmi >= 18.5:
            return "normal"
        else:
            return "under"


def main():
    data = [
        (80, 1.73),
        (55, 1.58),
        (49, 1.91)]
    for values in data:
        bmi = Bmi(values[0], values[1])
        print(bmi.get_grade(), end=' ')
    print()


if __name__ == '__main__':
    main()
