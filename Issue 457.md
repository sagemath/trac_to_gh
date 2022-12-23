# Issue 457: gp interface: TypeError: an integer is required

Issue created by migration from https://trac.sagemath.org/ticket/457

Original creator: mhansen

Original creation time: 2007-08-19 14:23:17

Assignee: was


Hello,

there is another issue with gp:

File "gp.py", line 324:
   sage: ComplexField(10)(gp(11243.9812+15*I))
Exception raised:
   Traceback (most recent call last):
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/
doctest.py", line 1212, in __run
       compileflags, 1) in test.globs
     File "<doctest __main__.example_10[2]>", line 1, in <module>
       ComplexField(Integer(10))(gp(RealNumber('11243.9812')
+Integer(15)*I))###line 324:
   sage: ComplexField(10)(gp(11243.9812+15*I))
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/rings/complex_field.py", line 178, in __call__
       return x._complex_mpfr_field_( self )
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/interfaces/gp.py", line 333, in _complex_mpfr_field_
       return sage.rings.all.ComplexNumber( CC, real, imag )
   TypeError: an integer is required

Cheers,

Michael




---

Comment by was created at 2007-08-19 18:49:37

Resolution: fixed


---

Comment by was created at 2007-08-19 18:49:37

it's been fixed now and the fix has been pushed out.
