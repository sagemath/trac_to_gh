# Issue 5748: Sage 3.4.1.rc2: isinf() related doctest failure in sage/rings/infinity.py

archive/issues_005748.json:
```json
{
    "body": "Assignee: mabshoff\n\nNotice the following on OSX and Solaris:\n\n```\nbsd:sage-3.4.1.rc2 mabshoff$ ./sage -t  devel/sage/sage/rings/infinity.py\nsage -t  \"devel/sage/sage/rings/infinity.py\"                \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.4.1.rc2/devel/sage/sage/rings/infinity.py\", line 408:\n    sage: CDF(-infinity)\nExpected:\n    -infinity\nGot:\n    +infinity\n**********************************************************************\n```\n\nIIRC there was an analog problem in the GSL when using isinf() on OSX and Solaris due to the system's math library having a bug.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5748\n\n",
    "created_at": "2009-04-11T08:13:38Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "Sage 3.4.1.rc2: isinf() related doctest failure in sage/rings/infinity.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5748",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Notice the following on OSX and Solaris:

```
bsd:sage-3.4.1.rc2 mabshoff$ ./sage -t  devel/sage/sage/rings/infinity.py
sage -t  "devel/sage/sage/rings/infinity.py"                
**********************************************************************
File "/Users/mabshoff/sage-3.4.1.rc2/devel/sage/sage/rings/infinity.py", line 408:
    sage: CDF(-infinity)
Expected:
    -infinity
Got:
    +infinity
**********************************************************************
```

IIRC there was an analog problem in the GSL when using isinf() on OSX and Solaris due to the system's math library having a bug.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5748





---

archive/issue_comments_044934.json:
```json
{
    "body": "We should use GSL to determine if the double is +infinity or -infinity. It fixes the problem on OSX for GSL's printing, etc:\n\n```\nint\ngsl_isinf (const double x)\n{\n  int fpc = _fpclass(x);\n\n  if (fpc == _FPCLASS_PINF)\n    return +1;\n  else if (fpc == _FPCLASS_NINF)\n    return -1;\n  else \n    return 0;\n}\n```\n\nWe should also take a look at sage/rings/real_double.pyx where cwitty does this clever thing:\n\n```\n        \"\"\"\n        cdef int isinf = gsl_isinf(self._value)\n        cdef bint isnan = gsl_isnan(self._value)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T04:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5748#issuecomment-44934",
    "user": "mabshoff"
}
```

We should use GSL to determine if the double is +infinity or -infinity. It fixes the problem on OSX for GSL's printing, etc:

```
int
gsl_isinf (const double x)
{
  int fpc = _fpclass(x);

  if (fpc == _FPCLASS_PINF)
    return +1;
  else if (fpc == _FPCLASS_NINF)
    return -1;
  else 
    return 0;
}
```

We should also take a look at sage/rings/real_double.pyx where cwitty does this clever thing:

```
        """
        cdef int isinf = gsl_isinf(self._value)
        cdef bint isnan = gsl_isnan(self._value)
```


Cheers,

Michael



---

archive/issue_comments_044935.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-15T05:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5748#issuecomment-44935",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_044936.json:
```json
{
    "body": "Code looks good, doctests pass.  Positive review.",
    "created_at": "2009-04-15T05:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5748#issuecomment-44936",
    "user": "cwitty"
}
```

Code looks good, doctests pass.  Positive review.



---

archive/issue_comments_044937.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-15T06:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5748#issuecomment-44937",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044938.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T06:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5748#issuecomment-44938",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
