# Issue 4240: magma -- increase doctest coverage of magma.py from current 17% to 100%.

Issue created by migration from https://trac.sagemath.org/ticket/4240

Original creator: was

Original creation time: 2008-10-04 03:42:48

Assignee: was

CC:  georgsweber

Right now the doctest coverage of devel/sage/sage/interfaces/magma.py is a pitiful 17%.  Increase this to 100%.   This will involving adding about 59 doctests and docstrings.  See also #4231, which adds two docstrings/doctests.


---

Comment by was created at 2008-10-04 03:42:57

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2008-10-11 15:28:11

coverage up to 69% -- all non underscore methods are now documented.


---

Attachment

insert all needed # optional's


---

Attachment


---

Comment by GeorgSWeber created at 2008-10-11 22:00:26

Hi,

several issues.
On the one hand, the first patch does not apply cleanly against 3.1.3 alpha series, since the hunk in gap.py does not fit (the "prompt" funtion to be removed did get a doctest, so the automatism breaks).
More severely, there are invalid absolute paths in beginning with "/home/wstein/", specific to your local install, see what I get:


```
sage -t -long devel/sage-main/sage/interfaces/magma.py      **********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 598:
    sage: magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Can't open package spec file /home/wstein/sage/data/extcode/magma/spec2 for reading (No such file or directory)
Got:
    Traceback (most recent call last):
      File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[3]>", line 1, in <module>
        magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)###line 598:
    sage: magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)
      File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 605, in attach_spec
        raise RuntimeError, s.strip()
    RuntimeError: Can't open package spec file /Users/georgweber/Public/sage/sage-3.1.3.alpha1/data/extcode/magma/spec2 for reading (No such file or directory)
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 626:
    sage: print magma.load(SAGE_TMP + 'a.m')
Expected:
    Loading "/home/wstein/.sage//temp/one/.../a.m"
    hi
Got:
    Loading "/Users/georgweber/.sage//temp/susanne_webers_computer.local/602/a.m"
    hi
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 930:
    sage: magma.get_verbose("Groebner")
Expected:
    2
Got:
    0
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 948:
    sage: magma.GetVerbose("Groebner")
Expected:
    2
Got:
    0
**********************************************************************
4 items had failures:
   1 of   4 in __main__.example_18
   1 of   5 in __main__.example_19
   1 of   3 in __main__.example_27
   1 of   3 in __main__.example_28
***Test Failed*** 4 failures.
For whitespace errors, see the file /Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/.doctest_magma.py
         [34.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage-main/sage/interfaces/magma.py
Total time for all tests: 34.6 seconds
```


The path issues should go away with some triple dots.

However, I have no idea yet what that last "Groebner" issue is (Expected: 2; Got: 0).

My Magma install says: "Magma V2.14-9", what does yours say?

Cheers,
gsw


---

Comment by GeorgSWeber created at 2008-10-11 22:04:04

Ah,

we try to load a package, that can't be found.
This does not go away just using triple dots in paths, instead some environment variable magic has to be used, but might explain the Groebner thing.


---

Comment by was created at 2008-10-12 12:30:57

> not apply cleanly against 3.1.3 alpha 

It's against 3.1.2.

Regarding the Groebner output, I think you didn't apply all the patches, since you have

```
sage: magma.get_verbose("Groebner")
```

in your log above, but the input line should be

```
sage: magma.get_verbose("Groebner")        # optional
```


In particular, you are doing

```
        sage -t -long devel/sage-main/sage/interfaces/magma.py
```

which with the third patch above should essentially do almost nothing, since
you forgot to put --optional.


Regarding
> we try to load a package, that can't be found. This does not go away 
> just using triple dots in paths, instead some environment variable magic 
> has to be used, but might explain the Groebner thing. 

It is unrelated to Groebner.  This will go away by putting in some ...'s.


---

Comment by mabshoff created at 2008-10-12 15:28:07

I fixed all the problems and a trivial reviewer patch is coming up. I did delete two hunks from the part3 patch since it contained fixes already done independently due to a previous patch. Tests pass with and without optional except two failures due to using Magma 2.13 instead of 2.14 on the test machine, but I can live with that:

```
sage -t -long -optional devel/sage/sage/interfaces/magma.py 
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/magma.py", line 90:
    sage: print M2
Expected:
    Space of modular forms on Gamma_1(5) with character $.1, weight 2, and dimension 2 over Integer Ring.
Got:
    Space of modular forms on Gamma_1(5) with character all conjugates of [$.1], weight 2, and dimension 2 over Integer Ring.
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/magma.py", line 92:
    sage: print M2.Basis()   # note -- this has been changed to be *wrong* as below in Magma 2.14!!
Expected:
    [
    1 + 10*q^2 + 20*q^3 + 20*q^5 + 60*q^7 + 50*q^8 + 30*q^10 + O(q^12),
    q + q^2 + 2*q^3 + 3*q^4 + 5*q^5 + 2*q^6 + 6*q^7 + 5*q^8 + 7*q^9 + 5*q^10 + 12*q^11 + O(q^12)
    ]
Got:
    [
    1 + 10*q^2 + 20*q^3 + 20*q^5 + 60*q^7 + O(q^8),
    q + q^2 + 2*q^3 + 3*q^4 + 5*q^5 + 2*q^6 + 6*q^7 + O(q^8)
    ]
**********************************************************************
```



---

Comment by mabshoff created at 2008-10-12 15:33:38

Resolution: fixed


---

Comment by mabshoff created at 2008-10-12 15:33:38

Merged in Sage 3.1.3.rc0
