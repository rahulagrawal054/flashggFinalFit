#!/usr/bin/env python

import os
from os import system, path

def rooArgSetToList(argset): ## taken from Andrea Marini's great repo here: https://github.com/amarini/rfwsutils/blob/master/wsutils.py#L300-L313
    """creates a python list with the contents of argset (which should be a RooArgSet)"""
    it = argset.createIterator()

    retval = []
    while True:
        obj = it.Next()

        if obj == None:
            break

        retval.append(obj)

    return retval

def raiseMultiError(lax=False):
    raise RuntimeError('Found more than one multipdf here - please create a workspace with just one for these bias studies. You can use "combineCards.py Datacard.txt --ic cat_name" for this)')

def raiseFailError(itoy, lax=False):
    text = 'some fits have failed, wrong quantile for toy number %g'%itoy
    if not lax: raise RuntimeError('ERROR %s'%text)
    else: print('WARNING %s'%text)

def shortName(name):
    return name.split('_')[-1]

def toyName(name, expectSignal, split=None):
    retval = f'BiasToys_Expected.{expectSignal}/biasStudy_{name}_toys.root'
    if split is not None:
        split = int(split)
        retval = retval.replace(name, f'{name}_split{split}')
    return retval


def fitName(name, expectSignal, split=None):
    retval = f'BiasFits_Expected.{expectSignal}/biasStudy_{name}_fits.root'
    if split is not None:
        split = int(split)
        retval = retval.replace(name, f'{name}_split{split}')
    return retval


def plotName(name, expectSignal):
    return f'BiasPlots_Expected.{expectSignal}/biasStudy_{name}_pulls'


def run(cmd, dry=False):
   print(cmd)
   if not dry: system(cmd)
