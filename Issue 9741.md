# Issue 9741: Sorting vertices of a graph

Issue created by migration from https://trac.sagemath.org/ticket/9741

Original creator: rbeezer

Original creation time: 2010-08-13 17:17:45

Assignee: jason, ncohen, rlm

This patch adds a "key" argument to allow custom sorting of the output of the graph method vertices().  It adds to the documentation to make it clear that vertices will not always have a default sort order.

See:

http://groups.google.com/group/sage-devel/browse_thread/thread/40ac90ee3f28d723/
http://groups.google.com/group/sage-devel/browse_thread/thread/5adbb850f787373c/


---

Attachment


---

Comment by rbeezer created at 2010-08-13 17:28:16

Changing status from new to needs_review.


---

Comment by jason created at 2010-08-14 02:44:39

Great idea!  So what about those functions that call vertices(), like adjacency matrix, for example?  Will they have a default key?


---

Comment by rbeezer created at 2010-08-14 03:38:08

Replying to [comment:2 jason]:
> Great idea!  So what about those functions that call vertices(), like adjacency matrix, for example?  Will they have a default key?

The default value for key (in Python) is None.  I've specified None as the default for the key argument in this new function, so the behavior should be unchanged in other places that call vertices(), though after this patch that could be changed easily.  This patch is really just a convenience, but more about highlighting that you should think about how the sorting is going to work (or not work) if you have "exotic" objects for vertices.


---

Comment by ncohen created at 2010-09-07 15:42:08

Hello !!!

Would it be possible to make a 

"Return the list of vertices"

out of your

"Return a list of the vertices, usually as a sorted list" (Why "usually as") ?

When key=None, it is sorted using the "default" order...  And anyway your docstrings make it perfectly clear later `:-)`

Nathann


---

Attachment

Standalone patch, apply only this


---

Comment by rbeezer created at 2010-09-07 19:13:55

Replying to [comment:4 ncohen]:
> Would it be possible to make a 
> 
> "Return the list of vertices"
> 
> out of your
> 
> "Return a list of the vertices, usually as a sorted list" (Why "usually as") ?

Yes, new v2 patch has this change.  My original goal was to make the default sorting behavior more obvious, but you are right that the doctests should do the job of explaining that.

Thanks,
Rob


---

Comment by ncohen created at 2010-09-07 20:51:42

Nothing to add ! Positive review `:-)`

Nathann


---

Comment by ncohen created at 2010-09-07 20:51:42

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 22:52:38

Resolution: fixed


---

Comment by mpatel created at 2010-09-18 23:11:26

We'll need to add a patch at #4000 to update this test line:


```python
    sage: dsc = sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense.discriminant
```

I think we can use `Polynomial_rational_flint`, instead. See [comment:ticket:4000:88 comment 88].


---

Comment by ncohen created at 2010-09-18 23:18:03

Mitesh ? Did you really intend to comment this ticket ? `O_o`

Nathann


---

Comment by mpatel created at 2010-09-18 23:28:45

Yes, in case the suggested change somehow compromises the test.  Or was the `dsc = ...` line introduced elsewhere?


---

Comment by ncohen created at 2010-09-18 23:34:48

I really have no idea what this line is about... `O_o`

Nathann


---

Comment by rbeezer created at 2010-09-19 03:15:10

I made a graph with polynomials as vertices.  The discriminant is a function on polynomials that I used as the key in a sort, to demo the new sorting capability of this ticket in the doctests.

Did something change elsewhere?  This was passing tests before.

I could change this to something different.  I'm traveling with family right now, but could work on it tomorrow night.  How urgent is a fix?

Rob


---

Comment by mpatel created at 2010-09-19 05:36:16

Replying to [comment:13 rbeezer]:
> Did something change elsewhere?  This was passing tests before.

Ticket #4000 implements fast polynomial arithmetic over the rationals via FLINT1.  It removes the class `Polynomial_rational_dense` but "replaces" it with `Polynomial_rational_flint`.  

Would `dsc = lambda x: x.discriminant()` work in the sorting test?  If it does, it could shield the test against changes to a lower-level API.

> I could change this to something different.  I'm traveling with family right now, but could work on it tomorrow night.  How urgent is a fix?

It's not very urgent, though we're hoping to merge #4000 in 4.6.alpha2, which I plan to release at least a week from now (alpha1 is not yet out).  Currently, however, there's a more serious build error at #4000.


---

Comment by ncohen created at 2010-09-19 08:22:08

(oops...sorry for my interruption then `^^;` )

Nathann


---

Comment by rbeezer created at 2010-09-19 15:21:22

Replying to [comment:14 mpatel]:

Mitesh,

Thanks for the explanation and suggestion.  I'll try to get something up in the next 12-24 hours.

Rob


---

Comment by rbeezer created at 2010-09-19 15:21:22

Changing status from closed to needs_work.


---

Comment by mpatel created at 2010-09-19 21:57:01

Thanks, Rob.  This ticket is actually already in the released 4.6.alpha1, so we probably just need to change the key function in a small patch at #4000.  I apologize for not being clear about this.


---

Comment by rbeezer created at 2010-09-20 03:06:27

Mitesh,

Sorry - not thinking clearly.  I got it now.  I thought carefully about messing with the ticket status - shoulda known not to!  

I'll attach a fix to #4000 then.  Maybe later tonight.

Thanks,
Rob


---

Comment by rbeezer created at 2010-09-20 05:54:59

Mitesh,

It would appear the `dsc = lambda ...` change would certainly fix this.  But looking at the doctests, I remember now why I did what I did.  All the other tests have keys made from lambda functions.  I wanted to show how you could write out the fully-qualified name of some function (I could have imported it, as well) and use that as the `key` function.

Would it be so bad to just adjust the modules to the new names?  I could add some documentation to make it clear why this construct looks a bit odd.  But I think it would be educational for people not 100% familiar with Python having functions as first-class objects.

Rob


---

Comment by mpatel created at 2010-09-20 07:18:04

No, that's sounds good to me.  Thanks for your explanation.

Oops:  I suppose I should have written `dsc = discriminant` or `dsc = sage.misc.functional.discriminant` above.


---

Comment by rbeezer created at 2010-09-20 18:26:16

Replying to [comment:20 mpatel]:
> No, that's sounds good to me.  Thanks for your explanation.
> 
> Oops:  I suppose I should have written `dsc = discriminant` or `dsc = sage.misc.functional.discriminant` above.

Patch to fix this, with a bit more explanation, up at #4000.

Thanks, Mitesh, for guiding me through this one.  First time I've had a mid-release conflict to resolve.

Rob


---

Comment by jdemeyer created at 2017-02-10 16:07:39

Why should vertices be sorted in the first place? This is going to break badly in Python 3: #22349
