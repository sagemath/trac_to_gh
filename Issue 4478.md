# Issue 4478: delete spkg-debian-maybe

archive/issues_004478.json:
```json
{
    "body": "Assignee: @timabbott\n\nHow can this file be serious?\n\n```\nwstein@one:~/devel/sage$ more spkg-debian-maybe\n#!/bin/sh -x\nBUILD_ROOT=../../../\nmv dist/debian $BUILD_ROOT\ncd $BUILD_ROOT/..\necho \"Starting Debian build\"\ndasource ./sage-2.10.1\nsbuildhack \"$DEBIAN_RELEASE\" *.dsc\necho \"Debian Build complete\"\n```\n\n\nSee for example the \"sage-2.10.1\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/4478\n\n",
    "created_at": "2008-11-09T08:13:11Z",
    "labels": [
        "debian-package",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "delete spkg-debian-maybe",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4478",
    "user": "@williamstein"
}
```
Assignee: @timabbott

How can this file be serious?

```
wstein@one:~/devel/sage$ more spkg-debian-maybe
#!/bin/sh -x
BUILD_ROOT=../../../
mv dist/debian $BUILD_ROOT
cd $BUILD_ROOT/..
echo "Starting Debian build"
dasource ./sage-2.10.1
sbuildhack "$DEBIAN_RELEASE" *.dsc
echo "Debian Build complete"
```


See for example the "sage-2.10.1"

Issue created by migration from https://trac.sagemath.org/ticket/4478





---

archive/issue_comments_033077.json:
```json
{
    "body": "The system for building all the dependencies Sage needed as Debian packages that never really worked for Sage itself, but this was a prototype for it dating to the sage 2.10 era.  Feel free to delete it.",
    "created_at": "2008-11-10T02:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33077",
    "user": "@timabbott"
}
```

The system for building all the dependencies Sage needed as Debian packages that never really worked for Sage itself, but this was a prototype for it dating to the sage 2.10 era.  Feel free to delete it.



---

archive/issue_comments_033078.json:
```json
{
    "body": "Changing assignee from @timabbott to mabshoff.",
    "created_at": "2008-11-10T04:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33078",
    "user": "mabshoff"
}
```

Changing assignee from @timabbott to mabshoff.



---

archive/issue_comments_033079.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-10T04:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33079",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033080.json:
```json
{
    "body": "This needs some careful fix, i.e. the file exists in two places:\n\n```\n./local/bin/spkg-debian-maybe\n./devel/sage-main/spkg-debian-maybe\n```\n\nBut it is also referred to in two places:\n\n```\ndevel/sage-main/setup.py\ndevel/sage-main/spkg-dist\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-10T04:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33080",
    "user": "mabshoff"
}
```

This needs some careful fix, i.e. the file exists in two places:

```
./local/bin/spkg-debian-maybe
./devel/sage-main/spkg-debian-maybe
```

But it is also referred to in two places:

```
devel/sage-main/setup.py
devel/sage-main/spkg-dist
```


Cheers,

Michael



---

archive/issue_comments_033081.json:
```json
{
    "body": "Attachment [trac-4478-bin.patch](tarball://root/attachments/some-uuid/ticket4478/trac-4478-bin.patch) by @craigcitro created at 2009-05-27 04:33:42\n\npatch for local/bin repository",
    "created_at": "2009-05-27T04:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33081",
    "user": "@craigcitro"
}
```

Attachment [trac-4478-bin.patch](tarball://root/attachments/some-uuid/ticket4478/trac-4478-bin.patch) by @craigcitro created at 2009-05-27 04:33:42

patch for local/bin repository



---

archive/issue_comments_033082.json:
```json
{
    "body": "I've added two patches to fix this. Note that `spkg-debian-maybe` was **not** under version control in `$SAGE_ROOT/local/bin` -- it was only mentioned in `.hgignore`. (It wouldn't hurt to leave that in there, I guess, so feel free to ignore the second patch.)\n\nNote that the main repo patch depends on #6133 -- both touch `MANIFEST.in`, so one had to depend on the other in the end ... and I wrote the other first, so that's how it ended up.\n\nI'm sure this patch could wait for `4.0.1` -- but the \"clean dead files in the build directory\" script I'm just finishing for #5977 notices it, so we might as well just kill it now.",
    "created_at": "2009-05-27T04:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33082",
    "user": "@craigcitro"
}
```

I've added two patches to fix this. Note that `spkg-debian-maybe` was **not** under version control in `$SAGE_ROOT/local/bin` -- it was only mentioned in `.hgignore`. (It wouldn't hurt to leave that in there, I guess, so feel free to ignore the second patch.)

Note that the main repo patch depends on #6133 -- both touch `MANIFEST.in`, so one had to depend on the other in the end ... and I wrote the other first, so that's how it ended up.

I'm sure this patch could wait for `4.0.1` -- but the "clean dead files in the build directory" script I'm just finishing for #5977 notices it, so we might as well just kill it now.



---

archive/issue_comments_033083.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-05-27T04:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33083",
    "user": "@craigcitro"
}
```

Changing status from assigned to new.



---

archive/issue_comments_033084.json:
```json
{
    "body": "Changing assignee from mabshoff to @craigcitro.",
    "created_at": "2009-05-27T04:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33084",
    "user": "@craigcitro"
}
```

Changing assignee from mabshoff to @craigcitro.



---

archive/issue_comments_033085.json:
```json
{
    "body": "Attachment [trac-4478.patch](tarball://root/attachments/some-uuid/ticket4478/trac-4478.patch) by @mwhansen created at 2009-05-28 20:06:57",
    "created_at": "2009-05-28T20:06:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33085",
    "user": "@mwhansen"
}
```

Attachment [trac-4478.patch](tarball://root/attachments/some-uuid/ticket4478/trac-4478.patch) by @mwhansen created at 2009-05-28 20:06:57



---

archive/issue_comments_033086.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33086",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_033087.json:
```json
{
    "body": "The previous patch was doubled up so it caused failures on applying.  The new trac-4478.patch applies.\n\nBoth patches merged in 4.0.rc2.",
    "created_at": "2009-05-28T20:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4478#issuecomment-33087",
    "user": "@mwhansen"
}
```

The previous patch was doubled up so it caused failures on applying.  The new trac-4478.patch applies.

Both patches merged in 4.0.rc2.
