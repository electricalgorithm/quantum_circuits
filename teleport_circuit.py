"""
Implementation of Quantum Teleporation using Qiskit.
Gökhan Koçmarlı, 18 Nov 2022
"""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

# Creating three Qubits and one classical bit.
# Two of the qubits will be entanglement. The
# other one will be the one shared.
# Classical bit would us perform conditional
# statements and will be used to store qubit's
# values after sharing it.
qreg_q = QuantumRegister(3, 'q')
creg_c0 = ClassicalRegister(1, 'c0')
circuit = QuantumCircuit(qreg_q, creg_c0)

# Set 3-qubit register to 0.
circuit.reset(qreg_q[0])
circuit.reset(qreg_q[1])
circuit.reset(qreg_q[2])

# Apply custom probabilites to Alice's
# own qubit (the one which is not 
# entanglemented) [q2].
circuit.h(qreg_q[2])
circuit.ry(3.5 * pi / 4, qreg_q[2])

# To have a distinguish.
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])

# Performing entanglement on Alice and Bob's
# qubits. (q[1] and q[0])
circuit.h(qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[0])

# To have a distinguish.
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])

# Apply a CNOT gate, and measure Alice's q[1].
# Save that qubit's value to classical bit.
circuit.cx(qreg_q[2], qreg_q[1])
circuit.measure(qreg_q[1], creg_c0[0])

# To have a distinguish.
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])

# If classical bit is 1, apply a NOT gate
# to Bob's qubit.
circuit.x(qreg_q[0]).c_if(creg_c0, 1)

# To have a distinguish.
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])

# Apply a Hadamard gate to Alice's indivudial
# qubit and measure it, save to classical bit.
circuit.h(qreg_q[2])
circuit.measure(qreg_q[2], creg_c0[0])

# To have a distinguish.
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])

# If classical bit is 1, apply a Z gate to
# Bob's qubit.
circuit.rz(pi / 2, qreg_q[0]).c_if(creg_c0, 1)

# We have copied the Alice's own qubit's first
# position to Bob's qubit. q[2] --> q[0]

# To have a distinguish.
circuit.barrier(qreg_q[0], qreg_q[1], qreg_q[2])

# Save the value of Bob's qubit to classical
# bit to see if it's 0 or 1, and to plot the
# probabilities.
circuit.measure(qreg_q[0], creg_c0[0])
