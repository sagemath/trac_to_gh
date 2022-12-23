# Issue 5109: add support for Bell polynomials in Sage

Issue created by migration from https://trac.sagemath.org/ticket/5109

Original creator: mhansen

Original creation time: 2009-01-27 00:14:11

Assignee: mhansen

CC:  sage-combinat




---

Attachment


---

Comment by wdj created at 2009-01-27 12:16:33

This applies cleanly to 3.3.alpha2 and passes sage -t. The examples also agree with some examples given on http://en.wikipedia.org/wiki/Bell_polynomials, as well as this agreement: 


```
sage: stirling_number2(6,2) == bell_polynomial(6,2)(1,1,1,1,1) 
True
sage: stirling_number2(6,4) == bell_polynomial(6,4)(1,1,1) 
True
sage: stirling_number2(7,4) == bell_polynomial(7,4)(1,1,1,1) 
True
```



I ran sage -testall and got this failure:


```
sage -t  "devel/sage/sage/rings/polynomial/toy_d_basis.py"  
**********************************************************************
File "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.3.alpha2/devel/sage/sage/rings/polynomial/toy_d_basis.py", line 91:
    sage: d_basis(I)
Expected:
    [x + 170269749119, y + 2149906854, z + 735710619426, 282687803443]
Got:
    [x + 170269749119, y + 2149906854, z + 170335012540, 282687803443]
**********************************************************************
```

Though I don't know what a d_basis is, I think it is an unrelated failure
so I'm giving this a positive review.


---

Comment by wdj created at 2009-01-27 12:24:35

One more test (also positive):


```
sage: n=6
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: n = 7
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: n = 8
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: n = 20
sage: add([bell_polynomial(n,i)((1,)*(n-i+1)) for i in range(1,n+1)]) == bell_number(n) 
True
sage: bell_number(n)
51724158235372
```

Returns these pretty fast too!


---

Comment by mabshoff created at 2009-01-28 12:40:00

Note that partial credit goes to Blair - see 

http://groups.google.com/group/sage-devel/browse_thread/thread/4ae02fd827f68eed#

Cheers,

Michael


---

Comment by mhansen created at 2009-01-28 12:42:04

Yep, I did the patch in his name.


---

Comment by mhansen created at 2009-01-28 12:42:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-28 12:45:19

I got Blair's "real name" from the hg commit message, but I pinged him to see if he wants to be credited with that name or not.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-28 13:03:33

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 13:03:33

Merged in Sage 3.3.alpha3.

Cheers,

Michael
