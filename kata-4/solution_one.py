
with open('kata-4/weather.dat') as f:
    #lines = f.read().splitlines()
    lines = [line.strip() for line in f]
    print(lines)
