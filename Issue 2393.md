# Issue 2393: the version of mercurial shipped with sage does not include the queue extension

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-03-05 06:20:44

Assignee: mabshoff

It is very annoying when trying to run hg under a Sage shell.


---

Comment by cwitty created at 2008-03-05 16:55:02

Actually, Sage's mercurial does include the queue extension; it's just not enabled by default.

You can enable it by adding these lines to $HOME/.hgrc:

```
[extensions]
# patch queues for mercurial
# add the 'q*' commands
hgext.mq=
```


Debian enables the queue extension (along with many others) for its version of mercurial, using configuration files in /etc/mercurial.  I patched Sage's mercurial spkg to not look in /etc/mercurial, because Debian's configuration enabled extensions that were not included in Sage's mercurial, leading to annoying (although harmless) warning messages on every mercurial command.

So this bug could be resolved by:

1) tell everybody who cares to add the above lines to their .hgrc

2) patch Sage's mercurial to look in $SAGE_LOCAL/etc/mercurial, and install a default configuration there that enables queues


---

Comment by mhansen created at 2008-03-05 22:48:05

Aha, I had I thought I enabled it in .hgrc, but it turns out it was just in /etc/mercurial.  Thanks!


---

Comment by was created at 2008-03-05 22:59:07

> 2) patch Sage's mercurial to look in 
> $SAGE_LOCAL/etc/mercurial, and install a default 
> configuration there that enables queues

I like this suggestion, since "1) tell everybody ..." is always doomed to failure and frustration.


---

Comment by mabshoff created at 2008-10-30 08:45:39


```
[01:39am] mabshoff: mhansen: isn't the que extension now part of hg 1.0.x?
[01:40am] mabshoff: I.e. we can close #2393 as fixed.
[01:40am] ddrake: mabshoff: queue is now standard in hg
[01:40am] mabshoff: excellent
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-30 08:45:39

Resolution: fixed
