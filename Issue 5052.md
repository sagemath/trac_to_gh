# Issue 5052: preparser does not respect leading space in front of "load foo.sage"

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2009-01-22 09:03:25

Assignee: cwitty

If you have something like the following in a file:

```
try:
    load foo.sage
except:
    print 'uh oh'
```

it gets preparsed to this, and blows up because of the bad indentation:

```
try:
execfile("foo.py")
except:
    print 'uh oh'
```

The preparser is not honoring the leading space before the `load` statement.


---

Attachment


---

Comment by ddrake created at 2009-01-23 03:58:34

The problem was in sage-preparse; it ran a lstrip() on the line and never took into consideration the indentation.

I wanted to add some doctests, since as we see here, anything not tested is broken -- do the files in `$SAGE_ROOT/local/bin` get doctested?


---

Comment by boothby created at 2009-01-24 08:02:25

works for me


---

Comment by mabshoff created at 2009-01-28 12:35:52

Merged in Sage 3.3.alpha3


---

Comment by mabshoff created at 2009-01-28 12:35:52

Resolution: fixed
