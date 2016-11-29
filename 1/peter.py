def parse_args(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('flips_per_experiment',
            type=int,
            help='number of times to toss the coin per experiment')
    parser.add_argument('--experiment_count',
            type=int,
            default=1000,
            help='number of times to do the experiment')
    return vars(parser.parse_args(args))

def main(args): 
    """
    In this experiment, each flip of a heads equals +1 penny and each flip of a tails equals -1
    penny. We use a fair coin (50/50 chance of heads or tails).
    """
    import numpy as np
    import lib

    n = args['flips_per_experiment']
    ec = args['experiment_count']

    # Each of the next three vectors has dimensions = (experiment_count,)
    # The amount of pennies the player won, per experiment.
    winnings_per_ex = np.zeros((ec,),dtype = np.int64)
    # The amount of flips the player was in the lead, per experiment.
    # If on any flip the player currently has:
    # - a positive number of pennies, the player is in the lead.
    # - a negative number of pennies, the player is not in the lead.
    # - zero pennies, the player is in the lead if they were in the lead last flip.
    n_lead_per_ex = np.zeros((ec,), dtype = np.int64)
    # The first flip per experiment, either 0 (tails) or 1 (heads).
    first_heads_per_ex = np.zeros((ec,), dtype = np.int64)

    for n_ex in range(ec):
        # n flips of either 0 (tails) or 1 (heads)
        flips = np.random.randint(2, size=n)
        n_lead = 1 if flips[0] == 1 else 0
        winnings = 1 if flips[0] == 1 else -1
        for n_flip in range(1, n):
            prev_winnings = winnings
            winnings += 1 if flips[n_flip] == 1 else -1
            if winnings > 0:
                n_lead += 1
            elif winnings == 0 and prev_winnings > 0:
                n_lead += 1
        winnings_per_ex[n_ex] = winnings
        n_lead_per_ex[n_ex] = n_lead
        first_heads_per_ex[n_ex] = bool(flips[0])

    lib.spikegraph_of_points(winnings_per_ex)
    lib.spikegraph_of_points(n_lead_per_ex)
    # spikegraph of the number of times the player was in the lead if their first flip was heads
    first_heads = [n_lead_per_ex[i] for i in range(ec) if first_heads_per_ex[i]]
    lib.spikegraph_of_points(first_heads)
    # spikegraph of t_pointshe number of times the player was in the lead if their first flip was tails
    first_tails = [n_lead_per_ex[i] for i in range(ec) if not first_heads_per_ex[i]]
    lib.spikegraph_of_points(first_tails)


if __name__ == '__main__':
    args = parse_args()
    main(args)
