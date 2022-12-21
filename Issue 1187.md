# Issue 1187: bug in G.conjugacy_classes_subgroups()

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-16 20:45:35

Assignee: mhansen

The following should work and be instant:


```
sage: G = SymmetricGroup(5)
sage: G.conjugacy_classes_subgroups()

RuntimeError:
Gap produced error output
Variable: 'Sym' must have a value


   executing $sage85:=Sym( [ 1 .. 5 ] );;
```



I really wanted this to find out which representative subgroups
are transitive, but can't do that either since `G.is_transitive()`
isn't wrapped -- since Gap has IsTransitive, this would be trivial to wrap.


---

Comment by AlexGhitza created at 2008-04-24 22:25:44

Changing component from combinatorics to group_theory.


---

Comment by AlexGhitza created at 2008-04-24 22:25:44

Changing assignee from mhansen to joyner.


---

Attachment

The attached patch fixes what I believe is a bug in conjugacy_classes_subgroups(), and adds the method is_transitive().  Note that the optional GAP database is *not* required.

Timings before the patch:


```
sage: G = SymmetricGroup(6)
sage: time cl = G.conjugacy_classes_subgroups()
CPU times: user 151.62 s, sys: 16.75 s, total: 168.37 s
Wall time: 175.53
```


and after:


```
sage: G = SymmetricGroup(6)
sage: time cl = G.conjugacy_classes_subgroups()
CPU times: user 0.54 s, sys: 0.09 s, total: 0.63 s
Wall time: 1.35
```



---

Comment by wdj created at 2008-04-24 23:10:47

Is this based on 3.0? I am getting aborted when I try to hg_sage.apply it.


---

Comment by AlexGhitza created at 2008-04-24 23:16:36

Yes, it's based on 3.0, with no other patches around.


---

Comment by wdj created at 2008-04-24 23:32:14

Thanks - I got it applied now. Will be running test, etc on it tonight.


---

Comment by wdj created at 2008-04-25 02:44:17

Looks like a great patch, adding functionality, fixing a bug and correcting some typos in the permgp.py docstrings. Passes sage -testall on an ubuntu 7.10amd64 machine and an intel macbook running OS10.4.


---

Comment by mabshoff created at 2008-04-25 03:05:09

Resolution: fixed


---

Comment by mabshoff created at 2008-04-25 03:05:09

Merged in Sage 3.0.1.alpha0
