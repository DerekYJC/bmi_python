import unittest
import numpy as np 
import plantlist
from tasks import bmi_recon_tasks
import dbfunctions as dbfn

idx = 5275
te = dbfn.TaskEntry(idx, dbname='testing')
n_iter = len(te.hdf.root.task)
        

cls = bmi_recon_tasks.KFRMLCGRecon
gen = []
task = cls(te, n_iter)

task.plant = plantlist.cursor_14x14_no_vel_wall
task.init()
        
error = task.calc_recon_error(verbose=False, n_iter_betw_fb=1000)
abs_max_error = np.max(np.abs(error))

print(abs_max_error)