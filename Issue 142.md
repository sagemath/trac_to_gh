# Issue 142: sage build shouldn't modify $HOME

Issue created by migration from https://trac.sagemath.org/ticket/142

Original creator: was

Original creation time: 2006-10-21 03:37:21

Assignee: was


```
>
> Yep...  My $HOME/.sage belonged to "root".  I have no idea why that
> happened either...  Maybe I used a "sudo" when I shouldn't...  (But I
> really think I just used to "make".)  In any case, a "sudo chown -R"
> fixed it.

Yes, this is a known bug in the install process. SAGE get's run 
during the install, which can cause some problems like you just
had if the user doing the build is root but the $HOME for root
is not /root.

William
```



---

Comment by was created at 2007-10-21 01:48:35

Sage should *definitely* be allowed to run during the build.  That's just the
way it is.


---

Comment by was created at 2007-10-21 01:48:35

Resolution: invalid
