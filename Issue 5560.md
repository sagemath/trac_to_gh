# Issue 5560: [with patch, needs review] NTL interface missing wrappers for vec_GF2 type and GF2X::MinPolySeq

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2009-03-18 16:38:46

Assignee: rhinton

CC:  malb

I want to use the `GF2X::MinPolySeq` function from my Cython application in Sage, but the function declaration and input data type, vec_GF2, are not included in the current NTL interface shim.



---

Comment by rhinton created at 2009-03-18 16:43:54

malb, is there a good way to handle the C++ overloading?  For example, in the patch I commented out one of the `put` methods (and I'm not sure if I picked the right one).


---

Comment by malb created at 2009-03-18 20:44:15

You'd have to define two functions:


```
void  (*put_G "put") (long i, GF2_c a)
void  (*put_l "put") (long i, long a)
```


and tell it that they are pointing to the same thing ('put')


---

Attachment

I split out the two cases into put_GF2 and put_long.  Anything other suggestions for positive review? :-)


---

Comment by malb created at 2009-03-25 11:29:57

Patch looks good and doesn't add any run-able code anyway.


---

Comment by mabshoff created at 2009-03-25 23:47:26

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 23:47:26

Resolution: fixed
