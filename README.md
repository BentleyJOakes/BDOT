BDOT - Block Diagram Optimization Transformations
====

Description

This is the code for the project detailed in the rep621.pdf created on April 27th, 2014.

The Simulink modelling tool is used to diagram and study cyber-physical systems. One advantage
of modelling the systems in this way is that embeddable code can generated from the models directly.
However, this process means that inefficiencies in the model may be propagated to the code. Code
generation optimizations are available, but may lead to an unacceptable loss of traceability in determining
which parts of the model were modified or removed during code generation.
In our work, we focus on defining model-to-model optimizations. This means that the optimized
model can be loaded back into Simulink for further development or analysis, improving traceability and
allowing model specialization for different platforms. An analysis framework has been created, based on
dataflow analysis from the compiler optimization domain. This allows fast and accurate definition of new
optimizations. As well, an initial optimization classification was developed to aid in the discovery of new
optimizations. At the present time, we have implemented three optimizations in our framework: constant
folding, dead-block removal, and hierarchy flattening. These optimizations are intended to simplify the
model and potentially increase model performance when simulated.
Our framework allows us to communicate directly with a Simulink instance to import and export
models, allowing us to test these optimizations on a number of sample Simulink models. In order to
test the performance benefits of our optimizations, our experiments generated simulation code for the
model before and after optimization. Examining the run-time of these simulations indicated that the
constant folding optimization decreased the run-time on all applicable models when code generation
optimizations were not used. This decrease in run-time is well above the fraction of a second that the
analysis and transformation took for this optimization. Thus, a net gain in performance was obtained.
Other optimizations did not show performance results, but did produce a simplified model, which is also
desirable for a modeller.


Running

Execute 'source run.sh' to set up the environment variables for the shared library. Only works on the ubuntu.cs.mcgill.ca server.

The entry point for the code is optimizationExperiment.py. Simply run this file to perform a constant folding optimization on a model. Command-line arguments can also be taken to customize the optimization.

Folders

CBD - Obsolete. Code for models created in the CBD format.

dot - dot files and svgs for the Himesis graphs produced during optimization. Note how the Simulink structure needs extra port nodes that must be accounted for in the analysis and transformation stages of an optimization.

examples - Example models. Also contains models that define transformations, which are future work at this time.

FlowAnalyzer - A dataflow analyzer that can run over the model in Python

himesis - The Himesis files created during optimization

HimesisToCBD - Helper code to load models from Himesis into Python objects, and back again

Optimizations - The actual optimizations written in Python code

results - Generated code produced for each model

Server - The code that communicates with Simulink to import/export models

temp - Location to store himesis graphs for transformations, as required by future work

