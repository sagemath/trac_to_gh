# Issue 2624: parallel testing: sage -tp foo/bar/file.py is broken

Issue created by migration from https://trac.sagemath.org/ticket/2624

Original creator: mabshoff

Original creation time: 2008-03-21 00:46:53

Assignee: gfurnish

Oops: 

```
./sage -tp -long devel/sage/sage/plot/plot.py
Global iterations: 1
File iterations: 1
TeX files: 0
Usage: sage -t <files or directories>.
For more information, type 'sage -help'.
```





---

Comment by gfurnish created at 2008-03-21 00:48:35

Missing number of threads parameter, invalid.


---

Comment by gfurnish created at 2008-03-21 00:48:35

Resolution: invalid


---

Comment by gfurnish created at 2008-03-21 00:49:34

Changing status from closed to reopened.


---

Comment by gfurnish created at 2008-03-21 00:49:34

This should be the responsiblity of sage-sage


---

Comment by gfurnish created at 2008-03-21 00:49:34

Resolution changed from invalid to 


---

Comment by gfurnish created at 2008-03-21 00:49:51

Changing assignee from gfurnish to mabshoff.


---

Comment by gfurnish created at 2008-03-21 00:49:51

Changing status from reopened to new.


---

Comment by AlexGhitza created at 2009-01-22 18:25:28

Changing type from defect to enhancement.


---

Comment by jhpalmieri created at 2009-09-21 22:42:38

Here's a patch.  If the first argument after "tp" can't be converted to an integer, this sets it to 1 and assumes that the first argument is part of the list of files.  The patch also expands on the error messages, changes the usage warning from "Usage: sage -t" to "Usage: sage -tp", gives a pointer to "sage -advanced" for more help, and adds a corresponding string to the output of "sage -advanced".


---

Comment by jhpalmieri created at 2009-09-21 22:42:38

Changing assignee from mabshoff to jhpalmieri.


---

Comment by jhpalmieri created at 2009-09-21 22:42:38

Changing status from new to assigned.


---

Comment by ddrake created at 2009-09-23 01:11:40

With this patch, when I do something like "sage -tp fjfjfjfjfj", it doesn't tell me that I gave it a bad file:

```
drake@klee:/var/tmp/sage-4.1.2.alpha2$ ./sage -tp fjfjfj 
Global iterations: 1
File iterations: 1
Using cached timings to run longest doctests first.
Doctesting 0 files 
 
----------------------------------------------------------------------
All tests passed!
Timings have been updated.
Total time for all tests: 0.1 seconds
```

Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)


---

Comment by jhpalmieri created at 2009-09-23 02:04:55

> With this patch, when I do something like "sage -tp fjfjfjfjfj", it doesn't tell me that I gave it a bad file:

I feel as though this belongs in another ticket.  For what it's worth, previous authors of the file seem to have made this decision intentionally:

```
               else:
                    continue # prefer silence to: raise TypeError, "Unknown File %s" % F
```


> Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)

That's easy enough to change; see the new patch.  This version also sets numthreads to be no more than the number of files.


---

Comment by ddrake created at 2009-09-23 02:36:52

Replying to [comment:8 jhpalmieri]:
> > With this patch, when I do something like "sage -tp fjfjfjfjfj", it doesn't tell me that I gave it a bad file:
> 
> I feel as though this belongs in another ticket.  For what it's worth, previous authors of the file seem to have made this decision intentionally:
> {{{
>                else:
>                     continue # prefer silence to: raise TypeError, "Unknown File %s" % F
> }}}

Okay, that does look like another ticket.

> > Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)
> 
> That's easy enough to change; see the new patch.  This version also sets numthreads to be no more than the number of files.

Those look like good changes. Magic 8-ball says...positive review likely.


---

Comment by ddrake created at 2009-09-23 04:54:42

Oops, there's a typo: `numthreads = min(numthreads, len(files))` should be *after* `files` is populated; otherwise, a directory with tons of files counts as one file! If you move that bit to line 324 (after the `populatefilelist(infiles)` stanza), everything works as expected. With that change, I give this patch a positive review. John, after updating your patch, you can change the title to positive review. 

*Release manager*: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.


---

Comment by jhpalmieri created at 2009-09-23 05:01:02

Replying to [comment:10 ddrake]:
> Oops, there's a typo

Good catch.  Fixed in the new patch.


---

Comment by jhpalmieri created at 2009-09-23 05:01:22

apply to scripts repository


---

Attachment


---

Comment by mvngu created at 2009-09-25 04:05:06

Replying to [comment:10 ddrake]:
> *Release manager*: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.
When packaging the Sage source tarball, the files `COPYING.txt`, `install`, and `spkg-install` all end up in the package `sage_scripts.x.y.z.spkg`. When building from source, those three files end up as

 * `COPYING.txt` becomes SAGE_ROOT/COPYING.txt --- The directory `SAGE_ROOT` is not tracked:
 {{{
[mvngu`@`sage sage-4.1.2.alpha2]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
 }}}
 * `install` becomes SAGE_ROOT/spkg/install --- The directory `SAGE_ROOT/spkg` is not tracked:
 {{{
[mvngu`@`sage spkg]$ pwd
/scratch/mvngu/release/sage-4.1.2.alpha2/spkg
[mvngu`@`sage spkg]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
 }}}
 * `spkg-install` becomes SAGE_ROOT/local/bin/sage-spkg-install --- The directory `SAGE_ROOT/local/bin` is indeed tracked.

As it now stand, the changes to `spkg-install` can be checked in to `SAGE_ROOT/local/bin/sage-spkg-install`. Changes for the other two files would need to be manually applied to the relevant files.


---

Comment by ddrake created at 2009-09-25 05:19:48

Replying to [comment:13 mvngu]:
> Replying to [comment:10 ddrake]:
> > *Release manager*: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.
> When packaging the Sage source tarball, the files `COPYING.txt`, `install`, and `spkg-install` all end up in the package `sage_scripts.x.y.z.spkg`. When building from source, those three files end up as
> 
>  * `COPYING.txt` becomes SAGE_ROOT/COPYING.txt --- The directory `SAGE_ROOT` is not tracked:
[snip]
>  * `install` becomes SAGE_ROOT/spkg/install --- The directory `SAGE_ROOT/spkg` is not tracked:
[snip]
>  * `spkg-install` becomes SAGE_ROOT/local/bin/sage-spkg-install --- The directory `SAGE_ROOT/local/bin` is indeed tracked.
> 
> As it now stand, the changes to `spkg-install` can be checked in to `SAGE_ROOT/local/bin/sage-spkg-install`. Changes for the other two files would need to be manually applied to the relevant files.

Okay. It does seem weird that basic source files are not version controlled...but whatever. :)  For the purposes of this ticket, you just need to merge the patch to sage-ptest.


---

Comment by mvngu created at 2009-09-25 06:24:27

Resolution: fixed


---

Comment by mvngu created at 2009-09-25 06:24:27

Merged in the script repository.


---

Comment by mvngu created at 2009-09-27 10:25:53

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
