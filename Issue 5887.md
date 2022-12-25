# Issue 5887: [with patch; positive review] major bugs in morphisms of R-modules

archive/issues_005887.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe image method on homomorphisms of R-modules is completely wrong.  Here is a simple example that illustrates this serious bug.  I start with V, which is a submodule of index 2 in `ZZ^2`, and define the identity map from V to V.  The image is `ZZ^2`, which is totally wrong.  I think the problem is that the image is being computed over the fraction field. \n\n```\nsage: V = (ZZ^2).span([[1,2],[3,4]])\nsage: phi = V.Hom(V)(identity_matrix(ZZ,2))\nsage: phi(V.0) == V.0\nTrue\nsage: phi(V.1) == V.1\nTrue\nsage: phi.image()\nFree module of degree 2 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1 0]\n[0 1]\nsage: phi.image() == V\nFalse\n```\n\nIn fact, the image isn't even contained in the codomain!\n\n```\nsage: phi.image() == phi.codomain()\nFalse\nsage: phi.image().is_submodule( phi.codomain() )\nFalse\n```\n\nAlso, the restrict_domain() function is broken:\n\n```\nsage: V = ZZ^2; phi = V.hom([3*V.0, 2*V.1])\nsage: phi.restrict_domain(V.span([V.0]))\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/teragon.local/5779/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.pyc in restrict_domain(self, sub)\n    383         D  = self.domain()\n    384         B  = sub.basis()\n--> 385         ims= sum([(self(D(b)).coordinate_vector()).list() for b in B],[])\n    386         \n    387         MS = matrix.MatrixSpace(self.base_ring(), len(B), self.codomain().rank())\n\nAttributeError: 'sage.modules.vector_integer_dense.Vector_integer_d' object has no attribute 'coordinate_vector'\n```\n\nDEPENDENCIES: This patch depends on #5886.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5887\n\n",
    "closed_at": "2009-05-04T16:13:24Z",
    "created_at": "2009-04-24T05:01:35Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch; positive review] major bugs in morphisms of R-modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5887",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The image method on homomorphisms of R-modules is completely wrong.  Here is a simple example that illustrates this serious bug.  I start with V, which is a submodule of index 2 in `ZZ^2`, and define the identity map from V to V.  The image is `ZZ^2`, which is totally wrong.  I think the problem is that the image is being computed over the fraction field. 

```
sage: V = (ZZ^2).span([[1,2],[3,4]])
sage: phi = V.Hom(V)(identity_matrix(ZZ,2))
sage: phi(V.0) == V.0
True
sage: phi(V.1) == V.1
True
sage: phi.image()
Free module of degree 2 and rank 2 over Integer Ring
Echelon basis matrix:
[1 0]
[0 1]
sage: phi.image() == V
False
```

In fact, the image isn't even contained in the codomain!

```
sage: phi.image() == phi.codomain()
False
sage: phi.image().is_submodule( phi.codomain() )
False
```

Also, the restrict_domain() function is broken:

```
sage: V = ZZ^2; phi = V.hom([3*V.0, 2*V.1])
sage: phi.restrict_domain(V.span([V.0]))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/5779/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.pyc in restrict_domain(self, sub)
    383         D  = self.domain()
    384         B  = sub.basis()
--> 385         ims= sum([(self(D(b)).coordinate_vector()).list() for b in B],[])
    386         
    387         MS = matrix.MatrixSpace(self.base_ring(), len(B), self.codomain().rank())

AttributeError: 'sage.modules.vector_integer_dense.Vector_integer_d' object has no attribute 'coordinate_vector'
```

DEPENDENCIES: This patch depends on #5886.

Issue created by migration from https://trac.sagemath.org/ticket/5887





---

