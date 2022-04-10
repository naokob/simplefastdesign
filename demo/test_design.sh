#!/bin/bash

### Requirement: pyrosetta already installed ###
python3 ../simplefastdesign.py -n 50 -p redesign_7ec8 -r ./7ec8A_mod.resfile -i 2 ./7ec8A.pdb
