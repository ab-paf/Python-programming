import matplotlib.pyplot as plt
list = [r]
try:
    f = open("data.dat", "w")
    f.write("x, x^3\n")
    for elem in x:
        cube = elem ** 3
        x_3.append(cube)
        data = str(elem) + ", " + str(cube) + "\n"
        f.write(data)
except:
    sys.exit("Some error happen while reading or converting")
