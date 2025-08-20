# created on Wed Aug 20 02:32:06 2025
# python 3
# utf-8
# @author: CombatWorthyWombat

# Self-made Base64 Decoder/Encoder (can be modified to work with alternative alphabets)

A_Z = [chr(i) for i in range(65, 91)]
a_z = [chr(i) for i in range(97, 123)]
zero_nine = [chr(i) for i in range(48, 58)]
additional_chars = ['+', '/']

def to_b64(string: str):

    b64_symbols = A_Z + a_z + zero_nine + additional_chars

    binary = []
    for char in string:
        binary.append(bin(ord(char)).split("b")[-1].rjust(8,'0'))

    binary = "".join(binary)

    six_bit = []

    while len(binary):
        six_bit.append(binary[0:6])
        binary = binary[6:]

    # padding for last six bit item
    six_bit[-1] = six_bit[-1].ljust(6, '0')


    result = ""
    for byte in six_bit:
        index = int(byte, 2)
        result = result + b64_symbols[index]

    # padding
    def get_multiple_of_4(num):

        while num % 4 != 0:
            num += 1
        return num
    result = result.ljust(get_multiple_of_4(len(result)),'=')
    
    return result


def from_b64(b64_string: str):

    b64_symbols = A_Z + a_z + zero_nine + additional_chars

    b64_string = b64_string.strip("=")

    index = []
    for char in b64_string:
        position = b64_symbols.index(str(char))
        index.append(position)
        
    binary = []
    for i in index:
        binary.append(bin(i).split("b")[-1].rjust(6, '0'))
        
    binary = "".join(binary)
    
    byte_data = []
    while len(binary):
        byte_data.append(binary[0:8])
        binary = binary[8:]
        

    result = ""
    for i in byte_data:
        result = result + chr(int(i, 2))
            
    return result
