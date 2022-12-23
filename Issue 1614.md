# Issue 1614: cleanup setup.py in sage.spkg

archive/issues_001614.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  craigcitro\n\nWe have a lot of extensions directly listed in the `ext_modules section`. Move those out and also sort the `ext_modules list`\n\nIssue created by migration from https://trac.sagemath.org/ticket/1614\n\n",
    "created_at": "2007-12-28T17:02:27Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "cleanup setup.py in sage.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1614",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  craigcitro

We have a lot of extensions directly listed in the `ext_modules section`. Move those out and also sort the `ext_modules list`

Issue created by migration from https://trac.sagemath.org/ticket/1614





---

archive/issue_comments_010265.json:
```json
{
    "body": "Is there any reason to not list extensions directly in the ext_modules list? This seems far simpler and less error prone. If anything needs to change, I'd move all of them there.",
    "created_at": "2008-01-04T22:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10265",
    "user": "robertwb"
}
```

Is there any reason to not list extensions directly in the ext_modules list? This seems far simpler and less error prone. If anything needs to change, I'd move all of them there.



---

archive/issue_comments_010266.json:
```json
{
    "body": "Well, as it it just seems very inconsistent. We can move it either way, it should just be consistent. I have a Cygwin build patch for setup.py that should be applied before anybody else touches setup.py with some major reorg patch. The is needed because the order of libraries matters on Cygwin. That patch is one of the first patches that I plan to merge for 2.10 as I am reluctant to merge it now for 2.9.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T22:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10266",
    "user": "mabshoff"
}
```

Well, as it it just seems very inconsistent. We can move it either way, it should just be consistent. I have a Cygwin build patch for setup.py that should be applied before anybody else touches setup.py with some major reorg patch. The is needed because the order of libraries matters on Cygwin. That patch is one of the first patches that I plan to merge for 2.10 as I am reluctant to merge it now for 2.9.2.

Cheers,

Michael



---

archive/issue_comments_010267.json:
```json
{
    "body": "This issue has been fixed via #4480 by Craig Citro.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T16:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10267",
    "user": "mabshoff"
}
```

This issue has been fixed via #4480 by Craig Citro.

Cheers,

Michael



---

archive/issue_comments_010268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-13T16:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1614#issuecomment-10268",
    "user": "mabshoff"
}
```

Resolution: fixed
