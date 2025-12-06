# Advent of Code 2025

This year, I tried to solve each problem with one line of Python.

Each solution file contains:
- The one-liner
- A pretty-printed version of the one-liner to aid readability (commented out)
- A standard non-one-liner solution (commented out)

## Tips and tricks

Write out a complete solution in regular code first. Your goal is to convert this solution into a one-liner by turning **EVERYTHING** into an expression and concatenating the expressions together using tuples.

- Assignments can be turned into assignment expressions with the walrus operator `:=`. For example:
   ```py
   a = 1
   ```
   becomes
   ```py
   a := 1
   ```
- Function definitions can be turned into expressions by instead making them named lambdas. For example:
   ```py
   def add(a, b):
       return a+b
   ```
   becomes
   ```py
   add := lambda a, b: a+b
   ```
- Your expressions will all live inside one big tuple. They'll be evaluated in order just like regular statements. For example:
   ```py
   (
       a := 1,
       b := 2,
       a+b
   ) # == 3
   ```
- `for` loops can be turned into list comprehensions. For example:
   ```py
   for i in range(n):
       for j in range(m):
           print(i, j)
   ```
   becomes
   ```py
   [
       print(i, j)
       for i in range(n)
       for j in range(m)
   ]
   ```
- `if` statements can be turned into conditional expressions. For example:
   ```py
   if n > 3:
       print(n)
   ```
   becomes
   ```py
   print(n) if n>3 else None
   ```
- `return` statements can be simulated by indexing into tuples. For example:
   ```py
   def add(a, b):
       total = a+b
       return total
   ```
   becomes
   ```py
   add := lambda a, b:
       (
           total := a+b,
           total
       )[-1]
   ```
- Assignments to subscripts can be turned into calls to `__setitem__`. For example:
   ```py
   a = [1, 2, 3]
   a[0] = 2
   ```
   becomes
   ```py
   (
       a := [1, 2, 3],
       a.__setitem__(0, 2)
   )
   ```
- The `global` keyword, which is used to allow mutations to global variables inside functions, can be simulated with mutations of the `globals()` dictionary. For example:
   ```py
   a = 1
   def f():
       global a
       a = 2
   f()
   print(a) # 2
   ```
   becomes
   ```py
   (
       a := 1,
       f := lambda:
           globals().__setitem__("a", 2),
       f(),
       print(a)
   ) # 2
   ```
- `while` loops can be simulated with `list(iter(<callable>, <sentinel>))`. `iter()`, when called with two arguments, returns an iterator which calls its first argument every time it is iterated until the sentinel value is returned. The sentinel in this case should be the negation of our `while` condition. We then wrap this with `list()` to evaluate the entire iterable because it's lazy otherwise. (Note that this is more like an `until` loop than a `while` loop because the lambda will always be called at least once.) For example:
   ```py
   a = 5
   while a != 0:
       print(a)
       a -= 1
   # 5, 4, 3, 2, 1
   ```
   becomes
   ```py
   (
       a := 5,
       list(iter(lambda:
           (
               print(a),
               globals().__setitem__("a", a-1),
               a
           )[-1]
       , 0))
   ) # 5, 4, 3, 2, 1
   ```