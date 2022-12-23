# Issue 8789: Improve doctest coverage of modules/free_module_element.pyx

Issue created by migration from https://trac.sagemath.org/ticket/8789

Original creator: was

Original creation time: 2010-04-28 04:16:47

Assignee: tbd

Starting score in sage-4.4:

```
free_module_element.pyx: 47% (50 of 105)
```




---

Attachment


---

Comment by was created at 2010-04-29 05:17:43

Changing status from new to needs_review.


---

Attachment

Looks good to me.


---

Comment by mhansen created at 2010-05-01 17:41:20

Changing status from needs_review to positive_review.


---

Attachment

The second patch doesn't apply when applied on top of the first one:


```sh
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8789/trac_8789.patch && hg qpush 
adding trac_8789.patch to series file
applying trac_8789.patch
now at: trac_8789.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8789/trac_8789_part2.patch && hg qpush 
adding trac_8789_part2.patch to series file
applying trac_8789_part2.patch
patching file sage/modules/free_module_element.pyx
Hunk #1 FAILED at 439
Hunk #2 FAILED at 576
Hunk #3 FAILED at 2137
3 out of 3 hunks FAILED -- saving rejects to file sage/modules/free_module_element.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8789_part2.patch
```


I have attached a rebase of the second patch.


---

Comment by mvngu created at 2010-05-08 21:47:57

Merged in this order:

 1. [trac_8789.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8789/trac_8789.patch)
 1. [trac_8789_part2-rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8789/trac_8789_part2-rebased.patch)


---

Comment by mvngu created at 2010-05-08 21:47:57

Resolution: fixed
