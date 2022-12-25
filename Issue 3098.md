# Issue 3098: [with patch; positive review] doctest failure in devel/sage/sage/rings/ring.pyx

archive/issues_003098.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nFile \"/data2/wpalenst/sage-3.0.1.rc0/tmp/ring.py\", line 879:\n    sage: S.<a,b> = R.quotient_ring((x^2, y))\nException raised:\n    Traceback (most recent call last):\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_39[6]>\", line 1, in <module>\n        S = R.quotient_ring((x**Integer(2), y),names=('a', 'b')); (a, b,) = S._first_ngens(Integer(2))###line 879:\n    sage: S.<a,b> = R.quotient_ring((x^2, y))\n      File \"parent_gens.pyx\", line 200, in sage.structure.parent_gens.ParentWithGens._first_ngens (devel/sage/sage/structure/parent_gens.c:1377)\n      File \"parent_gens.pyx\", line 283, in sage.structure.parent_gens.ParentWithGens.gens (devel/sage/sage/structure/parent_gens.c:1916)\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py\", line 496, in gen\n        return self(self.__R.gen(i))\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py\", line 404, in __call__\n        return quotient_ring_element.QuotientRingElement(self, x)\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py\", line 74, in __init__\n        self._reduce_()\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py\", line 78, in _reduce_\n        self.__rep = I.reduce(self.__rep)\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1919, in reduce\n        gb = self.groebner_basis()\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1835, in groebner_basis\n        gb = self._groebner_basis_using_singular(\"groebner\", *args, **kwds)\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 326, in wrapper\n        return func(*args, **kwds)\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 312, in __exit__\n        self.singular.option(\"set\",self.o)\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 803, in option\n        self.eval(\"option(set,%s)\"%val.name())\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 423, in eval\n        raise RuntimeError, 'Singular error:\\n%s'%s\n    RuntimeError: Singular error:\n       ? unknown option `set`\n       ? unknown option `sage33`\n       ? error occurred in STDIN line 3: `option(set,sage33);`\n**********************************************************************\nFile \"/data2/wpalenst/sage-3.0.1.rc0/tmp/ring.py\", line 884:\n    sage: a == b\nException raised:\n    Traceback (most recent call last):\n      File \"/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_39[9]>\", line 1, in <module>\n        a == b###line 884:\n    sage: a == b\n    NameError: name 'a' is not defined\n**********************************************************************\n1 items had failures:\n   2 of  10 in __main__.example_39\n***Test Failed*** 2 failures.\n```\n\nSince this might be strangeness in the singular pexpect interface, I'm attaching a log file of that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3098\n\n",
    "closed_at": "2008-05-04T17:40:23Z",
    "created_at": "2008-05-03T19:08:14Z",
    "labels": [
        "component: interfaces",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; positive review] doctest failure in devel/sage/sage/rings/ring.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3098",
    "user": "https://github.com/wjp"
}
```
Assignee: @williamstein

```
File "/data2/wpalenst/sage-3.0.1.rc0/tmp/ring.py", line 879:
    sage: S.<a,b> = R.quotient_ring((x^2, y))
Exception raised:
    Traceback (most recent call last):
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_39[6]>", line 1, in <module>
        S = R.quotient_ring((x**Integer(2), y),names=('a', 'b')); (a, b,) = S._first_ngens(Integer(2))###line 879:
    sage: S.<a,b> = R.quotient_ring((x^2, y))
      File "parent_gens.pyx", line 200, in sage.structure.parent_gens.ParentWithGens._first_ngens (devel/sage/sage/structure/parent_gens.c:1377)
      File "parent_gens.pyx", line 283, in sage.structure.parent_gens.ParentWithGens.gens (devel/sage/sage/structure/parent_gens.c:1916)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py", line 496, in gen
        return self(self.__R.gen(i))
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py", line 404, in __call__
        return quotient_ring_element.QuotientRingElement(self, x)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py", line 74, in __init__
        self._reduce_()
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py", line 78, in _reduce_
        self.__rep = I.reduce(self.__rep)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1919, in reduce
        gb = self.groebner_basis()
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1835, in groebner_basis
        gb = self._groebner_basis_using_singular("groebner", *args, **kwds)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 326, in wrapper
        return func(*args, **kwds)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 312, in __exit__
        self.singular.option("set",self.o)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 803, in option
        self.eval("option(set,%s)"%val.name())
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 423, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? unknown option `set`
       ? unknown option `sage33`
       ? error occurred in STDIN line 3: `option(set,sage33);`
