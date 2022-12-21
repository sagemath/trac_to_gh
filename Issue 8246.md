# Issue 8246: Carmichael lambda function for the Blum-Blum-Shub pseudorandom bit generator

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-02-12 05:25:55

Assignee: mvngu

CC:  wdj

Add a new function to calculate the Carmichael lambda function of a positive integer n. The Carmichael lambda function is related to the Blum-Blum-Shub pseudorandom bit generator. See [Wikipedia](http://en.wikipedia.org/wiki/Carmichael_function) for a definition, and [Mathematica documentation center](http://reference.wolfram.com/mathematica/ref/CarmichaelLambda.html) for examples.

*Prerequisites:* #7746


---

Comment by mvngu created at 2010-02-12 05:26:35

initial public domain version by Mike Hogan and David Joyner; for reference only


---

Attachment

based on Sage 4.3.2; depends on #7746


---

Comment by mvngu created at 2010-02-13 04:08:54

%timeit time in microseconds for Hogan & Joyner's implementation


---

Attachment

%timeit time in microseconds for newer implementation


---

Attachment

comparison between old (blue) and new (red) implementations


---

Attachment

The attachment [trac_8246-carmichael.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/trac_8246-carmichael.patch) provides a non-recursive implementation of the Carmichael function. This is in contrast to the recursive implementation as contained in [BBScrypto.sage](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/BBScrypto.sage). I have provided some timing comparison to justify the non-recursive implementation. Say [BBScrypto.sage](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/BBScrypto.sage) is at `/home/mvngu/BBScrypto.sage` and [trac_8246-carmichael.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/trac_8246-carmichael.patch) has been applied to Sage 4.3.2. The following generates some timing statistics for both Hogan & Joyner's implementation, and the non-recursive implementation. Here are some timing statistics for the recursive implementation, where the timing results (in microseconds) are saved to [carmichael.old](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/carmichael.old):

```
sage: load("/home/mvngu/BBScrypto.sage")
sage: T = []
sage: for n in xrange(1, 1001):
....:     t = %timeit carmichael(n)
....:     T.append(t.stats[3])
....:     
sage: f = open("/home/mvngu/carmichael.old", "w")
sage: for t in T:
....:     f.write(str(t) + "\n")
....:     
sage: f.close()
```


The following are some timing statistics for the non-recursive implementation. Timing results (in microseconds) are saved to [carmichael.new](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/carmichael.new):

```
sage: from sage.crypto.util import carmichael_lambda
sage: T = []
sage: for n in xrange(1, 1001):
....:     t = %timeit carmichael_lambda(n)
....:     T.append(t.stats[3])
....:     
sage: # First 10 elements of T are timings in nanoseconds. 
sage: # So convert them to microseconds.
sage: for i in xrange(10):
....:     T[i] = T[i] / 1000
....:     
sage: f = open("/home/mvngu/carmichael.new", "w")
sage: for t in T:
....:     f.write(str(t) + "\n")
....:     
sage: f.close()
```


Now plot the timing results. The plot in blue is for the recursive implementation, while the plot in red is for the non-recursive implementation. The horizontal axis is for integer values of `n` starting from 1, up to and including 1000. The vertical axis is for the values of the Carmichael function of `n`. The resulting combined plot is contained in [benchmark-carmichael.png](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/benchmark-carmichael.png). Timing statistics were obtained using the machine `sage.math`.

```
sage: X = [1..1000]
sage: Yold = []
sage: f = open("/home/mvngu/carmichael.old", "r")
sage: for t in f:
....:     Yold.append(RR(t.strip()))
....:     
sage: f.close()
sage: Ynew = []
sage: f = open("/home/mvngu/carmichael.new", "r")
sage: for t in f:
....:     Ynew.append(RR(t.strip()))
....:     
sage: f.close()
sage: Pold = line2d(zip(X, Yold), color="blue", thickness=1)
sage: Pnew = line2d(zip(X, Ynew), color="red", thickness=1)
sage: Pold + Pnew
```

First apply #7746 and then [trac_8246-carmichael.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/trac_8246-carmichael.patch).


---

Comment by mvngu created at 2010-02-13 04:29:02

Changing status from new to needs_review.


---

Comment by wdj created at 2010-02-13 17:40:10

Applies fine to 4.3.3.a0 on a mac 10.6.2. Passes sage -testall and the reference manual/documentation looks good.

Positive review. 

I should add that this is a completely different, and much faster, implementation that the Wikipedia one (which is the one originally submitted). 

Thanks again Minh!


---

Comment by wdj created at 2010-02-13 17:40:10

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-15 03:43:55

Resolution: fixed


---

Comment by mvngu created at 2010-02-15 03:43:55

Merged [trac_8246-carmichael.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8246/trac_8246-carmichael.patch).


---

Comment by ylchapuy created at 2010-02-15 17:19:24

Sorry to comment that late, but there are a few things in this patch I dislike:

 * Why hard code the first ten values?
 * `carmichael_lambda(16)` is of type `sage.rings.rational.Rational`
 * why use generic_power to compute the power of an integer?

here's my 2-cents implementation:


```

def carmichael_lambda(n):
    n = Integer(n)

    if n < 1: 
        raise ValueError("Input n must be a positive integer.")

    F = n.factor()
    L = []

    # first get rid of the even part
    if n & 1 == 0:
        e = F[0][1]
        F = F[1:]
        if e < 3:
            e = e-1
        else:
            e = e-2
        L.append(1<<e)
    
    # then other prime factors
    L += [ p**(k-1)*(p-1) for p,k in F]

    # finish the job
    return lcm(L)

```



---

Comment by wdj created at 2010-02-15 17:55:24

Replying to [comment:4 ylchapuy]:
> Sorry to comment that late, but there are a few things in this patch I dislike:
> ...

Did you test to see if your implementation was faster than the current one. If so, what were the results?


---

Comment by ylchapuy created at 2010-02-15 19:20:40

Replying to [comment:5 wdj]:
> Replying to [comment:4 ylchapuy]:
> > Sorry to comment that late, but there are a few things in this patch I dislike:
> > ...
> 
> Did you test to see if your implementation was faster than the current one. If so, what were the results?

Except if n<=10, timings are very similar, mine being slightly faster.
To obtain an even faster version one can replace the final lcm with `sage.rings.integer.LCM_list(L)`.

e.g.

```
sage: %timeit carmichael_lambda(1000)     # Minh's version
625 loops, best of 3: 270 µs per loop
sage: %timeit my_carmichael_lambda(1000)  # mine with lcm
625 loops, best of 3: 244 µs per loop
sage: %timeit my_carmichael_lambda2(1000) # mine with sage.rings.integer.LCM_list
625 loops, best of 3: 214 µs per loop
sage: %timeit factor(1000)                # just to compare
625 loops, best of 3: 177 µs per loop
```


we can see that most of the time is spent factoring.


---

Comment by wdj created at 2010-02-15 21:01:02

For me, a small speed up does not matter. The function is used theoretically in security estimates for the BBS stream cipher. I'm not saying that you should not try to speed things up, it is just that it is more important for the function to exist in Sage that for it to be fast. But if someone wants me to referee a new patch, that is fine too.


---

Comment by ylchapuy created at 2010-02-15 21:25:35

Replying to [comment:7 wdj]:
> For me, a small speed up does not matter. The function is used theoretically in security estimates for the BBS stream cipher. 

I totally agree on this, but you asked for speed results! I didn't mentionned speed at all in my first message.

> I'm not saying that you should not try to speed things up,

It's definitely not what I'm trying to do.

> it is just that it is more important for the function to exist in Sage that for it to be fast. But if someone wants me to referee a new patch, that is fine too.

My point was:

 * there is a bug: e.g. carmichael_lambda(16) is of type sage.rings.rational.Rational ;
 * a small speed up does not matter: therefore no need to hard code the first 10 cases, it just makes the code less readable ;
 * my code is IMHO just easier to read.


---

Comment by mvngu created at 2010-02-16 04:21:53

Replying to [comment:8 ylchapuy]:
> My point was:
> 
 * there is a bug: e.g. carmichael_lambda(16) is of type sage.rings.rational.Rational ;
 * a small speed up does not matter: therefore no need to hard code the first 10 cases, it just makes the code less readable ;
 * my code is IMHO just easier to read.
>
The patch is already merged. To reopen this ticket would result in confusion for release managers. Can I persuade you to open a ticket to get your implementation into Sage? It's always nice to have an expert look over a novice's work.


---

Comment by wdj created at 2010-02-16 12:15:51

Replying to [comment:9 mvngu]:
> Replying to [comment:8 ylchapuy]:

...

> Can I persuade you to open a ticket to get your implementation into Sage? 

I'll try to remember to do this myself later today.


---

Comment by wdj created at 2010-02-16 16:36:47

This issue is now http://trac.sagemath.org/sage_trac/ticket/8283
