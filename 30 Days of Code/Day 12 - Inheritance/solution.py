#!/usr/local/bin/python3

"""Task 

You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.
Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters:
    1. A string, firstName.
    2. A string, lastName.
    3. An integer, id.

An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:

O - 90 <= average <= 100
E - 80 <= average < 90
A - 70 <= average < 80
P - 55 <= average < 70
D - 40 <=  average < 55
T - average < 40
"""

class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    
    def __init__(self, firstName, lastName, idNumber, scores: list):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores    

    def calculate(self) -> str:
        average = 0
        for index, value in enumerate(scores):
            average += value
        
        average = average/(index+1)
        if 90 <= average  <= 100:
            return 'O'
        elif 80 <= average < 90:
            return 'E'
        elif 70 <= average < 80:
            return 'A'
        elif 55 <= average < 70:
            return 'P'
        elif 40 <= average < 55:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
