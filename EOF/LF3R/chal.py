import random

from secret import FLAG

class lfsr:
    def __init__(self, tap, state):
        assert len(state) == 32
        self._tap = tap
        self._state = state

    def getbit(self):
        f = sum([self._state[i] for i in self._tap]) & 1
        x = self._state[0]
        self._state = self._state[1:]
        return f, x

    def addbit(self, b):
        self._state.append(b)

class Cipher:
    def __init__(self, t1, t2, t3):
        self.lfsr1 = lfsr(t1, [random.randrange(2) for _ in range(32)])
        self.lfsr2 = lfsr(t2, [random.randrange(2) for _ in range(32)])
        self.lfsr3 = lfsr(t3, [random.randrange(2) for _ in range(32)])
    
    def getbit(self):
        f1, output = self.lfsr1.getbit()
        f2, _ = self.lfsr2.getbit()
        f3, _ = self.lfsr3.getbit()
        self.lfsr1.addbit(f2)
        self.lfsr2.addbit(f3)
        self.lfsr3.addbit(f1)
        return output

def get_tap(x):
    tap = []
    for i in range(32):
        if x & (1 << i):
            tap.append(i)
    return tap

t1 = get_tap(random.randrange(1 << 32))
t2 = get_tap(random.randrange(1 << 32))
t3 = get_tap(random.randrange(1 << 32))
cipher = Cipher(t1, t2, t3)

flag = list(map(int, ''.join(["{:08b}".format(c) for c in FLAG])))
output = []

for b in flag:
    output.append(cipher.getbit() ^ b)

for _ in range(300):
    output.append(cipher.getbit())

print("output = ", output)