# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:29:40 2019

@author: Naman
"""
import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )