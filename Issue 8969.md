# Issue 8969: problems with maxima inequalities

Issue created by migration from https://trac.sagemath.org/ticket/8969

Original creator: dsm

Original creation time: 2010-05-14 20:43:15

Assignee: burcin

'Sage Version 4.4.1, Release Date: 2010-05-02'
mac 10.4 32 bit running on 10.5.8.

sage: solve([2*x==3, x < 10], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)
sage: solve([2*x==3, x > 10], x)
[]
sage: solve([2*x==3, x == 10], x)
[]
sage: solve([2*x==3, x == 3/2], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

sage: solve([2*x==3, x < 4, x > 4], x)
[]


all work as expected, but:

sage: solve([2*x==3, x != 5], x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Applications/sage/devel/sage-main/build/sage/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)
    670                 s = []
    671 
--> 672         sol_list = string_to_list_of_solutions(repr(s))
    673         if 'solution_dict' in kwds and kwds!['solution_dict']==True:
    674             if isinstance(sol_list![0], list):

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in string_to_list_of_solutions(s)
    455     from sage.structure.sequence import Sequence
    456     from sage.calculus.calculus import symbolic_expression_from_maxima_string
--> 457     v = symbolic_expression_from_maxima_string(s, equals_sub=True)
    458     return Sequence(v, universe=Objects(), cr_str=True)
    459 

/Applications/sage/local/lib/python2.6/site-packages/sage/calculus/calculus.py in symbolic_expression_from_maxima_string(x, equals_sub, maxima)
   1527         return symbolic_expression_from_string(s, syms, accept_sequence=True)
   1528     except !!SyntaxError:
-> 1529         raise TypeError, "unable to make sense of Maxima expression '%s' in Sage"%s
   1530     finally:
   1531         is_simplified = False

TypeError: unable to make sense of Maxima expression '[This is the Trac macro *x==3/2,-7/2!==0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x==3/2,-7/2!==0-macro)' in Sage

--

The "!==" which is causing trouble is due to the

if equals_sub:
            s = s.replace('=','==')

lines in  symbolic_expression_from_maxima_string.  This could be fixed by changing the replace to a regexp, or adding a hack s = s.replace('!==', '!=') afterwards.

This deals with the obvious problem but not the underlying one, which is that the result is still IMHO underprocessed: 

MODIFIED_sage: solve([2*x==3, x != 4], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), )](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

when I wanted [This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2))](https://trac.sagemath.org/wiki/WikiMacros#x == -macro), or

MODIFIED_sage: solve([2*x==3, x != 3/2], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), 0 != 0)](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

when I wanted [].

In fact, even in cases not involving "!=", it's possible for maxima output -- %union([x = 3/2,  -5/2 # 0]) --  to be insufficiently processed,IMHO:

sage: solve([2*x==3, (x-4)!^2 > 0], x)
[This is the Trac macro *x == * that was inherited from the migration called with arguments (3/2), )](https://trac.sagemath.org/wiki/WikiMacros#x == -macro)

ISTM the extra information about what condition maxima used isn't worth the inconvenience of having to postprocess the solutions to see if one exists.


---

Comment by kcrisman created at 2011-06-14 17:59:49

DSM, is this really all one ticket? It's kind of confusing.


---

Comment by dsm created at 2012-05-25 23:45:32

Changing keywords from "" to "sd40.5".


---

Comment by dsm created at 2012-05-25 23:45:32

Changing status from new to needs_review.


---

Comment by dsm created at 2012-05-25 23:46:01

It was all one ticket in my head, but maybe it makes more sense to separate them.  Might as well address the low-hanging fruit.


---

Comment by kcrisman created at 2012-05-26 05:22:01

The problem wasn't really our translation of Maxima's inequality (`#`, which we finally fixed a while ago) but rather that we then had this little hack already.

But all of your tests already work in Sage 5.0, because of the `#` replacement.  It really has to test the original bug report example, otherwise this is trivial.  I suggest


```
sage: from sage.calculus.calculus import symbolic_expression_from_maxima_string as sefms 
sage: sefms("x != 3") == SR(x != 3) 
True
sage: sefms("x # 3") == SR(x != 3) 
True
sage:  solve([2*x==3, x != 5], x)
[[x == (3/2), (-7/2) != 0]]
```



---

Comment by dsm created at 2012-05-26 05:49:15

Oy, you're right that I truncated the original bug test (!).  But we do need to fix `!==` to round-trip neq, so I think it's worth doing.


---

Comment by dsm created at 2012-05-26 05:50:03

revised version


---

Comment by kcrisman created at 2012-05-26 06:36:26

Changing status from needs_review to positive_review.


---

Attachment

Positive review.


---

Comment by jdemeyer created at 2012-06-18 10:21:58

Resolution: fixed
