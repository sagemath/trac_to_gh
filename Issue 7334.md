# Issue 7334: Sage cannot simplify sums of logarithms

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-10-28 17:32:35

Assignee: burcin

CC:  fmaltey@nerim.fr

Keywords: logarithm

Currently there is no direct way in Sage to apply the transformation:

```
log(x) + log(y) -> log(x*y)
```


The attached patch fixes this by inserting a call to logcontract()
in the definition of simplify_radical.

Now the following works:

```
sage: f = log(sqrt(2) - 1) + log(sqrt(2) + 1)
sage: f.simplify_full()
0
```


But I'm not sure if this is the right place for this.


---

Attachment


---

Comment by whuss created at 2009-10-28 17:33:44

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-10-29 18:06:13

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-10-29 18:06:13

Hey, I love this idea!  And the code seems fine on the face of it.  

But probably it makes the most sense to make it separately available as a simplification, i.e. make a new method .simplify_log() or something.  Exposing as many of these as possible is good for the (many) users who keep one wanting some, but not all simplifications, which I think is something people really like about Maxima (from reading their lists).  

Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  And one would want a (perhaps slightly complicated) example added to simplify_full() which shows that it's used correctly there as well.


---

Comment by robert.marik created at 2009-11-07 21:14:57

I also think that it is better to keep the function logcontract separately from simplify_full() since sometimes the contraction of logarithms is not what user wants. Consider please also option which allows to set logconfcoef as described in [Maxima](http://maxima.sourceforge.net/docs/manual/en/maxima_14.html#Item_003a-logconcoeffp). This allows to contract expressions like log(x)+1/2*log(8) into log(x*sqrt(8)).


---

Comment by robert.marik created at 2009-11-07 21:23:38

Replying to [comment:2 kcrisman]:
> Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  

Do not do it please. The user knows if he/she wants to contract logarithms or not and then he/she can run the coresponding method. If you include this as an automatical simplification in simplify_full, consider the following

* domain of log(1-x)+log(1+x) is different from domain of log(1-x^2)

* you should add a function which expands logarithms

Thanks 
Robert


---

Comment by robert.marik created at 2009-11-07 23:19:21

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2009-11-07 23:19:21

Attached new patch, apply only this patch.

Options which controls if simplify expressions like 1/2*log(x) or not has been introduced.

simplify_log now does not use radcan, it calls only logcontract in Maxima session. However, there are many aliases for radcan:
radical_simplify, simplify_radical, exp_simplify, simplify_exp


---

Attachment

Replying to [comment:4 robert.marik]:
> Replying to [comment:2 kcrisman]:
> > Anyway, then you could just call this wherever you think is best in the definition of .simplify_full(), which certainly should have this included.  
> 
> Do not do it please. The user knows if he/she wants to contract logarithms or not and then he/she can run the coresponding method. If you include this as an automatical simplification in simplify_full, consider the following
> 

I disagree.  simplify_full is the sort of thing used by people who do NOT know if they want to contract - they want the simplest-looking form possible.  In fact, these people usually use just simplify() first and then email sage-support complaining it doesn't do things like this :)  

Anyone who is looking for something specific can use the specific wrappers for the Maxima simplifiers; the general user who is not actually interested in symbolics or niceties like domains (which presumably the other simplifiers also disrespect, e.g. x**2/x is not x but presumably one of them does this and is part of simplify_full) needs a function which applies as much machinery as possible, and simplify_full is it.

That said, wrapping more of the expanding functions is a very good idea!  One could even have an "expand_full" function to complement the "simplify_full".  

(Unfortunately, many users (including me) get tripped on on simplify versus expand linguistically, because in colloquial high school English they are often used interchangeably... sigh, but I'm just as guilty as anyone.)


---

Comment by robert.marik created at 2009-11-08 14:13:33

apply only this patch


---

Attachment

Added contraction of logarithms to simplify_full() and some more options.


---

Comment by robert.marik created at 2009-11-08 14:29:56

note that something does not work as expected due to recently fixed Maxima [bug](http://sourceforge.net/tracker/index.php?func=detail&aid=2835634&group_id=4933&atid=104933).

As a particular example (log(5)-log(2)).logcontract() does not work now, (log(x)-log(y)).logcontract() works as expected.


---

Comment by kcrisman created at 2009-11-10 14:13:12

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-11-10 14:13:12

Here are a few comments, which you can incorporate if you agree with them.  Overall, though, a VERY well documented patch, which tells the user exactly what they can and cannot do with it, options, etc.  Good work!

1. typo of "gowerns" instead of "governs" in line 5268

2. Maybe the if coeff is not None:  should be set off in a block? For better readability and logical flow.

3. Perhaps 

```
sage: (log(5)-log(2)).simplify_log()
-log(2) + log(5)
```

should be included as a doctest, with a comment that this is not simplified (though it's not mathematically wrong, so I am okay with this being as is).  This will also encourage us to upgrade Maxima :)

4. There are some duplicated doctests.  Is this intentional (i.e., to show it won't simplify any more)?  Since 

```
sage: x,y,t=var('x y t') 
sage: f = log(x)+2*log(y)+1/2*log(t) 
sage: f.simplify_log()
log(x*y^2) + 1/2*log(t)
sage: f
1/2*log(t) + log(x) + 2*log(y)
```

it must have some other rationale.  Anyway, that should be clarified, or the duplicates should be removed, as this is confusing.


---

Attachment

Apply only this patch.


---

Comment by robert.marik created at 2009-11-12 10:52:34

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2009-11-12 10:52:34

Many thanks for reviewing and comments. New patch is there. It accepts your suggestions and adds more:

If we contract logarithms, we have to build the way back - I added expansion of logarithms.

I also updated simplification of rational functions and added one option to simplify_trig.


---

Comment by robert.marik created at 2009-11-12 10:55:52

And there was also no way to go back after expanding trigonometric function. I added interface to Maxima's trigreduce to this patch.


---

Comment by burcin created at 2009-11-12 11:08:37

I really dislike the idea of adding a new function for each functionality of this kind. This makes it very hard for users to figure out the function name they need for a specific task.

We should be able to provide an interface to all these "rewriting" tasks through a few conceptually defined methods like rewrite(), expand() and combine()( or contract()?).

Francois Maltey had a proposal for a possible interface to all this. Maybe he can comment here, or we can discuss his proposal on sage-devel.


---

Comment by robert.marik created at 2009-11-12 13:06:30

started discussion [on sage-devel](http://groups.google.cz/group/sage-devel/browse_thread/thread/3899a578da747009)


---

Comment by robert.marik created at 2009-11-13 14:12:56

According to the discussion on sage-devel, let's wait (perhaps short time) and look for some cleaner solution.


---

Comment by robert.marik created at 2009-11-13 14:12:56

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-02-03 15:09:27

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-02-03 15:09:27

3 months is more than enough time to wait. The patch looks good to me (apart from minor formatting problems like long lines). I want to give a positive review, but it seems I can't switch from needs_work to positive_review directly. I'll run doctests first, then come back here.


---

Comment by burcin created at 2010-02-03 15:24:00

On Sage-4.3.2.alpha1, I get these doctest failures:


```
sage -t  devel/sage-s/sage/symbolic/expression.pyx
**********************************************************************
File "/scratch/berocal/sage/i686/sage-4.3.rc0/devel/sage-s/sage/symbolic/expression.pyx", line 5837:
    sage: (x*log(9)).simplify_log('all')
Expected:
    log(9^x)
Got:
    x*log(9)
**********************************************************************
File "/scratch/berocal/sage/i686/sage-4.3.rc0/devel/sage-s/sage/symbolic/expression.pyx", line 5849:
    sage: (log(5)-log(2)).simplify_log()
Expected:
    -log(2) + log(5)
Got:
    log(5/2)
**********************************************************************
```


I don't know about the first one, but the second one seems to be confirming a bug fix in Maxima. :)


---

Comment by burcin created at 2010-02-03 15:24:00

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2010-02-03 15:32:18

The first problem is outside  maxima, since I have

```
sage: maxima("logconcoeffp:'logconfun")
logconfun
sage: maxima("logconfun(m):= true")
logconfun(m):=true
sage: maxima("logcontract(x*log(9))")
log(9^x)
```

I have to investigate the problem in details (perhaps tomorrow).

Yes, the second "problem" is a fixed bug from Maxima :)


---

Attachment

New patch (switch temporary logexpand to false when doing logcontract) is attched. Apply only this patch.


```
./sage -t devel/sage/sage/symbolic
```

passed. Running all tests now. If they pass, I'll mark it as 'needs review' (tomorrow morning).


---

Attachment

apply after trac-7334-logcontract-5.patch


---

Comment by robert.marik created at 2010-02-04 11:45:52

tests passed. apply patches trac-7334-logcontract-5.patch  and trac-7334-logcontract-5-bugfix.patch


---

Comment by robert.marik created at 2010-02-04 12:15:23

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-02-04 16:05:47

Apply after others


---

Attachment

Reviewer patch adds some additional doctests, fixes typos, clarifies a few other things.  It also fixes a bug which may not have appeared on the author's platform, essentially the same one as in the 5-bugfix patch but for the log_expand function.  

I don't really understand why the original code didn't work, because it should!  But for some reason the logexpand variable was sticking around, also messing up other doctests in expression.pyx, for me, so I made this change.  Only this change needs review now; all else is enthusiastic positive review!


---

Comment by kcrisman created at 2010-02-04 16:10:41

An additional thought on this:

And to be honest, we should reset logexpand anyway, because after using log_expand one might want to do something else with Maxima where one might want the default logexpand setting, and be surprised that logexpand had been changed by log_expand.


---

Comment by robert.marik created at 2010-02-04 19:01:49

The reviwer patch seems to be O.K. for me. Thanks for fixing typos and adding docs. Running tests now.

restoring default value of logexpand was not necessary, since 'ev' environment has been used in my original patch and this has no influence to the value of logexpand

```
sage: maxima('logexpand')
true
sage: maxima('ev(log(x*y),logexpand:false)')
log(x*y)
sage: maxima('logexpand')
true
sage: maxima('ev(log(x*y),logexpand:super)')
log(y)+log(x)
sage: maxima('logexpand')
true
```


but the current method without 'ev' enviroment is also O.K. and perhaps better, since ev may lead sometimes to some other problems and should be avoided if possible (as I understand discussions related (for example)to substitution from maxima group).


---

Comment by kcrisman created at 2010-02-04 20:59:15

> restoring default value of logexpand was not necessary, since 'ev' environment has been used in my original patch and this has no influence to the value of logexpand

It shouldn't have, but for some reason it did in my installation - specifically in some tests in solve and friends which had logs in their answers that mysteriously began simplifying!  Anyway, glad you think this solution is okay.


---

Comment by robert.marik created at 2010-02-04 21:20:52

all tests passed for me after  trac-7334-logcontract-5.patch , trac-7334-logcontract-5-bugfix.patch, trac_7334-logcontract-5-reviewer.patch


---

Comment by kcrisman created at 2010-02-05 20:02:50

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-02-05 20:02:50

Replying to [comment:25 robert.marik]:
> all tests passed for me after  trac-7334-logcontract-5.patch , trac-7334-logcontract-5-bugfix.patch, trac_7334-logcontract-5-reviewer.patch 

It sounds like this means positive review for the last reviewer change.  Great!


---

Comment by mpatel created at 2010-02-11 15:02:55

Resolution: fixed
