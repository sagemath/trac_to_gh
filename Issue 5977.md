# Issue 5977: Implement sage -clean-residues

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-05-04 05:57:56

Assignee: mabshoff

CC:  sage-combinat

Keywords: cleanup

Add an option -clean-residues (or any better name) to the sage script to make it compare the list of .pyc files and .so files in the build directory with the list in the source directory.  If a file has been removed in the source directory, delete the corresponding .pyc and .so files (or maybe even: if a file has been removed from version control, then wipe the .pyc/.so files, even if the actual file still exists in the source directory).

Optionally, if the overhead is negligible, call this automatically upon sage -b.

See discussion 'Test failing on "ImportError: cannot import name Set"...' around March 11 on sage-devel.



---

Comment by mabshoff created at 2009-05-04 06:06:28

Whoever implements this needs to be aware that in Sage 3.4.2 and later DSage is no longer in the Sage library tree, but an external spkg that installs code into the site-package. So a special case needs to be implemented. 

I looked for another ticket that requests the same thing to be implemented, but I have not found it yet (should it exist).

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 14:37:26

This is quite important to get fixed since the new symbolics code will break the Sage startup otherwise.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 14:37:26

Changing priority from major to blocker.


---

Comment by was created at 2009-05-16 14:04:28

> This is quite important to get fixed since the new symbolics code will break the Sage startup otherwise. 

Craig is going to do this later.  If it isn't done in time for sage-4.0, we can include a single *1-line* fix to spkg-install that completely deals with the problem for symbolics.  Note that I have *already* included that fix in our branch, just in case.


---

Comment by craigcitro created at 2009-05-27 06:58:39

apply to repo in $SAGE_LOCAL/bin


---

Attachment

I've attached a patch to clean the build tree. It's really two patches: one for the `$SAGE_LOCAL/bin` repo, which has the actual functionality, and another for the main repo. 

The patch for the main repo simply removes two top-level imports of `dsage` -- there are dsage files sitting in my build dir with no corresponding files in the source tree; if something is simply wrong with my build (actually, with both of the builds I checked), then I'm happy to change this. 

The code itself should be fairly readable, I think. I've written a little script called `sage-sync-build`, which simply walks the `build` tree and looks for files that don't have a corresponding file in the source tree. If it finds any, it deletes them. After finishing each directory in `build/`, it deletes the directory if it's now empty.

Mostly for testing purposes, I gave this three command-line arguments:

 * `-p`: prune empty directories. (This is on by default, and passing `-p` turns it off.)

 * `-d`: dry run. If this is passed, simply mention what files it would delete.

 * `-v`: verbose. Print info about what it's doing.

NOTES:

 * I tested this in my sage tree, and it seemed to work. Then I touched some filenames in `sage/` or `build/` appropriately, and it *seems* to do what I expect. However, if playing with the build system has taught me anything, there are surely tons of cases that I didn't anticipate. I'm happy to fix any bugs people run into.

 * I tried to be careful about using `os.path.sep` and `os.path.extsep` to compose the paths; I'm sure I slipped up somewhere. I've got a shiny nickel for the first person to spot a slip-up ... `:)`

 * I'm not wedded to any of the names, or the command-line arguments. I made up `sync-build` after about 20 seconds of thought, so feel free to say it's a silly name, and think of something better. 

 * One more vague comment: I feel like we *should* be able to make distutils do this work for us. I spent about 5 minutes looking at documentation and source, and didn't see anything, but my search was by no means exhaustive. If anyone knows distutils better than I do, and has an idea, just let me know. I'd like to get back to putting the caching of dependencies back in place (#4651) soon, so I'll try and dig around more then.


---

Comment by craigcitro created at 2009-05-27 07:19:49

Hah, I forgot to mention how to actually *run* the code. `:)` You can just use `sage -sync-build`, and it correctly passes along any arguments you want to try. So a natural first step would be to type `sage -sync-build -d` to see a list of all the files in `build/` that it thinks need to be removed.


---

Comment by craigcitro created at 2009-05-27 07:43:20

I'm deleting the patch against the main repo: Mike Hansen has posted a much nicer patch at #6075.


---

Comment by mhansen created at 2009-05-28 04:50:34

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-28 04:50:34

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-05-28 04:50:34

I've tested and read through this a bit.  Looks good to me.


---

Comment by mhansen created at 2009-05-28 04:51:21

Merged in 4.0.rc1


---

Comment by mhansen created at 2009-05-28 06:10:59

Resolution: fixed
