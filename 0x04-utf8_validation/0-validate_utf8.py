#!/usr/bin/python3
"""
  Determines if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate through each byte in the data
    for byte in data:
        # Get only the least significant 8 bits of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            """ 
               Check the number of leading 1's to determine the number
               of bytes in this UTF-8 character
            """
            if (byte >> 5) == 0b110:  # 110xxxxx -> 2 bytes
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx -> 3 bytes
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx -> 4 bytes
                num_bytes = 3
            elif (byte >> 7):  # 1xxxxxxx -> Invalid for a single byte
                return False
        else:
            # Check if it is a continuation byte (starts with 10xxxxxx)
            if not (byte >> 6 == 0b10):
                return False
            num_bytes -= 1

    return num_bytes == 0

