# Issue 571: weird simon_two_descent doctest failure

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-02 18:16:12

Assignee: was

I removed the # long after this doctest:

```
             sage: E = EllipticCurve([0, 0, 1, -23737, 960366])    
             sage: r, s, G = E.simon_two_descent(); r,s       # long
             (8, 8)
```

then ran the doctests and it fails.  This is strange because from the console it works fine.
The failure (see below) suggests too low of precision in bnfsunit/get_arch (in PARI).  Very weird. 
John Cremona is working on many improvements to this very code, so maybe it will all be fixed
by that. 


```
was`@`ubuntu:~/d/sage/sage/schemes/elliptic_curves$ sage -t ell_rational_field.py
sage -t  ell_rational_field.py                               **********************************************************************
File "ell_rational_field.py", line 905:
    sage: r, s, G = E.simon_two_descent(); r,s
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s.dev/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[19]>", line 1, in <module>
        r, s, G = E.simon_two_descent(); r,s###line 905:
    sage: r, s, G = E.simon_two_descent(); r,s
      File "/home/was/s.dev/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 913, in simon_two_descent
        maxprob=maxprob, limbigprime=limbigprime)
      File "/home/was/s.dev/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/gp_simon.py", line 93, in simon_two_descent
        raise RuntimeError, "%s\nAn error occured while running Simon's 2-descent program"%s
    RuntimeError:   *** bnfsunit: precision too low in get_arch.
    An error occured while running Simon's 2-descent program
**********************************************************************
1 items had failures:
   1 of  20 in __main__.example_22
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_ell_rational_field.py
         [51.1 s]
```



---

Comment by AlexGhitza created at 2008-01-27 04:59:38

Resolution: worksforme


---

Comment by AlexGhitza created at 2008-01-27 04:59:38

Just tried this in 2.10 on Gentoo and the problem seems to have vanished:


```
sage -t  ell_rational_field.py                              
         [40.6 s]
```



---

Comment by mabshoff created at 2008-01-27 05:09:10

I can confirm that the doctest passes with `-t -long` on OSX 10.5.

Cheers,

Michael


---

Comment by was created at 2008-01-27 12:54:07

Resolution changed from worksforme to 


---

Comment by was created at 2008-01-27 12:54:07

Changing status from closed to reopened.


---

Comment by was created at 2008-01-27 12:54:07

John and Denis Simone in fact did greatly update this code and it is now in Sage (for quote some time).  And this particularly doctest runs almost instantly now:


```
sage: E = EllipticCurve([0, 0, 1, -23737, 960366])    
sage: time r, s, G = E.simon_two_descent(); r,s
CPU times: user 0.01 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.56
```


The attached patch removes the #long.


---

Attachment


---

Comment by mabshoff created at 2008-01-27 14:40:03

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 14:40:03

Merged trac-571-simon-2-descent.patch in Sage 2.10.1.rc2


---

Comment by mabshoff created at 2008-01-27 14:40:42

Obviously: Patch is trivial and looks good to me.


---

Comment by cremona created at 2008-01-28 13:01:12

Has the pari version changed since this was reported?  That might have fixed it since there was an underlying precision bug in the pari library in sage which was fix fixed in the current version of libpari.


---

Comment by was created at 2008-01-28 13:04:46

> Has the pari version changed since this was reported?

Yes it has.  But more importantly Simone's 2-descent library was *totally* rewritten by Simone since this was reported, so that also may have resolved this issue.
