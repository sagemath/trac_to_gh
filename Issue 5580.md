# Issue 5580: preparsing error in recursive load of .sage files

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-21 17:08:40

Assignee: cwitty

CC:  mvngu


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

  -- Jason Bandlow
```


I can confirm this bug in Sage-3.4. 


---

Comment by mpatel created at 2010-02-01 08:41:41

The example in the description works for me.  I suggest closing this ticket as fixed (probably by #7514) but reopening it, if I'm wrong.


---

Comment by mvngu created at 2010-02-01 08:49:14

Close as fixed:

```
[mvngu`@`mod sage-4.3.2.alpha1-sage.math]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: load foo.sage
sage: type(foo())
<type 'sage.rings.rational.Rational'>
sage: load bar.sage
sage: type(foo())
<type 'sage.rings.rational.Rational'>
sage: !more foo.sage
def foo():
    return (-1)**(-1)
sage: !more bar.sage
load foo.sage
```



---

Comment by mvngu created at 2010-02-01 08:49:14

Resolution: fixed


---

Comment by mpatel created at 2010-02-01 10:16:44

One can measure the importance of a scientific work by the number of earlier publications rendered superfluous by it. - D. Hilbert
