import argparse
import logging

class DialPermute:
    def __init__(self):
        self.current_depth = 1
        self.tree = []
        self.total = 0
        self.max_n = None

    def get_permutations(self, N: int = 0, start: int = 0) -> int:
        if N == 0:
            self.total = 0
            logging.info("Total Permutations: {}".format(self.total))
            return self.total

        self.max_n = N
        self.tree.append(start)
        self.__calc()
        logging.info("Total Permutations: {}".format(self.total))
        return self.total

    
    def __calc(self):
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
            self.__calc()
        self.tree.pop()
        self.current_depth -= 1


    def get_next(self, n):
        if n == 1:
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
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int)
    parser.add_argument('start', type=int)
    args = parser.parse_args()

    dp = DialPermute()
    dp.get_permutations(N=args.N, start=args.start)