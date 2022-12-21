# Issue 5407: fractional gens?  not good -- (QQ^3).gen(4/3) gives (0,1,0)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-01 05:59:34

Assignee: was

This patch fixes the bug. 


---

Comment by mabshoff created at 2009-03-01 06:11:59

Nice try wstein :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 06:20:29

One doctest failure:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.alpha1$ ./sage -t -long devel/sage/sage/modules/free_module.py
sage -t -long "devel/sage/sage/modules/free_module.py"      
**********************************************************************
File "/scratch/mabshoff/sage-3.4.alpha1/devel/sage/sage/modules/free_module.py", line 1438:
    sage: (QQ^3).gen(4/3)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_37[7]>", line 1, in <module>
        (QQ**Integer(3)).gen(Integer(4)/Integer(3))###line 1438:
    sage: (QQ^3).gen(4/3)
      File "/scratch/mabshoff/sage-3.4.alpha1/local/lib/python2.5/site-packages/sage/modules/free_module.py", line 1445, in gen
        return self.basis()[i]
      File "rational.pyx", line 236, in sage.rings.rational.Rational.__index__ (sage/rings/rational.c:4371)
    TypeError: rational is not an integer
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 04:30:41

This is an updated Version of Wiliam's patch


---

Attachment

Ok, the problem has been fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 04:31:50

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 04:31:50

Resolution: fixed
