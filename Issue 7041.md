# Issue 7041: GAP purposely unsets CC which screws up Sun Studio build.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 16:30:04

Assignee: tbd

CC:  dimpase ohanar

Keywords: gap solaris cc

The spkg-install for gap-4.4.10.p12

echo "*WARNING*: Unsetting CC since that tends to break GAP building"
unset CC
echo "*WARNING*: Unsetting CXX since that tends to break GAP building"
unset CXX

This appears to be done by Michael Abshoff as SPKG.txt shows:

### gap-4.4.10.p8 (Michael Abshoff, June 16th, 2008)
 * unset CC in spkg-install (work around for #2575)


Looking at http://sagetrac.org/sage_trac/ticket/2575 I can't help feel there must be a better solution.


---

Comment by ohanar created at 2012-02-06 23:14:32

well, ignore that patch, wrong ticket (sometimes tab browsing hates you)


---

Comment by leif created at 2012-03-22 14:08:50

For the record, the GAP 4.4.12.p6 spkg still unsets these variables, for whatever reason (#2575 and #4161 might shed some light on that).

Hopefully someone will soon upgrade to GAP 4.5, which *might* solve potential issues with not unsetting them; haven't tested that (or looked at it) at all.


---

Comment by leif created at 2012-03-22 14:08:50

Changing keywords from "gap solaris cc" to "gap solaris cc CXX compiler hardcoded hard-coded".


---

Comment by leif created at 2012-03-22 17:42:58

I'm currently preparing a GAP 4.4.12.p7 spkg fixing this issue (i.e., only unsetting `CC` and `CXX` if absolutely necessary), and cleaning up `SPKG.txt` and `spkg-install`.

There are still some open questions though; see e.g. my comments [comment:ticket:10825:14 here] (on #10825).


---

Comment by dimpase created at 2012-03-25 06:48:48

Replying to [comment:4 leif]:

> There are still some open questions though; see e.g. my comments [comment:ticket:10825:14 here] (on #10825).

I think what you did on #10825 is good.


---

Comment by leif created at 2012-04-09 12:12:13

Excerpt from (the modified) `SPKG.txt`:

## Dependencies

 * readline (according to spkg/standard/deps)
 * Sage (? also according to deps, "so that gap_reset_workspace works")

## Special !Update/Build Instructions

 * TODO:
   - Use `patch` instead of copying patched files.
     (Then also add `patch` to the dependencies above.)
   - "Flatten" (i.e. remove) the `build()` function.
   - Perhaps check whether we can fix GAP's configure / build scripts
     w.r.t. brokenness of multiple words in `CC` (and `CXX`?) and its
     ignorance concerning `CFLAGS`, `CPPFLAGS` and `LDFLAGS`.
     (Then also support `SAGE_DEBUG` in `spkg-install`, and probably
     set up reasonable default `CFLAGS`.)

 * Do we really want to copy everything from the build directory???
   (Cf. comment in `spkg-install`.)

 ...


I'll perhaps address some of the TODOs (I added myself) later, in a p8, but I'd really like to get this spkg in soon.

The stated (probably obsolete?) dependency on Sage and the last point should be answered by some of *you*... ;-)


---

Comment by leif created at 2012-04-09 12:12:13

Changing status from new to needs_review.


---

Attachment

Diff between the previous spkg in Sage and my new p7 spkg.  For reference / review only.


---

Comment by leif created at 2012-04-09 12:31:01

As usual, I've attached a diff of the spkg for easier reviewing.


---

Comment by leif created at 2012-04-09 12:31:01

Changing assignee from tbd to leif.


---

Comment by ohanar created at 2012-05-28 11:07:46

Changing status from needs_review to positive_review.


---

Comment by ohanar created at 2012-05-28 11:07:46

Looks good and works well.


---

Comment by ohanar created at 2012-05-29 06:15:06

Changing keywords from "gap solaris cc CXX compiler hardcoded hard-coded" to "gap solaris cc CXX compiler hardcoded hard-coded sd40.5".


---

Comment by jdemeyer created at 2012-06-06 19:10:05

Resolution: fixed
