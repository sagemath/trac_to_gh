# Issue 5597: [with patch, needs review] rename coercion action methods

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-03-24 05:09:01

Assignee: robertwb

CC:  nthiery georgsweber craigcitro


```
Currently, if A has an action on B (where B is not an A-module) one  
implements either a._l_action_ or b._r_action_. This is because  
sometimes it makes sense to put the method on the actor (e.g. Galois  
groups acting on field elements) and sometimes on the acted on (e.g.  
matrices acting on quadratic forms). However, the _x_action_ is hard  
to remember and doesn't always correspond to right/left actions. This  
may be why they're hardly used up to this point.

The proposal is to make the methods a._act_on_(b, self_on_left) and  
b._acted_upon_(a, self_on_left). In other words, a*b would try  
"a._act_on_(b, True)" and "b._acted_upon_(a, False)". 
```


See discussion at 

http://groups.google.com/group/sage-devel/browse_thread/thread/4c6ce1731ace1016


---

Attachment


---

Comment by robertwb created at 2009-03-24 05:18:45

Rename and cleanup actions. Depends on #5596.


---

Comment by GeorgSWeber created at 2009-03-24 21:00:39

Minor issue: in element.pyx, both new actions are commented with "Use this method to implement self acting on x." --- probably a copy'n'paste error for "_acted_upon_"?!

Cheers,
gsw


---

Comment by was created at 2009-04-12 05:02:12

REFEREE REPORT:

This patch contains substantial new code that has no doctests.  Please post another patch with full coverage.


---

Comment by robertwb created at 2009-09-25 08:36:48

rebased against 4.1.1


---

Attachment


---

Attachment


---

Attachment


---

Comment by nthiery created at 2009-10-12 10:51:44

Hi Robert,

Sorry for hopping so late in the discussion. I am not sure how I understand how left vs right actions are handled.

In a*b, are you always making the assumption that a is acting on b?

If I have an algebra B (whose code I don't want to touch), and implement a right B-module A,
am I supposed to implement:

   a.act_on(b)?

Or will a*b try all of:

   b.act_on(a, False)
   b.acted_upon(a, False)
   a.act_on(b, True)
   a.acted_upon(b, True)


---

Comment by robertwb created at 2009-10-13 00:29:46

Yes, it should be trying all 4 of these options.


---

Comment by nthiery created at 2009-10-14 10:35:50

Replying to [comment:7 robertwb]:
> Yes, it should be trying all 4 of these options. 

Ok. Then I would prefer:

a.act_on_left(b)
b.act_on_right(a)
a.acted_upon_right(b)
b.acted_upon_left(a)

which makes it easier to implement independently the left and right actions on a module, and possibly override just one or the other in a subclass.

That being said, we can leave things as is. Those modules for which left and right action do not coincide can later implement a.acted_upon(...) by delegating the work to
acted_upon_left and acted_upon_right.


---

Comment by robertwb created at 2009-10-15 05:44:26

But then we're back to the same problem of `s.acted_upon_right(p)` not being obvious whether s or p was the one on the right (though it's a bit better). In any case, this behavior is easy to implement in a superclass. 

So, is this a positive review (pending all doctests passing, which they did last I checked)?


---

Comment by nthiery created at 2009-10-15 12:15:33

Changing type from defect to enhancement.


---

Comment by nthiery created at 2009-10-15 12:15:33

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2009-10-15 12:15:33

Replying to [comment:9 robertwb]:
> But then we're back to the same problem of `s.acted_upon_right(p)` not being obvious whether s or p was the one on the right (though it's a bit better). 

It sounds rather clear to me.

> In any case, this behavior is easy to implement in a superclass. 

Yes.

> So, is this a positive review (pending all doctests passing, which they did last I checked)?

Yes, I just wanted to discuss the matter first. Also, part of this may become obsolete once I will have a prototype implementation of overloaded operators/functions as in MuPAD, with a declarative interface (the Sage-combinat people need them anyway for other purposes). I'll post here a link to the appropriate ticket when times come.


---

Comment by nthiery created at 2009-10-15 12:15:33

Changing keywords from "" to "actions, left actions, right actions".


---

Attachment


---

Comment by mhansen created at 2009-10-21 06:08:25

I've attached trac_5597.patch which is all the the relevant patches folded together and then rebased.

I also attached trac_5597-infinite_polynomial_ring.patch which fixes some failures since an_element was returning a "generator" and not an actual element.


---

Comment by mpatel created at 2009-10-21 06:16:59

I applied just [attachment:trac_5597-infinite_polynomial_ring.patch] to 4.2.alpha0 and doctested `sage/rings/polynomial/infinite_polynomial_ring.py`.  Positive review for this patch.


---

Comment by mhansen created at 2009-10-21 06:18:48

Resolution: fixed


---

Comment by mhansen created at 2009-10-21 06:18:48

Merged trac_5597.patch and trac_5597-infinite_polynomial_ring.patch in sage-4.2.alpha1.


---

Comment by robertwb created at 2009-10-21 06:50:46

Thanks! It's so good to finally see all these coercion and category patches go in.


---

Comment by mhansen created at 2009-10-21 06:54:15

Me too! Thanks for doing them!
