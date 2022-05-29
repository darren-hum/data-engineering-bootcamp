import sys
import pandas as pd

print(sys.argv)
#sys.argv[1] is the first param passed; [0] is the script name
day = sys.argv[1]


print(f'job completed successfully for day = {day}')