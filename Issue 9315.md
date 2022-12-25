# Issue 9315: Basic pickling bug in finite fields

archive/issues_009315.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona\n\n\n```\n\nwstein@redhawk:~/db/modsym-2010$ sage modp.sage \ndata/000000/gamma0-aplist-mod2-000002-0008-10000.sobj\ndata/000000/gamma0-aplist-mod2-000003-0004-10000.sobj\ndata/000000/gamma0-aplist-mod2-000077-0002-10000.sobj\nTraceback (most recent call last):\n  File \"modp.py\", line 57, in <module>\n    go()\n  File \"modp.py\", line 52, in go\n    all(Integer(0),Integer(2))\n  File \"/usr/local/sage/local/lib/python2.6/site-packages/sage/parallel/decorate.py\", line 101, in g\n    return f(*args, **kwds)\n  File \"modp.py\", line 48, in all\n    modp(d + '/' + name, p)\n  File \"modp.py\", line 27, in modp\n    save(X, name)\n  File \"sage_object.pyx\", line 763, in sage.structure.sage_object.save (sage/structure/sage_object.c:7999)\n  File \"finite_field_base.pyx\", line 674, in sage.rings.finite_rings.finite_field_base.FiniteField.__reduce__ (sage/rings/finite_rings/finite_field_base.c:4937)\nTypeError: 'NoneType' object is unsubscriptable\nwstein@redhawk:~/db/modsym-2010$ \n```\n\n\nMore details to come!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9315\n\n",
    "created_at": "2010-06-22T18:58:02Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Basic pickling bug in finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9315",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  @JohnCremona


```

wstein@redhawk:~/db/modsym-2010$ sage modp.sage 
data/000000/gamma0-aplist-mod2-000002-0008-10000.sobj
data/000000/gamma0-aplist-mod2-000003-0004-10000.sobj
data/000000/gamma0-aplist-mod2-000077-0002-10000.sobj
Traceback (most recent call last):
  File "modp.py", line 57, in <module>
    go()
  File "modp.py", line 52, in go
    all(Integer(0),Integer(2))
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/parallel/decorate.py", line 101, in g
    return f(*args, **kwds)
  File "modp.py", line 48, in all
    modp(d + '/' + name, p)
  File "modp.py", line 27, in modp
    save(X, name)
  File "sage_object.pyx", line 763, in sage.structure.sage_object.save (sage/structure/sage_object.c:7999)
  File "finite_field_base.pyx", line 674, in sage.rings.finite_rings.finite_field_base.FiniteField.__reduce__ (sage/rings/finite_rings/finite_field_base.c:4937)
TypeError: 'NoneType' object is unsubscriptable
wstein@redhawk:~/db/modsym-2010$ 
```


More details to come!

Issue created by migration from https://trac.sagemath.org/ticket/9315





---

