from aocd import submit

duration = 44826981
record = 202107611381458
options = 0
for time in range(1, duration):
    distance = time * (duration - time)
    if distance > record:
        options += 1

submit(options)
