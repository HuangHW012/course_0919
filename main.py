def char2utf8(input_character):
    input_unicode = ord(input_character)
    input_binary = bin(input_unicode)
    input_binary_without_0b = input_binary[2:]
    if len(input_binary_without_0b) <= 7:
        return hex(input_unicode)
    else:
        z = input_binary_without_0b[-6:]
        if len(input_binary_without_0b) <= 11:
            pass
        else:
            y = input_binary_without_0b[-12:-6]
            if len(input_binary_without_0b) <= 16:
                x = input_binary_without_0b[-16:-12]
                input_utf8 = '0b1110{:0>4}10{}10{}'.format(x, y, z)
                #input_utf8 = '0b1110' + '0' * (4 - len(x)) + x + '10' + y + '10' + z
                return hex(int(input_utf8, 2))
            else:
                pass


print(char2utf8('台'))
print(char2utf8('中'))
print(char2utf8('市'))