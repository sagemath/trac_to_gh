# Issue 6620: add a method to the Gap class to access elements of records

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2009-07-25 17:11:16

Assignee: was

CC:  nborie wdj

Accessing elements of GAP records should be easier.

```
            sage: rec = gap('rec( a := 1, b := "2" )')
            sage: gap.get_record_element(rec, 'a')
            1
            sage: gap.get_record_element(rec, 'b')
            2
```



---

Attachment


---

Comment by wdj created at 2009-07-27 15:45:03

Applies fine to 4.1.1.a0, and passes sage -testall. I also played with it a bit and could not find any bugs and the docstrings seem fine.


---

Comment by mvngu created at 2009-08-24 13:13:24

reviewer patch; fix typos in ReST format


---

Attachment

The patch `trac_6620-reviewer.patch` fixes some typos in ReST formatting introduced by `trac_6620.patch`. Such typos would result in warnings when (re)building the reference manual.


---

Comment by mvngu created at 2009-08-24 13:42:21

Resolution: fixed


---

Comment by mvngu created at 2009-08-24 13:42:21

Merged patches in this order:

 1. `trac_6620.patch`
 1. `trac_6620-reviewer.patch`
