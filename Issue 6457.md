# Issue 6457: Intersection of ideals in a number field

Issue created by migration from https://trac.sagemath.org/ticket/6457

Original creator: davidloeffler

Original creation time: 2009-07-02 13:10:13

Assignee: was

Keywords: ideal

This is not difficult but for some reason it wasn't implemented before. Here it is.


---

Comment by davidloeffler created at 2009-07-02 13:12:48

patch against 4.1.alpha2


---

Attachment


---

Comment by davidloeffler created at 2009-07-02 13:13:04

Changing keywords from "ideal" to "ideals".


---

Comment by ncalexan created at 2009-07-14 21:23:34

These doctests don't convince me that the the results are correct, but I don't see a one line way to assert that, so: positive review!


---

Comment by mvngu created at 2009-07-18 20:00:51

I assume David is the author of `trac_6457-ideal_intersection.patch`, since Nick reviewed this ticket. David, the patch `trac_6457-ideal_intersection.patch` doesn't contain your username. So I'm committing it in your name.


---

Comment by mvngu created at 2009-07-18 20:00:51

Resolution: fixed
