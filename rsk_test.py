#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:10:11 2022

@author: jacobpartida
"""

from pyrsktools import RSK
import numpy as np
import matplotlib.pyplot as plt

file = "/Users/jacobpartida/projects/thoon/data/rbrm/test/211566_20221219_1935.rsk"

with RSK(file) as rsk:

    rsk.readdata()
    rsk.deriveseapressure()
    rsk.derivedepth()
    rsk.derivevelocity()
    rsk.derivesalinity()

    # # see https://docs.rbr-global.com/pyrsktools/_rsk/process.html# for all:
    # lat = 41.05
    # lon = -124.25
    # rsk.derivebuoyancy(latitude=lat)
    # rsk.derivesigma(latitude=lat,longitude=lon)
    # rsk.derivetheta(latitude=lat,longitude=lon)

    # rsk.smooth()

    rsk.printchannels()
    print(f"number of samples: {len(rsk.data)} ")

    # rsk.plotdata()
    # rsk.plotTS()
