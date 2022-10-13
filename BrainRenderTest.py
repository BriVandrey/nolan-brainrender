# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from brainrender import Scene
scene=Scene(atlas_name="allen_mouse_10um")
scene.add_brain_region("ZI","SCm")
scene.render()