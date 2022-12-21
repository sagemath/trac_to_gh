# Issue 8362: Fix typo in documentation of Disjoint Union of Enumerated Sets

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-02-25 13:31:02

Assignee: slabbe

CC:  nborie nthiery

There is a typo in the doc of `cardinality` function.


---

Comment by nborie created at 2010-02-25 13:44:55

I put my name in Cc as I really want to follow the status of this ticket.


---

Comment by slabbe created at 2010-02-25 13:55:44

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-02-25 13:55:44

I post a patch, can somebody review it!?


---

Comment by novoselt created at 2010-02-25 22:59:39

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-26 01:51:37

The commit message is nonsensical:

```
[mq]: trac_8362_doc_fix-sl.patch
```

*Note to release manager:* When merging the patch, qrefresh and replace the above message with a sensible commit message such as:

```
#8362: Fix typo in documentation of Disjoint Union of Enumerated Sets
```



---

Attachment


---

Comment by slabbe created at 2010-02-26 15:53:19

Replying to [comment:4 mvngu]:
> The commit message is nonsensical:

I just fixed the commit message. The release manager won't need to do it.

Sébstien


---

Comment by mvngu created at 2010-03-02 22:22:29

Resolution: fixed
