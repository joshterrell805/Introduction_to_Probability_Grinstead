The corresponding notes for this chapter are at http://joshterrell.com/blog/posts/1482109511

# Section 3.1

## Exercises

### Problem 10
> A deck of ordinary cards is shuffled and 13 cards are dealt. What is the probability that the last card is an ace?

#### Theoretical Approach

P(ace on 13th) = P(1st ace is the 13th card) + P(2nd ace is 13th card) + P(3rd ace is 13th card) + P(4th ace is 13th card)

P(1st ace is 13th card) = P not draw ace on first + not draw ace on second + ... not draw ace on 12th + draw ace on 13th

= `48/52 * 47/51 * ... * 37/41 * 4/40` = (48<sub>12</sub>  \* 4) / 52<sub>13</sub>

P(2nd ace is 13th card) = P draw ace as first card and not draw ace on second to twelfth and draw ace on 13th + P not draw ace on first, draw ace second, not draw ace again until 13th + .. draw ace 12th and 13th

- first is first ace: `4/52 * 48/51 * 47/50 * ... * 38/41 * 3/40`
- second is first ace: `48/52 * 4/51 * 47/50 * ... * 38/41 * 3/40`
- third is first ace: `48/52 * 47/51 * 4/50 * ... * 38/41 * 3/40`
- 12th is first ace: `48/52 * 47/51 * 46/50 * ... * 4/41 * 3/40`

so P(2nd ace is 13th card) = 12 \* (4<sub>2</sub> \* 48<sub>11</sub>) / 52<sub>13</sub>

And lets extrapolate...

P(3rd ace is 13th card) = X \* (4<sub>3</sub> \* 48<sub>10</sub>) / 52<sub>13</sub>

What is X?  if we place the first ace at the first card, there are 11 places to stick the second ace, and the last ace goes at the 13th slot always. if we place the first ace at the second card, there are 10 places to stick the second ace... so there are 11 + 10 + 9 + 8 + ... + 1 ways to place the first 12 cards? = [11 \* (11+1) / 2](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF). I think this should also be equal to 12 chose 2 which is (12! / (2! * 10!)). Sweet.

P(4th ace is 13th card) = (12 choose 3) \* (4! \* 48<sub>9</sub>) / 52<sub>13</sub>

So P(ace on 13th) = (48<sub>12</sub>  \* 4) / 52<sub>13</sub> + 12 \* (4<sub>2</sub> \* 48<sub>11</sub>) / 52<sub>13</sub> + (12 choose 2) \* (4<sub>3</sub> \* 48<sub>10</sub>) / 52<sub>13</sub> + (12 choose 3) \* (4! \* 48<sub>9</sub>) / 52<sub>13</sub>

```py
import scipy.misc

def n_lower_r(n, r):
  v = 1
  while r > 0:
    v = v * n
    n -= 1
    r -= 1
  return v



n_lower_r(48,12)*4/n_lower_r(52, 13) + 12*4*3*n_lower_r(48,11)/n_lower_r(52,13) + scipy.misc.comb(12, 2)*n_lower_r(4,3)*n_lower_r(48,10)/n_lower_r(52,13) + scipy.misc.comb(12,3)*scipy.misc.factorial(4)*n_lower_r(48,9)/n_lower_r(52,13)
# 0.07692307692307693
```

1/13

#### Computational approach (simulation)

```py
import numpy as np

experiments = 0
count_ace_is_last = 0
cards = list(range(1, 14)) * 4 # 13 is ace

print('press ctrl+c to exit')
while True:
  np.random.shuffle(cards)
  delt_cards = np.random.choice(cards, 13, replace=False)
  experiments += 1
  if delt_cards[12] == 13:
    count_ace_is_last += 1
  if experiments % 1000 == 0:
    print('prob ace last in 13 draws: {}'.format(count_ace_is_last/experiments))

#0.077 ~= 1/13
```

#### Comments
Not only did my theoretical approach require much more knowledge than my computational approach, it was much more error-prone. When I ran the calculations for the first time, for the computational version I got 0.077 and for the theoretical version I got 0.052. Because the computational version was so simple, I accepted it as correct and investigated any errors in the theoretical computation. It turns out I had a subtle copying error in the first term--I forgot to multiply by 4. I think the computational approach was much more simple. In hind-sight, an easier way to do the theoretical approach would have been to take 1 minus the prob of not getting an ace on the 13th draw. The point still stands that the theoretical approach is more error prone (though less so) and requires more knowledge.

# Section 3.2 

## Power Curve

[power-curve.py](power-curve.py) calculates m, the critical value, for an experiment and plots the power curve described in this section of the book. See the [corresponding blog post](http://joshterrell.com/blog/posts/1482109511) for a good description of this.

![image](https://cloud.githubusercontent.com/assets/4649127/21297898/fbaae386-c53c-11e6-80ae-286f667d205a.png)

## Exercises

### Problem 10
> In a ten-question true-false exam, find the probability that a student gets a
grade of 70 percent or better by guessing. Answer the same question if the
test has 30 questions, and if the test has 50 questions.

For the first quesiton, either the student gets 7, 8, 9, or 10 questions correct.

The  binomial distribution will work well here and both conditions are met. Each trail is independent, each trial has probability p=0.5 of occuring.

```
P(7/10) = (10 choose 7) * 0.5^7 * 0.5^3
        = (10 choose 7) * 0.5^10

P(8/10) = (10 choose 8) * 0.5^10
...

P(>=7/10) = ((10 choose 7)  + (10 choose 8) + (10 choose 9) + (10 choose 10)) * 0.5^10
          = 0.171875 (see code below)
```
```py
import scipy.misc
c = scipy.misc.comb
(c(10, 7) + c(10, 8) + c(10, 9) + c(10, 10)) * 0.5**10
# 0.171875

def experiment(n, thresh=0.7, p=0.5):
  import math
  n_start = math.ceil(thresh * n)
  return sum(c(n, k) * p**k * (1-p)**(n-k) for k in range(n_start, n+1))

experiment(10)
# 0.171875
experiment(30)
# 0.02138697262853384
experiment(50)
# 0.0033002239834054592
```


























