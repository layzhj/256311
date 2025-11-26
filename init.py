from neuron import h, load_mechanisms

h.load_file('stdrun.hoc')
load_mechanisms('./mechanisms')

h.load_file('Network_CA1.hoc')

# If record the results after the network runs
# h.run()
# h.vout()
