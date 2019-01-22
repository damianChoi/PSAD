# -*- coding: utf-8 -*-
"""ch1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IjPF8OtlNhlXtUokOwEQ3ZnEdOqlcCog

# 1. Introduction

## 1.1 Objectives

* To review the ideas of computer science, programming, and problem-solving.
* To understand abstraction and the role it plays in the problem-solving process.
* To understand and implement the notion of an abstract data type.
* To review the Python programming language.

## 1.2 Getting Started

The science of computing is concerned with using computers to solve problems. This chapter emphasizes two important areas for the rest of the text. First, it reviews the framework within which computer science and the study of algorithms and data structures must fit, in particular, the reasons why we need to study these topics and how understanding these topics helps us to become better problem solvers. Second, we review the Python programming language.

## 1.3 What is Computer Science?

Computer science is the study of problems, problem-solving, and the solutions that come out of the problem-solving process.

We can fully define computer science, then, by including both types of problems and stating that computer science is the study of solutions to problems as well as the study of problems with no solutions.

It is also very common to include the word computable when describing problems and solutions. We say that a problem is computable if an algorithm exists for solving it. An alternative definition for computer science, then, is to say that computer science is the study of problems that are and that are not computable, the study of the existence and the nonexistence of algorithms.

* Abstraction

* Physical View / Logical View

* Interface

* Client

* Procedural Abstraction / Data Abstraction

## 1.4 What is Programming?

**Subchapter 1.4 provides easy-to-read and insightful explanation for Programming, Data Structure, and Algorithm at least for me. There's nothing to dump, no waste.**

## 1.5 Why We Study Data Structures and Abstract Data Types?

To manage the complexity of problems and the problem-solving process, computer scientists use abstractions to allow them to focus on the “big picture” without getting lost in the details. By creating models of the problem domain, we are able to utilize a better and more efficient problem-solving process. These models allow us to describe the data that our algorithms will manipulate in a much more consistent way with respect to the problem itself.
An abstract data type, sometimes abbreviated ADT, is a logical description of how we view the data and the operations that are allowed without regard to how they will be implemented. This means that we are concerned only with what the data is representing and not with how it will eventually be constructed.

* data Abstraction

* encapsulation

* information hiding

* data structure

* implementation independent view

## 1.6 Why We Study Algorithms?

By considering a number of different algorithms, we can begin to develop pattern recognition so that the next time a similar problem arises, we are better able to solve it.

we can learn analysis techniques that allow us to compare and contrast solutions based solely on their own characteristics, not the characteristics of the program or computer used to implement them.

There will often be trade-offs that we will need to identify and decide upon. As computer scientists, in addition to our ability to solve problems, we will also need to know and understand solution evaluation techniques. In the end, there are often many ways to solve a problem. Finding a solution and then deciding whether it is a good one are tasks that we will do over and over again.

## 1.7 Review of Basic Python
"""

print("Algorithms and Data Structures")

"""## 1.8 Getting Started With Data

We stated above that Python supports the object-oriented programming paradigm. This means that Python considers data to be the focal point of the problem-solving process. In Python, as well as in any other object-oriented programming language, we define a class to be a description of what the data look like (the state) and what the data can do (the behavior). Classes are analogous to abstract data types because a user of a class only sees the state and behavior of a data item. Data items are called objects in the object-oriented paradigm. An object is an instance of a class.

* object

* class

* object-oriented programming language

### 1.8.1 Built-in Atomic Data Types

* two numeric classes: <kbd>int</kbd> and <kbd>float</kbd>

* the return of true division for integers is float: interaction between classes

```python
print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)

```
"""

