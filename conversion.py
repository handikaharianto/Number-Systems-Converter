from functools import reduce

class Conversion:
    def binary_to_decimal(self, entry_field):
        if any(element not in ['0', '1'] for element in entry_field):
            return None
        
        binary = int(entry_field)
        decimal, i = 0, 0
        while binary != 0:
            last_digit = binary % 10
            decimal = decimal + last_digit * pow(2, i)
            binary //= 10
            i += 1
        return decimal

    def binary_to_hexa(self, entry_field):
        decimal = self.binary_to_decimal(entry_field)

        if decimal == None:
            return None
        
        return hex(decimal).upper().replace("X", "x")

    def binary_to_octal(self, entry_field):
        decimal = self.binary_to_decimal(entry_field)

        if decimal == None:
            return None
        
        return oct(decimal).replace("0o", "")

    def decimal_to_binary(self, entry_field):
        try:
            decimal = int(entry_field)
        except (ValueError, TypeError):
            return None
        else:
            if decimal == 0:
                return decimal

            i = 0
            binary = ""
            while decimal != 0:
                remainder = decimal % 2
                decimal //= 2
                binary = str(remainder) + binary
            return binary

    def decimal_to_hexa(self, entry_field):
        hexa_table = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        try:
            decimal = int(entry_field)
        except (ValueError, TypeError):
            return None
        else:
            hexadecimal = ""
            while decimal != 0:
                remainder = decimal % 16
                hexadecimal = hexa_table[remainder] + hexadecimal
                decimal //= 16
            return f"0x{hexadecimal}"

    def decimal_to_octal(self, entry_field):
        try:
            decimal = int(entry_field)
        except (ValueError, TypeError):
            return None
        else:
            octal = ""
            while decimal != 0:
                remainder = decimal % 8
                octal = str(remainder) + octal
                decimal //= 8
            return octal
    
    def hexa_to_binary(self, entry_field):
        entry_field = entry_field.strip()

        decimal = self.hexa_to_decimal(entry_field)
        
        binary = self.decimal_to_binary(decimal)

        if binary == None:
            return None

        return binary
    
    def hexa_to_decimal(self, entry_field):
        entry_field = entry_field.strip()

        hexa_table = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15
        }

        if entry_field.isalnum() == False:
            return None

        if entry_field[:2].lower() == '0x' and len(entry_field) == 2:
            return None
        elif entry_field[:2].lower() == '0x' and len(entry_field) > 2:
            entry_field = entry_field[2:]

        if entry_field.isalnum() and any(element.upper() not in hexa_table for element in entry_field):
            return None

        hex_list = list(entry_field)
        for i, num in enumerate(hex_list):
            num = num.upper()
            if num in hexa_table:
                hex_list[i] = hexa_table[num]
        
        int_list = list(map(int, hex_list))
        return reduce(lambda x, y: x * 16 + y, int_list)
    
    def hexa_to_octal(self, entry_field):
        decimal = self.hexa_to_decimal(entry_field)

        octal = self.decimal_to_octal(decimal)
        if octal == None:
            return None
        return octal

    def octal_to_binary(self, entry_field):
        decimal = self.octal_to_decimal(entry_field)

        binary = self.decimal_to_binary(decimal)

        if binary == None:
            return None
        return binary

    def octal_to_decimal(self, entry_field):
        octal_num = ['0', '1', '2', '3', '4', '5', '6', '7']

        if any(element not in octal_num for element in entry_field):
            return None

        octal = int(entry_field)
        decimal = 0
        base = 1
        while octal:
            last_digit = octal % 10
            octal //= 10
            decimal += last_digit * base
            base *= 8
        return decimal
        
    def octal_to_hexa(self, entry_field):
        decimal = self.octal_to_decimal(entry_field)

        hexa = self.decimal_to_hexa(decimal)

        if hexa == None:
            return None
        
        return hexa