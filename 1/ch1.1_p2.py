def main(args):
    import numpy as np
    import lib
    from collections import defaultdict

    n_dice = 3
    dice_sides = 6
    count_sums = defaultdict(int)
    for i in range(args['n']):
        toss = np.random.randint(1, dice_sides+1, size=(n_dice,))
        count_sums[np.sum(toss)] += 1

    lib.spikegraph_of_counts(count_sums)
    print('p9: {}, p10: {}'.format(count_sums[9]/sum(count_sums.values()), count_sums[10]/sum(count_sums.values())))


def parse_args(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('n',
            type=int,
            help='number of times to toss the coin')
    return vars(parser.parse_args(args))

if __name__ == '__main__':
    args = parse_args()
    main(args)
