# Issue 8750: numerical noise on solaris

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-04-23 05:18:46

Assignee: drkirkby

CC:  mvngu

I'm getting noise on doctests on Solaris.  One is straightforward to fix (chmm.pyx).  For the other (time_series.pyx), on Solaris I get

```
sage -t  -long devel/sage/sage/finance/time_series.pyx
**********************************************************************
File "/home/palmieri/t2/sage-4.4.alpha2/devel/sage-main/sage/finance/time_series.pyx", line 691:
    sage: finance.TimeSeries([1,0,3]).log()
Expected:
    [0.0000, -inf, 1.0986]
Got:
    [0.0000, -Inf, 1.0986]
**********************************************************************
```

So instead of `-inf`, it's printing `-Inf`.  However, if I do

```
   sage: finance.TimeSeries([1,0,3]).log()[1]
```

then I see `-inf`.  So I've changed the doctest to use this instead.


---

Attachment

Two questions: 

 * Is sage/finance/time_series.pyx failing on every platform? I'm trying to understand why Solaris would give -inf and other system(s) -Inf. It seems to me that:


```
finance.TimeSeries([1,0,3]).log()
```

is a lot nicer than 

```
 finance.TimeSeries([1,0,3]).log()[1]
```


So is it right to change the test to a more complicated one, just to get the answer we want? If this comes from python, I find it hard to understand why there should be the difference. Would a case-insensitive test be a better method? 

 * Do we know what an exact (or high numerical precision value) to the answer of the problem in sage/stats/hmm/chmm.pyx is? I'm always a bit reluctant seeing numerical results, with no justification of the answer. The approach taken in these doc tests seems to be: "The answer is X, since I got X on my computer." Then someone gets a different answer on their computer, so the precision of the test is reduced. But rarely do I see much justification for the answer. (An exception has been in some problems like exp(1.0), where the exact answer is known, and we can be sure the problems are numerical rounding issues. 

When one reads things like how SQLite (Open Source) is tested

http://sqlite.org/testing.html

or how Wolfram Research claim Mathematica (closed source) is tested

http://reference.wolfram.com/mathematica/tutorial/TestingAndVerification.html

I'm personally left with the feeling the testing in Sage leaves a lot to be desired. 


Dave


---

Comment by jhpalmieri created at 2010-04-23 14:50:48

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-23 14:50:48

Replying to [comment:1 drkirkby]:
> Two questions: 
> 
>  * Is sage/finance/time_series.pyx failing on every platform? 

This is the only one, and I don't know why.  I could try compiling time_series.py with "-std=c99"; maybe that would help?

> So is it right to change the test to a more complicated one, just to get the answer we want?

If the difference are for trivial but insurmountable reasons, I don't have an issue with this.

> If this comes from python, I find it hard to understand why there should be the difference. 

Maybe it comes from math.h somehow?

>  * Do we know what an exact (or high numerical precision value) to the answer of the problem in sage/stats/hmm/chmm.pyx is? 

This is essentially a new file in the Sage library: in previous versions, it was marked with "nodoctest" at the top of the file.  I think that it no longer uses an external library either.  So I view this sort of change as working kinks out, and it doesn't bother me.


I'm always a bit reluctant seeing numerical results, with no justification of the answer. The approach taken in these doc tests seems to be: "The answer is X, since I got X on my computer." Then someone gets a different answer on their computer, so the precision of the test is reduced. But rarely do I see much justification for the answer. (An exception has been in some problems like exp(1.0), where the exact answer is known, and we can be sure the problems are numerical rounding issues. 
> 
> When one reads things like how SQLite (Open Source) is tested
> 
> http://sqlite.org/testing.html
> 
> or how Wolfram Research claim Mathematica (closed source) is tested
> 
> http://reference.wolfram.com/mathematica/tutorial/TestingAndVerification.html
> 
> I'm personally left with the feeling the testing in Sage leaves a lot to be desired. 
> 
> 
> Dave


---

Comment by jhpalmieri created at 2010-04-23 15:01:17

Replying to [comment:2 jhpalmieri]:
> Replying to [comment:1 drkirkby]:
> > Two questions: 
> > 
> >  * Is sage/finance/time_series.pyx failing on every platform? 
> 
> This is the only one, and I don't know why.  I could try compiling time_series.py with "-std=c99"; maybe that would help?

Actually, it didn't help.  I wonder why log is imported from math.h rather than from Python's math module.


---

Comment by jhpalmieri created at 2010-04-23 15:13:36

I accidentally added this to the description of the ticket instead of to my reply about the change to chmm:

Oh, and actually reading the docstring, there is an optional argument eps which looks something like an error bound. By default it's set to 1e-12, and it looks to me like I've added the dots in the 12th place, so now I really don't have any problem with this change.


---

Comment by drkirkby created at 2010-04-23 17:02:50

Fair enough, positive review. 

The timeout issues you got are to be expected. On my 900 MHz Blade 2000, the longest 'long' doctest took a little under 1800 s (which is the default for SAGE_LONG_TIMEOUT) and the longest normal doctest took about 450 s (which is longer SAGE_TIMOUT) Hence I would certainly have needed to increase SAGE_TIMEOUT and the long one too to be sure it would work on a more loaded system. Given that machine is quicker than t2, the fact you get timeouts does not surprise me one bit. (My experience was with 4.3.4, not the latest alpha). 

Dave


---

Comment by drkirkby created at 2010-04-23 17:02:50

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-23 17:07:31

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-24 16:32:58

By the way, several of us have come to the conclusion that the "inf" vs. "Inf" thing is actually a bug in Python.
