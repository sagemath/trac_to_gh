# Issue 5579: preparsing error in recursive load of .sage files

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-21 17:08:22

Assignee: cwitty


```
Hi all,

I ran into the following unexpected behavior, which I assume is because
the preparser does not work with nested loads.  I have two files,
foo.sage and bar.sage.  Their contents are as follows:

foo.sage
--------
def foo():
 return (-1)**(-1)


bar.sage
--------
load foo.sage


The following sage session works as expected:
       sage: load foo.sage
       sage: type(foo())
       <type 'sage.rings.rational.Rational'>

The following session does not:
       sage: load bar.sage
       sage: type(foo())
       <type 'float'>

I'm guessing that in the second session the file foo.sage is not getting
preparsed (and so foo() returns a Python object and not a Sage object).
 Is this correct? If so, is there a way to force it to be preparsed?  I
like to have lots of little files with different functions, and then a
file which loads whichever of these happen to be working/relevant at the
moment.  That way I only have to load one file at the start of my session.

Any advice is much appreciated!
```


I can confirm this bug in Sage-3.4. 


---

Comment by was created at 2009-03-21 17:09:30

Resolution: duplicate


---

Comment by was created at 2009-03-21 17:09:30

stupid trac...
