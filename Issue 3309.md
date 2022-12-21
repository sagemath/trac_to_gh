# Issue 3309: massively optimize the binomial function when an input is real or complex floating point

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-26 17:46:19

Assignee: somebody


```
Hi Sage-Devel,

This email was to pari-devel, but is also directly relevant
to sage.   See my comment on the bottom below.  (I didn't
both to respond to the pari list because all my emails 
there bounce.)

On Mon, May 26, 2008 at 9:56 AM, Robert Gerbicz <robert.gerbicz`@`gmail.com> wrote:
> I'm really surprised that computing binomial numbers for floating point
> real/complex numbers so slow in Pari-Gp. For example:
> binomial(1140000.78,420000) takes about 6 seconds and more than 22 MB Ram on
> my computer.
> A much faster way:
> F(n,k)=gamma(n+1)/gamma(k+1)/gamma(n-k+1) gives binomial(n,k)

Great idea in the case when the first input to binomial is 
floating point. 

In Sage on my laptop:

sage: time a = binomial(RR(1140000.78), 420000)
CPU times: user 3.64 s, sys: 0.10 s, total: 3.73 s
Wall time: 3.76 s

Using your trick:
sage: F = lambda n,k: gamma(n+1)/gamma(k+1)/gamma(n-k+1)
sage: time b = F(RR(1140000.78),RR(420000))
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s

More precisely:
sage: timeit('F(RR(1140000.78),RR(420000))')
625 loops, best of 3: 422 µs per loop
sage: timeit('binomial(RR(1140000.78), 420000)')
5 loops, best of 3: 3.3 s per loop

So your suggestion is about 8000 times faster.

Note though that due to rounding the answers are different:

sage: a
2.99132584452787e325824
sage: b
2.99132584452800e325824
sage: a - b
-1.27118374810324e325811

Which is closer?  Definitely your formula using Gamma
gives a closer answer as i checked using interval
arithmetic to high precision:

sage: time a = binomial(RealIntervalField(1000)(1140000.78), 420000)
CPU times: user 6.33 s, sys: 0.26 s, total: 6.59 s
Wall time: 6.73 s
sage: a
[2.99132584452799583218670664806377915421591194817285057236221072979355793880728013777098522886127668070007188360739556123884662805319772820601950625710807401405804394169293082156154447701434820854783425949844303667313131986630753419142150368691407480323325019595168489899361691122207010886385330597605904e325824 .. 2.99132584452799583218670664806377915421591194817285057236221072979355793880728013777098522886127668070007188360739556123884662805319772820601950625710807401405804394169293082156154447701434820854783425949844303667313131986630753419142150368691407480323325019595168489899361691122207010886385330598928089e325824]


Doing 
sage: binomial??
shows that Sage's binomial function is not calling PARI
in this case (since the first input isn't an int), but presumably
Sage and PARI are implementing the same algorithm.

    if isinstance(x, (int, long, integer.Integer)):
        return integer_ring.ZZ(pari(x).binomial(m))
    try:
        P = x.parent()
    except AttributeError:
        P = type(x)
    if m < 0:
        return P(0)
    return misc.prod([x-i for i in xrange(m)]) / P(factorial(m))

I think making the gamma optimization you suggest when
the first input is floating point real or complex is a great
idea.  

```



---

Comment by was created at 2008-06-10 23:23:17

It looks like this will get fixed in an upcoming version of PARI:

```
* Robert Gerbicz [2008-05-26 19:02]:
- Show quoted text -
> I'm really surprised that computing binomial numbers for floating point
> real/complex numbers so slow in Pari-Gp. For example:
> binomial(1140000.78,420000) takes about 6 seconds and more than 22 MB Ram on
> my computer.
> A much faster way:
> F(n,k)=gamma(n+1)/gamma(k+1)/gamma(n-k+1) gives binomial(n,k)

Nobody had really needed it, but it's indeed easy to improve...

Not quite so simple as the above though, since gamma() becomes relatively more
costly as the precision increases:

(00:36) gp > \p1000
  realprecision = 1001 significant digits (1000 digits displayed)
(01:03) gp > for(i=1,10, F(1140000.78,100))
time = 709 ms.

(01:03) gp > for(i=1,10, binomial(1140000.78,  100))
time = 56 ms.
(01:05) gp > for(i=1,10, binomial(1140000.78, 1000))
time = 509 ms.

At this accuracy (\p1000) the threshold in favour of the gamma quotient is
around k ~ 1400, for binomial(n, k)  [ k <= n/2 ]



I have committed an improved version to svn.

Thanks for pointing this out,
Karim
```



---

Comment by ddrake created at 2009-03-24 00:49:55

Has this improvement been implemented in Pari yet? With Sage 3.4, I still see the above slowness, and the gamma() suggestion is over 1000 times faster than the current implementation with the above example.


---

Comment by ddrake created at 2009-03-24 06:46:00

I'm attaching a patch which uses gamma() when appropriate. We can use this until we get the fast Pari stuff in. Here are some timings:


```
BEFORE
sage: x, y = 1140000.78, 420000
sage: %timeit binomial(x, y)
10 loops, best of 3: 1.03 s per loop

sage: x, y = RR(pi^5), 10
sage: %timeit binomial(x, y)      
10000 loops, best of 3: 28.8 µs per loop

sage: x, y = RR(pi^15), 500
sage: %timeit binomial(x, y)
1000 loops, best of 3: 864 µs per loop

sage: x, y = RealField(500)(1729000*sqrt(2)), 17000
sage: %timeit binomial(x, y)                        
10 loops, best of 3: 35.8 ms per loop
```


With the patch:


```
AFTER
sage: x, y = 1140000.78, 420000
sage: %timeit binomial(x, y)
1000 loops, best of 3: 302 µs per loop

sage: x, y = RR(pi^5), 10
sage: %timeit binomial(x, y)
10000 loops, best of 3: 188 µs per loop

sage: x, y = RR(pi^15), 500
sage: %timeit binomial(x, y)
1000 loops, best of 3: 362 µs per loop

sage: x, y = RealField(500)(1729000*sqrt(2)), 17000
sage: %timeit binomial(x, y)                       
1000 loops, best of 3: 743 µs per loop
```



---

Attachment


---

Attachment


---

Comment by mabshoff created at 2009-04-13 02:25:43

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 02:25:43

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael
