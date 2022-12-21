# Issue 6005: [with patch, needs review] real and imaginary parts for quadratic number fields

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-05-07 21:22:29

Assignee: was




---

Attachment


```
sage: K.<i> = QuadraticField(-1) 
sage: i.imag()
1
```


The above is hundreds of times slower than i.real().  That needs to be fixed.

it's because of this line

```


---

Attachment


---

Comment by robertwb created at 2009-05-07 23:55:44

Now 


```
sage: K.<i> = QuadraticField(-1)
sage: timeit("i.imag()")
625 loops, best of 3: 9.73 µs per loop
```



---

Comment by mabshoff created at 2009-05-12 16:33:24

The two patches cause doctest failures in one file:

```
sage -t -long "devel/sage/sage/rings/number_field/number_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 5512:
    sage: F, F_into_L, _ = L.subfields(2)[0]; F  
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_124[42]>", line 1, in <module>
        F, F_into_L, _ = L.subfields(Integer(2))[Integer(0)]; F###line 5512:
    sage: F, F_into_L, _ = L.subfields(2)[0]; F  
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4676, in subfields
        both_maps=True, optimize=False)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4733, in _subfields_helper
        K = NumberField(f, names=name + str(i), embedding=embedding)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 423, in NumberField
        K = NumberField_quadratic(polynomial, name, check, embedding)
      File "/scratch/mabshoff/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 6852, in __init__
        self._standard_embedding = RDF(rootD) > 0
      File "parent.pyx", line 288, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4121)
      File "coerce_maps.pyx", line 81, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3064)
      File "coerce_maps.pyx", line 76, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2955)
      File "real_double.pyx", line 525, in sage.rings.real_double.RealDoubleElement.__init__ (sage/rings/real_double.c:5668)
    TypeError: float() argument must be a string or a number
**********************************************************************
<SNIP>
```


Cheers,

Michaep


---

Comment by davidloeffler created at 2009-07-21 08:17:15

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-21 08:17:15

Changing assignee from was to davidloeffler.


---

Comment by robertwb created at 2010-07-29 06:12:14

Resolution: duplicate


---

Comment by robertwb created at 2010-07-29 06:12:14

This was merged in as part of #5930. 

It was folded into one of those patches: http://hg.sagemath.org/sage-main/diff/d7533ae4895e/sage/rings/number_field/number_field_element_quadratic.pyx
