# Issue 9704: refactor "trace" -- make trace command call trace method on input if available

Issue created by migration from https://trac.sagemath.org/ticket/9704

Original creator: was

Original creation time: 2010-08-07 17:31:41

Assignee: jason

This is confusing.  Refactor to fix it:


```
sage: det(matrix(2,[1,2,3,4]))
-2
sage: trace(matrix(2,[1,2,3,4]))
Traceback (most recent call last)
...
AttributeError: 'sage.matrix.matrix_integer_dense.Matrix_integer_dense' object has no attribute 'lstrip'
```



---

Attachment


---

Comment by was created at 2010-08-07 17:43:46

Changing status from new to needs_review.


---

Comment by jason created at 2010-08-07 17:54:30

-1 on this idea.  This means that "trace" means *completely* different things depending on the input.  Instead, we ought to decide what "trace" means and make two functions.  I think trace(x) should be x.trace (and give a mathematical meaning), and the current trace should be code_trace or trace_execution or something like that.


---

Comment by mhansen created at 2010-08-07 18:45:19

I would just say leave it like it is except to add a deprecation warning to use "trace_execution" in the string case.  That way we get something that is backward compatible.


---

Comment by was created at 2010-08-07 19:10:08

* jason -- trace already means two different things, at least.   I'm not adding a new meaning. 

* regarding adding a deprecation warning, I think that is reasonable, but that should not go in this ticket.  If you want to do that, make it another ticket and do it.


---

Comment by jason created at 2010-08-07 19:19:22

Replying to [comment:4 was]:
> * jason -- trace already means two different things, at least.   I'm not adding a new meaning. 

When I read the code, trace() has one purpose, not two.  Your patch will mean that the trace function has two completely different purposes, depending on the input.  That is what I'm -1 on.

If we change the trace() function so that it instead computes the trace of an object (i.e., x.trace()), then I agree that for a short amount of time, a deprecation warning should be added and trace() will have to serve two purposes.


> 
> * regarding adding a deprecation warning, I think that is reasonable, but that should not go in this ticket.  If you want to do that, make it another ticket and do it. 

I'm -1 on a ticket (this one) which makes the Sage trace() function have two purposes (unless it's a temporary thing that is deprecated, of course).


---

Comment by cremona created at 2010-08-11 15:48:49

Sage already has _lots_ of functions f() which do very different things depending on the type of the arguments.

How about making the trace(x) function do what others do, which is to try returning x.trace() and if that fails do what the code_trace function does?


---

Comment by jason created at 2010-08-12 03:00:50

Replying to [comment:6 cremona]:
> Sage already has _lots_ of functions f() which do very different things depending on the type of the arguments.
> 
> How about making the trace(x) function do what others do, which is to try returning x.trace() and if that fails do what the code_trace function does?

Is there any other examples in Sage where a function does:

  * mathematically meaningful stuff (which may differ, depending on the mathematical object), and returns a mathematical answer
  * and also does something which is entirely non-mathematical, on a completely different level (a programming nuts-and-bolts debugging level, rather than a math level)?

The big conceptual difference between those two purposes is why I think having two functions, say `trace()` (which calls `x.trace()`) and `trace_execution()` (which does what trace does right now) is a much better design than lumping things into one function.


---

Comment by was created at 2010-08-12 11:17:52

Look Jason, this "trace" having two meanings is *already* in Sage.  Whether or not that changes is orthogonal to this ticket.   You could post a patch *after* this ticket gets in later if you're really worried.

English has words with different meanings.  Sorry. It's just the way the language works.


---

Comment by jason created at 2010-08-12 11:54:40

Replying to [comment:8 was]:
> Look Jason, this "trace" having two meanings is *already* in Sage.  

No, it doesn't at the top level, and not in the same function.

> Whether or not that changes is orthogonal to this ticket.   You could post a patch *after* this ticket gets in later if you're really worried.
> 

