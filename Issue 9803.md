# Issue 9803: Remove unnecessary dependy for cliquer in spkg/standard/deps

archive/issues_009803.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  mvngu mpatel ncohen\n\ncliquer used use to SCons, but for various reasons it was replaced by a simple `Makefile`. (IMHO, a good idea, as fighting with SCons seems to be a nightmare). Minh did the replacment, but there is an unnecessary dependency in `spkg/standard/deps`, which potentially means parallel builds are slower than they need be, as currently cliquer can't be built without SCons first being built.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9804\n\n",
    "created_at": "2010-08-26T01:17:47Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "title": "Remove unnecessary dependy for cliquer in spkg/standard/deps",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9803",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  mvngu mpatel ncohen

cliquer used use to SCons, but for various reasons it was replaced by a simple `Makefile`. (IMHO, a good idea, as fighting with SCons seems to be a nightmare). Minh did the replacment, but there is an unnecessary dependency in `spkg/standard/deps`, which potentially means parallel builds are slower than they need be, as currently cliquer can't be built without SCons first being built.

Issue created by migration from https://trac.sagemath.org/ticket/9804





---

archive/issue_comments_096319.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket9804/deps) by drkirkby created at 2010-08-26 01:21:13\n\nReplacement deps, which removes SCONS dependency",
    "created_at": "2010-08-26T01:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96319",
    "user": "drkirkby"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket9804/deps) by drkirkby created at 2010-08-26 01:21:13

Replacement deps, which removes SCONS dependency



---

archive/issue_comments_096320.json:
```json
{
    "body": "Unified diff file for spkg/standard/deps. Relative to 'deps' in sage-4.5.3.alpha2",
    "created_at": "2010-08-26T01:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96320",
    "user": "drkirkby"
}
```

Unified diff file for spkg/standard/deps. Relative to 'deps' in sage-4.5.3.alpha2



---

archive/issue_comments_096321.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-26T01:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96321",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096322.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9804/deps.diff) by drkirkby created at 2010-08-26 01:25:29",
    "created_at": "2010-08-26T01:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96322",
    "user": "drkirkby"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9804/deps.diff) by drkirkby created at 2010-08-26 01:25:29



---

archive/issue_comments_096323.json:
```json
{
    "body": "I'm adding Nathann Cohen to the CC list, as he is the package maintainer.",
    "created_at": "2010-08-28T19:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96323",
    "user": "drkirkby"
}
```

I'm adding Nathann Cohen to the CC list, as he is the package maintainer.



---

archive/issue_comments_096324.json:
```json
{
    "body": "Can you review it Leif? \n\nDave",
    "created_at": "2010-09-04T00:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96324",
    "user": "drkirkby"
}
```

Can you review it Leif? 

Dave



---

archive/issue_comments_096325.json:
```json
{
    "body": "Just for the record: Upstream comes with a Makefile, too (no SConscript).\n\nThe attached `deps` and `deps.diff` still apply to Sage 4.5.3.rc0.\n\n**Positive review.**",
    "created_at": "2010-09-04T05:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96325",
    "user": "leif"
}
```

Just for the record: Upstream comes with a Makefile, too (no SConscript).

The attached `deps` and `deps.diff` still apply to Sage 4.5.3.rc0.

**Positive review.**



---

archive/issue_comments_096326.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-04T05:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96326",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096327.json:
```json
{
    "body": "P.S.: There's a lot wrong with the Cliquer spkg, perhaps to be addressed at #9767.",
    "created_at": "2010-09-04T05:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96327",
    "user": "leif"
}
```

P.S.: There's a lot wrong with the Cliquer spkg, perhaps to be addressed at #9767.



---

archive/issue_comments_096328.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T22:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9803#issuecomment-96328",
    "user": "mpatel"
}
```

Resolution: fixed
