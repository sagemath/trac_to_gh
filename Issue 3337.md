# Issue 3337: Upgrade gap-guava to new 3.5 release

Issue created by migration from https://trac.sagemath.org/ticket/3337

Original creator: tabbott

Original creation time: 2008-05-30 06:06:30

Assignee: mabshoff

CC:  mhansen

Upgrading guava to 3.5 would be especially helpful for the Debianization, because that version includes fixes to several upstream problems that cause problems for the Debian package.


---

Comment by mabshoff created at 2008-12-12 11:11:41

David,

if you take care of the GAP 4.11 update can you also do this?

Cheers,

Michael


---

Comment by wdj created at 2008-12-12 11:47:53

Yes. (I assume you mean just include guava in the gap spkg.) Actually guava is now at 3.8:-)


---

Comment by wdj created at 2008-12-18 21:05:37

I have a new version of gap at
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.p1.spkg
which also has the new guava in it. The good news is that it seems to install okay. Bad news, it is huge (about 25M) and I don't know what I threw in there to make it so big. I just swapped the old "src" with the contents of the gap package, removing prim, small, trans, some pdfs_dvis, and some tst files. I think the old one was around 8M.

It is transferring now, so the above link should be good in 10 minutes or less.


---

Comment by mabshoff created at 2008-12-18 21:14:52

Nuke tomlib:

```
mabshoff@sage:~/gap-4.4.12.p1/src$ du -sch pkg/*
84K	pkg/Browse
28K	pkg/edim
12M	pkg/guava3.9
104K	pkg/io
4.0K	pkg/PKGDIR
76M	pkg/tomlib
88M	total
```


Cheers,

Michael


---

Comment by wdj created at 2008-12-18 23:33:50

Oops, I missed that one. I also deleted a few doc files in guava, so now this guava3.9 is smaller than the previously included guava3.4. I think gap is just bigger. This version is about 12M. Same url:
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.p1.spkg


---

Comment by mabshoff created at 2008-12-20 21:59:13

A couple remarks:

 * Why isn't this gap-4.4.12.spkg since this is the first gap.spkg from 4.4.12?
 * An SPKG.txt entry is missing.
 * changes in the root hg repo aren't checked in
 * it would be nice if the exact sequence this spkg was prepared with, i.e. removal of various packages, etc, was properly documented in SPKG.txt

I am sure I can find more issues :)

Cheers,

Michael


---

Comment by wdj created at 2008-12-21 00:32:29

> A couple remarks:
>    * Why isn't this gap-4.4.12.spkg since this is the first gap.spkg from 4.4.12?


Do you mean gap-4.4.12.p0.spkg? I can change that.


>    * An SPKG.txt entry is missing.

I'll fix that.


>    * changes in the root hg repo aren't checked in


I don't know what that means.


>    * it would be nice if the exact sequence this spkg was prepared 
> with, i.e. removal of various packages, etc, was properly documented in SPKG.txt 

I can fix that.

> I am sure I can find more issues :) 

Anything else?


---

Comment by mabshoff created at 2008-12-21 00:35:51

Replying to [comment:7 wdj]:

> 
> Do you mean gap-4.4.12.p0.spkg? I can change that.

No, gap-4.4.12.spkg since it is the first release of gap-4.4.12. 
 

> I don't know what that means.

Changes to the root directory of the spkg have to be checked in - just run 'hg status'

> Anything else?

There also seem to be some dynamic libraries in the spkg, i.e. some binary crap. I have to recheck if they are still there, but just search for .so files.

Cheers,

Michael


---

Comment by wdj created at 2008-12-21 00:50:00

> Comment (by mabshoff):
>
>  Replying to [comment:7 wdj]:
>
>  >
>  > Do you mean gap-4.4.12.p0.spkg? I can change that.
>
>  No, gap-4.4.12.spkg since it is the first release of gap-4.4.12.
>
>
>  > I don't know what that means.
>
>  Changes to the root directory of the spkg have to be checked in - just run
>  'hg status'


I still don't know what this means.

Here is my workflow.

(1) Download the tarball from the gapsite,
decompress in a directory sagestuff, thus creating a subdirectory
sagestuff/gap-4.4.12

(2) unpack the guava3.9 tarball in the sagestuff/gap*/pkg subdirectory

(3) unpack the last gap-4.4..10.p*.spkg in sagestuff, creating a subdirectory
sagestuff/gap-4.4.10.p*

(4) copy this to
sagestuff/gap-4.4.12 (or .p0 or .p1 or whatever)

(5) delete everything in the sagestuff/gap-4.4.12/src
subdirectory and replace it by sagestuff/gap-4.4.12

(6) Delete extraneous stuff (such as small, prim, etc).

(7) run tar -cjvf gap-4.4.12.tar.bz2 gap-4.4.12/

(8) Rename tar.bz2 to spkg, upload, and post to trac.

I don't see where in that sequence to run hg status. Maybe I
should

(9) run sage -f gap-4.4.12.spkg and then start sage and then
run
sage: hg_sage.status()?

Or is there some other way to do this?



>
>  > Anything else?
>
>  There also seem to be some dynamic libraries in the spkg, i.e. some binary
>  crap. I have to recheck if they are still there, but just search for .so
>  files.


They are there. I think they were added for some windows functionality, but I
mostly ignore windows emails on gap- (and sage-) devel so am not sure.
I don't know basically 0 about windows, what windows files look like, or what
should be done with windows files.


---

Comment by mabshoff created at 2008-12-21 00:56:24

David:

```
mabshoff@sage:/scratch/release-cycle$ tar xjf gap-4.4.12.p1.spkg 
mabshoff@sage:/scratch/release-cycle$ cd gap-4.4.12.p1
mabshoff@sage:/scratch/release-cycle/gap-4.4.12.p1$ pwd
/scratch/release-cycle/gap-4.4.12.p1
mabshoff@sage:/scratch/release-cycle/gap-4.4.12.p1$ hg stat
M spkg-install
? patch
```

