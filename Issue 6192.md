# Issue 6192: numerical noise on x86 fedora core 8 (cicero on skynet)

Issue created by migration from https://trac.sagemath.org/ticket/6192

Original creator: was

Original creation time: 2009-06-02 21:56:13

Assignee: tbd


```
sage -t  "devel/sage/sage/calculus/calculus.py"
**********************************************************************
File "/home/wstein/build-4.4.0/cicero/sage-4.0.1.alpha0/devel/sage/sage/calculus/calculus.py", line 700:
    sage: numerical_integral(f, 0, 1)
Expected:
    (0.52848223225314706, 6.8392846084921134e-07)
Got:
    (0.52848223225314706, 6.8392846078917534e-07)
**********************************************************************
1 items had failures:
   1 of  16 in __main__.example_2
```


Noise or a bug?

```
sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
**********************************************************************
File "/home/wstein/build-4.4.0/cicero/sage-4.0.1.alpha0/devel/sage/sage/rings/number_field/number_field_element.pyx", line 
766:
    sage: CDF(a)
Expected:
    1.0*I
Got:
    -2.88668828424e-18 - 1.0*I
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_21
***Test Failed*** 1 failures.
```



---

Comment by was created at 2009-06-02 22:03:13

The second issue is because the roots of x^2+1 are "sorted" as complex numbers, and because of numerical noise, the roots are swapped.


---

Attachment


---

Comment by mhansen created at 2009-06-04 06:29:51

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 06:29:51

Looks good to me.

Merged in 4.0.1.rc0.
