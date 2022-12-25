# Issue 3294: linear code bug: minimum_distance breaks over "large" fields

archive/issues_003294.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis seems to be caused by a change in the interface to GAP. Related methods\n(like spectrum) are also broken.\n\n\n```\nsage: C = ReedSolomonCode(4,3,GF(5)); C\nLinear code of length 4, dimension 3 over Finite Field of size 5\nsage: C.gen_mat()\n\n[1 1 1 1]\n[0 1 2 3]\n[0 1 4 4]\nsage: C.minimum_distance()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/<ipython console> in <module>()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/coding/linear_code.py in minimum_distance(self)\n   1366         q = F.order()\n   1367         G = self.gen_mat()\n-> 1368         gapG = gap(G)\n   1369         Gstr = \"%s*Z(%s)^0\"%(gapG, q)\n   1370         return hamming_weight(min_wt_vec(Gstr,F))\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)\n    948             return cls(self, x)\n    949         try:\n--> 950             return self._coerce_from_special_method(x)\n    951         except TypeError:\n    952             raise\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _coerce_from_special_method(self, x)\n    972             s = '_gp_'\n    973         try:\n--> 974             return (x.__getattribute__(s))(self)\n    975         except AttributeError:\n    976             return self(x._interface_init_())\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:2257)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:1884)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/matrix1.pyx in sage.matrix.matrix1.Matrix._gap_init_ (sage/matrix/matrix1.c:1287)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_abstract._gap_init_ (sage/rings/integer_mod.c:3124)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)\n    307         if len(x) == 0 or x[len(x) - 1] != ';':\n    308             x += ';'\n--> 309         s = Expect.eval(self, x)\n    310         if newlines:\n    311             return s\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, synchronize, **kwds)\n    915         try:\n    916             with gc_disabled():\n--> 917                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    918         except KeyboardInterrupt:\n    919             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    508                         return ''\n    509                 else:\n--> 510                     raise RuntimeError, message\n    511\n    512         except KeyboardInterrupt:\n\nRuntimeError: Unexpected EOF from Gap executing Int(Z(5));\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3294\n\n",
    "created_at": "2008-05-24T20:22:18Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "linear code bug: minimum_distance breaks over \"large\" fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3294",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @rlmill

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


Issue created by migration from https://trac.sagemath.org/ticket/3294





---

archive/issue_events_007395.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-24T20:25:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3294#event-7395"
}
```



---

archive/issue_comments_022735.json:
```json
{
    "body": "This is wrong and I don't know how to close the ticket. What is true, at least on my machine, is that if you stop the command using ctl-C the restart it *then* the above happens. That might be a bug in the GAP interface, I don't know.\n\nSorry for the false alarm.",
    "created_at": "2008-05-24T20:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22735",
    "user": "https://github.com/wdjoyner"
}
```

This is wrong and I don't know how to close the ticket. What is true, at least on my machine, is that if you stop the command using ctl-C the restart it *then* the above happens. That might be a bug in the GAP interface, I don't know.

Sorry for the false alarm.



---

archive/issue_comments_022736.json:
```json
{
    "body": "This is still a bug then and somebody should come up with a better title then. \n\nCheers,\n\nMichael",
    "created_at": "2008-05-24T20:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22736",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still a bug then and somebody should come up with a better title then. 

Cheers,

Michael



---

archive/issue_comments_022737.json:
```json
{
    "body": "It breaks over *all* fields. This is after a GAP computation was stopped using ctl-C:\n\n\n```\nsage: C = HammingCode(3,GF(2))\nsage: C\nLinear code of length 7, dimension 4 over Finite Field of size 2\nsage: C.minimum_distance()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/<ipython console> in <module>()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/coding/linear_code.py in minimum_distance(self)\n   1366         q = F.order()\n   1367         G = self.gen_mat()\n-> 1368         gapG = gap(G)\n   1369         Gstr = \"%s*Z(%s)^0\"%(gapG, q)\n   1370         return hamming_weight(min_wt_vec(Gstr,F))\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)\n    948             return cls(self, x)\n    949         try:\n--> 950             return self._coerce_from_special_method(x)\n    951         except TypeError:\n    952             raise\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _coerce_from_special_method(self, x)\n    972             s = '_gp_'\n    973         try:\n--> 974             return (x.__getattribute__(s))(self)\n    975         except AttributeError:\n    976             return self(x._interface_init_())\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._gap_ (sage/structure/sage_object.c:2257)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/sage_object.pyx in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:1884)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/matrix1.pyx in sage.matrix.matrix1.Matrix._gap_init_ (sage/matrix/matrix1.c:1287)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_abstract._gap_init_ (sage/rings/integer_mod.c:3124)()\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)\n    307         if len(x) == 0 or x[len(x) - 1] != ';':\n    308             x += ';'\n--> 309         s = Expect.eval(self, x)\n    310         if newlines:\n    311             return s\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, synchronize, **kwds)\n    915         try:\n    916             with gc_disabled():\n--> 917                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    918         except KeyboardInterrupt:\n    919             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/home/wdj/sagefiles/sage-3.0.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    508                         return ''\n    509                 else:\n--> 510                     raise RuntimeError, message\n    511\n    512         except KeyboardInterrupt:\n\nRuntimeError: Unexpected EOF from Gap executing Int(Z(2));\nsage:  \n```\n",
    "created_at": "2008-05-24T20:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22737",
    "user": "https://github.com/wdjoyner"
}
```

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

archive/issue_comments_022738.json:
```json
{
    "body": "Yes, the GAP interface needs a kick after using CTRL-C.",
    "created_at": "2008-05-25T01:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22738",
    "user": "https://github.com/rlmill"
}
```

Yes, the GAP interface needs a kick after using CTRL-C.



---

archive/issue_events_007396.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-08-10T03:38:39Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3294#event-7396"
}
```



---

archive/issue_events_007397.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-08-10T03:38:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3294#event-7397"
}
```



---

archive/issue_comments_022739.json:
```json
{
    "body": "Remove assignee @rlmill.",
    "created_at": "2008-08-10T03:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22739",
    "user": "https://github.com/rlmill"
}
```

Remove assignee @rlmill.



---

archive/issue_comments_022740.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-08-10T03:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22740",
    "user": "https://github.com/rlmill"
}
```

Changing priority from major to critical.



---

archive/issue_comments_022741.json:
```json
{
    "body": "Changing component from coding theory to interfaces.",
    "created_at": "2008-08-10T03:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22741",
    "user": "https://github.com/rlmill"
}
```

Changing component from coding theory to interfaces.



---

archive/issue_comments_022742.json:
```json
{
    "body": "Set assignee to @mwhansen.",
    "created_at": "2009-01-23T09:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22742",
    "user": "https://github.com/mwhansen"
}
```

Set assignee to @mwhansen.



---

archive/issue_comments_022743.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T09:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22743",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022744.json:
```json
{
    "body": "Attachment [trac_3294.patch](tarball://root/attachments/some-uuid/ticket3294/trac_3294.patch) by @mwhansen created at 2009-01-23 09:43:41",
    "created_at": "2009-01-23T09:43:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22744",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3294.patch](tarball://root/attachments/some-uuid/ticket3294/trac_3294.patch) by @mwhansen created at 2009-01-23 09:43:41



---

archive/issue_events_007398.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T16:28:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3294#event-7398"
}
```



---

archive/issue_comments_022745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T16:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022746.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T16:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3294#issuecomment-22746",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_events_007399.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T16:29:10Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3294#event-7399"
}
```



---

archive/issue_events_007400.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T16:29:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3294",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3294#event-7400"
}
```
