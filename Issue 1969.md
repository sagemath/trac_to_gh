# Issue 1969: ipython -- update to svn to get this new %hist functionality

Issue created by migration from https://trac.sagemath.org/ticket/1969

Original creator: was

Original creation time: 2008-01-29 10:54:40

Assignee: was


```
> Something like %history, but which writes the output to a file.

I just put it in SVN, as the new '-f flag'. This is what it looks like:

In [1]: hist -f foo
File 'foo' exists. Overwrite? n
Aborting.

In [2]: hist
1: _ip.magic("hist -f foo")
2: _ip.magic("hist ")

In [3]: hist -r
1: hist -f foo
2: hist
3: hist -r

In [4]: hist -rn
hist -f foo
hist
hist -r
hist -rn

In [5]: hist -rn -f foo
File 'foo' exists. Overwrite? y

In [6]: !cat foo
hist -f foo
hist
hist -r
hist -rn
hist -rn -f foo

> By the way, %hist still is preparsed in Sage.  I should have fixed
> this long ago.  Could you remind me what you recommended I do?

See above, -r gives you the raw history always, and -n omits line numbers.


Let me know how this works for you.

 -- Fernando
```



---

Comment by mabshoff created at 2008-08-13 07:31:22

Resolution: duplicate


---

Comment by mabshoff created at 2008-08-13 07:31:22

Duplicate, we did update to ipython 0.8.2.

Cheers,

Michael
