# Issue 5507: fix sage-sage script

Issue created by migration from Trac.

Original creator: dangrayson

Original creation time: 2009-03-13 03:04:47

Assignee: was

Keywords: sage-sage

I think there is a superfluous "shift" in the "sage-sage" script, because this works:

    $ sage -sh -c -c "echo hi there"

    Starting subshell with Sage environment variables set.
    Be sure to exit when you are done and do not do anything
    with other copies of Sage!

    Bypassing shell configuration files ...

    hi there
    Exited Sage subshell.

but this doesn't:

    $ sage -sh -c "echo hi there"

    Starting subshell with Sage environment variables set.
    Be sure to exit when you are done and do not do anything
    with other copies of Sage!

    Bypassing shell configuration files ...

    bash: echo hi there: No such file or directory
    Exited Sage subshell.


--

$ sage --version
| Sage Version 3.2.2, Release Date: 2008-12-18                       |


---

Comment by ddrake created at 2009-09-28 23:17:35

The patch at #4644 fixes this problem, according to this thread: http://groups.google.com/group/sage-devel/browse_thread/thread/384d4fe7dabb722c/


---

Comment by mvngu created at 2010-02-02 06:55:11

Resolution: fixed


---

Comment by mvngu created at 2010-02-02 06:55:11

With Sage 4.3.2.alpha1, I get:

```
[mvngu`@`mod sage-4.3.2.alpha1]$ ./sage -version
* Warning: this is a prerelease version, and it may be unstable.     *
[mvngu`@`mod sage-4.3.2.alpha1]$ ./sage -sh -c -c "echo hi there"
| Sage Version 4.3.2.alpha1, Release Date: 2010-01-31                |
Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

hi there
Exited Sage subshell.
[mvngu`@`mod sage-4.3.2.alpha1]$ ./sage -sh -c "echo hi there"

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

hi there
Exited Sage subshell.
```

I'm closing this ticket as fixed by #4644.