archive/issue_comments_046456.json:
```json
{
    "body": "There is one doctest failure (in the whole tree), so this isn't ready for review yet:\n\n```\nwstein@sage:~/build/sage-3.4.1$ ./sage -t --long devel/sage/sage/modular/abvar/morphism.py\nsage -t --long \"devel/sage/sage/modular/abvar/morphism.py\"  \n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1/devel/sage/sage/modular/abvar/morphism.py\", line 433:\n    sage: (t2 - 1)(C)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[26]>\", line 1, in <module>\n        (t2 - Integer(1))(C)###line 433:\n    sage: (t2 - 1)(C)\n      File \"/scratch/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py\", line 337, in __sub__\n        return self.parent()(self.matrix() - other.matrix())\n    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'matrix'\n**********************************************************************\nFile \"/scratch/wstein/build/sage-3.4.1/devel/sage/sage/modular/abvar/morphism.py\", line 148:\n    sage: (t-1).cokernel()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[3]>\", line 1, in <module>\n        (t-Integer(1)).cokernel()###line 148:\n    sage: (t-1).cokernel()\n      File \"/scratch/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py\", line 337, in __sub__\n        return self.parent()(self.matrix() - other.matrix())\n    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'matrix'\n**********************************************************************\n2 items had failures:\n   1 of  31 in __main__.example_10\n   1 of   7 in __main__.example_6\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-3.4.1/tmp/.doctest_morphism.py\n\t [3.4 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t --long \"devel/sage/sage/modular/abvar/morphism.py\"\nTotal time for all tests: 3.4 seconds\n```",
    "created_at": "2009-04-24T06:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46456",
    "user": "https://github.com/williamstein"
}
```

There is one doctest failure (in the whole tree), so this isn't ready for review yet:

```
wstein@sage:~/build/sage-3.4.1$ ./sage -t --long devel/sage/sage/modular/abvar/morphism.py
sage -t --long "devel/sage/sage/modular/abvar/morphism.py"  
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1/devel/sage/sage/modular/abvar/morphism.py", line 433:
    sage: (t2 - 1)(C)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[26]>", line 1, in <module>
        (t2 - Integer(1))(C)###line 433:
    sage: (t2 - 1)(C)
      File "/scratch/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py", line 337, in __sub__
        return self.parent()(self.matrix() - other.matrix())
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'matrix'
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1/devel/sage/sage/modular/abvar/morphism.py", line 148:
    sage: (t-1).cokernel()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[3]>", line 1, in <module>
        (t-Integer(1)).cokernel()###line 148:
    sage: (t-1).cokernel()
      File "/scratch/wstein/build/sage-3.4.1/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py", line 337, in __sub__
        return self.parent()(self.matrix() - other.matrix())
    AttributeError: 'sage.rings.integer.Integer' object has no attribute 'matrix'