print(2+3*4)
print((2+3)*4)
print(2**10)
print(6/3)
print(7/3)
print(7//3)
print(7%3)
print(3/6)
print(3//6)
print(3%6)
print(2**100)
# '//' operator in int class represents rounding-off
print(-7//3)
# '%' matches to '//': -7 = (-7//3) * 3 + (-7%3)
print(-7%3)

"""boolean data type is represented by <kbd>bool</kbd> class
* state: True and False
* operators: <kbd>and</kbd>, <kbd>or</kbd>,  and <kbd>not</kbd>
"""

print(True)
print(False)
print(False or True)
print(not(False or True))
print(True and True)

print(5==10)
print(10 > 5)
print((5 >= 1) and (5 <= 10))

"""identifier rules

* do not start with number

* can be any length

* possible to include underscore(_)

* better following camel case convention
"""

theSum = 0
print(theSum)

theSum = theSum + 1
print(theSum)

# dynamic characteristic of python
theSum = True
print(theSum)

"""### 1.8.2 Built-in Collection Data Types"""

# when Python evaluates a list, the list itself is returned
[1, 3, True, 6.5]

# in order to remember the list for later processing, its reference needs to be assigned to a variable
myList = [1,3,True,6.5]
print(myList)

# initialization
myList = [0] * 6
print(myList)

'''
One very important aside relating to the repetition operator is that the result is a repetition of references to the data objects in the sequence.

'''
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)

"""```python
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)
```
"""

myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2, 4.5)
print(myList)
print(myList.pop())
print(myList.pop(1))
print(myList)
myList.pop(2)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

range(10)

list(range(10))

range(5, 10)

list(range(5, 10))

list(range(5, 10, 2))

list(range(10, 1, -1))

#Strings

"David"

myName = "David"

myName[3]

myName * 2

len(myName)

myName

myName.upper()

myName.center(10)

myName.find('v')

myName.split('v')

"""* mutability: major difference between list and string

* tuples: immutable lists
"""

set()

{3, 6, "cat", 4.5, False}

mySet = {3,6,"cat",4.5,False}

mySet

capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
  print(capitals[k]," is the capital of ", k)

"""## 1.9 Input and Output"""

aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(), "and has length", len(aName))

print("Hello", "World", end="***")

sradius = input("Please enter the radius of the circle: ")
radius = float(sradius)
diameter = radius * 2

print("Hello, World")
print("Hello", "World")
print("Hello", "World", sep="*")
print("Hello", "World", end="*")

age = 30
print(aName, "is", age, "years old.")

"""A formatted string is a template in which words or spaces that will remain constant are combined with placeholders for variables that will be inserted into the string. For example, the statement"""

print("%s is %d years old" % (aName, age))

price = 24
item = "banana"
print("The %s costs %d cents" % (item, price))
print("The %+10s costs %5.2f cents" % (item, price))
print("The %+10s costs %10.2f cents"%(item,price))
itemdict = {"item": "banana", "price": 24}
print("The %(item)s costs %(price)7.1f cents" %itemdict)

print("Hello","World", sep="***")

"""## 1.10 Control Structures

As we noted earlier, algorithms require two important control structures: iteration and selection. Both of these are supported by Python in various forms. The programmer can choose the statement that is most useful for the given circumstance.

For iteration, Python provides a standard while statement and a very powerful for statement. The while statement repeats a body of code as long as a condition is true.
"""

counter = 1
while counter <= 5:
  print("Hello, World      iterNum=%d" % (counter))
  counter = counter + 1

for item in range(5):
  print(item ** 2)

wordlist = ['cat', 'dog', 'rabbit']
letterlist = []
for aword in wordlist:
  for aletter in aword:
    letterlist.append(aletter)
print(letterlist)

n = -7
if n < 0:
  print("Sorry, the value is negative")
else:
  print(math.sqrt(n))

# nested if-else selection construct
score = 81
if score >= 90:
  print("A")
else:
  if score >= 80:
    print("B")
  else:
    if score >= 70:
      print("C")
    else:
      print('F')

# alternative if-elif-else selection construct
score = 81
if score >= 90:
  print('A')
elif score >= 80:
  print('B')
elif socre >= 70:
  print('C')
else:
  print('F')

# single-way selection construct: if
import math
n = -80
if n<0:
   n = abs(n)
print(math.sqrt(n))

wordList = ['cat', 'dog', 'rabbit']
aLetterList = []
for aWord in wordList:
  for aLetter in aWord:
    aLetterList.append(aLetter)
singleCopyLetterList = list(set(aLetterList))
print(singleCopyLetterList)

"""**list comprehension** : an alternative method for creating a list that uses iteration and selection constructs

%%time
wordList = ['cat', 'dog', 'rabbit']
aLetterList = [aLetter for aWord in wordList for aLetter in aWord]

%%time
wordList = ['cat', 'dog', 'rabbit']
aLetterList = []
for aWord in wordList:
  for aLetter in aWord:
    aLetterList.append(aLetter)
"""

print(aLetterList)

aLetterList.count('k')

wordList = ['cat', 'dog', 'rabbit']
aLetterList = [aLetter for aWord in wordList for aLetter in aWord]

print(aLetterList)

singleLetterList = list(set(aLetterList))

print(singleLetterList)

