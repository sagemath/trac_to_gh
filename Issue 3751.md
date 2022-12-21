# Issue 3751: Type of output returned by QuadraticField(-1).class_number()

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-07-31 20:37:09

Assignee: was

The output of the class_number() method for QuadraticFields is a Python integer. Would it be possible to change this so that it returned a Sage integer?


```
sage: K=QuadraticField(-1,'a')
sage: K.class_number()
1
sage: type(K.class_number())
<type 'int'>
```



---

Attachment

The patch fixes this.  Based on 3.0.6, and all tests in sage/rings/number_fields pass.


---

Attachment

I added some tests, but this looks good.

Apply only 3751-ncalexan-class-number.patch.


---

Comment by mabshoff created at 2008-08-11 00:15:54

Resolution: fixed


---

Comment by mabshoff created at 2008-08-11 00:15:54

Merged 3751-ncalexan-class-number.patch in Sage 3.1.alpha1
