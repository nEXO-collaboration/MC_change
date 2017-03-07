#!/usr/bin/env python
#-*-coding: utf-8 -*-
from ROOT import TFile
import os
import sys
import Sniper

def get_entries(filename):
  tfile = TFile(filename)
  tree = tfile.Get("nEXOevents")
  n_entries = tree.GetEntries()
  return n_entries

def process_file(filename):
  task = Sniper.Task("mytask")
  task.asTop()
  #task.setLogLevel(0)

  # = arguments =
  inputmc = os.path.basename(filename)
  inputmcdir = os.path.dirname(filename)
  if inputmcdir == "": inputmcdir = "./"

  # = rootio =
  import RootIOSvc
  ros = task.createSvc("RootOutputSvc/OutputSvc")
  ros.property("OutputStreams").set({"/Event/Sim": "changed_%s" % inputmc})

  # = BufferMemMgr =
  import BufferMemMgr
  bufMgr = task.createSvc("BufferMemMgr")
  bufMgr.property("TimeWindow").set([0, 0]);

  # = geometry service =
  import Geometry
  simgeomsvc = task.createSvc("SimGeomSvc")

  # = MC_change = 
  Sniper.loadDll("libMyAlg.so")
  myalg = task.createAlg("MC_change/myalg")
  myalg.property("InputMCName").set(inputmc)
  myalg.property("InputMCDir").set(inputmcdir)

  n_entries = get_entries(filename) 
  task.setEvtMax(n_entries)
  task.show()
  task.run()

if __name__ == "__main__":

  process_file(sys.argv[1])
