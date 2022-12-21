# Issue 6422: [with patch, needs review] make sage.symbolic.expression.Expression.__init__ usable

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-06-26 14:13:50

From sage-support:


```
On Fri, 26 Jun 2009 06:14:13 -0700 (PDT)
Nicolas <nicolas.fressengeas`@`gmail.com> wrote:

> 
> I think there is definitely a bug in the __init__ method of the
> Expression class.
> Probably it has not been tracked down because this method is quasi
> never used in the new version of symbolics. However, it raises
> problems when one wants to derive a suclass from Expression.
> 
> The bug is described in details here for the 4.0.1 version. It is
> still present in the 4.0.2 :
> 
> http://groups.google.com/group/sage-support/browse_thread/thread/d50dc3bc2bdbeab0/34798c0585fc034f?lnk=gst&q=nicolas#34798c0585fc034f
> 
> Burcin provided a simple solution that works wonderfully, in the same
> thread.
> 
> Should we issue a ticket for this to be included in the future
> versions ?
```


The patch mentioned above is attached.


---

Comment by was created at 2009-06-26 15:13:20

Upon applying this to sage-4.1.alpha1 I get failures:

```
sage -t  devel/sage/sage/symbolic/expression.pyx
/scratch/wstein/build/sage-4.1.alpha1/local/lib/python/site-packages/sage/misc/misc.py:1900: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument
  warn(message, DeprecationWarning, stacklevel=3)
**********************************************************************
File "/scratch/wstein/build/sage-4.1.alpha1/devel/sage-main/sage/symbolic/expression.pyx", line 219:
    sage: sage.symbolic.expression.Expression(SR)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[2]>", line 1, in <module>
        sage.symbolic.expression.Expression(SR)###line 219:
    sage: sage.symbolic.expression.Expression(SR)
      File "expression.pyx", line 224, in sage.symbolic.expression.Expression.__init__ (sage/symbolic/expression.cpp:2761)
        cdef Expression exp = self.coerce_in(x)
      File "expression.pyx", line 1495, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:9537)
        return self._parent._coerce_(z)
    AttributeError: 'NoneType' object has no attribute '_coerce_'
**********************************************************************
File "/scratch/wstein/build/sage-4.1.alpha1/devel/sage-main/sage/symbolic/expression.pyx", line 221:
    sage: sage.symbolic.expression.Expression(SR, 5)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        sage.symbolic.expression.Expression(SR, Integer(5))###line 221:
    sage: sage.symbolic.expression.Expression(SR, 5)
      File "expression.pyx", line 224, in sage.symbolic.expression.Expression.__init__ (sage/symbolic/expression.cpp:2761)
        cdef Expression exp = self.coerce_in(x)
      File "expression.pyx", line 1495, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:9537)
        return self._parent._coerce_(z)
    AttributeError: 'NoneType' object has no attribute '_coerce_'
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_4
```



---

Comment by burcin created at 2009-06-27 15:22:12

second try at fixing Expression.__init__


---

Attachment

I attached a new patch which sets `self._parent` first, fixing the doctest problems above. I also added a new test for the problem reported by Nicolas in his initial message.


---

Comment by burcin created at 2009-06-27 15:24:53

Set assignee to burcin.


---

Comment by burcin created at 2009-06-27 15:24:53

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-07-17 09:34:10

Changing keywords from "" to "expression init".


---

Comment by AlexGhitza created at 2009-07-17 10:37:12

Looks good.


---

Comment by mvngu created at 2009-07-18 16:05:07

Resolution: fixed
