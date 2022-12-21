# Issue 5420: imag(complex(0,1)) gives TypeError (easy)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-02 17:38:06

Assignee: tbd


```
sage: imag(complex(0,1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/good/9936/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/functional.pyc in imag(x)
    376     Return the imaginary part of x.
    377     """
--> 378     try: return x.imag()
    379     except AttributeError: return CDF(x).imag()
    380 

TypeError: 'float' object is not callable
```


This is because complex(0,1).imag is a number, not a function, so trying to call that number gives the error.  As Robert Bradshaw said on the mailing list, Sage's imag() should really know about python complex numbers.


---

Comment by jason created at 2009-03-13 17:54:04

Changing assignee from tbd to jason.


---

Comment by jason created at 2009-03-13 17:54:04

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-06-02 07:44:06

This looks fine in sage-4.0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: imag(complex(0,1))
1.00000000000000
```



---

Comment by mvngu created at 2009-07-26 02:37:46

Resolution: fixed


---

Comment by mvngu created at 2009-07-26 02:37:46

This also looks OK with Sage 4.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: imag(complex(0,1))
1.00000000000000
```

So I'm closing this ticket as fixed.
