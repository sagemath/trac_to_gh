# Issue 4861: Update FLINT to 1.0.20 (latest 1.0.x upstream)

archive/issues_004861.json:
```json
{
    "body": "Assignee: mabshoff\n\nSee Summary :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4861\n\n",
    "created_at": "2008-12-24T00:12:04Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "Update FLINT to 1.0.20 (latest 1.0.x upstream)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4861",
    "user": "mabshoff"
}
```
Assignee: mabshoff

See Summary :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4861





---

archive/issue_comments_036844.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.3/alpha0/flint-1.0.20.spkg\n\nprovides the latest stable (1.0.x) FLINT release. Also note to apply the patch to the Sage library so that the FLINT dependent extensions are automatically rebuild for an updated FLINT.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T00:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4861#issuecomment-36844",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.3/alpha0/flint-1.0.20.spkg

provides the latest stable (1.0.x) FLINT release. Also note to apply the patch to the Sage library so that the FLINT dependent extensions are automatically rebuild for an updated FLINT.

Cheers,

Michael



---

archive/issue_comments_036845.json:
```json
{
    "body": "Attachment [trac_4861.patch](tarball://root/attachments/some-uuid/ticket4861/trac_4861.patch) by malb created at 2008-12-24 13:45:05\n\n**Review**\n* SPKG.txt is updated properly (+1)\n* hg status returns cleanly (+1)\n* doesn't seem to contain unneeded binary cruft (+1)\n* attached patch `trac_4861.patch` looks good (+1)\n* `spkg-install` works on sage.math (+1)\n* `spkg-install` **runs test suite** (-1)\n* `make ptest` passes on sage.math (+1)\n\n\"positive review\" if the test suite is disabled or it is explained why it needs to be run.",
    "created_at": "2008-12-24T13:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4861#issuecomment-36845",
    "user": "malb"
}
```

Attachment [trac_4861.patch](tarball://root/attachments/some-uuid/ticket4861/trac_4861.patch) by malb created at 2008-12-24 13:45:05

**Review**
* SPKG.txt is updated properly (+1)
* hg status returns cleanly (+1)
* doesn't seem to contain unneeded binary cruft (+1)
* attached patch `trac_4861.patch` looks good (+1)
* `spkg-install` works on sage.math (+1)
* `spkg-install` **runs test suite** (-1)
* `make ptest` passes on sage.math (+1)

"positive review" if the test suite is disabled or it is explained why it needs to be run.



---

archive/issue_comments_036846.json:
```json
{
    "body": "Every time we have upgrades FLINT we automatically run the test suite. This is usually turned off once we do the actual release.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T13:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4861#issuecomment-36846",
    "user": "mabshoff"
}
```

Every time we have upgrades FLINT we automatically run the test suite. This is usually turned off once we do the actual release.

Cheers,

Michael



---

archive/issue_comments_036847.json:
```json
{
    "body": "I know, we just need to stick a reminder somewhere, don't we? If you disagree, just change it to positive review since the worst thing that can happen is an extra couple of minutes of build time.",
    "created_at": "2008-12-24T13:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4861#issuecomment-36847",
    "user": "malb"
}
```

I know, we just need to stick a reminder somewhere, don't we? If you disagree, just change it to positive review since the worst thing that can happen is an extra couple of minutes of build time.



---

archive/issue_comments_036848.json:
```json
{
    "body": "Replying to [comment:4 malb]:\n\nHi Martin,\n\n> I know, we just need to stick a reminder somewhere, don't we? If you disagree, just change it to positive review since the worst thing that can happen is an extra couple of minutes of build time.\n\n#4870 is now a blocker for 3.2.3 to turn it off before release. I would imagine this is a solution we can both live with.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T14:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4861#issuecomment-36848",
    "user": "mabshoff"
}
```

Replying to [comment:4 malb]:

Hi Martin,

> I know, we just need to stick a reminder somewhere, don't we? If you disagree, just change it to positive review since the worst thing that can happen is an extra couple of minutes of build time.

#4870 is now a blocker for 3.2.3 to turn it off before release. I would imagine this is a solution we can both live with.

Cheers,

Michael



---

archive/issue_comments_036849.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-24T14:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4861#issuecomment-36849",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_036850.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-24T14:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4861#issuecomment-36850",
    "user": "mabshoff"
}
```

Resolution: fixed
