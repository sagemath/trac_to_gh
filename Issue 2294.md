# Issue 2294: RealDoubleElement _interface_init_ is very poor

Issue created by migration from https://trac.sagemath.org/ticket/2294

Original creator: cwitty

Original creation time: 2008-02-24 19:18:35

Assignee: was

We see here that _interface_init_() on RDF loses the last few digits of its value, by truncation.


```
sage: RR(RDF(sin(1)))
0.841470984807897
sage: RR(RDF(sin(1))._interface_init_())
0.841470984808000
```


I should have a patch for this very soon.



---

Comment by cwitty created at 2008-02-24 21:09:54

Changing assignee from was to cwitty.


---

Attachment


---

Comment by was created at 2008-02-24 21:19:37

REFEREE REPORT


Wow, this is a really important patch to apply ASAP.  

There is an English typo in a parenthetical remark:


```
 	105	        computer algebra system.  (This the default function used for
```



---

Comment by mabshoff created at 2008-02-24 21:28:30

Resolution: fixed


---

Comment by mabshoff created at 2008-02-24 21:28:30

Merged in Sage 2.10.3.alpha0


---

Attachment

The patch corrects some small issue and has already been merged.
