# Issue 4804: add latex output for ceiling, floor, and derivative functions

Issue created by migration from https://trac.sagemath.org/ticket/4804

Original creator: was

Original creation time: 2008-12-15 15:38:30

Assignee: burcin

This could look better:

```
sage: latex(ceil(x) + floor(x) + derivative(floor(x)))
{{d}\over{d\,x}}\,\left \lfloor x \right \rfloor + \text{floor} \left( x \right) + \text{ceil} \left( x \right)
```


Notice that floor and ceil do not have special latex support except strangely inside the derivative. Also, the derivative would be better written as a partial derivative, since that's what it is in Sage in general. 

Also, this guy wrote to sage-support 3 or 4 times about this and was ignored:

```
Dear all,

I tried to reply my questions below to an existing thread (notation
for derivatives) but for some reason it didn't work. So I opened this
new one.

I use the derivative function and want to get an output in latex
style. At the moment the output looks quite good but imho it would be
nicer if it uses the "\partial" latex command. It is possible to
implement this? Further I use the floor and ceil functions. Would it
be possible to implement a latex output for these functions too?

Thanks,
Andreas
```



---

Comment by mhansen created at 2008-12-15 18:14:16

Changing status from new to assigned.


---

Comment by mhansen created at 2008-12-15 18:14:16

Changing assignee from burcin to mhansen.


---

Comment by whuss created at 2008-12-16 10:08:19

I don't agree with the positive review, since the change breaks the latex output for
maxima expressions:


```
sage: m = maxima('d/(d-2)')
sage: latex(m)
{{\partial}\over{d-2}}
```


Cheers,

Wilfried


---

Comment by mhansen created at 2008-12-16 11:28:31

Good catch. I've updated the patch to deal with this.


---

Comment by whuss created at 2008-12-16 13:46:24

It is still not correct:


```
sage: m = maxima('2*diff(f(x), x)')
sage: latex(m)
2\,\left({{d}\over{d\,x}}\,f\left(x\right)\right)
```


This should be changed in the maxima code, there
it should be trivial. Trying to guess what part
of the latex representation is a differential
seems very error prone to me.

Cheers,

Wilfried


---

Attachment


---

Comment by mhansen created at 2008-12-16 14:54:45

I put up a new plot which changes the tex code in maxima.  I'm not sure how to get rid of the \it's but they're harmless.


---

Comment by mhampton created at 2008-12-29 20:48:28

I will review this at some point today.


---

Comment by mhampton created at 2008-12-29 21:20:55

This seems to work.  I'm not sure that I agree that partial derivatives look better, but I don't feel strongly about it.  It certainly is better for multivariate cases.


---

Comment by mabshoff created at 2009-01-12 01:21:05

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-12 01:21:05

Resolution: fixed
