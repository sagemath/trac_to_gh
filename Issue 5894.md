# Issue 5894: spkg/install shoud use #!/usr/bin/env bash

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-25 11:05:45

Assignee: mabshoff

On a rather minimal Ubuntu 8.04 system:

```
[03:52am] pamcd: ufff, thats almost what i have available
[03:52am] pamcd: ./install: 352: time: not found
<SNIP>
[03:56am] mabs: Ok, can you edit spkg/install ?
[03:56am] mabs: Change #!/bin/sh to #!/usr/bin/env bash and restart?
[03:57am] pamcd: ok, restarting
[03:58am] pamcd: what is that change for?
[03:58am] mabs: Well, it runs the shell script via bash instead of the default shell.
[03:58am] mabs: For most systems /bin/sh is in effect bash, but that has been changing.
[03:59am] pamcd: the default shell misses some needed functionallity?
[03:59am] mabs: On non-linux systems /bin/sh is often the original shell.
[03:59am] mabs: Well, it seems to not have a build in time command in your case.
[03:59am] pamcd: btw, it seems to have solved the problem: compiling
```



---

Comment by mabshoff created at 2009-04-25 11:06:38

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-15 14:34:10

Trivial to fix and a real bug, 4.0 material.

Cheers,

Michael


---

Comment by was created at 2009-05-28 06:42:05

Resolution: fixed
