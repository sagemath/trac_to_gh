# Issue 2173: [with patch; needs review] SAGE setup.py should run cython as "python2.5 cython"

archive/issues_002173.json:
```json
{
    "body": "Assignee: @timabbott\n\nthe cython in debian runs as #!/usr/bin/python, and /usr/bin/python is python2.4 by default in Debian.  Thus, the SAGE setup.py should explicitly run \"python2.5 cython\" to get python2.5.\n\nI'm submitting in non-mercurial format since I get the following error when I try to:\n\n[tabbott`@`mega-man sage$] hg diff\nabort: index 00changelog.i invalid format 2!\n[tabbott`@`mega-man sage$] cat .hg/00changelog.i ; echo\n\ufffd dummy changelog to prevent using the old repo layout\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2173\n\n",
    "created_at": "2008-02-16T01:06:23Z",
    "labels": [
        "component: debian-package"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch; needs review] SAGE setup.py should run cython as \"python2.5 cython\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2173",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

the cython in debian runs as #!/usr/bin/python, and /usr/bin/python is python2.4 by default in Debian.  Thus, the SAGE setup.py should explicitly run "python2.5 cython" to get python2.5.

I'm submitting in non-mercurial format since I get the following error when I try to:

[tabbott`@`mega-man sage$] hg diff
abort: index 00changelog.i invalid format 2!
[tabbott`@`mega-man sage$] cat .hg/00changelog.i ; echo
� dummy changelog to prevent using the old repo layout


Issue created by migration from https://trac.sagemath.org/ticket/2173





---

archive/issue_comments_014240.json:
```json
{
    "body": "Attachment [setup.py.diff](tarball://root/attachments/some-uuid/ticket2173/setup.py.diff) by mabshoff created at 2008-02-16 01:27:42\n\nThe patch doesn't work as is for the non-Debianized build:\n\n```\nBuilding sage/matrix/matrix_dense.c because it depends on sage/matrix/matrix_dense.pyx.\npython2.5 cython --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/devel/sage-main -o sage/matrix/matrix_dense.c sage/matrix/matrix_dense.pyx\npython2.5: can't open file 'cython': [Errno 2] No such file or directory\nsage: Error running cython.\nsage: There was an error installing modified sage library code.\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T01:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2173#issuecomment-14240",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [setup.py.diff](tarball://root/attachments/some-uuid/ticket2173/setup.py.diff) by mabshoff created at 2008-02-16 01:27:42

The patch doesn't work as is for the non-Debianized build:

```
Building sage/matrix/matrix_dense.c because it depends on sage/matrix/matrix_dense.pyx.
python2.5 cython --embed-positions --incref-local-binop -I/scratch/mabshoff/release-cycle/sage-2.10.2.alpha1/devel/sage-main -o sage/matrix/matrix_dense.c sage/matrix/matrix_dense.pyx
python2.5: can't open file 'cython': [Errno 2] No such file or directory
sage: Error running cython.
sage: There was an error installing modified sage library code.
```

Cheers,

Michael



---

archive/issue_comments_014241.json:
```json
{
    "body": "I guess it is a patch issue: `python2.5 `which cython`` works. We could just do something analog like the other places in setup.py and introduce a special case for the Debianized build.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T01:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2173#issuecomment-14241",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I guess it is a patch issue: `python2.5 `which cython`` works. We could just do something analog like the other places in setup.py and introduce a special case for the Debianized build.

Cheers,

Michael



---

archive/issue_comments_014242.json:
```json
{
    "body": "Yeah, python2.5 `which cython` is what I'd intended; for non-debian builds, SAGE_LOCAL/bin should be in PATH, and for Debian builds, /usr/bin/cython will be in PATH, so I think that's best.",
    "created_at": "2008-02-16T01:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2173#issuecomment-14242",
    "user": "https://github.com/timabbott"
}
```

Yeah, python2.5 `which cython` is what I'd intended; for non-debian builds, SAGE_LOCAL/bin should be in PATH, and for Debian builds, /usr/bin/cython will be in PATH, so I think that's best.



---

archive/issue_comments_014243.json:
```json
{
    "body": "I'm attaching a new patch that includes the python2.5 `which cython` change and also the other things that were needed to get SAGE 2.10.4 to build on Debian.\n\nI think the changeset can be cleaned up to just create a symlink 'python' in SAGE_LOCAL/bin that goes to the working python2.5 and then one would not have to do as many changes that replace 'python' with 'python2.5' in the build process.",
    "created_at": "2008-03-29T22:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2173#issuecomment-14243",
    "user": "https://github.com/timabbott"
}
```

I'm attaching a new patch that includes the python2.5 `which cython` change and also the other things that were needed to get SAGE 2.10.4 to build on Debian.

I think the changeset can be cleaned up to just create a symlink 'python' in SAGE_LOCAL/bin that goes to the working python2.5 and then one would not have to do as many changes that replace 'python' with 'python2.5' in the build process.



---

archive/issue_comments_014244.json:
```json
{
    "body": "Attachment [sage-spkg-debian.patch](tarball://root/attachments/some-uuid/ticket2173/sage-spkg-debian.patch) by mabshoff created at 2008-03-29 23:04:47\n\nsage-spkg-debian.patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T23:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2173#issuecomment-14244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-spkg-debian.patch](tarball://root/attachments/some-uuid/ticket2173/sage-spkg-debian.patch) by mabshoff created at 2008-03-29 23:04:47

sage-spkg-debian.patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_014245.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T23:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2173#issuecomment-14245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0



---

archive/issue_comments_014246.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T23:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2173",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2173#issuecomment-14246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
