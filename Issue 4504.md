# Issue 4504: Sage's .spkg extension

Issue created by migration from https://trac.sagemath.org/ticket/4504

Original creator: mvngu

Original creation time: 2008-11-12 22:52:44

Assignee: tba

Keywords: .spkg extension, Sage packages

At [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/3b877b874eda9e62), it's suggested that there should be a README.txt file to briefly explain the .spkg extension of Sage packages and pointers to more info.


---

Comment by mvngu created at 2008-11-12 22:55:13

brief info on the .spkg extension


---

Attachment

The patch *trac_4504.patch* creates a new file to briefly explain Sage's .spkg files. It also contains pointers to more info on the structure of Sage packages. It was created using sage-3.1.4 and the new file to be created by this patch should be

```
SAGE_ROOT/spkg/README.txt
```



---

Comment by mvngu created at 2008-11-12 23:00:07

Changing assignee from tba to mvngu.


---

Comment by GeorgSWeber created at 2008-11-13 00:38:26

Looks fine. Thumbs up!


---

Comment by mabshoff created at 2008-11-13 00:43:12

This won't work since it will not survive an -sdist. I am not quit sure where to best stick it, but somewhere in the doc or the global README.txt would be easier.

Cheers,

Michael


---

Comment by was created at 2008-11-13 05:56:02

Changing assignee from mvngu to was.


---

Comment by was created at 2008-11-13 05:56:02

1. How did you make a patch to add a file to SAGE_ROOT/spkg?  There's no hg repo in there?  Huh?!

2. Michael -- the file is in the right place.  The solution is to modify the -sdist command so that it copies the new README.txt file into the right place.   This will have to be done as a patch to the hg_scripts directory (SAGE_ROOT/local/bin/).

3. One thing that concerns me is it would also be good to have a different README.txt for binaries (i.e., bdist), since then spkg/standard has all the same spkg's, but they are empty!

William


---

Comment by mvngu created at 2008-11-13 22:33:42

Replying to [comment:4 was]:
> 1. How did you make a patch to add a file to SAGE_ROOT/spkg?  There's no hg repo in there?  Huh?!


Before making the patch, I loaded up a console Sage session and investigated all the `hg_*` family of commands. But I wasn't able to find one that would allow me to work with the directory `SAGE_ROOT/spkg`. So from the `SAGE_ROOT` directory, I executed the command `hg init`, created the file `SAGE_ROOT/spkg/README.txt`, and executed the command `hg add spkg/README.txt`. Then I edited that README.txt file with the text:

```
Sage packages 
============= 

This directory contains core Sage packages.  Sage packages are 
distributed as .spkg files, which are .tar.bz2 files (or tar files) 
but have the extension .spkg to discourage confusion.  Although Sage 
packages are packed using tar and/or bzip2, please note that .spkg 
files contain control information (installation scripts and metadata) 
that are necessary for building and installing them.  For more 
information on the structure of .spkg files, please refer to the Sage 
Developer's Guide in your local installation of Sage at 

SAGE_ROOT/devel/doc-main/html/prog/index.html 

or visit the URL 

http://www.sagemath.org/doc/prog 

Additional Sage packages can be found at 

http://www.sagemath.org/download-packages.html 
```

I then used mercurial to create the above patch. It was very careless of me not to mention that earlier. Sorry, folks. But if you're having trouble applying the patch, then perhaps you or the release manager can create the file `SAGE_ROOT/spkg/README.txt` with the above text.


---

Comment by GeorgSWeber created at 2008-11-14 22:49:42

A possible solution would be to put this file in another location, and adapt "sage -sdist" so that it is copied to the intended place.

Then we would need another "README.txt" for binary distributions explaining the empty spkg's (which puzzled my quite a bit when I was Sage newbie), also put in "another location", and copied by "sage -bdist" to the very same place.

I don't think this is a ticket to prevent 3.2 from going out, so I bump the Milestone up.


---

Comment by mvngu created at 2008-11-20 22:32:56

Replying to [comment:6 GeorgSWeber]:
> Then we would need another "README.txt" for binary distributions explaining the empty spkg's (which puzzled my quite a bit when I was Sage newbie), also put in "another location", and copied by "sage -bdist" to the very same place.


I'm not at all familiar with binary distros of Sage, since I've never got hold of a copy of a binary release. So in that sense, I'm not exactly sure how to go about writing the README.txt that you suggest. But from your comment, I guess that such a README.txt for a binary distro would include the same (or similar) text as contained in the above patch.


