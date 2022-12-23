# Issue 7544: downloading packages with sage-spkg

Issue created by migration from https://trac.sagemath.org/ticket/7544

Original creator: mvngu

Original creation time: 2009-11-27 16:17:40

Assignee: tbd

At least with Sage 4.3.alpha0, doing

```
./sage -i <url>/<package>-x.y.z.spkg
```

won't download the given package name if `<url>/<package>-x.y.z.spkg` is a URL other than that on the Sage website. The issue was reported in [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0df661d74b620901).




When one issues the following command:

```
sage -i <package>
```

then if <package> is already installed, one expects Sage to report that and quit trying to install `<package>`. In case, one really wants to install <package> regardless of whether or not `<package>` is already installed on one's local Sage installation, the following incantation should be used:

```
sage -f <package>
```

The documentation for installing an spkg, as output by "`sage -h | -advanced`", clearly documents the behaviour of the options "`-i`" and "`-f`" so I think we need to document the specific values that `<package>` can take. 




Suppose for discussion that `<package>-x.y.z.spkg` is a Sage package, whether that be in the standard, optional or experimental repository. At the very least, one expects both of the options "`-i`" and "`-f`" to consider the following as valid values:

 1. `<package>-x.y.z`, i.e. the name of the package plus the package's version numbers.
 1. the full name `<package>-x.y.z.spkg`, i.e. the name of the package in addition to the version numbers and the ".spkg" extension.
 1. `<URL>/<package>-x.y.z.spkg`, i.e. the full URL where the package is hosted. This can be a URL on the Sage website or somewhere else.
 1. `/path/to/<package>-x.y.z.spkg`, i.e. the package is found somewhere in your file system and you're giving an absolute or relative path to the package.

At least with Sage 4.3.alpha0, almost all of the above four values are valid. The exception is the reported issue, i.e. `<URL>/<package>-x.y.z.spkg` cannot be a URL other than that on the Sage website. Incidentally, with Sage 4.3.alpha0 one can also do "`sage -i <package>`", where `<package>` is just the package name without the version numbers nor the ".spkg" extension. I think all of the above four values should be valid and the install script should process them as valid values.


---

Comment by mvngu created at 2009-11-27 16:25:53

based on Sage 4.3.alpha0


---

Comment by mvngu created at 2009-11-27 16:53:13

Changing status from new to needs_review.


---

Attachment

The patch `trac_7544-sage-spkg.patch` should be applied to the script repository. It changes the file `SAGE_ROOT/local/bin/sage-spkg` so that one can install an spkg by passing any of the above four values to the options "`-i`" and "`-f`".


---

Comment by mhansen created at 2009-12-01 05:28:43

Resolution: fixed


---

Comment by mhansen created at 2009-12-01 05:28:43

Looks good.


---

Comment by mvngu created at 2009-12-09 01:09:28

This is a follow-up to #7355.


---

Comment by ddrake created at 2010-01-23 05:52:29

Unfortunately, this patch breaks the functionality introduced at #7355. That ticket made it so that in sage-spkg, at line 195 (or so), `$PKG_NAME` (which we get from `$1`) has been munged so that if no version number was provided, the appropriate one has now been added. However, the patch here comments out the line that uses `$PKG_NAME` and simply uses `$1`, thereby bypassing everything that we try to do in #7355. This patch is supposed to be a followup to #7355, but it completely breaks everything that that ticket was intended to do! Even with a casual inspection of the code -- which amounts to changing one line -- it should have been pretty obvious that blithely using `$1` wasn't going to work.

For example, if you try `sage -i vtk`, you'll see that it searches and finds that version 5.0.2 is the current version -- but then goes and tries to download a bare "vtk.spkg":

```
drake@klee:/opt/sage$ sage -i vtk
Installing vtk
Calling sage-spkg on vtk
Warning: Attempted to overwrite SAGE_ROOT environment variable
vtk
Machine:
Linux klee 2.6.31-9-rt #152-Ubuntu SMP PREEMPT RT Thu Oct 15 13:22:24 UTC 2009 x86_64 GNU/Linux
Deleting directories from past builds of previous/current versions of vtk
/opt/sage/local/bin/sage-spkg: file vtk does not exist
Attempting to download it.
Searching for latest version of vtk
Found package vtk-5.0.2
http://www.sagemath.org//packages/optional/vtk.spkg --> vtk.spkg
[ ]
http://www.sagemath.org//packages/standard/vtk.spkg --> vtk.spkg
[ ]
http://www.sagemath.org//packages/experimental/vtk.spkg --> vtk.spkg
[ ]
http://www.sagemath.org//packages/archive/vtk.spkg --> vtk.spkg
[ ]
**********************************************************************
* Unable to download vtk
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
sage: Failed to download package vtk-5.0.2 from http://www.sagemath.org/
```


I'll open another ticket to fix this.


---

Comment by ddrake created at 2010-01-25 04:55:52

The followup ticket is #8043.
