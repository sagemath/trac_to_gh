# Issue 5295: Make Maxima not read global config files

Issue created by migration from https://trac.sagemath.org/ticket/5295

Original creator: mabshoff

Original creation time: 2009-02-17 20:12:49

Assignee: mabshoff

From http://groups.google.com/group/sage-devel/browse_thread/thread/e7f7ddd0ad86971d


```
I finally got Sage.app working.  Still there seems 
something a bit odd about the fix.  I had, in my home 
directory, a .maxima directory with a file named 
maxima-init.mac that sets certain maxima preferences. 
Once I deleted this file, everything worked fine.  As I 
understand it though, the sage directory is supposed to be 
independent of the rest of the system.  Evidently, the 
latest version of sage is reading information from my 
home directory.  My old sage (v3.0.1) runs fine without 
removing the file, however. 

The two lines in the maxima-init file were exactly the 
following: 
set_plot_option([gnuplot_term, aqua]); 
set_plot_option([gnuplot_pipes_term, aqua]); 
Of course, now I can no longer plot from my standalone 
copy of maxima. :) 
One final comment: George's patch was unnecessary.  I 
hope I didn't send you on a wild goose chase. 

Mark McClure 
```



---

Comment by nbruin created at 2010-01-17 00:42:19

Changing assignee from mabshoff to nbruin.


---

Comment by nbruin created at 2010-01-17 00:42:19

The key here seems to be the `-userdir=` option. To illustrate (warning, this will seriously mess up maxima configuration you may have in your homedir. Back up `~/.maxima` if you have one)

First to show the effect of the option:

```
> mkdir .maxima
> echo "x : 1;" > .maxima/maxima-init.mac
> mkdir othermax
> echo "x : 2;" > othermax/maxima-init.mac
> maxima --batch-string "x;"
;;; Loading #P"/usr/local/sage/4.3/local/lib/ecl/defsystem.fas"
;;; Loading #P"/usr/local/sage/4.3/local/lib/ecl/cmp.fas"
;;; Loading #P"/usr/local/sage/4.3/local/lib/ecl/sysfun.lsp"
Maxima 5.19.1 http://maxima.sourceforge.net
Using Lisp ECL 9.10.2
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1)                                  x
(%o1)                                  1
> maxima --userdir="$HOME/othermax" --batch-string "x;"
;;; Loading #P"/usr/local/sage/4.3/local/lib/ecl/defsystem.fas"
;;; Loading #P"/usr/local/sage/4.3/local/lib/ecl/cmp.fas"
;;; Loading #P"/usr/local/sage/4.3/local/lib/ecl/sysfun.lsp"
Maxima 5.19.1 http://maxima.sourceforge.net
Using Lisp ECL 9.10.2
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1)                                  x
(%o1)                                  2
```


So, with the above `~/.maxima/maxima-init.mac` in place, currently the result is:

```
>  sage -c 'print maxima("x")'
                                       1
```

After applying attached patch "bug5295.patch" the result should be

```
> sage -c 'print maxima("x")'
                                       x
```

Since serious testing of this option involves making files in very sensitive locations, I think including a doctest for this behaviour is inadvisable.


---

Comment by nbruin created at 2010-01-17 00:43:33

Change maxima interface to look at $DOT_SAGE/maxima rather than "~/.maxima"


---

Comment by nbruin created at 2010-01-17 00:43:55

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-01-18 03:39:54

Here's how to replicate the errors with Sage 4.3.1.rc0. Create a hidden directory in your home directory called ".maxima":

```
[mvngu@mod ~]$ pwd
/home/mvngu
[mvngu@mod ~]$ mkdir .maxima
[mvngu@mod ~]$ cd .maxima/
[mvngu@mod .maxima]$ pwd
/home/mvngu/.maxima
```

Under the hidden directory ".maxima", create the Maxima initialization file "maxima-init.mac" with some initialization code:

```
[mvngu@mod .maxima]$ cat maxima-init.mac 
set_plot_option([gnuplot_term, aqua]);
set_plot_option([gnuplot_pipes_term, aqua]);
```

