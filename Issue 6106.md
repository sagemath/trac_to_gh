# Issue 6106: [with patch, need review] Addition Indefinite Binary Quadratic Forms

Issue created by migration from Trac.

Original creator: aliashamieh

Original creation time: 2009-05-21 05:22:11

Assignee: justin

CC:  ncalexan

Keywords: binary quadratic forms

I added functions to check for the reducibility of an indefinite binary quadratic form and reduce it.


---

Attachment

added missing doctests


---

Comment by davidloeffler created at 2009-06-10 10:11:55

Am changing this from "need review" to "needs review" so it shows up in the standard queries


---

Comment by cremona created at 2009-06-11 16:58:39

Review

The patch applied fine to 4.0.1, and it provides some functions which look useful.

I think that not all new new functions have doctests.  Why are the new functions not implemented as member functions of the BinaryQF class?  That would be much better;  as it is anyone using them has to import them explicitly.  So I suggest that they are converted to be member functions (which is trivial to do).

Secondly, the use of the python math functions sqrt and floor is not a good idea, since the coefficients of the form will be Sage integers.  For example:

```
sage: from sage.quadratic_forms.binary_qf import normalized_indefinite_form
sage: f = BinaryQF([10^100,10^500,10^200])
sage: f.discriminant()>0
True
sage: normalized_indefinite_form(f)
---------------------------------------------------------------------------
OverflowError                             Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/9768/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-4.0.1/local/lib/python2.5/site-packages/sage/quadratic_forms/binary_qf.pyc in normalized_indefinite_form(f)
    486         raise ValueError, "This only works for indefinite forms"
    487     
--> 488     if sqrt(delta) <= abs(a):
    489         s=(a/abs(a))*floor(-1*b/(2*abs(a)))
    490     else:

OverflowError: math range error
```

For example, the line if sqrt(delta) <= abs(a): could be replaced by if delta <= a**2: .

The docstring for this function should also say what the definition of "normalised" is.

I also slightly amended the ticket's title to give a better description.


---

Comment by ncalexan created at 2009-07-01 17:04:48

Alia and I are going to work on this in the next few days.


---

Attachment

[with patch, needs review] Additional functions for Indefinite Binary Quadratic Forms


---

Comment by pbruin created at 2014-02-26 17:38:07

This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.


---

Comment by pbruin created at 2018-06-19 11:49:21

Replying to [comment:6 pbruin]:
> This ticket seems to implement the same functionality as (part of) #4120, which has been inactive for a very long time, like this ticket.
Now that #4120 has been merged, it would be good to check if this ticket still adds new functionality.  If not, we could also just add the examples from this ticket.


---

Comment by sbrandhorst created at 2018-07-14 17:34:28

This ticket does not add anything new.


---

Comment by sbrandhorst created at 2018-07-14 17:34:28

Changing status from needs_work to needs_review.


---

Comment by pbruin created at 2018-07-16 08:41:28

Replying to [comment:10 sbrandhorst]:
> This ticket does not add anything new. 
OK.  It might still be useful to add the doctests from this ticket; what do you think?


---

Comment by sbrandhorst created at 2018-07-16 09:00:41

If I recall correctly the reduction of an indefinite form is not unique but instead we get a cycle of forms. So we can add some doctests. But the results may be different.

Note that we messed up a little for indefinite forms of square determinant #25861.


---

Comment by pbruin created at 2018-07-16 09:49:07

Here are some doctests from the patches.  I checked that they are mathematically correct.  The docstring for `reduced_form()` did not have any examples with `transformation=True` yet; now it does.


---

Comment by sbrandhorst created at 2018-07-16 10:26:03

Changing status from needs_review to positive_review.


---

Comment by sbrandhorst created at 2018-07-16 10:26:03

doc builds.


---

Comment by pbruin created at 2018-08-22 12:29:04

Replying to [comment:14 sbrandhorst]:
> doc builds.
From your other changes, it doesn't look like you really intended to delete the branch and change the milestone to _sage-duplicate/invalid/wontfix_...


---

Comment by sbrandhorst created at 2018-08-24 11:40:47

Ooops indeed. Thank you.


---

Comment by vbraun created at 2018-08-25 11:01:36

Resolution: fixed
