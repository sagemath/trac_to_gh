# Issue 1187: bug in G.conjugacy_classes_subgroups()

archive/issues_001187.json:
```json
{
    "body": "Assignee: @mwhansen\n\nThe following should work and be instant:\n\n\n```\nsage: G = SymmetricGroup(5)\nsage: G.conjugacy_classes_subgroups()\n\nRuntimeError:\nGap produced error output\nVariable: 'Sym' must have a value\n\n\n   executing $sage85:=Sym( [ 1 .. 5 ] );;\n```\n\n\n\nI really wanted this to find out which representative subgroups\nare transitive, but can't do that either since `G.is_transitive()`\nisn't wrapped -- since Gap has IsTransitive, this would be trivial to wrap.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1187\n\n",
    "created_at": "2007-11-16T20:45:35Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "bug in G.conjugacy_classes_subgroups()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1187",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

The following should work and be instant:


```
sage: G = SymmetricGroup(5)
sage: G.conjugacy_classes_subgroups()

RuntimeError:
Gap produced error output
Variable: 'Sym' must have a value


   executing $sage85:=Sym( [ 1 .. 5 ] );;
```



I really wanted this to find out which representative subgroups
are transitive, but can't do that either since `G.is_transitive()`
isn't wrapped -- since Gap has IsTransitive, this would be trivial to wrap.

Issue created by migration from https://trac.sagemath.org/ticket/1187





---

archive/issue_comments_007306.json:
```json
{
    "body": "Changing component from combinatorics to group_theory.",
    "created_at": "2008-04-24T22:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7306",
    "user": "https://github.com/aghitza"
}
```

Changing component from combinatorics to group_theory.



---

archive/issue_comments_007307.json:
```json
{
    "body": "Changing assignee from @mwhansen to joyner.",
    "created_at": "2008-04-24T22:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7307",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @mwhansen to joyner.



---

archive/issue_comments_007308.json:
```json
{
    "body": "Attachment [1187-permgroups.patch](tarball://root/attachments/some-uuid/ticket1187/1187-permgroups.patch) by @aghitza created at 2008-04-24 22:25:44\n\nThe attached patch fixes what I believe is a bug in conjugacy_classes_subgroups(), and adds the method is_transitive().  Note that the optional GAP database is *not* required.\n\nTimings before the patch:\n\n\n```\nsage: G = SymmetricGroup(6)\nsage: time cl = G.conjugacy_classes_subgroups()\nCPU times: user 151.62 s, sys: 16.75 s, total: 168.37 s\nWall time: 175.53\n```\n\n\nand after:\n\n\n```\nsage: G = SymmetricGroup(6)\nsage: time cl = G.conjugacy_classes_subgroups()\nCPU times: user 0.54 s, sys: 0.09 s, total: 0.63 s\nWall time: 1.35\n```\n",
    "created_at": "2008-04-24T22:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7308",
    "user": "https://github.com/aghitza"
}
```

Attachment [1187-permgroups.patch](tarball://root/attachments/some-uuid/ticket1187/1187-permgroups.patch) by @aghitza created at 2008-04-24 22:25:44

The attached patch fixes what I believe is a bug in conjugacy_classes_subgroups(), and adds the method is_transitive().  Note that the optional GAP database is *not* required.

Timings before the patch:


```
sage: G = SymmetricGroup(6)
sage: time cl = G.conjugacy_classes_subgroups()
CPU times: user 151.62 s, sys: 16.75 s, total: 168.37 s
Wall time: 175.53
```


and after:


```
sage: G = SymmetricGroup(6)
sage: time cl = G.conjugacy_classes_subgroups()
CPU times: user 0.54 s, sys: 0.09 s, total: 0.63 s
Wall time: 1.35
```




---

archive/issue_comments_007309.json:
```json
{
    "body": "Is this based on 3.0? I am getting aborted when I try to hg_sage.apply it.",
    "created_at": "2008-04-24T23:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7309",
    "user": "https://github.com/wdjoyner"
}
```

Is this based on 3.0? I am getting aborted when I try to hg_sage.apply it.



---

archive/issue_comments_007310.json:
```json
{
    "body": "Yes, it's based on 3.0, with no other patches around.",
    "created_at": "2008-04-24T23:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7310",
    "user": "https://github.com/aghitza"
}
```

Yes, it's based on 3.0, with no other patches around.



---

archive/issue_comments_007311.json:
```json
{
    "body": "Thanks - I got it applied now. Will be running test, etc on it tonight.",
    "created_at": "2008-04-24T23:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7311",
    "user": "https://github.com/wdjoyner"
}
```

Thanks - I got it applied now. Will be running test, etc on it tonight.



---

archive/issue_comments_007312.json:
```json
{
    "body": "Looks like a great patch, adding functionality, fixing a bug and correcting some typos in the permgp.py docstrings. Passes sage -testall on an ubuntu 7.10amd64 machine and an intel macbook running OS10.4.",
    "created_at": "2008-04-25T02:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7312",
    "user": "https://github.com/wdjoyner"
}
```

Looks like a great patch, adding functionality, fixing a bug and correcting some typos in the permgp.py docstrings. Passes sage -testall on an ubuntu 7.10amd64 machine and an intel macbook running OS10.4.



---

archive/issue_events_001319.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-25T03:05:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1187#event-1319"
}
```



---

archive/issue_comments_007313.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-25T03:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7313",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007314.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha0",
    "created_at": "2008-04-25T03:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1187",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1187#issuecomment-7314",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha0
