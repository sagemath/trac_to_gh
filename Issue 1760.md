# Issue 1760: on osx make a symlink sage.command --> sage

Issue created by migration from https://trac.sagemath.org/ticket/1760

Original creator: was

Original creation time: 2008-01-11 22:20:11

Assignee: was

CC:  iandrus


```
Well, perhaps this is know, but apropos the petition to make steps
4--6 of installation in OS X nicer, there are a very easy way. Simply
rename the sage script to sage.command. This way if you double-click
over it from finder it will be automatically launched inside a
Terminal session.

Saludos,
Rafa

P.D. I'm not a OSX guru, only a /bin/sh user in OSX landscape ;-)
```



---

Comment by was created at 2008-01-11 22:21:56

One way to implement this is make it so sage -bdist on osx, in addition to just making  dmg, also does

```
 ln -s sage sage.command
```

in SAGE_ROOT right before making the dmg file.   This should just involve
adding one line to SAGE_ROOT/local/bin/sage-bdist


---

Comment by mabshoff created at 2008-09-16 04:00:29

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-16 04:00:29

Changing assignee from was to mabshoff.


---

Comment by AlexGhitza created at 2009-01-23 07:09:20

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2011-06-02 04:44:09

Wow, I can't believe this ticket eluded detection for all this time.  Do we really need this now that we have the app bundle (even made all the time, thanks Jeroen!)?


---

Comment by kcrisman created at 2012-07-07 04:23:55

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-07-07 04:23:55

Bye-bye.  Not that it isn't fun to have a symlink, but anyone who really needs this will either
 * download the app because they don't know how to do this
 * make a symlink themselves because they do.


---

Comment by kcrisman created at 2012-07-07 04:25:13

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-01 12:26:28

Resolution: wontfix