There is a repo in there where changes need to be check in.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 00:58:58

Re binaries:

```
mabshoff@sage:/scratch/release-cycle/gap-4.4.12.p1$ find  . -name "*.so"
./src/pkg/Browse/bin/i686-pc-cygwin-gcc/ncurses.so
./src/pkg/io/bin/i686-pc-cygwin-gcc/io.so
./src/pkg/edim/bin/i686-pc-cygwin-gcc/ediv.so
```

I see no reason why we would shop binaries in the gap.spkg. In case we cannot buidl those from sources there is something seriously wrong about the GAP procject.

Cheers,

Michael


---

Comment by wdj created at 2008-12-21 01:41:36

>  Re binaries:
>  {{{
>  mabshoff`@`sage:/scratch/release-cycle/gap-4.4.12.p1$ find  . -name "*.so"
>  ./src/pkg/Browse/bin/i686-pc-cygwin-gcc/ncurses.so
>  ./src/pkg/io/bin/i686-pc-cygwin-gcc/io.so
>  ./src/pkg/edim/bin/i686-pc-cygwin-gcc/ediv.so
>  }}}
>  I see no reason why we would shop binaries in the gap.spkg. In case we
>  cannot buidl those from sources there is something seriously wrong about
>  the GAP procject.


I deleted these. Just to be precise - these are not part of GAP but
parts of (GPL'd) GAP packages.

I tried to make all the changes you suggested earlier.

I ran


```
wdj@hera:~/sagefiles/sagestuff/gap-4.4.12$ pwd
/home/wdj/sagefiles/sagestuff/gap-4.4.12
wdj@hera:~/sagefiles/sagestuff/gap-4.4.12$ hg stat
M SPKG.txt
M spkg-install
? patch
wdj@hera:~/sagefiles/sagestuff/gap-4.4.12$ ls
dist  patch  patches  spkg-debian  spkg-install  SPKG.txt  src
```


However, I don't know what "There is a repo in there where changes need to be check in."
means. Do I run hg_sage.status()? hg_sage.commit()?


The new spkg is at
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.spkg


---

Comment by mabshoff created at 2008-12-21 11:52:00

David,

you need to run hg directly in the root directory of the spkg. There are no wrappers from Sage to do that. Just read "hg help" and for example "hg help commit" for more details.

Cheers,

Micheal


---

Comment by wdj created at 2008-12-21 14:02:30

I don't know the definition of repo. I assumed it was something which is at least part of the sage tree. The old gap spkg is just a tarball I downloaded separately. Probably not the main problem here.

I read both "hg help commit" and "hg help" and don't see how the information they provide can be used in this situation. I described the process I used to create the spkg in the list above. What I am wondering is what step(s) needs to be added/subtracted/modified. When I try something like "hg commit" then "hg export", I get this:


```
wdj@hera:~/sagefiles/sagestuff/gap-4.4.12$ hg export
abort: export requires at least one changeset
}}
Obviously that is the wrong idea but it at least follows the process I am used to using for Sage code patches. If hg is to be used to create the new GAP spkg then obviously (a) I have to learn a lot more and (b) it isn't clear to me how to proceed. For example, is "hg remove" to be used for every file deleted from the old spkg and "hg add" to be used for every file/dir added to the new spkg?

Maybe all of this should be done inside a copy of Sage and then use sage_extcode somehow?


---

Comment by wdj created at 2008-12-21 14:31:13

Another thing I tried was a completely different workflow:

(a) download the old gap spkg, unpack it into sagestuff/gap-4.4.10.p10

(b) in sagestuff, create a clone using hg clone gap-4.4.10.p10 gap-4.4.12
(first, I backed up the old directory gap-4.4.12 for safety)
This creates a directory sagestuff/gap-4.4.12

(c) made all the changes described to this clone

(d) cd sagestuff/gap-4.4.12, and enter "hg commit" and "hg export"
I still get


```
wdj@hera:~/sagefiles/sagestuff/gap-4.4.12$ hg export
abort: export requires at least one changeset


```



---

Comment by mabshoff created at 2008-12-21 14:38:30

David,

 * please read the introduction to hg at http://hgbook.red-bean.com/hgbookch2.html and play around with it in some random location, i.e. create a repo, add files, check in all via hg directly and do not use the Sage wrapper. That will likely help you resolve many of the issues you seem to run into when applying patches for example.
 * each spkg has a repo in it - check for the .hg directory. In that repo is everything but the src directory. When changing spkg-install, SPKG.txt and so on the changes need to be checked in via "hg commit" (after adding new files for example via hg add and son on) before packing the spkg. There is no need to export any patches or so on. That checkin cannot be done via the Sage wrappers for hg.

If you still have problems please write to sage-support since this ticket is not about how to deal with hg and spkgs. Maybe you would want to contribute some documentation to the Sage development manual when this is all sorted out since this really seems to cause trouble for you. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 14:42:21

Replying to [comment:15 wdj]:
> Another thing I tried was a completely different workflow:
> 
> (a) download the old gap spkg, unpack it into sagestuff/gap-4.4.10.p10
> 
> (b) in sagestuff, create a clone using hg clone gap-4.4.10.p10 gap-4.4.12
> (first, I backed up the old directory gap-4.4.12 for safety)
> This creates a directory sagestuff/gap-4.4.12

Do not create a clone, just delete the old src directory, drop in the new src directory, fix what ever you have to do and then commit the new version before packing the archive.

> (d) cd sagestuff/gap-4.4.12, and enter "hg commit" and "hg export"
> I still get
> 
> {{{
> wdj`@`hera:~/sagefiles/sagestuff/gap-4.4.12$ hg export
> abort: export requires at least one changeset

No need to export anything. Just check if you checked in the changes via "hg log"
 
Cheers,

Michael


---

Comment by mabshoff created at 2008-12-24 15:57:17

Hi David,

the spkg needs work:

 * delete the patch binary in the root of the spkg
 * the changes need to be check in. One way to do this is via

```
 hg commit -m "gap-4.4.12: update to latest upstream, update to guava 3.9 (#3337)"
```

 * SPKG.txt is in the wrong format:

```
### gap-4.4.12 (David JOyner, 2008-12-20)

Upgraded to gap-4.4.12. Upgraded guava 3.4 to guava 3.9.
From the source GAP tarball, removed tomlib, small, prim,
trans, and some pdf+dvi files from guava3.9/doc.
```

This should be:

```
### gap-4.4.12 (David Joyner, 2008-12-20)
 *  Upgraded to gap-4.4.12, upgraded guava 3.4 to guava 3.9 (#3337)
```

Then you need to add a section about special build instructions with details, i.e.

```
## Special Update/Build Instructions

From the source GAP tarball, removed tomlib, small, prim,
trans by running $SOME_COMMAND, and some pdf+dvi files from guava3.9/doc 
by runnnig $SOME_OTHER_COMMAND.
```

SPKG.txt can use some improvements, i.e. check out 

 http://wiki.sagemath.org/spkgTemplate

for all the sections that should be in SPKG.txt. If I have time later I will fix all these problems.

Cheers,

Michael


---

Comment by wdj created at 2008-12-24 16:08:20

I plan on working on this soon.

I got distracted because I really want to dump guava from the list of installed packages. (I will stay in the optional gap_packages* of course.) I have now all the code written need to actually dump guava. Of course, this would involve some substantial changes and refereeing and so on, so it probably won't get done this cycle.

I also have been reading the mercurial manual, which is long overdue. I'm glad you pushed me to do it. I should have time later in the next several days, maybe even tonight.


---

Comment by wdj created at 2008-12-25 17:47:45

I am uploading a new spkg to http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.spkg right now. It seems to satisfy the format at http://wiki.sagemath.org/spkgTemplate and the hg commit produced a patch. 

What I did (more or less) was to apply hg remove and hg add to various directories of the old repo, combined with some editing and cp'ing, before running hg commit. Even after reading the documentation (which IMHO isn't very good) and googling, I could still not figure out what hg would accept and what it wouldn't. For example, over-writing a file seems to be not okay (in the sense that it doesn't get recorded as a changeset) but editing a file (with emacs say) is okay. Anyway, hope this is okay now. If it is okay, maybeI'll add some sensible comments to http://wiki.sagemath.org/SPKG_Audit, though it is hard for me to understand some of what is there so I'm not sure where the best pace to add such comments.


---

Comment by mabshoff created at 2008-12-25 18:14:54

Replying to [comment:20 wdj]:

Hi David,

> I am uploading a new spkg to http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.spkg right now. It seems to satisfy the format at http://wiki.sagemath.org/spkgTemplate and the hg commit produced a patch. 

Ok, this is a step in the right direction.
 
> What I did (more or less) was to apply hg remove and hg add to various directories of the old repo, combined with some editing and cp'ing, before running hg commit.

Why? Nothing in src is under version control. An update to GAP should just involve unpacking the new sources, deleting some things like the dbs, adding Guava, updating spkg-install and SPKG.txt and then committing. 

> Even after reading the documentation (which IMHO isn't very good) and googling, I could still not figure out what hg would accept and what it wouldn't. For example, over-writing a file seems to be not okay (in the sense that it doesn't get recorded as a changeset) but editing a file (with emacs say) is okay. Anyway, hope this is okay now. If it is okay, maybeI'll add some sensible comments to http://wiki.sagemath.org/SPKG_Audit, though it is hard for me to understand some of what is there so I'm not sure where the best pace to add such comments.

Please post to the devel list first before changing things. 

There are two issues:

 * The file patch is left in the root directory of the spkg. Just delete it
 * The text in SPKG.txt needs to be true wiki text, as is that needs some fixing. The dependencies are wrong, i.e. we list spkgs that GAP depends upon to build, not build tools. All people should be listed via lists and current spkg maintainers are probably you, rlm, William and me. 

If I get time today I will fix this up and post 4.4.12.p0.

One last question: How large is the test suite? I am asking since it would be nice to run tests via spkg-check and if the size increase is reasonable I would greatly prefer to be able to test.

Cheers,

Michael


---

Comment by wdj created at 2008-12-25 20:06:36

I am uploading a new version that I think fixes all the items you mentioned about SPKG.txt.

I also included this time the test suite (in src/tst). It is <1M uncompressed. 

Hope it is okay this time. If I'd understood src was not under version control, it would have gone a little faster probably.


---

Comment by mabshoff created at 2009-02-04 02:43:35

Hi David,

I noticed a couple things:

 * because you did not update the scripts you are still doctesting with GAP 4.4.10 and not with the new 4.4.12.
 * spkg-install has some problem installing wtdist, so things don't go to well for such doctests.

Overall we have a fair number of failure:

```
	sage -t -long devel/sage/sage/graphs/graph_isom.pyx # 2 doctests failed
	sage -t -long devel/sage/sage/coding/linear_code.py # 4 doctests failed
	sage -t -long devel/sage/sage/graphs/graph.py # 1 doctests failed
	sage -t -long devel/doc/const/const.tex # 1 doctests failed
	sage -t -long devel/sage/sage/rings/number_field/number_field.py # 1 doctests failed
	sage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx # 1 doctests failed
	sage -t -long devel/sage/sage/interfaces/gap.py # 2 doctests failed
	sage -t -long devel/sage/sage/groups/class_function.py # 1 doctests failed
	sage -t -long devel/sage/sage/groups/abelian_gps/abelian_group.py # 4 doctests failed
	sage -t -long devel/sage/sage/misc/sage_eval.py # 1 doctests failed
	sage -t -long devel/sage/sage/groups/abelian_gps/abelian_group_element.py # 1 doctests failed
```

Most of those are cosmetic, but someone ought to go over them and correct issues, some are trivial and some are worrying:

```
File "/scratch/mabshoff/sage-3.3.alpha5/devel/sage-main/sage/graphs/graph.py", line 6297:
   sage: M.determinant()
Expected:
   -712483534798848
Got:
   712483534798848
```

My latest spkg is at

  http://sage.math.washington.edu/home/mabshoff/spkgs/gap-4.4.12.p0.spkg

If you want to fix the issue with wtdist you ought to use that as a base.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 02:45:11

By the way: The same issue exists in the old gap-4.4.10.p10.spkg as I just found out:

```
ake[1]: Leaving directory `/scratch/mabshoff/sage-3.3.alpha5/spkg/build/gap-4.4.10.p10/src/pkg/guava3.4/src/leon'
cp: omitting directory `../../bin'
cp: cannot stat `cp': No such file or directory
```

For some reason wtdist does get installed - strange.

Cheers,

Michael


---

Comment by cwitty created at 2009-02-04 22:55:29

The files

```
src/src/GAP 4 PPC
src/src/tst/GAP 4 PPC
```

should be removed (they are MacOS 9 binaries).


---

Comment by cwitty created at 2009-02-04 23:08:34

Probably `src/bin/*` (various windows executables, DLLs, and batch files) should be removed too.


---

Comment by wdj created at 2009-02-07 13:05:41

Can you try http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.p2.spkg ? I think this
addresses cwitty's comments and avoids the previous failure since I added a line to spkg-install so now places the wtdist in the right directory. 

Unfortunately, sage -testall cannot be trusted on this machine since it fails on every module which uses maxima. (I hope when ecl is used, this will go away.) Therefore, I only did some limited and localized testing. Seems to work better anyway.


---

Comment by mabshoff created at 2009-02-07 18:53:34

David,

 * please change the status of the ticket if you post an updated spkg/patch
 * test the spkg on sage.math since there all the tests involving Maxima pass

The spkg cannot be merged without fixing a large number of printing issues with the doctests. I will take a closer look if wtdist and so on are now there.

Cheers,

Michael


---

Comment by wdj created at 2009-02-08 03:31:31

> David,
>     * please change the status of the ticket if you post an updated spkg/patch


Oops - sorry!


>    * test the spkg on sage.math since there all the tests involving Maxima pass 


Done. Modulo the maxima problems I have, it fails in the same way - there are lots of funny 
print statements in gap.py which yield test output such as



```
File "/home/wdj/sagefiles/sage-3.3.alpha5/devel/sage/sage/coding/code_constructions.py", line 501: 
    sage: C.minimum_distance()                                                                     
Expected:                                                                                          
    4                                                                                              
Got:                                                                                               
    Warning: this should never happen                                                              
    Warning: this should never happen                                                              
    Warning: this should never happen                                                              
    Warning: this should never happen                                                              
    Warning: this should never happen                                                              
    Warning: this should never happen                                                              
    4                                                    
```

I don't understand the purpose of this print statement but it seems to be fairly new.


> The spkg cannot be merged without fixing a large number of printing issues with the doctests.

Can the print statement in gap.py just be commented out?


---

Comment by mabshoff created at 2009-02-08 03:38:27

Replying to [comment:29 wdj]:

> 
> 
> >    * test the spkg on sage.math since there all the tests involving Maxima pass 
> 
> 
> Done. Modulo the maxima problems I have, it fails in the same way - there are lots of funny 
> print statements in gap.py which yield test output such as
> 
> I don't understand the purpose of this print statement but it seems to be fairly new.

This is not the problem I am referring to and the print issue were actual changes in GAP's output. These need to be fixed. I have never seen the above statement on sage.math. Which Sage release is this? Do you have anything in .gaprc?
 
> 
> > The spkg cannot be merged without fixing a large number of printing issues with the doctests.
> 
> Can the print statement in gap.py just be commented out?
> 

I doubt it, but you should ask someone who knowns the code better. 

This is wrong by the way:

```
     if [ $UNAME = "CYGWIN" ]; then
+        echo "** Cygwin install not supported **"
         $MKDIR bin
```

You also managed to delete .hgignore and not check in the changes to spkg-install:

```
M spkg-install
! .hgignore
```

I do not understand why it is such a problem to make two two line changes and check in the changes without breaking the spkg?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 03:45:39

Two more things:

 * spkg-check is missing - since we are now including the GAP test suite (or at least some subset) we need to actually be able to run it
 * SPKG.txt needs to be updated to (a) reflect the changes in gap-4.4.12.p2.spkg and (b) also to spell out the need to remove certain binary crap that cwitty pointed out.

Cheers,

Michael


---

Comment by wdj created at 2009-02-08 05:05:34

> This is not the problem I am referring to and the print issue were actual changes in GAP's 
> output. These need to be fixed. I have never seen the above statement on sage.math. Which Sage 
> release is this? Do you have anything in .gaprc?

This is sage-3.3.alpha5. No I don't have a .gaprc. Should I?

> This is wrong by the way:
>      if [ $UNAME = "CYGWIN" ]; then
> +        echo "** Cygwin install not supported **"
>          $MKDIR bin

Okay, I'll restore that. 

> You also managed to delete .hgignore and not check in the changes to spkg-install: 

Yes, I totally forgot it was an hg repo. Hopefully, when I check it in (or whatever - I'll have to look up your old emails since I don't remember the steps), those will get fixed.

> Two more things:
>     * spkg-check is missing - since we are now including the GAP test suite 
> (or at least some subset) we need to actually be able to run it


Is there some documentation on what spkg-check should be?


>     * SPKG.txt needs to be updated to (a) reflect the changes in gap-4.4.12.p2.spkg 
> and (b) also to spell out the need to remove certain binary crap that cwitty pointed out. 

Okay.

The bigger question for me is that (if we ignore all these problems) it is not clear to me if the package passes the tests. I don't understand the "Warning: this should never happen " lines. In other words, I don't know what they mean or what triggers them. For example, your statement "These need to be fixed" above. What needs to be fixed? The docstrings in guava? The print statement in gap.py?

Sorry I haven't had a lot of time to devote to Sage recently. (A lot of stuff is going on at work.) If this is pressing, if I can't fix this tomorrow maybe I should ask Carl Witty if he could finish it up?


---

Comment by mabshoff created at 2009-02-08 06:28:33

Replying to [comment:32 wdj]:

Hi David,

> > This is not the problem I am referring to and the print issue were actual changes in GAP's 
> > output. These need to be fixed. I have never seen the above statement on sage.math. Which Sage 
> > release is this? Do you have anything in .gaprc?
> 
> This is sage-3.3.alpha5. No I don't have a .gaprc. Should I?

No, but I do not have a .gaprc and I do not see the problem. So if you had one it could point to the problem. 

> > You also managed to delete .hgignore and not check in the changes to spkg-install: 
> 
> Yes, I totally forgot it was an hg repo. Hopefully, when I check it in (or whatever - I'll have to look up your old emails since I don't remember the steps), those will get fixed.

It is simple:

 * unpack spkg
 * move spkg to new name, i.e. gap-4.4.12.p0 to gap-4.4.12.p1 
 * change spkg
 * hg commit -m "Describe what you did"
 * repack spkg
 * test spkg
 
> > Two more things:
> >     * spkg-check is missing - since we are now including the GAP test suite 
> > (or at least some subset) we need to actually be able to run it
> 
> 
> Is there some documentation on what spkg-check should be?

It should invoke the test suite and return "0" when things pass and not "0". Note that the working directory when spkg-check is invoked is the same as at the end of spkg-install, so you might want to get the current working directory at the start of spkg-install and restore it at the end. 

> The bigger question for me is that (if we ignore all these problems) it is not clear to me if the package passes the tests. I don't understand the "Warning: this should never happen " lines. In other words, I don't know what they mean or what triggers them. For example, your statement "These need to be fixed" above. What needs to be fixed? The docstrings in guava? The print statement in gap.py?

The following is just the simplest example that fails with the new spkg:

```
    def version(self):
        """
        Returns the version of GAP being used.

        EXAMPLES:
            sage: gap.version()
            '4.4.10'
        """
        return gap_version()
```

If that did not fail for you you are doing something wrong since you are still running gap 4.4.10 then. There are about a dozen other problems related to printing and some other things. I did not take a closer look since it was clear to me that the spkg as is would not go into 3.3 without someone doing some major work.

> Sorry I haven't had a lot of time to devote to Sage recently. (A lot of stuff is going on at work.) If this is pressing, if I can't fix this tomorrow maybe I should ask Carl Witty if he could finish it up?

I can trivially do the one line change that matters in spkg-install, the point is that someone needs to fix the doctesting issues exposted by gap 4.4.12.

Cheers,

Michael


---

Comment by wdj created at 2009-02-08 14:43:49

Thanks very much. That clarifies the errors I should focus on. I'll work on the the sage -t gap.py falures you mentioned today but some seem to be non-trivial. I'll need to submit a docstring patch and a new spkg file. For the docstring patch, it might be that some methods used by GAP which were deterministic were switched to randomized algorithms. Tracking that down might take a little time but should be doable.


---

Attachment

to be applied to 3.3.alpha6


---

Comment by wdj created at 2009-02-09 03:41:21

Tested http://sage.math.washington.edu/home/wdj/sagefiles/gap-4.4.12.p1.spkg and patch above on my machine and sage.math. Install and testall go okay, modulo problems with seem unrelated (eg, plotting) and modulo the "Warning: this should never happen" business discussed above. Hope I did the hg commit stuff correctly.
 
Hopefully this is better than the last patch anyway!


---

Comment by mabshoff created at 2009-02-09 05:07:48

I am not sure if we need to make all these doctest #random since IIRC cwitty initializes the GAP rng for each doctest. 

Carl: Is this correct or was this a plan to make GAP's rng behave nicely with the doctesting framework?

And this change also makes me very uncomfortable:

```
6294	6294	            sage: C = graphs.CubeGraph(4) 
6295	6295	            sage: G = C.automorphism_group() 
6296	6296	            sage: M = G.character_table() 
6297	 	            sage: M.determinant() 
 	6297	            sage: M.determinant() # random sign (only abs. value is well-defined)  
6298	6298	            -712483534798848 
6299	6299	            sage: G.order() 
6300	6300	            384 
```

Why is the sign of the determinant of a character table random? In that case the doctest should check for the absolute value of the determinant since #random would hide bugs here, i.e. no one would notice if the determinant would change more than its sign. I would also appreciate adding that info the the docstring of the character table to make people aware of the problem.

Cheers,

Michael


---

Comment by cwitty created at 2009-02-09 08:52:23

For efficiency reasons, we only initialize the GAP random number generator when we know we're going to use it.  The way we do this is that in every Sage library function that calls a GAP function that uses random numbers, we put this at the beginning:

```
        current_randstate().set_seed_gap()
```

and this at the top of the file:

```
from sage.misc.randstate import current_randstate
```

(you can see several examples of this in perm_gps/permgroup.py and matrix_gps/matrix_group.py).

So if GAP has changed some of its functions to be randomized, we need to add the above incantation at the beginning of every Sage library function that calls such a function.


---

Comment by wdj created at 2009-02-10 00:27:54

to be applied to 3.3.alpha6 with others (in order)


---

Attachment

to be applied to 3.3.alpha6 with others (in order)


---

Attachment

to be applied to 3.3.alpha6 with others (in order)


---

Comment by wdj created at 2009-02-10 00:34:03

Thanks for the help!
I think all these patches implement the comments made by mabshoff and cwitty. 

> Why is the sign of the determinant of a character table random?

While the columns of the character table correspond to the conjugacy classes of the group, in general there is no way to order them canonically. (At least GAP does not have a canonical method to order the conjugacy classes implemented currently and I don't know of one which is valid for all finite groups.)


---

Comment by mabshoff created at 2009-02-10 00:38:12

Thanks David,

I know this was much more painful then you had asked for, but I would claim the quality of the GAP.spkg did improve and so did my understanding of the GAP.spkg. 

I will try to get this into 3.3 since Debian upstream would benefit from the guava update and it seems like a waste of effort to fix all the docstrings again post 3.4, but no promises.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 08:02:51

Ok, positive review pending doctests to pass. I build on all of SkyNet and am running long doctests on all of the machines. 

 * eno - building with 3.3.a6, doctesting long now
 * mark - building with 3.3.a6 - gap starts
 * fulvia - building with 3.3.a6 - gap starts
 * menas - building with 3.3.a6, doctesting long now
 * cicero - building with 3.3.a6, doctesting long now
 * cleo - building with 3.3.a6, doctesting long now
 * iras - building with 3.3.a6, doctesting long now
 * varro - building with 3.3.a6, doctesting long now  

It will take a while for them to pass, hence the pending. The spkg looks good, i.e. everything is checked in and clean, SPKG.txt is updated and so on. The patches look good, too. If doctests pass I will merge this ticker into 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 08:55:43

Hi David,

so far I have seen one issue:

```
**********************************************************************
File "/home/mabshoff/build-3.3.alpha6/sage-3.3.alpha6-fulvia/devel/doc/const/const.tex", line 2632:
    : print gap.eval("R:= PolynomialRing( GF(97))")
Expected:
    PolynomialRing(..., [ x_1 ])
Got:
    GF(97)[x_1]
**********************************************************************
```

This should be trivial to fix. I have also seen one box where the 

```
Warning: this should never happen
```

occurs, so we might want to take you up on your suggestions unless William or somebody else can nail down and fix the problem.

I will keep you updated as things develop.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 10:28:24

David,

I have looked some more at the issue with

```
Warning: this should never happen
```

and it comes out of interfaces/gap.py. I would suggest instead of disabling the code we should do the following:

 * turn them into proper warning at warning level 1 - that way we don't see them in the doctests
 * open a ticket to address the problem indicating which doctests to run with what warning level so the issue gets resolved.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 10:28:57

Another issue that only happens on 32 bit system:

```
sage -t  "devel/sage/sage/graphs/graph.py"                  
**********************************************************************
File "/home/mabshoff/build-3.3.alpha6/sage-3.3.alpha6-fulvia/devel/sage/sage/graphs/graph.py", line 6298:
    sage: int(abs(M.determinant()))
Expected:
    712483534798848
Got:
    712483534798848L
**********************************************************************
```

So change int to integer.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 12:01:47

David,

I am seeing doctest failures in 

```
        sage -t -long devel/doc/const/const.tex # 3 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix_integer_dense.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/coding/guava.py # 1 doctests failed
        sage -t -long devel/sage/sage/coding/code_constructions.py # 8 doctests failed
        sage -t -long devel/sage/sage/coding/linear_code.py # 16 doctests failed
```


You implied that all problems had been addressed, but this was clearly not the case. If you doctested your patches and they do not pass doctest do not mark them ready for review since at least on your test box all tests should pass. If they did I am very surprised, but at least the const.tex failure does happen regardless. Please make sure that in the future you also test the documentation since this issue has cropped up repeatedly via patches submitted by you.

I am not comfortable with merging this code into 3.3 unless someone takes a look at the issue with 

```
Warning: this should never happen
```

One last thing: Disregard my comment above. You don't even need to make the result of abs an int since in either case it returns integer:

```
sage: type(M.determinant().abs())
<type 'sage.rings.integer.Integer'>
sage: type(abs(M.determinant()))
<type 'sage.rings.integer.Integer'>
```


Cheers,

Michael


---

Comment by wdj created at 2009-02-10 12:34:56

As I said in my comments, I have no idea why the "This should never happen" prints are there. I said this several times, so I'm sorry if my last comment suggested otherwise. I did not insert that print statement into gap.py and don't know who did. The correct computation appears after those print statements.


I did not get the doctest error in const.tex listed in the list of failures at the bottom. That is the way I determine which failures have occurred.


Regarding M.determinant(), I get a failure unless I do exactly as I did. The tests passed for me. (I think there is a bug in abs but am not sure.)


Regarding the matrix_integer_dense.pyx failure, that just never happened for me:


```
The following tests failed:


	sage -t  "devel/sage/sage/coding/linear_code.py"
	sage -t  "devel/sage/sage/coding/guava.py"
	sage -t  "devel/sage/sage/coding/code_constructions.py"
	sage -t  "devel/sage/sage/server/notebook/worksheet.py"
	sage -t  "devel/sage/sage/server/notebook/template.py"
	sage -t  "devel/sage/sage/server/notebook/avatars.py"
	sage -t  "devel/sage/sage/server/notebook/cell.py"
	sage -t  "devel/sage/sage/server/notebook/twist.py"
	sage -t  "devel/sage/sage/server/notebook/notebook.py"
Total time for all tests: 2434.5 seconds
```



Sorry for the miscommunication. If you tell me what to change I will change it but AFAIK, there are not more failures that I know of that I can fix.


---

Comment by mabshoff created at 2009-02-10 13:00:07

Replying to [comment:45 wdj]:

Hi David,

> As I said in my comments, I have no idea why the "This should never happen" prints are there. I said this several times, so I'm sorry if my last comment suggested otherwise. I did not insert that print statement into gap.py and don't know who did. The correct computation appears after those print statements.

Well, someone needs to fix the bug. One way would be to make them real warnings, i.e. they are not raised with the default settings. But looking at the code something fishy is going on.

> I did not get the doctest error in const.tex listed in the list of failures at the bottom. That is the way I determine which failures have occurred.

That is because you did not run the documentation doctests. You corrected the same bug in some other place in the Sage library in one of the above patches. 
 
> Regarding M.determinant(), I get a failure unless I do exactly as I did. The tests passed for me. (I think there is a bug in abs but am not sure.)

As I mentioned this is a 32 vs. 64 bit issue. On a 64 bit box the tests pass, but not on a 32 bit box. Printing Python ints (*not* Sage integers) causes issues like that on 32 vs. 64 bit platforms when the value is between an in and a long. Just drop the int() and you are good to go since in this case the determinant returns a Sage integer anyway.

> Regarding the matrix_integer_dense.pyx failure, that just never happened for me:\

I did not see any failure in matrix_integer_dense.pyx. What file do you mean?

<SNIP>

This is the result of your doctesting? The patches should have never been posted as ready for review. The notebook failures have nothing to do with this failure. Maybe you ought to develop patches in branches so you don't get unrelated doctest failures like that. I expect any patch posted for review to pass the doctest suite 100%. Anything else is an instant "needs work" by me unless the issue is trivially fixable. 
 
> Sorry for the miscommunication. If you tell me what to change I will change it but AFAIK, there are not more failures that I know of that I can fix.

Ok, please make 100% clear if all doctests passed for you or not. I have spend considerable time on building and testing this GAP.spkg and the related patches since I assumed it would actually worked while I have 10 tickets or so to fix on my own for the 3.3 release which needs to drop soon. Knowing what I know now I would not have touched these patches at all.

Cheers,

Michael


---

Comment by wdj created at 2009-02-10 13:51:35

You have a number of incorrect statements. I will list them in order.

>  That is because you did not run the documentation 
>  doctests. 

sage -testall runs doctests, so your claim is incorrect. The problem is that it appears that it does not (for me) print the doctest failures for the documentation. It used to do that and someone changed the behaviour.


> As I mentioned this is a 32 vs. 64 bit issue. On a 
> 64 bit box the tests pass, but not on a 32 bit box.
> Printing Python ints (*not* Sage integers) causes 
> issues like that on 32 vs. 64 bit platforms when the 
> value is between an in and a long. Just drop the 
> int() and you are good to go since in this case 
> the determinant returns a Sage integer anyway.


This statement is incorrect for me (amd64 ubuntu 8.10).
Maybe it is true for the machines you test with? As I 
said, I think abs may have a bug but in any case I will
change int to ZZ. (I confirmed the type statement you 
made before adding the int, this is why I think there is a bug. Maybe the prepaser is changing things?)


> Maybe you ought to develop patches in branches so 
> you don't get unrelated doctest failures like that.


You were the one who suggested I do the testing on sage.math. You can see from


```
http://sage.math.washington.edu/home/wdj/sagefiles/sage-3.3.alpha6/devel/
```

that I am using a branch. I've forgotten how long it's been since I've gotten all doctests to pass! I will try to make that clearer in the future though.


I'll post a patch with the 2 changes you suggested hopefully in the next several hours.


---

Comment by mabshoff created at 2009-02-10 14:05:27

Replying to [comment:47 wdj]:

Hi David,

> You have a number of incorrect statements. I will list them in order.
> 
> >  That is because you did not run the documentation 
> >  doctests. 
> 
> sage -testall runs doctests, so your claim is incorrect. The problem is that it appears that it does not (for me) print the doctest failures for the documentation. It used to do that and someone changed the behaviour.

No, -testall tests the Sage library and not the documentation. I do not recall that testall ever tested the documentation and I have been doing releases for well over a year now fulltime. If you look at the check target in the Makefile you will see that the DSage unit tests are run, then the documentation tests, then the Sage library tests. 

Sage's -tp doctests also the documentation on demand if SAGE_TEXT_TEX is set to "1", but that is not the default. 

> > As I mentioned this is a 32 vs. 64 bit issue. On a 
> > 64 bit box the tests pass, but not on a 32 bit box.
> > Printing Python ints (*not* Sage integers) causes 
> > issues like that on 32 vs. 64 bit platforms when the 
> > value is between an in and a long. Just drop the 
> > int() and you are good to go since in this case 
> > the determinant returns a Sage integer anyway.
> 
> 
> This statement is incorrect for me (amd64 ubuntu 8.10).

It is a well know fact that Python ints can print differently on 32 and 64 bit platforms and that the difference is the extra L in certain cases on 32 bit boxen. I have pointed that out twice before. 

> Maybe it is true for the machines you test with? As I 
> said, I think abs may have a bug but in any case I will
> change int to ZZ. (I confirmed the type statement you 
> made before adding the int, this is why I think there is a bug. Maybe the prepaser is changing things?)

No, this is Python behavior since you convert it to a Python int. Do not convert it and it will just work since abs() will return an integer AFAIK in this situation, but I can test that later. 

> 
> > Maybe you ought to develop patches in branches so 
> > you don't get unrelated doctest failures like that.
> 
> 
> You were the one who suggested I do the testing on sage.math. You can see from
> 
> {{{
> http://sage.math.washington.edu/home/wdj/sagefiles/sage-3.3.alpha6/devel/
> }}}
> that I am using a branch. I've forgotten how long it's been since I've gotten all doctests to pass! I will try to make that clearer in the future though.

I do not merge *any* patch which causes doctest failures and the 3.3.alpha6 binary I posted doctested perfect on sage.math when I bdisted. As I pointed out in the release notes in 

  http://groups.google.com/group/sage-devel/browse_thread/thread/48b893e904634273#

you needed to apply a patch to work around a relocation issue which everyone triggers when they use a binary, but I discovered that afterwards:

```
Merging for rc0 has already started and one bug made it into alpha6 
that can cause cloning to fail has been resolved. So please pull in 
the fix below 
#5205: Michael Abshoff: Set "# -*- coding: utf-8 -*-" encoding for 
sage/server/notebook/template.py [Reviewed by Mike Hansen] 
in case you run into trouble cloning. It also happens when you move 
the tree.
```


If you look at the ticket it clearly outlines the doctest failure related to the notebook you saw. The other six alphas doctested perfect out of the box on sage.math. 

> 
> I'll post a patch with the 2 changes you suggested hopefully in the next several hours.

Ok.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-10 15:40:12

Hi David,

as Carl just pointed out to me in IRC -testall does test the documentation, but it does not properly summarize any failure at the end together with the other failures. So neither one of us is right in some aspect about this ;)

Cheers,

Michael


---

Comment by wdj created at 2009-02-10 15:52:39

Yes, someone changed the printing for the documentation failures in sage -testall. It used to work but maybe that was long ago.


I'm attaching a patch which makes the change to const.tex 
you told me to make. I cannot get it to apply though and 
don't know what I did wrong.

> Do not convert it and it will just work since abs() will 
> return an integer AFAIK in this situation, but I can 
> test that later. 


This is again incorrect but you have now told me directly twice 
to do this, so I will do as you say. The 5th patch does 
exactly as you instructed. Because this does not work (as I 
also said at least twice now), I get more failures.


So, I will leave this as "needs work" since there is nothing 
else I know how to to fix this.


If anything, one thing this process of testing both on my 
phenom ubuntu 8.10 machine and sage.math has given me is a 
much greater appreciation for the frustrations you go 
through dealing with all the architectures you do!!





```



The following tests failed:                                                                                                                           


        sage -t  "devel/sage/sage/coding/linear_code.py"
        sage -t  "devel/sage/sage/coding/guava.py"      
        sage -t  "devel/sage/sage/coding/code_constructions.py"
        sage -t  "devel/sage/sage/server/notebook/worksheet.py"
        sage -t  "devel/sage/sage/server/notebook/template.py" 
        sage -t  "devel/sage/sage/server/notebook/avatars.py"  
        sage -t  "devel/sage/sage/server/notebook/cell.py"     
        sage -t  "devel/sage/sage/server/notebook/twist.py"    
        sage -t  "devel/sage/sage/server/notebook/notebook.py" 
        sage -t  "devel/sage/sage/graphs/graph.py"             
Total time for all tests: 2434.6 seconds

```


I did not apply the 5204 patch as I wasn't sure how that 
should be applied not that supposedly a clone (or is it?) 
was already seemingly created.


---

Comment by wdj created at 2009-02-10 15:54:50

this does not apply for me, but was meant to work for 3.3.alpha6.


---

Attachment

Replying to [comment:50 wdj]:
> Yes, someone changed the printing for the documentation failures in sage -testall. It used to work but maybe that was long ago.

Yes, it must have been broken for a long, long time. In 3.4 the documentation will be inside the devel tree, so the issue will be moot. 

> 
> I'm attaching a patch which makes the change to const.tex 
> you told me to make. I cannot get it to apply though and 
> don't know what I did wrong.

Check the repo, -sdist changes the version number. 
> This is again incorrect but you have now told me directly twice 
> to do this, so I will do as you say. The 5th patch does 
> exactly as you instructed. Because this does not work (as I 
> also said at least twice now), I get more failures.

Ok, this is what works:

```
sage: abs(Integer(M.determinant()))
712483534798848
```

I tested with a different matrix type where it worked out of the box without the Integer constructor.

<SNIP>

> I did not apply the 5204 patch as I wasn't sure how that 
> should be applied not that supposedly a clone (or is it?) 
> was already seemingly created.
 
If you apply the patch via Sage's interface it will be applied to the current clone only. You can always do an "hg import foo.patch" inside devel/sage-something.

Cheers,

Michael


---

Comment by was created at 2009-02-14 00:30:38


```
16:20 < wstein-3337> I think it's just that somebody re-enabled or implemented notification that a 
                     subprocess
16:20 < wstein-3337> is started/stopped.
16:20 < wstein-3337> And Steve (in gap.py) hadn't implemented handling of that.
16:20 < wstein-3337> The proper handling is to ignore it.
16:20 < wstein-3337> I'll post a 2-line patch.
```



---

Attachment

fix "this shouldn't happen" issue


---

Comment by mabshoff created at 2009-02-14 01:07:37

I need to adjust one patch slightly to fix one last issue, so positive review in total. 

Finally :)

Cheers,

Michael


---

Attachment

Update version of wdj's patch that works :)


---

Comment by mabshoff created at 2009-02-14 01:43:50

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 01:43:50

Merged the spkg as well as 

 * trac_3337-gap-docstrings.patch
 * trac_3337-gap-docstrings2.patch
 * trac_3337-gap-docstrings3.patch
 * trac_3337-gap-docstrings4.patch
 * trac_3337-gap-docstrings5.patch
 * trac_3337-const-tex.patch
 * trac_3337-gap_subprocesses.patch

Mike: note that there is a patch to const.tex that fixes one doctest.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 02:15:22

Note: all the above were merged in Sage 3.3.rc1.

Cheers,

Michael
