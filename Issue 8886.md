# Issue 8886: tutorial on Python object and classes

Issue created by migration from https://trac.sagemath.org/ticket/8886

Original creator: mvngu

Original creation time: 2010-05-05 11:12:50

Assignee: mvngu

CC:  leif nthiery

As the subject says. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8275334246de4531) thread for some background information. This should be coordinated with #8470.


---

Comment by hivert created at 2010-05-05 11:38:58

Changing assignee from mvngu to hivert.


---

Comment by hivert created at 2010-05-05 11:38:58

I'm preparing a patch on sage-combinat queue... I took ownership of the ticket (to have it in the my ticket report).

Florent


---

Attachment


---

Comment by mvngu created at 2010-05-05 14:07:25

The patch [trac_8886-config.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8886/trac_8886-config.patch) contains the Sphinx configuration and build files. Such files are required to get Sphinx to build documents in the category "Thematic Tutorials". When #8468 was merged, the prerequisites listed on that ticket were not merged at all. This meant that the relevant build and configuration files did not go into Sage 4.4.1. The patch [trac_8886-config.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8886/trac_8886-config.patch) is an attempt to fix this. You should apply this patch prior to adding any new documents to "Thematic Tutorials".


---

Comment by mjordan7 created at 2010-05-05 19:59:48

I have sage 4.3.5 and have been manually applying the doc patches. This one does not apply even though I have the prereqs. I have applied 8464, 8465, 8469, and 8442. Is that the wrong order?
~Mark


---

Comment by mvngu created at 2010-05-05 20:04:10

Replying to [comment:3 mjordan7]:
> I have sage 4.3.5 and have been manually applying the doc patches. This one does not apply even though I have the prereqs.

I didn't mention that you need to apply patches on top of Sage 4.4.1. The patches on this ticket and the prequisite ticket were produced on top of Sage 4.4.1. Sorry for the inconvenience.


---

Comment by jhpalmieri created at 2010-07-28 01:39:27

If #8465 is merged, then trac_8886-config.patch is no longer needed.


---

Comment by hivert created at 2011-06-28 08:29:07

Changing status from new to needs_review.


---

Attachment


---

Comment by jhpalmieri created at 2011-07-26 23:27:55

There is a mistake in thematic_tutorials/conf.py which prevents math like `\QQ` from being rendered properly.  This is fixed in #11632, so I've made that a dependency for this ticket.  (Please review it!)

I've fixed some typos and grammatical errors.  See the "delta" patch for the differences between my patch and the previous one.  I'm happy with what you've done, so if you're happy with my changes, give the ticket a positive review.


---

Attachment


---

Comment by hivert created at 2011-07-28 08:24:19

Changing status from needs_review to positive_review.


---

Attachment

Replying to [comment:9 jhpalmieri]:
> There is a mistake in thematic_tutorials/conf.py which prevents math like
> `\QQ` from being rendered properly.  This is fixed in #11632, so I've made
> that a dependency for this ticket.  (Please review it!)

I'll do it. 


> I've fixed some typos and grammatical errors.  See the "delta" patch for the
> differences between my patch and the previous one.  I'm happy with what
> you've done, so if you're happy with my changes, give the ticket a positive
> review.

Thanks for correcting my bad English. I'm mostly happy with your change. The
only remark I have is the removal of the link
`:ref:`tutorial-programming-python``. It is an up coming tutorial which is
not yet fully finished. I'm creating a new ticket (#11633) and reinstating the pointer
there.

Thanks for your careful review.

Florent


---

Comment by hivert created at 2011-08-31 09:32:16

Nicolas pointed out the following typo:

line 14: 

``functions (see the "Programming" section of the Sage tutorial) -- but now further
+knowledge``

"now" should be "no". I'm updating a corrected patch.


---

Comment by hivert created at 2011-08-31 09:32:16

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by hivert created at 2011-08-31 09:43:45

New new patch is updated it should be reviewed. The diff from the preceding patch is:


```
1.1 --- a/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 09:50:46 2011 +0200 
1.2 +++ b/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 11:37:04 2011 +0200 
1.3 @@ -890,7 +890,7 @@ 
1.4 +This tutorial is an introduction to object-oriented programming in Python and 
1.5 +Sage. It requires basic knowledge about imperative/procedural programming (the 
1.6 +most common programming style) -- that is, conditional instructions, loops, 
1.7 -+functions (see the "Programming" section of the Sage tutorial) -- but now further knowledge 
1.8 ++functions (see the "Programming" section of the Sage tutorial) -- but no further knowledge 
1.9 +about objects and classes is assumed. It is designed as an alternating 
1.10 +sequence of formal introduction and exercises. :ref:`solutions` are given at 
1.11 +the end. 
```



---

Comment by hivert created at 2011-08-31 09:43:45

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2011-08-31 11:56:05

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2011-08-31 11:56:05

Replying to [comment:14 hivert]:
> New new patch is updated it should be reviewed. The diff from the preceding patch is:
> 
> {{{
> 1.1 --- a/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 09:50:46 2011 +0200 
> 1.2 +++ b/trac_8886-objects-classes_tutorial-fh-jhp.patch Wed Aug 31 11:37:04 2011 +0200 
> 1.3 `@``@` -890,7 +890,7 `@``@` 
> 1.4 +This tutorial is an introduction to object-oriented programming in Python and 
> 1.5 +Sage. It requires basic knowledge about imperative/procedural programming (the 
> 1.6 +most common programming style) -- that is, conditional instructions, loops, 
> 1.7 -+functions (see the "Programming" section of the Sage tutorial) -- but now further knowledge 
> 1.8 ++functions (see the "Programming" section of the Sage tutorial) -- but no further knowledge 
> 1.9 +about objects and classes is assumed. It is designed as an alternating 
> 1.10 +sequence of formal introduction and exercises. :ref:`solutions` are given at 
> 1.11 +the end. 
> }}}

I suggested that tiny change, so positive review on it :-)


---

Attachment


---

Comment by jdemeyer created at 2011-10-08 18:15:05

Resolution: fixed