archive/issue_comments_087626.json:
```json
{
    "body": "There is a function in finite_field_base.pyx that tries to pickle.  It has doctests but clearly can *never* actually work if run, i.e., it is never actually tested.  Here's the function:\n\n```\n\n    def __reduce__(self):\n        \"\"\"\n        Used in pickling.\n\n        EXAMPLES::\n\n            sage: A = FiniteField(127)\n            sage: A == loads(dumps(A)) # indirect doctest\n            True\n            sage: B = FiniteField(3^3,'b')\n            sage: B == loads(dumps(B))\n            True\n            sage: C = FiniteField(2^16,'c')\n            sage: C == loads(dumps(C))\n            True\n            sage: D = FiniteField(3^20,'d')\n            sage: D == loads(dumps(D))\n            True\n        \"\"\"\n        return self._factory_data[0].reduce_data(self)\n```\n\n\nHowever, _factory_data is not defined anywhere else in the source code:\n\n```\nwstein@redhawk:~/build/sage-4.4.4.alpha1/devel/sage/sage/rings/finite_rings$ grep _factory_data *.pyx *.pxd\n *.py                                                                                                      \nfinite_field_base.pyx:        return self._factory_data[0].reduce_data(self)\n```\n",
    "created_at": "2010-06-22T20:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87626",
    "user": "https://github.com/williamstein"
}
```

There is a function in finite_field_base.pyx that tries to pickle.  It has doctests but clearly can *never* actually work if run, i.e., it is never actually tested.  Here's the function:

```

    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: A = FiniteField(127)
            sage: A == loads(dumps(A)) # indirect doctest
            True
            sage: B = FiniteField(3^3,'b')
            sage: B == loads(dumps(B))
            True
            sage: C = FiniteField(2^16,'c')
            sage: C == loads(dumps(C))
            True
            sage: D = FiniteField(3^20,'d')
            sage: D == loads(dumps(D))
            True
        """
        return self._factory_data[0].reduce_data(self)
```


However, _factory_data is not defined anywhere else in the source code:

```
wstein@redhawk:~/build/sage-4.4.4.alpha1/devel/sage/sage/rings/finite_rings$ grep _factory_data *.pyx *.pxd
 *.py                                                                                                      
finite_field_base.pyx:        return self._factory_data[0].reduce_data(self)
```




---

archive/issue_comments_087627.json:
```json
{
    "body": "Attachment [trac_9315.patch](tarball://root/attachments/some-uuid/ticket9315/trac_9315.patch) by @williamstein created at 2010-06-23 03:04:46",
    "created_at": "2010-06-23T03:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87627",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9315.patch](tarball://root/attachments/some-uuid/ticket9315/trac_9315.patch) by @williamstein created at 2010-06-23 03:04:46



---

archive/issue_comments_087628.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-23T03:04:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87628",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087629.json:
```json
{
    "body": "I get this doctest failure (and no more in finite_rings):\n\n\n```\nsage -t  \"sage/rings/finite_rings/element_ntl_gf2e.pyx\"     \n**********************************************************************\nFile \"/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx\", line 1092:\n    sage: f = loads(dumps(e))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_40[4]>\", line 1, in <module>\n        f = loads(dumps(e))###line 1092:\n    sage: f = loads(dumps(e))\n      File \"sage_object.pyx\", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)\n      File \"element_ntl_gf2e.pyx\", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)\n    TypeError: __cinit__() takes at least 1 positional argument (0 given)\n**********************************************************************\nFile \"/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx\", line 1093:\n    sage: e is f\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_40[5]>\", line 1, in <module>\n        e is f###line 1093:\n    sage: e is f\n    NameError: name 'f' is not defined\n**********************************************************************\nFile \"/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx\", line 1095:\n    sage: e == f\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_40[6]>\", line 1, in <module>\n        e == f###line 1095:\n    sage: e == f\n    NameError: name 'f' is not defined\n**********************************************************************\nFile \"/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx\", line 1449:\n    sage: loads(dumps(a)) == a\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_55[3]>\", line 1, in <module>\n        loads(dumps(a)) == a###line 1449:\n    sage: loads(dumps(a)) == a\n      File \"sage_object.pyx\", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)\n      File \"element_ntl_gf2e.pyx\", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)\n    TypeError: __cinit__() takes at least 1 positional argument (0 given)\n**********************************************************************\nFile \"/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx\", line 1499:\n    sage: f = loads(dumps(e)) # indirect doctest\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_57[4]>\", line 1, in <module>\n        f = loads(dumps(e)) # indirect doctest###line 1499:\n    sage: f = loads(dumps(e)) # indirect doctest\n      File \"sage_object.pyx\", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)\n      File \"element_ntl_gf2e.pyx\", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)\n    TypeError: __cinit__() takes at least 1 positional argument (0 given)\n**********************************************************************\nFile \"/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx\", line 1500:\n    sage: e == f\nException raised:\n    Traceback (most recent call last):\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/john/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_57[5]>\", line 1, in <module>\n        e == f###line 1500:\n    sage: e == f\n    NameError: name 'f' is not defined\n**********************************************************************\n3 items had failures:\n   3 of   8 in __main__.example_40\n   1 of   4 in __main__.example_55\n   2 of   6 in __main__.example_57\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/john/.sage//tmp/.doctest_element_ntl_gf2e.py\n\t [2.6 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"sage/rings/finite_rings/element_ntl_gf2e.pyx\"\nTotal time for all tests: 2.6 seconds\n```\n",
    "created_at": "2010-07-07T12:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87629",
    "user": "https://github.com/JohnCremona"
}
```

I get this doctest failure (and no more in finite_rings):


```
sage -t  "sage/rings/finite_rings/element_ntl_gf2e.pyx"     
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1092:
    sage: f = loads(dumps(e))
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[4]>", line 1, in <module>
        f = loads(dumps(e))###line 1092:
    sage: f = loads(dumps(e))
      File "sage_object.pyx", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)
      File "element_ntl_gf2e.pyx", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)
    TypeError: __cinit__() takes at least 1 positional argument (0 given)
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1093:
    sage: e is f
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[5]>", line 1, in <module>
        e is f###line 1093:
    sage: e is f
    NameError: name 'f' is not defined
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1095:
    sage: e == f
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[6]>", line 1, in <module>
        e == f###line 1095:
    sage: e == f
    NameError: name 'f' is not defined
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1449:
    sage: loads(dumps(a)) == a
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_55[3]>", line 1, in <module>
        loads(dumps(a)) == a###line 1449:
    sage: loads(dumps(a)) == a
      File "sage_object.pyx", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)
      File "element_ntl_gf2e.pyx", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)
    TypeError: __cinit__() takes at least 1 positional argument (0 given)
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1499:
    sage: f = loads(dumps(e)) # indirect doctest
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_57[4]>", line 1, in <module>
        f = loads(dumps(e)) # indirect doctest###line 1499:
    sage: f = loads(dumps(e)) # indirect doctest
      File "sage_object.pyx", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)
      File "element_ntl_gf2e.pyx", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)
    TypeError: __cinit__() takes at least 1 positional argument (0 given)
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1500:
    sage: e == f
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_57[5]>", line 1, in <module>
        e == f###line 1500:
    sage: e == f
    NameError: name 'f' is not defined
**********************************************************************
3 items had failures:
   3 of   8 in __main__.example_40
   1 of   4 in __main__.example_55
   2 of   6 in __main__.example_57
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/john/.sage//tmp/.doctest_element_ntl_gf2e.py
	 [2.6 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "sage/rings/finite_rings/element_ntl_gf2e.pyx"
Total time for all tests: 2.6 seconds
```




---

archive/issue_comments_087630.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-07T12:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87630",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087631.json:
```json
{
    "body": "And a similar failure in sage/rings/polynomial/multi_polynomial_libsingular.pyx",
    "created_at": "2010-07-07T12:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87631",
    "user": "https://github.com/JohnCremona"
}
```

And a similar failure in sage/rings/polynomial/multi_polynomial_libsingular.pyx



---

archive/issue_comments_087632.json:
```json
{
    "body": "Doctesting the whole the tree: http://sage.math.washington.edu/home/wstein/build/sage-4.5.alpha4/doctest-9315.out",
    "created_at": "2010-07-07T21:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87632",
    "user": "https://github.com/williamstein"
}
```

Doctesting the whole the tree: http://sage.math.washington.edu/home/wstein/build/sage-4.5.alpha4/doctest-9315.out



---

archive/issue_comments_087633.json:
```json
{
    "body": "apply only this; I updated the patch to address the issues John pointed out, and clearly document what the whole point of _factory_data is (I was confused before).",
    "created_at": "2010-08-14T02:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87633",
    "user": "https://github.com/williamstein"
}
```

apply only this; I updated the patch to address the issues John pointed out, and clearly document what the whole point of _factory_data is (I was confused before).



---

archive/issue_comments_087634.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-14T02:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87634",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087635.json:
```json
{
    "body": "Attachment [trac_9315.2.patch](tarball://root/attachments/some-uuid/ticket9315/trac_9315.2.patch) by @williamstein created at 2010-08-14 02:04:58",
    "created_at": "2010-08-14T02:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87635",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9315.2.patch](tarball://root/attachments/some-uuid/ticket9315/trac_9315.2.patch) by @williamstein created at 2010-08-14 02:04:58



---

archive/issue_comments_087636.json:
```json
{
    "body": "I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?\n\nI guess that you considered this already, and that it is harder than I am suggesting.\n\nOn with the testing, anyway!",
    "created_at": "2010-08-14T16:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87636",
    "user": "https://github.com/JohnCremona"
}
```

I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?

I guess that you considered this already, and that it is harder than I am suggesting.

On with the testing, anyway!



---

archive/issue_comments_087637.json:
```json
{
    "body": "#9409 may well be ok after this;  I will test that.",
    "created_at": "2010-08-14T16:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87637",
    "user": "https://github.com/JohnCremona"
}
```

#9409 may well be ok after this;  I will test that.



---

archive/issue_comments_087638.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?\n> \n> I guess that you considered this already, and that it is harder than I am suggesting.\n> \n\nYes, i tried for several hours to figure out how to do that and failed completely.  Obviously, if somrbody can find a way to do whatvyou propose that might be good.  But the fact is the currrent patch fixes a major bug, and nobody has suggested a better fix.\n\n> On with the testing, anyway!",
    "created_at": "2010-08-14T16:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87638",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:8 cremona]:
> I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?
> 
> I guess that you considered this already, and that it is harder than I am suggesting.
> 

Yes, i tried for several hours to figure out how to do that and failed completely.  Obviously, if somrbody can find a way to do whatvyou propose that might be good.  But the fact is the currrent patch fixes a major bug, and nobody has suggested a better fix.

> On with the testing, anyway!



---

archive/issue_comments_087639.json:
```json
{
    "body": "Replying to [comment:10 was]:\n> Replying to [comment:8 cremona]:\n> > I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?\n> > \n> > I guess that you considered this already, and that it is harder than I am suggesting.\n> > \n> \n> Yes, i tried for several hours to figure out how to do that and failed completely.  Obviously, if somrbody can find a way to do whatvyou propose that might be good.  But the fact is the currrent patch fixes a major bug, and nobody has suggested a better fix.\n> \n\nI guessed you would have tried.\n\n\n> > On with the testing, anyway!\n\nAll tests pass (sage -tp 10 -long).\n\nUnfortunately,  this does not fix #9409.  But as it is not certain that pickling of residue fields is the issue there (though I reckon it must be) I will not delay this one on that account.",
    "created_at": "2010-08-14T17:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87639",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:10 was]:
> Replying to [comment:8 cremona]:
> > I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?
> > 
> > I guess that you considered this already, and that it is harder than I am suggesting.
> > 
> 
> Yes, i tried for several hours to figure out how to do that and failed completely.  Obviously, if somrbody can find a way to do whatvyou propose that might be good.  But the fact is the currrent patch fixes a major bug, and nobody has suggested a better fix.
> 

I guessed you would have tried.


> > On with the testing, anyway!

All tests pass (sage -tp 10 -long).

Unfortunately,  this does not fix #9409.  But as it is not certain that pickling of residue fields is the issue there (though I reckon it must be) I will not delay this one on that account.



---

archive/issue_comments_087640.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-14T17:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87640",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087641.json:
```json
{
    "body": "> Unfortunately, this does not fix #9409. But as it is not certain\n>  that pickling of residue fields is the issue there (though \n> I reckon it must be) I will not delay this one on that account. \n\nBy \"pickling\" maybe you mean \"caching\"?   I didn't make any changes at all, whatsoever to caching.  The only actual change my patch makes is that the default __reduce__ method is now used when explicitly pickling residue fields.   Before pickling residue fields just resulted in a big error.   So what I do can't possibly fix any bug that wasn't very explicit before (i.e., \"pickling doesn't work at all\").",
    "created_at": "2010-08-15T17:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87641",
    "user": "https://github.com/williamstein"
}
```

> Unfortunately, this does not fix #9409. But as it is not certain
>  that pickling of residue fields is the issue there (though 
> I reckon it must be) I will not delay this one on that account. 

By "pickling" maybe you mean "caching"?   I didn't make any changes at all, whatsoever to caching.  The only actual change my patch makes is that the default __reduce__ method is now used when explicitly pickling residue fields.   Before pickling residue fields just resulted in a big error.   So what I do can't possibly fix any bug that wasn't very explicit before (i.e., "pickling doesn't work at all").



---

archive/issue_comments_087642.json:
```json
{
    "body": "Replying to [comment:12 was]:\n> > Unfortunately, this does not fix #9409. But as it is not certain\n> >  that pickling of residue fields is the issue there (though \n> > I reckon it must be) I will not delay this one on that account. \n> \n> By \"pickling\" maybe you mean \"caching\"?   I didn't make any changes at all, whatsoever to caching.  The only actual change my patch makes is that the default __reduce__ method is now used when explicitly pickling residue fields.   Before pickling residue fields just resulted in a big error.   So what I do can't possibly fix any bug that wasn't very explicit before (i.e., \"pickling doesn't work at all\").\n\nOK, I just don't know what I am talking about.... \n>",
    "created_at": "2010-08-15T19:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87642",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:12 was]:
> > Unfortunately, this does not fix #9409. But as it is not certain
> >  that pickling of residue fields is the issue there (though 
> > I reckon it must be) I will not delay this one on that account. 
> 
> By "pickling" maybe you mean "caching"?   I didn't make any changes at all, whatsoever to caching.  The only actual change my patch makes is that the default __reduce__ method is now used when explicitly pickling residue fields.   Before pickling residue fields just resulted in a big error.   So what I do can't possibly fix any bug that wasn't very explicit before (i.e., "pickling doesn't work at all").

OK, I just don't know what I am talking about.... 
>



---

archive/issue_comments_087643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9315#issuecomment-87643",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022959.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T11:13:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9315",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9315#event-22959"
}
```
