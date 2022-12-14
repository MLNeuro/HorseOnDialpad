import abc
import argparse
import logging
from typing import List
from DialPermute import DialPermute


class DialPermuteBreadth(DialPermute):
    def __init__(self):
        DialPermute.__init__(self)
        self.current_depth = 0
        self.tree = []
        self.total = 0
        self.max_n = None

    def calc(self) -> None:
        '''
            Working routine to find all permutations, searches for all combinations in
            breath first order. Termnates upon reaching the desired combinations length
        '''
        cur = self.tree
        self.current_depth += 1
        logging.debug('cur {}'.format((cur)))

        if self.current_depth >= self.max_n:
            # reached end
            logging.debug('end, incr by {}'.format(len(cur)))
            self.total += len(cur)
            return 

        nbr = []
        for c in cur: 
            nbr += self.get_next(c)

        logging.debug('append {}'.format(nbr))
        self.tree = nbr
        self.calc()



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int)
    parser.add_argument('start', type=int)
    args = parser.parse_args()

    dp = DialPermuteBreadth()
    dp.get_permutations(N=args.N, start=args.start)