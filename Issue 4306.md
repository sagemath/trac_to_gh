# Issue 4306: bug in supersingular module

archive/issues_004306.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @loefflerd\n\n\n```\nsage: X = SupersingularModule(389)\nsage: X\nModule of supersingular points on X_0(1)/F_389 over Integer Ring\nsage: X.basis()\nTraceback (most recent call last):\n...\nAttributeError: 'SupersingularModule' object has no attribute 'free_module'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4306\n\n",
    "created_at": "2008-10-16T09:17:19Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "bug in supersingular module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4306",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro

CC:  @loefflerd


```
sage: X = SupersingularModule(389)
sage: X
Module of supersingular points on X_0(1)/F_389 over Integer Ring
sage: X.basis()
Traceback (most recent call last):
...
AttributeError: 'SupersingularModule' object has no attribute 'free_module'
```


Issue created by migration from https://trac.sagemath.org/ticket/4306





---

archive/issue_comments_031450.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T13:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31450",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_031451.json:
```json
{
    "body": "The attached patch doesn't implement elements of supersingular modules -- that isn't implemented yet at all!  But it implements a free_module() method so that now the above input results in a NotImplementedError, which is the right behavior when something isn't implemented.",
    "created_at": "2010-01-19T13:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31451",
    "user": "https://github.com/williamstein"
}
```

The attached patch doesn't implement elements of supersingular modules -- that isn't implemented yet at all!  But it implements a free_module() method so that now the above input results in a NotImplementedError, which is the right behavior when something isn't implemented.



---

archive/issue_comments_031452.json:
```json
{
    "body": "Attachment [trac_4306.patch](tarball://root/attachments/some-uuid/ticket4306/trac_4306.patch) by @williamstein created at 2010-01-19 13:09:23",
    "created_at": "2010-01-19T13:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31452",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4306.patch](tarball://root/attachments/some-uuid/ticket4306/trac_4306.patch) by @williamstein created at 2010-01-19 13:09:23



---

archive/issue_comments_031453.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-23T02:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31453",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_031454.json:
```json
{
    "body": "With the patch applied, I'm getting\n\n\n```\nsage -t -long \"modular/ssmod/ssmod.py\"                      \n**********************************************************************\nFile \"/opt/sage-4.3.1/devel/sage-main/sage/modular/ssmod/ssmod.py\", line 38:\n    sage: t = X.T(2).matrix()            # long time (but still less than a minute!)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/ghitza/sage-devel/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/ghitza/sage-devel/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/ghitza/sage-devel/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[9]>\", line 1, in <module>\n        t = X.T(Integer(2)).matrix()            # long time (but still less than a minute!)###line 38:\n    sage: t = X.T(2).matrix()            # long time (but still less than a minute!)\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py\", line 1343, in T\n        return self.hecke_operator(n)\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py\", line 1330, in hecke_operator\n        return self.hecke_algebra().hecke_operator(n)\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py\", line 325, in hecke_algebra\n        self.__hecke_algebra = algebra.HeckeAlgebra(self)\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/algebra.py\", line 136, in HeckeAlgebra\n        k = (M, M.basis_matrix())\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py\", line 828, in basis_matrix\n        return self.free_module().basis_matrix()\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modules/free_module.py\", line 2087, in basis_matrix\n        A = MAT.identity_matrix()\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py\", line 944, in identity_matrix\n        A = self(0)\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py\", line 395, in __call__\n        return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)\n      File \"/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py\", line 1087, in matrix\n        return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)\n      File \"matrix_rational_dense.pyx\", line 149, in sage.matrix.matrix_rational_dense.Matrix_rational_dense.__cinit__ (sage/matrix/matrix_rational_dense.c:4931)\n    MemoryError: out of memory allocating a matrix\n**********************************************************************\nFile \"/opt/sage-4.3.1/devel/sage-main/sage/modular/ssmod/ssmod.py\", line 39:\n    sage: t.nrows()                      # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/ghitza/sage-devel/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/ghitza/sage-devel/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/ghitza/sage-devel/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[10]>\", line 1, in <module>\n        t.nrows()                      # long time###line 39:\n    sage: t.nrows()                      # long time\n    NameError: name 't' is not defined\n**********************************************************************\n1 items had failures:\n   2 of  18 in __main__.example_0\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_ssmod.py\n\t [21.4 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"modular/ssmod/ssmod.py\"\nTotal time for all tests: 21.4 seconds\n```\n",
    "created_at": "2010-01-23T02:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31454",
    "user": "https://github.com/aghitza"
}
```

With the patch applied, I'm getting


```
sage -t -long "modular/ssmod/ssmod.py"                      
**********************************************************************
File "/opt/sage-4.3.1/devel/sage-main/sage/modular/ssmod/ssmod.py", line 38:
    sage: t = X.T(2).matrix()            # long time (but still less than a minute!)