I'm posting one right now.


> English has words with different meanings.  Sorry. It's just the way the language works. 

Sure, but that doesn't excuse a bad design.


---

Comment by jason created at 2010-08-12 12:00:41

My patch may cause some doctest somewhere to fail because of deprecation warnings.  I've tested the misc/*.py and matrix/*.py* files (and only got errors that should be from other patches on my stack).


---

Comment by jason created at 2010-08-12 12:26:56

apply instead of previous patch


---

Attachment

I incline to Jason's argument. I propose 'trace_through' as a more palpable name than Jason's 'trace_execution'.


---

Comment by rlm created at 2010-11-11 13:55:01

LGTM.


---

Comment by rlm created at 2010-11-11 13:55:01

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-15 15:30:03

Sorry, but the discussion at sage-devel yielded very few people in favour of this patch, so I'm not planning to merge it.


---

Comment by jason created at 2010-11-15 16:03:59

Thanks for asking on sage-devel.  I'm still in favor of it, since (as a linear algebra person and a math teacher) I'd rather have trace have mathematical meaning instead of programming meaning, and it is a natural complement to having a top-level det function.  My vote wasn't counted on sage-devel yet, so add another +1.


---

Comment by vbraun created at 2012-06-30 18:34:45

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2012-06-30 18:39:43

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2012-06-30 18:39:43

Since there seems to have been a vote that this patch should not be merged, I think we should close it as *wontfix*.


---

Comment by jason created at 2012-06-30 18:42:40

I think we should have another vote.  I was the major -1 vote, and I fixed the issues I had with it in my updated patch.

I'll post to sage-devel one more time.  It's been a long time since this issue was raised.


---

Comment by jason created at 2012-06-30 18:42:40

Changing status from positive_review to needs_info.


---

Comment by jason created at 2012-06-30 18:53:05

I've posted to sage-devel again: https://groups.google.com/group/sage-devel/browse_thread/thread/61ca252973c4930f


---

Comment by git created at 2016-04-27 05:46:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by klee created at 2016-04-27 05:52:49

As not everyone is happy with refactoring `trace()` for dual purposes, we may add `tr()` for mathematical trace instead of `trace()`. Actually I guess that it is more frequent and convenient to think of `tr(m)` than `trace(m)` for a non-programmer mathematician. Also it nicely balances with `det(m)`


---

Comment by klee created at 2016-04-27 05:53:53

Changing status from needs_info to needs_review.


---

Comment by klee created at 2016-11-06 18:35:02

Changing status from needs_review to needs_work.


---

Comment by git created at 2016-11-06 18:36:12

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by klee created at 2016-11-06 18:38:43

Changing status from needs_work to needs_review.


---

Comment by git created at 2017-08-04 07:34:14

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by klee created at 2017-08-04 07:46:37

Previously I somehow ended up kidnapping this ticket, and uploaded a patch not for the original purpose of the ticket. I felt guilty, so now I recover the ticket for the original purpose. 

The newly pushed branch only contains the code by Jason with slight changes. The code by Jason implements the idea discussed in https://groups.google.com/group/sage-devel/browse_thread/thread/61ca252973c4930f


---

Comment by chapoton created at 2018-03-11 17:11:54

does not apply


---

Comment by chapoton created at 2018-03-11 17:11:54

Changing status from needs_review to needs_work.


---

Comment by git created at 2018-03-12 00:38:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by klee created at 2018-03-13 00:14:31

Changing status from needs_work to needs_review.


---

Comment by klee created at 2019-05-07 05:44:10

It seems that there is no enough consensus in changing the meaning of `trace` command, which is now commonly used to trace code execution in Sage.

At least I myself prefer to use the methods `m.det()` and `m.trace()` than the functions `det(m)` or `trace(m)`. So I would rather remove the function `det` instead of introducing new `trace` function.

Hence I close this ticket as "won't fix".
