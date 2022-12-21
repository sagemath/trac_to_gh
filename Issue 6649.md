# Issue 6649: doctest failure in decorate.py (on OS X only)

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2009-07-28 18:06:40

Assignee: GeorgSWeber

It is a Python 2.6 issue:

```
sage -t -long "devel/sage/sage/parallel/decorate.py"
**********************************************************************
File "/Users/Shared/sage/sage-4.1.1.alpha1/devel/sage/sage/parallel/
decorate.py", line 64:
    sage: `@`parallel()
    def f(N): return N**Integer(2)
Expected nothing
Got:
    doctest:49: DeprecationWarning: os.popen2 is deprecated.  Use the
subprocess module.
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_3
***Test Failed*** 1 failures.
```



---

Attachment

tested against 4.1.1.alpha1


---

Comment by GeorgSWeber created at 2009-07-28 18:11:51

Changing status from new to assigned.


---

Comment by mhampton created at 2009-08-01 15:18:11

I can check this out on Tuesday.  Looks good just based on reading the patch.


---

Comment by wdj created at 2009-08-02 11:52:45

The patch applies fine to 4.1.1.rc0. I tested this out on an intel macbook running 10.4.11. The only error (which may or may not be related) was the following.


```
sage -t  "devel/sage/sage/symbolic/expression.pyx"          
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx", line 2503:
    sage: ((x+y)^a).match(w0^w1)
Expected:
    {$1: a, $0: x + y}
Got:
    {$0: x + y, $1: a}
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx", line 2509:
    sage: ((a+b)*(a+c)).match((a+w0)*(a+w1))
Expected:
    {$1: c, $0: b}
Got:
    {$0: b, $1: c}
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.rc0/devel/sage/sage/symbolic/expression.pyx", line 2515:
    sage: (a*(x+y)+a*z+b).match(a*w0+w1)
Expected:
    {$1: a*z + b, $0: x + y}
Got:
    {$0: x + y, $1: a*z + b}
**********************************************************************
1 items had failures:
   3 of  24 in __main__.example_62
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/davidjoyner/sagefiles/sage-4.1.1.rc0/tmp/.doctest_expression.py
         [38.4 s]
```



---

Comment by mvngu created at 2009-08-02 23:10:14

David: The doctest failures you got are, I think, harmless. By definition, a non-empty dictionary is made up of a number of key-value pairs, which are stored in an arbitrary but non-random order. You can think of a non-empty Python dictionary as a set of unordered key-value pairs. From your report, I see that there are 3 failures. If you compare

```
Expected:
    {$1: a, $0: x + y}
```

with

```
Got:
    {$0: x + y, $1: a}
```

you see that these two dictionaries are essentially the same. Again by comparison, the dictionaries

```
Expected:
    {$1: c, $0: b}
```

and

```
Got:
    {$0: b, $1: c}
```

are equivalent, and likewise for

```
Expected:
    {$1: a*z + b, $0: x + y}
```

and

```
Got:
    {$0: x + y, $1: a*z + b}
```

I would say that you can ignore these 3 failures.


---

Comment by wdj created at 2009-08-02 23:13:06

Okay, I would then give this a positive review. Is there more testing needed?


---

Comment by mvngu created at 2009-08-02 23:25:47

To be extra safe, apply the patch `trac_6649_doctest.patch` to a fresh clone of the main repository, rebuild the clone and run it. Then execute the following from the Sage command line:

```
sage: `@`parallel()
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: `@`parallel('reference')
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: sage.parallel.ncpus.ncpus()
24
```

The command `sage.parallel.ncpus.ncpus()` would return different answers depending on the number of CPU's on your system. In the case of the machine sage.math it returns 24, which is the number of cores on that machine. For an Intel Mac with dual core, I would expect `sage.parallel.ncpus.ncpus()` to return 2. But in any case, testing that command on a Mac should not result in a deprecation warning. The idea of Georg's patch is to prevent the deprecation warning when using a Mac.


---

Comment by wdj created at 2009-08-02 23:57:58

What I got agrees with what you said should happen:


```
Loading Sage library. Current Mercurial branch is: 6649
sage: `@`parallel()
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: `@`parallel('reference')
....: def f(N): return N^2
....: 
sage: v = list(f([1,2,4])); v.sort(); v
[(((1,), {}), 1), (((2,), {}), 4), (((4,), {}), 16)]
sage: sage.parallel.ncpus.ncpus()
2
sage: 
```

So changing this from "needs review" to "positive review".


---

Comment by mvngu created at 2009-08-03 06:21:51

Resolution: fixed
