print(sum(test for line in open(0) for test, *nums in [map(int, line.strip().replace(':', '').split())] if test in (rec := lambda l: l if len(l) == 1 else [j for i in rec(l[:-1]) for j in [i + l[-1], i * l[-1], int(str(i) + str(l[-1]))]])(nums)))
