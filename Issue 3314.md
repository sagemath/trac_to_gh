# Issue 3314: dsage.setup() add_default_client broken

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-05-27 05:43:21

Assignee: mabshoff

twisted changed it's conch interface and I forgot to toString the pubkey object in some instances. 


---

Attachment


---

Comment by mabshoff created at 2008-05-28 12:04:13

Changing component from Cygwin to dsage.


---

Comment by mabshoff created at 2008-05-28 12:04:13

Changing assignee from mabshoff to yi.


---

Comment by craigcitro created at 2008-06-15 21:48:35

Changing keywords from "" to "editor_gfurnish".


---

Comment by gfurnish created at 2008-06-16 20:31:26

DSage is completely broken in 3.0.2 and 3.0.3!!!!!  Make me some patches so that I can actually run dsage.


---

Comment by mabshoff created at 2008-06-16 21:50:15

DSage is not completely broken in Sage 3.0.2 with the patch applied and in 3.3.0.rc0. If you make claims like that you should back them up with details.

Cheers,

Michael


---

Comment by gfurnish created at 2008-06-16 22:15:48

If you do not have an existing known good .sage directory with existing dsage materials from some previous version (unknown), dsage is completely broken.


---

Comment by mabshoff created at 2008-06-17 00:15:27

Ok, the bug is the following *after* deleting the dsage directory in DOT_SAGE:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.3.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.3.rc0, Release Date: 2008-06-16                   |
| Type notebook() for the GUI, and license() for information.        |
sage: dsage.setup()
==================================================
Generating public/private key pair for authentication...
Your key will be stored in /home/mabshoff/.sage/dsage/dsage_key
Just hit enter when prompted for a passphrase
==================================================
<SNIP>
sage: dsage.start_all()
Spawned twistd -d /home/mabshoff/.sage/dsage --pidfile=server.pid --logfile=/home/mabshoff/.sage/dsage/server.log -y dsage_server.tac (pid = 26784)

Spawned python /scratch/mabshoff/release-cycle/sage-3.0.3.rc0/local/bin/dsage_worker.py -s localhost -p 8087 -u mabshoff -w 2 --poll 1.0 -l 0 -f /home/mabshoff/.sage/dsage/worker.log --privkey=/home/mabshoff/.sage/dsage/dsage_key --pubkey=/home/mabshoff/.sage/dsage/dsage_key.pub --priority=20 --ssl --noblock (pid = 26801)

Not connected.
sage: 
```


The DSage server log says:

```
2008-06-16 17:08:52-0700 [-] Log opened.
2008-06-16 17:08:52-0700 [-] twistd 8.0.1 (/scratch/mabshoff/release-cycle/sage-3.0.3.rc0/local/bin/python 2.5.2) starting up
2008-06-16 17:08:52-0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008-06-16 17:08:52-0700 [-] twisted.spread.pb.PBServerFactory starting on 8087
2008-06-16 17:08:52-0700 [-] Starting factory <twisted.spread.pb.PBServerFactory instance at 0x2b54f6e88998>
2008-06-16 17:08:52-0700 [-] twisted.web2.channel.http.HTTPFactory starting on 8088
2008-06-16 17:08:52-0700 [-] Starting factory <twisted.web2.channel.http.HTTPFactory instance at 0x2b54f6e88e60>
2008-06-16 17:08:52-0700 [Broker,1,127.0.0.1] <client:'mabshoff'> connected
2008-06-16 17:08:53-0700 [Broker,2,127.0.0.1] <unauthenticated_worker:'Anonymous'> connected
2008-06-16 17:12:03-0700 [Broker,1,127.0.0.1] <client:'mabshoff'> disconnected
2008-06-16 17:12:03-0700 [Broker,2,127.0.0.1] <unauthenticated_worker:'Anonymous'> disconnected
```



Cheers,

Michael


---

Comment by yi created at 2008-06-17 22:04:26

Michael, Gary, did you test this after applying the patch I posted?


---

Comment by yi created at 2008-06-17 23:00:50

Ok. I tried this with 3.0.3rc0 after applying both #3312 and #3314 and can't repro this.


---

Comment by was created at 2008-06-18 04:39:31

Resolution: fixed


---

Comment by mabshoff created at 2008-06-18 23:18:43

Merged in Sage 3.0.3.final
