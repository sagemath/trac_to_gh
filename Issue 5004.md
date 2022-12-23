# Issue 5004: bug in latexing of powers of negative numbers

Issue created by migration from https://trac.sagemath.org/ticket/5004

Original creator: was

Original creation time: 2009-01-17 21:29:04

Assignee: burcin


```
>
> Hello all
>
> The command latex(7-(-1)^(1/3))   produces 7 - {-1}^{\frac{1}{3}}
> Is it possible to change it into 7 - \left(-1\right)^{\frac{1}{3}}
>
> Which function should be redefined to gain this behavior?
>
> I think that two minus sign, one following the other, could be
> confusing (for students of economics, for example :) )
>
> Thank you
> Robert

I would start by doing:

sage: a = (-1)^(1/3)
sage: a._latex_??
[... source code in calculus.py...]

Then I would look at the code, and be confused for about an hour, finally probably figure out what is going on, and maybe with luck be able to fix this.
IIRC the code to get the latex for symbolic expressions is complicated.  I think it was written by Bobby Moretti (and undergrad who used to be a sage developer).

I think this sort of behavior, e.g.,

sage: a = (-1)^(1/4)
sage: latex(a)
{-1}^{\frac{1}{4}} 

should officially be considered a bug in fact.  It's not just confusing, it's wrong. 

By the way, one trick you can use is to convert the expression to maxima first and use its latex.  For some things, e.g., your example above, this works better:

sage: a = 7-(-1)^(1/3)
sage: latex(a._maxima_())
7-\left(-1\right)^`1}\over{3`

Don't use maxima(a), since then you'll get a in a session of maxima that has different defaults than the calculus module uses, in particular, roots are always assumed real, which may be bad (though maybe ok for economists):

sage: a = 7-(-1)^(1/3)
sage: latex(maxima(a))
8

 -- William
```



---

Attachment


---

Comment by was created at 2009-01-17 22:07:50

Looks great !  I'm glad you untangled the code.  

I doctested the whole tree and nothing breaks:


```
All tests passed!
Timings have been updated.
Total time for all tests: 145.9 seconds    
wstein@sage:/space/sage-3.2.3$ 
```


Yep, 145 seconds on the new hardware on a ram disk :-)

William


---

Comment by mabshoff created at 2009-01-18 15:57:22

Resolution: fixed


---

Comment by mabshoff created at 2009-01-18 15:57:22

Merged in Sage 3.3.alpha0
