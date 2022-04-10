# simplefastdesign
This is a simple script to do FastDesign in pyrosetta based on resfile.

## Requirements
PyRosetta must already be installed.
PyRosetta can be downloaded under license from the following link
https://www.pyrosetta.org/home

## About resfile
Resfile syntax and conventions
https://www.rosettacommons.org/docs/latest/rosetta_basics/file_types/resfiles

The resfile used in the demo was generated using gcndesign_resfile.py from Dr. Shintaro Minami's GCNdesign and modified.

GCNdesign
https://github.com/ShintaroMinami/GCNdesign

## Usage
 ```python3 simplefastdesign.py -n 50 -r ./demo/7ec8A_mod.resfile ./demo/7ec8A.pdb```

## License
The original of this file is licensed under the license noted below.

Copyright (c) 2020 Shintaro Minami
Originally under MIT license in GCNdesign, https://github.com/ShintaroMinami/GCNdesign/blob/master/scripts/gcndesign_autodesign.py
