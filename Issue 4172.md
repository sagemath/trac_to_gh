# Issue 4172: exception in timeit permanetly disables gc

Issue created by migration from Trac.

Original creator: anakha

Original creation time: 2008-09-23 05:44:42

Assignee: mabshoff


```
sage: import gc
sage: gc.isenabled()
True
sage: %timeit raise RuntimeError, "test"
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Volumes/Place/anakha/Applications/sage/devel/sage-tri/sage/geometry/<ipython console> in <module>()

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/iplib.py in ipmagic(self, arg_s)
    946         else:
    947             magic_args = self.var_expand(magic_args,1)
--> 948             return fn(magic_args)
    949 
    950     def ipalias(self,arg_s):

/Volumes/Place/anakha/Applications/sage/local/lib/python2.5/site-packages/IPython/Magic.py in magic_timeit(self, parameter_s)
   1779             for i in range(1, 10):
   1780                 number *= 10
-> 1781                 if timer.timeit(number) >= 0.2:
   1782                     break
   1783         

/Volumes/Place/anakha/Applications/sage/local/lib/python/timeit.py in timeit(self, number)
    159         gcold = gc.isenabled()
    160         gc.disable()
--> 161         timing = self.inner(it, self.timer)
    162         if gcold:
    163             gc.enable()

/Volumes/Place/anakha/Applications/sage/devel/sage-tri/sage/geometry/<magic-timeit> in inner(_it, _timer)

RuntimeError: test
sage: gc.isenabled()
False
```



---

Comment by mhansen created at 2008-10-23 21:41:28

Patch is up at #4353


---

Comment by mhansen created at 2008-10-23 21:41:28

Resolution: duplicate
