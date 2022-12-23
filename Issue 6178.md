# Issue 6178: Hermite normal form over PID's

Issue created by migration from https://trac.sagemath.org/ticket/6178

Original creator: davidloeffler

Original creation time: 2009-06-01 14:18:08

Assignee: was

CC:  was ncalexan

Keywords: echelon form

I've written some code that calculates Hermite normal form over a general PID. I wrote this because I needed it for a particular application; I will now go ahead with that as a means of stress-testing the code I've just written, but this ticket is here to remind me.


---

Comment by davidloeffler created at 2009-06-02 21:37:32

patch against 4.0.1.alpha0


---

Comment by davidloeffler created at 2009-06-02 21:50:15

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-06-02 21:50:15

Changing status from new to assigned.


---

Attachment

Here's a patch, which adds echelon form (= Hermite normal form) over PID's. I've also added a simple routine for kernel finding over PID's using Smith form (since the algorithm we had before silently assumed that the base ring was a field).

With this installed, I've done some playing around with free modules over the ring of integers of Q(sqrt(-7)), and it seems to be quite usable. There are unresolved uniqueness issues, because I don't know how to pick a canonical generator for an ideal or a canonical representative for an element modulo an ideal (even in the particular case of number field orders), but I haven't yet found an example where this is a problem :-)

William: I'm CCing you on this, because you seemed interested in the Smith form stuff. In conjunction with your work at #5882 this will mean we can handle all sorts of new kinds of modules.


---

Comment by cremona created at 2009-06-11 10:41:33

First a remark:  using #6044 (which as of writing has a positive review but has not been closed yet) solves the issue of non-canonical representatives modulo ideals.

    1. Applies fine to 4.0.1 and builds ok.
    2. Tests in sage/rings.number_field pass
    3. Tests in sage/modules pass
    4. tests in sage/matrix pass
    5. I tried some examples and they worked fine.

On the last point it is not much use trying to create random matrices over a number field order OK, since OK.random_element() returns a random integer!  I think that should be changed.


---

Comment by was created at 2009-06-13 09:16:49

> On the last point it is not much use trying to create 
> random matrices over a number field order OK, since OK.random_element() 
> returns a random integer! I think that should be changed. 

That's the second complaint I've heard about this missing functionality just this week!
Definitely this should get implemented.


---

Comment by davidloeffler created at 2009-06-13 10:36:36

I've opened a ticket (#6273).


---

Comment by ncalexan created at 2009-06-13 19:35:59

Resolution: fixed


---

Comment by was created at 2014-08-26 13:02:49

In case anybody looks at this ticket, and is concerned about speed... I just compared a random 4x4 example over the integers of a quadratic field and it took 3/10 of a second.  In comparison, the code wrapped at #13509 was 1000 times faster.  So watch out.
