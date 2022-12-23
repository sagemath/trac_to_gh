# Issue 1294: v.n() function blows up when v is a vector

Issue created by migration from https://trac.sagemath.org/ticket/1294

Original creator: jason

Original creation time: 2007-11-27 23:13:24

Assignee: was


```
sage: v=vector(QQ,[1,2,3])
sage: v.n()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/graphs/<ipython console> in <module>()

/home/grout/sage/devel/sage-main/sage/graphs/element.pyx in sage.structure.element.Element.n()

/home/grout/sage/local/lib/python2.5/site-packages/sage/misc/functional.py in numerical_approx(x, prec, digits)
    731             return sage.rings.real_mpfr.RealField(prec)(x)
    732         except TypeError:
--> 733             return sage.rings.complex_field.ComplexField(prec)(x)
    734
    735 n = numerical_approx

/home/grout/sage/local/lib/python2.5/site-packages/sage/rings/complex_field.py in __call__(self, x, im)
    179             except AttributeError:
    180                 pass
--> 181         return complex_number.ComplexNumber(self, x, im)
    182
    183     def _coerce_impl(self, x):

/home/grout/sage/devel/sage-main/sage/graphs/complex_number.pyx in sage.rings.complex_number.ComplexNumber.__init__()

<type 'exceptions.TypeError'>: unable to coerce to a ComplexNumber
```


I'm not sure what it should do, but maybe call n() on each entry would make sense.


---

Attachment


---

Comment by mhansen created at 2007-12-22 10:45:22

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-22 10:45:22

Changing assignee from was to mhansen.


---

Comment by ncalexan created at 2008-01-20 06:46:33

Frustrating that the same snippet of code is duplicated, but this is the correct way to fix this.  Apply.


---

Comment by mabshoff created at 2008-01-21 05:39:25

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 05:39:25

Resolution: fixed
