#!/usr/local/bin/python3
import atheris
import sys

def MyTestFunction(num):
    if num == 2:
        raise Exception("You got it!")

@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    num = fdp.ConsumeIntInRange(1, 10)

    MyTestFunction(num)


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()