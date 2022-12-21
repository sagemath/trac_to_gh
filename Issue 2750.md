# Issue 2750: Implement GF(p^n) as relative extension of GF(p^d)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-01 12:04:12

Assignee: somebody

CC:  robertwb dmharvey mderickx

Over at #2384 Robert wrote:
> On another note, I think I remember hearing somewhere that magma uses zech logs as 
> coefficients, e.g. GF(p<sup>n</sup>) is implemented as a relative extension of GF(p<sup>d</sup>) 
> where p<sup>d</sup> is small enough for the log representation. Would this be worth looking
> at?

and David replied:
> This would only work when n is sufficiently composite, but in that case I think
> it's a great idea. Still, you need to have very good generic polynomial arithmetic
> to make this work. I think this is something to work on later.


---

Comment by ylchapuy created at 2009-11-19 01:10:07

Some references on how Magma works.

www.math.ru.nl/~bosma/pubs/JSC1997FiFi.pdf
