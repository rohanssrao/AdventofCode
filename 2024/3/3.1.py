print(sum(int(a)*int(b) for a,b in __import__("re").findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", open(0).read())))
