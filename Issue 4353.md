# Issue 4353: [with patch, needs review] make sure garbage collection is reenabled after an exception in timeit.

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-10-23 21:38:38

Assignee: cwitty




---

Attachment

This fixes the problem with timeit() but not with the magic version (%timeit).

But I realize that this one is a python problem.


```
sage: def f(): raise RuntimeError
....: 
sage: gc.enable()
sage: gc.isenabled()
True
sage: %timeit f()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (17, 0))

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Volumes/Place/anakha/Applications/sage/devel/<ipython console> in <module>()

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/iplib.pyc in ipmagic(self, arg_s)
    958         else:
    959             magic_args = self.var_expand(magic_args,1)
--> 960             return fn(magic_args)
    961 
    962     def ipalias(self,arg_s):

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/Magic.pyc in magic_timeit(self, parameter_s)
   1796             for i in range(1, 10):
   1797                 number *= 10
-> 1798                 if timer.timeit(number) >= 0.2:
   1799                     break
   1800         

/Volumes/Place/anakha/Applications/sage/local/lib/python/timeit.pyc in timeit(self, number)
    159         gcold = gc.isenabled()
    160         gc.disable()
--> 161         timing = self.inner(it, self.timer)
    162         if gcold:
    163             gc.enable()

/Volumes/Place/anakha/Applications/sage/devel/<magic-timeit> in inner(_it, _timer)

/Volumes/Place/anakha/Applications/sage/devel/<ipython console> in f()

RuntimeError: 
sage: gc.isenabled()
False
```



---

Comment by mabshoff created at 2008-10-26 03:18:41

Merged in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 03:18:41

Resolution: fixed
