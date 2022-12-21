# Issue 1289: serious problems with how ceil and floor are computed symbolically

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-27 14:34:11

Assignee: somebody

These are mostly the result of maxima getting used at some point to do the computation (except the one that leaves floor(a) symbolic?!)


```
sage: a = factorial(50) / e
sage: ceil(a)
11188719610782480421414879249141773426630319613740326700720324608
sage: floor(a)
floor(30414093201713378043612608166064768844377641568960512000000000000*e^-1)
sage: ceil(factorial(50) / n(e,20000))
11188719610782480504630258070757734324011354208865721592720336801
sage: floor(factorial(50) / n(e,20000))
11188719610782480504630258070757734324011354208865721592720336800
sage: int(floor(a))
11188719610782479690664060583690314324787903255598816872754053120L
```


Basically the ceil and floor need to be improved to *not* fall back on Maxima,
but hopefully do something more sensible, especially when large numbers are
involved.  

I think this is an extremely important bug to fix, since it is something
that will come up in practice and produce wrong results, e.g., in a recent
patch by Dan Drake posted on sage-devel it *did*.


---

Comment by mhansen created at 2007-12-06 21:11:27

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-06 21:11:27

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2007-12-07 22:03:57

Since this is a maxima issue as well, I posted about it upstream:
http://www.math.utexas.edu/pipermail/maxima/2007/009327.html


---

Attachment


---

Comment by was created at 2008-01-17 01:48:01

Some irc conversation about this with examples:

```
17:34 < was-1289> Does the algorithm you implemented actually provably work?
17:35 < was-1289> I'm having a little trouble seeing why it should always work.
17:36 < mhansen> No, I don't think that it will always work, but I haven't found a case where it hasn't 
                 yet.  According to Fateman's posts, you won't ever be able to get something that 
                 provably works in general.
17:37 < was-1289> It should say that in the documentation!
17:37 < was-1289> :-)
17:37 < was-1289> I wonder if Fateman is right though.
17:37 < was-1289> I haven't got that far.
17:37 < mhansen> There is a result from the 60s on this sort of thing.
17:38 < was-1289> Then he says "For expression in some subclass of what is allowed in Maxima, there are
17:38 < was-1289> possibilities."
17:38 < was-1289> Certainly for an arbitrary number given by an algorithm, it is impossible to decide if 
                  a number is 0 or not.
17:38 < was-1289> That's really easy to see, since it happens all the time that one can't
17:38 < was-1289> easily decide.
17:39 < was-1289> But if the number is of a fairly restricted form, I bet the situation is different.
17:39 < was-1289> Hmm.
17:40 < mhansen> I really don't know enough of the mathematics in this area.  But, what is up there 
                 certainly improves things from before.
17:40 < was-1289> your code gets this wrong:
17:40 < was-1289> sage: a = SR(10^50 + 10^(-50))
17:40 < was-1289> sage: ceil(a)
17:40 < was-1289> 100000000000000000000000000000000000000000000000000
17:41 < was-1289> If you started with a larger number of bits at the beginning, you would get the right 
                  answer.
17:41 < was-1289> sage: RealField(500)(a).ceil()
17:41 < was-1289> 100000000000000000000000000000000000000000000000001
17:42 < mhansen> Hmm....
17:42 < was-1289> Both Maple and Matheamtica have no trouble at all getting this right.
17:42 < was-1289> sage: maple(a).ceil()
17:42 < was-1289> 100000000000000000000000000000000000000000000000001
17:42 < was-1289> sage: mathematica(a).Ceiling()
17:42 < was-1289> 100000000000000000000000000000000000000000000000001
 [17:42] [was-1289(+i)] [2:#sage-devel(+ns)] [Act: 1]                                                    
[#sage-devel] 
```


Then Carl Witty comes to the rescue:

```
17:43 -!- cwitty_ is now known as cwitty
17:44 < mhansen> Yeah, I know that.
17:44 < was-1289> In my example, we could defeat it by first trying to coerce to QQ.
17:44 < was-1289> I.e., instead of trying RealField(n) first, try QQ first. If that works we're in great 
                  shap.
17:44 < mhansen> That seems like a reasonable plan.
17:45 < was-1289> I wonder what else we should do.
17:45 < cwitty> Here's another idea:
17:45 < cwitty> Coerce into increasingly precise intervals.
17:45 < cwitty> If you find an interval such that the lower and upper bound have the same ceiling, then 
                that's the answer.
17:46 < was-1289> How do we coerce into increasingly precise intervals?
17:46 < was-1289> got it.
17:46 < was-1289> That's a great idea!!!!
17:46 < was-1289> sage: RealIntervalField(500)(a)
17:46 < mhansen> Yeah, that's really nice.
17:46 < cwitty> If you find an interval that contains only one integer, then compare the original 
                symbolic expression against that integer to see if you can prove that it is less than 
                that integer, or greater than that integer, or equal to that integer.
17:47 < was-1289> mhansen -- can you implement it?
17:47 < mhansen> Yes, but I have to go meet someone for dinner now.  I will do it afterwards though.
17:47 < was-1289> ok
17:47 -!- mhansen is now known as mhansen-dinner
}}}}


---

Attachment


---

Comment by mhansen created at 2008-01-17 05:45:05

New patch up implementing the interval method.


---

Comment by mabshoff created at 2008-01-18 01:45:44

Positive review by wstein. Merged in Sage 2.10.alpha4.


---

Comment by mabshoff created at 2008-01-18 01:45:44

Resolution: fixed
