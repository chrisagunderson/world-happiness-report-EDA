#!/usr/bin/env python3

## Add a prefix to filenames

# Load libaries

from glob import glob
import os

# Set Prefix
pre = "world-happiness-"

# Rename all .csv files with prefix

[os.rename(f, "{}{}".format(pre, f)) for f in glob("*.csv")]
