import os
import sys
print(__file__)#相对路径
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

Base_Dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(Base_Dir)
sys.path.append(Base_Dir)
from Scrapy.function.func_test1 import func2
func2()