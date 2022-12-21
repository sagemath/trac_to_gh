# Issue 5107: incorrect trailing digits for continued fraction

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-01-26 19:52:27

Assignee: somebody


```
continued_fraction(sqrt(2))
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]

the last two digits are incorrect

continued_fraction(sqrt(109))
[10, 2, 3, 1, 2, 4, 1, 6, 6, 1, 4, 2, 1, 3, 2, 20, 3]

the last digit (3) is incorrect
```


See http://groups.google.com/group/sage-devel/browse_thread/thread/ab840e109863fcf3/c38d571a161b7628


---

Comment by mabshoff created at 2009-02-06 22:58:18

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-08-25 05:32:55

The computation is done in the function `continued_fraction_list()` of `rings/arith.py`, where it says "This may be slow for real number input, since it's implemented in pure Python. For rational number input the PARI C library is used."

I wonder why we're not using PARI also when the input is a real number.  It's fast, and it looks right:


```
sage: x = sqrt(2)
sage: CFF = ContinuedFractionField()
sage: CFF(pari(x).contfrac().python())
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
sage: timeit("CFF(pari(x).contfrac().python())
625 loops, best of 3: 258 µs per loop
sage: timeit("CFF(continued_fraction_list(x))")
625 loops, best of 3: 1.17 ms per loop
```



---

Attachment


---

Comment by was created at 2010-01-18 09:24:50

Hi,

I've looked through this carefully.

 1. I strongly disagree that any of the examples above are bugs.  They are the result of users misunderstanding what the `continued_fraction` function is supposed to do.  This may be partly because that function has 0 documentation!   

 2. Regarding speed: correctness is much more important for starters, and it's also good to have a precise definition of exactly what is being computed.  That is impossible to do in PARI, mainly because of how PARI's precision can't be set exactly in bits.   This is difficult to appreciate without the function continued_fraction being documented.  The right way to make this function faster is to just reimplement continued_fraction_list in Cython. 

So, I've attached a patch that:

  1. Brings the coverage of contfrac.py to 100%.

  2. Explains in detail what continued_fraction is actually supposed to compute.  

  3. Changes the docs in the whole contfrac.py file to use ReST formatting. 


It doesn't change what anything actually does in any significant way.


---

Comment by was created at 2010-01-18 09:24:50

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-18 18:39:43

Positive review, except for two minor typos which I'm adding a separate patch for.


---

Attachment

I find it surprising that `continued_fraction(x)`, where x is symbolic, or even an exact rational, would only give me the continued fraction of a numerical approximation to some number of bits. I guess what would be ideal would be an ideal, lazy continued fraction class. What I would find more useful than bits would be an nterms parameter that specified the (minimum?) number of terms to give, and it would work with sufficient precision to deduce all nterms coefficients correctly (e.g. using interval arithmetic). 

The fact that it's not documented is a huge step forward, so +1 to that.


---

Comment by robertwb created at 2010-01-18 19:10:11

I guess I should say regarding the "incorrect" results above, that "this function doesn't do what it looks like it does, read the documentation" which is somewaht unsatisfactory.


---

Comment by was created at 2010-01-18 22:34:15

+1 to the referee patch.  
Robert: You expected continued_fraction(symbolic) would be some cool lazy infinite continued fraction object, since the function "continued_fraction" didn't have any documentation.   It would be nice to have that capability, but nobody has written it.    At least now continued_fraction clearly documents what it does.       

Perhaps the only thing that would easily make you happy right now would be to require the prec option if the input is symbolic?  That way in the future when somebody writes "continued_fraction(pi)", then it will work as you want...  Thoughts?


---

Comment by AlexGhitza created at 2010-01-20 09:53:11

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-01-20 09:53:11

I interpret the discussion above as: (a) William's patch gets a positive review from Willem, (b) Willem's referee patch gets a positive review from William, and (c) there are improvements we should make to the continued fractions code, which should probably be a new enhancement ticket.


---

Comment by mvngu created at 2010-01-22 18:27:44

Resolution: fixed
