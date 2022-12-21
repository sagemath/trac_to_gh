# Issue 3531: [With SPKG, needs review] Boehm_GC spkg

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-06-28 23:36:39

Assignee: gfurnish

Boehm GC is a prerequisite for ECL lisp and M2 (See #10)
Download at http://sage.math.washington.edu/home/gfurnish/spkg/boehm_gc-7.1.spkg


---

Comment by mhansen created at 2008-06-29 19:45:33

This builds fine on my machine.


---

Comment by mabshoff created at 2008-06-29 19:48:57

The issue here is that as is with the current config the amount of memory available to the gc is 1GB and that is not even enough to run the M2 test suite, hence not ready for review.

Gary: Next time you change the summary of a ticket make sure to provide sufficient information why it was changed.


---

Comment by gfurnish created at 2008-06-30 04:46:27

We are not actually convinced this is not as intended - M2 does not build Boehm with nonstandard options.


---

Comment by mabshoff created at 2008-06-30 06:13:12

Replying to [comment:4 gfurnish]:
> We are not actually convinced this is not as intended - M2 does not build Boehm with nonstandard options. 

Yes, but last time I tested M2's own test suite failed due to out of memory conditions. Enabling

```
  --enable-large-config   Optimize for large (> 100 MB) heap or root set
```

ought to fix the problem. This option carries slight memory consumption overhead, see http://gcc.gnu.org/ml/java/2005-02/msg00181.html but I will enforce `--enable-large-config` for ecl anyway.

Cheers,

Michael


---

Comment by gfurnish created at 2008-06-30 16:24:34

I have replaced the old spkg with one with --enable-large-config.  Please rereview.


---

Comment by gfurnish created at 2008-06-30 16:24:34

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-02 20:01:48

Changing keywords from "" to "editor_mabshoff".


---

Comment by mabshoff created at 2008-07-16 16:58:00


```
[09:44am] mabshoff|afk: gfurnish: oops, negative review.;
[09:44am] gfurnish: also yay to that
[09:44am] gfurnish: boo
[09:44am] mabshoff|afk: just kidding 
[09:44am] schilly: mabshoff|afk: very good
[09:44am] mabshoff|afk: I have not looked yet 
[09:45am] You are now known as mabshoff.
[09:47am] mabshoff: boehm_gc-7.1$ hg status
[09:47am] mabshoff: abort: There is no Mercurial repository here (.hg not found)!
[09:47am] mabshoff: then: spkg-install is not executable
[09:47am] gfurnish: is that bad
[09:47am] mabshoff: And there is OSX crap in there.
[09:47am] mabshoff: ._src
[09:47am] mabshoff: re executable: Not really, but it ought to be.
[09:47am] gfurnish: uh
[09:47am] mabshoff: spkg-install makes it executable as needed.
[09:47am] gfurnish: reviewer fix? 
[09:48am] mabshoff: SPKG.txt is also not in the proper format.
[09:48am] gfurnish: what the heck SPKG.txt is in the proper format
[09:48am] gfurnish: I copied the template right off the wiki!
[09:48am] mabshoff: And my dead grand mother could write a better spkg-install.
[09:49am] mabshoff: Maybe even my imaginary cat could 
[09:49am] mabshoff: I doubt that.
[09:49am] gfurnish: what is wrong with the spkg-install
[09:49am] elbie joined the chat room.
[09:49am] mabshoff: you need to copy http://wiki.sagemath.org/spkgTemplate?action=edit&editor=text
[09:49am] mabshoff: I.e. SPKG.txt is written in wiki text
[09:49am] mabshoff: re spkg-install
[09:49am] mabshoff: shebang is missing
[09:50am] mabshoff: #633 needs to be checked
[09:50am] mabshoff: cd src
[09:50am] mabshoff: ./configure
[09:50am] mabshoff: You also don't seem to believe in error checking 
[09:50am] gfurnish: well it successfully blows up on error
[09:51am] mabshoff: And the shebang has to be #!/usr/bin/env  bash
[09:51am] mabshoff: I don't care we check return codes and print proper error messages.
[09:51am] gfurnish:  
[09:52am] gfurnish: is there an example of a simple spkg-install that is well done?
[09:52am] mabshoff: Sure.
[09:52am] gfurnish: can you tell me an example of a simple spkg-install that is well done? 
[09:53am] mabshoff: The problem is that all the really good ones are comples.
[09:53am] mabshoff: *complex
[09:53am] mabshoff: I am looking for a simple good one right now.
[09:54am] gfurnish: alternatively you could fix boehm_gc and then I'll fix gdbm and m2
[09:54am] gfurnish: but I do some complicated stuff in m2 so it would be nice if you would look at it first too
[09:54am] mabshoff: Well, that is probably the easiest idea.
[09:54am] gfurnish: namely M2 does OS specific stuff
[09:54am] mabshoff: Otherwise I will send you back a couple times until you get it right.
[09:55am] gfurnish: that I think avoids bashisms given it works on sparc solaris
[09:55am] gfurnish: but it still would be nice if you
[09:55am] gfurnish: give me some advice on it
[09:55am] mabshoff: Well, M2 is not a high concern to me personally, boehm is since it will become standard soon.
```



---

Comment by mabshoff created at 2008-07-16 17:34:13

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha0/boehm_gc-7.1.p0.spkg

fixes all known issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 18:22:50

Merged in Sage 3.0.6.alpha0


---

Comment by mabshoff created at 2008-07-16 18:22:50

Resolution: fixed
