import env_examples  # Modifies path, DO NOT REMOVE

from src import Circuit, Current, Wire, World


if __name__ == "__main__":
    world = World(shape=(51, 51))

    WIRES = [Wire(start=(25, 0), stop=(0, 0), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(0, 0), stop=(0, 50), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(0, 50), stop=(25, 50), current=Current(x=0, y=-1), voltage=4.5),
        Wire(start=(25, 50), stop=(50, 50), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(50, 50), stop=(50, 0), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(50, 0), stop=(25, 0), current=Current(x=0, y=1), voltage=-4.5),
    ]
        # TODO : Add wires here

    circuit = Circuit(wires=WIRES)

    world.place(circuit)

    world.compute()

    world.show_all()
