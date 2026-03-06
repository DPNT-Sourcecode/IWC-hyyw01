class SumSolution:
    def _validate_number_in_range(self, value: int) -> None:
        if value < 0 or value > 100:
            raise ValueError("Value must be in range 0 - 100")

    def compute(self, x, y):
        self._validate_number_in_range(value=x)
        self._validate_number_in_range(value=y)
        return x + y

