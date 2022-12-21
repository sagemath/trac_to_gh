# Issue 3298: Cython warnings for PolyBoRi

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-05-25 13:41:31

Assignee: cwitty

CC:  robertwb burcin

Keywords: polybori, cython


```
python2.5 `which cython` --embed-positions --incref-local-binop -I/usr/local/sage-3.0/devel/sage-main -opbori.pyx
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:40:56: Function signature does not match previous declaration
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:41:59: Function signature does not match previous declaration
warning: /usr/local/sage-3.0/devel/sage-main/sage/rings/polynomial/../../libs/polybori/decl.pxi:200:10: Function signature does not match previous declaration
Finished updating Cython code (time = 2.520616 seconds)
```


I couldn't figure out what is wrong. Maybe a false positive?


---

Comment by burcin created at 2009-01-24 19:05:25

fix cython warnings for pbori.pyx


---

Comment by burcin created at 2009-01-24 19:07:29

Changing assignee from cwitty to burcin.


---

Attachment

Through a chain of typedefs the parameter expected by these functions was defined to be int, not the enum declared in the .pxi file. With the attached patch, the warnings go away. :)


---

Comment by mabshoff created at 2009-01-24 19:08:49

Looks good.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 19:13:54

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 19:13:54

Merged in Sage 3.3.alpha2
