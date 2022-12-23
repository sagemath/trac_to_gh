# Issue 8396: element_class of Subsets is broken

Issue created by migration from https://trac.sagemath.org/ticket/8396

Original creator: giraudo

Original creation time: 2010-02-28 15:13:10

Assignee: sage-combinat

CC:  nborie

element_class of Subsets is broken

```
sage: s = Subsets(Set([1]))
sage: e = s.first()
sage: isinstance(e, s.element_class)
False
```


Note: this should be caught by setting good categories

```
sage: s.category()
Category of objects
}}


---

Comment by giraudo created at 2010-02-28 15:14:05

Changing keywords from "" to "Subsets element_class".


---

Comment by giraudo created at 2010-02-28 15:43:21

Changing assignee from sage-combinat to giraudo.


---

Comment by nborie created at 2010-02-28 20:28:42

There is a little mistake I made a lot with the Trac...

Samuele, you have to export your patch and after upload them to the trac. Clic on your patch on the trac and after, read on the top the information : 
*****************************************************************
#8367: fix element_class of Subsets

diff --git a/sage/combinat/subset.py *****************************************************************

It's to short because you probably just upload the patch from .hg/patches/

use: sage -hg trac_8396_subsets_element_class_fix-sg.patch > your_favorite_directory/trac_8396_subsets_element_class_fix-sg.patch

and upload to the trac the exported patch, you will see more hg information at the top of the patch.

Once you do that, I will have a look on your fix!

Bye Samuele.


---

Comment by nborie created at 2010-02-28 20:30:14

use: sage -hg export trac_8396_subsets_element_class_fix-sg.patch > your_favorite_directory/trac_8396_subsets_element_class_fix-sg.patch 

sorry!!! I forget the export in the command. And do this command from
sage-combinat/ directory.


---

Attachment

Thanks Nicolas, it is done !


---

Comment by nborie created at 2010-02-28 21:57:31

Perfect! Now to inform any reviewer that you think your job is over on this problem, you should set your ticket as 'needs review' and thus, some people will download it and test it...

If you do so, I will review it. If you don't change the status, we will have the impression you are still working on the problem and you don't want the review now.


---

Comment by giraudo created at 2010-02-28 22:44:27

Changing status from new to needs_review.


---

Comment by nborie created at 2010-02-28 23:35:00

Changing status from needs_review to positive_review.


---

Comment by nborie created at 2010-02-28 23:35:00

The patch apply, the tests passed and the patch fix this ticket. Positive review.


---

Comment by giraudo created at 2010-03-01 17:20:11

Thanks a lot Nicolas for your revision and advices :-)


---

Comment by mvngu created at 2010-03-02 21:40:37

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 21:40:37

Samuele: Mercurial interprets your "commit message" as a comment, hence the message itself won't appear as your commit message:

```
# 8367: fix element_class of Subsets
```

Notice the white space between "#" and "8367:". Avoid putting white space between "#" and your ticket number. Your commit message should be something like this:

```
#8367: fix element_class of Subsets
```

