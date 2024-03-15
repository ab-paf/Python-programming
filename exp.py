# 6: Table with different objects
# the format string can be assigned to variable, so it
# can be reused
fm = "{0:04d}{1:>12}{2:>4d}{3:>8.2f} Euro{4:8.2f} Euro"

# 3 dicts are created
artname = {23: "apple", 8: "banana", 42: "peach"}
count = {23: 1, 8: 3, 42: 5}
price = {23: 1.95, 8: 1.45, 42: 3.05}

print("{0:>4}{1:>12}{2:>4}{3:>13}{4:>13}".format
      ("No.", "Name", "#", "Price", "Total"))

for x in 23, 8, 42:
    print(fm.format(x, artname[x], count[x],
                    price[x], count[x] * price[x]))
print()

# 7: Table with different objects
# the format string can be assigned to variable, so it
# can be reused
fm = "{0:04d}{1:>12}{2:>4d}{3:>8.2f} Euro{4:8.2f} Euro"

# 8: 4 iterable objects are created
# zip glues these together
artno = [23, 8, 42]
artname = ["apple", "banana", "peach"]
count = {1, 3, 5}
price = [1.95, 1.45, 3.05]

articles = zip(artno, artname, count, price)

print("{0:>4}{1:>12}{2:>4}{3:>13}{4:>13}".format
      ("No.", "Name", "#", "Price", "Total"))

for x in articles:
    print(fm.format(x[0], x[1], x[2], x[3], x[2] * x[3]))