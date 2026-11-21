

class Polynomial:
    """Коэффициенты хранятся в списке: индекс элемента = степень."""

    def __init__(self, *coefficients):
        # один аргумент: многочлен, список/кортеж, словарь или число
        if len(coefficients) == 1:
            value = coefficients[0]
            if isinstance(value, Polynomial):
                coefs = list(value.coefficients)
            elif isinstance(value, (list, tuple)):
                coefs = list(value)
            elif isinstance(value, dict):
                coefs = [0] * (max(value, default=-1) + 1)
                for power, coef in value.items():
                    coefs[power] = coef
            else:
                coefs = [value]
        else:
            # набор коэффициентов через запятую
            coefs = list(coefficients)

        # убираем старшие нулевые коэффициенты (но оставляем хотя бы один)
        while len(coefs) > 1 and coefs[-1] == 0:
            coefs.pop()
        self.coefficients = coefs or [0]

    @staticmethod
    def _convert(other):
        """Приводит число к многочлену; для чужих типов возвращает None."""
        if isinstance(other, Polynomial):
            return other
        if isinstance(other, (int, float)):
            return Polynomial(other)
        return None

    def __repr__(self):
        return f"Polynomial {self.coefficients}"

    def __str__(self):
        result = ""
        for power in range(len(self.coefficients) - 1, -1, -1):
            coef = self.coefficients[power]
            if coef == 0:
                continue
            # коэффициент 1 не пишем, кроме свободного члена
            num = "" if (abs(coef) == 1 and power > 0) else str(abs(coef))
            x = "" if power == 0 else "x" if power == 1 else f"x^{power}"
            if result == "":
                result = ("-" if coef < 0 else "") + num + x
            else:
                result += (" - " if coef < 0 else " + ") + num + x
        return result or "0"

    def __eq__(self, other):
        other = self._convert(other)
        if other is None:
            return NotImplemented
        return self.coefficients == other.coefficients

    def __add__(self, other):
        other = self._convert(other)
        if other is None:
            return NotImplemented
        # дополняем более короткий список нулями до одинаковой длины
        n = max(len(self.coefficients), len(other.coefficients))
        a = self.coefficients + [0] * (n - len(self.coefficients))
        b = other.coefficients + [0] * (n - len(other.coefficients))
        return Polynomial([x + y for x, y in zip(a, b)])

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Polynomial([-c for c in self.coefficients])

    def __sub__(self, other):
        other = self._convert(other)
        if other is None:
            return NotImplemented
        return self + (-other)

    def __rsub__(self, other):
        other = self._convert(other)
        if other is None:
            return NotImplemented
        return other + (-self)

    def __call__(self, x):
        return sum(c * x ** i for i, c in enumerate(self.coefficients))

    def degree(self):
        return len(self.coefficients) - 1

    def der(self, d=1):
        coefs = self.coefficients
        for _ in range(d):
            coefs = [i * coefs[i] for i in range(1, len(coefs))]
        return Polynomial(coefs)

    def __mul__(self, other):
        other = self._convert(other)
        if other is None:
            return NotImplemented
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result[i + j] += a * b
        return Polynomial(result)

    def __rmul__(self, other):
        return self * other

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i >= len(self.coefficients):
            raise StopIteration
        pair = (self._i, self.coefficients[self._i])
        self._i += 1
        return pair


# примеры работы кода:
print(Polynomial([1, 2, 3]))            # 3x^2 + 2x + 1
print(Polynomial({0:-3, 2:1, 5:4}))     # 4x^5 + x^2 - 3
print(Polynomial([7, -2, 0, -1]))       # -x^3 - 2x + 7
print(repr(Polynomial(1, 2, 3, 0, 0)))  # Polynomial [1, 2, 3]
print(Polynomial(1, 2, 3)(1))           # 6