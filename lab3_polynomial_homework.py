# """ очевидно, что буду использовать для хранения кэфов список: 
# ведь хранить степени нет смысла - степень это и есть индекс элемента в списке """
# class Polynomial():


#     def __init__(self, *coefficients):
#         # нужно обработать случаи: словарь, список, другой многочлен, или уп-й набор кэфов
#         # тк звездочка собирает все позиц. агр. в кортеж, то придется все корректно обработать
#         # важно: первый элемент в кортеже [0] - это один из следующих типов данных:
#         if len(coefficients) == 1:
#             value = coefficients[0] # первый элемент в кортеже входных данных

#             if isinstance(value, Polynomial):
#                 self.coefficients = value.coefficients

#             elif isinstance(value, (list, tuple)):
#                 self.coefficients = list(value)

#             elif isinstance(value, dict):
#                 self.coefficients = value.values()[::-1]
                




#     def __repr__(self):
#         pass


#     def __str__(self):
#         pass


#     def __eq__(self, other):
#         pass


#     def __add__(self, other):
#         pass


#     def __radd__(self, other):
#         pass


#     def __neg__(self):
#         pass


#     def __sub__(self, other):
#         pass


#     def __rsub__(self, other):
#         pass


#     def __call__(self, x):
#         pass


#     def degree(self):
#         pass


#     def der(self, d=1):
#         pass


#     def __mul__(self, other):
#         pass


#     def __rmul__(self, other):
#         pass


#     def __iter__(self):
#         pass


#     def __next__(self):
#         pass    


## polynomial.py
from itertools import zip_longest

 
 
class Polynomial:
    """Коэффициенты хранятся в списке: индекс элемента = степень."""

 
    def __init__(self, *coefficients):
        # одиночный аргумент: многочлен, список/кортеж, словарь или просто число
        if len(coefficients) == 1:
            value = coefficients[0]
            if isinstance(value, Polynomial):
                coefs = list(value.coefficients)
            elif isinstance(value, (list, tuple)):
                coefs = list(value)
            elif isinstance(value, dict):
                coefs = [0] * (max(value, default=0) + 1)
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

 
    def __repr__(self):
        return f"Polynomial {self.coefficients}"
    
 
    def __str__(self):
        terms = []
        for power in range(len(self.coefficients) - 1, -1, -1):
            coef = self.coefficients[power]
            if coef == 0:
                continue
            sign = "-" if coef < 0 else "+"
            coef = abs(coef)
            num = str(coef) if (power == 0 or coef != 1) else ""
            x = "" if power == 0 else "x" if power == 1 else f"x^{power}"
            terms.append((sign, num + x))
 
        if not terms:
            return "0"
        first_sign, first_body = terms[0]
        result = ("-" if first_sign == "-" else "") + first_body
        for sign, body in terms[1:]:
            result += f" {sign} {body}"
        return result
    
 
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
            return NotImplemented
        return self.coefficients == other.coefficients
    
 
    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
            return NotImplemented
        return Polynomial([a + b for a, b in
                           zip_longest(self.coefficients, other.coefficients, fillvalue=0)])
    
 
    def __radd__(self, other):
        return self + other
    
 
    def __neg__(self):
        return Polynomial([-c for c in self.coefficients])
    
 
    def __sub__(self, other):
        return self + (-other)
    
 
    def __rsub__(self, other):
        return (-self) + other
    
 
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
        if isinstance(other, (int, float)):
            other = Polynomial(other)
        if not isinstance(other, Polynomial):
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
 
