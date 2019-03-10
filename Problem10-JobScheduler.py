"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds
"""
from time import sleep
def solution(f, n):
    sleep(n/1000)
    return f()

from threading import Thread
def test(a):
    print a
job = Thread(target=solution, args=(lambda: test("HI"), 4))
print("Start")
job.start()
sleep(0.004)
print("End")



