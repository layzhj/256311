from neuron import h, load_mechanisms
import os

h.load_file('stdrun.hoc')
load_mechanisms('./mechanisms')

h.load_file('Network_CA1.hoc')
# Since the folders involved in the model may not exist, it is best to run the folder creation first
os.makedirs(h.temp_dir, exist_ok=True)

# If record the results after the network runs
# h.run()
# h.vout()
