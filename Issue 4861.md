# Issue 4861: Update FLINT to 1.0.20 (latest 1.0.x upstream)

Issue created by migration from https://trac.sagemath.org/ticket/4861

Original creator: mabshoff

Original creation time: 2008-12-24 00:12:04

Assignee: mabshoff

See Summary :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-24 00:17:13

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.3/alpha0/flint-1.0.20.spkg

provides the latest stable (1.0.x) FLINT release. Also note to apply the patch to the Sage library so that the FLINT dependent extensions are automatically rebuild for an updated FLINT.

Cheers,

Michael


---

Attachment

*Review*
 * SPKG.txt is updated properly (+1)
 * hg status returns cleanly (+1)
 * doesn't seem to contain unneeded binary cruft (+1)
 * attached patch `trac_4861.patch` looks good (+1)
 * `spkg-install` works on sage.math (+1)
 * `spkg-install` *runs test suite* (-1)
 * `make ptest` passes on sage.math (+1)

"positive review" if the test suite is disabled or it is explained why it needs to be run.


---

Comment by mabshoff created at 2008-12-24 13:53:14

Every time we have upgrades FLINT we automatically run the test suite. This is usually turned off once we do the actual release.

Cheers,

Michael


---

Comment by malb created at 2008-12-24 13:58:38

I know, we just need to stick a reminder somewhere, don't we? If you disagree, just change it to positive review since the worst thing that can happen is an extra couple of minutes of build time.


---

Comment by mabshoff created at 2008-12-24 14:02:11

Replying to [comment:4 malb]:

Hi Martin,

> I know, we just need to stick a reminder somewhere, don't we? If you disagree, just change it to positive review since the worst thing that can happen is an extra couple of minutes of build time.

#4870 is now a blocker for 3.2.3 to turn it off before release. I would imagine this is a solution we can both live with.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-24 14:15:52

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-24 14:15:52

Resolution: fixed
