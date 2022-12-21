# Issue 2222: sage-2.10.2.alpha1 -- bessel_K is now broken -- higher precision doesn't work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-20 06:46:29

Assignee: was


```
sage -t  const.tex                                          **********************************************************************
File "const.py", line 4626:
    : bessel_K(3,2,100)
Expected:
    0.64738539094863415315923557097
Got:
    0.647385390948634
```


Note that the later 100 input is totally ignored.  I think this is due
to some use of scipy or something for some special functions by David
Joyner recently??


---

Comment by wdj created at 2008-02-20 11:23:57

Yes. The correct syntax is bessel_K(3,2,"pari",100):
sage: bessel_K(3,2,"pari",100)
0.64738539094863415315923557097
I ran "sage -t" on the file - I guess I should have run "sage -testall" also,
to find things like this.


---

Comment by mabshoff created at 2008-02-20 11:30:53

You should just make pari the default algorithm, which would fix the issue in all other files.

Cheers,

Michael


---

Comment by wdj created at 2008-02-20 19:17:47

As I see it. pari is the default:
def bessel_K(nu,z,alg="pari",prec=53):
I must be missing something obvious or else const.tex needs to change.

sage: bessel_K(3,2,"pari",100)
0.64738539094863415315923557097
sage: bessel_K(3,2,prec=100)
0.64738539094863415315923557097
sage: bessel_K(3,2,100)
0.647385390948634

I'm happy to be corrected but it seems to me that the patch is okay,
it's just that it's broken const.tex.


---

Comment by mabshoff created at 2008-02-21 17:05:56

The patch at #2246 fixes the issue -> close this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 17:05:56

Resolution: fixed
