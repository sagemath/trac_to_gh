# Issue 44: customize preparsing

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:55:32

Assignee: somebody

> I made the suggested changes and everything works fine.
>
> Thank you for replying so quickly.
>
> I think that modifying the preparser to meet different needs
> sounds like a good idea as long as the underlying code didn't
> have to change.

WAIT ! -- good point.  In fact, there is code in the SAGE library
that assumes that the preparser replaces ^'s by **'s.  If you
do exactly what I suggested, you could get subtle bugs in certain
places involved in moving expressions between GAP/Singular and SAGE
that use the SAGE preparser.
So at least don't make those changes to preparse.py.

It's fine to make the changes to integer.pyx that defines __xor__,
and certainly you'll find that useful.  

For now, the best thing for you to do might be to start SAGE with

    sage -ipython 

to get SAGE with no preparsing at all. 

The solution to all this is probably to make the interactive preparser 
customizable and make those customizations only apply to the
interactive preparser.  (I.e., the preparser will have a context as input,
one for the interactive session, and the other used internally by
the library).  One could also have a context set at the top of a .sage
file.  

Sorry for the confusion.  

william


---

Comment by was created at 2008-05-14 22:23:44

Resolution: invalid


---

Comment by was created at 2008-05-14 22:23:44

We discussed this a lot in sage-devel.  Having a user-customizable preparser is something that has happened a little -- e.g., Bradshaw added support for implicit multiplication preparsing.  But it doesn't make any sense for "this" to be a trac ticket.  It is general, vague, done, and can never be finished, all at once.
