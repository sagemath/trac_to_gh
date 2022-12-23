# Issue 9083: 'make distclean' fails to remove some files or directories.

Issue created by migration from https://trac.sagemath.org/ticket/9083

Original creator: drkirkby

Original creation time: 2010-05-29 07:30:09

Assignee: GeorgSWeber

Keywords: beginner

Conventionally 'make distclean' removes all traces of a build process, leaving only the original files. 

However, at least the following four files or directories are being left after running 'make distclean'.


```
./.BUILDSTART 
dochtml.log
spkg/install
spkg/installed
```

There is a section in the makefile

```
distclean:
        make clean
        rm -rf local
        rm -rf spkg/installed/*
        rm -f install.log
        rm -f test.log testall.log testlong.log ptest.log ptestlong.log
        rm -rf data
        rm -rf dist
        rm -rf devel
        rm -rf doc
        rm -rf examples
        rm -rf sage-python
        rm -rf spkg/build
        rm -rf spkg/archive
        rm -rf ipython
        rm -rf matplotlibrc
        rm -rf tmp
```


The two files and two directories need adding to that section. There may be other files created too. The way to find any new files or directories would be to 

 * Extract the Sage tarball.
 * Build Sage fully. 
 * Run the following two commands from the top level Sage directory.
 

```
$ 'make distclean'
$ find . -mtime -2
```


That will list any files or directories updated in the last two days. 

The following files
  * sage-README-osx.txt
  * COPYING.txt
  * README.txt

are having their modification times changed. I think that is undesirable, but that is another problem and the subject of #9082. So the changes to the makefile should not remove those 3 files, despite their recent modification times. 




---

Comment by ddrake created at 2010-06-01 07:52:58

patch for SAGE_ROOT/makefile


---

Attachment

The attached patch removes .BUILDSTART, dochtml.log, spkg/install, and spkg/installed. It's a regular unified diff, since SAGE_ROOT isn't in a Mercurial repo.

Hrm, I see the "beginner" tag...I hope I'm not stepping on any beginner's toes here! Although changing files in SAGE_ROOT is a bit strange, since they're not version controlled.


---

Comment by drkirkby created at 2010-06-01 08:34:14

I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line


```
	rm -rf spkg/installed/*
```


can actually be removed, as your 


```
	rm -rf spkg/installed
```


will do it, but it does not make much difference. 

I've got another patch I marked 'beginner' which might well be something that is a bit unusual in Sage, (though trivial). I better revisit that one and see if 'beginner' should be removed. 

Dave


---

Comment by drkirkby created at 2010-06-01 08:34:14

Changing assignee from GeorgSWeber to drkirkby.


---

Comment by ddrake created at 2010-06-01 08:34:31

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-06-01 09:10:44

Replying to [comment:2 drkirkby]:
> I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line
> 
> {{{
> 	rm -rf spkg/installed/*
> }}}
> 
> can actually be removed, as your 
> 
> {{{
> 	rm -rf spkg/installed
> }}}
> 
> will do it, but it does not make much difference.

I think those actually are different because of the trailing slash -- if we do

```
rm -rf spkg/installed*
```

I think that will get everything, right? If so, I can change the patch.
> 
> I've got another patch I marked 'beginner' which might well be something that is a bit unusual in Sage, (though trivial). I better revisit that one and see if 'beginner' should be removed. 
> 
> Dave


---

Comment by drkirkby created at 2010-06-01 22:20:37

Replying to [comment:4 ddrake]:
> Replying to [comment:2 drkirkby]:
> > I stuck 'beginner' since the change to makefile was trivial, but I do take your point that it is a bit different to most other changes in Sage. The line
> > 
> > {{{
> > 	rm -rf spkg/installed/*
> > }}}
> > 
> > can actually be removed, as your 
> > 
> > {{{
> > 	rm -rf spkg/installed
> > }}}
> > 
> > will do it, but it does not make much difference.
> 
> I think those actually are different because of the trailing slash -- if we do
> {{{
> rm -rf spkg/installed*
> }}}
> I think that will get everything, right? If so, I can change the patch.

The trailing slash should make no difference


```
rm -rf spkg/installed
```


will remove the directory spkg/installed and of course anything in any subdirectory of spkg/installed. 

In contrast


```
rm -rf spkg/installed*
```


would remove anything starting with spkg/installed, such as 


```
spkg/installeda
spkg/installedb
spkg/installedc
spkg/installed-but-do-not-delete-this-directory
```

 
I have removed the 'beginner' tag. 

Dave


---

Comment by drkirkby created at 2010-06-01 22:20:37

Changing keywords from "beginner" to "".


---

Comment by jhpalmieri created at 2010-06-21 22:54:47

I think that the directory spkg/optional should also be removed.


---

Attachment

the file SAGE_ROOT/makefile


---

Attachment

diff between original makefile and the one I attached


---

Comment by jhpalmieri created at 2010-06-27 05:39:50

Here's a new version of "makefile" along with "makefile-new.patch" which is the diff between the current makefile and the new version.  Rebased against 4.5.alpha0.


---

Comment by jhpalmieri created at 2010-06-27 05:44:01

By the way, we shouldn't remove spkg/install, because this file is there when you first unpack the Sage tar file, and it is used when you type "make": when you run "make" from SAGE_ROOT, the following command gets executed:

```
cd spkg && ./install all 2>&1 | tee -a ../install.log
```

Admittedly, I think the file spkg/install gets overwritten when the sage_scripts spkg gets installed, but if the release manager has done their job right, the new file should be identical to the old one.  Regardless, removing it will break "make" for Sage.


---

Comment by mpatel created at 2010-07-07 05:06:30

Also delete `docpdf.log`.


---

Attachment

Diff of `makefile.2` vs. 4.5.alpha4.


---

Attachment

I've attached a reviewer's update that also deletes `docpdf.log`.


---

Comment by jhpalmieri created at 2010-07-07 05:41:44

Replying to [comment:9 mpatel]:
> I've attached a reviewer's update that also deletes `docpdf.log`.

That change looks good to me.


---

Comment by mpatel created at 2010-07-07 06:37:57

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-07 06:39:18

To the release manager:  Copy just [attachment:makefile.2] to `SAGE_ROOT/`.


---

Comment by ddrake created at 2010-07-22 23:39:40

Replying to [comment:12 mpatel]:
> To the release manager:  Copy just [attachment:makefile.2] to `SAGE_ROOT/`.

Done, in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-22 23:39:40

Resolution: fixed