Now load the version of Maxima that is shipped with Sage. This should result in some errors thrown by Maxima:

```
[mvngu@mod sage-4.3.1.rc0-5295-maxima]$ pwd
/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima
[mvngu@mod sage-4.3.1.rc0-5295-maxima]$ ./sage -maxima
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/defsystem.fas"
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/cmp.fas"
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 9.10.2
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
set_plot_option: Unknown plot option specified: gnuplot_pipes_term
 -- an error. To debug this try: debugmode(true);
Maxima encountered a Lisp error:

 THROW: The catch MACSYMA-QUIT is undefined.

Automatically continuing.
To enable the Lisp debugger set *debugger-hook* to nil.
```

I might be missing something here. But after applying [bug5295.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5295/bug5295.patch), I still received the same error:

```
[mvngu@mod sage-4.3.1.rc0-5295-maxima]$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 1.50203704834e-05 seconds
Finished compiling Cython code (time = 0.346451997757 seconds)
running install
running build
running build_py
copying sage/interfaces/maxima.py -> build/lib.linux-x86_64-2.6/sage/interfaces
running build_ext
Total time spent compiling C/C++ extensions:  0.0161008834839 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/interfaces/maxima.py -> /dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/python2.6/site-packages/sage/interfaces
byte-compiling /dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/python2.6/site-packages/sage/interfaces/maxima.py to maxima.pyc
running install_egg_info
Removing /dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m1.409s
user	0m1.050s
sys	0m0.360s
[mvngu@mod sage-4.3.1.rc0-5295-maxima]$ ./sage -maxima
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/defsystem.fas"
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/cmp.fas"
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 9.10.2
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
set_plot_option: Unknown plot option specified: gnuplot_pipes_term
 -- an error. To debug this try: debugmode(true);
Maxima encountered a Lisp error:

 THROW: The catch MACSYMA-QUIT is undefined.

Automatically continuing.
To enable the Lisp debugger set *debugger-hook* to nil.
```

It also failed when I loaded Maxima from within a Sage session:

```
[mvngu@mod sage-4.3.1.rc0-5295-maxima]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: !maxima
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/defsystem.fas"
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/cmp.fas"
;;; Loading #P"/dev/shm/mvngu/sage-4.3.1.rc0-5295-maxima/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 9.10.2
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
set_plot_option: Unknown plot option specified: gnuplot_pipes_term
 -- an error. To debug this try: debugmode(true);
Maxima encountered a Lisp error:
| Sage Version 4.3.1.rc0, Release Date: 2010-01-15                   |
| Type notebook() for the GUI, and license() for information.        |
 THROW: The catch MACSYMA-QUIT is undefined.

Automatically continuing.
To enable the Lisp debugger set *debugger-hook* to nil.
```



---

Comment by nbruin created at 2010-01-19 04:26:50

The patch fixes that the maxima expect interface from within sage
ignores `$HOME/.maxima`. I think people would expect maxima itself to work as described in the maxima manual, and hence by default look in `$HOME/.maxima` for configuration files.

If someone wants the maxima distributed with sage to *never* look at `$HOME/.maxima` then one should edit the `sage/local/bin/maxima` script to use the {{{--userdir}} command line option by default. I think that is wrong.


---

Comment by nbruin created at 2010-01-20 00:21:32

> If someone wants the maxima distributed with sage to *never* look at `$HOME/.maxima` then one should edit the `sage/local/bin/maxima` script to use the {{{--userdir}} command line option by default. I think that is wrong.

However, should someone want to do this anyway, then the environment variable $MAXIMA_USERDIR should do the trick. Thus,

```
MAXIMA_USERDIR=$DOT_SAGE/maxima
export MAXIMA_USERDIR
```

could just go into sage_env or something similar. This would be an alternative to the attached patch.


---

Comment by mvngu created at 2010-01-20 18:45:24

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-20 18:45:24

Looks good. Work as advertised.


---

Comment by mvngu created at 2010-01-22 22:31:33

Resolution: fixed
