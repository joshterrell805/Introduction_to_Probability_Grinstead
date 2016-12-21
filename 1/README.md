My notes for chapter 1 are at http://joshterrell.com/blog/posts/1480434719

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
Below I just practice a few of the exercises. I'll proably pick a few more to practice from these sections as time progresses. So far it's review for me and pretty simple; I want to spend my time effectively.

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

### Problem 3
> In the early 1600s, Galileo was asked to explain the fact that, although the
number of triples of integers from 1 to 6 with sum 9 is the same as the number
of such triples with sum 10, when three dice are rolled, a 9 seemed to come
up less often than a 10—supposedly in the experience of gamblers.
>
> (a) Write a program to simulate the roll of three dice a large number of
times and keep track of the proportion of times that the sum is 9 and
the proportion of times it is 10.
>
> (b) Can you conclude from your simulations that the gamblers were correct?

code: [ch1.1\_p2.py](ch1.1_p2.py)

plot: [spikegraph](https://cloud.githubusercontent.com/assets/4649127/20650661/d910659a-b488-11e6-8dfa-5f25f2faca2a.png)

The gamblers were correct. In one million rolls of 3 six-sided die, 9 came up less often than ten.

- ways to roll any = 6 * 6 * 6 = 216
- ways to roll 9
  - 1 + 2 + 6 (6)
  - 1 + 3 + 5 (6)
  - 1 + 4 + 4 (3)
  - 2 + 2 + 5 (3)
  - 2 + 3 + 4 (6)
  - 3 + 3 + 3 (1)
  - 25 ways
  - 22/216 =  approx 0.116
- ways to roll 10
  - 1 + 3 + 6 (6)
  - 1 + 4 + 5 (6)
  - 2 + 2 + 6 (3)
  - 2 + 3 + 5 (6)
  - 2 + 4 + 4 (3)
  - 3 + 3 + 4 (3)
  - 27 ways
  - 27/216 = 0.125
- actual numbers from experiment: p9: 0.115561, p10: 0.124739

### Problem 15
> Estimate, by simulation, the average number of children there would be in
a family if all people had children until they had a boy. Do the same if all
people had children until they had at least one boy and at least one girl. How
many more children would you expect to find under the second scheme than
under the first in 100,000 families? (Assume that boys and girls are equally
likely.)

#### Mean # of children until boy (p=0.5)

```
import time
import numpy as np

n_experiments = 0
last_print = time.time()
print('press ctrl+c to exit')
X = []
while True:
  trials = 0
  boy = False
  while not boy:
    trials += 1
    if np.random.randint(2) == 0:
      boy = True
  X.append(trials)
  now = time.time()
  if now - last_print > 10:
    print('n: {}'.format(len(X)))
    print('average: {}'.format(np.mean(X)))
    last_print = now
  
# n: 592209
# average: 1.9987555069240759
# n: 1180436
# average: 2.000324456387301
# n: 1759775
# average: 1.9998317966785526
```

#### Mean # of children until boy and girl (p=0.5)
```
import time
import numpy as np

n_experiments = 0
last_print = time.time()
print('press ctrl+c to exit')
X = []
while True:
  trials = 0
  boy = False
  girl = False
  while not (boy and girl):
    trials += 1
    if np.random.randint(2) == 0:
      boy = True
    else:
      girl = True
  X.append(trials)
  now = time.time()
  if now - last_print > 10:
    print('n: {}'.format(len(X)))
    print('average: {}'.format(np.mean(X)))
    last_print = now

# n: 342066
# average: 2.9966673098174037
# n: 735956
# average: 2.9981805977531266
# n: 1127937
# average: 2.9990362936937083
```

#### More children in second than first?
I'd expect to find 1 more child, on average, in second scheme (mean=3) than first (mean=2).

# Section 1.2
## Exercises
### Problem 15
> John and Mary are taking a mathematics course. The course has only three
grades: A, B, and C. The probability that John gets a B is .3. The probability
that Mary gets a B is .4. The probability that neither gets an A but at least
one gets a B is .1. What is the probability that at least one gets a B but
neither gets a C?

- E1 = John gets a B. {JB}. P(E1) = 0.3
  - {{MA,JB}, {MB,JB}, {MC,JB}}
- E2 = Mary gets a B. {MB}. P(E2) = 0.4
  - {{MB,JA}, {MB,JB}, {MB,JC}}
- E3 = !(Mary or John gets A) && (Mary or John gets B). P(E3) = 0.1
  - = M and J in {B, C} && (M in {B} or J in {B})
  - {MB, MC} && {JB, JC} && {MB, JB} = {{MB,JB}, {MB,JC}, {MC,JB}}
- E4 = (Mary or John gets B) && !(Mary or John gets C).
  - W.T.F. = P(E4)
  - = M and J in {A, B} && (M in {B} or J in {B})
  - {MA, MB} && {JA, JB} && {MB, JB} = {{MB,JB}, {MB,JA}, {MA,JB}}
- E1 U E2
  - {{MA,JB}, {MB,JB}, {MC,JB}, {MB,JA}, {MB, JC}}
  = E3 U E4 !! :)
- E3 U E4 = E1 U E2
- P(E3 U P4) = P(E1 U E2)
- P(E3) + P(E4) - P(E3^E4) = P(E1) + P(E2) - P(E1^E2)
- P(E4) = P(E1) + P(E2) - P(E3) - P(E1^E2) + P(E3^E4)
- E1^E2 = {MB, JB}
- E3^E4 = {MB, JB} -> P(E1^E2) = P(E3^E4)
- P(E4) = P(E1) + P(E2) - P(E3) ~~- P(E1^E2) + P(E3^E4)~~
- P(E4) = P(E1) + P(E2) - P(E3)
- P(E4) = 0.3 + 0.4 - 0.1
- P(E4) = 0.6
