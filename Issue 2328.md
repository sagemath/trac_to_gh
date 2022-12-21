# Issue 2328: many docstrings in combinat functions are unhelpful, outdated, or wrong

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-02-27 06:32:59

Assignee: mhansen

CC:  sage-combinat

[This link has my original complaints](http://groups.google.com/group/sage-devel/browse_thread/thread/91fb37af7f6bd0a2). On IRC, the consensus was that the uncapitalized versions of these functions should not be used, and may be deprecated in the future. The documentation for such functions should be updated to reflect this, and the documentation for other functions should be improved as well.


---

Comment by wdj created at 2008-02-27 16:40:43

The attached patch fixes a few of the docstring problems mentioned by Dan Drake. Really very minor changes. I didn't touch the functions written by Mike Hansen since I wasn't sure what plans he had for them. The issue of the lower case vs upper case functions wasn't dealt with. Perhaps the lower case functions should be removed from combinat/all.py?


---

Attachment

Replying to [comment:1 wdj]:
> Perhaps the lower case functions should be removed from combinat/all.py? 

They should first be marked deprecated, and later removed. The exact process for doing this is not yet determined; there was some discussion on sage-devel in January. Until more has been decided on that front, I think we should just say in the docstrings "this function will be deprecated in the future, and eventually removed; use Foo.whatever() instead".


---

Attachment


---

Comment by ddrake created at 2008-03-10 08:56:50

I've attached a patch which addresses most of my complaining in the email thread. :)

It's against 2.10.2 with mhansen's [2432 patch](http://sagetrac.org/sage_trac/ticket/2432) and wdj's 8710 patch applied.


---

Attachment

I've uploaded combinat-doc.2.patch which replaces the first combinat-doc.patch


---

Comment by wdj created at 2008-03-10 11:22:26

I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.


---

Comment by ddrake created at 2008-03-10 22:49:03

Replying to [comment:5 wdj]:
> I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.
My patch was against 2.10.2 + your 8710 patch + the #2432 patch...AFAIK mhansen just fiddled with a couple commented lines to get combinat-doc.2.patch.


---

Comment by mhansen created at 2008-03-11 08:21:55

I've looked over the patches and give this a positive review.

Since my patch addressing the referee's concerns for #2432 touches a lot of things, I'll build a patch with the changes in #2328 to be included with #2432.


---

Attachment

Apply only 2328.patch after #2432 is applied.


---

Comment by mabshoff created at 2008-03-14 19:56:28

Resolution: fixed


---

Comment by mabshoff created at 2008-03-14 19:56:28

Merged in Sage 2.10.4.alpha0
