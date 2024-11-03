# Encoding and Decoding a string with simple scheme

This exercise intended to teach you what encoding and decoding is and how to implement an overly simplified version of it.
See answers/question-1.py for the solution.

#### Additional Learning
Run length encoding (RLE) is a compression technique with a brute-force simplicity. 
It works by replacing a sequence of identical values with a single value and a count. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

This technique and/or variants of this technique is used in many compression algorithms.
- https://www.sciencedirect.com/topics/computer-science/run-length-encoding


#### Solution to Puzzle
- The encoding scheme will work only if characters are repeated 2-9 times, beyond that it will fail
- The answer in answers/question-1.py is for a simple case where the characters are repeated 2-9 times
- Enhance the program to handle cases where characters are repeated more than 9 times
  - There are many potential solutions to this problem  
  - Repeat the # Symbol for Multiples of 10
    - #count[char]#count[char]#count[char]... (eg: #9Y#9Y#3Y)
  - Prefix-Based Encoding with Special Separator (| or -)
    - #count[-|@][char] (eg: #100-Y or #100|Y or #100@Y)
    - #<count>[char] (eg: #<21>Y)
  - Delimiter-Based Encoding
    - #-count-[char] (eg: #-100-Y)
  - Hexadecimal Representation for Large Counts
    - #0xHEX[char] (eg: #0x64-Y)
  - 
#### What you should have additionally learnt from this exercise:
- How to write simple testcase in Python
  - Testcases are used to check if your program is working as expected
  - Testcases are written in the form of assert statements
  - If the assert statement fails, the program will throw an error
  - This is very simplified form of writing tests for simple programs, advanced testcases will be covered in later exercises
- How to name variables and functions (some of these are not covered in the example)
  - Use descriptive names, do not use variables like a,b,c, i,j,k, x,y,z etc
  - Use snake_case for naming variables and functions
  - Use CamelCase for naming classes
  - Use UPPERCASE for naming constants
  - Use lowercase for naming modules
  - Use leading underscore for naming private variables and functions
  - Use trailing underscore for naming variables that are already taken by Python keywords
- How to create docstring
  - Used to describe what the function does
  - Used by IDEs to show the function description
  - Used by Python's help() function to show the function description
  - Used by Sphinx to generate documentation
    - https://www.sphinx-doc.org/en/master/
    - https://docs.readthedocs.io/en/stable/intro/sphinx.html
    - [Examples of famous Python libraries](https://www.sphinx-doc.org/en/master/examples.html)
      - Refer: Requests, Beautiful Soup, OpenCV, Django, scikit-learn etc
  - These are extremely useful in large projects and if others are using/enhancing your code
  - Always write docstrings for all functions and classes, even if it is a simple one-liner

