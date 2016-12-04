import math

def parse_args(**args):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',
            default=1000,
            type=int,
            help='number of times to randomly pick an outcome in the experiment')
    parser.add_argument('--func',
            choices=list(funcs.keys()),
            default='y=sin(pi*x)',
            help='function to estimate area under')
    parser.add_argument('--seed',
            default=0,
            type=int,
            help='value to seed the random function with. Specify 0 to pick a random seed')
    parser.add_argument('--nograph',
            action='store_true',
            help='turn off graphing')
    parser.add_argument('--markersize',
            default=3.0,
            type=float,
            help='marker size (in pixels)')
    return vars(parser.parse_args(**args))

def main(args):
    import random
    import numpy as np
    import matplotlib.pyplot as plt


    if args['seed'] != 0:
        random.seed(args['seed'])
    n = args['n']
    fn = funcs[args['func']]
    nograph = args['nograph']
    markersize = args['markersize']

    n_outside = 0
    if not nograph:
        points_inside = np.zeros((n, 2))
        points_outside = np.zeros((n, 2))

    for i in range(n):
        x,y = random.random(), random.random()
        if fn['fn'](x, y):
            if not nograph:
                points_inside[i, :] = np.array([x, y])
        else:
            n_outside += 1
            if not nograph:
                points_outside[i, :] = np.array([x, y])

    area = 1 - n_outside/n
    print('probability = area = {}'.format(area))
    print('error (true_area - area) = {}'.format(fn['true_area'] - area))
    estimate = fn['estimate_val'](area)
    print('estimated {} to be {}'.format(fn['estimate_sym'], estimate))
    print('estimate error ({} - estimate) = {}'.format(fn['estimate_sym'],
            fn['estimate_true_val'] - estimate))
    plt.plot(points_outside[:, 0], points_outside[:, 1], 'k.',
            points_inside[:, 0], points_inside[:, 1], 'r.', markersize=markersize)
    plt.show()

funcs = {
    'y=sin(pi*x)': {
        'fn': lambda x, y: y <= math.sin(math.pi * x),
        'true_area': 2 / math.pi,
        'estimate_val': lambda area: 1/area*2,
        'estimate_true_val': math.pi,
        'estimate_sym': 'pi',
    },
    '(y-.5)^2+(x-.5)^2=.5^2': {
        'fn': lambda x, y: -math.sqrt(0.5**2 - (x-0.5)**2) + 0.5 \
                <= y <= math.sqrt(0.5**2 - (x-0.5)**2) + 0.5,
        'true_area': math.pi / 4,
        'estimate_val': lambda area: area*4,
        'estimate_true_val': math.pi,
        'estimate_sym': 'pi',
    },
    'y=1/(x+1)': {
        'fn': lambda x, y: y <= 1/(x+1),
        'true_area': math.log(2),
        'estimate_val': lambda area: 10**(math.log(2, 10)/area),
        'estimate_true_val': math.exp(1),
        'estimate_sym': 'e',
    },
}

if __name__ == '__main__':
    args = parse_args()
    main(args)
