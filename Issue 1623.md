# Issue 1623: update gsl to 1.10

archive/issues_001623.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1623\n\n",
    "created_at": "2007-12-29T04:36:48Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "update gsl to 1.10",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1623",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/1623





---

archive/issue_comments_010306.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-12-29T04:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10306",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_010307.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-29T04:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010308.json:
```json
{
    "body": "Beware that in version 1.10 GNU gsl has chaged its license to\nGPL version 3 (as it is stated in the linked mail), \nso that may raise a license issue",
    "created_at": "2007-12-31T22:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10308",
    "user": "https://github.com/pdenapo"
}
```

Beware that in version 1.10 GNU gsl has chaged its license to
GPL version 3 (as it is stated in the linked mail), 
so that may raise a license issue



---

archive/issue_comments_010309.json:
```json
{
    "body": "All licensing issues regarding GPL V3 and Sage have been resolved by the relicensing of Singular 3-0-4 to \"GPL V2 and V3\".\n\nCheers,\n\nMichael",
    "created_at": "2007-12-31T22:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10309",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

All licensing issues regarding GPL V3 and Sage have been resolved by the relicensing of Singular 3-0-4 to "GPL V2 and V3".

Cheers,

Michael



---

archive/issue_comments_010310.json:
```json
{
    "body": "The other posible problematic package regarding licensing issues is Pari, that I believe is GPL-2",
    "created_at": "2008-01-22T00:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10310",
    "user": "https://github.com/pdenapo"
}
```

The other posible problematic package regarding licensing issues is Pari, that I believe is GPL-2



---

archive/issue_comments_010311.json:
```json
{
    "body": "Nope, pari is licensed under:\n\n```\nPARI/GP is free software; you can redistribute it and/or modify it under the\nterms of the GNU General Public License as published by the Free Software\nFoundation. It is distributed in the hope that it will be useful, but WITHOUT\nANY WARRANTY WHATSOEVER.\n```\n\nSince they do not mention a specific version it is any GPL license version, which include GPL V3. They do ship a copy of the GPL V2 in their sources tarball, but that doesn't imply GPL V2.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T00:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nope, pari is licensed under:

```
PARI/GP is free software; you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation. It is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY WHATSOEVER.
```

Since they do not mention a specific version it is any GPL license version, which include GPL V3. They do ship a copy of the GPL V2 in their sources tarball, but that doesn't imply GPL V2.

Cheers,

Michael



---

archive/issue_comments_010312.json:
```json
{
    "body": "PARI is *not* GPL-2.  It is \"GPL versions >= 2\".  They include the GPL V2 license file, but that file very explicitly says that anything licensed under it is GPL >= 2 unless there is an explicit statement to the contrary elsewhere in the distribution, which there isn't.",
    "created_at": "2008-01-22T00:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10312",
    "user": "https://github.com/williamstein"
}
```

PARI is *not* GPL-2.  It is "GPL versions >= 2".  They include the GPL V2 license file, but that file very explicitly says that anything licensed under it is GPL >= 2 unless there is an explicit statement to the contrary elsewhere in the distribution, which there isn't.



---

archive/issue_comments_010313.json:
```json
{
    "body": "The updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/gsl-1.10.spkg\n\nIt builds fine on OSX & Linux. Currently doctesting.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T22:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/gsl-1.10.spkg

It builds fine on OSX & Linux. Currently doctesting.

Cheers,

Michael



---

archive/issue_comments_010314.json:
```json
{
    "body": "I am seeing the following doctest failure:\n\n```\nsage -t  devel/sage-main/sage/rings/real_double.pyx\n**********************************************************************\nFile \"real_double.pyx\", line 477:\n    sage: a = -RDF(1)/RDF(0); a.str()\nExpected:\n    '-inf'\nGot:\n    'inf'\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T22:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am seeing the following doctest failure:

```
sage -t  devel/sage-main/sage/rings/real_double.pyx
**********************************************************************
File "real_double.pyx", line 477:
    sage: a = -RDF(1)/RDF(0); a.str()
Expected:
    '-inf'
Got:
    'inf'
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_010315.json:
```json
{
    "body": "Another remark: The `spkg-check` target is broken, I am looking into that.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T23:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Another remark: The `spkg-check` target is broken, I am looking into that.

Cheers,

Michael



---

archive/issue_comments_010316.json:
```json
{
    "body": "Ok, this boils down that at least on MacIntel OSX 10.5 the system's `isinf` returns always 1, i.e. all inf's are positive. The issue does not pop up on Linux at all and I have a fixed gsl.spkg that uses a workaround on OSX only.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-25T23:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10316",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, this boils down that at least on MacIntel OSX 10.5 the system's `isinf` returns always 1, i.e. all inf's are positive. The issue does not pop up on Linux at all and I have a fixed gsl.spkg that uses a workaround on OSX only.

Cheers,

Michael



---

archive/issue_comments_010317.json:
```json
{
    "body": "An updated spkg, that passes doctests now on OSX & Linux is at:\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/gsl-1.10.p0.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T00:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10317",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An updated spkg, that passes doctests now on OSX & Linux is at:

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/gsl-1.10.p0.spkg

Cheers,

Michael



---

archive/issue_comments_010318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-26T00:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10318",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001782.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-26T00:19:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1623#event-1782"
}
```



---

archive/issue_comments_010319.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-26T00:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1623#issuecomment-10319",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
