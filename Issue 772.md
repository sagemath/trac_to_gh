# Issue 772: Interface to QEPCAD for quantifier elimination and solving systems of inequalities

archive/issues_000772.json:
```json
{
    "body": "Assignee: was\n\nCC:  burcin\n\nQEPCAD uses cylindrical algebraic decomposition to eliminate quantifiers in\nstatements.  QEPCAD takes the statement\n\n\n```\nthere exists an x such that a*x2 + b*x + c = 0 and a /= 0 (i.e., a!=0)\n```\n\n\nand eliminates the quantifier and answers that:\n\n\n```\na /= 0 and 4 a c - b^2 <= 0\n(i.e., a!=0 and 4ac-b^2<=0)\n```\n\n\nIn other words, it gives you the conditions of a solution satisfying\nyour original statement.  See more examples at [http://www.cs.usna.edu/~qepcad/B/examples/Examples.html](http://www.cs.usna.edu/~qepcad/B/examples/Examples.html)\n\nQEPCAD is not currently GPL and depends on the saclib library, which currently is not GPL.  However, both of those could change if there was interest.\n\nDavid Joyner talked with Chris Brown, and reported that:\n\n  I spoke with Chris Brown, who is essentially now the maintainer of\nqepcad. Here is his response:\n\n  \"Saclib's actual status is probably a bit up in the air.  What I might\n  call the saclib \"stakeholders\" had agreed to GPL it, but everybody\n  was, I guess, too busy to do anything about it.  Qepcad's status is\n  similar ... except that my contributions are necessarily public\n  domain.\"\n\n  In a second email, he added:\n\n  \"If you're interested, we can talk about this. Ultimately I can ask the\n  saclib/qepcad folks for permission and move forward.\"\n\n  (see [http://groups.google.com/group/sage-devel/msg/4f63c0636720ed51](http://groups.google.com/group/sage-devel/msg/4f63c0636720ed51))\n\nReferences:\n\nQEPCAD: [http://www.cs.usna.edu/~qepcad/B/QEPCAD.html](http://www.cs.usna.edu/~qepcad/B/QEPCAD.html)\n\nMathematica implementation (Resolve, Reduce, FindInstance,\nCylindricalDecomposition, etc.):\n\n[http://reference.wolfram.com/mathematica/tutorial/Quantifiers.html](http://reference.wolfram.com/mathematica/tutorial/Quantifiers.html)\n\n[http://reference.wolfram.com/mathematica/tutorial/TheRepresentationOfSolutionSets.html](http://reference.wolfram.com/mathematica/tutorial/TheRepresentationOfSolutionSets.html)\n\n[http://reference.wolfram.com/mathematica/tutorial/Inequalities-ManipulatingEquationsAndInequalities.html](http://reference.wolfram.com/mathematica/tutorial/Inequalities-ManipulatingEquationsAndInequalities.html)\n\n[http://reference.wolfram.com/mathematica/tutorial/EquationsAndInequalitiesOverDomains.html](http://reference.wolfram.com/mathematica/tutorial/EquationsAndInequalitiesOverDomains.html)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/772\n\n",
    "created_at": "2007-10-01T14:24:04Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "Interface to QEPCAD for quantifier elimination and solving systems of inequalities",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/772",
    "user": "jason"
}
```
Assignee: was

CC:  burcin

QEPCAD uses cylindrical algebraic decomposition to eliminate quantifiers in
statements.  QEPCAD takes the statement


```
there exists an x such that a*x2 + b*x + c = 0 and a /= 0 (i.e., a!=0)
```


and eliminates the quantifier and answers that:


```
a /= 0 and 4 a c - b^2 <= 0
(i.e., a!=0 and 4ac-b^2<=0)
```


