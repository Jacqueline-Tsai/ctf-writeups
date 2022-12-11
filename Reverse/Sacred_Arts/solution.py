import math

qword = [0x8D909984B8BEBAB3, 0x8D9A929E98D18B92, 0x0D0888BD19290D29C, 0x8C9DC08F978FBDD1, 
        0x0D9C7C7CCCDCB92C2, 0x0C8CFC7CEC2BE8D91, 0x0FFFFFFFFFFFFCF82]

for val in qword:
    exch_val = ((val >> 16) << 16) + (val >> 8) % (1 << 8) + val % (1 << 8) * (1 << 8)
    flag = (1 << 64) - exch_val
    print(flag.to_bytes(math.ceil(math.log(flag, 256)), 'big').decode("utf-8")[::-1], end='')