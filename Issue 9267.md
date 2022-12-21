# Issue 9267: Update the charge statistic on words

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2010-06-18 18:40:13

Assignee: sage-combinat

Keywords: words, charge, cocharge

The following behavior is currently in sage:

```
sage: w = Word([1,2,3,1,2])
sage: w.charge()
0
```

This is inconsistent with the definition one usually finds in the
literature, which would give the charge of this word as 2. (see
Macdonald's book, for example).

The goal of this ticket is to fix this bug, add a cocharge statistic, and extend the definition to words without partition content.


---

Comment by jbandlow created at 2010-06-28 18:24:41

Changing status from new to needs_review.


---

Comment by saliola created at 2010-06-29 19:43:55

Changing status from needs_review to needs_work.


---

Comment by saliola created at 2010-06-29 19:43:55

Tested against sage-4.4.4. Patch applies cleanly. All tests pass. The code looks good.

Just a few documentation issues:

- Add a line break here:

```
 r"""Implements Lascoux and Schutzenberger's `s_i` operator, swapping
```


- Please add a reference in the documentation to an article or book that defines charge, cocharge, Lascoux and Schutzenberger's `s_i` operators, etc.

- Since this definition of charge differs from that found in Macdonald's book, and since Sage uses many of Macdonald's conventions, I think it is a good idea to add a warning in the docstring of charge that explains that this is the common definition found in the literature and that it differs from that in Macdonald's book.


---

Comment by jbandlow created at 2010-06-30 16:12:46

Changing status from needs_work to needs_review.


---

Comment by jbandlow created at 2010-06-30 16:12:46

Wow, I can't believe I forgot to put those comments in after all the discussion.  Thanks a lot for the review, Franco.  Please look at the new version and let me know what you think.


---

Comment by saliola created at 2010-06-30 17:40:31

Jason, is the \A intentional in references [2] and [3]?

Otherwise, this gets a positive review from me, provided that the documentation builds correctly (I have not had the chance to build it yet, and won't be able to do it today).


---

Comment by saliola created at 2010-06-30 17:40:31

Changing status from needs_review to needs_info.


---

Attachment


---

Comment by jbandlow created at 2010-06-30 18:07:46

Changing status from needs_info to needs_review.


---

Comment by jbandlow created at 2010-06-30 18:07:46

Replying to [comment:4 saliola]:
> Jason, is the \A intentional in references [2] and [3]?

In a first, incorrectly sphinxed, attempt to add these references, the 'A.' was being interpreted as the start of a list, so I had to make the 'A' a literal.  But that's not happening anymore, so I've removed the backslash.

> Otherwise, this gets a positive review from me, provided that the documentation builds correctly (I have not had the chance to build it yet, and won't be able to do it today).

Great!  I think the doc builds ok, but I will wait until someone else verifies this instead of setting positive review on my own patch.

Thanks again, Franco.


---

Comment by saliola created at 2010-07-02 01:48:37

Documentation looks good.


---

Comment by saliola created at 2010-07-02 01:48:37

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 01:44:28

Resolution: fixed
