# Issue 6672: Elliptic curve isogeny coercion of output to codomain curve takes too long

Issue created by migration from Trac.

Original creator: shumow

Original creation time: 2009-08-04 02:21:57

Assignee: shumow

CC:  shumow@gmail.com

As per William's debugging, the correct behavior is to coerce the tuple with check=False.

On Mon, Aug 3, 2009 at 6:10 PM, VictorMiller<victorsmiller`@`gmail.com> wrote:
>
> Sorry, here's the definition of Q:
>
> Q = E.random_element()
>
> Victor
>
> On Aug 3, 8:45 pm, Simon King <simon.k...`@`nuigalway.ie> wrote:
>> Hi!
>>
>> On 4 Aug., 02:31, VictorMiller <victorsmil...`@`gmail.com> wrote:
>>
>> > Here are the commands I used:
>>
>> > qq = [z for z in primes(100000,100000+100) if (z%12) == 11]
>> > E = EllipticCurve(j=GF(qq[0])(1728))
>> > # E has qq[0]+1 points over GF(qq[0])
>> > factor(qq[0]+1)
>> > P = ((qq[0]+1)//3)*E.random_element()
>> > K = [E(0),P,-P]
>> > phi = E.isogeny(K)

There appears to be a memory leak -- or some sort of caching (!) -- in
the code to evaluate phi.  This is likely impacting the complexity of
the some code that is run during the computation of phi(P).  The log
below shows that memory usage increases upon evaluation of phi(P):


```
sage: get_memory_usage()
210.109375
sage: timeit('phi(P)')
125 loops, best of 3: 7.13 ms per loop
sage: get_memory_usage()
210.609375
sage: timeit('phi(P)')
125 loops, best of 3: 7.3 ms per loop
sage: get_memory_usage()
211.109375
sage: timeit('phi(P)')
125 loops, best of 3: 7.49 ms per loop
sage: get_memory_usage()
211.609375
sage: timeit('phi(P)')
125 loops, best of 3: 7.69 ms per loop
sage: get_memory_usage()
212.109375
```


Now I looked at the source code for the function phi(P) =
phi.__call__(P) and bisected by putting early returns in.  If you
change

```
       else:
           outP = self.__E2(outP)
```

to

```
       else:
           return outP
           outP = self.__E2(outP)
```


in that function in ell_curve_isogeny.py (around line 875), then the
leak and slowdown vanishes.

Thus the real problem is in the "trivial" line "self.__E2(outP)",
which by the way takes even in good cases like 10 times as long as the
rest of the whole function put together.  Indeed, coercing a point
into a curve is a horrendous disaster (this is the real problem,
forget the isogeny stuff):


```
sage: get_memory_usage()
195.81640625
sage: timeit('E(P)')
625 loops, best of 3: 4.24 ms per loop
sage: get_memory_usage()
201.31640625
```


In fact, the function E.point is to blame, evidently:


```
sage: timeit('E.point(P)')
125 loops, best of 3: 4.13 ms per loop
sage: get_memory_usage()
202.08984375
sage: timeit('E.point(P)')
125 loops, best of 3: 4.4 ms per loop
sage: get_memory_usage()
203.08984375
```


... but *ONLY* with check=True (the default):


```
sage: timeit('E.point(P,check=False)')
625 loops, best of 3: 8.26 µs per loop
sage: get_memory_usage()
203.08984375
sage: timeit('E.point(P,check=False)')
625 loops, best of 3: 7.29 µs per loop
sage: get_memory_usage()
203.08984375
```


I.e., we get a speedup of a factor of nearly 1000 by using
check=False, plus the leak goes away.    So in the check -- which
involves arithmetic -- maybe the coercion model is surely being
invoked at some point (I guess), and that is perhaps caching
information, thus memory usage goes up and performance goes down.  I
don't know, I'm not looking further.

Going back to your original problem, if I change in ell_curve_isogeny.py


```
       else:
           outP = self.__E2(outP)
```


to


```
       else:
           outP = self.__E2.point(outP,check=False)
```


then we have the following, which is exactly what you would hope for
(things are fast,  no slowdown).


```
sage: qq = [z for z in primes(100000,100000+100) if (z%12) == 11]
sage: E = EllipticCurve(j=GF(qq[0])(1728))
sage: # E has qq[0]+1 points over GF(qq[0])
sage: factor(qq[0]+1)
2^2 * 3 * 5 * 1667
sage: P = ((qq[0]+1)//3)*E.random_element()
sage: K = [E(0),P,-P]
sage: phi = E.isogeny(K)
sage: get_memory_usage()
190.56640625
sage: timeit('phi(P)')
625 loops, best of 3: 69.8 µs per loop
sage: for i in xrange(20): timeit('phi(P)')

....:
625 loops, best of 3: 69.3 µs per loop
625 loops, best of 3: 69.3 µs per loop
625 loops, best of 3: 69.6 µs per loop
625 loops, best of 3: 69.9 µs per loop
625 loops, best of 3: 69.8 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 71.2 µs per loop
625 loops, best of 3: 69.3 µs per loop
625 loops, best of 3: 70.8 µs per loop
625 loops, best of 3: 69.2 µs per loop
625 loops, best of 3: 70.2 µs per loop
625 loops, best of 3: 70.7 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 71 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 70.2 µs per loop
625 loops, best of 3: 70.1 µs per loop
625 loops, best of 3: 70 µs per loop
625 loops, best of 3: 70.1 µs per loop
625 loops, best of 3: 70.1 µs per loop
```


The above change is very sensible, since we know that outP is on
self.__E2, so should directly create a point on E2 and not check again
that our point is really on E2 (which is very expensive).

I hope the above is helpful and that somebody opens a trac ticket and
submits a patch.    I have to get back to what I was doing...   I also
hope the above email provides some ideas as to how to quickly get to
the bottom of questions like this.  Note that I did all this in < 10
minutes by using ?? to see where relevant source code is, putting in
some return statements (often better than print statements), and
knowing that P(...) means P.__call__.

 -- William


---

Attachment


---

Comment by cremona created at 2009-08-16 17:53:39

Apply after previous


---

Attachment

Apply after previous


---

Comment by cremona created at 2009-08-16 17:56:08

Trac just lost my long comment, explaining what I did complete with test data and timings.  Reviewer can ask me if they want to know.


---

Comment by AlexGhitza created at 2009-08-17 12:34:26

Positive review.  Apply the three patches in order.

Tested on some random examples such as:

BEFORE THE PATCHES:

```
sage: E = EllipticCurve('109a').change_ring(GF(71))
sage: lis = E.rational_points()
sage: P = lis[20]
sage: timeit('E(P)')
625 loops, best of 3: 840 µs per loop
```


AFTER THE PATCHES:


```
sage: E = EllipticCurve('109a').change_ring(GF(71))
sage: lis = E.rational_points()
sage: P = lis[20]
sage: timeit('E(P)')
625 loops, best of 3: 191 µs per loop
```



---

Comment by mvngu created at 2009-08-23 14:25:14

Resolution: fixed
