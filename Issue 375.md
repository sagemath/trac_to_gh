# Issue 375: biopython spkg installer hangs in SAGE 2.5.3

archive/issues_000375.json:
```json
{
    "body": "Assignee: was\n\nWhen installing the biopython-1.43 spkg in SAGE 2.5.3 the installer hangs at:\n\ncopying mx/COPYRIGHT -> /usr/local/sage/local/lib/python2.5/site-packages/mx\ncopying mx/LICENSE -> /usr/local/sage/local/lib/python2.5/site-packages/mx\nrunning install_egg_info\nWriting /usr/local/sage/local/lib/python2.5/site-packages/egenix_mx_base-2.0.6-py2.5.egg-info\nrunning install\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/375\n\n",
    "created_at": "2007-05-23T16:00:46Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "biopython spkg installer hangs in SAGE 2.5.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/375",
    "user": "Jondice"
}
```
Assignee: was

When installing the biopython-1.43 spkg in SAGE 2.5.3 the installer hangs at:

copying mx/COPYRIGHT -> /usr/local/sage/local/lib/python2.5/site-packages/mx
copying mx/LICENSE -> /usr/local/sage/local/lib/python2.5/site-packages/mx
running install_egg_info
Writing /usr/local/sage/local/lib/python2.5/site-packages/egenix_mx_base-2.0.6-py2.5.egg-info
running install


Issue created by migration from https://trac.sagemath.org/ticket/375





---

archive/issue_comments_001787.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2007-05-23T16:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/375#issuecomment-1787",
    "user": "Jondice"
}
```

Changing priority from minor to major.



---

archive/issue_comments_001788.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-05-24T02:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/375#issuecomment-1788",
    "user": "Jondice"
}
```

Changing priority from major to minor.



---

archive/issue_comments_001789.json:
```json
{
    "body": "This seems to be a buffering issue, just pressing enter a few times helps ...",
    "created_at": "2007-05-24T02:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/375#issuecomment-1789",
    "user": "Jondice"
}
```

This seems to be a buffering issue, just pressing enter a few times helps ...



---

archive/issue_comments_001790.json:
```json
{
    "body": "It's still important to fix this.\n\n\n```\n>> biopython install:\n>>\n> This is a known problem.  We are trying to find a hack to get\n> around it,\n> but nobody has found one yet.  I believe if you just hit return a few\n> times when it appears to \"hang\", then it will contiue fine to the end\n> of the build.\n\nIndeed, that works quite nicely. I think I've got everything that is\nlikely to build on OSX, except for the open question about Axiom.\n\nMany thanks\n```\n",
    "created_at": "2007-08-10T20:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/375#issuecomment-1790",
    "user": "was"
}
```

It's still important to fix this.


```
>> biopython install:
>>
> This is a known problem.  We are trying to find a hack to get
> around it,
> but nobody has found one yet.  I believe if you just hit return a few
> times when it appears to "hang", then it will contiue fine to the end
> of the build.

Indeed, that works quite nicely. I think I've got everything that is
likely to build on OSX, except for the open question about Axiom.

Many thanks
```




---

archive/issue_comments_001791.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T12:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/375#issuecomment-1791",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_001792.json:
```json
{
    "body": "Fixed by William and me when we fixed up the new biopython-1.44.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-11-03T12:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/375#issuecomment-1792",
    "user": "mabshoff"
}
```

Fixed by William and me when we fixed up the new biopython-1.44.spkg

Cheers,

Michael
