#!/usr/local/bin/python3
import atheris
import sys

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    num = fdp.ConsumeIntInRange(1, 10)

    if num == 2:
        raise Exception("You got it!")

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()