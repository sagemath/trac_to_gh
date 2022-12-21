# Issue 8437: wrong unix rights/permissions of some files after make dist

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-03-04 19:12:41

Assignee: tbd

CC:  thome

see #1240 for the description (I was told not to reopen tickets).


---

Comment by zimmerma created at 2010-03-05 08:47:20

In fact my colleague did not really use `make dist`, but `mv` to install Sage.
Thus I did check again with `make dist`, and there are still wrong permissions:

```
pasta% find /localdisk/tmp/sage433_install \! -perm -644 -ls
...
1975926   76 -rw-r-----   1 zimmerma caramel     71306 Jan 19 00:37 /localdisk/tmp/sage433_install/sage/local/share/moin/underlay/pages/LanguageSetup/attachments/Brazilian_Portuguese--optional_system_pages.zip
1975927    4 -rw-r-----   1 zimmerma caramel      1848 Jan 19 00:37 /localdisk/tmp/sage433_install/sage/local/share/moin/underlay/pages/LanguageSetup/attachments/Polish--optional_system_pages.zip
1975928   12 -rw-r-----   1 zimmerma caramel      8587 Jan 19 00:37 /localdisk/tmp/sage433_install/sage/local/share/moin/underlay/pages/LanguageSetup/attachments/Latvian--essential_system_pages.zip
1975929    8 -rw-r-----   1 zimmerma caramel      4865 Jan 19 00:37 /localdisk/tmp/sage433_install/sage/local/share/moin/underlay/pages/LanguageSetup/attachments/Croatian--essential_system_pages.zip
2089187    4 -rw-r-----   1 zimmerma caramel         9 Jan 19 00:33 /localdisk/tmp/sage433_install/sage/local/share/moin/underlay/pages/LanguageSetup/current
1388864 8836 -r-xr-xr-x   1 zimmerma caramel   9029932 Mar  4 15:24 /localdisk/tmp/sage433_install/sage/local/lib/libpython2.6.a
3426776    4 -rwxr-x---   1 zimmerma caramel      1533 Mar  4 16:58 /localdisk/tmp/sage433_install/sage/local/lib/gap-4.4.12/terminfo/c/cygwin
3426777    4 -rwxr-x---   1 zimmerma caramel      1885 Mar  4 16:58 /localdisk/tmp/sage433_install/sage/local/lib/gap-4.4.12/terminfo/r/rxvt
2050275    4 -rwxr-x---   1 zimmerma caramel      2100 Mar  4 16:58 /localdisk/tmp/sage433_install/sage/local/lib/gap-4.4.12/terminfo/x/xterm
```



---

Comment by zimmerma created at 2010-03-05 14:57:22

A followup from Emmanuel Thome: the following command should give no output (from an extracted
tarball of Sage):

```
find . -name '*.spkg' | while read f ; do bzip2 -dc $f | tar tvf - | grep -v '^.rw.r..r..'  ; done
```

Currently (in sage-4.3.3) it gives many hundred lines:

```
...
-rw-r----- wstein/wstein   2382 2006-11-12 23:45 lapack-20071123.p1/src/manpages/man/manl/clatzm.l
-rw-r----- wstein/wstein   1969 2006-11-12 23:45 lapack-20071123.p1/src/manpages/man/manl/dlange.l
-rw-r----- wstein/wstein   8989 2006-11-13 23:26 lapack-20071123.p1/src/manpages/man/manl/sstemr.l
-rw-r----- wstein/wstein   1950 2006-11-12 23:45 lapack-20071123.p1/src/manpages/man/manl/zhpgst.l
-rw-r----- wstein/wstein   2985 2006-11-12 23:45 lapack-20071123.p1/src/manpages/man/manl/zunmqr.l
-rwx------ jaap/jaap      1626 2010-01-25 22:11 givaro-3.2.13rc2.p0/spkg-install
-rw------- jaap/jaap      4041 2010-01-28 14:00 givaro-3.2.13rc2.p0/SPKG.txt
```



---

Comment by jhpalmieri created at 2010-04-23 04:56:12

I agree with the comment from #1240: 

> I declare this as a blocker since this issue should be fixed *once for all* (and automatically checked before doing a release).

There is no patch doing this (the automatic checking, in particular), so I'm delaying this to Sage 5.0.  Also, this should probably be a meta-ticket: it should point to other tickets, each dealing with a specific spkg which has this problem.


---

Comment by zimmerma created at 2010-04-23 07:46:25

> There is no patch doing this (the automatic checking, in particular), so I'm delaying this to Sage 5.0. 

strange way to deal with a blocker ticket... Two years ago, such tickets were considered very seriously by the release manager.

Paul Zimmermann


---

Comment by jhpalmieri created at 2010-04-23 14:16:07

What else can I do about it?  I'm not even sure it should be labeled a blocker, since Sage seems to function perfectly well without fixing it.

Perhaps you can be the release manager next, rather than suggest that I'm not taking things seriously.


---

Comment by zimmerma created at 2010-04-23 14:26:40

> I'm not even sure it should be labeled a blocker, since Sage seems to function perfectly well without fixing it. 

please look at comment 6 in #1240: Sage does not function at all in a multi-user environment.
I just ask that this item should be added in the "TODO" list of the release manager: just run the
command given in comment 2 above before each release (it takes less than one minute) and fix the
corresponding permissions if needed.


---

Comment by jhpalmieri created at 2010-04-23 14:42:53

To fix the corresponding permissions, I would have to modify over 20 spkgs.  Each of these changes would need review -- the release manager can't just make those changes.  Furthermore, most of those have no effect on Sage's functioning, since most of the files go away after the corresponding spkgs are installed.  If I look at permissions after I've built Sage, I see

```
392669357        8 -rwxr-x---    1 palmieri admin        1533 Apr 22 00:25 /Applications/sage_builds/sage-4.4.alpha2/local/lib/gap-4.4.12/terminfo/c/cygwin
392669359        8 -rwxr-x---    1 palmieri admin        1885 Apr 22 00:25 /Applications/sage_builds/sage-4.4.alpha2/local/lib/gap-4.4.12/terminfo/r/rxvt
392669361        8 -rwxr-x---    1 palmieri admin        2100 Apr 22 00:25 /Applications/sage_builds/sage-4.4.alpha2/local/lib/gap-4.4.12/terminfo/x/xterm
392451131    13928 -r-xr-xr-x    1 palmieri admin     7129840 Apr 21 20:53 /Applications/sage_builds/sage-4.4.alpha2/local/lib/libpython2.6.a
```

and a lot of files related to the moin package.  The python library is clearly not a problem, since the only permission issue is that it's not writeable.  Do the gap files really cause Sage to not work in a multi-user environment?

I would assert that comment 6 at #1240 should be ignored, because as you say above, your colleague didn't install Sage properly in the first place.  Please provide other evidence that Sage doesn't function without this ticket being fixed, and then upgrade this to a blocker again.


---

Comment by jhpalmieri created at 2010-04-23 14:42:53

Changing priority from blocker to critical.


---

Comment by jdemeyer created at 2012-10-05 09:47:47

Closing this since
 1. Many of the files in spkgs now have the correct permissions.
 2. Even if they don't, it seems all files are _installed_ with the correct permissions, which is really what matters, I checked this with:

```
find . -not \( \( -type f -perm 0644 \) -or \( -type f -perm 0755 \) -or \( -type d -perm 0755 \) -or -type l \) -ls
```

 3. The issue of running Sage as a different user is being tracked at #5155.  If non-readable files would be a problem, then the doctests would fail.


---

Comment by jdemeyer created at 2012-10-05 09:47:47

Resolution: worksforme
