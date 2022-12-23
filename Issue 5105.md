# Issue 5105: behaviour of the norm function in the p-adic ring

Issue created by migration from https://trac.sagemath.org/ticket/5105

Original creator: ljpk

Original creation time: 2009-01-26 18:16:35

Assignee: was

The p-adic norm seems to be defined differently in SAGE to the standard textbook definition, in which it is usually normalized so that $|p|=1/p$, but this is what SAGE does:

```
sage: Q11=pAdicField(11)
sage: n=Q11(11)
sage: n.norm()
11 + O(11^21)
```

Would it be possible to swap it round so that the norm of 11 is given as 1/11?


---

Comment by mabshoff created at 2009-02-06 23:02:32

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by fwclarke created at 2009-02-10 18:37:54

Changing type from defect to enhancement.


---

Comment by fwclarke created at 2009-02-10 18:37:54

There is a confusion of terminology here.  It's the "field norm" that's defined for p-adics.  Thus

```
sage: Q11 = pAdicField(11, 6)
sage: F.<a> = Q11.ext(x^2 - 2)
sage: (2 + 3*a).norm()
8 + 9*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + O(11^6)
sage: (2 + 3*a)*(2 - 3*a)
8 + 9*11 + 10*11^2 + 10*11^3 + 10*11^4 + 10*11^5 + O(11^6)
```

So

```
sage: Q11(22).norm()
2*11 + O(11^7)
```

is correct, as is

```
sage: QQ(-163).norm()
-163
```

What you're wanting is usually called the p-adic absolute value (it's a norm in the functional analysis sense).  It would be
good if one could do

```
sage: Q11(22).abs()
```

and get 1/11.  This isn't currently defined, if z is an element of a padic field, the absolute value can be obtained as

```
z.parent().prime()^(-z.ordp())
```



---

Comment by cremona created at 2009-04-09 16:07:32

I thought this looked good, and it applied ok to 3.4.1.rc1, but I got a whole lot of doctest failures in sage/rings/padics:

```
The following tests failed:


        sage -t  "devel/sage-5105/sage/rings/padics/padic_generic.py"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CA_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/pow_computer_ext.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx"
        sage -t  "devel/sage-5105/sage/rings/padics/padic_printing.pyx"
```


Most look like this:

```
sage -t  "devel/sage-5105/sage/rings/padics/padic_generic.py"
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_generic.py", line 304:
    sage: y = W.teichmuller(3); y
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[14]>", line 1, in <module>
        y = W.teichmuller(Integer(3)); y###line 304:
    sage: y = W.teichmuller(3); y
      File "sage_object.pyx", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1342)
      File "padic_generic_element.pyx", line 212, in sage.rings.padics.padic_generic_element.pAdicGenericElement._repr_ (sage/rings/padics/padic_generic_element.c:6185)
      File "padic_printing.pyx", line 373, in sage.rings.padics.padic_printing.pAdicPrinter_class.repr_gen (sage/rings/padics/padic_printing.cpp:8469)
      File "padic_printing.pyx", line 460, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_gen (sage/rings/padics/padic_printing.cpp:9866)
      File "padic_printing.pyx", line 580, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_spec (sage/rings/padics/padic_printing.cpp:12415)
      File "padic_ext_element.pyx", line 171, in sage.rings.padics.padic_ext_element.pAdicExtElement._ext_p_list (sage/rings/padics/padic_ext_element.cpp:3643)
      File "padic_ext_element.pyx", line 162, in sage.rings.padics.padic_ext_element.pAdicExtElement.ext_p_list (sage/rings/padics/padic_ext_element.cpp:3540)
    NotImplementedError
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_generic.py", line 310:
    sage: b = A.teichmuller(1 + 2*a - a^2); b
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-3.4.1.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_11[18]>", line 1, in <module>
        b = A.teichmuller(Integer(1) + Integer(2)*a - a**Integer(2)); b###line 310:
    sage: b = A.teichmuller(1 + 2*a - a^2); b
      File "sage_object.pyx", line 98, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1342)
      File "padic_generic_element.pyx", line 212, in sage.rings.padics.padic_generic_element.pAdicGenericElement._repr_ (sage/rings/padics/padic_generic_element.c:6185)
      File "padic_printing.pyx", line 373, in sage.rings.padics.padic_printing.pAdicPrinter_class.repr_gen (sage/rings/padics/padic_printing.cpp:8469)
      File "padic_printing.pyx", line 460, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_gen (sage/rings/padics/padic_printing.cpp:9866)
      File "padic_printing.pyx", line 580, in sage.rings.padics.padic_printing.pAdicPrinter_class._repr_spec (sage/rings/padics/padic_printing.cpp:12415)
      File "padic_ext_element.pyx", line 171, in sage.rings.padics.padic_ext_element.pAdicExtElement._ext_p_list (sage/rings/padics/padic_ext_element.cpp:3643)
      File "padic_ext_element.pyx", line 162, in sage.rings.padics.padic_ext_element.pAdicExtElement.ext_p_list (sage/rings/padics/padic_ext_element.cpp:3540)
    NotImplementedError
**********************************************************************
1 items had failures:
   2 of  20 in __main__.example_11
```


while there also some simpler ones:

```
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx", line 80:
    sage: y.precision_relative()
Expected:
    20
Got:
    2
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_CR_element.pyx", line 82:
    sage: y.precision_absolute()
Expected:
    24
Got:
    6
```


and 

```
sage -t  "devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx"
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1214:
    sage: ((1+2*w)^5).norm()
Expected:
    1 + 5^2 + O(5^5)
Got:
    1 + O(5^2)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1216:
    sage: ((1+2*w)).norm()^5
Expected:
    1 + 5^2 + O(5^5)
Got:
    1 + O(5^2)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1246:
    sage: a.trace()
Expected:
    3*5 + 2*5^2 + 3*5^3 + 2*5^4 + O(5^5)
Got:
    O(5)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1248:
    sage: a.trace() + b.trace()
Expected:
    4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
Got:
    O(5)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1250:
    sage: (a+b).trace()
Expected:
    4*5 + 5^2 + 5^3 + 2*5^4 + O(5^5)
Got:
    O(5)
**********************************************************************
File "/home/jec/sage-3.4.1.rc1/devel/sage-5105/sage/rings/padics/padic_ZZ_pX_FM_element.pyx", line 1277:
    sage: c._ntl_rep()
Expected:
    [89 9 4 1]
Got:
    [4 4 4]
**********************************************************************
3 items had failures:
   2 of   8 in __main__.example_29
   3 of  11 in __main__.example_30
   1 of   8 in __main__.example_31
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/jec/sage-3.4.1.rc1/tmp/.doctest_padic_ZZ_pX_FM_element.py
         [1.4 s]
```


I have absolutely no idea what in the patch has caused this, but it needs to be looked at!


---

Comment by mabshoff created at 2009-04-26 19:55:48

Changing assignee from was to roed.


---

Comment by mabshoff created at 2009-04-26 19:55:48

Changing component from number theory to padics.


---

Comment by mabshoff created at 2009-05-11 09:09:46

I guess this is reviewed by #5778 and the issues reported here due to doctest failures have been fixed there.

Cheers,

Michael


---

Comment by roed created at 2009-05-11 10:10:35

Implements abs() and exlains the difference between it and norm()


---

Attachment

Positive review due to #5778 - credit goes to RobertWB.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 10:33:37

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 10:33:37

Resolution: fixed
