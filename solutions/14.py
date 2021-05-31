"""Plan of attack:
    v1: (1.078704 seconds)
        Use memoization to optimize the count of longest collatz sequence.
"""
import _init_paths
from lib.utils.generic import Timer
from lib.sequence_generators import CollatzSequenceGenerator


@Timer(name='decorator')
def execute_v1():
    print(CollatzSequenceGenerator.longest_sequence_seed(1000000))


if __name__ == "__main__":
    execute_v1()
