#!/usr/bin/env python

'''
Copyright (c) 2020 Shintaro Minami
Originally under MIT license in GCNdesign, https://github.com/ShintaroMinami/GCNdesign/blob/master/scripts/gcndesign_autodesign.py
'''

from os import path
import sys
import argparse
import importlib
import pyrosetta

parser = argparse.ArgumentParser()
parser.add_argument('pdb', type=str, default=None, metavar='[PDB File]',
                    help='PDB file input.')
parser.add_argument('--nstruct', '-n', type=int, default=10, metavar='[Int]',
                    help='Number of structures output. (default:{})'.format(10))
parser.add_argument('--prefix', '-p', type=str, default='design', metavar='[String]',
                    help='Prefix for output PDB files. (default:{})'.format('design'))
parser.add_argument('--scorefxn', '-s', type=str, default='ref2015', metavar='[String]',
                    help='Rosetta score function. (default:{})'.format('ref2015'))
parser.add_argument('--resfile', '-r', type=str, default=None, metavar='[String]', help='resfile input.')
parser.add_argument('--iterate', '-i', type=int, default=1, metavar='[Int]', help='Number of repeats of Relax in FastDesign.  (default:{})'.format(1))
args = parser.parse_args()

pyrosetta.init("-ignore_unrecognized_res 1 -ex1 -ex2aro")
scorefxn = pyrosetta.create_score_function(args.scorefxn)

pose_in = pyrosetta.pose_from_pdb(args.pdb)

taskf = pyrosetta.rosetta.core.pack.task.TaskFactory()
taskf.push_back(pyrosetta.rosetta.core.pack.task.operation.InitializeFromCommandline())
taskf.push_back(pyrosetta.rosetta.core.pack.task.operation.IncludeCurrent())

readresfile = pyrosetta.rosetta.core.pack.task.operation.ReadResfile(args.resfile)
taskf.push_back(readresfile)

packer_task = taskf.create_task_and_apply_taskoperations(pose_in)
print(packer_task)

movemapf = pyrosetta.rosetta.core.select.movemap.MoveMapFactory()
movemapf.all_bb(setting=True)
movemapf.all_chi(setting=True)
movemapf.all_jumps(setting=False)

number_repeat=args.iterate
fastdesign = pyrosetta.rosetta.protocols.denovo_design.movers.FastDesign(scorefxn_in=scorefxn, standard_repeats=number_repeat)
fastdesign.set_task_factory(taskf)
fastdesign.set_movemap_factory(movemapf)

for i in range(args.nstruct):
    pose = pose_in.clone()
    fastdesign.apply(pose)
    file_out = '{:s}_{:03d}.pdb'.format(args.prefix, i+1)
    pose.dump_pdb(file_out)
