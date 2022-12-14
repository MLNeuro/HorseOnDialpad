import argparse
import logging

class DialPermute:
    def __init__(self):
        self.current_depth = 0
        self.tree = []
        self.total = 0
        self.max_n = None

    def get_permutations(self, N: int = 0, start: int = 0) -> int:
        if N == 0:
            self.total = 0
            print("Total Permutations: {}".format(self.total))
            return

        self.max_n = N
        self.tree.append([start])
        self.__calc()
        print("Total Permutations: {}".format(self.total))

    
    def __calc(self):
        cur = self.tree.pop()
        self.current_depth += 1
        logging.info('cur {}'.format((cur)))

        if self.current_depth >= self.max_n:
            # reached end
            logging.info('end, incr by {}'.format(len(cur)))
            self.total += len(cur)
            return 

        nbr = []
        for c in cur: 
            nbr += self.get_next(c)

        logging.info('append {}'.format(nbr))
        self.tree.append(nbr)
        self.__calc()

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