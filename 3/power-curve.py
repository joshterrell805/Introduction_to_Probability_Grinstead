def parse_args(args=None):
    import argparse
    parser = argparse.ArgumentParser(description=
            """
            Determines the range that the critical value can take on such that the probability of
            making a Type 1 error < `t1` and the probability of making a Type 2 error < `t2`. Draws
            the power curves described on pages 112-113 of Introduction to Probability by Grinstead
            and Snell. NOTE: This application models a one-sided hypothesis (that hA > h0).
            """)
    parser.add_argument('--desc',
            action='store_true',
            help='Print a longer description of this application and exit.')
    parser.add_argument('--n',
            default=100,
            type=int,
            help='Number of trials.')
    parser.add_argument('--t1',
            default=0.05,
            type=float,
            help='Maximum probability of making a type-1 error, of observing >= "critical vale" ' +
                    'successes even though there was no effect (proportion of successes = `h0`).')
    parser.add_argument('--t2',
            default=0.05,
            type=float,
            help='Maximum probability of making a type-2 error, of observing < "critical value" ' +
                    'successes even though there was an effect (proportion of successes = `hA`).')
    parser.add_argument('--h0',
            default=0.6,
            type=float,
            help='The expected proportion of successes if there was no effect (null hypothesis ' +
                    'is true).')
    parser.add_argument('--hA',
            default=0.8,
            type=float,
            help='The minimum proportion of successes that practically shows there was an effect ' +
                    '(alternative hypothesis is true).')
    parser.add_argument('--no_graph',
            action='store_true',
            help='Don\'t graph the power curves.')
    return vars(parser.parse_args(args))

def p_observe(k, n, p):
    """Probability of observing k successes in n trials where each success has probability p of
    occurring."""
    import scipy.misc
    return scipy.misc.comb(n, k) * p**k * (1-p)**(n-k)

def alpha(m, n, p):
    """Probability of the observing >= m successes in n trials of an experiment if p is the
    proportion of successes."""
    return sum(p_observe(successes, n, p) for successes in range(m, n+1))

def do_desc(args):
    if not args['desc']:
        return
    print('This program finds the "critical value" for an experiment which tests the effect of an independent variable. For example, we might be testing whether a drug alleviates symptoms. We (arbitrarily) call a "success" the case where we observe an effect, and a "failure" as a case where we don\'t observe an effect.  \n\nWe assume a bernoulli process to model success and failures. What that means is that each case is independent of all other cases, and that the probability of observing a success in any case is constant. This is useful for modeling the effect of independent variables in ranomized experiments, but will not be too useful to model something such as whether sleeping in warmer temperatures makes an individual wake up tired (since the probability is likely not constant nor independent day to day (case to case)) \n\nIf we observe >= "critical value" successes, we should reject the hypothesis stating that there was no effect. A smaller critical value results in more Type 1 errors and less Type 2 errors.')
    import sys
    sys.exit(0)
    
def main(args):
    do_desc(args)

    import numpy as np
    n, t1, t2, h0, hA = (args[a] for a in ('n', 't1', 't2', 'h0', 'hA'))
    assert 0 < h0 < 1 and 0 < hA < 1
    if not h0 < hA:
        print('Currently, this application only supports modeling alternative effects that are observed with higher proportion than the null effect/proportion. If your experiment has the effect smaller than the null effect, consider refactoring the usage of "successes" and "failures" in this program, or using a different program.')

    m_lower = None
    m_upper = None
    for m in range(n+1):
        p_t1 = alpha(m, n, h0)
        p_t2 = 1 - alpha(m, n, hA)
        if p_t1 > t1 or p_t2 > t2:
            continue
        if m_lower is None:
            m_lower = m
        m_upper = m

    print('The critical value can range between [{}, {}] while P(Type 1 error) < {} and P(Type 2 error) < {}'.format(m_lower, m_upper, t1, t2))

    if args['no_graph']:
        return

    if m_lower is None or m_upper is None:
        print('Could not graph.')
    else:
        import matplotlib.pyplot as plt
        alpha_by_m_lower = np.zeros(n+1)
        alpha_by_m_upper = np.zeros(n+1)
        probs = np.array([successes/n for successes in range(n+1)])
        for successes,p in enumerate(probs):
            alpha_by_m_lower[successes] = sum(p_observe(s, n, p) for s in range(m_lower, n+1))
            alpha_by_m_upper[successes] = sum(p_observe(s, n, p) for s in range(m_upper, n+1))

        fig = plt.figure()
        ax = fig.gca()
        ax.set_xticks(np.arange(0,1,0.05))
        ax.set_yticks(np.arange(0,1.,0.05))
        plt.plot(probs, alpha_by_m_lower)
        plt.plot(probs, alpha_by_m_upper)
        plt.grid()
        plt.xlabel('Proportion of observed successes')
        plt.ylabel('Probability of rejecting the null hypothesis')
        plt.legend(['critical value = {}'.format(m) for m in (m_lower, m_upper)])
        plt.show()

if __name__ == '__main__':
    args = parse_args()
    main(args)
