#!/usr/bin/env python
#-*-coding: utf-8 -*-
import os
import sys
import Sniper

def get_entries(filename):
  from ROOT import TFile
  tfile = TFile(filename)
  tree = tfile.Get("nEXOevents")
  n_entries = tree.GetEntries()
  tfile.Close()
  return n_entries

task = Sniper.Task("mytask")
task.asTop()
#task.setLogLevel(0)

# = arguments =
filename =  sys.argv[1]
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


n_entries = 48
#n_entries = get_entries(filename) # causes seg fault
print "n_entries", n_entries
task.setEvtMax(n_entries)
#task.setEvtMax(-1) doesn't work
task.show()
print "--> running"
task.run()

