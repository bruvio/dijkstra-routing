import argparse
import logging
import sys

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
    logger.info("creating Graph from {}".format(path))

    logger.info("computing shortest path between nodes {} and {}".format(node1, node2))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run dijkstrasAlgorithm")
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="path to Graph file",
        default="citymapper-coding-test-graph.dat",
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
        default=1,
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

    logger.setLevel(logging.INFO)
    main(
        args.path,
        args.node1,
        args.node2,
    )
