# Encoding and Decoding a string with simple scheme

In an encoding scheme when characters are consecutive, it must be shortened by encoding it with #count[char]<br>
Eg: the character string YYYYY, is expressed as #5Y.<br>
If a character repeats consecutively two or more times, encode it in the format #count[char]. If # is present in the string, encode it as ##.<br>
Write a program that has 2 functions, one for encoding and one for decoding<br>
Input: `XYZZZZZZ10000%2%%13`<br>
Output: `XY#6Z1#40%2#2%13`

Hint: Write a test case as shown below in your program

## Test Case
```python
original_string = "YYYYYYY00000000%%2222222203333333300YZ######4444444"
print("Original String:", original_string)
encoded = encode_string(original_string)
print("Encoded:", encoded)
decoded = decode_string(encoded)
print("Decoded:", decoded)

assert original_string == decoded, "The decoded string does not match the original!"
```

## Puzzle
Also think of cases where your program will not work properly. 
Hint: Will it work for all kinds of input ?