**********************************************************************
File "/data2/wpalenst/sage-3.0.1.rc0/tmp/ring.py", line 884:
    sage: a == b
Exception raised:
    Traceback (most recent call last):
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_39[9]>", line 1, in <module>
        a == b###line 884:
    sage: a == b
    NameError: name 'a' is not defined
**********************************************************************
1 items had failures:
   2 of  10 in __main__.example_39
***Test Failed*** 2 failures.
```

Since this might be strangeness in the singular pexpect interface, I'm attaching a log file of that.

Issue created by migration from https://trac.sagemath.org/ticket/3098





---

archive/issue_comments_021345.json:
```json
{
    "body": "Attachment [singular_bad.log](tarball://root/attachments/some-uuid/ticket3098/singular_bad.log) by @wjp created at 2008-05-03 19:58:14\n\nSome further debugging shows that the problem here is caused by `expect._synchronize` being called while _another_ `expect._synchronize` is running. This caused the outer `_synchronize` to miss its trigger and time-out.\n\nThe inner one was called through the garbage collector calling `ExpectElement.__del__`  calling `clear()` calling `eval()` calling `_synchronize()`.",
    "created_at": "2008-05-03T19:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21345",
    "user": "https://github.com/wjp"
}
```

Attachment [singular_bad.log](tarball://root/attachments/some-uuid/ticket3098/singular_bad.log) by @wjp created at 2008-05-03 19:58:14

Some further debugging shows that the problem here is caused by `expect._synchronize` being called while _another_ `expect._synchronize` is running. This caused the outer `_synchronize` to miss its trigger and time-out.

The inner one was called through the garbage collector calling `ExpectElement.__del__`  calling `clear()` calling `eval()` calling `_synchronize()`.



---

archive/issue_comments_021346.json:
```json
{
    "body": "Attachment [sage-3098.patch](tarball://root/attachments/some-uuid/ticket3098/sage-3098.patch) by @williamstein created at 2008-05-03 21:26:59",
    "created_at": "2008-05-03T21:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21346",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3098.patch](tarball://root/attachments/some-uuid/ticket3098/sage-3098.patch) by @williamstein created at 2008-05-03 21:26:59



---

archive/issue_comments_021347.json:
```json
{
    "body": "After applying this patch the doctest of `sage/schemes/generic/divisor.py` hangs with the following in the singular pexpect log:\n\n```\n> intvec sage241=. if(defined(sage220)>0){kill sage220;}\nintvec sage241=. if(defined(sage220)>0){kill sage220;}\n   ? error occurred in STDIN line 1059: `intvec sage241=. if(defined(sage220)>0){kill sage220;}`\n   ? expected intvec-expression. type 'help intvec;'\n   ? last reserved name was `intvec`\n   skipping text from ` `. \nquit\n\nAuf Wiedersehen.\n```",
    "created_at": "2008-05-03T22:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21347",
    "user": "https://github.com/wjp"
}
```

After applying this patch the doctest of `sage/schemes/generic/divisor.py` hangs with the following in the singular pexpect log:

```
> intvec sage241=. if(defined(sage220)>0){kill sage220;}
intvec sage241=. if(defined(sage220)>0){kill sage220;}
   ? error occurred in STDIN line 1059: `intvec sage241=. if(defined(sage220)>0){kill sage220;}`
   ? expected intvec-expression. type 'help intvec;'
   ? last reserved name was `intvec`
   skipping text from ` `. 
quit

Auf Wiedersehen.
```



---

archive/issue_comments_021348.json:
```json
{
    "body": "It looks like it just needed an extra semicolon at the end, actually. I don't have time to finish a -testall now, but pending that, positive review.",
    "created_at": "2008-05-03T23:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21348",
    "user": "https://github.com/wjp"
}
```

It looks like it just needed an extra semicolon at the end, actually. I don't have time to finish a -testall now, but pending that, positive review.



---

archive/issue_comments_021349.json:
```json
{
    "body": "Attachment [3098-semicolon.patch](tarball://root/attachments/some-uuid/ticket3098/3098-semicolon.patch) by mabshoff created at 2008-05-04 05:32:46\n\nWith both patches applied I get four doctest failures:\n\n```\nsage -t -long devel/sage/sage/schemes/generic/algebraic_scheme.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/algebraic_scheme.py\", line 374:\n    sage: loads(S.dumps()) == S\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_10\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_algebraic_scheme.py\n         [3.8 s]\nexit code: 1024\n```\nAnd:\n\n```\nsage -t -long devel/sage/sage/rings/polynomial/polynomial_singular_interface.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/polynomial_singular_interface.py\", line 330:\n    sage: R(h^20) == f^20\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[11]>\", line 1, in <module>\n        R(h**Integer(20)) == f**Integer(20)###line 330:\n    sage: R(h^20) == f^20\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 1056, in __call__\n        raise TypeError, \"Unable to coerce singular object\"\n    TypeError: Unable to coerce singular object\n**********************************************************************\n1 items had failures:\n   1 of  12 in __main__.example_6\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_polynomial_singular_interface.py\n         [3.4 s]\nexit code: 1024\n```\nAnd:\n\n```\nsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/multi_polynomial_ideal.py\", line 502:\n    sage: reduce(lambda Qi,Qj: Qi.intersection(Qj), [Qi for (Qi,radQi) in pd]) == I\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/multi_polynomial_ideal.py\", line 1886:\n    sage: J.groebner_basis()\nExpected:\n    [x + y + z, y^2 + y*z + z^2, z^3 - 1]\nGot:\n    [x + y + z, x*y + x*z + y*z, y^2 + y*z + z^2, x*y*z - 1, z^3 - 1]\n**********************************************************************\n2 items had failures:\n   1 of   8 in __main__.example_14\n   1 of   9 in __main__.example_44\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_multi_polynomial_ideal.py\n         [6.1 s]\nexit code: 1024\n```\nAnd:\n\n```\nsage -t -long devel/sage/sage/interfaces/singular.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/singular.py\", line 238:\n    sage: a = singular('2')*3; a\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[59]>\", line 1, in <module>\n        a = singular('2')*Integer(3); a###line 238:\n    sage: a = singular('2')*3; a\n      File \"element.pyx\", line 1374, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:8544)\n      File \"coerce.pyx\", line 265, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5005)\n      File \"coerce.pyx\", line 455, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c (sage/structure/coerce.c:7010)\n      File \"coerce.pyx\", line 511, in sage.structure.coerce.CoercionModel_cache_maps.discover_action_c (sage/structure/coerce.c:7489)\n      File \"parent.pyx\", line 213, in sage.structure.parent.Parent.get_action_c (sage/structure/parent.c:1829)\n      File \"parent.pyx\", line 282, in sage.structure.parent.Parent.get_action_c_impl (sage/structure/parent.c:2641)\n      File \"parent.pyx\", line 696, in sage.structure.parent._register_pair (sage/structure/parent.c:6199)\n      File \"parent.pyx\", line 689, in sage.structure.parent.EltPair.__eq__ (sage/structure/parent.c:6049)\n      File \"element.pyx\", line 623, in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:4551)\n      File \"element.pyx\", line 595, in sage.structure.element.Element._richcmp (sage/structure/element.c:4446)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1257, in __cmp__\n        if P.eval(\"%s %s %s\"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/interfaces/singular.py\", line 423, in eval\n        raise RuntimeError, 'Singular error:\\n%s'%s\n    RuntimeError: Singular error:\n       ? `sage60` is not defined\n       ? error occurred in STDIN line 52: `sage60 < sage60;`\n**********************************************************************\n1 items had failures:\n   1 of  61 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_singular.pyException exceptions.RuntimeError: RuntimeError('Singular error:\\n   ? `sage60` is not defined\\n   ? error occurred in STDIN line 36: `sage60 < sage60;`',) in 'sage.structure.parent._unregister_pair' ignored\nException exceptions.RuntimeError: RuntimeError('Singular error:\\n   ? `sage60` is not defined\\n   ? error occurred in STDIN line 38: `sage60 < sage60;`',) in 'sage.structure.parent._unregister_pair' ignored\n\n         [3.3 s]\nexit code: 1024\n```\n\nWithout the second semicolon patch I get hangs for some of the above tests.\n\nThis is on sage.math where the ring.pyx issue never hit me.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-04T05:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [3098-semicolon.patch](tarball://root/attachments/some-uuid/ticket3098/3098-semicolon.patch) by mabshoff created at 2008-05-04 05:32:46

With both patches applied I get four doctest failures:

```
sage -t -long devel/sage/sage/schemes/generic/algebraic_scheme.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/algebraic_scheme.py", line 374:
    sage: loads(S.dumps()) == S
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_10
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_algebraic_scheme.py
         [3.8 s]
exit code: 1024
```
And:

```
sage -t -long devel/sage/sage/rings/polynomial/polynomial_singular_interface.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/polynomial_singular_interface.py", line 330:
    sage: R(h^20) == f^20
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[11]>", line 1, in <module>
        R(h**Integer(20)) == f**Integer(20)###line 330:
    sage: R(h^20) == f^20
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 1056, in __call__
        raise TypeError, "Unable to coerce singular object"
    TypeError: Unable to coerce singular object
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_polynomial_singular_interface.py
         [3.4 s]
exit code: 1024
```
And:

```
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/multi_polynomial_ideal.py", line 502:
    sage: reduce(lambda Qi,Qj: Qi.intersection(Qj), [Qi for (Qi,radQi) in pd]) == I
Expected:
    True
Got:
    False
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/multi_polynomial_ideal.py", line 1886:
    sage: J.groebner_basis()
Expected:
    [x + y + z, y^2 + y*z + z^2, z^3 - 1]
Got:
    [x + y + z, x*y + x*z + y*z, y^2 + y*z + z^2, x*y*z - 1, z^3 - 1]
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_14
   1 of   9 in __main__.example_44
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_multi_polynomial_ideal.py
         [6.1 s]
exit code: 1024
```
And:

```
sage -t -long devel/sage/sage/interfaces/singular.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/singular.py", line 238:
    sage: a = singular('2')*3; a
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[59]>", line 1, in <module>
        a = singular('2')*Integer(3); a###line 238:
    sage: a = singular('2')*3; a
      File "element.pyx", line 1374, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:8544)
      File "coerce.pyx", line 265, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5005)
      File "coerce.pyx", line 455, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c (sage/structure/coerce.c:7010)
      File "coerce.pyx", line 511, in sage.structure.coerce.CoercionModel_cache_maps.discover_action_c (sage/structure/coerce.c:7489)
      File "parent.pyx", line 213, in sage.structure.parent.Parent.get_action_c (sage/structure/parent.c:1829)
      File "parent.pyx", line 282, in sage.structure.parent.Parent.get_action_c_impl (sage/structure/parent.c:2641)
      File "parent.pyx", line 696, in sage.structure.parent._register_pair (sage/structure/parent.c:6199)
      File "parent.pyx", line 689, in sage.structure.parent.EltPair.__eq__ (sage/structure/parent.c:6049)
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:4551)
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp (sage/structure/element.c:4446)
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1257, in __cmp__
        if P.eval("%s %s %s"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 423, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? `sage60` is not defined
       ? error occurred in STDIN line 52: `sage60 < sage60;`
**********************************************************************
1 items had failures:
   1 of  61 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_singular.pyException exceptions.RuntimeError: RuntimeError('Singular error:\n   ? `sage60` is not defined\n   ? error occurred in STDIN line 36: `sage60 < sage60;`',) in 'sage.structure.parent._unregister_pair' ignored
Exception exceptions.RuntimeError: RuntimeError('Singular error:\n   ? `sage60` is not defined\n   ? error occurred in STDIN line 38: `sage60 < sage60;`',) in 'sage.structure.parent._unregister_pair' ignored

         [3.3 s]
exit code: 1024
```

Without the second semicolon patch I get hangs for some of the above tests.

This is on sage.math where the ring.pyx issue never hit me.

Cheers,

Michael



---

archive/issue_comments_021350.json:
```json
{
    "body": "Attachment [sage-3098-queue.patch](tarball://root/attachments/some-uuid/ticket3098/sage-3098-queue.patch) by @williamstein created at 2008-05-04 17:14:35\n\napply this *after* the other patches",
    "created_at": "2008-05-04T17:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21350",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3098-queue.patch](tarball://root/attachments/some-uuid/ticket3098/sage-3098-queue.patch) by @williamstein created at 2008-05-04 17:14:35

apply this *after* the other patches



---

archive/issue_comments_021351.json:
```json
{
    "body": "With all three patches applied:\n\n```\nAll tests passed!\nTotal time for all tests: 944.7 seconds\n```\nw00t - 3.0.1 - here we come.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-04T17:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21351",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With all three patches applied:

```
All tests passed!
Total time for all tests: 944.7 seconds
```
w00t - 3.0.1 - here we come.

Cheers,

Michael



---

archive/issue_comments_021352.json:
```json
{
    "body": "Merged in Sage 3.0.1.final. William did also test on boxen affected by the ring.pyx failure.",
    "created_at": "2008-05-04T17:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21352",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.final. William did also test on boxen affected by the ring.pyx failure.



---

archive/issue_comments_021353.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-04T17:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3098#issuecomment-21353",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006992.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-04T17:40:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3098",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3098#event-6992"
}
```
