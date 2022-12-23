# Issue 3104: pbori.pyx: Make some doctest long since it uses a lot of RAM

Issue created by migration from https://trac.sagemath.org/ticket/3104

Original creator: mabshoff

Original creation time: 2008-05-05 12:16:16

Assignee: failure

CC:  polybori


```
[13:32] <wstein> Is there a ticket up for pbori.pyx not passing?
[13:32] <mabshoff> nope.
[13:33] <wstein> I propose that we put a --long in there to mean "need more ram".
[13:33] <mabshoff> You mean because it uses so much RAM?
[13:33] <mabshoff> yes
[13:33] <wstein> Yes.
[13:33] <wstein> --long meaning "--big" or something.
[13:33] <mabshoff> :)
[13:33] <wstein> It's annoying that pbori.pyx fails on so many of my test machines.
[13:33] <mabshoff> yep
[13:34] <mabshoff> I usually just ignore pbori.pyx failures, which is somewhat dangerous.
[13:34] <mabshoff> fixed
[13:34] <wstein> exactly.
[13:34] <wstein> Can you make a ticket?
[13:34] <mabshoff> sure
```



---

Attachment


---

Comment by mabshoff created at 2008-05-05 15:46:55

Patch looks good to me. I will do some testing to see how much less RAM we need with the patch applied.

Cheers,

Michael


---

Comment by malb created at 2008-05-05 19:19:58

I don't think that this strategy is right: If simple substitution takes too much RAM this is a serious bug not just something to be dealt with by adding `#long`.


---

Comment by mabshoff created at 2008-05-05 19:23:39

There are know memory leaks in this code in the order of 0.5GB in PolyBoRi. Making those doctests long will avoid people hitting the issue. I normally run *every* doctest as long, so the test coverage is still there. It is certainly a workaround until we fix the real issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-05 21:34:01

Hi Martin,

after discussing the issue with William in IRC: How about first upgrading to the PolyBoRi 0.4 release that Alexander just mentioned, check out the result with valdring. If there still is a large memory leak we apply this patch, open a new ticket to fix the memory leak and then revert the longs once the leaks are plugged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-21 13:21:14

Changing assignee from failure to mabshoff.


---

Comment by mabshoff created at 2008-05-21 13:21:14

Because this continues to be a problem with 3.0.2.alpha1 we will apply this patch to 3.0.2. Once #3264 has been merged [the upgrade to PolyBoRi 0.4] we will revisit the issue. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-21 13:21:14

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-21 13:23:01

Resolution: fixed


---

Comment by mabshoff created at 2008-05-21 13:23:01

Merged in Sage 3.0.2.rc0
