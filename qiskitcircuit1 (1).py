import qiskit as qiskit
get_ipython().run_line_magic('matplotlib', 'inline')


circuit = qiskit.QuantumCircuit(2,2) # 2 qubits, 2 classical bits

# Currently: 0,0
circuit.x(0) # NOT gate, now 1,0
circuit.cx(0,1) # CNOT gate, flips second qubit only if first qubit is a 1.

# now we should have 1,1
circuit.measure([0,1], [0,1]) #measuring here, value should fall to 0 or 1. This function will produce a 24:00
circuit.draw() # this function gives an ascii representation of the circuit

circuit.draw(output="mpl")

from qiskit import IBMQ
IBMQ.save_account(open("token.txt", "r").read())
IBMQ.load_account
# lets talk a look at the simulators available to me and how many jobs they have queued now.
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
for backend in provider.backends():
    try:
        qubit_count = len(backend.properties().qubits)
    except:
        qubit_count = "simulated"
    print(f"{backend.name()} has {backend.status().pending_jobs} queued and {qubit_count} qubits")


from qiskit.tools.monitor import job_monitor
backend = provider.get_backend("ibmq_wasm_simulator")
job = qiskit.execute(circuit, backend=backend, shots=500)
job_monitor(job)

from qiskit.visualization import plot_histogram
from matplotlib import style

style.use("dark_background")
result = job.result()

counts = result.get_counts(circuit)
plot.histogram([counts])

# going to run on qasm simulator now.
backend = provider.get_backend("ibmq_qasm_simulator")
circuit = qiskit.QuantumCircuit(2,2) # 2 qubits and 2 bits

#currently 0,0
circuit.h(0) #hadamard gate; whatever qubit passed through in superposition.
# 1,0
circuit.measure([0,1], [0,1]) 
circuit.draw()

job = qiskit.execute(circuit, backend=backend, shots=500)
job_monitor(job)
result = job.result()
counts = result.get_counts(circuit)
plot_histogram([counts])



from qiskit import Aer
sim_backend = Aer.get_backend("qasm_simulator")
for backend in Aer.backends():
    print(backend)



job = qiskit.execute(circuit, backend=sim_backend, shots=500)
job_monitor(job)

result = job.result()
counts = result.get_counts(circuit)

plot_histogram([counts])





