def parse_args(**args):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',
            default=1000,
            type=int,
            help='number of times to randomly pick an outcome in the experiment')
    return vars(parser.parse_args(**args))

def main(args):
    import random
    n = args['n']
    counts = [0, 0, 0]
    for i in range(n):
        x = random.uniform(2.0, 10.0)
        if x > 5:
            counts[0] += 1
        if 5 < x < 7:
            counts[1] += 1
        if x**2 - 12*x + 35 > 0:
            counts[2] += 1
    print('Experimental results from drawing a random real number from [2, 8] n={} times:'.format(n))
    print('P(X > 5) = {}'.format(counts[0] / n))
    print('P(5 < X < 7) = {}'.format(counts[1] / n))
    print('P(X^2 - 12X + 35 > 0) = {}'.format(counts[2] / n))

if __name__ == '__main__':
    args = parse_args()
    main(args)
