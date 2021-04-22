from Turing_machine import Turing_machine 






















#Testing
MT = Turing_machine()
print(MT.table)
MT.add_symbol('0')
MT.add_symbol('1')
MT.add_symbol('Z')
MT.replace_command(4, '0', 'Z>12')
print(MT.table)
print(MT.alphabet)