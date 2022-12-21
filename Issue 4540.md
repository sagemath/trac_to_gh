# Issue 4540: Symmetrica segfault converting Schur functions to k-Schurs

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2008-11-17 19:01:51

Assignee: mhansen

CC:  sage-combinat

Keywords: kschur, symmetrica, segfault

Example:


```
sage: ks3 = kSchurFunctions(QQ,3,1)  # k-Schur functions without a 't' variable
sage: s = SFASchur(base_ring())
sage: ks3(s([3]))

Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
function: mult(1) 
python: mult(1): Unknown error 3052408646
```


I don't know if the definition of ks3 above was ever intended to be supported.  I just tried it because I wanted k-Schur functions without a 't' and it seemed the natural thing to do.  Conversions the other way (i.e., s(ks3([3])) ) do seem to work.  And, whether it's intended to be supported or not, segfaults are bad.


---

Attachment


---

Comment by mabshoff created at 2008-11-21 09:33:02

Segfaults are bad, so make this a blocker.

Mike: Can you have a look?

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 09:33:02

Changing priority from major to blocker.


---

Comment by mhansen created at 2008-11-21 14:54:59

Good work Jason!


---

Comment by mhansen created at 2008-11-21 14:54:59

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-21 23:06:46

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-21 23:06:46

Resolution: fixed
