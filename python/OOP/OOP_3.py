# coding: utf-8

from functools import singledispatch

@singledispatch
def func(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@func.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Integer,", end=" ")
    print(arg)


@func.register(float)
def _(arg, verbose=False):
    if verbose:
        print("Float,", end=" ")
    print(arg)


@func.register(type(None))
def _(arg, verbose=False):
    print("Nothing,")


func('1', verbose=True)
func(1, verbose=True)
func(1.0, verbose=True)
func(None)

