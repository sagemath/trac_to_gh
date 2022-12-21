# Issue 7186: maxima update #6699 introduced hard-coded paths, unable to start maxima

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2009-10-10 20:41:40

Assignee: tbd

Just take a newly built Sage-4.1.2.alpha4, say, containing the newly introduced maxima 5.19.1 / ecl 9.8.4 (Sage-4.1.1 had older versions of maxima/ecl). In the SAGE_ROOT directory type

```
(build_path)$ ./sage -sh
(build_path)$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: exit
(build_path)$ maxima
;;; Loading #P"/Users/Shared/sage/sage-4.1.2.alpha4/local/lib/ecl-9.8.4/DEFSYSTEM.fas"
;;; Loading #P"/Users/Shared/sage/sage-4.1.2.alpha4/local/lib/ecl-9.8.4/cmp.fas"
;;; Loading #P"/Users/Shared/sage/sage-4.1.2.alpha4/local/lib/ecl-9.8.4/sysfun.lsp"
Maxima 5.19.1 http://maxima.sourceforge.net
Using Lisp ECL 9.8.4
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) quit(); 
```

and you'll see a slightly different output, since obviously a hardcoded path to ecl is displayed. Now move the entire Sage build to some other directory. Type the above again, you'll get

```
(other_path)$ ./sage -sh
(other_path)$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
The Sage install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(please wait at most a few minutes)...
Do not interrupt this.
Loading Sage library. Current Mercurial branch is: test
sage: exit
Exiting SAGE (CPU time 0m0.14s, Wall time 0m7.62s).
Exiting spawned Gap process.
(other_path)$ maxima
| Sage Version 4.1.2.alpha4, Release Date: 2009-09-27                |
| Type notebook() for the GUI, and license() for information.        |
| Sage Version 4.1.2.alpha4, Release Date: 2009-09-27                |
| Type notebook() for the GUI, and license() for information.        |
Internal or unrecoverable error in:
Cannot find ECL's directory
  [2: No such file or directory]
Abort trap
(other_path)$
```

and inside this "moved" Sage, any calls to functionalities involving calling maxima now fail thus:

```
sage: f = x^2
sage: f.integrate(x)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...

TypeError: Unable to start maxima
```

This means, among other things, that it will be impossible to create Sage binaries, that work --- unless they're installed in *precisely* the path they were built in!


---

Comment by was created at 2009-10-11 17:41:09


```

I was reading the ecl binaries and grepping around (I felt a bit like a "warez person" for a moment)... and found this in the binary:

    ... ECLDIR^`@`Cannot find ECL's directory^...

So I tried setting ECLDIR, and that fixes the problem.  Maybe we just broken setting it somewhere?   Or?

wstein`@`sage:~/build/sage-4.1.2.rc1.alpha2.moved/local/lib/ecl-9.8.4$ export ECLDIR=`pwd`
wstein`@`sage:~/build/sage-4.1.2.rc1.alpha2.moved/local/lib/ecl-9.8.4$ ecl
[works]

wstein`@`sage:~/build/sage-4.1.2.rc1.alpha2.moved/local/lib/ecl-9.8.4$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: sage: f = x^2
sage: sage: f.integrate(x)
1/3*x^3
```



---

Comment by was created at 2009-10-11 17:52:55

Planned fix:

Option 1: Put 

```
ECLDIR="$SAGE_LOCAL/lib/ecl"; export ECLDIR
```

in sage-env, and put the following in the ecl spkg:

```
cd $SAGE_LOCAL/lib/; rm -f ecl; ln -s ecl-* ecl
```


This is robust against moves.  It assumes we don't have multiple local/lib/ecl's installed, which the spkg should fix anyways, right?


---

Comment by GeorgSWeber created at 2009-10-11 18:33:53

Good catch!

I just finished building from scratch Sage-4.1.2.rc0, with the single change the ecl-9.8.4 was replaced by the older ecl-9.41 spkg from Sage-4.1.1. and had essentially the same finding as before. Starting maxima from the build dir:

```
computer:/Users/Shared/sage/build/sage-4.1.2.rc0 georgweber$ maxima
;;; Loading #P"/Users/Shared/sage/build/sage-4.1.2.rc0/local/lib/ecl-9.4.1/DEFSYSTEM.fas"
;;; Loading #P"/Users/Shared/sage/build/sage-4.1.2.rc0/local/lib/ecl-9.4.1/cmp.fas"
;;; Loading #P"/Users/Shared/sage/build/sage-4.1.2.rc0/local/lib/ecl-9.4.1/sysfun.lsp"
Maxima 5.19.1 http://maxima.sourceforge.net
Using Lisp ECL 9.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) quit();

```

After moving, starting maxima failed silently (i.e. without error message), but failed nevertheless. So I guessed it's not something wrong with ecl, but with the way that maxima is built/installed. Now let's have a look into the script $SAGE_ROOT/local/bin/maxima. Near the start, we have:

