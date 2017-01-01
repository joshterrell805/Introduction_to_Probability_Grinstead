The corresponding notes for this chapter are at http://joshterrell.com/blog/posts/1482943425

# Section 4.1

## Exercises

### Problem 1
> Assume that E and F are two events with positive probabilities. Show that
if P(E|F) = P(E), then P(F|E) = P(F).

1. P(E|F) = P(E) (given)
1. P(E|F) = P(E ^ F) / P(F) (by definition)
1. P(E) = P(E ^ F) / P(F) (rhs are equal since lhs are equal)
1. P(E ^ F) = P(E) * P(F) (conclusion to be used later)
1. ...
1. P(F|E) = P(F ^ E) / P(E) (by definition)
1. P(F|E) = (P(E) * P(F)) / P(E) (substitute #4)
1. P(F|E) = P(F) (proof complete)

\#4 was really the key here. From [my chapter 4.1 notes](http://joshterrell.com/blog/posts/1482943425): "Two events E and F are independent if and only if P(F^E) = P(E)P(F)."

### Problem 6
> From a deck of five cards numbered 2, 4, 6, 8, and 10, respectively, a card
is drawn at random and replaced. This is done three times. What is the
probability that the card numbered 2 was drawn exactly two times, given
that the sum of the numbers on the three draws is 12?

#### theoretical approach
- Situation: 3 draws with replacement from random deck of {2, 4, 6, 8, 10}
- Find: P(2x2 | sum=12) probability of two of the draws being the card labeled 2, given that the sum of the 3 draws is 12.

P(2x2 | sum=12) = P(2x2 ^ sum=12) / P(sum=12)

Ways to draw sum=12:

- 2+2+8 x 3P3 / 2 = 3
- 2+4+6 x 3P3 = 6
- **4+4+4 x 1**
  - I missed this one originally in my theoretical approach and got 3/9 as the probability, but the computational approach yielded 3/10. Lesson: double check theory with an experiment, because you probably messed up.
- = 10

Ways to draw 2x2 ^ sum=12:

- 2+2+8 x 3
- = 3

Ways to draw:

- 5^3
- = 125


P(sum=12) = ways to draw sum=12 / ways to draw

= 10 / 125

P(2x2 ^ sum=12) = ways to draw 2x2 ^ sum=12 / ways to draw

= 3 / 125


P(2x2 | sum=12) = P(2x2 ^ sum=12) / P(sum=12)
= 3/125 / (10/125)
= 3/10

#### experimental/computational approach
```py
import numpy as np
import time
deck = np.array([2, 4, 6, 8, 10])
print('press ctrl+c to quit')
last_print = time.time()
n_sum_12 = 0
n_2x2_and_sum_12 = 0
while True:
  hand = np.random.choice(deck, 3)
  if sum(hand) == 12:
    n_sum_12 += 1
    if sum(1 for n in hand if n == 2) == 2:
      n_2x2_and_sum_12 += 1
  if time.time() - last_print >= 5:
    print(n_2x2_and_sum_12 / n_sum_12)
    last_print = time.time()
```
