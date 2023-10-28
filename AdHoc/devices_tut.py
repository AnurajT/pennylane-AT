import pennylane as qml

# define the qubit
dev = qml.device("default.qubit", wires = 1)

# define the quantum function
@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)

print(circuit())

# define the lighting qubit. It is the same as the default qubit but is written in C++ and thus provides faster operation
dev_l = qml.device("lightning.qubit", wires = 1)

# define the quantum function
@qml.qnode(dev_l)
def circuit_l():
    qml.Hadamard(wires=0)
    return qml.probs(wires=0)

print(circuit_l())

# The above two devices are to be used when you know the quantum state that you are working with.
# When you dont know the quantum state, a.k.a the state is mixed, use the default mixed qubit

# define the default mixed qubit
dev_m = qml.device("default.mixed", wires = 1)

# define the quantum function
@qml.qnode(dev_m)
def circuit_m():
    qml.BitFlip(0.5, wires=0) # apply a Pauli X
    return qml.probs(wires=0)

print(circuit_m())