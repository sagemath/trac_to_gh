# Issue 6943: Make @parallel work for callable objects

Issue created by migration from https://trac.sagemath.org/ticket/6943

Original creator: boothby

Original creation time: 2009-09-16 02:07:16

Assignee: boothby

CC:  was craigcitro rlm

The following should work:


```
@parallel
@cached_function
def foo(x):
    return x+1
```


however, when we attempt to evaluate foo...


```
sage: for k in foo(range(200)):
...       print k
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/boothby/.sage/sage_notebook/worksheets/admin/69/code/995.py", line 7, in <module>
    for k in foo(range(_sage_const_200 )):\u000a    print k
  File "", line 1, in <module>
    
  File "/scratch/boothby/sage/local/lib/python2.6/site-packages/sage/parallel/multiprocessing.py", line 63, in parallel_iter
    fp = pickle_function(f)
  File "fpickle.pyx", line 60, in sage.misc.fpickle.pickle_function (sage/misc/fpickle.c:746)
AttributeError: 'CachedFunction' object has no attribute 'func_code'
```


If any callable object is picklable, it should work with the parallel decorator.


---

Comment by boothby created at 2009-09-20 04:49:07

depends on #6927 and #6937


---

Attachment


---

Attachment

Rebased on referee patch of #6927. Depends on #6927. Apply this patch only


---

Comment by timdumol created at 2009-11-30 16:50:52

Things work perfectly and as advertised. Positive review on my part, but my referee patch must be reviewed by someone else.


---

Comment by was created at 2010-01-21 16:11:16

Hi,

This asks for:
 (1) not pickling args, and (2) timeouts. 

#6967 also does both as a biproduct.


---

Comment by mpatel created at 2010-01-31 03:26:55

Should we close this ticket as fixed?


---

Comment by mvngu created at 2010-01-31 18:21:20

Resolution: fixed


---

Comment by mvngu created at 2010-01-31 18:21:20

Close as fixed by #6967.
