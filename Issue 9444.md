# Issue 9444: Fix "rm: Cannot remove any directory in the path of the current working directory" on t2

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-07 05:29:55

Assignee: drkirkby

CC:  drkirkby

In `/rootpool2/local/kirkby/sage-4.5.alpha1` on t2:

```sh
$ tail spkg/logs/rubiks-20070912.p11.log
real    2m30.575s
user    2m20.699s
sys     0m5.083s
Successfully installed rubiks-20070912.p11
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/rootpool2/local/kirkby/sage-4.5.alpha1/spkg/build/rubiks-20070912.p11
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing rubiks-20070912.p11.spkg
```

This leaves an empty directory `SAGE_ROOT/spkg/build/rubiks-20070912.p11`.

It seems the problem is

```sh
rm -rf "$SAGE_PACKAGES/build/$PKG_NAME"
```

near the end of `SAGE_LOCAL/bin/sage-spkg`.  What if we precede this with `cd ..`, say?


---

Attachment

Step out of spkg/build/foo-x.y.z before deleting it.


---

Comment by mpatel created at 2010-07-07 05:40:22

I've attached a trial patch that uses `cd "$SAGE_PACKAGES/build/"`.


---

Comment by drkirkby created at 2010-07-07 07:16:03

This looks good and I'm confident it would fix this rather annoying bug. 

My only concern is whether fixing this bug will cause a problem for any code that might have relied on the old behavior. That will need testing. 

Dave


---

Comment by jhpalmieri created at 2010-07-27 22:56:48

I think that this message only appears on Solaris; at least, that's been my experience.  On sage.math, for example, I can do this:

```
$ cd /scratch/palmieri
$ mkdir TEMP
$ cd TEMP
$ rm -rf /scratch/palmieri/TEMP
```

but doing this on t2.math results in an error:

```
rm: Cannot remove any directory in the path of the current working directory
```

So if it ever relied on this behavior, it didn't rely on it on sage.math.  (All of the linux machines I've used, and also Mac OS X, behave like sage.math in this regard.)

I'm trying a build on sage.math with this patch, and I'll try it on t2 later.


---

Comment by jhpalmieri created at 2010-07-27 22:57:09

mpatel: I assume this is ready for review?


---

Comment by jhpalmieri created at 2010-07-27 22:57:09

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-27 23:13:40

I'm ok with the patch, though we could replicate

```sh
   # Make triply sure that we are in the build directory before doing 
    # a scary "rm -rf".
    cd "$SAGE_PACKAGES/build"
    if [ $? -ne 0 ]; then
        echo "Unable to find build directory."
    else
        rm -rf "$PKG_BASE-"*
    fi
```

which is what is done some lines above.

There are many other things to fix or improve in `sage-spkg`, but I'll leave those for further tickets (something like work in progress) since hopefully this one gets merged soon.

If anyone feels Mitesh's solution is not sufficient, feel free to revert it to "needs review" or "needs work".

-Leif


---

Comment by leif created at 2010-07-27 23:13:40

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-07-27 23:18:05

I'm happy too. My initial concern was that the directory was not getting deleted on any operating system, in which case deleting it could be dangerous. But now I realise it gets deleted on Linux, then clearly there is no risk. 

I'm 100% happy with this. 

Dave


---

Comment by leif created at 2010-07-27 23:26:21

Just for the record: Besides other things, I'd like to have something like `$SAGE_SPKG_KEEP_SRC` (or `SAGE_KEEP_BUILT_SPKGS`) for developers, because `-s` is not available for whole builds (with `make`).


---

Comment by mpatel created at 2010-07-28 05:09:02

Replying to [comment:4 jhpalmieri]:
> mpatel: I assume this is ready for review?

Yes.  I didn't change the status field because I had tested the patch only with `sage -f` on sage.math and t2.

Were there any problems with your builds?


---

Comment by jhpalmieri created at 2010-07-28 05:25:59

No, everything has worked fine.


---

Comment by jhpalmieri created at 2010-08-06 21:50:52

Replying to [comment:7 leif]:
> Just for the record: Besides other things, I'd like to have something like `$SAGE_SPKG_KEEP_SRC` (or `SAGE_KEEP_BUILT_SPKGS`) for developers, because `-s` is not available for whole builds (with `make`).

See #4949.


---

Comment by drkirkby created at 2010-08-08 09:44:19

Why is the milestone for this set to 5.0? Do we really need to wait that long to fix this bug, given it already has positive review and is one of the simplest possible bug fixes. 

Dave


---

Comment by mpatel created at 2010-08-09 09:39:39

Resolution: fixed
