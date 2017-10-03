#!/usr/bin/env python3

from pyflow.flow_network import FlowNetwork
from pyflow.push_relabel_algorithm import PushRelabelExecutor

if __name__ == '__main__':
    entrances = [0, 1]
    exits = [4, 5]
    graph = [
        [0, 0, 4, 6, 0, 0],
        [0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 4, 4],
        [0, 0, 0, 0, 6, 6],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    # prepare our network
    flowNetwork = FlowNetwork(graph, entrances, exits)
    # set algorithm
    flowNetwork.setMaximumFlowAlgorithm(PushRelabelExecutor)
    # and calculate
    maximumFlow = flowNetwork.findMaximumFlow()

    print("maximum flow is {}".format(maximumFlow))