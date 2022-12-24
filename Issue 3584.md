# Issue 3584: cython.py -- randomness in doctests

archive/issues_003584.json:
```json
{
    "body": "Assignee: failure\n\nOn Debian 64-bit vmware:\n\n```\nsage -t  devel/sage/sage/misc/cython.py                     **********************************************************************\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/cython.py\", line 109:\n    sage: pyx_preparse(\"\")\nExpected:\n    ('\\ninclude \"interrupt.pxi\"  # ctrl-c interrupt block support\\ninclude \"stdsage.pxi\"  # ctrl-c interrupt block support\\n\\ninclude \"cdefs.pxi\"\\n',\n    ['mpfr',\n    'gmp',\n    'gmpxx',\n    'stdc++',\n    'pari',\n    'm',\n    'curvesntl',\n    'g0nntl',\n    'jcntl',\n    'rankntl',\n    'gsl',\n    'cblas',\n    'atlas',\n    'ntl',\n    'csage'],\n    ['.../local/include/csage/',\n    '.../local/include/',\n    '.../local/include/python2.5/',\n    '.../devel/sage/sage/ext/',\n    '.../devel/sage/',\n    '.../devel/sage/sage/gsl/'],\n    'c',\n    [])\nGot:\n    ('\\ninclude \"interrupt.pxi\"  # ctrl-c interrupt block support\\ninclude \"stdsage.pxi\"  # ctrl-c interrupt block support\\n\\ninclude \"cdefs.pxi\"\\n', ['mpfr', 'gmp', 'gmpxx', 'stdc++', 'pari', 'm', 'curvesntl', 'g0nntl', 'jcntl', 'rankntl', 'gsl', 'gslcblas', 'atlas', 'ntl', 'csage'], ['/home/was/build/sage-3.0.4.alpha2/local/include/csage/', '/home/was/build/sage-3.0.4.alpha2/local/include/', '/home/was/build/sage-3.0.4.alpha2/local/include/python2.5/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/sage/ext/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/sage/gsl/'], 'c', [])\n**********************************************************************\nFile \"/home/was/build/sage-3.0.4.alpha2/tmp/cython.py\", line 138:\n    sage: libs\nExpected:\n    ['foo', 'mpfr',\n    'gmp', 'gmpxx',\n    'stdc++',\n    'pari',\n    'm',\n    'curvesntl', 'g0nntl', 'jcntl', 'rankntl',\n    'gsl', 'cblas', 'atlas',\n    'ntl',\n    'csage']\nGot:\n    ['foo', 'mpfr', 'gmp', 'gmpxx', 'stdc++', 'pari', 'm', 'curvesntl', 'g0nntl', 'jcntl', 'rankntl', 'gsl', 'gslcblas', 'atlas', 'ntl', 'csage']\n**********************************************************************\n1 items had failures:\n   2 of   7 in __main__.example_1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3584\n\n",
    "created_at": "2008-07-07T15:21:02Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "cython.py -- randomness in doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3584",
    "user": "was"
}
```
Assignee: failure

On Debian 64-bit vmware:

```
sage -t  devel/sage/sage/misc/cython.py                     **********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/cython.py", line 109:
    sage: pyx_preparse("")
Expected:
    ('\ninclude "interrupt.pxi"  # ctrl-c interrupt block support\ninclude "stdsage.pxi"  # ctrl-c interrupt block support\n\ninclude "cdefs.pxi"\n',
    ['mpfr',
    'gmp',
    'gmpxx',
    'stdc++',
    'pari',
    'm',
    'curvesntl',
    'g0nntl',
    'jcntl',
    'rankntl',
    'gsl',
    'cblas',
    'atlas',
    'ntl',
    'csage'],
    ['.../local/include/csage/',
    '.../local/include/',
    '.../local/include/python2.5/',
    '.../devel/sage/sage/ext/',
    '.../devel/sage/',
    '.../devel/sage/sage/gsl/'],
    'c',
    [])
Got:
    ('\ninclude "interrupt.pxi"  # ctrl-c interrupt block support\ninclude "stdsage.pxi"  # ctrl-c interrupt block support\n\ninclude "cdefs.pxi"\n', ['mpfr', 'gmp', 'gmpxx', 'stdc++', 'pari', 'm', 'curvesntl', 'g0nntl', 'jcntl', 'rankntl', 'gsl', 'gslcblas', 'atlas', 'ntl', 'csage'], ['/home/was/build/sage-3.0.4.alpha2/local/include/csage/', '/home/was/build/sage-3.0.4.alpha2/local/include/', '/home/was/build/sage-3.0.4.alpha2/local/include/python2.5/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/sage/ext/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/', '/home/was/build/sage-3.0.4.alpha2/devel/sage/sage/gsl/'], 'c', [])
**********************************************************************
File "/home/was/build/sage-3.0.4.alpha2/tmp/cython.py", line 138:
    sage: libs
Expected:
    ['foo', 'mpfr',
    'gmp', 'gmpxx',
    'stdc++',
    'pari',
    'm',
    'curvesntl', 'g0nntl', 'jcntl', 'rankntl',
    'gsl', 'cblas', 'atlas',
    'ntl',
    'csage']
Got:
    ['foo', 'mpfr', 'gmp', 'gmpxx', 'stdc++', 'pari', 'm', 'curvesntl', 'g0nntl', 'jcntl', 'rankntl', 'gsl', 'gslcblas', 'atlas', 'ntl', 'csage']
**********************************************************************
1 items had failures:
   2 of   7 in __main__.example_1
```


Issue created by migration from https://trac.sagemath.org/ticket/3584





---

archive/issue_comments_025301.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-07T18:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3584#issuecomment-25301",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025302.json:
```json
{
    "body": "Attachment [trac-3584.patch](tarball://root/attachments/some-uuid/ticket3584/trac-3584.patch) by craigcitro created at 2008-07-07 18:31:39\n\nThe attached patch fixes the doctest, and adds another that's slightly better. I also did a bit of cleanup in the file. \n\nI added a docstring to `parse_keywords`, and also made one minor change to that function. (It used to always add a `#` right before the keyword, so I had it check to see if it was already on a line containing a hash. I could be convinced this isn't worth it.)",
    "created_at": "2008-07-07T18:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3584#issuecomment-25302",
    "user": "craigcitro"
}
```

Attachment [trac-3584.patch](tarball://root/attachments/some-uuid/ticket3584/trac-3584.patch) by craigcitro created at 2008-07-07 18:31:39

The attached patch fixes the doctest, and adds another that's slightly better. I also did a bit of cleanup in the file. 

I added a docstring to `parse_keywords`, and also made one minor change to that function. (It used to always add a `#` right before the keyword, so I had it check to see if it was already on a line containing a hash. I could be convinced this isn't worth it.)



---

archive/issue_comments_025303.json:
```json
{
    "body": "Changing assignee from failure to craigcitro.",
    "created_at": "2008-07-07T18:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3584#issuecomment-25303",
    "user": "craigcitro"
}
```

Changing assignee from failure to craigcitro.



---

archive/issue_comments_025304.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T21:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3584#issuecomment-25304",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_025305.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T21:51:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3584#issuecomment-25305",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0
