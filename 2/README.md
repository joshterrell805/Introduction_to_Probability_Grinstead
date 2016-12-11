The corresponding notes for this chapter are at http://joshterrell.com/blog/posts/1481168309

# Section 2.1

## Exercises

### Problem 3
> Alter the program MonteCarlo to estimate the area of the circle of radius
1/2 with center at (1/2, 1/2) inside the unit square by choosing 1000 points
at random. Compare your results with the true value of &pi;/4. Use your results
to estimate the value of &pi;. How accurate is your estimate?

**code for the following output & graphs: [ch2.1_p3.py](ch2.1_p3.py)**

```
[josh@joshLT 2]$ python ch2.1_p3.py  --n=10000 --markersize=4 --func='(y-.5)^2+(x-.5)^2=.5^2'
probability = area = 0.7857000000000001
error (true_area - area) = -0.000301836602551786
estimated pi to be 3.1428000000000003
estimate error (pi - estimate) = -0.001207346410207144
```

![image](https://cloud.githubusercontent.com/assets/4649127/20868427/45d65644-ba10-11e6-9774-77d5c93784c3.png)

### Problem 4
> Alter the program MonteCarlo to estimate the area under the graph of
y = sin &pi;x inside the unit square by choosing 10,000 points at random. Now
calculate the true value of this area and use your results to estimate the value
of &pi;. How accurate is your estimate?

```
[josh@joshLT 2]$ python ch2.1_p3.py  --n=10000 --markersize=4 --func='y=sin(pi*x)'
probability = area = 0.6387
error (true_area - area) = -0.002080227632418663
estimated pi to be 3.1313605761703456
estimate error (pi - estimate) = 0.010232077419447538
```

![image](https://cloud.githubusercontent.com/assets/4649127/20868416/efd20e5a-ba0f-11e6-8d1e-91dc0935e8f6.png)

### Problem 5
> Alter the program MonteCarlo to estimate the area under the graph of
y = 1/(x + 1) in the unit square in the same way as in Exercise 4. Calculate
the true value of this area and use your simulation results to estimate the
value of log 2. How accurate is your estimate?

```
[josh@joshLT 2]$ python ch2.1_p3.py  --n=10000 --markersize=4 --func='y=1/(x+1)'                                                                                                                                                   
probability = area = 0.6909000000000001
error (true_area - area) = 0.0022471805599452166
estimated e to be 2.7271375454731155
estimate error (e - estimate) = -0.008855717014070397
```

![image](https://cloud.githubusercontent.com/assets/4649127/20868393/618013b8-ba0f-11e6-8397-57633a7cf69b.png)

# Section 2.2

## Exercises

### Problem 1
> Suppose you choose at random a real number X from the interval [2, 10].
>
> (a) Find the density function f(x) and the probability of an event E for this experiment, where E is a subinterval [a, b] of [2, 10].
>
> (b) From (a), find the probability that X > 5, that 5 < X < 7, and that
X<sup>2</sup> − 12X + 35 > 0.

#### Problem 1(a)
Since X is chosen randomly from the interval, no area of the interval is more likely to be drawn from than any other. The density function for the outcome of X is uniform (constant).

The cumulative distribution function, F(x), is:

- 0 where X < 2
- (X-2)/(10-2) where 2 <= X <= 10
- 1 where X > 10

The probability density function, f(x), is the derivative of the cumulative distribution function:

- 0 where X < 2
- 1/8 where 2 <= X <= 10
- 0 where X > 10

And the probability of some event E occuring where E is a subinterval [a, b] of [2, 10] is

![image](https://cloud.githubusercontent.com/assets/4649127/21082188/78ebfe1e-bf8b-11e6-9635-c6a1fe991a7e.png)


#### Problem 1(b)

P(X > 5):

![image](https://cloud.githubusercontent.com/assets/4649127/21082182/54b0bf6c-bf8b-11e6-8809-f5f10852bb9c.png)

P(5 < X < 7):

![image](https://cloud.githubusercontent.com/assets/4649127/21082194/9289c036-bf8b-11e6-98f1-0d0eeaa000de.png)

P(X^2 - 12X + 35 > 0):

![image](https://cloud.githubusercontent.com/assets/4649127/21082219/035d7442-bf8c-11e6-8bd0-bee1abc0221a.png)


or

![image](https://cloud.githubusercontent.com/assets/4649127/21082248/828b9974-bf8c-11e6-8113-18873540b889.png)

### Problem 17
> Write a program to choose a random number X in the interval [2, 10] 1000 times and record what fraction of the outcomes satisfy X > 5, what fraction satisfy 5 < X < 7, and what fraction satisfy x 2 − 12x + 35 > 0. How do these results compare with Exercise 1?

```
[josh@joshLT 2]$ python ch2.2_p17.py
Experimental results from drawing a random real number from [2, 8] n=1000 times:
P(X > 5) = 0.628
P(5 < X < 7) = 0.235
P(X^2 - 12X + 35 > 0) = 0.765
```

Originally I had made an arithmetic error converting (10-5)/8 to 1/2. The experiment made me recheck my work, and the experimental results were correct.
