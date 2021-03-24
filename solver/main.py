from solver import *
from constant import OG
# s = Solver3x3(OG) # (48, ~1.6e7)
# s = Solver3x3_OS(OG) # (8, 2 501 456)
s = Solver3x3_OS_SY(OG) # (2, 251 129)
# s = Solver3x3_OS_SY_BI(OG) # (2, 112 333) But much slower
print(s.solve())