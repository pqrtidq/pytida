#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Learning python: Plotting downloaded SST near Trinidad

@author: pqrtidq
"""

# %% Import

from erddapy import erddapy


# %% Construct ERDDAP url

e = erddapy.ERDDAP(server="UAF", protocol="griddap")
e.dataset_id = "nasa_jpl_dde5_3be1_897b"
e.griddap_initialize()
e.constraints["latitude>="] = 38
e.constraints["latitude<="] = 46
e.constraints["longitude>="] = -130
e.constraints["longitude<="] = -123


# %% Download

ds = e.to_xarray()
ds["analysed_sst"].plot()
ds
