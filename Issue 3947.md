# Issue 3947: readline and ipython

archive/issues_003947.json:
```json
{
    "body": "Assignee: tbd\n\nWhen built with --enable-framework, python doesn't produce a file \n` local/lib/python2.5/lib-dynload/readline.so `\nbecause it doesn't find libreadline.dylib.\n\nThe reason for that is that with enable-framework, python doesn't look in the SAGE_LOCAL/include and SAGE_LOCAL/lib directories.  mabshoff reckons this is a generic issue.\n\nspkg-install requires the following:\n\n```\nLDFLAGS=\"-L/Users/dphilp/sage-3.0.3fo/local/lib $LDFLAGS\"\nexport LDFLAGS\n\nCPPFLAGS=\"-I/Users/dphilp/sage-3.0.3fo/local/include $CPPFLAGS\"\nexport CPPFLAGS\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3947\n\n",
    "created_at": "2008-08-25T07:04:19Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "readline and ipython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3947",
    "user": "dphilp"
}
```
Assignee: tbd

When built with --enable-framework, python doesn't produce a file 
` local/lib/python2.5/lib-dynload/readline.so `
because it doesn't find libreadline.dylib.

The reason for that is that with enable-framework, python doesn't look in the SAGE_LOCAL/include and SAGE_LOCAL/lib directories.  mabshoff reckons this is a generic issue.

spkg-install requires the following:

```
LDFLAGS="-L/Users/dphilp/sage-3.0.3fo/local/lib $LDFLAGS"
export LDFLAGS

CPPFLAGS="-I/Users/dphilp/sage-3.0.3fo/local/include $CPPFLAGS"
export CPPFLAGS
```


Issue created by migration from https://trac.sagemath.org/ticket/3947





---

archive/issue_comments_028333.json:
```json
{
    "body": "except probly not that specific to my system.",
    "created_at": "2008-08-25T07:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28333",
    "user": "dphilp"
}
```

except probly not that specific to my system.



---

archive/issue_comments_028334.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-08-25T07:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28334",
    "user": "mabshoff"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_028335.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2008-08-25T07:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28335",
    "user": "mabshoff"
}
```

Changing component from algebra to build.



---

archive/issue_comments_028336.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-25T07:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28336",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028337.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/python-2.5.2.p4.spkg\n\nfixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T07:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28337",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha1/python-2.5.2.p4.spkg

fixes the issue.

Cheers,

Michael



---

archive/issue_comments_028338.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-08-25T19:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28338",
    "user": "@mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_028339.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T20:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28339",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_028340.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T20:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3947",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3947#issuecomment-28340",
    "user": "mabshoff"
}
```

Resolution: fixed
