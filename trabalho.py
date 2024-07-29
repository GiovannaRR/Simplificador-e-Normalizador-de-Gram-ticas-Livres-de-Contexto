class Grammar:
    def __init__(self, productions):
        self.productions = productions
        self.non_terminals = set(productions.keys())
        self.terminals = set()
        for rhs in productions.values():
            for symbol in rhs:
                if symbol.islower():
                    self.terminals.add(symbol)

    def remove_unreachable_symbols(self):
        reachable = set()
        to_process = {'S'}

        while to_process:
            symbol = to_process.pop()
            if symbol not in reachable:
                reachable.add(symbol)
                if symbol in self.productions:
                    for rhs in self.productions[symbol]:
                        for s in rhs:
                            if s in self.non_terminals and s not in reachable:
                                to_process.add(s)

        self.non_terminals = self.non_terminals.intersection(reachable)
        self.productions = {k: v for k, v in self.productions.items() if k in self.non_terminals}

    def remove_empty_productions(self):
        nullable = set()
        for nt, rhss in self.productions.items():
            for rhs in rhss:
                if rhs == '':
                    nullable.add(nt)

        while True:
            new_nullable = nullable.copy()
            for nt, rhss in self.productions.items():
                for rhs in rhss:
                    if all(s in nullable for s in rhs):
                        new_nullable.add(nt)
            if new_nullable == nullable:
                break
            nullable = new_nullable

        new_productions = {}
        for nt, rhss in self.productions.items():
            new_productions[nt] = set()
            for rhs in rhss:
                subsets = self.get_non_empty_subsets(rhs, nullable)
                for subset in subsets:
                    if subset:
                        new_productions[nt].add(subset)

        self.productions = new_productions

    def get_non_empty_subsets(self, rhs, nullable):
        if not rhs:
            return {''}
        first = rhs[0]
        rest_subsets = self.get_non_empty_subsets(rhs[1:], nullable)
        if first in nullable:
            return {first + s for s in rest_subsets} | rest_subsets
        else:
            return {first + s for s in rest_subsets}

    def remove_unit_productions(self):
        new_productions = {nt: set() for nt in self.productions}
        for nt, rhss in self.productions.items():
            for rhs in rhss:
                if len(rhs) == 1 and rhs in self.non_terminals:
                    for unit_rhs in self.productions[rhs]:
                        new_productions[nt].add(unit_rhs)
                else:
                    new_productions[nt].add(rhs)
        self.productions = new_productions

    def to_chomsky_normal_form(self):
        # Step 1: Eliminate start symbol from RHS
        self.productions['S0'] = {'S'}
        self.non_terminals.add('S0')

        # Step 2: Remove empty productions
        self.remove_empty_productions()

        # Step 3: Remove unit productions
        self.remove_unit_productions()

        # Step 4: Convert to binary productions
        new_productions = {}
        for nt, rhss in self.productions.items():
            new_productions[nt] = set()
            for rhs in rhss:
                if len(rhs) > 2:
                    new_nt = nt
                    while len(rhs) > 2:
                        new_nt_1 = new_nt + '_1'
                        new_productions[new_nt_1] = {rhs[0] + new_nt}
                        new_nt = new_nt_1
                        rhs = rhs[1:]
                    new_productions[new_nt].add(rhs)
                else:
                    new_productions[nt].add(rhs)

        self.productions = new_productions

    def to_greibach_normal_form(self):
        pass  # This is a complex process and usually requires substantial effort.

    def left_factor(self):
        pass  # Implement left factoring if needed

    def remove_left_recursion(self):
        pass  # Implement removal of left recursion if needed

    def __str__(self):
        result = []
        for nt, rhss in self.productions.items():
            result.append(f"{nt} -> {' | '.join(rhss)}")
        return '\n'.join(result)


# Example usage
productions = {
    'S': {'aAa', 'bBv'},
    'A': {'a', 'aA'}
}

grammar = Grammar(productions)
grammar.remove_unreachable_symbols()
print("After removing unreachable symbols:")
print(grammar)

grammar.remove_empty_productions()
print("After removing empty productions:")
print(grammar)

grammar.remove_unit_productions()
print("After removing unit productions:")
print(grammar)

grammar.to_chomsky_normal_form()
print("In Chomsky Normal Form:")
print(grammar)

# grammar.to_greibach_normal_form()
# print("In Greibach Normal Form:")
# print(grammar)

# grammar.left_factor()
# print("After left factoring:")
# print(grammar)

# grammar.remove_left_recursion()
# print("After removing left recursion:")
# print(grammar)