---

Comment by GeorgSWeber created at 2008-11-21 11:40:06

>But from your comment, I guess that such a README.txt for a binary distro would include the same (or similar) text as contained in the above patch. 
Not really --- in a binary distro, the files "sage_scripts-3.2.spgk" and so on all exist, but they are all empty files. The "spkg/standard" directory then looks pretty much the same as the "spkg/installed" directory, there is no real data contained in it except for the list of names of empty files. Which is confusing and deserves some kind of explanatory "README.txt", which would have to explain this.


---

Comment by GeorgSWeber created at 2008-11-21 12:22:15

BTW --- if you have a sage src distro, just issue "sage -bdist my_version" and a binary distribution will be built. You can look at it then (in "$SAGE_ROOT/dist/" if I remember correctly).


---

Attachment

explain .spkg files for source distros


---

Comment by mvngu created at 2008-12-06 01:51:12

explain .spkg for binary distros


---

Attachment

The files *trac_4504-spkg-src.tex* and *trac_4504-spkg-bin.tex* are readme files that briefly explain Sage's .spkg extensions. Due to some stupidity on my part, I named them with the ".tex" extension and forgot to change the ".tex" to ".txt". Sorry folks.



The file *trac_4504-spkg-src.tex* gives some brief explanation about files with the .spkg extension as part of their name. That is, *trac_4504-spkg-src.tex* is a replacement for *trac_4504.patch*, so we can ignore *trac_4504.patch*. For source distributions of Sage, *trac_4504-spkg-src.tex* should be renamed to "README.txt" and placed under the directory `SAGE_ROOT/spkg` or somewhere under that directory tree.



The file *trac_4504-spkg-bin.tex* gives some brief explanation about the empty .spkg files found in binary distributions of Sage. For binary distributions of Sage, *trac_4504-spkg-bin.tex* should be renamed to "README.txt" and placed under the directory `SAGE_ROOT/spkg` or somewhere under that directory tree.


---

Comment by was created at 2008-12-06 21:38:39

Hi,

Right now in a fresh install of sage-3.2.2.alpha0, there is a README.txt file in spkg/standard/.  It is simply an OLD out-of-date version of the README.txt file in SAGE_ROOT.  I think it should be completely deleted.  Then a file README.txt in the spkg directory should be created with two short sections, and those sections should contain the text mvngu wrote.  That's it.

I'm not convinced about having all the extra infrastructure for two separate readme's for the source and binary versions of Sage.  Even if that is a good idea, it could be a separate ticket, since as is, this ticket would not be in "with patch; needs review" status if that extra stuff has to be done. 

So in short, I suggest doing the following:
  1. (see attached patch trac_4504_scripts.patch) Add the line

```
cp -p $PKGDIR/README.txt $TMP/$PKGDIR/
```

as line 64 of local/bin/sage-sdist. The analogue of this is currently already done in sage-bdist (line 90).  

  2. Delete spkg/standard/README.txt

  3. Make a new spkg/README.txt file that has two sections, one for each of Minh's patches. 

By the way, it's been suggested above that the spkg/standard/*.spkg files are empty in a bdist.  They aren't empty. They contain the single sentence: "Placeholder spkg file so this binary version of Sage knows this package version used when installing Sage."


Also, I have issues with the actual wording of mvngu's patch, which is:

```
4 	If you've downloaded a binary distribution of Sage, you'd likely see
5 	a number of files with the extension ".spkg" under the directory
6 	SAGE_ROOT/spkg. In a binary distribution of Sage, such files are empty
7 	files and you don't need to do anything about them. Just ignore such
8 	files for the moment.
9 	
10 	However, note that in a source distribution of Sage, .spkg files under
11 	SAGE_ROOT/spkg are core Sage packages, which extend Sage's
12 	functionalities.
```


First, there are no spkg files in SAGE_ROOT/spkg; they are in SAGE_ROOT/spkg/standard/.
Second, it's not "likely" -- they will always be there with probability 1.
Third, they aren't empty, as mentioned above. 
Fourth, in the case of source they don't "extend Sage's functionalities", they *are* the source code that defines Sage.    So I would replace all the above with:

```
The directories SAGE_ROOT/spkg/standard and SAGE_ROOT/spkg/optional contain spkg's.  
In a source install, these are all Sage spkg files (actually .tar or .tar.bz2 files), which are the source code that defines Sage.  In a binary install some of these may be small placeholder files to save space.
```



