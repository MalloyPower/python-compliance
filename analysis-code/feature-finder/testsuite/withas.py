
# New style
with A() as a, B() as b:
    pass

#Can have a bunch of these
with A() as a, B() as b, C() as c, D() as d:
    pass


# Old 2.6 style
with A() as a:
    with B() as b:
        pass


