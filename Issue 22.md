# Issue 22: 32/64/32-bit building switch

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:21:52

Assignee: somebody

Should there be something to keep people from building on 32-bit then 64-bit then 32-bit.



---

Comment by was created at 2007-08-19 08:14:34


```
[01:10] <william> the problem was doing something like "sage -br" on both a 32-bit and 64-bit machine but
[01:10] <william> with a shared filesystem.
[01:10] <mabshoff> Ah, that makes sense.
[01:10] <william> I.e., when you build sage for one architecture, maybe you shouldn't be allowed to
[01:10] <william> do "sage -br" or "sage -i" if the architectrue doesn't match.
[01:11] <mabshoff> okay,
[01:11] <william> or something like that.
```



---

Comment by was created at 2007-09-18 17:11:52


```
[10:01] <wstein> regarding #22 the idea is that people might do "sage -br" on one machine, then login to another machine that
[10:02] <wstein> nsf mounts the same directory, and muck things up.
[10:02] <wstein> We should cache "uname -p" in SAGE_ROOT, and if it changes not allow "sage -br" unless the user
[10:02] <wstein> (or sage -i) or sage -upgrade, unless the user manually deletes the file.
[10:03] <wstein> Thoughts?
```



---

Comment by mabshoff created at 2007-11-26 01:12:02

Changing assignee from somebody to mabshoff.


---

Comment by mabshoff created at 2007-11-26 01:12:02

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-21 23:52:02

Changing assignee from mabshoff to gfurnish.


---

Comment by gfurnish created at 2008-03-21 23:52:02

Changing status from assigned to new.


---

Comment by gfurnish created at 2008-03-21 23:53:04

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-23 12:09:24

Fixed in #1261 (PBuild)


---

Comment by gfurnish created at 2008-04-04 19:55:36

Changing component from basic arithmetic to build.


---

Attachment


---

Comment by mabshoff created at 2009-01-16 17:30:08

Changing status from assigned to new.


---

Comment by mabshoff created at 2009-01-16 17:30:08

Changing assignee from gfurnish to mabshoff.


---

Comment by mabshoff created at 2009-01-16 17:30:15

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-16 17:46:35

Mhh, looking at the complete ticket history this patch does not cover all what needs to be fixed on this ticket. I will post a patch on top that also fixes this issue.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-16 17:50:15

Unfortunately the trick William suggested does not work everywhere, i.e. even on the latest stable Debian release this happens:

```
mabshoff`@`modular:~$ uname -p
unknown
```

From *man uname* on that box:

```
       -p, --processor
              print the processor type or "unknown"
```


So we might want to make that part of the ticket a followup ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-16 18:03:39

Having thought about this and played around a little with uname it seems that it will not work and is not fine grained enough anyway. I would suggest to do write a small C program that identifies the following:

 * mode: i.e. 32, 64 bit
 * os: linux, osx, solaris, freebsd, cygwin
 * release: this would be the distribution on Linux, OSX 10.4/10.5, Solaris 10/Solaris 11/Opensolaris and so on

The way we can properly identify the build platform and decide more intelligently if we issue a warning, i.e running the Fedora 10 build on a Fedora 9 box should abort since it doesn't work. The test should be wrapped in a shell script since the binary will obviously only run on a subset of arches, i.e. if the binary fails to run we just about and print a canned warning together with a config info saved as text that is created when building the binary.

This is enough a task to split it off to a new ticket. I have some basic code that does some of the above already for OSX since I need this kind of code while cleaning up the build system.

Thoughts?

Cheers,

Michael


---

Comment by rlm created at 2009-01-22 17:14:47

This is a "perfect patch."

... ;-)


---

Comment by mabshoff created at 2009-01-23 00:34:46

Merged in Sage 3.3.alpha1.

Note that the remaining issue from this ticket has been moved to #5062.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 00:34:46

Resolution: fixed
