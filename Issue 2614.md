# Issue 2614: [with patch, needs review] MPolynomial coefficient/polynomial_coefficient merging

Issue created by migration from https://trac.sagemath.org/ticket/2614

Original creator: jbmohler

Original creation time: 2008-03-20 14:46:25

Assignee: was

Keywords: multivariate coefficient

This ticket is a continuation and final aim of #2385.  I was hoping to generate a bit of discussion with that patch, but it got merged before the discussion was generated.

The end result is this (illustrated with ZZ, but applying equally to QQ):

```
sage: R.<x,y,z> = ZZ[]
sage: f=(-x^2-x+3)*(y-1)
sage: f
-1*x^2*y + x^2 - x*y + x + 3*y - 3
sage: f.coefficient(x^1)
-1*y + 1
sage: f.coefficient(x^0)
-1*x^2*y + x^2 - x*y + x + 3*y - 3
sage: f.coefficient({x:0})
3*y - 3
sage: f.coefficient([0,None,None])
3*y - 3
```


Note that the "f.coefficient(x^0)" is possibly mis-leading and this motivated both #2385 and this ticket.  Note that for ZZ "f.coefficient(x^0)" actually returned the constant coefficient as a special case -- I think that was dead wrong.


---

Comment by jbmohler created at 2008-03-20 14:50:33

Changing component from algebraic geometry to commutative algebra.


---

Comment by jbmohler created at 2008-03-20 14:50:33

Changing assignee from was to malb.


---

Comment by dfdeshom created at 2008-03-20 18:13:50

I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?


---

Comment by jbmohler created at 2008-03-20 19:00:32

Replying to [comment:3 dfdeshom]:
> I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?
>  

What do you mean by "restriction on a constant"?  Is this bit what you are talking about:

>Note that for ZZ "f.coefficient(x0)" actually returned the constant coefficient as a special case -- I think that was dead wrong.

Perhaps I should have said:  In the current 2.10.4 code "f.coefficient(x<sup>0</sup>)" returns the constant coefficient -- I think this is dead wrong.

I feel like I might be missing the point of your question.  If so, please clarify!


---

Comment by dfdeshom created at 2008-03-20 19:37:31

Replying to [comment:4 jbmohler]:
> Replying to [comment:3 dfdeshom]:
> > I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?
> >  
> 
> What do you mean by "restriction on a constant"?  Is this bit what you are talking about:
> 
> >Note that for ZZ "f.coefficient(x0)" actually returned the constant coefficient as a special case -- I think that was dead wrong.

Actually, you were crystal clear. I was confused: I thought f was a mpoly in x and y only and was asking why you were doing `f.coefficient([0,None,None])`.


---

Comment by AlexGhitza created at 2008-03-28 14:31:33

Looks good.  I think it makes things much clearer than before, and the doctests are good.


---

Comment by mabshoff created at 2008-03-28 15:20:36

Sorry, the patch no longer applies cleanly. Please rebase against 2.11.alpha2 out shortly:

```
sage-2.11.alpha2/devel/sage$ patch -p1 --dry-run < trac_2614_mpoly-coeff.patch
patching file sage/rings/polynomial/multi_polynomial_element.py
Hunk #1 succeeded at 428 (offset -2 lines).
Hunk #2 succeeded at 439 with fuzz 1 (offset -2 lines).
Hunk #3 succeeded at 538 (offset -1 lines).
Hunk #4 succeeded at 550 (offset -1 lines).
Hunk #5 FAILED at 564.
Hunk #6 succeeded at 600 (offset -1 lines).
Hunk #7 succeeded at 612 (offset -1 lines).
1 out of 7 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #1 succeeded at 2175 (offset 4 lines).
Hunk #2 succeeded at 2187 (offset 4 lines).
Hunk #3 succeeded at 2201 (offset 4 lines).
Hunk #4 succeeded at 2226 (offset 4 lines).
Hunk #5 succeeded at 2238 (offset 4 lines).
Hunk #6 succeeded at 2288 (offset 4 lines).
Hunk #7 succeeded at 2299 (offset 4 lines).
Hunk #8 succeeded at 2495 (offset 4 lines).
```



---

Comment by jbmohler created at 2008-03-28 18:11:01

rebased against 2.11.alpha2 (or some approximation there-of)


---

Attachment

The current patch is re-based against 2.11.alpha1 augmented with patches from mabshoff's alpha2 release cycle directory.  I don't have a build of this to really test, but I believe doc-tests should pass.

If this is not integrated by the time alpha2 is released, I'll probably double-check some things with a built alpha2.


---

Comment by mabshoff created at 2008-03-28 18:21:12

The patch applies cleanly now. Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 18:21:12

Resolution: fixed
