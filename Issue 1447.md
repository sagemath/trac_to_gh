# Issue 1447: Polybori permissions issues

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2007-12-10 10:18:19

Assignee: burcin


```
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/gbrefs.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/memusage.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/nf.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/ll.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/randompoly.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/PyPolyBoRi.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/heuristics.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/coding.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/statistics.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/blocks.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/__init__.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/dynamic/__init__.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/gbcore.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/specialsets.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/aes.pyc'
[Errno 13] Permission denied: '/home/rlmill/sage-2.9.alpha4-sage-math-only-x86_64-Linux/local/lib/python//site-packages/polybori/check_claims.pyc'
```



---

Comment by burcin created at 2007-12-15 10:53:48

Changing component from commutative algebra to packages.


---

Comment by burcin created at 2007-12-15 10:53:48

This was caused by an absolute symlink in the polybori package polybori-0.1.p4.spkg, included in alpha4. Update to polybori-0.1-r5.spkg makes the symlinks relative and fixes the problem.

New package is included in 2.9.alpha7.


---

Comment by burcin created at 2007-12-15 10:53:48

Resolution: fixed