"""## 1.11 Exception Handling

The other type of error, known as a logic error, denotes a situation where the program executes but gives the wrong result. This can be due to an error in the underlying algorithm or an error in your translation of that algorithm. In some cases, logic errors lead to very bad situations such as trying to divide by zero or trying to access an item in a list where the index of the item is outside the bounds of the list. In this case, the logic error leads to a runtime error that causes the program to terminate. These types of runtime errors are typically called exceptions.
"""

anumber = int(input("Please enter an integer "))
try:
  print(math.sqrt(anumber))
#except RuntimeError:
except ValueError:
  print("Bad Value for square root")
  print("Using absolute value instead")
  print(math.sqrt(abs(anumber)))

aNumber = int(input("Please enter an integer: "))
if aNumber < 0:
  raise RuntimeError("You can't use a negative number")
else:
  print(math.sqrt(aNumber))

"""## 1.12 Defining Functions"""

# Newton's method to approximate square root of a number
def squareRoot(n):
  
  root = n/2
  for k in range(20):
    root = (1/2) * (root + n / root)
    
  return root

# this method is quite accurate
print("%10.8f"% (squareRoot(9)))

targetString ="methinks it is like a weasel"
len(targetString)

import random
random.choice("abcdefghijklmnopqrstuvwxyz ")
del random

def createRandomStringOfLength(n):
  import random
  alphabetPlusSpace = "abcdefghijklmnopqrstuvwxyz "
  generatedString = ""
  for _ in range(n):
    generatedString += random.choice(alphabetPlusSpace)
  return generatedString

createRandomStringOfLength(28)

def scoreRandomlyGeneratedString(generatedString, target=targetString):
  maxScore = len(target)
  score = 0
  for i in range(len(target)):
    if generatedString[i] == target[i]:
      score += 1
  return score

def infiniteMonkeyExperiment(maxIteration=10000, target=targetString):
  iterationNumber = 1
  maxScore = len(target)
  done = False
  while iterationNumber <= maxIteration and not done:
    generatedString = createRandomStringOfLength(len(target))
    score = scoreRandomlyGeneratedString(generatedString)
    if score == maxScore:
      done = True
    if iterationNumber % 1000 == 0:
      print("Iteration number is %d, and score is %d" % (iterationNumber, score))
    iterationNumber += 1
  return done

infiniteMonkeyExperiment()

def hillClimbingExperiment(maxIterationNumber=10000, target="methinks it is like a weasel"):
  
  import random
  alphabetPlusSpace = "abcdefghijklmnopqrstuvwxyz "
  maxScore = len(target)
  listOfTargetString = list(target)
  bestListOfStringSoFar = list(createRandomStringOfLength(len(target)))
  score = scoreRandomlyGeneratedString(bestListOfStringSoFar)
  iterationNumber = 1
  
  if score == maxScore:
    done = True
    print("The experiment ends in iteration %d" % (iterationNumber))
    return True
  else:
    done = False
    
  while iterationNumber <= maxIterationNumber and not done:
    for i in range(maxScore):
      if bestListOfStringSoFar[i] != listOfTargetString[i]:
        bestListOfStringSoFar[i] = random.choice(alphabetPlusSpace)
    score = scoreRandomlyGeneratedString(bestListOfStringSoFar)
    if score == maxScore:
      print("The experiment ends in iteration %d" % (iterationNumber))
      done = True
      return done
    iterationNumber += 1
    if iterationNumber % 1000 == 0:
      print("Iteration number: %d, best list of string so far: %s, score: %d" % (iterationNumber, bestListOfStringSoFar, score))
      
  return done

hillClimbingExperiment()

def hillClimbingExperiment2(maxIterationNumber=10000, target="methinks it is like a weasel"):
  
  import random
  alphabetPlusSpace = "abcdefghijklmnopqrstuvwxyz "
  maxScore = len(target)
  listOfTargetString = list(target)
  bestListOfStringSoFar = list(createRandomStringOfLength(len(target)))
  score = scoreRandomlyGeneratedString(bestListOfStringSoFar)
  iterationNumber = 1
  
  if score == maxScore:
    done = True
    print("The experiment ends in iteration %d" % (iterationNumber))
    return True
  else:
    done = False
    
  while iterationNumber <= maxIterationNumber and not done:
    
    for i in range(maxScore):
      
      if bestListOfStringSoFar[i] != listOfTargetString[i]:
        bestListOfStringSoFar[i] = random.choice(alphabetPlusSpace)
        break
    
    score = scoreRandomlyGeneratedString(bestListOfStringSoFar)
    
    if score == maxScore:
      print("The experiment ends in iteration %d" % (iterationNumber))
      done = True
      return done
    
    iterationNumber += 1
    
    if iterationNumber % 1000 == 0:
      print("Iteration number: %d, best list of string so far: %s, score: %d" % (iterationNumber, bestListOfStringSoFar, score))
      
  return done

