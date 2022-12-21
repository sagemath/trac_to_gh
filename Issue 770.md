# Issue 770: Bad behaviour when Ctrl-C hit while running an expect interface

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2007-10-01 05:31:35

Assignee: was

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

Among all the derived classes of `Expect` in `sage/interfaces` directory, the only one that seems to redefine `Expect.eval` in a not "default-to-base-class" way is `Lisp` in `lisp.py`, which should also be fixed. AFAICT, the other classes should be ok, but note that I only tested `Gp` as above: _I didn't test `Lisp` class either with the allegedly broken code nor with the fix!!_

This issue is similar (but really unrelated) to #710.

A patch is attached.


---

Comment by tornaria created at 2007-10-01 05:33:13

Proposed patch to fix this issue


---

Attachment


---

Comment by was created at 2007-10-04 14:41:50

Resolution: fixed
