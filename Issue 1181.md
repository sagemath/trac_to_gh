# Issue 1181: polynomial/fraction field __hash__ re-write

Issue created by migration from https://trac.sagemath.org/ticket/1181

Original creator: jbmohler

Original creation time: 2007-11-15 22:07:38

Assignee: somebody

The attached patch has a number of goals.
 1.  Allow shared members of ZZ and ZZ[x] to be used interchangeably in a dictionary.
 2.  Replace ZZ in !#1 by QQ, IntegerModRing(p) and probably a bunch of other things.
 3.  Replace ZZ[x] in !#1 by ZZ[x,y,...]
 4.  Allow shared members of FractionFields and their base rings to be used interchangeably in a dictionary.
 5.  Make the __hash__ function faster in polynomial rings

Goal !#5 was achieved very nicely for univariate poly rings, but __hash__ in QQ[x,y] was extremely fast in the original code.  Unfortunately, that very fast __hash__ violated all good things of the goals above.  It also wasn't asymptotically fast (think huge numerical coefficients).

The goals 1-4 above result in a fix for the subs method:

```
sage: R.<x,y>=ZZ[]
sage: (x/y).subs({x:1})
1/y  # produced x/y in the old version
```


A bad thing about this patch is that the results of hash(x) changing reorders the output of things that come from a dictionary.  There is a number of doc-tests output changes which are only a matter of order in the list.  I think this is probably bad style in doc-tests and in real life.  At least some of those outputs have a very natural order (to the human mind if not mathematically).

The attached patch entirely supersedes #1075 and I'm going to go close it right now.


---

Comment by jbmohler created at 2007-11-16 12:31:43

Some benchmarks:

Original:

```
sage: R.<x>=ZZ[]
sage: one=R(1)
sage: f=x^2+2*x+1
sage: timeit hash(one)
1000000 loops, best of 3: 1.03 Âµs per loop
sage: timeit hash(f)
100000 loops, best of 3: 3.53 Âµs per loop
sage: timeit hash(x)
100000 loops, best of 3: 2.91 Âµs per loop
sage: R.<x,y>=QQ[]
sage: one=R(1)
sage: f=x^2+2*y+1
sage: timeit hash(one)
1000000 loops, best of 3: 931 ns per loop
sage: timeit hash(f)
1000000 loops, best of 3: 1.86 Âµs per loop
sage: timeit hash(x)
1000000 loops, best of 3: 486 ns per loop
```


Patched:

```
sage: # first the success
sage: R.<x>=ZZ[]
sage: one=R(1)
sage: f=x^2+2*x+1
sage: timeit hash(one)
1000000 loops, best of 3: 1.04 Âµs per loop
sage: timeit hash(f)
1000000 loops, best of 3: 1.98 Âµs per loop
sage: timeit hash(x)
1000000 loops, best of 3: 1.4 Âµs per loop
sage: # second: the huge slowdown
sage: R.<x,y>=QQ[]
sage: one=R(1)
sage: f=x^2+2*y+1
sage: timeit hash(one)
100000 loops, best of 3: 2.88 Âµs per loop
sage: timeit hash(f)
100000 loops, best of 3: 6.31 Âµs per loop
sage: timeit hash(x)
100000 loops, best of 3: 3.18 Âµs per loop
```


I believe (but haven't verified too much) that the big problem is converting coefficients to the base ring from the singular poly.  This should probably be optimized for a whole bunch of reasons other than hashing, which will carry over to hashing.


---

Comment by jbmohler created at 2007-11-16 12:44:43

the patch


---

Attachment


---

Comment by robertwb created at 2007-12-02 09:06:12

I've looked at the code and tried it out and it is a great idea that works well. Despite multivariate hashes slowing down, they are still really quite fast, and the properties listed are much more important.


---

Comment by mabshoff created at 2007-12-02 20:27:25

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 20:27:25

Resolution: fixed
