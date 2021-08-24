import argparse
import logging
import os
import pdb
import sys
import time

from utils import Graph, MinHeap, dijkstrasAlgorithm, remap_nodes

logger = logging.getLogger(__name__)

# ----------------------------
__author__ = "bruvio"
__version__ = "0"
__maintainer__ = "Bruno Viola"
__email__ = "bruno.viola@pm.me"
__status__ = "Testing"
# __status__ = "Production"


def main(
    path,
    node1,
    node2,
):

    if os.path.exists(path):
        logger.debug("path exists")
        logger.info("creating Graph from {}".format(path))
        logger.debug("reading number of nodes in current Graph")
        start = time.time()
        with open(path) as f:
            num_nodes = int(f.readline().rstrip())
            logger.debug("{} found".format(num_nodes))
        list_tuples = []
        with open(path, "r") as f:
            for line in f.readlines()[num_nodes + 2 :]:
                n1, n2, distance = (
                    line.split()[0],
                    line.split()[1],
                    int(line.split()[2]),
                )
                list_tuples.append(tuple([n1, n2, distance]))
        # building graph
        graph = Graph(list_tuples)
        # copying neighbours dictionary
        neighbours = graph.neighbours
        # creting list of vertices
        vertices = list(graph.vertices)

        # remapping list of vertices using hashtable

        edges, hashmap = remap_nodes(vertices, neighbours)

        start_node = hashmap[str(node1)]
        dest_node = hashmap[str(node2)]
        logger.debug("Elapsed Time to prepare the data: %s" % (time.time() - start))
        start = time.time()

        min_distance = dijkstrasAlgorithm(start_node, dest_node, edges)

        logger.info(
            "computing shortest path between nodes {} and {}".format(node1, node2)
        )
        # distance = graph.dijkstra(node1, node2)
        logger.debug("Elapsed Time: %s" % (time.time() - start))
        if min_distance != -1:
            logger.info(
                "distance between node {} and node {} is \n {}".format(
                    node1, node2, min_distance
                )
            )

    else:
        logger.error("specified path does not exists")
        return


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run dijkstrasAlgorithm")
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="path to Graph file",
        required=True,
    )
    parser.add_argument("-n1", "--node1", type=str, help="start node", required=True)
    parser.add_argument(
        "-n2", "--node2", type=str, help="destination node", required=True
    )
    parser.add_argument(
        "-d",
        "--debug",
        type=int,
        help="Debug level. 0: Error, 1: Warning, 2: Info, 3: Debug, 4: Debug Plus",
        default=2,
    )
    args = parser.parse_args(sys.argv[1:])

    # Setup the logger
    debug_map = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
        4: 5,
    }

    logging.basicConfig(level=debug_map[args.debug])

    logging.addLevelName(5, "DEBUG_PLUS")

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=debug_map[args.debug])
    main(
        args.path,
        args.node1,
        args.node2,
    )
