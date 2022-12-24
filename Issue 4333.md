# Issue 4333: bernoulli_python doesn't work

archive/issues_004333.json:
```json
{
    "body": "Assignee: was\n\nKeywords: bernoulli\n\nI was considering adding doctests to sage/rings/bernoulli.py and discovered that the code has probably not been used much and is broken.  For example, bernoulli_python gives different answers starting from the 28th Bernoulli number, and returns errors for some small positive integers (such as 2 and 4).  For example:\n\n\n```\nq = 28\nprint bernoulli(q, algorithm='gap')   \nprint bernoulli(q, algorithm='gp')\nprint bernoulli(q, algorithm='pari')    \nprint bernoulli(q, algorithm='python')\nprint bernoulli(q, algorithm='bernmm')\n\n-23749461029/870\n-23749461029/870\n-23749461029/870\n-818946929/30\n-23749461029/870\n```\n\n\nIt seems like it would be easiest to delete this file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4333\n\n",
    "created_at": "2008-10-21T02:18:19Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "bernoulli_python doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4333",
    "user": "mhampton"
}
```
Assignee: was

Keywords: bernoulli

I was considering adding doctests to sage/rings/bernoulli.py and discovered that the code has probably not been used much and is broken.  For example, bernoulli_python gives different answers starting from the 28th Bernoulli number, and returns errors for some small positive integers (such as 2 and 4).  For example:


```
q = 28
print bernoulli(q, algorithm='gap')   
print bernoulli(q, algorithm='gp')
print bernoulli(q, algorithm='pari')    
print bernoulli(q, algorithm='python')
print bernoulli(q, algorithm='bernmm')

-23749461029/870
-23749461029/870
-23749461029/870
-818946929/30
-23749461029/870
```


It seems like it would be easiest to delete this file.

Issue created by migration from https://trac.sagemath.org/ticket/4333





---

archive/issue_comments_031772.json:
```json
{
    "body": "Changing assignee from was to mhampton.",
    "created_at": "2008-10-22T16:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4333#issuecomment-31772",
    "user": "mhampton"
}
```

Changing assignee from was to mhampton.



---

archive/issue_comments_031773.json:
```json
{
    "body": "Attachment [trac_4333_remove_bernoulli_py.patch](tarball://root/attachments/some-uuid/ticket4333/trac_4333_remove_bernoulli_py.patch) by mhampton created at 2008-10-22 19:02:44\n\nbased against 3.2 alpha0",
    "created_at": "2008-10-22T19:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4333#issuecomment-31773",
    "user": "mhampton"
}
```

Attachment [trac_4333_remove_bernoulli_py.patch](tarball://root/attachments/some-uuid/ticket4333/trac_4333_remove_bernoulli_py.patch) by mhampton created at 2008-10-22 19:02:44

based against 3.2 alpha0



---

archive/issue_comments_031774.json:
```json
{
    "body": "The patch removes the file bernoulli.py entirely, since it is broken and redundant, and removes the corresponding option from the bernoulli function in rings/arith.py.\n\nI also added some long tests.  I noticed, but did not fix, a problem with the GAP version of bernoulli, that affects computations of B_{2256} and higher:\n\n```\nsage: bernoulli(2256, algorithm = 'gap')\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/Users/mh/sagetest-notebook/worksheets/admin/65/code/18.py\", line 7, in <module>\n    bernoulli(_sage_const_2256 , algorithm = \\u0027gap\\u0027)\n  File \"/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \n  File \"/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/sage/rings/arith.py\", line 212, in bernoulli\n    return Rational(x)\n  File \"rational.pyx\", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4035)\n  File \"rational.pyx\", line 284, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4742)\n  File \"/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 1533, in _rational_\n    return sage.rings.all.Rational(repr(self))\n  File \"rational.pyx\", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4035)\n  File \"rational.pyx\", line 280, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4708)\nTypeError: unable to convert <<an integer too large to be printed>>/14828319870 to a rational\n\n```\n",
    "created_at": "2008-10-22T19:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4333#issuecomment-31774",
    "user": "mhampton"
}
```

The patch removes the file bernoulli.py entirely, since it is broken and redundant, and removes the corresponding option from the bernoulli function in rings/arith.py.

I also added some long tests.  I noticed, but did not fix, a problem with the GAP version of bernoulli, that affects computations of B_{2256} and higher:

```
sage: bernoulli(2256, algorithm = 'gap')

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mh/sagetest-notebook/worksheets/admin/65/code/18.py", line 7, in <module>
    bernoulli(_sage_const_2256 , algorithm = \u0027gap\u0027)
  File "/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/sage/rings/arith.py", line 212, in bernoulli
    return Rational(x)
  File "rational.pyx", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4035)
  File "rational.pyx", line 284, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4742)
  File "/Volumes/D/sage-3.1.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1533, in _rational_
    return sage.rings.all.Rational(repr(self))
  File "rational.pyx", line 189, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:4035)
  File "rational.pyx", line 280, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4708)
TypeError: unable to convert <<an integer too large to be printed>>/14828319870 to a rational

```




---

archive/issue_comments_031775.json:
```json
{
    "body": "Looks good and breaks no doctests.",
    "created_at": "2008-10-24T03:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4333#issuecomment-31775",
    "user": "was"
}
```

Looks good and breaks no doctests.



---

archive/issue_comments_031776.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T00:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4333#issuecomment-31776",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031777.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T00:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4333#issuecomment-31777",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1
