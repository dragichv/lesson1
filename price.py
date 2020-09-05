def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return one + delimiter + two

p = get_summ("Learn", "python")
p=p.upper()
print(p)