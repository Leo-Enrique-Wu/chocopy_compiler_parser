class testcase(obj):
    def func(x:int, y:int, z:int):
        # for expression with multiple comparison operators, our parser are able to parse it without throwing error just like Python. This enables us to do semantic analysis further and allows us to implement feature in Python like (1 == 2 and 2 == 3).
        1 == 2 == 3

        # It also works in more complicated context (e.g. if-elif statement)

        if x > y > z:
            pass
        elif y < z > x:
            pass

        # or expressions need to be evaluated
        if x + y > z - y > 7 * z * y < x * y:
            if 2 + z - x == x != y == x * y * z:
                pass
