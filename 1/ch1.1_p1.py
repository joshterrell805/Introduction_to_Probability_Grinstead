def main(args):
    import numpy as np
    count_heads = 0
    for count_tosses in range(1, args['n']+1):
        toss = np.random.randint(2)
        if toss == 1:
            count_heads += 1
        if count_tosses % args['print_interval'] == 0:
            proportion_of_heads = count_heads/count_tosses
            print('count_tosses: {}'.format(count_tosses))
            print('proportion_of_heads - 1/2: {}'.format(proportion_of_heads - 1/2))
            print('count_heads - 1/2 * count_tosses: {}'.format(count_heads - 1/2 * count_tosses))

def parse_args(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('n',
            type=int,
            help='number of times to toss the coin')
    parser.add_argument('--print_interval',
            type=int,
            default=100,
            help='how often to print the proportions')
    return vars(parser.parse_args(args))

if __name__ == '__main__':
    args = parse_args()
    main(args)
