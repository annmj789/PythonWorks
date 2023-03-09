def one():
    def two():
        global name
        name="ann"
        print(name)
    def three():
        nonlocal name
        name="mary"
        print(name)
    def four():
        name="Jose"
        print(name)
    name="Sam"
    print(name)
    two()
    three()
    four()

one()
# print(name)
