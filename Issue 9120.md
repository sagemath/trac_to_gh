# Issue 9120: plot3d transformations don't respect variable names

Issue created by migration from https://trac.sagemath.org/ticket/9120

Original creator: jason

Original creation time: 2010-06-03 02:55:23

Assignee: jason, was

CC:  olazo wcauchois

If a transformation is applied to a plotting function, it may return a function with the wrong parameter names.  This wrecks havoc since there are assumptions about the variables being passed in being the variable names of the function.  This patch corrects and tests for this.


---

Comment by jason created at 2010-06-03 03:01:23

Changing status from new to needs_review.


---

Attachment


---

Comment by wcauchois created at 2010-06-03 05:10:31

Hi Jason!

Thanks for your patch. However I'm having trouble understanding what this code does & what problem it fixes.

So basically, in the old code, if you passed in a lambda expression then the functions returned by to_cartesian() wouldn't have the correct parameter names? Can you give me some examples of when this would lead to incorrect behavior in Sage?


---

Comment by jason created at 2010-06-03 05:17:27

The current implementation _will_ lead to incorrect behavior in the fast_callable patch I'm working on...

I don't know if they lead to incorrect behavior right now.  The idea is that if you do plot(f, (x,0,1), (y,2,3), transformation=...), then the plotting code expects f to be called with f(x=.., y=...).  However, if a transformation is applied first, then x and y may not be the right keyword arguments to use for f, since the parameters could be changed in the current implementation.


---

Comment by wcauchois created at 2010-06-03 05:21:10

Hmm, I see. Its too bad the only way to make this work is to call eval() on a string. I wish there were a more... static alternative.


Have you been using plot3d transformations, in your class or otherwise?


---

Comment by wcauchois created at 2010-06-03 05:30:08

Well, this all looks good and it seems to do what you're describing.

Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake?


---

Comment by jason created at 2010-06-03 15:02:54

Replying to [comment:5 wcauchois]:

> Well, this all looks good and it seems to do what you're describing. Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake
>

Can we make that another ticket?


---

Comment by jason created at 2010-06-03 15:03:33

Replying to [comment:4 wcauchois]:


> Have you been using plot3d transformations, in your class or otherwise?

It was merged too late to use in my class this last semester, but I do plan to use it in my class next semester.


---

Comment by jason created at 2010-06-03 15:32:03

apply on top of previous patches


---

Attachment

Replying to [comment:5 wcauchois]:
> Well, this all looks good and it seems to do what you're describing.
> 
> Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake?

On second thought, that's a really good suggestion and relatively easy to do right now.  I've attached a second patch, to be applied on top of the first one.


---

Comment by wcauchois created at 2010-06-05 22:16:03

Changing status from needs_review to positive_review.


---

Comment by wcauchois created at 2010-06-05 22:16:03

REFEREE REPORT

With this refactoring, I think this patch passes review. Applies fine to Sage 4.4.2, and fixes the (rather obscure :) bug it sets out to fix. plot3d.py passes all doctests.

Positive review.


---

Attachment

incorporates all of the patches, based on sage 4.4.2


---

Comment by mhansen created at 2010-06-06 19:49:00

Resolution: fixed
