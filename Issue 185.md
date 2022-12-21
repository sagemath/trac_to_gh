# Issue 185: Firefox + Xorg (Linux) take way too much cputime while waiting for results from the notebook server

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2006-12-18 00:00:39

Assignee: boothby

On my P4 so as my P3 system whenever I undertake a long calculation using the notebook the polling for results takes way too much cputime. I guess it's caused by a very high polling frequency. top output follows:

```
 XXXX martin    25   0  125m  36m 9.8m R   80  2.4   1:13.44 python
 XXXX root      16   0  285m 176m 2860 R   36 11.6 204:18.81 Xorg
 XXXX martin    15   0 95860  43m  19m S   30  2.8   3:50.28 firefox-bin
```

How to reproduce: Calculate something difficult and monitor top.


---

Comment by was created at 2007-01-19 09:41:29

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-09-10 02:37:31

Please investigate the issue. The orignial milestone was 1.8 so it has been a while.

Cheers,

Michael


---

Comment by malb created at 2008-01-17 12:50:12

The issues has not been resolved, an truncated exponential backoff was discussed here:

http://groups.google.com/group/sage-devel/browse_thread/thread/f8f76d438163e546/110cf0c908689635?


---

Comment by boothby created at 2008-03-16 21:22:44

I've implemented something like exponential falloff.  Polling slows down gradually; after about 30 seconds, poll delay is 5 seconds.


---

Attachment


---

Comment by was created at 2008-03-17 04:20:50

It works fine for me; the code makes sense.


---

Comment by mabshoff created at 2008-03-17 04:24:47

Merged in Sage 2.10.4.final


---

Comment by mabshoff created at 2008-03-17 04:24:47

Resolution: fixed
