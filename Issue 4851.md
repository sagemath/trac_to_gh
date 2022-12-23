# Issue 4851: infinite recursion with encoding entities for worksheet titles with apostrophes, etc

Issue created by migration from https://trac.sagemath.org/ticket/4851

Original creator: ddrake

Original creation time: 2008-12-22 07:34:52

Assignee: boothby

The title seems complicated but the problem is easy to see: if one creates a worksheet with an apostrophe in the title, like this:

```
I'm an apostrophe
```

then saves, quits, and reloads the worksheet, the title is now:

```
I&apos;m an apostrophe
```

If you quit and reload the worksheet, the title becomes:

```
I&amp;apos;m an apostrophe
```

...and so on. The ampersand is replaced by "`&amp;`", and then THAT ampersand gets replaced by...and so on. The problem seems to happen with any HTML entity. I'm seeing this with 3.2.2.


---

Comment by mhansen created at 2009-01-19 08:04:00

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2009-01-19 08:04:00

Changing status from new to assigned.


---

Attachment

The code looks good, and the reported problem is fixed. I give this a positive review provided that a doctest gets added, or a test in the Selenium test suite is added.


---

Comment by mabshoff created at 2009-01-19 09:51:59

Merged in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-19 09:51:59

Resolution: fixed
