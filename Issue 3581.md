# Issue 3581: The new pbuild pyhon files are not copied on sdist

archive/issues_003581.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.alpha2/spkg/standard/sage-3.0.4.alpha2$ hg status\n! build.py\n! clib.py\n! sagebuild.py\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3581\n\n",
    "created_at": "2008-07-07T06:33:59Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "The new pbuild pyhon files are not copied on sdist",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3581",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.alpha2/spkg/standard/sage-3.0.4.alpha2$ hg status
! build.py
! clib.py
! sagebuild.py
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3581





---

archive/issue_comments_025286.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-07T06:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3581#issuecomment-25286",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025287.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-07T22:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3581#issuecomment-25287",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_025288.json:
```json
{
    "body": "Positive revivew, but we should then also remove the three offending files from MANIFEST.in. I am doing an sdist with the patch applied to make 100% sure it works.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3581#issuecomment-25288",
    "user": "mabshoff"
}
```

Positive revivew, but we should then also remove the three offending files from MANIFEST.in. I am doing an sdist with the patch applied to make 100% sure it works.

Cheers,

Michael



---

archive/issue_comments_025289.json:
```json
{
    "body": "I can now confirm this actually works:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard$ tar xjf sage-3.0.4.foo.spkg \nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard$ cd sage-3.0.4.foo\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard/sage-3.0.4.foo$ hg status\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard/sage-3.0.4.foo$ \n```\n\nsage-3.0.4.foo is the sdisted 3.0.4.a2 with the patch applied :)\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T22:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3581#issuecomment-25289",
    "user": "mabshoff"
}
```

I can now confirm this actually works:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard$ tar xjf sage-3.0.4.foo.spkg 
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard$ cd sage-3.0.4.foo
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard/sage-3.0.4.foo$ hg status
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/dist/sage-3.0.4.foo/spkg/standard/sage-3.0.4.foo$ 
```

sage-3.0.4.foo is the sdisted 3.0.4.a2 with the patch applied :)

Cheers,

Michael



---

archive/issue_comments_025290.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T22:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3581#issuecomment-25290",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_025291.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T23:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3581#issuecomment-25291",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0
