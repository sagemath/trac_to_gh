# Issue 6563: [with patch; needs review] Singular fails to install header files, since it fails to find install-sh

Issue created by migration from https://trac.sagemath.org/ticket/6563

Original creator: drkirkby

Original creation time: 2009-07-19 23:03:29

Assignee: tbd

CC:  malb

Keywords: solaris

singular-3-1-0-2-20090620 appeared to install on a Solaris machine, with the file $SAGE_HOME/spkg/installed/singular-3-1-0-2-20090620 existing. 

However, it was later realised that some of the singular header files were not copied to $SAGE_HOME/local/include/singular. Closer inspection of the install.log showed: 


```

make[1]: Entering directory 
`/export/home/drkirkby/sage/sage-4.1/spkg/build/singular-3-1-0-2-20090620/src/kernel'
./mkinstalldirs /export/home/drkirkby/sage/sage-4.1/local/include/singular
for file in *.h; do ../.././install-sh -c $file 
/export/home/drkirkby/sage/sage-4.1/local/include/singular; done
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
/bin/sh: ../.././install-sh: not found
```




Changing to the directory 
`/export/home/drkirkby/sage/sage-4.1/spkg/build/singular-3-1-0-2-20090620/src/kernel' 
and doing an 'ls' of ../.././ I see that it got me to the root directory 
of the singular installation - by that I mean where spkh-install, 
SPKG.txt etc exist.

Copying install-sh to there solved the problem.

Willem Jan Palenstijn said on sage-devel:

''If I understand things correctly, this is what happens:
when src/Singular/config.status outputs ../kernel/Makefile, it
interprets the two slashes in that path as the output file being two
subdirectories down from Makefile, and so adjusts (the correct)
'./install.sh' (i.e., actually src/Singular/install-sh) to (the broken)''

'../.././install.sh' .

''The reason this doesn't show up on my system (and presumably other
systems) is that /usr/bin/install (with an absolute path) is found and used
instead of ./install.sh.''

[actually, the missing file is install-sh, not install.sh]

Whatever may or may not be the real reason for this, the simplest solution is to simply copy install-sh to the top level directory. I know it's not normal to do it this way, but it might be the quickest. I've created a patch based on doing just that. 
 http://sage.math.washington.edu/home/kirkby/Solaris-fixes/singular-3-1-0-2-20090620.p0/

The actual .spkg file is:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/singular-3-1-0-2-20090620.p0/singular-3-1-0-2-20090620.p0.spkg

It should be noted there are about 10-15 identical copies of the file in the source distribution! Perhaps someone before had trouble find the file. 

So far this has only been seen on Solaris I believe. but is clearly not specifically a Solaris bug. 

Dave 



---

Comment by mvngu created at 2009-07-23 07:17:19

I've checked in all changes in your name. The updated SPKG is up at

http://sage.math.washington.edu/home/mvngu/patch/singular-3-1-0-2-20090620.p0.spkg


---

Comment by mvngu created at 2009-07-24 00:06:17

The SPKG at

http://sage.math.washington.edu/home/mvngu/patch/singular-3-1-0-2-20090620.p0.spkg

builds OK on the machine t2 running Solaris. (It also compiles on Linux.)


---

Comment by mvngu created at 2009-07-24 00:06:17

Resolution: fixed


---

Comment by jdemeyer created at 2011-12-10 00:21:53

Did this ever get reported upstream?  Just wondering whether the fix is still needed today (making a new Singular spkg at #12137).

This quote from the description really made me laugh:
> It should be noted there are about 10-15 identical copies of the file in the source distribution! Perhaps someone before had trouble find the file.

So many copies but still not enough...
