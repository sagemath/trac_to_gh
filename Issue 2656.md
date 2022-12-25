# Issue 2656: "sage -hg" does not handle quoting correctly

archive/issues_002656.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf you use \"sage -hg\" with arguments containing spaces, like:\n\n```\n  sage -hg commit -m \"This is my great new code.\"\n```\nthen the argument gets split up, so Mercurial sees something more like\n\n```\n  hg commit -m This is my great new code.\n```\n(and tries to check in files named is,my,great,new,code., with a commit message of \"This\").\n\nIssue created by migration from https://trac.sagemath.org/ticket/2656\n\n",
    "created_at": "2008-03-23T17:40:40Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"sage -hg\" does not handle quoting correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2656",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

If you use "sage -hg" with arguments containing spaces, like:

```
  sage -hg commit -m "This is my great new code."
```
then the argument gets split up, so Mercurial sees something more like

```
  hg commit -m This is my great new code.
```
(and tries to check in files named is,my,great,new,code., with a commit message of "This").

Issue created by migration from https://trac.sagemath.org/ticket/2656





---

archive/issue_comments_018246.json:
```json
{
    "body": "We need to escape the '\"' (and probably some other characters):\n\n```\n[mabshoff@localhost ~]$ ./foo.bash commit -m \"This is my great new code.\"\ncommit -m This is my great new code.\n[mabshoff@localhost ~]$ ./foo.bash commit -m \\\"This is my great new code.\\\"\ncommit -m \"This is my great new code.\"\n```\nwhere foo.bash is\n\n```/bin/bash\necho \"$@\"\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T19:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2656#issuecomment-18246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We need to escape the '"' (and probably some other characters):

```
[mabshoff@localhost ~]$ ./foo.bash commit -m "This is my great new code."
commit -m This is my great new code.
[mabshoff@localhost ~]$ ./foo.bash commit -m \"This is my great new code.\"
commit -m "This is my great new code."
```
where foo.bash is

```/bin/bash
echo "$@"
```

Cheers,

Michael



---

archive/issue_events_006217.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-10-10T21:09:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2656",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2656#event-6217"
}
```



---

archive/issue_comments_018247.json:
```json
{
    "body": "Seems to be fixed in sage-4.6.",
    "created_at": "2010-10-10T21:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2656#issuecomment-18247",
    "user": "https://github.com/jdemeyer"
}
```

Seems to be fixed in sage-4.6.



---

archive/issue_comments_018248.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-10T21:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2656#issuecomment-18248",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_006218.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-22T09:32:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2656",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2656#event-6218"
}
```



---

archive/issue_comments_018249.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-10-22T09:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2656#issuecomment-18249",
    "user": "https://github.com/qed777"
}
```

Resolution: worksforme
