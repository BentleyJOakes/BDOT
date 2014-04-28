CBD.py contains the class definitions for the various CBD blocks
CBDsimulator.py contains the operational semantics (aka simulation kernel) for CBD models

ExampleCBD.py demonstrates how to instantiate CBD models

EulerSubsystemTest.py demonstrates how to instantiate and connect subsystems with regular blocks (in- or outputport name has to be passed on as argument).
(Note: for connecting 2 subsystems in- and outport name have to be passed) 


simulationExperiment.py instantiates EulerSubsystemTest and passes it to the CBDsimulator for simulation.



Some extra.

the CBD.py contains a function to flatten the model and a function for constant folding


The constant folding doesn't work yet. I didn't had time yet, after returning from Barbados, to continue on this.
There even might be an error in there at the moment.

