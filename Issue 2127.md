# Issue 2127: Mod n determinant and LinBox/FFPACK

archive/issues_002127.json:
```json
{
    "body": "Assignee: cpernet\n\nImprove efficiency of the dense mod n determinant by wrapping directly the LinBox/FFPACK Det.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2127\n\n",
    "created_at": "2008-02-09T14:43:02Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "Mod n determinant and LinBox/FFPACK",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2127",
    "user": "cpernet"
}
```
Assignee: cpernet

Improve efficiency of the dense mod n determinant by wrapping directly the LinBox/FFPACK Det.

Issue created by migration from https://trac.sagemath.org/ticket/2127





---

archive/issue_comments_013946.json:
```json
{
    "body": "Adds a wrapper to LinBox/FFPACK Det, for dense modular matrices",
    "created_at": "2008-02-09T14:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13946",
    "user": "cpernet"
}
```

Adds a wrapper to LinBox/FFPACK Det, for dense modular matrices



---

archive/issue_comments_013947.json:
```json
{
    "body": "Attachment\n\nChange the wrapper for linbox rank and det to use Modular<double> (fixes a bug) and add appropriate delete.",
    "created_at": "2008-02-09T15:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13947",
    "user": "cpernet"
}
```

Attachment

Change the wrapper for linbox rank and det to use Modular<double> (fixes a bug) and add appropriate delete.



---

archive/issue_comments_013948.json:
```json
{
    "body": "The updated version of linbox spkg is available at [http://sage.math.washington.edu/home/pernet/linbox-20080209.spkg](http://sage.math.washington.edu/home/pernet/linbox-20080209.spkg)",
    "created_at": "2008-02-09T15:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13948",
    "user": "cpernet"
}
```

