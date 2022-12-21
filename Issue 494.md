# Issue 494: local/bin/sage-env uses 'bashism'

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-26 19:54:51

Assignee: was

Hello,

local/bin/sage-env shipped with Sage 2.8.2 is officially a sh shell script. So it should run flawlessly with a tcsh. But

```
[mabshoff`@`m940 sage-2.8.2]# /bin/tcsh local/bin/sage-env
SAVEDIR=/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2: Command not found.
if: Expression Syntax.
```


This was originally mentioned to me "dropdrive" in #sage-devel

While we are at it: all spkg-install seem to use /bin/bash as shebang. While it is very uncommen to find a Unixy system these days without a bash it might still happen. We should consider fixing those scripts, too, or make it a requirement that users have a bash installed.

Cheers,

Michael


---

Comment by cwitty created at 2007-10-07 19:11:21

The first half of this bug is invalid as stated.  tcsh is not supposed to be sh-compatible, so it's not surprising that it can't source sage-env.


---

Comment by mabshoff created at 2008-02-17 19:54:25

The second part of the ticket, i.e. to use `/use/bin/env bash` is now #1638, so I am closing this ticket as invalid shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-17 19:54:43

Resolution: invalid