hillClimbingExperiment2()

"""## 1.13 Object-Oriented Programming in Python: Defining Classes

### 1.13.1 A Fraction Class
"""

class Fraction:
  
  # the constructor method is always called '__init__' in python
  def __init__(self, top, bottom):
    
    self.numerator = top
    self.denominator = bottom

myFraction = Fraction(3, 5)

print(myFraction)

print(myFraction)

id(myFraction)

class Fraction:
  
  # the constructor method is always called '__init__' in python
  def __init__(self, top, bottom):
    
    self.numerator = top
    self.denominator = bottom
    
  # customized show method
  def show(self):
    print(self.numerator, "/", self.denominator)

myFraction = Fraction(3, 5)
myFraction.show()

print(myFraction)

class Fraction:
  
  # the constructor method is always called '__init__' in python
  def __init__(self, top, bottom):
    
    self.numerator = top
    self.denominator = bottom
    
  # customized show method
  def show(self):
    print(self.numerator, "/", self.denominator)
  
  # override standard '__str__' method
  def __str__(self):
    return str(self.numerator) + "/" + str(self.denominator)

myFraction = Fraction(3, 5)
print(myFraction)
print("I only like", myFraction, "of Andy Kim")
str(myFraction)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f1 + f2

class Fraction:
  
  # the constructor method is always called '__init__' in python
  def __init__(self, top, bottom):
    
    self.numerator = top
    self.denominator = bottom
    
  # customized show method
  def show(self):
    print(self.numerator, "/", self.denominator)
  
  # override standard '__str__' method
  def __str__(self):
    return str(self.numerator) + "/" + str(self.denominator)
  
  # override standard addition method
  def __add__(self, otherFraction):
    newTop = self.numerator * otherFraction.denominator + otherFraction.numerator * self.denominator
    newBottom = self.denominator * otherFraction.denominator
    
    return Fraction(newTop, newBottom)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)

def gcd(m,n):
  while m % n != 0:
    oldM = m
    oldN = n
    
    m = oldN
    n = oldM % oldN
    
  return n


class Fraction:
  
  # the constructor method is always called '__init__' in python
  def __init__(self, top, bottom):
    
    self.numerator = top
    self.denominator = bottom
    
  # customized show method
  def show(self):
    print(self.numerator, "/", self.denominator)
  
  # override standard '__str__' method: in lowest forms
  def __str__(self):
    common = gcd(self.numerator, self.denominator)
    return str(int(self.numerator / common)) + "/" + str(int(self.denominator / common))
  
  # override standard addition method
  def __add__(self, otherFraction):
    newTop = self.numerator * otherFraction.denominator + otherFraction.numerator * self.denominator
    newBottom = self.denominator * otherFraction.denominator
    
    return Fraction(newTop, newBottom)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)

"""* shallow equality / deep equality"""

def gcd(m,n):
  while m % n != 0:
    oldM = m
    oldN = n
    
    m = oldN
    n = oldM % oldN
    
  return n


class Fraction:
  
  # the constructor method is always called '__init__' in python
  def __init__(self, top, bottom):
    
    self.numerator = top
    self.denominator = bottom
    
  # customized show method
  def show(self):
    print(self.numerator, "/", self.denominator)
  
  # override standard '__str__' method: in lowest forms
  def __str__(self):
    common = gcd(self.numerator, self.denominator)
    return str(int(self.numerator / common)) + "/" + str(int(self.denominator / common))
  
  # override standard addition method
  def __add__(self, otherFraction):
    newTop = self.numerator * otherFraction.denominator + otherFraction.numerator * self.denominator
    newBottom = self.denominator * otherFraction.denominator
    
    return Fraction(newTop, newBottom)
  
  # implement deep equality by overriding standard equality method
  def __eq__(self, otherFraction):
    
    return self.numerator * otherFraction.denominator == self.denominator * otherFraction.numerator

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)

def gcd(m,n):
  while m % n != 0:
    oldM = m
    oldN = n
    
    m = oldN
    n = oldM % oldN
    
  return n