In other words, it gives you the conditions of a solution satisfying
your original statement.  See more examples at [http://www.cs.usna.edu/~qepcad/B/examples/Examples.html](http://www.cs.usna.edu/~qepcad/B/examples/Examples.html)

QEPCAD is not currently GPL and depends on the saclib library, which currently is not GPL.  However, both of those could change if there was interest.

David Joyner talked with Chris Brown, and reported that:

  I spoke with Chris Brown, who is essentially now the maintainer of
qepcad. Here is his response:

  "Saclib's actual status is probably a bit up in the air.  What I might
  call the saclib "stakeholders" had agreed to GPL it, but everybody
  was, I guess, too busy to do anything about it.  Qepcad's status is
  similar ... except that my contributions are necessarily public
  domain."

  In a second email, he added:

  "If you're interested, we can talk about this. Ultimately I can ask the
  saclib/qepcad folks for permission and move forward."

  (see [http://groups.google.com/group/sage-devel/msg/4f63c0636720ed51](http://groups.google.com/group/sage-devel/msg/4f63c0636720ed51))

References:

QEPCAD: [http://www.cs.usna.edu/~qepcad/B/QEPCAD.html](http://www.cs.usna.edu/~qepcad/B/QEPCAD.html)

Mathematica implementation (Resolve, Reduce, FindInstance,
CylindricalDecomposition, etc.):

[http://reference.wolfram.com/mathematica/tutorial/Quantifiers.html](http://reference.wolfram.com/mathematica/tutorial/Quantifiers.html)

[http://reference.wolfram.com/mathematica/tutorial/TheRepresentationOfSolutionSets.html](http://reference.wolfram.com/mathematica/tutorial/TheRepresentationOfSolutionSets.html)

[http://reference.wolfram.com/mathematica/tutorial/Inequalities-ManipulatingEquationsAndInequalities.html](http://reference.wolfram.com/mathematica/tutorial/Inequalities-ManipulatingEquationsAndInequalities.html)

[http://reference.wolfram.com/mathematica/tutorial/EquationsAndInequalitiesOverDomains.html](http://reference.wolfram.com/mathematica/tutorial/EquationsAndInequalitiesOverDomains.html)



Issue created by migration from https://trac.sagemath.org/ticket/772





---

archive/issue_comments_004582.json:
```json
{
    "body": "This doesn't have someone assigned, so it should be in the wishlist.",
    "created_at": "2007-10-03T00:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4582",
    "user": "jason"
}
```

This doesn't have someone assigned, so it should be in the wishlist.



---

archive/issue_comments_004583.json:
```json
{
    "body": "To compile SACLIB 2.1, right now tcsh has to be installed.  This may not be needed if the bin/mk* scripts are modified to not require tcsh.\n\n1. Set the $saclib environment variable to the saclib directory.\n2. run `$saclib/mklib all`\n\nThe commands that are executed by the above are below---looks like we don't need tcsh after all.  I think that the objd directory is debugging stuff, while objo stuff is optimized stuff.\n\n\n```\n  pushd >/dev/null  $saclib/lib/objd\n  make  CC=$CC \"SACFLAG=-g -DNO_SACLIB_MACROS\" EXTENSION=d\n  popd >/dev/null\n  pushd >/dev/null  $saclib/lib/objo\n  make  CC=$CC \"SACFLAG=-O4\" EXTENSION=o\n  popd >/dev/null\n```\n\n\n\nTo compile qepcad\n\n1. Set the $saclib and $qe environment variables (the latter to the qesource directory)\n2. run `make` in the $qe directory.\n\nThe Makefile for qepcad uses \"gmake\" for the make program name (it must be GNU Make).  This should probably be changed to \"make\" (if we assume that make is GNU make).\n\nQEPCAD uses the readline library.",
    "created_at": "2007-10-17T23:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4583",
    "user": "jason"
}
```

To compile SACLIB 2.1, right now tcsh has to be installed.  This may not be needed if the bin/mk* scripts are modified to not require tcsh.

1. Set the $saclib environment variable to the saclib directory.
2. run `$saclib/mklib all`

The commands that are executed by the above are below---looks like we don't need tcsh after all.  I think that the objd directory is debugging stuff, while objo stuff is optimized stuff.


```
  pushd >/dev/null  $saclib/lib/objd
  make  CC=$CC "SACFLAG=-g -DNO_SACLIB_MACROS" EXTENSION=d
  popd >/dev/null
  pushd >/dev/null  $saclib/lib/objo
  make  CC=$CC "SACFLAG=-O4" EXTENSION=o
  popd >/dev/null
```



To compile qepcad

1. Set the $saclib and $qe environment variables (the latter to the qesource directory)
2. run `make` in the $qe directory.

The Makefile for qepcad uses "gmake" for the make program name (it must be GNU Make).  This should probably be changed to "make" (if we assume that make is GNU make).

QEPCAD uses the readline library.



---

archive/issue_comments_004584.json:
```json
{
    "body": "From Robert Bradshaw trying to compile this on Mac OSX Tiger\n\n* Comment out #include <ieee754.h> (seems to compile fine without this)\n\nThere are some serious, deep issues with floating point exceptions that apparently need to be addressed to port SACLIB to OSX.  See FPHAND.c and FPCATCH.c in SACLIB.",
    "created_at": "2008-01-10T03:48:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4584",
    "user": "jason"
}
```

From Robert Bradshaw trying to compile this on Mac OSX Tiger

* Comment out #include <ieee754.h> (seems to compile fine without this)

There are some serious, deep issues with floating point exceptions that apparently need to be addressed to port SACLIB to OSX.  See FPHAND.c and FPCATCH.c in SACLIB.



---

archive/issue_comments_004585.json:
```json
{
    "body": "Thanks to Robert Bradshaw sitting right next to me and helping me every few seconds, we have a (very alpha and currently broken) QEPCAD spkg now.  The error is in linking to readline---I think it can't find the readline library.\n\nThe source is not included because of licensing restrictions (I've emailed Chris Brown about that).  However, the spkg will download the source from the webpage automatically.\n\nCan someone figure out how to fix the build issue with readline?  I'm still fumbling my way through doing an spkg.  The error is:\n\n\n```\ng++ -O4 -I/home/grout/sage/spkg/build/qepcad/saclib2.1/include -I/home/grout/sage/spkg/build/qepcad/qesource/source  -I. -o cad2d ../source/saclib/GCSI.c \\\n                        cad2d.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline  cad2d.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline \n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `PC'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetflag'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetent'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `UP'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tputs'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgoto'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetnum'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `BC'\n/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetstr'\ncollect2: ld returned 1 exit status\nmake: *** [opt] Error 1\n```\n",
    "created_at": "2008-01-10T07:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4585",
    "user": "jason"
}
```

Thanks to Robert Bradshaw sitting right next to me and helping me every few seconds, we have a (very alpha and currently broken) QEPCAD spkg now.  The error is in linking to readline---I think it can't find the readline library.

The source is not included because of licensing restrictions (I've emailed Chris Brown about that).  However, the spkg will download the source from the webpage automatically.

Can someone figure out how to fix the build issue with readline?  I'm still fumbling my way through doing an spkg.  The error is:


```
g++ -O4 -I/home/grout/sage/spkg/build/qepcad/saclib2.1/include -I/home/grout/sage/spkg/build/qepcad/qesource/source  -I. -o cad2d ../source/saclib/GCSI.c \
                        cad2d.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline  cad2d.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/source/qepcad.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline 
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `PC'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetflag'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetent'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `UP'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tputs'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgoto'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetnum'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `BC'
/home/grout/sage/local/lib/../lib/libreadline.so: undefined reference to `tgetstr'
collect2: ld returned 1 exit status
make: *** [opt] Error 1
```




---

archive/issue_comments_004586.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-10T07:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4586",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_004587.json:
```json
{
    "body": "Hi Jason,\n\ntry linking against termcap instead. Most of the time they are interchangeable. Sage builds termcap 1.1.3.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T07:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4587",
    "user": "mabshoff"
}
```

Hi Jason,

try linking against termcap instead. Most of the time they are interchangeable. Sage builds termcap 1.1.3.

Cheers,

Michael



---

archive/issue_comments_004588.json:
```json
{
    "body": "I tried linking termcap and it complained about not having rl_instream.  So I switched it back to -lreadline and made sure that I had -L${SAGE_LOCAL}/lib at the top of the compile line.  I get the same errors:\n\n\n```\nLinking the optimized program......\ng++ -O4 -I/home/grout/sage/spkg/build/qepcad/saclib2.1/include  -I. saclib/GCSI.c \\\n                        qepcad.a -L/home/grout/sage/local/lib /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline  qepcad.a -L/home/grout/sage/local/lib /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline  -o qepcad\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `PC'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetflag'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetent'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `UP'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `tputs'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgoto'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetnum'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `BC'\n/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetstr'\ncollect2: ld returned 1 exit status\nmake[1]: *** [opt] Error 1\n```\n\n\nCould it be from not using the readline headers in sage, but using the ones in the system instead?  I have the libreadline-dev package installed in Gutsy.",
    "created_at": "2008-01-10T09:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4588",
    "user": "jason"
}
```

I tried linking termcap and it complained about not having rl_instream.  So I switched it back to -lreadline and made sure that I had -L${SAGE_LOCAL}/lib at the top of the compile line.  I get the same errors:


```
Linking the optimized program......
g++ -O4 -I/home/grout/sage/spkg/build/qepcad/saclib2.1/include  -I. saclib/GCSI.c \
                        qepcad.a -L/home/grout/sage/local/lib /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline  qepcad.a -L/home/grout/sage/local/lib /home/grout/sage/spkg/build/qepcad/qesource/extensions/sfext/sfexto.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/lift2D/lift2Do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/newadj/newadjo.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/adj2d/adj2do.a /home/grout/sage/spkg/build/qepcad/qesource/extensions/rend/rendo.a /home/grout/sage/spkg/build/qepcad/saclib2.1/lib/saclibo.a -lreadline  -o qepcad
/home/grout/sage/local/lib/libreadline.so: undefined reference to `PC'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetflag'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetent'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `UP'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `tputs'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgoto'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetnum'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `BC'
/home/grout/sage/local/lib/libreadline.so: undefined reference to `tgetstr'
collect2: ld returned 1 exit status
make[1]: *** [opt] Error 1
```


Could it be from not using the readline headers in sage, but using the ones in the system instead?  I have the libreadline-dev package installed in Gutsy.



---

archive/issue_comments_004589.json:
```json
{
    "body": "I got this to compile by editing qesource/source/Makefile, and changing \"-lreadline\" to \"-lreadline -lncurses\" (in two places in that file).",
    "created_at": "2008-01-19T19:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4589",
    "user": "cwitty"
}
```

I got this to compile by editing qesource/source/Makefile, and changing "-lreadline" to "-lreadline -lncurses" (in two places in that file).



---

archive/issue_comments_004590.json:
```json
{
    "body": "cwitty, that worked!  Thanks!",
    "created_at": "2008-01-25T00:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4590",
    "user": "jason"
}
```

cwitty, that worked!  Thanks!



---

archive/issue_comments_004591.json:
```json
{
    "body": "The qepcad-1.48.spkg now compiles on my Ubuntu 7.10 system.  The package downloads the appropriate source tarballs since we do not have a clear situation with the license agreement yet (working on it, though).  Please read and agree to the license in SPKG.txt for SACLIB.\n\nTo test the package, go to $SAGE_LOCAL/bin and execute qepcad.  Several example sessions are found at http://www.cs.usna.edu/~qepcad/B/examples/Examples.html\n\nCan someone test this spkg and give me feedback?  It's my first spkg, so I'm sure I've done something wrong.",
    "created_at": "2008-01-25T00:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4591",
    "user": "jason"
}
```

The qepcad-1.48.spkg now compiles on my Ubuntu 7.10 system.  The package downloads the appropriate source tarballs since we do not have a clear situation with the license agreement yet (working on it, though).  Please read and agree to the license in SPKG.txt for SACLIB.

To test the package, go to $SAGE_LOCAL/bin and execute qepcad.  Several example sessions are found at http://www.cs.usna.edu/~qepcad/B/examples/Examples.html

Can someone test this spkg and give me feedback?  It's my first spkg, so I'm sure I've done something wrong.



---

archive/issue_comments_004592.json:
```json
{
    "body": "On my 64-bit x86 Debian testing system, compilation fails with:\n\n```\ng++ -I/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/saclib2.1/include -I/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/qesource/source  -I. -O4 -o src/MAIN.o -c src/MAIN.c\nIn file included from src/MAIN.c:5:\n/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/qesource/source/db/convenientstreams.h: In member function 'virtual int cacInBuff::underflow()':\n/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/qesource/source/db/convenientstreams.h:82: error: no matching function for call to 'min(const int&, long int)'\nsrc/MAIN.c: In function 'int main(int, char**)':\nsrc/MAIN.c:33: warning: deprecated conversion from string constant to 'char*'\nsrc/MAIN.c: In function 'void QEPCAD_ProcessRC(int, char**)':\nsrc/MAIN.c:45: warning: deprecated conversion from string constant to 'char*'\nsrc/MAIN.c:45: warning: deprecated conversion from string constant to 'char*'\nmake: *** [src/MAIN.o] Error 1\nrm src/CAD2D.o src/CONSTRUCT.o\n```\n",
    "created_at": "2008-01-26T00:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4592",
    "user": "cwitty"
}
```

On my 64-bit x86 Debian testing system, compilation fails with:

```
g++ -I/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/saclib2.1/include -I/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/qesource/source  -I. -O4 -o src/MAIN.o -c src/MAIN.c
In file included from src/MAIN.c:5:
/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/qesource/source/db/convenientstreams.h: In member function 'virtual int cacInBuff::underflow()':
/home/cwitty/sage-2.10.1.alpha1/spkg/build/qepcad-1.48/qesource/source/db/convenientstreams.h:82: error: no matching function for call to 'min(const int&, long int)'
src/MAIN.c: In function 'int main(int, char**)':
src/MAIN.c:33: warning: deprecated conversion from string constant to 'char*'
src/MAIN.c: In function 'void QEPCAD_ProcessRC(int, char**)':
src/MAIN.c:45: warning: deprecated conversion from string constant to 'char*'
src/MAIN.c:45: warning: deprecated conversion from string constant to 'char*'
make: *** [src/MAIN.o] Error 1
rm src/CAD2D.o src/CONSTRUCT.o
```




---

archive/issue_comments_004593.json:
```json
{
    "body": "On my 32-bit x86 Debian testing system, qepcad crashes immediately unless the \"qe\" environment variable is set to my $SAGE_LOCAL directory.  If \"qe\" is set, then qepcad seems to work (I went through one of the examples Jason linked to above, and got the expected answer).",
    "created_at": "2008-01-26T00:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4593",
    "user": "cwitty"
}
```

On my 32-bit x86 Debian testing system, qepcad crashes immediately unless the "qe" environment variable is set to my $SAGE_LOCAL directory.  If "qe" is set, then qepcad seems to work (I went through one of the examples Jason linked to above, and got the expected answer).



---

archive/issue_comments_004594.json:
```json
{
    "body": "Fixes:\n\n* For the environment variable, make a qepcad shell script which sets the $qe variable to $SAGE_LOCAL and then calls qepcad.real\n\nFor the 64 bit issue:\n\n\n```\n~/download/qesource/source$ grep -nr \" min[^A-Za-z]\" *\ndb/readlineistream.h:63:    int leftover =  min(extra,gptr()-eback());\ndb/unnamedpipe.h:60:      int leftover = min(extra, gptr() - eback()), readSize;\nsaclib/IPPSCT.c:11: L     : (psc_(A,B),psc_1(A,B),...,psc_k(A,B)), where 0 <= k < min(deg(A),deg(B)).  \nsaclib/IPPSCT.c:14:         many common zeros, or k = min(deg(A),deg(B))-1.\n```\n",
    "created_at": "2008-01-26T01:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4594",
    "user": "jason"
}
```

Fixes:

* For the environment variable, make a qepcad shell script which sets the $qe variable to $SAGE_LOCAL and then calls qepcad.real

For the 64 bit issue:


```
~/download/qesource/source$ grep -nr " min[^A-Za-z]" *
db/readlineistream.h:63:    int leftover =  min(extra,gptr()-eback());
db/unnamedpipe.h:60:      int leftover = min(extra, gptr() - eback()), readSize;
saclib/IPPSCT.c:11: L     : (psc_(A,B),psc_1(A,B),...,psc_k(A,B)), where 0 <= k < min(deg(A),deg(B)).  
saclib/IPPSCT.c:14:         many common zeros, or k = min(deg(A),deg(B))-1.
```




---

archive/issue_comments_004595.json:
```json
{
    "body": "It looks like there is some low-level pointer arithmetic going on.  I don't have a 64-bit system (or experience with one), so hopefully someone can help with this one.",
    "created_at": "2008-01-26T01:29:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4595",
    "user": "jason"
}
```

It looks like there is some low-level pointer arithmetic going on.  I don't have a 64-bit system (or experience with one), so hopefully someone can help with this one.



---

archive/issue_comments_004596.json:
```json
{
    "body": "Two more failures on 64-bit Linux.  The build continues after each of these errors.\n\n\n```\ncc -I/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/include -c -O4 /home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FPHAND.c\n/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FPHAND.c: In function 'FPHAND':\n/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FPHAND.c:28: error: 'struct _libc_fpstate' has no member named 'cw'\nmake: *** [FPHAND.o] Error 1\n```\n\n\n\n```\ng++ -I/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/include  -I. -O4 -o main/FAIL.o -c main/FAIL.c\nmain/FAIL.c: In function 'void FAIL(char*, char*, ...)':\nmain/FAIL.c:16: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:17: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:17: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:18: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:18: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:28: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:28: error: cast from 'char*' to 'int' loses precision\nmain/FAIL.c:28: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:29: warning: deprecated conversion from string constant to 'char*'\nmain/FAIL.c:29: error: cast from 'char*' to 'int' loses precision\n```\n\nfollowed by many more similar \"warning:\" lines.\n\nAnd here's a couple of scary warnings:\n\n```\ncc -I/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/include -c -O4 /home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c\n/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c: In function 'FAIL':\n/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c:43: warning: cast from pointer to integer of different size\n/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c:44: warning: cast from pointer to integer of different size\n```\n",
    "created_at": "2008-01-28T17:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4596",
    "user": "cwitty"
}
```

Two more failures on 64-bit Linux.  The build continues after each of these errors.


```
cc -I/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/include -c -O4 /home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FPHAND.c
/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FPHAND.c: In function 'FPHAND':
/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FPHAND.c:28: error: 'struct _libc_fpstate' has no member named 'cw'
make: *** [FPHAND.o] Error 1
```



```
g++ -I/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/include  -I. -O4 -o main/FAIL.o -c main/FAIL.c
main/FAIL.c: In function 'void FAIL(char*, char*, ...)':
main/FAIL.c:16: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:17: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:17: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:18: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:18: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:28: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:28: error: cast from 'char*' to 'int' loses precision
main/FAIL.c:28: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:29: warning: deprecated conversion from string constant to 'char*'
main/FAIL.c:29: error: cast from 'char*' to 'int' loses precision
```

followed by many more similar "warning:" lines.

And here's a couple of scary warnings:

```
cc -I/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/include -c -O4 /home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c
/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c: In function 'FAIL':
/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c:43: warning: cast from pointer to integer of different size
/home/cwitty/sage-2.10.1.rc1/spkg/build/qepcad-1.48/saclib2.1/src/FAIL.c:44: warning: cast from pointer to integer of different size
```




---

archive/issue_comments_004597.json:
```json
{
    "body": "Chris Brown emailed me today and told me that he would try to send an email out today asking about licensing saclib and qepcad under something like BSD.  If saclib and qepcad do go opensource, cwitty agreed on IRC to help more with porting things to 64-bit linux.",
    "created_at": "2008-01-28T17:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4597",
    "user": "jason"
}
```

Chris Brown emailed me today and told me that he would try to send an email out today asking about licensing saclib and qepcad under something like BSD.  If saclib and qepcad do go opensource, cwitty agreed on IRC to help more with porting things to 64-bit linux.



---

archive/issue_comments_004598.json:
```json
{
    "body": "Attachment\n\nUpdate to address the environment variable issues by creating sage-qepcad and sage-cad2d scripts that should be run instead of qepcad and cad2d",
    "created_at": "2008-01-28T17:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4598",
    "user": "jason"
}
```

Attachment

Update to address the environment variable issues by creating sage-qepcad and sage-cad2d scripts that should be run instead of qepcad and cad2d



---

archive/issue_comments_004599.json:
```json
{
    "body": "I've posted an interface to qepcad.  A couple of the doctests fail because the doctest framework can't handle trailing backslashes in an expected output; I'll post another bug about that problem soon (probably tomorrow).",
    "created_at": "2008-03-27T07:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4599",
    "user": "cwitty"
}
```

I've posted an interface to qepcad.  A couple of the doctests fail because the doctest framework can't handle trailing backslashes in an expected output; I'll post another bug about that problem soon (probably tomorrow).



---

archive/issue_comments_004600.json:
```json
{
    "body": "The doctest failures referred to in the previous comment are fixed by #2713.",
    "created_at": "2008-03-29T01:10:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4600",
    "user": "cwitty"
}
```

The doctest failures referred to in the previous comment are fixed by #2713.



---

archive/issue_comments_004601.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_cwitty\".",
    "created_at": "2008-06-15T21:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4601",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_cwitty".



---

archive/issue_comments_004602.json:
```json
{
    "body": "Changing keywords from \"editor_cwitty\" to \"\".",
    "created_at": "2008-06-15T21:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4602",
    "user": "cwitty"
}
```

Changing keywords from "editor_cwitty" to "".



---

archive/issue_comments_004603.json:
```json
{
    "body": "I'm moving the interface to a separate ticket (#3431).",
    "created_at": "2008-06-15T21:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4603",
    "user": "cwitty"
}
```

I'm moving the interface to a separate ticket (#3431).



---

archive/issue_comments_004604.json:
```json
{
    "body": "\n```\n<cwitty> The current package in #772 can't become an optional package because optional packages are supposed to work on almost all machines that Sage works on,\n<cwitty> and it doesn't work on 64-bit.\n```\n",
    "created_at": "2008-08-04T16:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4604",
    "user": "burcin"
}
```


```
<cwitty> The current package in #772 can't become an optional package because optional packages are supposed to work on almost all machines that Sage works on,
<cwitty> and it doesn't work on 64-bit.
```




---

archive/issue_comments_004605.json:
```json
{
    "body": "A new spkg is up at: http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg\n\nIt includes the BSD-licensed source for qepcad and saclib.  It also includes 64-bit linux patches by Carl Witty.",
    "created_at": "2008-08-16T21:21:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4605",
    "user": "jason"
}
```

A new spkg is up at: http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg

It includes the BSD-licensed source for qepcad and saclib.  It also includes 64-bit linux patches by Carl Witty.



---

archive/issue_comments_004606.json:
```json
{
    "body": "I've updated http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg to not install CAD2D, which wasn't being used and has not been fixed for 64-bit yet.  The new version of the spkg also does not use \"patch\" at install time, but rather caches the effects of applying the patches and copies files at install time.",
    "created_at": "2008-08-22T04:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4606",
    "user": "jason"
}
```

I've updated http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg to not install CAD2D, which wasn't being used and has not been fixed for 64-bit yet.  The new version of the spkg also does not use "patch" at install time, but rather caches the effects of applying the patches and copies files at install time.



---

archive/issue_comments_004607.json:
```json
{
    "body": "The latest package at http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg compiles and works at least minimally (passes the doctests in my interfaces/qepcad.py) on 32-bit and 64-bit x86 Linux.\n\nIt does not work on OSX.\n\nI think this should become an experimental package.  (I'm not sure what the rules are, but I'm guessing that not working on OSX makes it ineligible for optional status.)\n\nNote that I wrote a lot of the patches involved, but Jason did all the packaging work; hopefully you will still accept this review.",
    "created_at": "2008-08-22T05:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4607",
    "user": "cwitty"
}
```

The latest package at http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg compiles and works at least minimally (passes the doctests in my interfaces/qepcad.py) on 32-bit and 64-bit x86 Linux.

It does not work on OSX.

I think this should become an experimental package.  (I'm not sure what the rules are, but I'm guessing that not working on OSX makes it ineligible for optional status.)

Note that I wrote a lot of the patches involved, but Jason did all the packaging work; hopefully you will still accept this review.



---

archive/issue_comments_004608.json:
```json
{
    "body": "Even for experimental this spkg is not ready:\n\n```\nmabshoff@sage:~/foo/qepcad-1.50$ hg status\n! patches/cached/AFUPHIBRI.c.19\n! patches/cached/AFUPHIBRI.c.19.filename\n! patches/cached/ANHI.c.20\n! patches/cached/ANHI.c.20.filename\n! patches/cached/BEGINSACLIB.c.21\n! patches/cached/BEGINSACLIB.c.21.filename\n! patches/cached/FAIL.c.11\n! patches/cached/FAIL.c.11.filename\n! patches/cached/FMAPOLLIST.c.7\n! patches/cached/FMAPOLLIST.c.7.filename\n! patches/cached/FPCATCH.c.23\n! patches/cached/FPCATCH.c.23.filename\n! patches/cached/FPCHECK.c.24\n! patches/cached/FPCHECK.c.24.filename\n! patches/cached/FPHAND.c.30\n! patches/cached/FPHAND.c.30.filename\n! patches/cached/FPHAND.c.31\n! patches/cached/FPHAND.c.31.filename\n! patches/cached/FPHAND.c.32\n! patches/cached/FPHAND.c.32.filename\n! patches/cached/FPHAND.c.33\n! patches/cached/FPHAND.c.33.filename\n! patches/cached/FPHAND.c.35\n! patches/cached/FPHAND.c.35.filename\n! patches/cached/HIPBHT.c.25\n! patches/cached/HIPBHT.c.25.filename\n! patches/cached/HIPIR.c.26\n! patches/cached/HIPIR.c.26.filename\n! patches/cached/HIPRRISD.c.27\n! patches/cached/HIPRRISD.c.27.filename\n! patches/cached/HIPVCHT.c.28\n! patches/cached/HIPVCHT.c.28.filename\n! patches/cached/IBPRRIOAP.c.3\n! patches/cached/IBPRRIOAP.c.3.filename\n! patches/cached/MAIN.c.12\n! patches/cached/MAIN.c.12.filename\n! patches/cached/Makefile.1\n! patches/cached/Makefile.1.filename\n! patches/cached/Makefile.13\n! patches/cached/Makefile.13.filename\n! patches/cached/Makefile.2\n! patches/cached/Makefile.2.filename\n! patches/cached/RHI.c.29\n! patches/cached/RHI.c.29.filename\n! patches/cached/Rend_Win.h.6\n! patches/cached/Rend_Win.h.6.filename\n! patches/cached/convenientstreams.h.8\n! patches/cached/convenientstreams.h.8.filename\n! patches/cached/external.c.22\n! patches/cached/external.c.22.filename\n! patches/cached/install.34\n! patches/cached/install.34.filename\n! patches/cached/mksysdep.pl.14\n! patches/cached/mksysdep.pl.14.filename\n! patches/cached/modHIPRRISD.c.4\n! patches/cached/modHIPRRISD.c.4.filename\n! patches/cached/modIBPRRIOAP.c.5\n! patches/cached/modIBPRRIOAP.c.5.filename\n! patches/cached/readlineistream.h.9\n! patches/cached/readlineistream.h.9.filename\n! patches/cached/saclib.h.16\n! patches/cached/saclib.h.16.filename\n! patches/cached/sacproto.h.17\n! patches/cached/sacproto.h.17.filename\n! patches/cached/sacsys.h.18\n! patches/cached/sacsys.h.18.filename\n! patches/cached/sconf.15\n! patches/cached/sconf.15.filename\n! patches/cached/unnamedpipe.h.10\n! patches/cached/unnamedpipe.h.10.filename\n```\n\nIt also needs an `.hgignore` that adds the src directory.\n\nI also *extremely* dislike the `patch-cache.sh` and `apply-patches.sh` scripts. We have discussed this in IRC to no end, so no need to go into details again. If you need to heavily patch the src directory just ship a patched src directory and wait for upstream to integrate your patches before updating the spkg to vanilla sources. `spkg-install` also needs a massive amount of work.\n\nThat cwitty did the review is fine in this context. \n\nCheers,\n\nMichael",
    "created_at": "2008-08-22T18:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4608",
    "user": "mabshoff"
}
```

Even for experimental this spkg is not ready:

```
mabshoff@sage:~/foo/qepcad-1.50$ hg status
! patches/cached/AFUPHIBRI.c.19
! patches/cached/AFUPHIBRI.c.19.filename
! patches/cached/ANHI.c.20
! patches/cached/ANHI.c.20.filename
! patches/cached/BEGINSACLIB.c.21
! patches/cached/BEGINSACLIB.c.21.filename
! patches/cached/FAIL.c.11
! patches/cached/FAIL.c.11.filename
! patches/cached/FMAPOLLIST.c.7
! patches/cached/FMAPOLLIST.c.7.filename
! patches/cached/FPCATCH.c.23
! patches/cached/FPCATCH.c.23.filename
! patches/cached/FPCHECK.c.24
! patches/cached/FPCHECK.c.24.filename
! patches/cached/FPHAND.c.30
! patches/cached/FPHAND.c.30.filename
! patches/cached/FPHAND.c.31
! patches/cached/FPHAND.c.31.filename
! patches/cached/FPHAND.c.32
! patches/cached/FPHAND.c.32.filename
! patches/cached/FPHAND.c.33
! patches/cached/FPHAND.c.33.filename
! patches/cached/FPHAND.c.35
! patches/cached/FPHAND.c.35.filename
! patches/cached/HIPBHT.c.25
! patches/cached/HIPBHT.c.25.filename
! patches/cached/HIPIR.c.26
! patches/cached/HIPIR.c.26.filename
! patches/cached/HIPRRISD.c.27
! patches/cached/HIPRRISD.c.27.filename
! patches/cached/HIPVCHT.c.28
! patches/cached/HIPVCHT.c.28.filename
! patches/cached/IBPRRIOAP.c.3
! patches/cached/IBPRRIOAP.c.3.filename
! patches/cached/MAIN.c.12
! patches/cached/MAIN.c.12.filename
! patches/cached/Makefile.1
! patches/cached/Makefile.1.filename
! patches/cached/Makefile.13
! patches/cached/Makefile.13.filename
! patches/cached/Makefile.2
! patches/cached/Makefile.2.filename
! patches/cached/RHI.c.29
! patches/cached/RHI.c.29.filename
! patches/cached/Rend_Win.h.6
! patches/cached/Rend_Win.h.6.filename
! patches/cached/convenientstreams.h.8
! patches/cached/convenientstreams.h.8.filename
! patches/cached/external.c.22
! patches/cached/external.c.22.filename
! patches/cached/install.34
! patches/cached/install.34.filename
! patches/cached/mksysdep.pl.14
! patches/cached/mksysdep.pl.14.filename
! patches/cached/modHIPRRISD.c.4
! patches/cached/modHIPRRISD.c.4.filename
! patches/cached/modIBPRRIOAP.c.5
! patches/cached/modIBPRRIOAP.c.5.filename
! patches/cached/readlineistream.h.9
! patches/cached/readlineistream.h.9.filename
! patches/cached/saclib.h.16
! patches/cached/saclib.h.16.filename
! patches/cached/sacproto.h.17
! patches/cached/sacproto.h.17.filename
! patches/cached/sacsys.h.18
! patches/cached/sacsys.h.18.filename
! patches/cached/sconf.15
! patches/cached/sconf.15.filename
! patches/cached/unnamedpipe.h.10
! patches/cached/unnamedpipe.h.10.filename
```

It also needs an `.hgignore` that adds the src directory.

I also *extremely* dislike the `patch-cache.sh` and `apply-patches.sh` scripts. We have discussed this in IRC to no end, so no need to go into details again. If you need to heavily patch the src directory just ship a patched src directory and wait for upstream to integrate your patches before updating the spkg to vanilla sources. `spkg-install` also needs a massive amount of work.

That cwitty did the review is fine in this context. 

Cheers,

Michael



---

archive/issue_comments_004609.json:
```json
{
    "body": "Notes from IRC conversation with mabshoff:\n\n* There are way too many files that are being copied at install time; ship patched sources until upstream has applied the patches.\n\n* spkg-install should address #633, it should check the error status of the make, delete the commented stuff at the end \n\n\n```\n[15:33] <mabshoff> Also: Check the return status of make and so on and throw an intelligent error\n[15:35] <mabshoff> i.e. if make returns non-zero say something like \"building $FOO failed\"\n[15:35] <mabshoff> Also delete all that commented out junk at the end.\n[15:36] <mabshoff> spkg-install should also be executable in the repo\n[15:36] <mabshoff> And while you are at it reset the repo and check everything in again.\n[15:36] <jason--> I left the CAD2D in there because we originally had it in there, but it hadn't been converted to 64-bit \n[15:36] <mabshoff> add an .hgignore and add src in there.\n[15:36] <mabshoff> Ok.\n[15:36] <mabshoff> So that is another binary? I did not notice that.\n[15:36] <jason--> I didn't want to lose the work to build it.\n[15:36] <jason--> yes, another binary\n[15:37] <jason--> sage-cad2d, I believe\n[15:37] <jason--> it's an optimization in the 2d case\n[15:37] <mabshoff> Then add an exit(0)  before it and comment that you are currently not building it due to 64 bit issues.\n```\n",
    "created_at": "2008-08-22T20:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4609",
    "user": "jason"
}
```

Notes from IRC conversation with mabshoff:

* There are way too many files that are being copied at install time; ship patched sources until upstream has applied the patches.

* spkg-install should address #633, it should check the error status of the make, delete the commented stuff at the end 


```
[15:33] <mabshoff> Also: Check the return status of make and so on and throw an intelligent error
[15:35] <mabshoff> i.e. if make returns non-zero say something like "building $FOO failed"
[15:35] <mabshoff> Also delete all that commented out junk at the end.
[15:36] <mabshoff> spkg-install should also be executable in the repo
[15:36] <mabshoff> And while you are at it reset the repo and check everything in again.
[15:36] <jason--> I left the CAD2D in there because we originally had it in there, but it hadn't been converted to 64-bit 
[15:36] <mabshoff> add an .hgignore and add src in there.
[15:36] <mabshoff> Ok.
[15:36] <mabshoff> So that is another binary? I did not notice that.
[15:36] <jason--> I didn't want to lose the work to build it.
[15:36] <jason--> yes, another binary
[15:37] <jason--> sage-cad2d, I believe
[15:37] <jason--> it's an optimization in the 2d case
[15:37] <mabshoff> Then add an exit(0)  before it and comment that you are currently not building it due to 64 bit issues.
```




---

archive/issue_comments_004610.json:
```json
{
    "body": "Okay, new spkg up at http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg which addresses mabshoff's concerns.\n\nLet me know if you have any other objections.",
    "created_at": "2008-08-27T17:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4610",
    "user": "jason"
}
```

Okay, new spkg up at http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg which addresses mabshoff's concerns.

Let me know if you have any other objections.



---

archive/issue_comments_004611.json:
```json
{
    "body": "The latest version of http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg compiles and passes doctests on 64-bit x86 linux, and also addresses mabshoff's packaging comments. Positive review (for experimental).",
    "created_at": "2008-08-27T17:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4611",
    "user": "cwitty"
}
```

The latest version of http://sage.math.washington.edu/home/jason/qepcad-1.50.spkg compiles and passes doctests on 64-bit x86 linux, and also addresses mabshoff's packaging comments. Positive review (for experimental).



---

archive/issue_comments_004612.json:
```json
{
    "body": "Builds successfully for me on 32 and 64 bit debian etch boxes. However, fails on my laptop, since I don't have tcsh installed.\n\nIt might be a good idea to add error checking to the saclib phase, since the package goes on to build qepcad, then fails at the linking phase with a misleading message.\n\nHere is my install log (look around line 2422):\n\nhttp://sage.math.washington.edu/home/burcin/spkg/install.log",
    "created_at": "2008-08-27T19:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4612",
    "user": "burcin"
}
```

Builds successfully for me on 32 and 64 bit debian etch boxes. However, fails on my laptop, since I don't have tcsh installed.

It might be a good idea to add error checking to the saclib phase, since the package goes on to build qepcad, then fails at the linking phase with a misleading message.

Here is my install log (look around line 2422):

http://sage.math.washington.edu/home/burcin/spkg/install.log



---

archive/issue_comments_004613.json:
```json
{
    "body": "I am still not happy about some details, especially things like `export CC=cc`, but this is good enough for experimental now :)\n\nBurcin's concern should also be addressed in the future.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-28T02:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4613",
    "user": "mabshoff"
}
```

I am still not happy about some details, especially things like `export CC=cc`, but this is good enough for experimental now :)

Burcin's concern should also be addressed in the future.

Cheers,

Michael



---

archive/issue_comments_004614.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T02:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4614",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_comments_004615.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T02:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/772#issuecomment-4615",
    "user": "mabshoff"
}
```

Resolution: fixed
