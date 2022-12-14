import argparse
import logging
from typing import List


class DialPermute:
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
        self.__calc()
        logging.info("Total Permutations: {}".format(self.total))
        return self.total

    
    def __calc(self) -> None:
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
        self.__calc()


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



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int)
    parser.add_argument('start', type=int)
    args = parser.parse_args()

    dp = DialPermute()
    dp.get_permutations(N=args.N, start=args.start)