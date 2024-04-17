class LSystem:
    def __init__(self, variables, axiom, rules):
        self.variables = variables
        self.axiom = axiom
        self.rules = rules

    def apply_rules(self, string):
        new_string = ""
        for char in string:
            if char in self.variables:
                new_string += self.rules[char]
            else:
                new_string += char
        return new_string

    def produce(self, n):
        current_string = self.axiom
        for _ in range(n):
            current_string = self.apply_rules(current_string)
        return current_string


variables = {'A', 'B'}
axiom = 'A'
rules = {'A': 'AB', 'B': 'A'}

lsystem = LSystem(variables, axiom, rules)
n = 5
result = lsystem.produce(n)
print("Result:", result)