Exception raised:
    Traceback (most recent call last):
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        t = X.T(Integer(2)).matrix()            # long time (but still less than a minute!)###line 38:
    sage: t = X.T(2).matrix()            # long time (but still less than a minute!)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 1343, in T
        return self.hecke_operator(n)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 1330, in hecke_operator
        return self.hecke_algebra().hecke_operator(n)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 325, in hecke_algebra
        self.__hecke_algebra = algebra.HeckeAlgebra(self)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/algebra.py", line 136, in HeckeAlgebra
        k = (M, M.basis_matrix())
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modular/hecke/module.py", line 828, in basis_matrix
        return self.free_module().basis_matrix()
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/modules/free_module.py", line 2087, in basis_matrix
        A = MAT.identity_matrix()
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py", line 944, in identity_matrix
        A = self(0)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py", line 395, in __call__
        return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
      File "/home/ghitza/sage-devel/local/lib/python/site-packages/sage/matrix/matrix_space.py", line 1087, in matrix
        return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce)
      File "matrix_rational_dense.pyx", line 149, in sage.matrix.matrix_rational_dense.Matrix_rational_dense.__cinit__ (sage/matrix/matrix_rational_dense.c:4931)
    MemoryError: out of memory allocating a matrix
**********************************************************************
File "/opt/sage-4.3.1/devel/sage-main/sage/modular/ssmod/ssmod.py", line 39:
    sage: t.nrows()                      # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/ghitza/sage-devel/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1, in <module>
        t.nrows()                      # long time###line 39:
    sage: t.nrows()                      # long time
    NameError: name 't' is not defined
**********************************************************************
1 items had failures:
   2 of  18 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/ghitza/.sage//tmp/.doctest_ssmod.py
	 [21.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "modular/ssmod/ssmod.py"
Total time for all tests: 21.4 seconds
```




---

archive/issue_comments_031455.json:
```json
{
    "body": "OK, it seems like the underlying issue in the last comment has disappeared.  With sage-5.10:\n\n\n```\nsage: X = SupersingularModule(389)\nsage: X.basis()                   \n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n<ipython-input-2-30f7d3cb5e51> in <module>()\n----> 1 X.basis()\n\n/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/modular/hecke/module.pyc in basis(self)\n    865             return self.__basis\n    866         except AttributeError:\n--> 867             self.__basis = self.gens()\n    868         return self.__basis\n    869 \n\n/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:3292)()\n\n/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/modular/hecke/module.pyc in gen(self, n)\n   1342             (1,17)\n   1343         \"\"\"\n-> 1344         return self(self.free_module().gen(n))\n   1345 \n   1346     def hecke_matrix(self, n):\n\n/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7916)()\n\nNotImplementedError: \n```\n\n\nI am adding a reviewer patch that doctests this.",
    "created_at": "2013-07-22T17:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31455",
    "user": "https://github.com/aghitza"
}
```

OK, it seems like the underlying issue in the last comment has disappeared.  With sage-5.10:


```
sage: X = SupersingularModule(389)
sage: X.basis()                   
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-2-30f7d3cb5e51> in <module>()
----> 1 X.basis()

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/modular/hecke/module.pyc in basis(self)
    865             return self.__basis
    866         except AttributeError:
--> 867             self.__basis = self.gens()
    868         return self.__basis
    869 

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:3292)()

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/modular/hecke/module.pyc in gen(self, n)
   1342             (1,17)
   1343         """
-> 1344         return self(self.free_module().gen(n))
   1345 
   1346     def hecke_matrix(self, n):

/opt/ghitza/sage/local/lib/python2.7/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7916)()

NotImplementedError: 
```


I am adding a reviewer patch that doctests this.



---

archive/issue_comments_031456.json:
```json
{
    "body": "Attachment [trac_4306-doctest.patch](tarball://root/attachments/some-uuid/ticket4306/trac_4306-doctest.patch) by @aghitza created at 2013-07-22 17:26:58",
    "created_at": "2013-07-22T17:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31456",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_4306-doctest.patch](tarball://root/attachments/some-uuid/ticket4306/trac_4306-doctest.patch) by @aghitza created at 2013-07-22 17:26:58



---

archive/issue_comments_031457.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-22T17:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31457",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_031458.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd51, beginner\".",
    "created_at": "2013-07-22T17:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31458",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "sd51, beginner".



---

archive/issue_comments_031459.json:
```json
{
    "body": "Alex's patch with a better commit message",
    "created_at": "2013-07-25T11:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31459",
    "user": "https://github.com/loefflerd"
}
```

Alex's patch with a better commit message



---

archive/issue_comments_031460.json:
```json
{
    "body": "Attachment [trac_4306-doctest.2.patch](tarball://root/attachments/some-uuid/ticket4306/trac_4306-doctest.2.patch) by @loefflerd created at 2013-07-25 11:08:38\n\nI edited Alex's patch to add a better commit message. Other than that I think this is fine.",
    "created_at": "2013-07-25T11:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31460",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_4306-doctest.2.patch](tarball://root/attachments/some-uuid/ticket4306/trac_4306-doctest.2.patch) by @loefflerd created at 2013-07-25 11:08:38

I edited Alex's patch to add a better commit message. Other than that I think this is fine.



---

archive/issue_comments_031461.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-07-25T11:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31461",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009722.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-07-25T17:31:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4306#event-9722"
}
```



---

archive/issue_comments_031462.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-19T06:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4306#issuecomment-31462",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009723.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-19T06:45:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4306",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4306#event-9723"
}
```
