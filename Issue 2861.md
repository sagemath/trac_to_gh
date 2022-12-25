# Issue 2861: scripts do not exit with correct exit code when sys.exit() is used

archive/issues_002861.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf I call `sys.exit()` from a Sage script, the script exits but not with the correct exit code. For example, the script\n\n```\nimport sys\n\nprint 'exiting!'\nsys.exit(1)\n```\n\nexits with exit code 0 when run from Sage:\n\n```\n$ sage exitcode.sage \nexiting!\n1\n$ echo $?\n0\n```\n\n(the 1 gets printed because the preparser turns it into a Sage integer, and Python prints out anything except Python integers.) But the same script works properly when run from Python:\n\n```\n$ python exitcode.sage\nexiting!\n$ echo $?\n1\n```\n\nI don't know if this is Sage or IPython behavior, but having this work would be really useful.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2861\n\n",
    "created_at": "2008-04-09T06:42:30Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "scripts do not exit with correct exit code when sys.exit() is used",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2861",
    "user": "https://github.com/dandrake"
}
```
Assignee: @williamstein

If I call `sys.exit()` from a Sage script, the script exits but not with the correct exit code. For example, the script

```
import sys

print 'exiting!'
sys.exit(1)
```

exits with exit code 0 when run from Sage:

```
$ sage exitcode.sage 
exiting!
1
$ echo $?
0
```

(the 1 gets printed because the preparser turns it into a Sage integer, and Python prints out anything except Python integers.) But the same script works properly when run from Python:

```
$ python exitcode.sage
exiting!
$ echo $?
1
```

I don't know if this is Sage or IPython behavior, but having this work would be really useful.


Issue created by migration from https://trac.sagemath.org/ticket/2861





---

archive/issue_events_006548.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-09T09:30:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2861#event-6548"
}
```



---

archive/issue_comments_019589.json:
```json
{
    "body": "Attachment [trac_2861-scripts.patch](tarball://root/attachments/some-uuid/ticket2861/trac_2861-scripts.patch) by @williamstein created at 2009-01-24 15:08:00",
    "created_at": "2009-01-24T15:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2861#issuecomment-19589",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_2861-scripts.patch](tarball://root/attachments/some-uuid/ticket2861/trac_2861-scripts.patch) by @williamstein created at 2009-01-24 15:08:00



---

archive/issue_comments_019590.json:
```json
{
    "body": "+1\n\nwas showed me this patch working in all the permutations of inputs... Looks good to me.",
    "created_at": "2009-01-24T15:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2861#issuecomment-19590",
    "user": "https://github.com/rlmill"
}
```

+1

was showed me this patch working in all the permutations of inputs... Looks good to me.



---

archive/issue_comments_019591.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T22:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2861#issuecomment-19591",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006549.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T22:47:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2861#event-6549"
}
```



---

archive/issue_events_006550.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T22:47:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2861#event-6550"
}
```



---

archive/issue_events_006551.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T22:47:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2861#event-6551"
}
```



---

archive/issue_comments_019592.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T22:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2861#issuecomment-19592",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_019593.json:
```json
{
    "body": "I was going to reopen this ticket, but instead I'll leave this comment as warning to anyone else trying to use this:\n\nIf you do `sys.exit(0)` in a Sage script, because of preparsing, you effectively get `sys.exit(Integer(0))`, which results in the script exiting with code 1! This is not what anyone would expect! This is because of [how sys.exit works](http://docs.python.org/library/sys.html#sys.exit) when given non-Python-integer arguments. To make sure that you get the desired behavior, use `int` inside the call to get a Python integer: `sys.exit(int(2))` or whatever.",
    "created_at": "2009-04-21T01:48:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2861",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2861#issuecomment-19593",
    "user": "https://github.com/dandrake"
}
```

I was going to reopen this ticket, but instead I'll leave this comment as warning to anyone else trying to use this:

If you do `sys.exit(0)` in a Sage script, because of preparsing, you effectively get `sys.exit(Integer(0))`, which results in the script exiting with code 1! This is not what anyone would expect! This is because of [how sys.exit works](http://docs.python.org/library/sys.html#sys.exit) when given non-Python-integer arguments. To make sure that you get the desired behavior, use `int` inside the call to get a Python integer: `sys.exit(int(2))` or whatever.
