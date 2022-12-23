# Issue 5400: parser error

Issue created by migration from https://trac.sagemath.org/ticket/5400

Original creator: jason

Original creation time: 2009-02-28 16:29:19

Assignee: cwitty

CC:  mvngu

Using Sage 3.4.alpha0:


```
sage: RDF(e^(1j))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1535, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

(then a TypeError is thrown since I don't have an RDF value)

```


Now, of course, the above gives a TypeError, but there still shouldn't be the scary preparser error.



---

Comment by jason created at 2009-02-28 16:29:50

Trying this again:


```
sage: RDF(e^(1j))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1535, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1419, 0))
```



---

Comment by jason created at 2009-02-28 16:30:31

Changing assignee from cwitty to robertwb.


---

Comment by jason created at 2009-02-28 16:31:09

Robert, I "assigned" you the bug because I don't know an easy way to CC you on the bug report, since you are likely the best person to look at this currently.


---

Comment by mabshoff created at 2009-02-28 16:33:05

Replying to [comment:3 jason]:
> Robert, I "assigned" you the bug because I don't know an easy way to CC you on the bug report, since you are likely the best person to look at this currently.

I assume you know about the CC field, so what is the problem? 

Many account holders in trac are listed at http://trac.sagemath.org/sage_trac/wiki

Cheers,

Michael


---

Comment by jason created at 2009-02-28 16:52:40

The only CC option I have now with the new trac is to add myself.  It's not a text box anymore.


---

Comment by mabshoff created at 2009-02-28 16:56:23

Replying to [comment:5 jason]:
> The only CC option I have now with the new trac is to add myself.  It's not a text box anymore.

Ok, this is a permission issue with the new trac since I can CC anybody :) 

This is now #5401.

Cheers,

Michael


---

Comment by robertwb created at 2009-02-28 22:08:37

Hmm... this doesn't happen in 3.3. 

What does `sage: preparse('RDF(e^(1j))')` give you?


---

Comment by robertwb created at 2009-02-28 22:12:02

This is not a preparsing bug. 


```
sage: a = sage: a = e^1j; a
 e^(1.0*I)
sage: RDF(a)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1088, 0))
...
```



---

Comment by jason created at 2009-03-01 03:12:02

Good point with your test.  The tokenizing statement made me think it was the preparser.


---

Comment by robertwb created at 2009-05-18 21:50:44

This gives the correct error now. 


```
sage: RDF(e^(1j))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5834, in _real_double_
    return self._convert(field)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5718, in _convert
    return typ(g)
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5834, in _real_double_
    return self._convert(field)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5712, in _convert
    fops = [typ(op) for op in self._operands]
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5834, in _real_double_
    return self._convert(field)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5712, in _convert
    fops = [typ(op) for op in self._operands]
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4839, in _real_double_
    return R(self._obj)
  File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4320)
  File "coerce_maps.pyx", line 155, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4225)
  File "/usr/local/sage/local/lib/python2.5/site-packages/sage/functions/constants.py", line 973, in _real_double_
    raise TypeError
TypeError

```



---

Comment by timdumol created at 2010-01-18 01:44:29

Right now it gives?:


```
sage: RDF(e^(1j))
[...]
/home/timdumol/sage-4.3.1.alpha0/local/lib/python2.6/site-packages/sage/rings/complex_number.so in sage.rings.complex_number.ComplexNumber.__float__ (sage/rings/complex_number.c:7209)()

TypeError: can't convert complex to float; use abs(z)
```


This seems to be the right error. Should this be closed?


---

Comment by robertwb created at 2010-01-18 19:51:19

I hate the fact that 


```
sage: RR(CC(-1))
-1.00000000000000
```


but


```
sage: RDF(CDF(-1))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:5007)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)
  File "real_double.pyx", line 540, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5553)
  File "complex_double.pyx", line 808, in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6628)
TypeError: can't convert complex to float; use abs(z)
```



---

Comment by jason created at 2010-05-04 15:53:44

Replying to [comment:12 robertwb]:
> I hate the fact that 
> 
> {{{
> sage: RR(CC(-1))
> -1.00000000000000
> }}}
> 
> but
> 
> {{{
> sage: RDF(CDF(-1))
> ------------------------------------------------------------
> Traceback (most recent call last):
>   File "<ipython console>", line 1, in <module>
>   File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:5007)
>   File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)
>   File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)
>   File "real_double.pyx", line 540, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5553)
>   File "complex_double.pyx", line 808, in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6628)
> TypeError: can't convert complex to float; use abs(z)
> }}}

That problem should be a different ticket.

This ticket should be closed.


---

Comment by jason created at 2010-05-04 15:56:54

The CDF float conversion problem is now #8869


---

Comment by jason created at 2010-05-11 20:51:49

The issue for this ticket is fixed.  This ticket should be closed.


---

Comment by mvngu created at 2010-05-11 21:01:20

Close as fixed:


```
[mvngu@sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: RR(CC(-1))
-1.00000000000000
sage: RDF(CDF(-1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/real_double.so in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5541)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__float__ (sage/rings/complex_double.c:6510)()

TypeError: can't convert complex to float; use abs(z)
```



---

Comment by mvngu created at 2010-05-11 21:01:20

Resolution: fixed
