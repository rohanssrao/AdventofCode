print(sum(any(all(r[i+1] - r[i] in range(s*1, s*4, s) for i in range(len(r)-1)) for s in [-1,1]) for r in [list(map(int, l.split())) for l in open(0).read().splitlines()]))
