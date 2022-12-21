# Issue 3052: mercurial --> plain text --> mercurial

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-29 05:18:58

Assignee: mabshoff

Robert Bradshaw has mostly solved this:

```
I've looked into this some more and it looks like we can completely
reconstruct a repository from the export of all its keywords. The
trick is to use the --exact keyword when importing. This forces it to
apply the given patch to the correct parent (sometimes creating a new
head) and will also correctly import merge patches (removing heads).
Some scripts to do this are up at

http://sage.math.washington.edu/home/robertwb/hg/

I've successfully exported and re-created simple repositories (with
branching) with these scripts, and it works great and preserves all
the history. The only issue is that I can't seem to get it to work
with any repositories older than a certain date. I think the issue is
that mercurial changed the way nodeid's are calculated (and I keep
getting an error "abort: patch is damaged or loses information" which
is thrown when the newly computed nodeid does not match the one in
the patch (command.py:1632 in 0.9.5)). Matt Mackall, any suggestions
on how to cleanly get around this/get the old node-id numbers instead?

- Robert Bradshaw
```


But there are issues.  See the complete thread here:

http://groups.google.com/group/sage-devel/browse_thread/thread/79da4852b8e20851/c4b8e87260f08f96?#c4b8e87260f08f96


---

Comment by kini created at 2011-04-04 17:18:17

Is this ticket still valid? I'm not sure I understand what exactly needs to be done with this, but it seems to apply to ancient mercurial versions and sage 2.x...


---

Comment by kini created at 2011-08-06 07:23:04

OK, William explained it to me simply - some users (especially, say, corporate environments) might be afraid of viruses in Mercurial's binary history data. This ticket is looking for a way to make our source distribution consist *entirely* of text files only.


---

Comment by kini created at 2011-08-10 08:05:06

I've written a python program that converts Mercurial 1.0+ bundles to a JSON representation and back. This doesn't produce a series of patch files, but it is a fully 7-bit-clean text format which is human-readable (though not as easy to grasp as a git diff or unified diff). It is also a bit-identically reversible computation and preserves all node IDs. The transformation from repository to bundle is also fully reversible as it is what Mercurial itself uses for pushes and pulls.


---

Comment by kini created at 2011-08-11 05:01:29

apply to $SAGE_ROOT


---

Attachment

apply to $SAGE_ROOT/spkg/base


---

Comment by kini created at 2011-08-11 05:13:56

So here are a couple of patches. Apply as indicated. The python file is not doctested, but most of the functions are pretty side-effectful so I don't see how exactly to do this. It at least does fail the doctester if it can't find the correct things to import, so that much is at least safeguarded (in case Mercurial is too old or too new, for example). Speaking of which, this patch depends on #10594 (merged in 4.7.2.alpha0).

Test this patch by unpacking a source distro tarball, doing `make text-expand`, `make text-collapse`, `make`, and `make ptestlong` (in that order, of course). Works for me on sage.math.washington.edu .


---

Comment by kini created at 2011-08-11 05:13:56

Changing status from new to needs_review.


---

Comment by vbraun created at 2011-09-18 12:18:35

Sounds good, positive review. 

Of course there is still a 35MB spkg containing various OSX Fortran compilers, thats a lot of binary code ;) Hopefully apple will fix their toolchain at one point...


---

Comment by vbraun created at 2011-09-18 12:18:35

Changing status from needs_review to positive_review.


---

Comment by kini created at 2011-09-21 04:07:44

Thanks for the review! :)


---

Comment by leif created at 2011-09-23 11:28:41

Looks like Jeroen's merger doesn't yet support the base repository... :(


---

Comment by leif created at 2011-09-27 17:40:17

Resolution: fixed


---

Attachment


---

Comment by leif created at 2011-10-06 11:47:10

I rebased all patches with fuzz 2, but didn't bother about this one because it was so trivial (or obvious). ;-)


---

Comment by kini created at 2011-10-31 08:40:15

BTW this code imports stuff from Mercurial internals so it may need to be updated when we next upgrade Mercurial. Any ideas on how to make a doctest that will break when Mercurial is upgraded so that this will be noticed when the time comes? I guess there's always the trivial


```rst
>>> import mercurial.__version__.version
>>> mercurial.__version__.version
'1.8.4'
```


But even if we use this silly doctest, where should it go? `$SAGE_ROOT/spkg/base` is not doctested by `make ptestlong`.


---

Comment by was created at 2011-10-31 16:13:12

Odd tests go in `SAGE_ROOT/devel/sage/sage/tests`.


---

Comment by leif created at 2011-10-31 21:10:06

Perhaps we could tag such tests `# optional - release` such they get only run by developers and the release manager(s) or release scripts.  Then we could really test whether `text-expand` and `text-collapse` are still functional (and not just test for a Mercurial version, which is a bit odd).