The updated version of linbox spkg is available at [http://sage.math.washington.edu/home/pernet/linbox-20080209.spkg](http://sage.math.washington.edu/home/pernet/linbox-20080209.spkg)



---

archive/issue_comments_013949.json:
```json
{
    "body": "The patches at #2107 and this ticket clash. It is also unclear where linbox-20080209.spkg comes from, i.e. is it an update to the latest linbox svn or just an incremental change over the last linbox.spkg, which should make it linbox-20070915.p4.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T17:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13949",
    "user": "mabshoff"
}
```

The patches at #2107 and this ticket clash. It is also unclear where linbox-20080209.spkg comes from, i.e. is it an update to the latest linbox svn or just an incremental change over the last linbox.spkg, which should make it linbox-20070915.p4.

Cheers,

Michael



---

archive/issue_comments_013950.json:
```json
{
    "body": "Fixed linbox_wrap.cpp.\nThe new linbox spkg is available at\n[http://sage.math.washington.edu/home/pernet/linbox-2007-09-15.p5.spkg](http://sage.math.washington.edu/home/pernet/linbox-2007-09-15.p5.spkg)",
    "created_at": "2008-02-16T23:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13950",
    "user": "cpernet"
}
```

Fixed linbox_wrap.cpp.
The new linbox spkg is available at
[http://sage.math.washington.edu/home/pernet/linbox-2007-09-15.p5.spkg](http://sage.math.washington.edu/home/pernet/linbox-2007-09-15.p5.spkg)



---

archive/issue_comments_013951.json:
```json
{
    "body": "Fix the wrong url of spkg\n\n[http://sage.math.washington.edu/home/pernet/linbox-20070915.p5.spkg](http://sage.math.washington.edu/home/pernet/linbox-20070915.p5.spkg)",
    "created_at": "2008-02-16T23:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13951",
    "user": "cpernet"
}
```

Fix the wrong url of spkg

[http://sage.math.washington.edu/home/pernet/linbox-20070915.p5.spkg](http://sage.math.washington.edu/home/pernet/linbox-20070915.p5.spkg)



---

archive/issue_comments_013952.json:
```json
{
    "body": "Attachment\n\nUpdated patch for rank/det wrapping of ffpack",
    "created_at": "2008-02-16T23:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13952",
    "user": "cpernet"
}
```

Attachment

Updated patch for rank/det wrapping of ffpack



---

archive/issue_comments_013953.json:
```json
{
    "body": "The updated linbox.spkg fixes the issue, but there are two problems:\n\n* it is not based on linbox-20070915.p4.spkg, but  linbox-20070915.p3.spkg, i.e. missing the Debianization infrastructure\n* there are outstanding changes not committed to the repo.\n\nI am fixing both issues ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T23:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13953",
    "user": "mabshoff"
}
```

The updated linbox.spkg fixes the issue, but there are two problems:

* it is not based on linbox-20070915.p4.spkg, but  linbox-20070915.p3.spkg, i.e. missing the Debianization infrastructure
* there are outstanding changes not committed to the repo.

I am fixing both issues ;)

Cheers,

Michael



---

archive/issue_comments_013954.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/linbox-20070915.p5.spkg\n\nresolves all the issues.",
    "created_at": "2008-02-17T00:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13954",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha1/linbox-20070915.p5.spkg

resolves all the issues.



---

archive/issue_comments_013955.json:
```json
{
    "body": "With linboxdet.1.patch applied I am seeing doctest failures like\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1$ ./sage -t devel/sage/sage/matrix/matrix_modn_dense.pyx\nsage -t  devel/sage-main/sage/matrix/matrix_modn_dense.pyx  dd = 1\n**********************************************************************\nFile \"matrix_modn_dense.pyx\", line 61:\n    sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[16]>\", line 1, in <module>\n        G = MatrixGroup([M([[Integer(0),Integer(1),Integer(0)],[Integer(0),Integer(0),Integer(1)],[Integer(1),Integer(0),Integer(0)]]), M([[Integer(0),Integer(1),Integer(0)],[Integer(1),Integer(0),Integer(0)],[Integer(0),Integer(0),Integer(1)]])])###line 61:\n    sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py\", line 146, in MatrixGroup\n        return MatrixGroup_gens_finite_field(gens)\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py\", line 586, in __init__\n        if not x.is_invertible():\n      File \"matrix0.pyx\", line 1414, in sage.matrix.matrix0.Matrix.is_invertible\n        return self.is_square() and self.determinant().is_unit()\n    AttributeError: 'long' object has no attribute 'is_unit'\n**********************************************************************\nFile \"matrix_modn_dense.pyx\", line 62:\n    sage: G\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[17]>\", line 1, in <module>\n        G###line 62:\n    sage: G\n    NameError: name 'G' is not defined\n**********************************************************************\nFile \"matrix_modn_dense.pyx\", line 65:\n    sage: gap(G)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[18]>\", line 1, in <module>\n        gap(G)###line 65:\n    sage: gap(G)\n    NameError: name 'G' is not defined\n**********************************************************************\nFile \"matrix_modn_dense.pyx\", line 901:\n    sage: m.det()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_14[0]>\", line 1, in <module>\n        m.det()###line 901:\n    sage: m.det()\n    NameError: name 'm' is not defined\n**********************************************************************\n2 items had failures:\n   3 of  24 in __main__.example_0\n   1 of   3 in __main__.example_14\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file .doctest_matrix_modn_dense.pyx\n         [2.2 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n```\n\nErgo: negative review for now until those issues are sorted out.\n\nFYI: My linbox.spkg from #2107 has been merged. The patch linboxdet.3.patch is a non-unified diff, so next to useless :(\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T01:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13955",
    "user": "mabshoff"
}
```

With linboxdet.1.patch applied I am seeing doctest failures like

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1$ ./sage -t devel/sage/sage/matrix/matrix_modn_dense.pyx
sage -t  devel/sage-main/sage/matrix/matrix_modn_dense.pyx  dd = 1
**********************************************************************
File "matrix_modn_dense.pyx", line 61:
    sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[16]>", line 1, in <module>
        G = MatrixGroup([M([[Integer(0),Integer(1),Integer(0)],[Integer(0),Integer(0),Integer(1)],[Integer(1),Integer(0),Integer(0)]]), M([[Integer(0),Integer(1),Integer(0)],[Integer(1),Integer(0),Integer(0)],[Integer(0),Integer(0),Integer(1)]])])###line 61:
    sage: G = MatrixGroup([M([[0,1,0],[0,0,1],[1,0,0]]), M([[0,1,0],[1,0,0],[0,0,1]])])
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 146, in MatrixGroup
        return MatrixGroup_gens_finite_field(gens)
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 586, in __init__
        if not x.is_invertible():
      File "matrix0.pyx", line 1414, in sage.matrix.matrix0.Matrix.is_invertible
        return self.is_square() and self.determinant().is_unit()
    AttributeError: 'long' object has no attribute 'is_unit'
**********************************************************************
File "matrix_modn_dense.pyx", line 62:
    sage: G
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        G###line 62:
    sage: G
    NameError: name 'G' is not defined
**********************************************************************
File "matrix_modn_dense.pyx", line 65:
    sage: gap(G)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        gap(G)###line 65:
    sage: gap(G)
    NameError: name 'G' is not defined
**********************************************************************
File "matrix_modn_dense.pyx", line 901:
    sage: m.det()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[0]>", line 1, in <module>
        m.det()###line 901:
    sage: m.det()
    NameError: name 'm' is not defined
**********************************************************************
2 items had failures:
   3 of  24 in __main__.example_0
   1 of   3 in __main__.example_14
***Test Failed*** 4 failures.
For whitespace errors, see the file .doctest_matrix_modn_dense.pyx
         [2.2 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:
```

Ergo: negative review for now until those issues are sorted out.

FYI: My linbox.spkg from #2107 has been merged. The patch linboxdet.3.patch is a non-unified diff, so next to useless :(

Cheers,

Michael



---

archive/issue_comments_013956.json:
```json
{
    "body": "Fix the doctest failure due to linboxdet.1.patch",
    "created_at": "2008-02-17T01:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13956",
    "user": "cpernet"
}
```

Fix the doctest failure due to linboxdet.1.patch



---

archive/issue_comments_013957.json:
```json
{
    "body": "Attachment\n\nfix the last doctest failure with det over nonprime modular rings.",
    "created_at": "2008-02-17T02:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13957",
    "user": "cpernet"
}
```

Attachment

fix the last doctest failure with det over nonprime modular rings.



---

archive/issue_comments_013958.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-17T02:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13958",
    "user": "cpernet"
}
```

Attachment



---

archive/issue_comments_013959.json:
```json
{
    "body": "Please just apply /home/was/patches/hnf.hg, which includes this plus a little followup to better integrate the functionality into sage.",
    "created_at": "2008-02-17T05:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13959",
    "user": "was"
}
```

Please just apply /home/was/patches/hnf.hg, which includes this plus a little followup to better integrate the functionality into sage.



---

archive/issue_comments_013960.json:
```json
{
    "body": "Merged William's hnf.hg in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T11:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13960",
    "user": "mabshoff"
}
```

Merged William's hnf.hg in Sage 2.10.2.alpha1



---

archive/issue_comments_013961.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T11:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2127#issuecomment-13961",
    "user": "mabshoff"
}
```

Resolution: fixed
