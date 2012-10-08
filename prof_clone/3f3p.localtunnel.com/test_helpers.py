def assert_evolution(evaluator, compare):
    def checker():
        old_value = evaluator()
        while True:
            yield 
            new_value = evaluator()
            assert compare(new_value, old_value) 
            old_value = new_value
    return checker().next

def approximately_eq(precision):
    def approximately_eq_inner(lhs, rhs):
        return round(lhs-rhs, precision) == 0
    return approximately_eq_inner
