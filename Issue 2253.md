# Issue 2253: sage-2.10.2 -- timeit doctests not robust enough

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-21 22:50:39

Assignee: failure


```

Alpha2 installed and tested on Toshiba Laptop under Ubuntu.

make test failures:


       sage -t  devel/sage-main/sage/groups/group.pyx
       sage -t  devel/sage-main/sage/functions/special.py
       sage -t  devel/sage-main/sage/misc/sage_timeit_class.pyx
       sage -t  devel/sage-main/sage/misc/functional.py
       sage -t  devel/sage-main/sage/schemes/elliptic_curves/padics.py
       sage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py
       sage -t  devel/sage-main/sage/rings/padics/padic_ZZ_pX_CR_element.pyx
       sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
Total time for all tests: 4938.4 seconds

test log is on my server:

       http://www.billp.org/alpha2-test.log

if you need any further details.
Time for bed!

```


Looking at the actual doctest log suggest what to do to fix such things,
and I'll do it now.


---

Attachment


---

Comment by mabshoff created at 2008-02-21 23:05:33

Patch looks good to me, is obviously correct.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-21 23:06:36

Merged in Sage 2.10.2.rc0


---

Comment by mabshoff created at 2008-02-21 23:06:36

Resolution: fixed
