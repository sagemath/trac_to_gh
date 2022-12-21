# Issue 2090: basic univariate polynomial efficiency issues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-07 22:14:38

Assignee: somebody


```
Marshall Buck to sage-support

(sage 2.10 on X86 linux.)

Suppose you define the ring of polynomials over GF(2):

R.<x> = GF(2)[]

Then a simple polynomial like

f = x^32000

takes time quadratic in the degree to construct.
Meanwhile, the left shift operator will construct the polynomial
almost instantly:

f = x << (32000 - 1)

Also, constructing from a list of coefficients takes quadratic time if
most of the coefficients are zero.

For example

f = R( [1]+ 32000*[0] + [1])

is very slow, but a dense list is fast:

f = R(32000*[1])
```



---

Comment by was created at 2010-11-22 20:22:40

Resolution: fixed


---

Comment by was created at 2010-11-22 20:22:40

From James Pfeiffer  from a Math 581d homework problem.

"Is this still open for a reason?

```
    sage: sage: R.<x> = GF(2)[]
    sage: timeit('f = x^32000')
        625 loops, best of 3: 3.72 µs per loop
    sage: timeit('x << (32000 - 1)')
        625 loops, best of 3: 12.9 µs per loop
```

 I could just close the ticket, as it seems to be addressed."

Good point.  It is definitely addressed. Closing.
