# TDD 101

---

# Testing

- Testing verifies that the system meets the different requirements including,
functional, performance, reliability, security, usability, and so on.

- [https://en.wikipedia.org/wiki/Portal:Software_testing](https://en.wikipedia.org/wiki/Portal:Software_testing)

---

# Unit Testing

- Low level testing of individual software "units"

- In OOP units tend to be classes

- Executing unit tests should be fast

- Done using frameworks

---

# xUnit Frameworks

- Originally in Smalltalk by Kent Beck

- JUnit for Java

- [unittest](https://docs.python.org/3.4/library/unittest.html) in Pyhton

- AAA: Arrange, Act, Assert

---

# Test Cases

    !python
    import unittest

    import poker


    class TestPokerGame(unittest.TestCase):

        def setUp(self):
            self.game = poker.Game()

        def test_card_name(self):
            name = self.game.card_name("AS")
            self.assertEqual("Ace of Spades", name)

        def tearDown(self):
            self.game.game_over()

---

# Run the test suite

    !bash
    python -m unittest test_poker.py

    E
    ======================================================================
    ERROR: test_card_name (test_poker.TestPokerGame)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/doug1088/Workspaces/Playground/test_poker.py", line 12, in test_card_name
          name = self.game.card_name("AS")
    TypeError: card_name() takes 1 positional argument but 2 were given

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

---

# Run the test suite

    !bash
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

---

# Test-Driven Development

- Technique for building software that guides software development by writing
tests

- Develop sofware by following these steps:
    - Write test for the next piece of functionality you want to add
    - Write functional code to make the test pass
    - Refactor new and old functional code to make it well structured

- Red, Green, Refactor

---

# Code Kata

- In martial arts, a Kata is a series of basic movements

- Code Katas are "practice sessions" for programmers

---

# Roman Numeral Kata

- Convert arabic numbers (1, 2, 3, 4...) into Roman Numerals (I, II, III, IV...)

---

# Dojo Time!

---

# Further Reading

- [Test Driven Development By Example - Kent Beck](http://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_1?ie=UTF8&qid=1425576992&sr=8-1&keywords=kent+beck)

- [UnitTest - Martin Fowler](http://martinfowler.com/bliki/UnitTest.html)

- [Xunit - Martin Fowler](http://martinfowler.com/bliki/Xunit.html)

- [codekata.com](http://codekata.com/)
