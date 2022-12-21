# Issue 4646: Create Sage 3.2.1 release notes

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-28 23:08:43

Assignee: mabshoff

CC:  mvngu

As the summary says :)

Cheers,

Michael


---

Attachment

Draft 1 is based in 3.2.1.rc1, so some things will likely be added in 3.2.1.final


---

Comment by mabshoff created at 2008-12-01 11:12:52

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-01 11:12:52

Hi Minh,

here is draft 1. As mentioned there is likely some change log to be added for 3.2.1.final. Some of the data like release dates, final tally of tickets and so on still need to be filled in once we get closed to the real 3.2.1.

If you got any fixes please post a patch against draft 1. 

Cheers,

Michael


---

Comment by mvngu created at 2008-12-01 22:46:45

Changing keywords from "" to "release note".


---

Comment by mvngu created at 2008-12-01 22:46:45

Replying to [comment:1 mabshoff]:
> Hi Minh,
> 
> here is draft 1. As mentioned there is likely some change log to be added for 3.2.1.final. Some of the data like release dates, final tally of tickets and so on still need to be filled in once we get closed to the real 3.2.1.


The first draft is good. I'm planning to edit notes for the release tour of Sage 3.2.1, and hopefully have some high-level stuff to patch against your first draft, before Sage 3.2.1 is released. So I can definitely give your patch a positive review as it now stands.


---

Attachment

the only change draft1->draft2 was the correct assignment of credit for #4646. Two more small fixes are needed:

 * now the list of names is no longer alphabetically sorted
 * It should say "3.2.1" in known issues instead of "3.2"

draft3 coming up.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-12-02 13:09:33


```
[04:23am] mabshoff|zzzz: craigcitro, mhansen: the problem is that we cleanup up which flags to consider.
[04:24am] mhansen: I don't understand why this should affect a build from source.
[04:36am] gabkdlly joined the chat room.
[04:53am] mabshoff|zzzz: on sage.math it is likely an upgrade.
[04:53am] mabshoff|zzzz: So the flags file with the old flags already existed.
[04:54am] mabshoff|zzzz: I am not sure it is worth working around that since the
problem only happens when upgrading from 3.2, so in a couple releases this will 
become a non-issue.
[04:54am] mhansen: I got this on my own box too.
[04:56am] gabkdlly left the chat room. ("Leaving.")
[05:00am] mabshoff|zzzz: Did you upgrade?
[05:01am] mhansen: Yes
[05:01am] mabshoff|zz:
[05:01am] mabshoff|zz: delete $SAGE_LOCAL/lib/sage-flags.txt and the problem is gone
[05:02am] mhansen: Yes, I know.  I fixed it on my box and sage.math.
[05:02am] mabshoff|zz: thanks
[05:02am] mabshoff|zz: It is an annoyance and I think we shouldn't add a workaround to the detection code.
[05:03am] mabshoff|zz: The people who can upgrade will be able to fix it themselves, but we might want to add an FAQ entry
[05:03am] mabshoff|zz: Going back to catch a few more z 
[05:03am] mhansen: Or send a preemptive email to sage-devel.
[05:03am] mabshoff|zz: +1
[05:04am] mabshoff|zz: knock yourself out 
[05:04am] mabshoff|zz: We might as well add  a warning to the release notes to "KNOWN ISSUES".
[05:04am] mhansen: Too busy with #3950
[05:04am] mabshoff|zz: I.e feel free to post a patch at #4646
[05:05am] mabshoff|zz: Ok, I will do it then.
```



---

Comment by mabshoff created at 2008-12-07 03:42:07

The release notes have been posted.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-07 03:42:07

Resolution: fixed
