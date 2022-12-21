# Issue 9323: Remove devel/sage/doc/en/faq/Makefile

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-24 03:43:49

Assignee: mvngu

Why?  'cause Mike Hansen says so.


---

Comment by mvngu created at 2010-06-24 16:20:42

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-06-24 16:20:42

It is removed in Sage 4.4.4:

```
[mvngu`@`sage faq]$ pwd
/dev/shm/mvngu/sandbox/sage-4.4.4/devel/sage-main/doc/en/faq
[mvngu`@`sage faq]$ hg st
! doc/en/faq/Makefile
```

This has not effect on building the HTML or PDF versions of the FAQ. Both of these versions build fine. The release manager can close this ticket as fixed.


---

Comment by mvngu created at 2010-06-24 16:20:49

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 03:22:25

It appears that someone has already removed the FAQ `Makefile`.


---

Comment by mpatel created at 2010-07-21 03:22:25

Resolution: fixed


---

Comment by mpatel created at 2010-07-21 03:24:59

Just to check:  Should we keep `doc/en/tutorial/Makefile`?


---

Comment by mpatel created at 2010-07-21 03:27:46

Minh, should I select a different resolution and/or milestone?


---

Comment by mvngu created at 2010-07-21 06:08:23

Replying to [comment:5 mpatel]:
> Minh, should I select a different resolution and/or milestone?

The file `doc/en/faq/Makefile` was removed from revision control in Sage 4.5.alpha1:

```sh
[mvngu`@`sage sage-main]$ hg tags | grep '4.5.alpha'
4.5.alpha4                     14585:31da167254fd
4.5.alpha3                     14573:8bb71030944a
4.5.alpha2                     14567:1be02074cf97
4.5.alpha1                     14563:c25e907dc34d
4.5.alpha0                     14531:8dec8b43ccca
[mvngu`@`sage sage-main]$ hg export 14532 | head
# HG changeset patch
# User Robert Miller <rlm`@`rlmiller.org>
# Date 1277467893 25200
# Node ID c3719ae4c319132134fc1ff501e134d9930648d8
# Parent  8dec8b43ccca5f104b1e280cb33c8f4c2c1b8f85
Added tag 4.5.alpha0 for changeset 8dec8b43ccca

diff --git a/.hgtags b/.hgtags
--- a/.hgtags
+++ b/.hgtags
[mvngu`@`sage sage-main]$ hg export 14534 | head
# HG changeset patch
# User Robert Miller <rlm`@`rlmiller.org>
# Date 1277743380 25200
# Node ID ddd5427e99b9d7ba94842c479bf3bfd5b3e08ff9
# Parent  5c14ca9acdd371af75f7e9cc8fc342c8bbd2ed05
Remove doc/en/faq/Makefile from revision control

diff --git a/doc/en/faq/Makefile b/doc/en/faq/Makefile
deleted file mode 100644
--- a/doc/en/faq/Makefile
[mvngu`@`sage sage-main]$ hg export 14564 | head
# HG changeset patch
# User Robert Miller <rlm`@`rlmiller.org>
# Date 1277828988 25200
# Node ID 995b80b5b58b0374c04d891c35159cce5c48a0a6
# Parent  c25e907dc34d83f4ed0b0edf0fdfb06cc5eba957
Added tag 4.5.alpha1 for changeset c25e907dc34d

diff --git a/.hgtags b/.hgtags
--- a/.hgtags
+++ b/.hgtags
```

The ticket then should be resolved as fixed in milestone 4.5 and merged in 4.5.alpha1.


---

Comment by mvngu created at 2010-07-21 06:12:53

Replying to [comment:4 mpatel]:
> Just to check:  Should we keep `doc/en/tutorial/Makefile`?
I think it can safely be deleted. We need to ensure that its removal has no effect on building the HTML and PDF versions of the documentation.


---

Comment by mpatel created at 2010-07-21 11:02:51

Thanks, Minh!  (Yes, I should have figured that out myself.)  Do you mind being listed as the reviewer, possibly/albeit after the fact?

I've opened #9563 for removing `doc/en/tutorial/Makefile`.
