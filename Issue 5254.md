# Issue 5254: Mac app bundle: check for relocation at startup since the bundle version does not trigger the move check

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-13 10:32:41

Assignee: mabshoff

CC:  mhansen

From 

When starting Sage right after copying it over from the dmg Maxima as well as clisp do not work. After quitting a manual start triggers the rewrite:

```
Sprocketer:sage michaelabshoff$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH (please wait at
most a few minutes)...
Do not interrupt this.
```

Then Maxima as well as clisp work:

```
sage: !maxima
Maxima 5.16.3 http://maxima.sourceforge.net
Using Lisp CLISP 2.46 (2008-07-02)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) 2+2;
(%o1)                                  4
(%i2) 
sage: !clisp
  i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
  I I I I I I I      8     8   8           8     8     o  8    8
  I  \ `+' /  I      8         8           8     8        8    8
   \  `-+-'  /       8         8           8      ooooo   8oooo
    `-__|__-'        8         8           8           8  8
        |            8     o   8           8     o     8  8
  ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8
| Sage Version 3.3.rc0, Release Date: 2009-02-11                     |
| Type notebook() for the GUI, and license() for information.        |
Welcome to GNU CLISP 2.46 (2008-07-02) <http://clisp.cons.org/>

Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
Copyright (c) Bruno Haible, Sam Steingold 1999-2000
Copyright (c) Sam Steingold, Bruno Haible 2001-2008

Type :h and hit Enter for context help.

[1]> 
Bye.
sage: 
Exiting SAGE (CPU time 0m0.12s, Wall time 0m21.46s).
Sprocketer:sage michaelabshoff$ 
```


Change the logic of the Sage startup script to trigger the relocation script in case Sage has moved. 

Cheers,

Michael


---

Comment by GeorgSWeber created at 2009-02-15 09:44:45

replaces the file "script" under $SAGE_APP_ROOT/Contents/Resources/


---

Attachment

Hi Michael,

I couldn't trigger the Maxima failure (don't know why), but I could see that the Sage app bundle's "/local/lib/sage-current-location.txt" wasn't updated as it should. The new script I attached does fix this and should handle environmental settings cleaner on a broader scale. I didn't know where you want me to put it (certainly not inside some "tar.gz"), so I uploaded it plain as-is.

You said in sage-devel (Google thread) that you had a fix for dir names with spaces -- I don't see where, but anyway that fix of yours should apply as before.

One important thing I noted: The README.txt in the .dmg dates from Sage 2.9.2 and should definiteley either be updated, or killed. Probably you have to adjust sage-sdist and sage-bdist a bit to stop remnants of this (e.g. "$SAGE_ROOT/sage-README-osx.txt") from lurking around.

One other thing:

+1 to your idea to name the app bundle "Sage.x.y.z" instead of "Sage". What do you think of putting in the name also the dependency "Intel vs. PPC" resp. "32Bit vs. 64Bit"? (It's not a "universal binary" we deliver, do we?)

Cheers, gsw


---

Comment by mabshoff created at 2009-02-15 10:49:02

Replying to [comment:1 GeorgSWeber]:
> Hi Michael,

Hi Georg,

> I couldn't trigger the Maxima failure (don't know why),

The original poster in that thread had some other issues, too, but I could certainly hit it when I used a dmg build on another box where my home directory was different. If the original Sage build is still in place it should "just work" since the old install is being picked up.

> but I could see that the Sage app bundle's "/local/lib/sage-current-location.txt" wasn't updated as it should. The new script I attached does fix this and should handle environmental settings cleaner on a broader scale. I didn't know where you want me to put it (certainly not inside some "tar.gz"), so I uploaded it plain as-is.

Cool.

> You said in sage-devel (Google thread) that you had a fix for dir names with spaces -- I don't see where, but anyway that fix of yours should apply as before.

The fix isn't up yet and it is mostly in the "I think I know how to fix this stage", so no tested code yet. Notice that at #5261 there are all the other issues I would like to sort out.

> One important thing I noted: The README.txt in the .dmg dates from Sage 2.9.2 and should definiteley either be updated, or killed. Probably you have to adjust sage-sdist and sage-bdist a bit to stop remnants of this (e.g. "$SAGE_ROOT/sage-README-osx.txt") from lurking around.

Ok, please open a critical ticket against 3.3 to update the OSX readme. 

> One other thing:
> 
> +1 to your idea to name the app bundle "Sage.x.y.z" instead of "Sage". What do you think of putting in the name also the dependency "Intel vs. PPC" resp. "32Bit vs. 64Bit"? (It's not a "universal binary" we deliver, do we?)

Yep, please add that as a comment to #5261 so it doesn't get lost. We don't do universal since there are issues with the build all over the place, i.e. gmp doesn't support it. MPIR might at some point in the future, but that leaves other issues to be fixed. 

I can imagine to fix this in three ways: 

 * Make everything build universal by adjusting and fixing all build systems in Sage's spkg (giant amount of work)
 * use lipo to join all binaries and libraries after building them locally (I have played with this)
 * add a wrapper script that starts the appropriate sage since we could have sage-x86, sage-x86-64, sage-ppc and sage-ppc64 sitting inside the DMG all in parallel. This causes its own set of issues (how do you upgrade something like that? Will people download the 1.2GB?), but if there is interest given that we now have the DMG + App bundle in place this would be the quickest way to get a universal binary going (Once we have fixed the last couple pesky bugs for 64 bit OSX support :)
 
Anyway, if you feel this point warrants discussion and/or interest please open a new thread on sage-devel.

> Cheers, gsw

Thanks for fixing this, I am *swamped* :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:25:26

Better luck in 3.4.1.

Cheers,

Michael


---

Comment by justin created at 2009-03-16 04:46:22

I found the following while testing this:

1) lisp.run crashes each time I quit Sage.app (I don't think the crash is related to the script; just mentioning it).

2) The app can be repeatedly run and maxima exits and restarts as appropriate, with no apparent issues.  This is good.

3) The script is run each time Sage.app starts.  The script should only be run if the .app has been moved, correct?

See #5261 for related issues, and coordinate this (which should be a true patch) with fixes for that Trac report.


---

Comment by GeorgSWeber created at 2009-03-17 22:08:02

Hi Justin, thanks for the comments!

Having slept over them, I feel a bit at a loss, however:

1, 2) I have seen "lisp.run" threads (via the OS X "activity monitor") only during doctests, or when Maxima was somehow started explicitly or implicitly during a Sage session. I have no clue how the "app" mechanism is related to the crashes you see. Perhaps an "exit" command at the end of the script might help, but this is wild guessing, and right now I don't have the time to poke around.

3) Incorrect. The script itself is the "app" script that starts Sage up, so has to be called itself every time. And as for checking whether the Sage app has moved, we have to call the "sage-location" script every time, too --- or double somehow its content. How should we know that the Sage app has moved without checking whether it has moved? And checking this is exactly what the "sage-location" script does, so there. (Why reinvent the wheel?)


---

Comment by iandrus created at 2009-11-28 09:16:23

These changes were incorporated into #5261.

I haven't been able to reproduce the lisp.run crashes.


---

Comment by kcrisman created at 2009-12-08 15:24:39

I recommend this ticket be closed.  #5261 and #7546 do take care of the other issues, or at the very least are responsible for them (I'm almost done reviewing them on two different Mac platforms).


---

Comment by mhansen created at 2009-12-08 17:12:54

Sounds good to me.


---

Comment by mhansen created at 2009-12-08 17:12:54

Resolution: invalid
