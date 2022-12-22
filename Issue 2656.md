# Issue 2656: "sage -hg" does not handle quoting correctly

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-23 17:40:40

Assignee: was

If you use "sage -hg" with arguments containing spaces, like:

```
  sage -hg commit -m "This is my great new code."
```

then the argument gets split up, so Mercurial sees something more like

```
  hg commit -m This is my great new code.
```

(and tries to check in files named is,my,great,new,code., with a commit message of "This").


---

Comment by mabshoff created at 2008-04-13 19:03:49

We need to escape the '"' (and probably some other characters):

```
[mabshoff`@`localhost ~]$ ./foo.bash commit -m "This is my great new code."
commit -m This is my great new code.
[mabshoff`@`localhost ~]$ ./foo.bash commit -m \"This is my great new code.\"
commit -m "This is my great new code."
```

where foo.bash is

```/bin/bash
echo "$`@`"
```


Cheers,

Michael


---

Comment by jdemeyer created at 2010-10-10 21:09:52

Seems to be fixed in sage-4.6.


---

Comment by jdemeyer created at 2010-10-10 21:09:52

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-10-22 09:32:49

Resolution: worksforme
