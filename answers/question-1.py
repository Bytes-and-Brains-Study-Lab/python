
def encode_string(input_: str):
    """
    Encode a string using a custom encoding scheme.
    If a character repeats consecutively two or more times, encode it in the format #count[char]

    Parameters
    ----------
    input_: str
        The input string to encode

    Returns
    -------
    str
        The encoded string
    """

    encoded: list[str] = []
    index: int = 0

    # Iterate through the string, char by char
    while index < len(input_):
        current_char = input_[index]
        char_count: int = 1
        # If next char is the same as the current char and increment char_count and index
        while index + 1 < len(input_) and input_[index + 1] == current_char:
            char_count += 1
            index += 1

        # If the character is '#', encode it as '##'
        if current_char == '#':
            encoded.append(f"#{char_count}##")
        # If the char_count is greater than 1, encode it as '#char_count[char]'
        elif char_count >= 2:
            encoded.append(f"#{char_count}{current_char}")
        # Do not encode single char, output as-is
        else:
            encoded.append(current_char)

        # Move to next distinct character
        index += 1

    return "".join(encoded)


def decode_string(input: str):
    """
    Decode a string that was encoded using the custom encoding scheme.

    Parameters
    ----------
    input: str
        The input string to decode

    Raises
    ------
    ValueError
        Invalid encoding format

    Returns
    -------
    str
        The decoded string
    """

    decoded: list[str] = []
    index: int = 0
    str_length: int = len(input)

    # Iterate through the encoded string character by character
    while index < str_length:

        current_char: str = input[index]
        next_char: str = input[index + 1] if index + 1 < str_length else None

        if input[index] == '#':  # Check if the character is '#'

            # Check if next char is an integer
            if next_char and not next_char.isdigit():
                raise ValueError("Invalid encoding format!")

            # Extract the character count
            char_count: int = int(next_char)

            # Check if char after count exists and we do not move past the end of the string
            if index + 2 >= str_length:
                raise ValueError("Invalid encoding format!")

            if index + 3 < str_length and input[index + 2: index + 4] == '##':  # Check for '##'
                current_char = '#'
                index += 4  # Move past '##'
            else:
                current_char = input[index + 2]
                index += 3  # Move past the count & char

            decoded.append(current_char * char_count)

        else:
            # Append the character as-is if it's not part of an encoding
            decoded.append(current_char)
            index += 1

    return "".join(decoded)

# Test case
original_string = "YYYYYYY00000000%%2222222203333333300YZ######4444444"
print("Original String:", original_string)
encoded = encode_string(original_string)
print("Encoded:", encoded)
decoded = decode_string(encoded)
print("Decoded:", decoded)

assert original_string == decoded, "The decoded string does not match the original!"