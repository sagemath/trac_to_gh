# Issue 701: port srange to Cython for speed

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-20 10:31:27

Assignee: somebody

William complained about srange being slow several times now. Let's fix it.


---

Comment by was created at 2007-09-21 00:00:58

Resolution: fixed


---

Attachment


---

Comment by jsp created at 2007-09-21 14:28:13

Resolution changed from fixed to 


---

Comment by jsp created at 2007-09-21 14:28:13

Changing status from closed to reopened.


---

Comment by jsp created at 2007-09-21 14:28:13

The srange function with include_endpoint=True
does not include the endpoint in some cases:

sage: srange(1.0, 5.0, include_endpoint=True)

[1.00000000000000, 2.00000000000000, 3.00000000000000, 4.00000000000000]


---

Attachment


---

Comment by was created at 2007-10-04 03:16:54

Resolution: fixed
