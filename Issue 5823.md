# Issue 5823: Update clisp to 2.47 and introduce noreadline mode dynammically for clisp and maxima

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-19 07:13:51

Assignee: mabshoff

CC:  tornaria

This is shared credit with Gonzalo and split off from #5662. I have taken on of his patches, integrated it into an updated clisp version and changed his workaround after a clever suggestion by William. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 07:18:33

There are two spkgs that work together:

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/clisp-2.47.spkg

and

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/maxima-5.16.3.p0.spkg

Note that the patch from #5662 must be applied for those two above to actually pass doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 07:18:33

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-19 07:20:28

Note that the above clisp.spkg fails to build on iras on SkyNet. We will provide a workaround spkg based on clisp-2.46 for SLES10/Itanium boxen.

Cheers,

Michael


---

Comment by tornaria created at 2009-04-19 14:06:52

The `clisp-noreadline` script looks ok. The `maxima-noreadline` script, however, has a path issue:

```
tornaria`@`sage2:~/sage-3.4$ SAGE_ROOT=~/sage-3.4 local/bin/maxima-noreadline 
local/bin/maxima-noreadline: line 3: maxima: command not found
```

Maybe the `maxima-noreadline` script should be changed by

```/bin/sh
SAGE_CLISP_DISABLE_READLINE_HACK="yes"; export SAGE_CLISP_DISABLE_READLINE_HACK
"$SAGE_ROOT/maxima" "$`@`"
```


OTOH, I don't know if there is a reason to use a separate script with the `-noreadline` option instead of adding a `--disable-readline` command line option to the scripts as I had done in #5662. Particularly for maxima, given that `maxima --help` actually lists `--disable-readline` as one of its command line options (it's broken now).

Other than that, the changes look good to me. I'll run the test suite a couple of times just to be sure, and report back.


---

Comment by tornaria created at 2009-04-19 14:21:03

Actually, shouldn't the scripts be something like:

```/bin/sh
SAGE_CLISP_DISABLE_READLINE_HACK="yes"; export SAGE_CLISP_DISABLE_READLINE_HACK
exec "$SAGE_ROOT/maxima" "$`@`"
```

i.e. use `exec` so that we can avoid the (unnecessary) fork?

Ditto for `clisp` and `clisp-noreadline`. The script `maxima` (which is the upstream one) seems to use `exec`.


---

Comment by mabshoff created at 2009-04-19 15:14:38

* neither `maxima --disable-readline` nor `clisp --noreadline` worked for me with clisp 2.47 and Maxima 5.16.3, so I changed the scripts.
 * I think the exec change is a good one
 * `local/bin/maxima-noreadline` does indeed not work, but then it is not intended to be used that way since I use `./sage -sh` and then `maxima-noreadline` since that is how we use it from inside Sage. But I can use `exec "$SAGE_ROOT/maxima" "$`@`"` and something analog for clisp.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 15:21:09

To be more precise about --disable-readline:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc4$ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc4$ which clisp
/scratch/mabshoff/sage-3.4.1.rc4/local/bin/clisp
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc4$ which maxima
/scratch/mabshoff/sage-3.4.1.rc4/local/bin/maxima
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc4$ clisp
  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8

Welcome to GNU CLISP 2.46 (2008-07-02) <http://clisp.cons.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2008

Type :h and hit Enter for context help.

[1]> 
Bye.
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc4$ clisp --disable-readline
GNU CLISP: invalid argument: '--disable-readline'
GNU CLISP: use '-h' for help
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc4$ maxima
Maxima 5.16.3 http://maxima.sourceforge.net
Using Lisp CLISP 2.46 (2008-07-02)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) 
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc4$ maxima --disable-readline
Maxima 5.16.3 http://maxima.sourceforge.net
Using Lisp CLISP 2.46 (2008-07-02)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) 
```

So while Maxima seems to accept the --disable-readline option it does unfortunately still use readline, but that is non-obvious if I post the session output here.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-04-19 21:04:05

On my MacPPC, the known culprits like "calculus.py", "functional.py" or "partition.py" still behave badly. I see one new doctests failure I never have seen before:

```
sage -t -long "devel/sage/sage/calculus/tests.py"           
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.4.1.rc3/devel/sage/sage/calculus/tests.py", line 219:
    sage: integral(1/sqrt(2*t^4 - 3*t^2 - 2), t, 2, 3)     # todo: maple can do this
Expected:
    integrate(1/sqrt(2*t^4 - 3*t^2 - 2), t, 2, 3)
Got:
    integrate(e^(-x^2)*log(x), x)
**********************************************************************
1 items had failures:
   1 of  84 in __main__.example_0
