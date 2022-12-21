# Issue 4541: kschur functions don't properly convert to schur's

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2008-11-17 20:01:47

Assignee: mhansen

CC:  sage-combinat

Keywords: symmetric functions, kschur

Example:


```
sage: ks3 = kSchurFunctions(QQ,3)
sage: s = SFASchur(ks3.base_ring())
sage: s(ks3(s([1,1,1,1])))
s[1, 1, 1, 1] + t^3*s[4]
```


In general, s(ks3(foo)) returns the_right_thing + bad_stuff  where bad_stuff is a sum of Schur functions with first part larger than 3.  Possibly, this is because the ks3->s conversion doesn't understand that the kschur's do not form a basis for all symmetric functions; only for the span of schur functions with first part <= k.  I will look more at this and see if I can't put up a patch, but assistance is very welcome!


---

Comment by jbandlow created at 2008-11-19 01:25:04

Ignore my comments above.  This is maybe still a problem, but for a different reason.  The problem is that s([1,1,1,1]) doesn't live in the space spanned by the the ks3's.  So in cases like this, there are three choices for what ks3(f) should do (f symmetric, but not in the span of the ks3's):

1) Throw an error

2) Project f to the ks3's and return that answer.  This is the current behavior.

3) Do (2) but warn the user about it.

I'd vote for (1), but I'll see what sage-combinat-devel has to say first.


---

Comment by jbandlow created at 2008-11-19 01:25:35

Changing assignee from mhansen to jbandlow.


---

Attachment

Fixed.  And lots of doctests added.


---

Comment by jbandlow created at 2008-11-25 03:52:17

oh, i forgot to mention, this patch applies on top of the patch at 4540.  is that ok, mabshoff?


---

Comment by mabshoff created at 2008-11-25 03:55:17

Yes, dependencies on other patches is fine, especially if they have been already merged.

Cheers,

Michael


---

Comment by jbandlow created at 2008-11-25 03:59:50

Ok, thanks.  I'm changing the milestone since this is done.  I'll solicit reviews on sage-combinat-devel right now.


---

Comment by mhansen created at 2008-11-25 19:21:03

Hi Jason,

This looks good to me.  I'll make a new ticket for adding a method which does the projection.  This should be pretty easy as we can just add a flag to the change by triangularity method.

--Mike


---

Comment by mabshoff created at 2008-11-25 20:11:11

Resolution: fixed


---

Comment by mabshoff created at 2008-11-25 20:11:11

Merged in Sage 3.2.1.alpha1. 

Jason: This was a diff, please make sure to post hg patches, i.e. "hg export" vs. hg "diff". The code was committed in your name, so the changelog properly reflects the credit situation.

Cheers,

Michael


---

Comment by jbandlow created at 2008-11-25 20:19:22

Michael,
whoops, sorry.  Thanks for fixing.


Mike,
Sounds good.  You can assign such a ticket to me, if you'd like, so I can keep my changes to kschur.py organized (adding dual kschurs is probably next...)  Anyway, I agree that projection should be pretty easy.
