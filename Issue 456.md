# Issue 456: TypeError: unable to coerce to a ComplexNumber

Issue created by migration from https://trac.sagemath.org/ticket/456

Original creator: mhansen

Original creation time: 2007-08-19 14:08:02

Assignee: somebody


Hello,

I get the following doc-test failure:

File "maxima.py", line 1215:
   sage: ComplexField(10)(maxima('2342.23482943872+234*%i'))
Exception raised:
   Traceback (most recent call last):
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/
doctest.py", line 1212, in __run
       compileflags, 1) in test.globs
     File "<doctest __main__.example_23[2]>", line 1, in <module>
       ComplexField(Integer(10))(maxima('2342.23482943872+234*
%i'))###line 1215:
   sage: ComplexField(10)(maxima('2342.23482943872+234*%i'))
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/rings/complex_field.py", line 178, in __call__
       return x._complex_mpfr_field_( self )
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/interfaces/maxima.py", line 1218, in
_complex_mpfr_field_
       return sage.rings.all.ComplexNumber( CC, self.real(),
self.imag() )
     File "complex_number.pyx", line 930, in
complex_number.create_ComplexNumber
     File "complex_number.pyx", line 93, in
complex_number.ComplexNumber.__init__
   TypeError: unable to coerce to a [ComplexNumber](ComplexNumber)

Cheers,

Michael



---

Comment by mhansen created at 2007-08-19 19:05:04

Resolution: fixed
