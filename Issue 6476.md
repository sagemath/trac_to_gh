# Issue 6476: upgrade Singular to 3.1.0.4

Issue created by migration from https://trac.sagemath.org/ticket/6476

Original creator: rlm

Original creation time: 2009-07-07 20:16:38

Assignee: tbd

CC:  aginiewicz polybori john_perry was

See #6470 and #6362 for a bit of history...


---

Comment by GeorgSWeber created at 2009-07-15 22:26:43

The thread http://lists.apple.com/archives/unix-porting/2006/Aug/msg00022.html started years ago by Justin C. Walker on how to build Singular on OS X (for Sage!) brought some more insights.

If one uses "g++ -dynamiclib ..." instead of "libtool -dynamic ..." (note the "lib" at the ending of "-dynamiclib", this seems to superspecial for g++ instead of just gcc on Mac OS X) to build libsingular.dylib, then together with the changes I already wrote in #6470, the modified 3.1.0.4 singular spkg from #6362 (as included in Sage-4.1.rc0) seems finally to (build and also to) work on OS X.

But one not only needs to adapt "src.Singular.Makefile.in" which is already in the patch directory, but also add some "src.Singular.config.in" there and even "src.Singular.config" because although the Makefile is created from Makefile.in in the install process, config is *not* updated from config.in. This will take some more time, and testing also for the PPC Darwin target. I see if can do that soon and upload a new spkg for review, but probably not in the next days.


---

Comment by malb created at 2009-07-22 08:04:06

I completely lost track.

Can someone please point me to the most recent 3-1-0-4 SPKG I should start working on? I am visiting the Singular group right now so I have them within reach for the week.


---

Comment by GeorgSWeber created at 2009-07-22 15:45:04

The last "official" Singular 3-1-0-4 spkg was the one included in Sage-4.1.rc0. Since I couldn't find a still working link, I uploaded it here: http://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090703.spkg.

As far as I remember, this spkg did build and work fine, except for OS X. I managed to make it build with rather minor changes, but then Sage wouldn't start on OS X. After looking more deeply into it, I managed to produce a version that both did build and work fine on my MacIntel. I uploaded this version here:
http://sage.math.washington.edu/home/weberg/spkg/singular-3-1-0-4-20090715.spkg

However, this is "work in progress", the last changes were done in a quick and hackish way, e.g. altering directly the files under /src/ inside the spkg. The remaining work would be to:
1. clean this up, e.g. create new files under /patch/, make sage-install copy these over, update mercurial repository, ...
2. make (and test) these changes also for MacPPC

Sorry, I didn't get around doing this yet, so you'll have to look into the half-cooked new spkg and search for the "newest" files via modification time. If you have questions, please ask.


---

Comment by malb created at 2009-07-23 07:41:09

Hi, I produced a new SPKG which should contain all your changes (but we fixed a bug in your fix of GNUmakefile.in). I've uploaded it to

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg

I'll run tests and silently update that file (until it works). I'll report back when I consider it 'stable'. I'll have to check whether it works with GCC 4.4.

Credit for this ticket goes to GeorgSWeber, Michael Brickenstein, Hans Schönemann, aginiewicz and Martin Albrecht.


---

Comment by malb created at 2009-07-23 11:33:19

It seems Georg's fix to replace `-dynamic` with `-dynamiclib` is not universally valid (i.e. on bsd.math it wouldn't compile with his change applied)

aginiewicz can you send me a patch with your GCC 4.4 patches, your server is down and I can't track down your changes.


---

Comment by malb created at 2009-07-23 14:01:24

There version at 

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg

seems to pass tests now on anything but OSX where the `__eprintf` bug shows. As mentioned above, Georg's fix doesn't work for me.


---

Comment by malb created at 2009-07-23 14:43:17

There version at 

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090723.spkg

now seems to work on sage.math and bsd.math ... finally. Please test with a GCC 4.4 compiler.


---

Comment by AlexGhitza created at 2009-08-18 02:32:08

I tried your latest spkg with gcc 4.4.1 and did not get far.  The install log is at

http://www.ms.unimelb.edu.au/~aghitza/singular_install.log


---

Comment by malb created at 2009-08-18 09:45:13

Alright, it seems I missed some GCC 4.4 changes. I will provide an updated SPKG (directly instead of patches because the next version of Singular will have exactly the same changes anyway). Is there any machine where I can try GCC 4.4 myself to speed up the process?


---

Comment by malb created at 2009-08-18 09:48:37

Alright, try this: http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090818.spkg


---

Comment by AlexGhitza created at 2009-08-18 10:29:16

Martin,

I currently only have GCC 4.4 on my laptop and on a rather slow machine at the office.  If you need access to it, I can make an account for you there.

Anyway, the new spkg builds fine for me.  I am running tests now.


---

Comment by malb created at 2009-08-18 11:18:48

Alex, since it builds now I think I won't need access. But thanks for the offer!


---

Comment by AlexGhitza created at 2009-08-18 13:39:10

So far, looks good.  I should be done with testing by tomorrow morning.  There is one very minor issue: the most recent changelog entry in SPKG.txt talks about 3-1-0-4-20090723, where it probably should say something about 3-1-0-4-20090818.  Could you fix this and replace the spkg?


---

Comment by malb created at 2009-08-18 13:45:35

done, the SPKG is at the same place with the same name.


---

Comment by AlexGhitza created at 2009-08-19 07:26:35

OK, I think this is good to go.  Positive review.


---

Comment by mvngu created at 2009-08-24 04:46:45

Merged `singular-3-1-0-4-20090818.spkg` in the standard spkg repository.


---

Comment by mvngu created at 2009-08-24 04:46:45

Resolution: fixed