**********************************************************************
2 items had failures:
   1 of  31 in __main__.example_10
   1 of   7 in __main__.example_6
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1/tmp/.doctest_morphism.py
	 [3.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t --long "devel/sage/sage/modular/abvar/morphism.py"
Total time for all tests: 3.4 seconds
```



---

archive/issue_comments_046457.json:
```json
{
    "body": "Attachment [trac_5887.patch](tarball://root/attachments/some-uuid/ticket5887/trac_5887.patch) by @williamstein created at 2009-04-24 07:03:49\n\nOK, I fixed the patch.",
    "created_at": "2009-04-24T07:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46457",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5887.patch](tarball://root/attachments/some-uuid/ticket5887/trac_5887.patch) by @williamstein created at 2009-04-24 07:03:49

OK, I fixed the patch.



---

archive/issue_comments_046458.json:
```json
{
    "body": "Is this supposed to apply cleanly to sage-3.4.2.alpha0?  I can't seem to be able to do that:\n\n```\n[aghitza@cartan sage]$ hg qpush\napplying trac_5887.patch\npatching file sage/modules/matrix_morphism.py\nHunk #12 FAILED at 555\nHunk #13 FAILED at 576\n2 out of 15 hunks FAILED -- saving rejects to file sage/modules/matrix_morphism.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_5887.patch\n```",
    "created_at": "2009-04-30T09:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46458",
    "user": "https://github.com/aghitza"
}
```

Is this supposed to apply cleanly to sage-3.4.2.alpha0?  I can't seem to be able to do that:

```
[aghitza@cartan sage]$ hg qpush
applying trac_5887.patch
patching file sage/modules/matrix_morphism.py
Hunk #12 FAILED at 555
Hunk #13 FAILED at 576
2 out of 15 hunks FAILED -- saving rejects to file sage/modules/matrix_morphism.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_5887.patch
```



---

archive/issue_comments_046459.json:
```json
{
    "body": "Replying to [comment:5 AlexGhitza]:\n> Is this supposed to apply cleanly to sage-3.4.2.alpha0?  I can't seem to be able to do that:\n\n\nWell, given that #5882 also touches that file (but this ticket is a requirement) I think that the current situation is somewhat messed up. In the end I would not be surprised if this patch gets folded into the other ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-01T01:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 AlexGhitza]:
> Is this supposed to apply cleanly to sage-3.4.2.alpha0?  I can't seem to be able to do that:


Well, given that #5882 also touches that file (but this ticket is a requirement) I think that the current situation is somewhat messed up. In the end I would not be surprised if this patch gets folded into the other ticket.

Cheers,

Michael



---

archive/issue_comments_046460.json:
```json
{
    "body": "this is rebased against 3.4.2.rc0",
    "created_at": "2009-05-02T08:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46460",
    "user": "https://github.com/williamstein"
}
```

this is rebased against 3.4.2.rc0



---

archive/issue_comments_046461.json:
```json
{
    "body": "Attachment [trac_5887-rebased_3.4.2.rc0.2.patch](tarball://root/attachments/some-uuid/ticket5887/trac_5887-rebased_3.4.2.rc0.2.patch) by @williamstein created at 2009-05-02 08:43:57\n\nThis isn't being folded into #5882, and I do not view the \"current situation\" as at all messed up. There are three tickets: \n    #5886, #5887, and #5882.  \n\n#5886 is first, then #5887, then finally #5882.   \n\nI just applied #5886 and this rebased #5887 to my 3.4.2.rc0 tree on sage.math, and \"sage -t devel/sage/sage\" passes all tests.",
    "created_at": "2009-05-02T08:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46461",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5887-rebased_3.4.2.rc0.2.patch](tarball://root/attachments/some-uuid/ticket5887/trac_5887-rebased_3.4.2.rc0.2.patch) by @williamstein created at 2009-05-02 08:43:57

This isn't being folded into #5882, and I do not view the "current situation" as at all messed up. There are three tickets: 
    #5886, #5887, and #5882.  

#5886 is first, then #5887, then finally #5882.   

I just applied #5886 and this rebased #5887 to my 3.4.2.rc0 tree on sage.math, and "sage -t devel/sage/sage" passes all tests.



---

archive/issue_comments_046462.json:
```json
{
    "body": "Looks good!  I have only a few minor issues, in `matrix_morphism.py`:\n\n* In the method `__invert__()`, the second example says \"Check that a certain non-invertible morphism isn't invertible\", but the error that's thrown says \"TypeError: no conversion of this rational to integer\".  It would be nicer if the error said something like \"This morphism is not invertible\" instead.\n\n* There are a couple of typos in the docstring for `decomposition()`: on the (new) line 383, \"invariants\" should be \"invariant\", and on line 385, \"fro\" should be \"for\".\n\n* On line 511, \"Verify that trac 5887 is fixed\" looks out of place.  Did you want to put it before the previous doctest block?",
    "created_at": "2009-05-02T12:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46462",
    "user": "https://github.com/aghitza"
}
```

Looks good!  I have only a few minor issues, in `matrix_morphism.py`:

* In the method `__invert__()`, the second example says "Check that a certain non-invertible morphism isn't invertible", but the error that's thrown says "TypeError: no conversion of this rational to integer".  It would be nicer if the error said something like "This morphism is not invertible" instead.

* There are a couple of typos in the docstring for `decomposition()`: on the (new) line 383, "invariants" should be "invariant", and on line 385, "fro" should be "for".

* On line 511, "Verify that trac 5887 is fixed" looks out of place.  Did you want to put it before the previous doctest block?



---

archive/issue_comments_046463.json:
```json
{
    "body": "Attachment [trac_5887-part2-referee_comments.patch](tarball://root/attachments/some-uuid/ticket5887/trac_5887-part2-referee_comments.patch) by @williamstein created at 2009-05-02 22:56:20",
    "created_at": "2009-05-02T22:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46463",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5887-part2-referee_comments.patch](tarball://root/attachments/some-uuid/ticket5887/trac_5887-part2-referee_comments.patch) by @williamstein created at 2009-05-02 22:56:20



---

archive/issue_comments_046464.json:
```json
{
    "body": "Merged  trac_5887-rebased_3.4.2.rc0.2.patch and trac_5887-part2-referee_comments.patch in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T16:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged  trac_5887-rebased_3.4.2.rc0.2.patch and trac_5887-part2-referee_comments.patch in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_046465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T16:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5887#issuecomment-46465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013831.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-04T16:13:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5887",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5887#event-13831"
}
```
