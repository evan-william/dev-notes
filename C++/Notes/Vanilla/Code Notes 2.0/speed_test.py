import time

start = time.time()

for _ in range(10000000):
    print(_)

end = time.time()

print(f"Execution time: {round((end - start) * 1000)} ms")
