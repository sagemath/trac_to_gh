# Issue 991: problem in interaction with Singular subprocesses

archive/issues_000991.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following happens in 2.8.9.rc1, on 32-bit and 64-bit x86 Linux.\nNote that the problem does not occur if the \"T = ...\" line is omitted.\n\n\n```\ncwitty@comet:~/sage-2.8.9.rc1$ ./sage\n\nsage: K.<w> = GF(27)\nsage: P.<x, y> = PolynomialRing(K, 2, order='lex')\nsage: I = Ideal([ x^8 + y + 2, y^6 + x*y^5 + x^2 ])\nsage: T = I.triangular_decomposition('singular:triangLfak')\nsage: I.variety()\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/home/cwitty/sage-2.8.9.rc1/<ipython console> in <module>()\n\n/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in variety(self)\n   1113 \n   1114         P = self.ring()\n-> 1115         T = self.triangular_decomposition('singular:triangLfak')\n   1116 \n   1117         V = []\n\n/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in triangular_decomposition(self, algorithm)\n    426         P = self.ring()\n    427 \n--> 428         is_groebner = self.basis_is_groebner()\n    429 \n    430         # make sure to work w.r.t. 'lex'\n\n/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in basis_is_groebner(self)\n    913         LTF = singular( [f.lt() for f in self.gens()] , \"module\" )\n    914 \n--> 915         M = (F * LTF.syz()).reduce(self._singular_())\n    916 \n    917         for i in range(M.nrows()):\n\n/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_(self, singular)\n    214         if singular is None: singular = singular_default\n    215         try:\n--> 216             self.ring()._singular_(singular).set_ring()            \n    217             I = self.__singular\n    218             if not (I.parent() is singular):\n\n/home/cwitty/sage-2.8.9.rc1/multi_polynomial_libsingular.pyx in multi_polynomial_libsingular.MPolynomialRing_libsingular._singular_()\n\n/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in eval(self, x, allow_semicolon, strip)\n    372 \n    373             if s.find(\"error\") != -1 or s.find(\"Segment fault\") != -1:\n--> 374                 raise RuntimeError, 'Singular error:\\n%s'%s\n    375         finally:\n    376             gc.enable()\n\n<type 'exceptions.RuntimeError'>: Singular error:\n   ? type 444 too complex...set minpoly before\n   ? error occurred in STDIN line 166: `minpoly=(w^3+2*w+1);`\nsage: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/991\n\n",
    "created_at": "2007-10-25T01:19:31Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "problem in interaction with Singular subprocesses",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/991",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

The following happens in 2.8.9.rc1, on 32-bit and 64-bit x86 Linux.
Note that the problem does not occur if the "T = ..." line is omitted.


```
cwitty@comet:~/sage-2.8.9.rc1$ ./sage

sage: K.<w> = GF(27)
sage: P.<x, y> = PolynomialRing(K, 2, order='lex')
sage: I = Ideal([ x^8 + y + 2, y^6 + x*y^5 + x^2 ])
sage: T = I.triangular_decomposition('singular:triangLfak')
sage: I.variety()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/home/cwitty/sage-2.8.9.rc1/<ipython console> in <module>()

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in variety(self)
   1113 
   1114         P = self.ring()
-> 1115         T = self.triangular_decomposition('singular:triangLfak')
   1116 
   1117         V = []

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in triangular_decomposition(self, algorithm)
    426         P = self.ring()
    427 
--> 428         is_groebner = self.basis_is_groebner()
    429 
    430         # make sure to work w.r.t. 'lex'

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in basis_is_groebner(self)
    913         LTF = singular( [f.lt() for f in self.gens()] , "module" )
    914 
--> 915         M = (F * LTF.syz()).reduce(self._singular_())
    916 
    917         for i in range(M.nrows()):

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py in _singular_(self, singular)
    214         if singular is None: singular = singular_default
    215         try:
--> 216             self.ring()._singular_(singular).set_ring()            
    217             I = self.__singular
    218             if not (I.parent() is singular):

/home/cwitty/sage-2.8.9.rc1/multi_polynomial_libsingular.pyx in multi_polynomial_libsingular.MPolynomialRing_libsingular._singular_()

/home/cwitty/sage-2.8.9.rc1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in eval(self, x, allow_semicolon, strip)
    372 
    373             if s.find("error") != -1 or s.find("Segment fault") != -1:
--> 374                 raise RuntimeError, 'Singular error:\n%s'%s
    375         finally:
    376             gc.enable()

<type 'exceptions.RuntimeError'>: Singular error:
   ? type 444 too complex...set minpoly before
   ? error occurred in STDIN line 166: `minpoly=(w^3+2*w+1);`
sage: 
```


Issue created by migration from https://trac.sagemath.org/ticket/991





---

archive/issue_comments_006024.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2007-11-17T17:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/991#issuecomment-6024",
    "user": "https://github.com/malb"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_006025.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-17T17:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/991#issuecomment-6025",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006026.json:
```json
{
    "body": "Attachment [trac_991.patch](tarball://root/attachments/some-uuid/ticket991/trac_991.patch) by @malb created at 2007-11-17 17:21:29\n\nThe attached patch fixes this issue for me.",
    "created_at": "2007-11-17T17:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/991#issuecomment-6026",
    "user": "https://github.com/malb"
}
```

Attachment [trac_991.patch](tarball://root/attachments/some-uuid/ticket991/trac_991.patch) by @malb created at 2007-11-17 17:21:29

The attached patch fixes this issue for me.



---

archive/issue_comments_006027.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-11-17T17:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/991#issuecomment-6027",
    "user": "https://github.com/malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_events_002737.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-11-17T17:21:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "milestone": "sage-2.8.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/991#event-2737"
}
```



---

archive/issue_comments_006028.json:
```json
{
    "body": "Attachment [trac_991_doctest.patch](tarball://root/attachments/some-uuid/ticket991/trac_991_doctest.patch) by @williamstein created at 2007-11-20 15:33:24\n\nLooks good to me, probably.  It's just a format issue anyways.",
    "created_at": "2007-11-20T15:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/991#issuecomment-6028",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_991_doctest.patch](tarball://root/attachments/some-uuid/ticket991/trac_991_doctest.patch) by @williamstein created at 2007-11-20 15:33:24

Looks good to me, probably.  It's just a format issue anyways.



---

archive/issue_events_002738.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-20T15:51:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/991#event-2738"
}
```



---

archive/issue_comments_006029.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-20T15:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/991#issuecomment-6029",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006030.json:
```json
{
    "body": "Merged in 2.8.13.rc1.",
    "created_at": "2007-11-20T15:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/991",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/991#issuecomment-6030",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.13.rc1.