```
setup_vars() {
  if [ -z "$MAXIMA_VERSION" ]; then
    MAXIMA_VERSION=5.19.1
  fi
  prefix=`unixize "/Users/Shared/sage/build/sage-4.1.2.rc0/local"`
  exec_prefix=`unixize "${prefix}"`
  PACKAGE=maxima
  top_srcdir=`unixize "/Users/Shared/sage/build/sage-4.1.2.rc0/spkg/build/maxima-5.19.1.p0/src"`
  libdir=`unixize "${exec_prefix}/lib"`
```

which made me curious how this could have ever worked (it's essentially the same for the old maxima from Sage-4.1.1). But then I saw lines 111 - 123:

```
setup_vars

if [ ! -d "$MAXIMA_IMAGESDIR" ]; then
# Have we been moved?
  MAXIMA_PREFIX=`(cd \`dirname $0\` 1>/dev/null 2>/dev/null; dirname \`pwd\`)`
  export MAXIMA_PREFIX
  unsetup_vars
  setup_vars
  if [ ! -d "$MAXIMA_IMAGESDIR" ]; then
    echo "$0: unable to determine MAXIMA_PREFIX" 1>&2
    exit 1
  fi
fi
```

This might be a another good place to set the ECLDIR environment variable (i.e., if it isn't already set), what do you think? (This would avoid the introduction of a new environment variable in sage-env.)

Who's going to make the changes, and who's going to review?
(I do like the one-line change to ecl you proposed.)


---

Comment by GeorgSWeber created at 2009-10-11 20:47:41

Almost, there's more than meets the eye.

If I do the "cd $SAGE_LOCAL/lib/ && rm -f ecl && ln -s ecl-* ecl" command and add the following after line 123 in $SAGE_ROOT/local/bin/maxima (which one should patch in maxima_spkg/src/src/maxima.in by maxima's "spkg-install"):

```
if [ -n "$MAXIMA_PREFIX" ]; then
  ECLDIR="$MAXIMA_PREFIX"/lib/ecl/
else
  ECLDIR="$libdir"/ecl/
fi
export ECLDIR
```

(do mind the slash at the end of the variables, for me, it does seem to be worse without), then on one test installation it works. On the other I get (and Sage doesn't work either):

```
computer:/Users/Shared/sage/test/sage-4.1.2.alpha4 georgweber$ maxima
;;; Loading #P"/Users/Shared/sage/test/sage-4.1.2.alpha4/local/lib/ecl/DEFSYSTEM.fas"
;;; Loading #P"/Users/Shared/sage/test/sage-4.1.2.alpha4/local/lib/ecl/cmp.fas"
;;; Loading #P"/Users/Shared/sage/test/sage-4.1.2.alpha4/local/lib/ecl/sysfun.lsp"
Maxima encountered a Lisp error:

 NIL is not of type (OR FILE-STREAM STRING PATHNAME).

Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
computer:/Users/Shared/sage/test/sage-4.1.2.alpha4 georgweber$
```

If the slash (remark in parenthese above) is missing, the same error message occurs, but without the three lines beginning with ";;;".

The "working installation" is the one with Sage-4.1.2.rc0 and ecl replaced by ecl-9.4.1; the "non-working installation" is Sage-4.1.2.alpha4 (with the current maxima and ecl spkgs). I don't know yet what exactly makes the difference. Next I'll try with Sage-4.1.2.rc0 "vanilla".


---

Comment by was created at 2009-10-12 04:55:17

Changing Maxima as you mention above is not a good plan at all, since one still wants to be able to run ECL from Sage, e.g., no matter what hack you can imagine to fix Maxima along the lines above, this will still fail:

```
./sage -ecl
```



---

Comment by was created at 2009-10-12 05:02:43

Changing status from new to needs_review.


---

Comment by was created at 2009-10-12 05:02:43

See the new spkg here, which must be combine with the attached patch to sage-env (against "scripts" repo):
http://sage.math.washington.edu/home/wstein/patches/ecl-9.8.4-20090913cvs.p2.spkg


---

Attachment

Yep, I missed the point about standalone "./sage -sh && sage -ecl" not working after a move of the Sage tree. This should go in now, in order to get the necessary testing on many platforms as soon as possible. The new spkg is clean (I just downloaded it, unpacked it, and looked at "hg export default"), and the changes to sage-env look sane, so I give a positive review right away.


---

Comment by GeorgSWeber created at 2009-10-12 06:05:21

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2009-10-12 09:59:27

Just fixing the title to make sure it isn't confusing.


---

Comment by was created at 2009-10-12 19:30:14

Resolution: fixed


---

Comment by was created at 2009-10-12 19:30:14

> and the changes to sage-env look sane, so I give a positive review right away. 

For the record, it turns out one must do

```
ECLDIR="$SAGE_LOCAL/lib/ecl/"
```

instead of what I had.  I've made this fix.


---

Comment by chapoton created at 2017-07-19 09:02:59

for uniqueness of author names
