def xor_operation(dividend, key):
    """Perform XOR between dividend and key for CRC."""
    result = []
    for i in range(len(key)):
        result.append('0' if dividend[i] == key[i] else '1')
    return ''.join(result)

def crc(data, key):
    """Calculate the CRC remainder for the given data and key."""
    data_length = len(data)
    key_length = len(key)

    # Append zeros to the dividend (data)
    dividend = data + '0' * (key_length - 1)

    # Perform division using XOR
    for i in range(data_length):
        if dividend[i] == '1':
            dividend = dividend[:i] + xor_operation(dividend[i:], key) + dividend[i + key_length:]

    # Return the remainder (last part of the dividend)
    return dividend[data_length:]

def check_for_errors(received_data, key):
    """Check if there are any errors in the received data using CRC."""
    remainder = crc(received_data, key)
    # If the remainder contains any '1', an error is detected
    return '1' in remainder

def main():
    # Input the data and key
    data = input("Enter data word (binary): ")
    key = input("Enter key (binary): ")

    # Generate the CRC remainder at the sender side
    crc_result = crc(data, key)
    print(f"CRC Remainder at Sender Side: {crc_result}")

    # Create the transmitted data (data + CRC remainder)
    transmitted_data = data + crc_result
    print(f"Transmitted codeword (data + remainder): {transmitted_data}")

    # Receiver side
    received_data = input("\nReceiver Side\nEnter received data (binary): ")

    # Check CRC remainder at the receiver side
    remainder = crc(received_data, key)
    print(f"CRC Remainder at Receiver Side: {remainder}")

    # Check for errors
    if check_for_errors(received_data, key):
        print("Since remainder is non-zero, error detected in received data!")
    else:
        print("Since remainder is zero, there is no error detected in received data.")

if __name__ == "__main__":
    main()
