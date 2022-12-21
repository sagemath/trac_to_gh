# Issue 2118: "Delete all output" function on notebook

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2008-02-08 19:02:22

Assignee: boothby

There's already a "hide all output" function that is really good. However, it is not persistent:
If you navigate away from the worksheet and go back, all the output is there again.

In a presentation scenario, one would probably want the output to be not there right when you open up the worksheet. (you might for instance want to make the opening of the worksheet part of the demo). Therefore, a more persistent hiding or removing of output would be good to have.

I guess I could do it myself: delete all lines between

///

and 

}}}

but I think this is a sufficiently frequent operation that it deserves its own place.


---

Comment by was created at 2008-05-10 17:10:36

This is a duplicate of #336.


---

Comment by was created at 2008-05-10 17:10:36

Resolution: duplicate
