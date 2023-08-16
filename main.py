# This is a sample Python script.
import pandas
import math
import numpy
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arr = [-4.28966245711595,1.14507650781293,-5.17385997917229,-3.34912337481094,1.6163991289095]
    print("一维数组 :", arr)
    print("标准差 ", numpy.std(arr))
    print("年化标准差 ", numpy.std(arr)* math.sqrt(12))


    arr = [-4.28966245711595,(-4.28966245711595+1.14507650781293),(-4.28966245711595+1.14507650781293+-5.17385997917229),(-4.28966245711595+1.14507650781293+-5.17385997917229+-3.34912337481094),(-4.28966245711595+1.14507650781293+-5.17385997917229+ -3.34912337481094+ 1.6163991289095)]
    print("一维数组 :", arr)
    print("标准差 ", numpy.std(arr))
    print("年化标准差 ", numpy.std(arr)* math.sqrt(12))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
