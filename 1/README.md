# Section 1.1
## The Peter coin-flipping problem
The problem is described on \[my notes for this chapter\](TODO: link to blog) as well as in the source code.

code: [peter.py](peter.py).

The following graphs are constructed when using number-of-flips-per-experiment=100 and number-of-experiments=1,000,000.

- [winnings](https://cloud.githubusercontent.com/assets/4649127/20638100/055f7110-b351-11e6-9622-913dd7947a78.png) - bar graph of the total winnings per experiment (+1 penny per heads, -1 penny per tails). X axis is total winnings, Y axis is percentage of experiments.
- [count lead](https://cloud.githubusercontent.com/assets/4649127/20638102/122b9f7c-b351-11e6-9b15-9d0994f8a069.png) - bar graph of the number of flips where the cumulative winnings were positive, per experiment. Y axis is percentage of total experiments.
- [count lead if first is heads](https://cloud.githubusercontent.com/assets/4649127/20638103/192eeea0-b351-11e6-8801-126eee3dd8fc.png) - bar graph of  the number of flips where the cumulative winnings were positive if the first flip was heads, per experiment. Y axis is percentage of experiments where first flip was heads.
- [count lead if first is tails](https://cloud.githubusercontent.com/assets/4649127/20638105/2625ab3a-b351-11e6-8606-eb1b969f40ed.png)

The first graph agrees with intuition (I expect to come out of the experiment having neither lost nor gained any money). The other graphs do not. If I flipped a coin 100 times and got a penny each time I got heads and lost a penny each time I flipped tails, I'd expect to spend about 50% of the time in the positive and about 50% of the time in the negative. This experiment shows otherwise. If I flip a coin as heads, it is most likely that I will always have a positive balance. The next most likely thing to occur is for me to have a positive balance for most of the time or negative balance for most of the time. The least likely outcome is for me to spend an equal amount of time with a positive and a negative balance. The power of simulation!

## Exercises
### Problem 1
> Modify the program CoinTosses to toss a coin `n` times and print out after
every 100 tosses the proportion of heads minus 1/2. Do these numbers appear
to approach 0 as `n` increases? Modify the program again to print out, every
100 times, both of the following quantities: the proportion of heads minus 1/2,
and the number of heads minus half the number of tosses. Do these numbers
appear to approach 0 as `n` increases?

Code: [ch1.1\_p1.py](ch1.1_p1.py)

The proportion of heads minus 1/2 approaches 0.

The number of heads minus half the number of tosses does not appear to approach 0. This variable does appear to stay near to zero relative to the number of tosses total (the proportion).
