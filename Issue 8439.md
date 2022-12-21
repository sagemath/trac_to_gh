# Issue 8439: maxima interface hangs gcl and/or clisp backends

Issue created by migration from Trac.

Original creator: pcpa

Original creation time: 2010-03-04 22:37:40

Assignee: was

CC:  mjo chapoton

This is a possible problem when using an external maxima, that uses a backend other then ecl.

clisp has some peculiar ways to figure out there is an associated pty, that is created by pty.py from pexpect interface.

gcl hangs due to an "unexcaped" ecl specific command at the start of maxima interface; this took quite some time to find, as I was thinking it was a clisp like related issue, and tried to correct the problem in gcl and/or sage-maxima.lisp.

Also, probably not related, or a know issue, any lisp backend will hang with a command as simple as:

    sage: maxima.eval('1+1;;')

that is, two sequential semicolons will apparently confuse the expect interface.

With the attached patch, going to be used in mandriva rpm, all currently maxima backends works in sage. (When installing sagemath, unless using --auto-select, the installation process will ask what package that provides maxima-backend the user wants, and the options are sbcl, clisp, gcl and ecl).


---

Comment by pcpa created at 2010-03-17 20:24:56

I asked in http://lists.gnu.org/archive/html/gcl-devel/2010-03/msg00000.html about some possible solution for the issue of gcl backend hanging, but now I believe I found a better workaround, so that, maxima gcl backend has the same behavior as other lisps.

The problem is that adapting the solution used for clisp in `$SAGE_LOCAL/bin/sage-maxima.lisp `was not enough, as for some reason, the predicate `(output-stream-p *standard-input*) `was still true in the maxima parsing error message code.

The new patch should correct the issue, or at least, now it doesn't hang in the doctect

`sage: maxima.eval('sage0: x == x;')`


---

Comment by pcpa created at 2010-03-17 20:26:03

sage-4.3.3-maxima.patch


---

Comment by mjo created at 2012-01-16 02:55:39

Changing status from new to needs_review.


---

Attachment


---

Comment by kcrisman created at 2012-01-28 02:34:39

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2012-01-28 02:34:39

Umm... is this even valid anymore?  Putting 'needs info'.  

I certainly can't believe that this would apply properly any more... and it doesn't.


---

Comment by mjo created at 2012-01-28 02:57:21

Actually, I took a look at this when I was looking for tickets that might be fixed by maxima-5.24. Right now on my machine, it hangs:


```
$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: devel
sage: maxima.eval('1+1;;')
```

| Sage Version 5.0.beta1, Release Date: 2012-01-22                   |
| Type notebook() for the GUI, and license() for information.        |
(I've waited a good minute.)


---

Comment by kcrisman created at 2012-01-28 03:04:17

Here's what happens in Maxima.

```

(%i4) 1+1;;

(%o4) 2

stdin:76667:incorrect syntax: Premature termination of input at ;.
;
 ^
```

I'm just going to make a ticket for that - it's #12372.

This is still a somewhat weird ticket.  I didn't even know we allowed other Maxima backends officially.


---

Comment by kcrisman created at 2012-01-28 03:04:24

Changing priority from major to minor.


---

Comment by pcpa created at 2012-01-28 04:51:39

I do not remember the exact reason I used the "1+1;;" example. Maybe as a hint to show that the interface was very fragile.

I did the initial work to make maxima clisp backend functional because at the time I worked in the first sagemath package it was the lisp used by sage.

I just tested, and all backends (clisp, gcl, ecl, and sbcl) appear functional in my sagemath package.

The patch used is still sage-4.3.3-maxima.patch (renamed/rediffed) and the related maxima patch is http://svn.mandriva.com/viewvc/packages/cooker/maxima/current/SOURCES/maxima-5.23.0-clisp-noreadline.patch?view=markup that should need a somewhat recent clisp, that understands the -disable-readline option (it was added upstream due to my bug report about this same issue).

In the case of my sagemath rpm package, for quite some time it requires maxima-runtime-ecl, so, only experienced users should usually install other backends in normal conditions due to never being asked to choose one, at least when installing sagemath.


---

Comment by kcrisman created at 2012-01-28 05:05:58

This is very interesting.  Is there any documentation about this backend business?  I'm not as familiar with Mandriva as I ought to be - is this something like the Gentoo idea, where Sage is used with system versions of the programs?


---

Comment by pcpa created at 2012-01-28 05:50:39

Yes. It is a rpm package installing a sagemath that uses (mostly) system packages. The first working package (at least notebook and most interfaces) I had was for sage 3.2.3. But update after update, it got only good when updating to sage 4.0.1.

About maxima backends, I think the proper term is maxima runtime. Just the lisps enabled at compile time. Example:


```
$ maxima --list-avail
Available versions:
version 5.24.0, lisp ecl
version 5.24.0, lisp clisp
version 5.24.0, lisp sbcl

```



---

Comment by mkoeppe created at 2020-06-28 19:22:09

Changing status from needs_info to needs_review.


---

Comment by mkoeppe created at 2020-06-28 19:22:09

This ticket is outdated and should be closed.


---

Comment by chapoton created at 2020-06-28 19:29:53

Resolution: invalid
