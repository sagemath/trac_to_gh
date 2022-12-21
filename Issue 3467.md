# Issue 3467: [with patch, needs review] implements @parallel decorator using dsage

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-06-19 02:11:52

Assignee: tbd

Here's how to use it:

sage: d = dsage.start_all()
Spawned twistd -d /Users/yqiang/.sage/dsage --pidfile=server.pid --logfile=/Users/yqiang/.sage/dsage/server.log -y dsage_server.tac (pid = 73563)

Spawned python /Users/yqiang/Software/sage-3.0.3.rc0/local/bin/dsage_worker.py -s localhost -p 8083 -u yqiang -w 2 --poll 1.0 -l 0 -f /Users/yqiang/.sage/dsage/worker.log --privkey=/Users/yqiang/.sage/dsage/dsage_key --pubkey=/Users/yqiang/.sage/dsage/dsage_key.pub --priority=20 --ssl --noblock (pid = 73571)

sage: P = parallel(p_iter = d.parallel_iter)
sage: `@`P
....: def MS1(N,k):
....:     return ModularSymbols(N,k,sign=1).decomposition(10)[0]
....: 
sage: time v = MS1([(250,2), (11,2), (37,2)])


---

Comment by yi created at 2008-06-19 02:12:23

Changing assignee from tbd to yi.


---

Comment by yi created at 2008-06-19 02:12:23

Changing component from algebra to dsage.


---

Attachment


---

Attachment

new patch with doctests.


---

Attachment

Ok, doctests are added.


---

Comment by yi created at 2008-06-19 04:07:28

Replying to [comment:3 yi]:
> Ok, doctests are added.
Also, be sure to remove nodoctest.py in dsage/interface. For some reason MQ doesn't pick up that I removed the file.


---

Comment by mhansen created at 2008-06-19 21:24:37

All tests pass AFTER removing nodoctest.py from sage/dsage/interface .  Also, you should explicitly note the patches that this depends on (if any).


---

Attachment


---

Comment by yi created at 2008-06-19 21:30:31

dsage_interface.4.patch uses git style diffs which will remove nodoctest.py


---

Comment by mabshoff created at 2008-06-23 05:58:54

Yi,

could you please clarify which patches should be applied in which order? This likely also depends on some other patches to be applied first I assume in which case it would be great to note that on the ticket first, too.

Cheers,

Michael


---

Comment by yi created at 2008-06-23 20:00:17

Please apply dsage_interface.4.patch. It is the only one you need. Also, this patch depends on getting #3458 merged in.


---

Comment by mabshoff created at 2008-06-26 04:29:30

Merged dsage_interface.3.patch in Sage 3.0.4.alpha1. I also removed the nodoctest manually.


---

Comment by mabshoff created at 2008-06-26 04:29:30

Resolution: fixed
