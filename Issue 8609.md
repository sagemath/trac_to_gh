# Issue 8609: Switch AmbientSpace and Scheme to Parent

Issue created by migration from https://trac.sagemath.org/ticket/8609

Original creator: novoselt

Original creation time: 2010-03-25 22:39:30

Assignee: AlexGhitza

The patch switches AmbientSpace and Scheme to inherit from Parent rather than old-style classes. I used to get random segfaults in "sage -testall" with this patch applied, but with 4.3.3 it seems to be smooth and in anyway the patch is very simple and should not introduce new bugs.

To "fix" broken doctests because of the missing list() method I have just removed them, since they were in functions not directly related to list() anyway.


---

Comment by novoselt created at 2010-03-25 22:52:48

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-04-02 15:20:24

Changing status from needs_review to needs_info.


---

Comment by cremona created at 2010-04-02 15:20:24

Patch applies fine to 4.3.5.  Testing all and will report back....

Andrey, what exactly is the motivation for this?  I see no harm in it, but you must have had a reason for making the change!


---

Comment by cremona created at 2010-04-02 15:34:59

All tests pass.  I'll give this a positive review as soon as I know the reason for it!


---

Comment by novoselt created at 2010-04-02 15:44:37

Changing status from needs_info to needs_review.


---

Comment by novoselt created at 2010-04-02 15:44:37

Replying to [comment:2 cremona]:
> Patch applies fine to 4.3.5.  Testing all and will report back....
> 
> Andrey, what exactly is the motivation for this?  I see no harm in it, but you must have had a reason for making the change!

Yeah, I should have probably explained it better. I am working on support for (Fano) toric varieties and Calabi-Yau hypersurfaces/complete intersections inside (with a hope to finish by this summer). So when I was going over schemes/general to figure out what is already there and what do I need to do to fit nicely into existing framework, I got this question:
http://groups.google.com/group/sage-devel/browse_thread/thread/ddb9f2c592082c02/4120466d01cacae0#4120466d01cacae0
and wrote the patch. It took me a while to post it due to those Segfaults that ALWAYS were appearing with the patch during non-parallel testing, although in different/unrelated places. Now I did manage to get at least one clean run and think that it should go in. After all, as I understand it, if this patch causes problems, it is because it exposes some deeper bugs in Sage and it actually can be nice if they become more visible...

I also wanted to make the following change (I don't have a ready-to-review patch for this one, but can make one quickly), but nobody got interested in discussing it and I don't think such changes should happen silently:
http://groups.google.com/group/sage-devel/browse_thread/thread/1279e373341da951/e0efa737426d5b19#e0efa737426d5b19

Thank you!


---

Comment by cremona created at 2010-04-05 15:03:10

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-04-05 15:03:10

Thanks for the explanation -- and sorry for delay, I did not get a message from trac to say that you had replied.  Anyway -- positive review.


---

Comment by jhpalmieri created at 2010-04-16 18:52:33

Merged "trac_8609_switch_ambient_space_and_scheme_to_parent.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-16 18:52:33

Resolution: fixed
