# Issue 6990: readline tab completion has an extra space appended

Issue created by migration from https://trac.sagemath.org/ticket/6990

Original creator: jason

Original creation time: 2009-09-22 18:09:11

Assignee: mabshoff

CC:  kcrisman

This is the same problem we had in #2469, which apparently again crops up with the upgrade to readline-6.0.

I get it with a fresh compile of 4.1.2.alpha2 on ubuntu 9.04.


---

Comment by jason created at 2009-09-22 18:36:53

This bug is documented here: http://bugs.python.org/issue5833

A nice patch is here: http://bugs.python.org/file14599/python-2.6-readline.patch

I'll make a new python spkg.


---

Comment by jason created at 2009-09-22 18:53:36

(that patch is from: http://bugs.python.org/issue5833)


---

Comment by jason created at 2009-09-22 19:07:05

My spkg is up


---

Comment by jason created at 2009-09-22 19:37:38

This spkg takes care of the problem for me.


---

Comment by mvngu created at 2009-09-22 19:39:39

Changing priority from major to blocker.


---

Comment by ddrake created at 2009-09-23 00:42:22

I tested the spkg (64-bit Ubuntu 9.04), and it does fix the problem. Couple other recommendations:

  * in SPKG.txt, delete Michael from maintainers, and fix the "cimmunity" typo just below that
  * in spkg-install, should we have "set -e"? I recall some discussion about that, so that failed builds immediately stop.

I'll try the spkg on some other platforms.


---

Comment by mvngu created at 2009-09-27 03:45:33

See my report at #6849. Positive review from me, pending the fixes suggested by ddrake. If ddrake's happy, I'm happy.



ddrake --- Any comments on this ticket?


---

Comment by jhpalmieri created at 2009-09-27 16:05:53

Seems to work on OS X 10.5 (32 and 64 bit).


---

Comment by ddrake created at 2009-09-28 01:55:43

I'm trying to build 4.1.2.alpha4 on Arch amd64, and with the new readline/python package, I'm getting "undefined symbols". It compiles readline just fine, and then it starts working on the sqlite spkg, and immediately bombs out with:

```
/bin/bash: symbol lookup error: $SAGE_ROOT/local/lib/libreadline.so.6: undefined symbol: PC
```

I tried skipped sqlite (by touching spkg/installed/sqlite-3.6.17) and when it started working on libgpg_error, it immediately failed with the same error.

It looks like the shell is getting confused and picking up the wrong libreadline, probably because Arch includes readline 6. On other systems, maybe this isn't a problem because the shell looks for a different readline...I guess?

On Ubuntu Karmic (9.10) amd64, I don't see this error, even though it does use readline 6.

(Apologies if this comment should be on the readline spkg ticket, or should be in a new ticket...)


---

Comment by mvngu created at 2009-09-28 06:13:01

Replying to [comment:10 ddrake]:
> I'm trying to build 4.1.2.alpha4 on Arch amd64, and with the new readline/python package, I'm getting "undefined symbols". It compiles readline just fine, and then it starts working on the sqlite spkg, and immediately bombs out with:

```
/bin/bash: symbol lookup error: $SAGE_ROOT/local/lib/libreadline.so.6: undefined symbol: PC
```

> I tried skipped sqlite (by touching spkg/installed/sqlite-3.6.17) and when it started working on libgpg_error, it immediately failed with the same error.

I don't see why the error on Arch would prevent this ticket from getting into 4.1.2. The official supported platforms are CentOS, Debian, Fedora, RHEL, Mandriva, openSUSE, OS X 10.5, and Ubuntu. We are now porting to OS X 10.6 as well, a goal of the 4.1.2 release. Testing on all of these platforms, the updated spkg build OK and doctests pass, except for known doctest failures. Having said that, it's good to investigate why Jason's updated spkg failed to build on Arch. But that's another ticket.




An updated spkg based on Jason's is available at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/python-2.6.2.p3.spkg

The changes from Jason's spkg include:

 * Some general clean up of the file `SPKG.txt`. In particular, the typo pointed out by Dan, and some typo fixes. Make lines no more than 75 or so characters wide. Any line wider than that and it would be difficult to read on a standard terminal width, i.e. 80 characters wide.
 * Put in the lines "set -e" and "set +e".


---

Comment by was created at 2009-10-04 18:04:20

I'm giving this a positive review, though I have issues with how "set -e" is used.  However, in this particular case no harm will be done.


---

Comment by was created at 2009-10-04 18:04:20

Resolution: fixed
