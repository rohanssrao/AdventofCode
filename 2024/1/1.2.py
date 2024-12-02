print(sum(a*b_s.count(a) for a_s, b_s in (zip(*[map(int, line.split()) for line in open(0).read().splitlines()]),) for a in a_s))
