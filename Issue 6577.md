# Issue 6577: Reference manual build errors in 4.1.1.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/6577

Original creator: davidloeffler

Original creation time: 2009-07-21 09:56:01

Assignee: tba

This is in 4.1.1.alpha0: 

```
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.get:8: (WARNING/2) Inline literal start-string without end-string.                                              
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.ramified_at:11: (WARNING/2) Inline literal start-string without end-string.                                     
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/databases/jones.py:docstring of sage.databases.jones.JonesDatabase.unramified_outside:13: (WARNING/2) Inline literal start-string without end-string.                              
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:3: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.                                                                                 
WARNING: /home/david/sage-4.1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py:docstring of sage.schemes.elliptic_curves.ell_rational_field.ModularParameterization:4: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
}}}        


---

Attachment


---

Comment by davidloeffler created at 2009-07-21 11:22:06

Changing priority from major to blocker.


---

Comment by davidloeffler created at 2009-07-21 11:22:06

Changing keywords from "" to "reference manual".


---

Comment by mvngu created at 2009-07-21 14:18:28

Begone are the warnings :-)


---

Comment by mvngu created at 2009-07-23 01:58:29

Resolution: fixed
