# Issue 4644: No new prompt when doing a ./sage -sh

Issue created by migration from https://trac.sagemath.org/ticket/4644

Original creator: jsp

Original creation time: 2008-11-28 18:24:42

Assignee: was

We used to have:


```
[jaap@paix sage-3.1.1]$ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Sage subshell$ exit
exit
Exited Sage subshell.
[jaap@paix sage-3.1.1]$ 

```


But in sage-3.2:


```
[jaap@paix sage-3.2]$ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

[jaap@paix sage-3.2]$ 

```


I've been bitten by this once more!

Jaap





---

Comment by mabshoff created at 2008-11-28 18:31:20

Hi Jaap, 

this one should have gone to [sage-devel] since we need to find out what the bug is. Anmd having a discussion on the ticket sucks. But:

 * are you using bash as default login shell?
 * please post the output from sage-sage after changing "#!/usr/bin/env bash" to "#!/usr/bin/env bash -x"

Cheers,

Michael


---

Comment by jsp created at 2008-12-03 16:05:14

Ok, sorry. We had a discussion long time ago. You said you were bitten by this many times!

Due to #4512 mhansen:
Could we at least have a PS1 that includes the current directory? I always hated it when I was on a machine where "sage -sh" didn't use my existing PS1.


We now have the trouble of finding out which shell we use!


```
Exited Sage subshell.
[jaap@paix sage-3.2.1.rc0]$ vi local/bin/sage-sage
[jaap@paix sage-3.2.1.rc0]$ ./sage -sh
/usr/bin/env: bash -x: No such file or directory
[jaap@paix sage-3.2.1.rc0]$ which bash
/bin/bash
[jaap@paix sage-3.2.1.rc0]$ local/bin/sage-sage
/usr/bin/env: bash -x: No such file or directory
[jaap@paix sage-3.2.1.rc0]$ 

```


Jaap


---

Comment by jsp created at 2009-02-05 16:41:42

Maybe we can have a PS1 that is different and includes the current directory!

I've been bitten by this "defect" once more.

Jaap


---

Comment by jsp created at 2009-06-09 15:25:19

From sage-devel:


```
William Stein wrote:

> The justification for the existence of "./sage -sh" is that you can
> type "exit" to get out of that subshell, and all the Sage environment
> variables are no longer defined.  Also, on some systems "./sage -sh"
> changes the prompt as a reminder (it's a bug that it doesn't do this
> on all systems).
>
+1

This is http://trac.sagemath.org/sage_trac/ticket/4644
I opened 6 month ago.

We have to thank Mike Hansen and Craig Citro for this :)

http://trac.sagemath.org/sage_trac/ticket/4512

Mike:
> Could we at least have a PS1 that includes the current directory? I always hated it when I was on a machine where "sage -sh" didn't use my existing PS1.

Craig:
> Yeah, that would be very reasonable.

Jaap


```



---

Comment by ddrake created at 2009-09-28 23:15:17

There's a suggested solution to this problem: http://groups.google.com/group/sage-devel/browse_thread/thread/384d4fe7dabb722c/

I'll upload the patch from that thread in a moment.


---

Attachment


---

Comment by mhansen created at 2009-10-05 05:37:36

I think this seems good.

Note that the patch applies to the scripts repo.


---

Comment by was created at 2009-10-13 20:17:46

Resolution: fixed


---

Comment by was created at 2009-10-13 20:17:46

merged into sage-4.1.2.
