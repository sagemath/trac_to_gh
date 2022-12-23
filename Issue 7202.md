# Issue 7202: On OS X ppc, to_poly_solve evidently doesn't exist / work, which breaks some symbolic doctests

Issue created by migration from https://trac.sagemath.org/ticket/7202

Original creator: was

Original creation time: 2009-10-13 16:59:57

Assignee: burcin

CC:  kcrisman


```
sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
**********************************************************************
File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/devel/sage/sage/rings/number_field/number_field_element.pyx", lin
e 1421:
    sage: SR(a)
Exception raised:    Traceback (most recent call last):
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/bin/ncadoctest.py", line 1231, in run_one_test        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[20]>", line 1, in <module>        SR(a)###line 1421:
    sage: SR(a)
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4174)
      File "coerce_maps.pyx", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.
c:4067)  
      File "number_field_element.pyx", line 1464, in sage.rings.number_field.number_field_element.NumberFieldElement._sym
bolic_ (sage/rings/number_field/number_field_element.cpp:11758)
      File "expression.pyx", line 5608, in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:22471)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/lib/python/site-packages/sage/calculus/calculus.py", 
line 1810, in symbolic_expression_from_maxima_element
        return symbolic_expression_from_maxima_string(x.name(), maxima=maxima)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/lib/python/site-packages/sage/calculus/calculus.py", 
line 1693, in symbolic_expression_from_maxima_string
        raise TypeError, "unable to make sense of Maxima expression '%s' in Sage"%s
    TypeError: unable to make sense of Maxima expression 'to_poly_solve(x*(x^4-1)+1=0,x)' in Sage
**********************************************************************
1 items had failures:
   1 of  23 in __main__.example_40
***Test Failed*** 1 failures.


and


sage -t  "devel/sage/sage/symbolic/expression.pyx"
**********************************************************************
File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/devel/sage/sage/symbolic/expression.pyx", line 5564:
    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_140[5]>", line 1, in <module>
        solve(Q*sqrt(Q**Integer(2) + Integer(2)) - Integer(1),Q)###line 5564:
    sage: solve(Q*sqrt(Q^2 + 2) - 1,Q)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/lib/python/site-packages/sage/symbolic/relation.py", line 491, in solve
        return f.solve(*args,**kwds)
      File "expression.pyx", line 5608, in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:22471)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/lib/python/site-packages/sage/calculus/calculus.py", line 1810, in symbolic_expression_from_maxima_element
        return symbolic_expression_from_maxima_string(x.name(), maxima=maxima)
      File "/home/wstein/screen/varro/build/sage-4.1.2.rc1.p1/local/lib/python/site-packages/sage/calculus/calculus.py", line 1693, in symbolic_expression_from_maxima_string
        raise TypeError, "unable to make sense of Maxima expression '%s' in Sage"%s
    TypeError: unable to make sense of Maxima expression 'to_poly_solve(Q*sqrt(Q^2+2)-1=0,Q)' in Sage
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_140
```



---

Comment by kcrisman created at 2009-10-28 14:17:47

Can you test this again on 4.2?  Reasons follow.

This works fine on my OSX 10.4 G4 PPC with 4.1.2.rc2 with #6642 also loaded.  Namely:

```
sage: var('Q')Q
sage: solve(Q*sqrt(Q^2+2)-1,Q)[Q == 1/sqrt(Q^2 + 2)]
sage: solve(Q*sqrt(Q^2+2)-1,Q,to_poly_solve=True)
[Q == -1/sqrt(-sqrt(2) + 1), Q == 1/sqrt(-sqrt(2) + 1), Q == -1/sqrt(sqrt(2) + 1), Q == 1/sqrt(sqrt(2) + 1)]
sage:  K.<a> = NumberField(x^5-x+1, embedding=-1)
sage: SR(a)
-1.1673040153
```

Note that the behavior has changed since #6642, because using to_poly_solve as a default meant that we didn't always get multiplicities, so now it is an option.   Also note that in the ONE case above, out of many many new correct solutions, we get two spurious ones - this is fixed in Maxima CVS, though, so when the new one comes out in December (probably) we can upgrade and fix that.

Anyway, I think it is much more likely that this build which was tested for some reason had something patched which asked for to_poly_solve to be used but didn't have to_poly_solver loaded by Maxima, as this is precisely the error message which would come out of that.  However, #6642 has both in Sage since 4.2.alpha0, so I don't think this should be a problem any more.


---

Comment by was created at 2009-10-29 18:58:56

Resolution: fixed
