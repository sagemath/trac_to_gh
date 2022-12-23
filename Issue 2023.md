# Issue 2023: dynkin diagram weights

Issue created by migration from https://trac.sagemath.org/ticket/2023

Original creator: wdj

Original creation time: 2008-02-01 04:54:06

Assignee: mhansen

CC:  sage-combinat

I may be misinterpreting something but it seems to me that
sage: dynkin_diagram(['C',4]).show()
does not display the Dynkin diagram of C_4 correctly.
There is a an online generator at http://www-math.mit.edu/~lesha/dynkin-diagrams.html
which indicates the arrow and the long root in that case.
Also, there are no examples for that function but the docstring says
"Returns a DiGraph corresponding to the Dynkin diagram..." but the Dynkin 
diagram is not a digraph, AFAIK.


---

Comment by mabshoff created at 2008-08-13 07:14:03

Mike,

this has been sitting around for a while. What is the status here?

Cheers,

Michael


---

Comment by nthiery created at 2009-04-15 16:11:45

It's indeed a bit of an abuse to have Dynkin diagram derive from Digraphs (some edges are not oriented). But they are not Graphs either (some edges are). They don't really deserve a special class graph just for themselves, do they? So, I guess we can live with this abuse.

That being said, plot should definitely be overriden to get appropriate pictures. Volunteers?

See also #5502 for ascii art drawing.


---

Comment by tscrim created at 2013-02-21 17:12:16

I've uploaded a patch that gives custom latex printing for Dynkin diagrams for crystallographic types.


---

Comment by tscrim created at 2013-02-21 17:12:16

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-03-11 15:54:23

New version which uses the global options framework for notation choices.


---

Comment by tscrim created at 2013-03-11 16:43:17

Cleaned up some docstrings.


---

Comment by nthiery created at 2013-04-15 21:42:56

Hi Travis,

I pushed a reviewer patch on the queue which makes the logic more concise as we had discussed this morning. Please check my changes and fold them. Due to some changes I undid in my patch, you probably want to have a look at the folded patch, and strip away trivial space changes that could be left due to uncomplete undoes.

I'll then have a final check on the updated patch.

Cheers,
                                     Nicolas


---

Comment by tscrim created at 2013-04-16 13:30:38

Hey Nicolas,

Thank you for the review. I had to make some minor tweaks to affine types B,C, and D. However this patch will change depending on what happens in #14248.

Thanks,

Travis


---

Comment by tscrim created at 2013-04-16 17:21:51

Updated with a better note about the conventions used in sage.


---

Comment by nthiery created at 2013-05-07 21:02:26

I have just been through the patch, and wrote a little reviewer patch which I just pushed to the Sage-Combinat queue. It sounds good to go assuming all tests pass.

Travis: if you are happy with the reviewer patch, please fold upload and set a positive review on my behalf.


---

Comment by tscrim created at 2013-05-07 21:12:30

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-08 14:00:48


```
dochtml.log:[combinat ] /mazur/release/merger/sage-5.10.beta3/devel/sage/doc/en/reference/combinat/sage/combinat/root_system/cartan_type.rst:11: WARNING: error while formatting signature for sage.combinat.root_system.cartan_type.CartanType_crystalographic.ascii_art: invalid syntax (<unknown>, line 1)
```



---

Comment by jdemeyer created at 2013-05-08 14:00:48

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2013-05-08 15:16:56

Sorry, we should have caught that. Worked around in the attached patch. See also #14553.

The updated patch was checked by Travis. I am running the tests now.


---

Comment by nthiery created at 2013-05-08 15:18:05

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2013-05-08 15:44:33

All test passed on sage.math.u-psud.fr and documentation built smoothly:

For the full logs, see:
 - http://sage.math.washington.edu/home/nthiery/2023-buildlog
 - http://sage.math.washington.edu/home/nthiery/2023-docbuildlog
 - http://sage.math.washington.edu/home/nthiery/2023-testlog


---

Comment by nthiery created at 2013-05-08 15:46:01

Changing type from defect to enhancement.


---

Comment by nthiery created at 2013-05-08 15:46:01

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2013-05-08 18:54:09

Some doctests are ignored with the new doctest framework, and the framework complains about it with long tests.

See discussion on:

https://groups.google.com/forum/?fromgroups=#!topic/sage-devel/4m1ydGdiGf8


---

Comment by nthiery created at 2013-05-08 18:54:09

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2013-05-09 01:39:28

The new patches contains two little changes we agreed with Travis / on sage-devel:

- Some trailing whitespace in new lines
- Updating the number of currently ignored tests in doctest/sources

All long test passed.

Back to positive review!


---

Comment by nthiery created at 2013-05-09 01:39:28

Changing status from needs_work to positive_review.


---

Attachment

Minor doc tweak


---

Comment by jdemeyer created at 2013-05-13 13:26:32

Resolution: fixed
