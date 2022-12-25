# Issue 2790: very annoying output of new "sage -tp"

archive/issues_002790.json:
```json
{
    "body": "Assignee: failure\n\nThe new sage -tp has output like this:\n\n```\n\nThe following tests failed:\n\n\tsage -t  devel/sage-modabvar/sage/modular/modform/space.py: 8 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/modform/eisenstein_submodule.py: 1 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/modform/element.py: 1 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/abvar/morphism.py: 8 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/abvar/homspace.py: 8 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1586.7 seconds\nteragon:sage was$ \n```\n\n\nThis is very annoying because I typically *paste* in the output in order to rerun broken doctests.\n\nEasy fix insert a #, i.e., change : x doctests failed to # : x doctests failed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2790\n\n",
    "created_at": "2008-04-03T04:19:57Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "very annoying output of new \"sage -tp\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2790",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

The new sage -tp has output like this:

```

The following tests failed:

	sage -t  devel/sage-modabvar/sage/modular/modform/space.py: 8 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/modform/eisenstein_submodule.py: 1 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/modform/element.py: 1 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/abvar/morphism.py: 8 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/abvar/homspace.py: 8 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1586.7 seconds
teragon:sage was$ 
```


This is very annoying because I typically *paste* in the output in order to rerun broken doctests.

Easy fix insert a #, i.e., change : x doctests failed to # : x doctests failed.

Issue created by migration from https://trac.sagemath.org/ticket/2790





---

archive/issue_comments_019123.json:
```json
{
    "body": "Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T14:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_019124.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-03T14:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19124",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019125.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-04-03T14:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19125",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_019126.json:
```json
{
    "body": "Attachment [trac_2790-separation-character.patch](tarball://root/attachments/some-uuid/ticket2790/trac_2790-separation-character.patch) by mabshoff created at 2008-04-03 15:09:20",
    "created_at": "2008-04-03T15:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2790-separation-character.patch](tarball://root/attachments/some-uuid/ticket2790/trac_2790-separation-character.patch) by mabshoff created at 2008-04-03 15:09:20



---

archive/issue_comments_019127.json:
```json
{
    "body": "Patch looks good.",
    "created_at": "2008-04-03T15:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19127",
    "user": "https://github.com/dfdeshom"
}
```

Patch looks good.



---

archive/issue_events_006444.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-03T15:35:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2790#event-6444"
}
```



---

archive/issue_comments_019128.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T15:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19128",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019129.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-03T15:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19129",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1
