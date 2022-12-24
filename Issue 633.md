# Issue 633: spkg-[install|check] should verify that SAGE_LOCAL is defined

archive/issues_000633.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: spkg-install, spkg-check\n\nWhen building spkgs manually by invoking spkg-install on the shell I oftern do not have sage-env sourced. Consequently odd things happen:\n\n```\n[mabshoff@m940 mpfr-2.2.1.p1]$ ./spkg-install\n./spkg-install: line 16: [: =: unary operator expected\n```\n\nWe ought to verify that at least SAGE_LOCAL is non-empty. If it is empty print a warning message and exit.\n\nTo fix this we need to touch every spkg-install in the tree which is more that 75 scripts. So while we are at it we should also add spkg-check scripts to each spkg while we are at it.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/633\n\n",
    "created_at": "2007-09-10T03:42:39Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "spkg-[install|check] should verify that SAGE_LOCAL is defined",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/633",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Keywords: spkg-install, spkg-check

When building spkgs manually by invoking spkg-install on the shell I oftern do not have sage-env sourced. Consequently odd things happen:

```
[mabshoff@m940 mpfr-2.2.1.p1]$ ./spkg-install
./spkg-install: line 16: [: =: unary operator expected
```

We ought to verify that at least SAGE_LOCAL is non-empty. If it is empty print a warning message and exit.

To fix this we need to touch every spkg-install in the tree which is more that 75 scripts. So while we are at it we should also add spkg-check scripts to each spkg while we are at it.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/633





---

archive/issue_comments_003258.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-18T13:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/633#issuecomment-3258",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003259.json:
```json
{
    "body": "I suggest adding the following to the top of all spkg-install and spkg-check scripts:\n\n```\nif [ \"$SAGE_LOCAL\" = \"\" ]; then\n   echo \"SAGE_LOCAL undefined ... exiting\";\n   exit 1\nfi\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T10:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/633#issuecomment-3259",
    "user": "mabshoff"
}
```

I suggest adding the following to the top of all spkg-install and spkg-check scripts:

```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   exit 1
fi
```


Cheers,

Michael



---

archive/issue_comments_003260.json:
```json
{
    "body": "Wouldn't it be useful to also give a hint about what the user should do, e.g., something like:\n\n\n```\nif [ \"$SAGE_LOCAL\" = \"\" ]; then\n   echo \"SAGE_LOCAL undefined ... exiting\";\n   echo \"Maybe run 'sage -sh'?\"\n   exit 1\nfi\n```\n",
    "created_at": "2008-01-27T13:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/633#issuecomment-3260",
    "user": "@williamstein"
}
```

Wouldn't it be useful to also give a hint about what the user should do, e.g., something like:


```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi
```




---

archive/issue_comments_003261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T03:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/633#issuecomment-3261",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003262.json:
```json
{
    "body": "I have been adding the above code snippet to every spkg that I have touched in the last couple month and I assume all of them have been fixed. If there is any more specific spkg with issue it should be dealt with at its own ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T03:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/633#issuecomment-3262",
    "user": "mabshoff"
}
```

I have been adding the above code snippet to every spkg that I have touched in the last couple month and I assume all of them have been fixed. If there is any more specific spkg with issue it should be dealt with at its own ticket.

Cheers,

Michael
