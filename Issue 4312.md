# Issue 4312: major @interact (hence pyprocessing) new bug in 3.1.3, still in 3.1.4

Issue created by migration from https://trac.sagemath.org/ticket/4312

Original creator: was

Original creation time: 2008-10-17 12:52:39

Assignee: cwitty

In 3.1.2 this worked fine. It's totally broken in 3.1.4.

```
sage@modular:~/build/sage-3.1.4$ more a.sage
@parallel(8)
def f(p):
    print p
    t = cputime()
    M = ModularSymbols(p^2,sign=1)
    w = M.atkin_lehner_operator(p)
    K = (w-1).kernel()
    N = K.new_subspace()
    D = N.decomposition()
    print cputime(t)
    M.save(str(p))
    save(D, '%s-decomp'%p)



sage@modular:~/build/sage-3.1.4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: load a.sage
sage: list(f([11,17]))
17
11
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/home2/sage/.sage/temp/modular/25347/_home2_sage_build_sage_3_1_4_a_sage_0.py in <module>()
----> 1
      2
      3
      4
      5

/home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/sage/parallel/multiprocessing.pyc in parallel_iter(processes, f, inputs)
     64
     65     result = p.imapUnordered(call_pickled_function, [ (fp, t) for t in inputs ])
---> 66     for res in result:
     67         yield res
     68

/home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/processing/pool.pyc in next(self, timeout)
    468         if success:
    469             return value
--> 470         raise value
    471
    472     def _set(self, i, obj):

NameError: global name '_sage_const_2' is not defined
sage:           
```


This is a pyprocessing problem since:

```
sage: load a.sage
sage: f(11)
11
0.168011
sage: f(13)
13
0.244015
sage:              
```

}}}


---

Comment by jason created at 2008-10-17 14:12:18

So does this issue have anything to do with `@`interact?  Or is it `@`parallel that has the problem?


---

Comment by mabshoff created at 2008-10-30 05:55:12

Bug Day 15 material? This certainly should get fixed in 3.2.

Cheers,

Michael


---

Comment by was created at 2008-11-16 20:05:32

I've posted a hack-ish patch that at least fixes this problem.  Something better might be to modify `@`parallel to more properly transfer all _sage_const*'s to subprocesses or something.


---

Attachment


---

Attachment


---

Comment by craigcitro created at 2008-11-18 09:40:04

Looks good. 

I made a new ticket to have someone find an *actual* fix, which is #4545. I also edited the patch to have this info in it, and posted that above.


---

Comment by mabshoff created at 2008-11-18 18:17:21

Resolution: fixed


---

Comment by mabshoff created at 2008-11-18 18:17:21

Merged sage-4312-edited.patch in Sage 3.2.rc2
