import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=2)

# By default in pennylane all qbits are initialised in the 0 state

@qml.qnode(dev)             # This is called a decorator 
def circuit(theta): 
    qml.PauliX(wires=1)     # This refers to the 2nd wire since python lists start with 0
    qml.CNOT(wires=[1,0])
    qml.RY(theta, wires=0)

    return qml.expval(qml.PauliZ(wires=0))

# print(circuit(np.pi))

thetas = np.arange(-np.pi, np.pi, 0.01)

measurements = np.zeros(len(thetas))

for i, theta in enumerate(thetas):
    measurements[i] = circuit(theta)

plt. plot(thetas, measurements)
plt.show()