class Fraction:
  
  # the constructor method is always called '__init__' in python
  def __init__(self, top, bottom):
    
    self.numerator = top
    self.denominator = bottom
    
  # customized show method
  def show(self):
    print(self.numerator, "/", self.denominator)
  
  # override standard '__str__' method: in lowest forms
  def __str__(self):
    common = gcd(self.numerator, self.denominator)
    return str(int(self.numerator / common)) + "/" + str(int(self.denominator / common))
  
  # override standard addition method
  def __add__(self, otherFraction):
    newTop = self.numerator * otherFraction.denominator + otherFraction.numerator * self.denominator
    newBottom = self.denominator * otherFraction.denominator
    
    return Fraction(newTop, newBottom)
  
  # implement deep equality by overriding standard equality method
  def __eq__(self, otherFraction):
    
    return self.numerator * otherFraction.denominator == self.denominator * otherFraction.numerator
  
  # implement '*', '/', and '-' operation for our Fraction class
  def __mul__(self, other):
    return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
  
  def __div__(self, other):
    return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
  
  def __sub__(self, other):
    return Fraction(self.numerator * otherFraction.denominator - otherFraction.numerator * self.denominator, self.denominator * other.denominator)
  
  # implement logical operators '>', '<', '>=', and '<='
  def __gt__(self, other):
    return self.numerator * other.denominator - other.numerator * self.denominator > 0
  
  def __lt__(self, other):
    return self.numerator * other.denominator - other.numerator * self.denominator < 0
  
  def __ge__(self, other):
    return self.numerator * other.denominator - other.numerator * self.denominator >= 0

  def __le__(self, other):
    return self.numerator * other.denominator - other.numerator * self.denominator <= 0

f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
print(f1 > f2)

f1 <= f2

"""### 1.13.2 Inheritance: Logic Gates and Circuits"""

class LogicGate:
  
  def __init__(self, n):
    self.label = n
    self.output = None
    
  def getLabel(self):
    return self.label
  
  def getOutput(self):
    self.output = self.performGateLogic()
    return self.output

class BinaryGate(LogicGate):
  
  def __init__(self, n):
    LogicGate.__init__(self, n)
    
    self.pinA = None
    self.pinB = None
    
  
  def getPinA(self):
    if self.pinA == None:
      return int(input("Enter Pin A for gate " + self.getLabel() + "-->"))
    else:
      return self.pinA.fromgate.getOutput()
    
  def getPinB(self):
    if self.pinB == None:
      return int(input("Enter Pin B for gate " + self.getLabel() + "-->"))
    else:
      return self.pinB.fromgate.getOutput()

class UnaryGate(LogicGate):

  def __init__(self,n):
    LogicGate.__init__(self,n)

    self.pin = None

  def getPin(self):
    if self.pin == None:
      return int(input("Enter Pin for gate " + self.getLabel() + "-->"))
    else:
      return self.pin.fromgate.getOutput()

class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0
          
    def setNextPin(self,source):
      if self.pinA == None:
          self.pinA = source
      else:
          if self.pinB == None:
              self.pinB = source
          else:
             raise RuntimeError("Error: NO EMPTY PINS")

g1 = AndGate("G1")
g1.getOutput()

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        
        if a==1 or b==1:
            return 1
        else:
            return 0
          
    def setNextPin(self,source):
      if self.pinA == None:
          self.pinA = source
      else:
          if self.pinB == None:
              self.pinB = source
          else:
             raise RuntimeError("Error: NO EMPTY PINS")

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPin()
        if a==0:
            return 1
        else:
            return 0
          
    def setNextPin(self,source):
      if self.pin == None:
          self.pin = source
      else:
        raise RuntimeError("Error: NO EMPTY PIN")

g2 = OrGate("G2")

g2.getOutput()

g3 = NotGate("G3")
g3.getOutput()

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

class NandGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1
          
    def setNextPin(self,source):
      if self.pinA == None:
          self.pinA = source
      else:
          if self.pinB == None:
              self.pinB = source
          else:
             raise RuntimeError("Error: NO EMPTY PINS")

class NorGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 0
        else:
            return 1
          
    def setNextPin(self,source):
      if self.pinA == None:
          self.pinA = source
      else:
          if self.pinB == None:
              self.pinB = source
          else:
             raise RuntimeError("Error: NO EMPTY PINS")

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

g4.getOutput()

g1 = AndGate("G1")
g2 = NotGate("G2")
g3 = AndGate("G3")
g4 = NotGate("G4")
g5 = AndGate("G5")
c1 = Connector(g1, g2)
c2 = Connector(g3, g4)
c3 = Connector(g2, g5)
c4 = Connector(g4, g5)

g5.getOutput()