import abc
import argparse
import logging
from typing import List

class DialPermute(abc.ABC):
    def __init__(self):
        self.current_depth = 0
        self.tree = []
        self.total = 0
        self.max_n = None

    def get_permutations(self, N: int = 0, start: int = 0) -> int:
        '''
            Given a starting number start on a dialpad and a length N
            we calculate all possible unique phone combinations, restricting ourself only to 
            chesses horse jumps. 
            :param N:       Length of phone number
            :param start:   Starting number to begin with
            :return:        Number of possible unique comibinations
        '''
        if N == 0 or start == 5:
            self.total = 0
            logging.info("Total Permutations: {}".format(self.total))
            return self.total

        self.max_n = N
        self.tree.append(start)
        self.calc()
        logging.info("Total Permutations: {}".format(self.total))
        return self.total

    
    @abc.abstractmethod
    def calc(self) -> None:
        raise NotImplementedError


    def get_next(self, n: int) -> List[int]:
        '''
            Given a current number on the dialpad we return all possible next targets as list,
            the special tokens 40 and 60 are to remember the parents of the 0, as they form a 
            loop where the origin matters.

            :param n:   Current number on dialpad
            :return:    List with all next reachable targets
        '''
        if n == 0:
            return [4,6]
        elif n == 1:
            return [6,8]
        elif n == 2:
            return [7,9]
        elif n == 3:
            return [4,8]
        elif n == 4:
            return [40,3,9]
        elif n == 6:
            return [60, 1, 7]
        elif n == 7:
            return [2,7]
        elif n == 8:
            return [1,3]
        elif n == 9:
            return [2,4]
        elif n == 40:
            return [4]
        elif n == 60:
            return [6]

