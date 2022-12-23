# Issue 3882: explain in the programming guide why spkg source patches should be applied by copying entire files

Issue created by migration from https://trac.sagemath.org/ticket/3882

Original creator: jason

Original creation time: 2008-08-17 03:13:45

Assignee: tba

In the sage programming guide (and maybe on the wiki too), it should be explained how to distribute a patch to the source of an spkg.  The way I think about it (thanks to wstein and mabshoff!) is that the end result of the patches should be cached in whole files, which are then copied over the sources at install time.  Thus, at spkg-install time, there should be no reliance on patch and friends; only files copied over onto the sources.

So one way to do it would be to maintain a set of patches to the sources.  When the spkg is created, apply all the patches and copy the affected files to a patches-cached (or patches-applied or something) directory.  When the spkg is installed, just copy the affected files over the source files.


---

Comment by jhpalmieri created at 2008-08-19 01:51:07

I'm working on editing the programming guide, but I don't understand what you mean. Can you explain it again, or give an example?

(Probably part of the issue is that I haven't really worked with spkg's, just the core sage library.)


---

Comment by robertwb created at 2008-08-19 03:12:22

I'm not understanding why one would want to do it this way, rather than just patch the source. It makes it much clearer what's going on. Also, we can assume something like patch is available as we are using it for mercurial (or do we need it later on?)

If not, I think it would be very good to make it clear with an (automated) patches-applied directory, so someone could update an spkg without having to manually figure out all the diffs and re-apply them.


---

Comment by mabshoff created at 2008-08-19 03:57:30

A couple reasons *not* to use patch:

 * GNU patch that can apply unified diffs does not exist on some platforms per default, i.e. Solaris
 * the number of changes to the sources in the src directory are usually small and should be pushed upstream anyway
 * copying patches is dead simple and very KISS
 * hg's patch requires the sources to be under revision control, doubling the size of a Sage tarball
 * hg is only available late in the build process, so it is a chicken and egg problem
 * some changes are conditional on the platform we are building on

William and I discussed this with Jason in IRC for an hour. As an opinion from the trenches: patch has no advantage over copying. Most spkgs have the new files and their diff in the patches directory. Upgrading spkgs will not be any easier by applying some patches to the source since it requires some understanding what is being changed. And those reasons should be documented in SPKG.txt.

Cheers,

Michael


---

Comment by robertwb created at 2008-08-19 04:21:01

Yes, those seem like good enough reasons.


---

Comment by jhpalmieri created at 2008-08-20 00:41:34

I just posted lots of revisions to the programming guide in #3905, but I have not dealt with the issue raised here.  I would suggest, if anyone feels inspired to work on this one, wait until #3905 makes it through the review process so we don't get conflicts -- both in the technical sense of being unable to apply one patch or the other, and also stylistically and content-wise: if the changes in #3905 go through, any changes for this ticket should be based on the new version.


---

Comment by mvngu created at 2010-02-09 12:11:45

A patch to revise the Developer's Guide is up at #8079.


---

Comment by mvngu created at 2010-02-14 14:39:26

Close as fixed by #8079.


---

Comment by mvngu created at 2010-02-14 14:39:26

Resolution: fixed
