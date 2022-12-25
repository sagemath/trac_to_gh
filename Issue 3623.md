# Issue 3623: Factory and pickling framework (part of coercion branch)

archive/issues_003623.json:
```json
{
    "body": "Assignee: @robertwb\n\nUniqueness of parents makes Sage operate much more smoothly. This leads to an enormous amount of nearly identical caching code scattered throughout the library. This factory handles all the caching for you, and also provides a good pickling mechanism. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3623\n\n",
    "created_at": "2008-07-09T08:03:41Z",
    "labels": [
        "component: coercion"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Factory and pickling framework (part of coercion branch)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3623",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

Uniqueness of parents makes Sage operate much more smoothly. This leads to an enormous amount of nearly identical caching code scattered throughout the library. This factory handles all the caching for you, and also provides a good pickling mechanism. 

Issue created by migration from https://trac.sagemath.org/ticket/3623





---

archive/issue_comments_025562.json:
```json
{
    "body": "Code documented and works great/passes tests. Just need some doctests in factory.pyx (perhaps via a fake test class?)",
    "created_at": "2008-07-09T08:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25562",
    "user": "https://github.com/robertwb"
}
```

Code documented and works great/passes tests. Just need some doctests in factory.pyx (perhaps via a fake test class?)



---

archive/issue_comments_025563.json:
```json
{
    "body": "Needs to be rebased against 3.1.2.alpha4:\n\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-2.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-2.patch?format=raw\nLoading: [....]\ncd \"/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage\" && hg status\ncd \"/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage\" && hg status\ncd \"/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage\" && hg import   \"/Users/anakha/.sage/temp/fullmetal.umn/58245/tmp_1.patch\"\napplying /Users/anakha/.sage/temp/fullmetal.umn/58245/tmp_1.patch\npatching file sage/modules/free_module.py\nHunk #1 FAILED at 157\nHunk #2 FAILED at 261\n2 out of 2 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej\nabort: patch failed to apply\n```\n\n\nOtherwise, I like this very much after having gone through the pain of implementing a unique factory for a parent already, I would have wasted a week less if this had already been in sage.",
    "created_at": "2008-09-06T15:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25563",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Needs to be rebased against 3.1.2.alpha4:


```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-2.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-2.patch?format=raw
Loading: [....]
cd "/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage" && hg status
cd "/Volumes/Place/anakha/sage-3.1.2.alpha4/devel/sage" && hg import   "/Users/anakha/.sage/temp/fullmetal.umn/58245/tmp_1.patch"
applying /Users/anakha/.sage/temp/fullmetal.umn/58245/tmp_1.patch
patching file sage/modules/free_module.py
Hunk #1 FAILED at 157
Hunk #2 FAILED at 261
2 out of 2 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
abort: patch failed to apply
```


Otherwise, I like this very much after having gone through the pain of implementing a unique factory for a parent already, I would have wasted a week less if this had already been in sage.



---

archive/issue_comments_025564.json:
```json
{
    "body": "Thanks. I'll rebase this as soon as 3.1.2 comes out (as I doubt this ticket will make it into there).",
    "created_at": "2008-09-08T16:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25564",
    "user": "https://github.com/robertwb"
}
```

Thanks. I'll rebase this as soon as 3.1.2 comes out (as I doubt this ticket will make it into there).



---

archive/issue_comments_025565.json:
```json
{
    "body": "Attachment [3623-factory-1.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-1.patch) by @robertwb created at 2008-09-23 23:11:01",
    "created_at": "2008-09-23T23:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25565",
    "user": "https://github.com/robertwb"
}
```

Attachment [3623-factory-1.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-1.patch) by @robertwb created at 2008-09-23 23:11:01



---

archive/issue_comments_025566.json:
```json
{
    "body": "Attachment [3623-factory-3.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-3.patch) by @robertwb created at 2008-09-23 23:11:26",
    "created_at": "2008-09-23T23:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25566",
    "user": "https://github.com/robertwb"
}
```

Attachment [3623-factory-3.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-3.patch) by @robertwb created at 2008-09-23 23:11:26



---

archive/issue_comments_025567.json:
```json
{
    "body": "Attachment [3623-factory-4.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-4.patch) by @robertwb created at 2008-09-23 23:12:25\n\nAll four patches rebased.",
    "created_at": "2008-09-23T23:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25567",
    "user": "https://github.com/robertwb"
}
```

Attachment [3623-factory-4.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-4.patch) by @robertwb created at 2008-09-23 23:12:25

All four patches rebased.



---

archive/issue_comments_025568.json:
```json
{
    "body": "Attachment [3623-factory-5.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-5.patch) by @robertwb created at 2008-09-24 05:29:50",
    "created_at": "2008-09-24T05:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25568",
    "user": "https://github.com/robertwb"
}
```

Attachment [3623-factory-5.patch](tarball://root/attachments/some-uuid/ticket3623/3623-factory-5.patch) by @robertwb created at 2008-09-24 05:29:50



---

archive/issue_comments_025569.json:
```json
{
    "body": "Hi Robert,\n\nThis bitrotted again.  Sorry!\n\n```\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-1.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-1.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/14985/tmp_0.patch\"\napplying /home/was/.sage/temp/sage/14985/tmp_0.patch\npatching file setup.py\nHunk #1 FAILED at 533\n1 out of 1 hunk FAILED -- saving rejects to file setup.py.rej\nabort: patch failed to apply\nsage: \n```\n\n| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |\n| Type notebook() for the GUI, and license() for information.        |\nCan you rebase it an email me asap so this can get properly refereed and *not* bitrot again.",
    "created_at": "2008-11-28T21:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25569",
    "user": "https://github.com/williamstein"
}
```

Hi Robert,

This bitrotted again.  Sorry!

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-1.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/3623/3623-factory-1.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/14985/tmp_0.patch"
applying /home/was/.sage/temp/sage/14985/tmp_0.patch
patching file setup.py
Hunk #1 FAILED at 533
1 out of 1 hunk FAILED -- saving rejects to file setup.py.rej
abort: patch failed to apply
sage: 
```

| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
Can you rebase it an email me asap so this can get properly refereed and *not* bitrot again.



---

archive/issue_comments_025570.json:
```json
{
    "body": "patches 1-5 folded and rebased onto 3.2.1",
    "created_at": "2008-12-02T12:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25570",
    "user": "https://github.com/robertwb"
}
```

patches 1-5 folded and rebased onto 3.2.1



---

archive/issue_comments_025571.json:
```json
{
    "body": "Attachment [3623-all-3.2.1.patch](tarball://root/attachments/some-uuid/ticket3623/3623-all-3.2.1.patch) by @robertwb created at 2008-12-02 12:42:03\n\nOK, this is once again rebased.",
    "created_at": "2008-12-02T12:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25571",
    "user": "https://github.com/robertwb"
}
```

Attachment [3623-all-3.2.1.patch](tarball://root/attachments/some-uuid/ticket3623/3623-all-3.2.1.patch) by @robertwb created at 2008-12-02 12:42:03

OK, this is once again rebased.



---

archive/issue_comments_025572.json:
```json
{
    "body": "The patch applies cleanly against 3.2.1 and together with #4276 I am seeing two doctest failures:\n\n```\nsage -t -long \"devel/sage/sage/structure/coerce.pyx\"        \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx\", line 862:\n    sage: V is W\nExpected:\n    False\nGot:\n    True\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx\", line 865:\n    sage: cm.coercion_maps(V, W)\nExpected:\n    (None,\n     Call morphism:\n      From: Vector space of dimension 3 over Rational Field\n      To:   Vector space of dimension 3 over Rational Field)\nGot:\n    (None, None)\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx\", line 870:\n    sage: cm.coercion_maps(W, V)\nExpected:\n    (None,\n     Call morphism:\n      From: Vector space of dimension 3 over Rational Field\n      To:   Vector space of dimension 3 over Rational Field)\nGot:\n    (None, Free module morphism defined by the matrix\n    [1 0 0]\n    [0 1 0]\n    [0 0 1]\n    Domain: Vector space of dimension 3 over Rational Field\n    Codomain: Vector space of dimension 3 over Rational Field)\n**********************************************************************\n1 items had failures:\n   3 of  21 in __main__.example_15\n***Test Failed*** 3 failures.\n```\n\nI guess the first one is worrying while the rest is mostly a printing issue.\n\nThe other failure is:\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\", line 667:\n    sage: [E.tamagawa_exponent(P) for P in K(11).support()]\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_20[7]>\", line 1, in <module>\n        [E.tamagawa_exponent(P) for P in K(Integer(11)).support()]###line 667:\n    sage: [E.tamagawa_exponent(P) for P in K(11).support()]\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py\", line 675, in tamagawa_exponent\n        return self.local_data(P, proof).tamagawa_exponent()\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py\", line 401, in local_data\n        return self._get_local_data(P,proof)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py\", line 418, in _get_local_data\n        self._local_data[P] = EllipticCurveLocalData(self, P, proof)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.py\", line 140, in __init__\n        self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.py\", line 528, in _tate\n        r = -pinv(12*c4) * (c6 + b2 * c4)\n      File \"element.pyx\", line 1074, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:8580)\n      File \"coerce.pyx\", line 697, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5808)\n    TypeError: unsupported operand parent(s) for '*': 'Maximal Order in Number Field in a with defining polynomial x^2 + 11' and 'Number Field in a with defining polynomial x^2 + 11'\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T15:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25572",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch applies cleanly against 3.2.1 and together with #4276 I am seeing two doctest failures:

```
sage -t -long "devel/sage/sage/structure/coerce.pyx"        
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx", line 862:
    sage: V is W
Expected:
    False
Got:
    True
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx", line 865:
    sage: cm.coercion_maps(V, W)
Expected:
    (None,
     Call morphism:
      From: Vector space of dimension 3 over Rational Field
      To:   Vector space of dimension 3 over Rational Field)
Got:
    (None, None)
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/structure/coerce.pyx", line 870:
    sage: cm.coercion_maps(W, V)
Expected:
    (None,
     Call morphism:
      From: Vector space of dimension 3 over Rational Field
      To:   Vector space of dimension 3 over Rational Field)
Got:
    (None, Free module morphism defined by the matrix
    [1 0 0]
    [0 1 0]
    [0 0 1]
    Domain: Vector space of dimension 3 over Rational Field
    Codomain: Vector space of dimension 3 over Rational Field)
**********************************************************************
1 items had failures:
   3 of  21 in __main__.example_15
***Test Failed*** 3 failures.
```

I guess the first one is worrying while the rest is mostly a printing issue.

The other failure is:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_number_field.py", line 667:
    sage: [E.tamagawa_exponent(P) for P in K(11).support()]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[7]>", line 1, in <module>
        [E.tamagawa_exponent(P) for P in K(Integer(11)).support()]###line 667:
    sage: [E.tamagawa_exponent(P) for P in K(11).support()]
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 675, in tamagawa_exponent
        return self.local_data(P, proof).tamagawa_exponent()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 401, in local_data
        return self._get_local_data(P,proof)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 418, in _get_local_data
        self._local_data[P] = EllipticCurveLocalData(self, P, proof)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.py", line 140, in __init__
        self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.py", line 528, in _tate
        r = -pinv(12*c4) * (c6 + b2 * c4)
      File "element.pyx", line 1074, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:8580)
      File "coerce.pyx", line 697, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5808)
    TypeError: unsupported operand parent(s) for '*': 'Maximal Order in Number Field in a with defining polynomial x^2 + 11' and 'Number Field in a with defining polynomial x^2 + 11'
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_025573.json:
```json
{
    "body": "Attachment [3623-fix.patch](tarball://root/attachments/some-uuid/ticket3623/3623-fix.patch) by @robertwb created at 2008-12-02 20:18:39\n\napply after 3623-3.2.1-all.patch",
    "created_at": "2008-12-02T20:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25573",
    "user": "https://github.com/robertwb"
}
```

