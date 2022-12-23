# Issue 572: in sage-env make sure we do not append ":"  LD_WHATEVER

archive/issues_000572.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello,\n\nThe optinal gcc spkg doesn't like trailing \":\" in environment variables:\n\n```\n[20:06] <mabshoff> Another thing:\n[20:06] <mabshoff> *** LIBRARY_PATH shouldn't contain the current directory when\n[20:06] <mabshoff> *** building gcc. Please change the environment variable\n[20:06] <mabshoff> *** and run configure again.\n<SNIP>\n[20:10] <mabshoff> Problem might be that \"LIBRARY_PATH=/tmp/Work2/sage-2.8.3.rc3/local/lib/:\" has the trailing \":\"\n[20:10] <sage> ah. you could change that too\n[20:10] <mabshoff> If LD_WHATEVER is empty skip the $LD_WHATEVER on export :\n[20:10] <mabshoff> .\n[20:11] <mabshoff> Removing the trailing \":\" makes configure work.\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/572\n\n",
    "created_at": "2007-09-02T18:29:57Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "in sage-env make sure we do not append \":\"  LD_WHATEVER",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/572",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Hello,

The optinal gcc spkg doesn't like trailing ":" in environment variables:

```
[20:06] <mabshoff> Another thing:
[20:06] <mabshoff> *** LIBRARY_PATH shouldn't contain the current directory when
[20:06] <mabshoff> *** building gcc. Please change the environment variable
[20:06] <mabshoff> *** and run configure again.
<SNIP>
[20:10] <mabshoff> Problem might be that "LIBRARY_PATH=/tmp/Work2/sage-2.8.3.rc3/local/lib/:" has the trailing ":"
[20:10] <sage> ah. you could change that too
[20:10] <mabshoff> If LD_WHATEVER is empty skip the $LD_WHATEVER on export :
[20:10] <mabshoff> .
[20:11] <mabshoff> Removing the trailing ":" makes configure work.
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/572





---

archive/issue_comments_002974.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T18:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/572#issuecomment-2974",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-02T20:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/572",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/572#issuecomment-2975",
    "user": "was"
}
```

Resolution: fixed
