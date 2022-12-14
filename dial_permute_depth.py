import argparse
import logging
from DialPermute import DialPermute


class DialPermuteDepth(DialPermute):
    def __init__(self):
        DialPermute.__init__(self)
        self.current_depth = 1
        self.tree = []
        self.total = 0
        self.max_n = None

    
    def calc(self):
        '''
            Working routine to find all permutations, searches for all combinations in
            depth first order. Termnates upon reaching the desired combinations length
        '''
        cur = self.tree[-1]
        logging.debug('cur {}'.format((cur)))

        if self.current_depth >= self.max_n:
            # reached end
            self.total += 1
            self.current_depth -= 1
            logging.info(self.tree)
            logging.debug('end, total: {}'.format(self.total))
            self.tree.pop()
            return 

        nbr = self.get_next(cur)
        
        for n in nbr:
            logging.debug('append {}'.format(n))
            self.current_depth += 1
            self.tree.append(n)
            self.calc()
        self.tree.pop()
        self.current_depth -= 1



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int)
    parser.add_argument('start', type=int)
    args = parser.parse_args()

    dp = DialPermuteDepth()
    dp.get_permutations(N=args.N, start=args.start)