***Test Failed*** 1 failures.
```

This might be blamed on the MacPPC "being of the bronze age", too. But I can't test this on my MacIntel (or sage.math) right now, this will have to wait for tomorrow. Since there is a slight chance that the change from clisp 2.46 to 2.47 did introduce this doctest failure, I hesitate to give a positive review for this ticket, based on my current insufficient knowledge. From mere "code reviewing" the changes in the two spkgs, all is fine resp. looks good to me.

Cheers, gsw


---

Comment by tornaria created at 2009-04-19 22:46:01

Replying to [comment:5 mabshoff]:
>  * neither `maxima --disable-readline` nor `clisp --noreadline` worked for me with clisp 2.47 and Maxima 5.16.3, so I changed the scripts.

I know they don't work out of the box. The purpose of my second batch of spkg's in #5662 was to implement this, after wstein suggestion. Sorry I neglected to comment properly.

Here's the patch to `maxima.in` (maxima script) to support `--disable-readline` option:

```
$ cat maxima-5.16.3.p1/patches/maxima.in.patch
--- src/src/maxima.in   2008-08-10 10:41:15.000000000 -0700
+++ patches/maxima.in   2009-04-05 21:40:50.009173050 -0700
`@``@` -76,6 +76,7 `@``@`
 arg9=$9
 while [ -n "$1" ]; do
     case $1 in 
+       --disable-readline ) export SAGE_CLISP_DISABLE_READLINE_HACK=1 ; shift ;;
        -l ) MAXIMA_LISP=$2 ; shift;;
        --lisp ) MAXIMA_LISP=$2 ; shift;;
        --lisp=*) MAXIMA_LISP=`echo "$1" | sed 's/--lisp=//'` ;;
```


And here's the version of `clisp.sh`, to be installed as `$SAGE_ROOT/local/bin/clisp`:

```
$ cat clisp-2.46.p9/patches/clisp.sh 
#!/bin/sh
case $1 in
    --disable-readline ) export SAGE_CLISP_DISABLE_READLINE_HACK=1 ; shift ;;
esac
exec "$SAGE_ROOT/local/bin/clisp.bin" -B "$SAGE_ROOT/local/lib/clisp-2.46" "$`@`"
```


The full patches and clean trees for all my spkgs are in http://sage.math.washington.edu/home/tornaria/maxima-pexpect-bug, in particular
[clisp-2.46.p8-p9.patch](http://sage.math.washington.edu/home/tornaria/maxima-pexpect-bug/clisp-2.46.p8-p9.patch)
and
[maxima-5.16.3.p0-p1.patch](http://sage.math.washington.edu/home/tornaria/maxima-pexpect-bug/maxima-5.16.3.p0-p1.patch).

>  * `local/bin/maxima-noreadline` does indeed not work, but then it is not intended to be used that way since I use `./sage -sh` and then `maxima-noreadline` since that is how we use it from inside Sage. But I can use `exec "$SAGE_ROOT/maxima" "$`@`"` and something analog for clisp.

Yes, but what if I run `./sage -sh` and then mess with the `PATH` in some random way, i.e. prepending my alternate system-wide maxima to the PATH, etc. Then `maxima-noreadline` won't work as expected. If it's not expected that the user runs `maxima-noreadline`, then it doesn't belong into `$SAGE_ROOT/local/bin`, IMHO...

Unless there is a compelling reason not to, I'm inclined to use my version of the scripts which don't have any of these issues, and also give the user the option to run maxima or clisp with readline disabled, with a sensible command line UI. In the case of maxima, this is even complying with what's offered by `maxima --help`.


---

Comment by mabshoff created at 2009-04-20 00:23:13

I am happy to address the issue with `exec "$SAGE_LOCAL"/bin/...`, but I still prefer my version since upstream clisp and maxima do not have such version.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-20 00:42:49

The above change has been implemented in 

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/maxima-5.16.3.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-20 00:59:27

The clisp.spkg at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/rc4/clisp-2.47.p0.spkg

uses exec to avoid running an extra bash process when starting clisp. This has been requested by Gonzalo and he is right to insist :)

Cheers,

Michael


---

Comment by tornaria created at 2009-04-20 01:09:05

Replying to [comment:9 mabshoff]:
> I am happy to address the issue with `exec "$SAGE_LOCAL"/bin/...`, but I still prefer my version since upstream clisp and maxima do not have such version.

Not my choice, but I'm fine with this.


---

Comment by tornaria created at 2009-04-20 01:12:54

I'm ok with the scripts in maxima-5.16.3.p1.spkg and clisp-2.47.p0.spkg.


---

Comment by mabshoff created at 2009-04-20 03:48:23

Resolution: fixed


---

Comment by mabshoff created at 2009-04-20 03:48:23

Merged maxima-5.16.3.p1.spkg and clisp-2.47.p0.spkg in Sage 3.4.1.rc4.

Cheers,

Michael
