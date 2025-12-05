from neuron import h, load_mechanisms
import os
h.nrnmpi_init()
h.load_file('stdrun.hoc')
load_mechanisms('./mechanisms')

h.load_file('Network_CA1.hoc')
# Since the folders involved in the model may not exist, it is best to run the folder creation first
os.makedirs(h.temp_dir, exist_ok=True)
percentDeath = 0.1

def celldeath(percentDeath):
    deadlist=[]
    if percentDeath:
        num2pick = int(percentDeath * h.npcell)

        new_random = h.Random(400)
        new_random.discunif(h.iPC, h.iAAC - 1)

        for x in range(num2pick):

            tmpvar = int(new_random.repick())
            while deadlist.count(tmpvar) > 0:
                tmpvar = int(new_random.repick())

            deadlist.append(tmpvar)

        list_clamps = []
        for cell2kill in deadlist:
          # integer = h.pc.gid_exists(cell2kill)
          # if interger == 0: continue
          # model_cell = h.pc.gid2cell(cell2kill)
            for idx in range(h.gidvec.size()):
                gid = int(h.gidvec.x[idx])
                if gid == cell2kill:
                    model_cell = cell_list[idx]
                    print(model_cell)
            # keep remaining lines that add an IClamp and set its properties
            for seg in model_cell.soma:
                seg.gnabar_hha2 = 0
            for i in range(len(h.tgvec)):
                if h.tgvec[i] == cell2kill or h.srvec[i] == cell2kill:
                    h.nclist[i].active(0)
            stimobj = h.IClamp(model_cell.soma(0.5))
            stimobj.delay = 2
            stimobj.dur = h.SIMDUR
            stimobj.amp = -.8
            list_clamps.append(stimobj)
    return deadlist

# If record the results after the network runs
# h.run()
# h.vout()
