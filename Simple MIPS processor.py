import sys

mem = []
mem = [0 for i in range(0,33)]

reg = []
reg = [0 for q in range(0,33)]

#registries write & read
def readReg(RegNum):
    x = reg[RegNum]
    return x

def writeReg(RegNum, valReg):
    reg[RegNum] = valReg
     

#memories write & read
def writeMem(MemNum, valMem):
    mem[MemNum] = valMem
    

def readMem(MemNum):
    y = mem[MemNum]
    return y

def start():
    print('Welcome to our single-cycle simple MIPS Processor!')
    op = input('Please enter your instruction:  ')
    op = op.upper()

    if op == ("ADD"):
        opcode=32
        functype='R'
    elif op == ("ADDI") :
        opcode=8
        functype='I'
    elif op == ("SUB"):
        opcode = 34
        functype='R'
    elif op == ("AND") :
        opcode=32
        functype='R'
    elif op == ("ANDI") :
        opcode = 36
        functype='I'
    elif op == ("OR") :
        opcode=37
        functype='R'
    elif op == ("ORI") :
        opcode = 13
        functype='I'
    elif op == ("NOR"):
        opcode = 39
        functype='R'
    elif op == ("SLT"):
        opcode = 42
        functype='R'
    elif op ==  ("LW"):
        opcode = 32
        functype='B'
    elif op ==  ("SW"):
        opcode = 34
        functype='B'
    else:
        print('Please enter one of the following instructions: Add, Addi, Sub, And, Andi, Ori, Nor, Slt, LW, SW')
        print('Thank you!')
        sys.exit()
    
    
    if functype == ('R'):
        rs = input('Please enter your desired rs:  ')
        rs.upper()
        rt = input('Please enter your desired rt:  ')
        rt.upper()
        rd = input('Please enter your desired rd:  ')
        rd.upper()
    elif functype == ('B'):
        rs = input('Please enter your desired rs:  ')
        rd = input('Please enter your desired rd:  ')
        offs = input('Please enter your desired offset:  ')
    else: ##I Type
        rs = input('Please enter your desired rs:  ')
        rs.upper()
        rt = input('Please enter your desired rt:  ')
        rt.upper()
        imm = input('Please enter your desired immediate value:  ')
        imm = int(imm)
    
##Execution of ALU
    if op == ("ADD"):
        readReg(int(rt))
        readReg(int(rd))
        reg[int(rs)]  = reg[int(rt)] + reg[int(rd)]
        print('Instr Executed :  ' + op + ' $' + rs + ', $ ' + rt + ', $ ' + rd)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' $' + bin(int(rs)) + ', $ ' + bin(int(rt)) + ', $ ' + bin(int(rd)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ') 
        print(reg)
    
    if op == ("ADDI"):
        readReg(int(rt))
        reg[int(rs)]  = reg[int(rt)] + int(imm)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' ' + bin(int(rs)) + ',  ' + bin(int(rt)) + ',  ' + bin(int(imm)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)
        
    if op == ("LW"):
        reg[int(rs)]=readMem(readReg(int(rd)))+int(offs)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' ' + bin(int(rs)) + ',  ' + bin(int(offs)) + '(' + bin(int(rd))+')')
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)

    if op == ("SW"):
        mem[int(rd)+int(offs)]=readReg(int(rs))
        print('Instr Executed in Binary :  ' + bin(opcode) + ' ' + bin(int(rs)) + ',  ' + bin(int(offs)) + '(' + bin(int(rd))+')')
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)
        
    if op == ("SUB"):
        readReg(int(rt))
        readReg(int(rd))
        reg[int(rs)]  = reg[int(rt)] - reg[int(rd)]
        print('Instr Executed :  ' + op + ' $' + rs + ', $' + rt + ', $' + rd)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' $' + bin(int(rs)) + ', $' + bin(int(rt)) + ', $' + bin(int(rd)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)

    if op == ("AND"):
        readReg(int(rt))
        readReg(int(rd))
        reg[int(rs)]  = reg[int(rt)] & reg[int(rd)]
        print('Instr Executed :  ' + op + ' $' + rs + ', $' + rt + ', $' + rd)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' $' + bin(int(rs)) + ', $' + bin(int(rt)) + ', $' + bin(int(rd)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)
        

    if op == ("ANDI"):
        readReg(int(rt))
        reg[int(rs)]  = reg[int(rt)] & int(imm)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' ' + bin(int(rs)) + ',  ' + bin(int(rt)) + ',  ' + bin(int(imm)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)

    if op == ("OR"):
        readReg(int(rt))
        readReg(int(rd))
        reg[int(rs)]  = reg[int(rt)] | reg[int(rd)]
        print('Instr Executed :  ' + op + ' $' + rs + ', $' + rt + ', $' + rd)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' $' + bin(int(rs)) + ', $' + bin(int(rt)) + ', $' + bin(int(rd)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)

    if op == ("ORI"):
        readReg(int(rt))
        reg[int(rs)]  = reg[int(rt)] | int(imm)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' ' + bin(int(rs)) + ',  ' + bin(int(rt)) + ',  ' + bin(int(imm)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)
    
    if op == ("NOR"):
        readReg(int(rt))
        readReg(int(rd))
        reg[int(rs)]  = reg[~int(rt)] | reg[~int(rd)]
        print('Instr Executed :  ' + op + ' $' + rs + ', $' + rt + ', $' + rd)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' $' + bin(int(rs)) + ', $' + bin(int(rt)) + ', $' + bin(int(rd)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)

    if op == ("SLT"):
        readReg(int(rt))
        readReg(int(rd))
        if  reg[int(rt)] < reg[~int(rd)]:
            reg[int(rs)]  = 1
        else:
            reg[int(rs)]  = 0
        print('Instr Executed :  ' + op + ' $' + rs + ', $' + rt + ', $' + rd)
        print('Instr Executed in Binary :  ' + bin(opcode) + ' $' + bin(int(rs)) + ', $' + bin(int(rt)) + ', $' + bin(int(rd)))
        print('Memory Values:  ')
        print(mem)
        print('Registry Values:  ')
        print(reg)
        
    dec = input('Do you want to run another instruction? Type Yes / No:   ')
    dec.lower()
    if dec == 'yes':
        start()
    elif dec == 'no':
        sys.exit()
    else:
        print('Unsupported reply. Please choose yes/no...    ')
        start()
        
start()

#writeReg(4, 5)
#readReg(4)

##This Coding is made by BUiD Students group that consists of: AhmedAlHelwany, Abdullah Elabora, Kinan, Naser, Jameela, and Rashed.