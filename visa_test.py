import pyvisa as visa
rm = visa.ResourceManager('@py')
#print(rm.list_resources())  # bug, see https://github.com/pyvisa/pyvisa-py/issues/282

instr = rm.open_resource('GPIB0::6::INSTR')

instr.write('EOI ON')   # by default, EOI is OFF when counter is switched ON.
instr.read_termination = '\n'  # from github https://github.com/pyvisa/pyvisa-py/issues/283
instr.write_termination = '\n'

instr.write('ID?')
print(instr.read_raw())

instr.close()