---

Attachment


---

Comment by mvngu created at 2008-12-07 21:21:13

The attached file *trac_4504-draft2.txt* is a revised draft of a README file explaining Sage's .spkg extension. This second draft has been re-worded and incorporates suggestions by [comment:12 was]. Draft 2 replaces *trac_4504-spkg-src.tex* and *trac_4504-spkg-bin.tex*. 



So at the moment, the job of the reviewer(s) is to review the patch *trac_4504_scripts_sdist.patch* and the text file *trac_4504-draft2.txt*.


---

Comment by jhpalmieri created at 2008-12-09 22:10:05

Is it worth changing

```
SAGE_ROOT/devel/doc-main/html/prog/index.html 
```

to

```
SAGE_ROOT/doc/prog/index.html 
```

in the various places in which this occurs?


---

Comment by mvngu created at 2008-12-09 22:23:25

Replying to [comment:14 jhpalmieri]:
> Is it worth changing
> {{{
> SAGE_ROOT/devel/doc-main/html/prog/index.html 
> }}}
> to
> {{{
> SAGE_ROOT/doc/prog/index.html 
> }}}
> in the various places in which this occurs?


I don't have a copy of Sage with me at the moment, but I think `SAGE_ROOT/doc` is a symbolic link to `SAGE_ROOT/devel/doc-main`. If in the future the official documentation is moved to somewhere else, say `SAGE_ROOT/path/to/doc-main`, then I would expect that `SAGE_ROOT/doc` would still point to `SAGE_ROOT/path/to/doc-main`. If that is the case, and a reason for having a symbolic link to doc-main, then we should use the symbolic link instead of the path to doc-main.


---

Comment by GeorgSWeber created at 2008-12-29 21:17:17

Target time for the review: January 14th


---

Comment by GeorgSWeber created at 2009-01-20 23:43:05

Review: Looks good, but I have to test it against 3.3.alpha0 yet.


---

Comment by GeorgSWeber created at 2009-02-14 23:17:09

Hi Michael,

this can go as-is into 3.3. There are three things to do:

A) Delete the "README.txt" file (no repo) under $SAGE_ROOT/spkg/standard/

B) Copy the "trac_4504-draft2.txt" as "README.txt" file under $SAGE_ROOT/spkg/
   (this is intentionally one directory "above" where the old file was)

C) Apply the patch "trac_4504_scripts_sdist.patch" from William to /local/bin

Tested with 3.3.rc0.

Cheers, gsw


---

Comment by mabshoff created at 2009-02-15 01:09:29

I consider this patch too risky since it has to be tested via sdisting given the issue that is fixes, so better luck post 3.3 :(

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-02-15 10:22:03

Understandable. Given that we do not need a rebase for 3.4.1, and the "minor" priority of this ticket, a wise decision. Good luck for 3.3!

Cheers, gsw


---

Comment by mabshoff created at 2009-02-15 10:30:40

Replying to [comment:21 GeorgSWeber]:
> Understandable. Given that we do not need a rebase for 3.4.1, and the "minor" priority of this ticket, a wise decision. Good luck for 3.3!

Well, there will be non-trivial work done on -sdist and -bdist in 3.4, so this time might also go in. We will see.

> Cheers, gsw

Cheers,

Michael


---

Comment by mvngu created at 2009-03-19 02:11:35

I think some parts of *trac_4504-draft2.txt* needs to be rewritten to take into account changes in where the doc directory has been moved to in the Sage 3.4.x series. I intend to do a 3rd draft some time in the next few days, unless someone beats me to it.


---

Comment by mvngu created at 2009-03-24 09:29:10

updated 2nd draft


---

Attachment

The file *trac_4504-draft2.txt* is an updated 2nd draft to reflect changes in where the standard documentation is now located since Sage 3.4.


---

Comment by GeorgSWeber created at 2009-03-24 20:19:58

Yep, positive review (again).

The patch from William still applies as-is to Sage-3.4. (See me A-B-C step procedure above.)

Cheers,
gsw


---

Comment by mhansen created at 2009-06-01 04:38:09

Resolution: fixed


---

Comment by mhansen created at 2009-06-01 04:38:09

Merged trac_4504_scripts_sdist.patch and trac_4504-draft2.txt in 4.0.1.alpha0.
