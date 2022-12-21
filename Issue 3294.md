# Issue 3294: linear code bug: minimum_distance breaks over "large" fields

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-05-24 20:22:18

Assignee: rlm

This seems to be caused by a change in the interface to GAP. Related methods
(like spectrum) are also broken.


```
sage: C = ReedSolomonCode(4,3,GF(5)); C
Linear code of length 4, dimension 3 over Finite Field of size 5
sage: C.gen_mat()

[1 1 1 1]
[0 1 2 3]
[0 1 4 4]
sage: C.minimum_distance()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/wdj/sagefiles/sage-3.0.2.rc3/<ipython console> in <module>()

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/coding/linear_code.py in minimum_distance(self)
   1366         q = F.order()
   1367         G = self.gen_mat()
-> 1368         gapG = gap(G)
   1369         Gstr = "%s*Z(%s)^0"%(gapG, q)
   1370         return hamming_weight(min_wt_vec(Gstr,F))

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    948             return cls(self, x)
    949         try:
--> 950             return self._coerce_from_special_method(x)
    951         except TypeError:
    952             raise

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _coerce_from_special_method(self, x)
    972             s = '_gp_'
    973         try:
--> 974             return (x.__getattribute__(s))(self)
    975         except AttributeError:
    976             return self(x._interface_init_())

/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:2257)()

/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:1884)()

/home/wdj/sagefiles/sage-3.0.2.rc3/matrix1.pyx in sage.matrix.matrix1.Matrix._gap_init_ (sage/matrix/matrix1.c:1287)()

/home/wdj/sagefiles/sage-3.0.2.rc3/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_abstract._gap_init_ (sage/rings/integer_mod.c:3124)()

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)
    307         if len(x) == 0 or x[len(x) - 1] != ';':
    308             x += ';'
--> 309         s = Expect.eval(self, x)
    310         if newlines:
    311             return s

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, synchronize, **kwds)
    915         try:
    916             with gc_disabled():
--> 917                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    918         except KeyboardInterrupt:
    919             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    508                         return ''
    509                 else:
--> 510                     raise RuntimeError, message
    511
    512         except KeyboardInterrupt:

RuntimeError: Unexpected EOF from Gap executing Int(Z(5));
```



---

Comment by wdj created at 2008-05-24 20:27:22

This is wrong and I don't know how to close the ticket. What is true, at least on my machine, is that if you stop the command using ctl-C the restart it *then* the above happens. That might be a bug in the GAP interface, I don't know.

Sorry for the false alarm.


---

Comment by mabshoff created at 2008-05-24 20:30:36

This is still a bug then and somebody should come up with a better title then. 

Cheers,

Michael


---

Comment by wdj created at 2008-05-24 20:39:03

It breaks over *all* fields. This is after a GAP computation was stopped using ctl-C:


```
sage: C = HammingCode(3,GF(2))
sage: C
Linear code of length 7, dimension 4 over Finite Field of size 2
sage: C.minimum_distance()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/wdj/sagefiles/sage-3.0.2.rc3/<ipython console> in <module>()

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/coding/linear_code.py in minimum_distance(self)
   1366         q = F.order()
   1367         G = self.gen_mat()
-> 1368         gapG = gap(G)
   1369         Gstr = "%s*Z(%s)^0"%(gapG, q)
   1370         return hamming_weight(min_wt_vec(Gstr,F))

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    948             return cls(self, x)
    949         try:
--> 950             return self._coerce_from_special_method(x)
    951         except TypeError:
    952             raise

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _coerce_from_special_method(self, x)
    972             s = '_gp_'
    973         try:
--> 974             return (x.__getattribute__(s))(self)
    975         except AttributeError:
    976             return self(x._interface_init_())

/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:2257)()

/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:1884)()

/home/wdj/sagefiles/sage-3.0.2.rc3/matrix1.pyx in sage.matrix.matrix1.Matrix._gap_init_ (sage/matrix/matrix1.c:1287)()

/home/wdj/sagefiles/sage-3.0.2.rc3/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_abstract._gap_init_ (sage/rings/integer_mod.c:3124)()

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)
    307         if len(x) == 0 or x[len(x) - 1] != ';':
    308             x += ';'
--> 309         s = Expect.eval(self, x)
    310         if newlines:
    311             return s

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, synchronize, **kwds)
    915         try:
    916             with gc_disabled():
--> 917                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    918         except KeyboardInterrupt:
    919             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    508                         return ''
    509                 else:
--> 510                     raise RuntimeError, message
    511
    512         except KeyboardInterrupt:

RuntimeError: Unexpected EOF from Gap executing Int(Z(2));
sage:  
```



---

Comment by rlm created at 2008-05-25 01:30:19

Yes, the GAP interface needs a kick after using CTRL-C.


---

Comment by rlm created at 2008-08-10 03:38:39

Remove assignee rlm.


---

Comment by rlm created at 2008-08-10 03:38:39

Changing priority from major to critical.


---

Comment by rlm created at 2008-08-10 03:38:39

Changing component from coding theory to interfaces.


---

Comment by mhansen created at 2009-01-23 09:42:40

Set assignee to mhansen.


---

Comment by mhansen created at 2009-01-23 09:42:40

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-01-24 16:28:17

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 16:28:17

Merged in Sage 3.3.alpha2
