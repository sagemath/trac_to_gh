# Issue 439: Interace with remote programs allowing for as many hops as needed

Issue created by migration from https://trac.sagemath.org/ticket/439

Original creator: pdehaye

Original creation time: 2007-08-18 18:02:27

Assignee: pdehaye

see
http://groups.google.com/group/sage-support/browse_thread/thread/b7215f69359ff4c2



---

Comment by pdehaye created at 2007-08-18 21:52:09

Changing status from new to assigned.


---

Attachment

Just posted a patch. Issues that still need to be resolved:
 * could do better when converting with _sage_() remote objects
 * the _remote_tmpfile is defaulted to "/tmp", I am not sure that's a good idea, and if we shouldn't just return an error if (server_tmpdir is None) and not (server is None)


---

Comment by pdehaye created at 2007-08-19 23:19:06

also, removed expect.tmp as this was confusing:
there ought to be two different temporary files in expect.py. one would be _local_tmpfile and interact with sage/python and the other one _remote_tmpfile and interact with the remote CAS session. 
allowing for something named tmp in expect.py is confusing as people who program more interfaces don t tend to think of the distinction needed when doing things remotely, and end up using the same file for both (without scp'ing one to the other if is_remote())


---

Comment by pdehaye created at 2007-08-20 19:39:27

Trac #160, which will be included before this, might need to be revisited.


---

Comment by was created at 2007-08-23 01:47:01

Paul has implemented this, sent me a patch, and I've applied it.


---

Comment by was created at 2007-08-23 01:47:01

Resolution: fixed
