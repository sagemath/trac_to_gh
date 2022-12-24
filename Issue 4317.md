# Issue 4317: relocation after make install is broken

archive/issues_004317.json:
```json
{
    "body": "Assignee: cwitty\n\nTo reproduce:\n\n1) build sage from source, say in /tmp/sage-3.1.4\n\n2) type make install DESTDIR=/usr/local/sage-3.1.4 (for example)\n\n3) modify a file in /usr/local/sage-3.1.4, say integers.pyx (for example change the default base for digits)\n\n4) run /usr/local/sage-3.1.4/bin/sage -br\n\n5) try the modified function: the change has not been taken into account!\n\nThe fix is to rename /tmp/sage-3.1.4 into (say) /tmp/sage-3.1.4-old. It appears the relocation does\nnot work any more, or more precisely that sage first looks into the build directory if it still\nexists.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4317\n\n",
    "created_at": "2008-10-18T15:22:07Z",
    "labels": [
        "relocation",
        "major",
        "bug"
    ],
    "title": "relocation after make install is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4317",
    "user": "zimmerma"
}
```
Assignee: cwitty

To reproduce:

1) build sage from source, say in /tmp/sage-3.1.4

2) type make install DESTDIR=/usr/local/sage-3.1.4 (for example)

3) modify a file in /usr/local/sage-3.1.4, say integers.pyx (for example change the default base for digits)

4) run /usr/local/sage-3.1.4/bin/sage -br

5) try the modified function: the change has not been taken into account!

The fix is to rename /tmp/sage-3.1.4 into (say) /tmp/sage-3.1.4-old. It appears the relocation does
not work any more, or more precisely that sage first looks into the build directory if it still
exists.

Issue created by migration from https://trac.sagemath.org/ticket/4317





---

archive/issue_comments_031593.json:
```json
{
    "body": "\n```\n[11:04pm] mabshoff: craigcitro: so the problem happens when we deal with changed py files - not pyx?\n[11:04pm] craigcitro: i haven't tested pyx\n[11:04pm] mabshoff: ok\n[11:04pm] craigcitro: got it.\n[11:04pm] craigcitro: well, got halfway there, anyway\n[11:04pm] mabshoff: Paul hits the same problem with pyx files, too.\n[11:05pm] mabshoff: Excellent \n[11:05pm] craigcitro: there's a file called $SAGE_ROOT/local/lib/python-2.5/site-packages/easy-install.pth\n[11:05pm] craigcitro: that file has your directory in it.\n[11:05pm] craigcitro: kill the line with your directory, everything works.\n[11:05pm] mabshoff: ah\n[11:06pm] mabshoff: So that file needs to be updated when a moved Sage install is detected.\n```\n",
    "created_at": "2008-10-30T06:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31593",
    "user": "mabshoff"
}
```


```
[11:04pm] mabshoff: craigcitro: so the problem happens when we deal with changed py files - not pyx?
[11:04pm] craigcitro: i haven't tested pyx
[11:04pm] mabshoff: ok
[11:04pm] craigcitro: got it.
[11:04pm] craigcitro: well, got halfway there, anyway
[11:04pm] mabshoff: Paul hits the same problem with pyx files, too.
[11:05pm] mabshoff: Excellent 
[11:05pm] craigcitro: there's a file called $SAGE_ROOT/local/lib/python-2.5/site-packages/easy-install.pth
[11:05pm] craigcitro: that file has your directory in it.
[11:05pm] craigcitro: kill the line with your directory, everything works.
[11:05pm] mabshoff: ah
[11:06pm] mabshoff: So that file needs to be updated when a moved Sage install is detected.
```




---

archive/issue_comments_031594.json:
```json
{
    "body": "Check out http://www.mail-archive.com/distutils-sig`@`python.org/msg05817.html\n\nAlso note that easy-install.pth is used in a bunch of places\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha2$ grep -r \"easy-install.pth\" *\ninstall.log:Adding setuptools 0.6c8 to easy-install.pth file\ninstall.log:Adding SQLAlchemy 0.4.6 to easy-install.pth file\ninstall.log:Adding Jinja 1.2 to easy-install.pth file\ninstall.log:Adding Pygments 0.11.1 to easy-install.pth file\ninstall.log:Adding Sphinx 0.5dev-20081027 to easy-install.pth file\ninstall.log:Adding docutils 0.5 to easy-install.pth file\ninstall.log:Jinja 1.2 is already the active version in easy-install.pth\ninstall.log:Pygments 0.11.1 is already the active version in easy-install.pth\n```\n",
    "created_at": "2008-10-30T06:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31594",
    "user": "mabshoff"
}
```

Check out http://www.mail-archive.com/distutils-sig`@`python.org/msg05817.html

Also note that easy-install.pth is used in a bunch of places

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha2$ grep -r "easy-install.pth" *
install.log:Adding setuptools 0.6c8 to easy-install.pth file
install.log:Adding SQLAlchemy 0.4.6 to easy-install.pth file
install.log:Adding Jinja 1.2 to easy-install.pth file
install.log:Adding Pygments 0.11.1 to easy-install.pth file
install.log:Adding Sphinx 0.5dev-20081027 to easy-install.pth file
install.log:Adding docutils 0.5 to easy-install.pth file
install.log:Jinja 1.2 is already the active version in easy-install.pth
install.log:Pygments 0.11.1 is already the active version in easy-install.pth
```




---

archive/issue_comments_031595.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-20T00:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31595",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_031596.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-20T00:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31596",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031597.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-11-20T00:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31597",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_031598.json:
```json
{
    "body": "This really ought to get fixed for 3.2.1.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-20T00:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31598",
    "user": "mabshoff"
}
```

This really ought to get fixed for 3.2.1.

Cheers,

Michael



---

archive/issue_comments_031599.json:
```json
{
    "body": "Attachment [trac_4317_scripts.patch](tarball://root/attachments/some-uuid/ticket4317/trac_4317_scripts.patch) by was created at 2008-12-01 08:37:43",
    "created_at": "2008-12-01T08:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31599",
    "user": "was"
}
```

Attachment [trac_4317_scripts.patch](tarball://root/attachments/some-uuid/ticket4317/trac_4317_scripts.patch) by was created at 2008-12-01 08:37:43



---

archive/issue_comments_031600.json:
```json
{
    "body": "Positive review. I fixed the spelling issue that Craig pointed out to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T08:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31600",
    "user": "mabshoff"
}
```

Positive review. I fixed the spelling issue that Craig pointed out to me.

Cheers,

Michael



---

archive/issue_comments_031601.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-12-01T08:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31601",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc1



---

archive/issue_comments_031602.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-01T08:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4317#issuecomment-31602",
    "user": "mabshoff"
}
```

Resolution: fixed
