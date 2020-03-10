#!/usr/local/bin/python3

"""Task 

Complete the Difference class by writing the following:
  - A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
  - A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.
"""

class Difference:
  def __init__(self, a):
    self.__elements = a

  # Add your code here
  def computeDifference(self):
    maximum = 0
    minimum = 100
    for value in self.__elements:
      if value > maximum:
        maximum = value
      if value < minimum:
        minimum = value

    self.maximumDifference = abs(maximum - minimum)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
    
    