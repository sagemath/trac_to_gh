# Issue 770: [with patch] Bad behaviour when Ctrl-C hit while running an expect interface

archive/issues_000770.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere are two different types of bad behaviour, and which one occurs seems random.\n\nOne case is lost synchronization with the slave:\n\n```\nsage: gp.eval('factor(2^997-1)')\n[CTRL-C]\nInterrupting GP/PARI interpreter...\nInterrupting GP/PARI interpreter...\n---------------------------------------------------------------------------\n<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)\n...\n<type 'exceptions.KeyboardInterrupt'>: Ctrl-c pressed while running GP/PARI interpreter\nsage: gp.eval('factor(2^997-1)')\n[CTRL-C]\n'factor(2^997-1)'\nsage: gp.eval('factor(2^997-1)')\n[CTRL-C]\n''\n```\nAfter this third time, synchronization is regained.\n\nThe second type of bad behaviour is an apparent \"hang\"\n\n```\nsage: gp.eval('factor(2^997-1)')\n[CTRL-C]\nInterrupting GP/PARI interpreter...\nInterrupting GP/PARI interpreter...\n[loops until CTRL-C hit again]\n```\nThe traceback shows that expect is waiting for a prompt, so this is again a synchronization problem except some timing issues make it behave differently.\n\nIn both cases the problem is the same, namely `Expect._keyboard_interrupt()` is being called twice when it should only be called once.\n\nIn fact, there are two nested `try` blocks both catching `KeyboardInterrupt` and running `_keyboard_interrupt()`. Since the latter raises `KeyboardInterrupt`, it ends up executed twice.\n\nThe proposed solution is to remove the outer catch for `KeyboardInterrupt`, which happens in `expect.eval`, and leave this error handling to `expect._eval_line`.\n\nAmong all the derived classes of `Expect` in `sage/interfaces` directory, the only one that seems to redefine `Expect.eval` in a not \"default-to-base-class\" way is `Lisp` in `lisp.py`, which should also be fixed. AFAICT, the other classes should be ok, but note that I only tested `Gp` as above: *I didn't test `Lisp` class either with the allegedly broken code nor with the fix!!*\n\nThis issue is similar (but really unrelated) to #710.\n\nA patch is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/770\n\n",
    "closed_at": "2007-10-04T14:41:50Z",
    "created_at": "2007-10-01T05:31:35Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "[with patch] Bad behaviour when Ctrl-C hit while running an expect interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/770",
    "user": "https://github.com/tornaria"
}
```
Assignee: @williamstein

There are two different types of bad behaviour, and which one occurs seems random.

One case is lost synchronization with the slave:

```
sage: gp.eval('factor(2^997-1)')
[CTRL-C]
Interrupting GP/PARI interpreter...
Interrupting GP/PARI interpreter...
---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)
...
<type 'exceptions.KeyboardInterrupt'>: Ctrl-c pressed while running GP/PARI interpreter
sage: gp.eval('factor(2^997-1)')
[CTRL-C]
'factor(2^997-1)'
sage: gp.eval('factor(2^997-1)')
[CTRL-C]
''
```
After this third time, synchronization is regained.

The second type of bad behaviour is an apparent "hang"

```
sage: gp.eval('factor(2^997-1)')
[CTRL-C]
Interrupting GP/PARI interpreter...
Interrupting GP/PARI interpreter...
[loops until CTRL-C hit again]
```
The traceback shows that expect is waiting for a prompt, so this is again a synchronization problem except some timing issues make it behave differently.

In both cases the problem is the same, namely `Expect._keyboard_interrupt()` is being called twice when it should only be called once.

In fact, there are two nested `try` blocks both catching `KeyboardInterrupt` and running `_keyboard_interrupt()`. Since the latter raises `KeyboardInterrupt`, it ends up executed twice.

The proposed solution is to remove the outer catch for `KeyboardInterrupt`, which happens in `expect.eval`, and leave this error handling to `expect._eval_line`.

Among all the derived classes of `Expect` in `sage/interfaces` directory, the only one that seems to redefine `Expect.eval` in a not "default-to-base-class" way is `Lisp` in `lisp.py`, which should also be fixed. AFAICT, the other classes should be ok, but note that I only tested `Gp` as above: *I didn't test `Lisp` class either with the allegedly broken code nor with the fix!!*

This issue is similar (but really unrelated) to #710.

A patch is attached.

Issue created by migration from https://trac.sagemath.org/ticket/770





---

archive/issue_comments_004561.json:
```json
{
    "body": "Proposed patch to fix this issue",
    "created_at": "2007-10-01T05:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/770#issuecomment-4561",
    "user": "https://github.com/tornaria"
}
```

Proposed patch to fix this issue



---

archive/issue_comments_004562.json:
```json
{
    "body": "Attachment [patch.770](tarball://root/attachments/some-uuid/ticket770/patch.770) by mabshoff created at 2007-10-01 11:51:23",
    "created_at": "2007-10-01T11:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/770#issuecomment-4562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [patch.770](tarball://root/attachments/some-uuid/ticket770/patch.770) by mabshoff created at 2007-10-01 11:51:23



---

archive/issue_events_002118.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-01T11:51:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/770",
    "milestone": "sage-2.8.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/770#event-2118"
}
```



---

archive/issue_events_002119.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T14:41:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/770",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/770#event-2119"
}
```



---

archive/issue_comments_004563.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T14:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/770",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/770#issuecomment-4563",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