Attachment [3623-fix.patch](tarball://root/attachments/some-uuid/ticket3623/3623-fix.patch) by @robertwb created at 2008-12-02 20:18:39

apply after 3623-3.2.1-all.patch



---

archive/issue_comments_025574.json:
```json
{
    "body": "OK, I fixed the doctests in coerce.pyx. The issue was that loads(dumps(V)) wasn't returning a new object anymore (this is *good*) so it wasn't testing what I wanted to test (equal but not identical parents). \n\nThe other one is almost certainly due to #4276, looking into that now.",
    "created_at": "2008-12-02T20:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25574",
    "user": "https://github.com/robertwb"
}
```

OK, I fixed the doctests in coerce.pyx. The issue was that loads(dumps(V)) wasn't returning a new object anymore (this is *good*) so it wasn't testing what I wanted to test (equal but not identical parents). 

The other one is almost certainly due to #4276, looking into that now.



---

archive/issue_comments_025575.json:
```json
{
    "body": "3623-fix.patch does indeed fix the problem and seem to not have any side effects, i.e. the doctest failure in ell_number_field.py is still there. No additional doctests did fail.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-02T21:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25575",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

3623-fix.patch does indeed fix the problem and seem to not have any side effects, i.e. the doctest failure in ell_number_field.py is still there. No additional doctests did fail.

Cheers,

Michael



---

archive/issue_comments_025576.json:
```json
{
    "body": "Ok, since 3623-all-3.2.1.patch and 3623-fix.patch + the two patches from #4276 make all tests pass I am giving this a positive review. There might still be issues here, so if anyone does take a closer look please open another ticket. The cost of this bitrotting is too high, so if this blows up there is only me and not Robert to blame.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T11:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25576",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, since 3623-all-3.2.1.patch and 3623-fix.patch + the two patches from #4276 make all tests pass I am giving this a positive review. There might still be issues here, so if anyone does take a closer look please open another ticket. The cost of this bitrotting is too high, so if this blows up there is only me and not Robert to blame.

Cheers,

Michael



---

archive/issue_comments_025577.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha0",
    "created_at": "2008-12-04T11:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25577",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha0



---

archive/issue_comments_025578.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-04T11:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25578",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008314.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-04T11:57:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3623#event-8314"
}
```



---

archive/issue_comments_025579.json:
```json
{
    "body": "One last remark: A couple doctests for the various \"create_key\" methods would be nice, but that can be done via a new ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T12:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25579",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One last remark: A couple doctests for the various "create_key" methods would be nice, but that can be done via a new ticket.

Cheers,

Michael



---

archive/issue_comments_025580.json:
```json
{
    "body": "Thanks you. This one is a real pain to rebase, and I've wanted to use it elsewhere too. \n\nNote that Mike Hansen did look at these during Sage Days 10, and the response was generally positive (though not formal).",
    "created_at": "2008-12-04T20:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3623#issuecomment-25580",
    "user": "https://github.com/robertwb"
}
```

Thanks you. This one is a real pain to rebase, and I've wanted to use it elsewhere too. 

Note that Mike Hansen did look at these during Sage Days 10, and the response was generally positive (though not formal).
