# Issue 3211: rref function for matrices

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-05-15 13:43:48

Assignee: was

CC:  was kcrisman rbeezer

The rref() function would copy the matrix to a matrix over the field of fractions of its base ring, then return echelon_form() of the new matrix.




---

Comment by was created at 2008-05-15 14:02:44


```
06:40 < jason-> Running an idea past people: an RREF function for matrices which first converts the matrix to be over the field of fractions of its base ring, then 
                returns the echelon form.
06:41 < jason-> Thoughts?
06:41 < jason-> (except, of course, the function would be lower-cased: m.rref() )
06:43 -!- mhampton [n=hampton`@`75-163-23-225.dlth.qwest.net] has quit []
06:56 < wstein> jason- ICK!
06:56 < wstein> Are you serious?
06:56 < jason-> wow, I didn't expect such a huge negative reaction
06:56 < wstein> You are advocating that we have E.echelon_form() with the current behavior, but
06:57 < wstein> E.rref() with completely different behavior?
06:57 < jason-> is that really bad?
06:57 < wstein> Well, yes.
06:57 < wstein> An abreviation must have exactly the same behavior.
06:57 < wstein> Also, the current E.echelon_form() *is* reduced row echelon form.
06:58 < mabshoff> well, #3211 ought to be changed/invalidated then
06:58 < wstein> Yep, I don't like it.
06:58 < jason-> the current echelon_form function was really confusing for some people that are senior people in linear algebra....
06:58 < wstein> People will expect rref = echelon_form.
06:58 < jason-> and undergrad students in linear algebra
06:58 < jason-> because the default ring is ZZ
06:58 < wstein> True.
06:58 < jason-> so matrix(3, range(9))
06:59 < jason-> gives a *much* different rref than any other software or calculator out there.
06:59 < wstein> Not true.
06:59 < wstein> It gives exactly the same answer as the *only* other program out there that has a notion of "matrix over ZZ".
06:59 < wstein> Namely Magma.
07:00 < jason-> okay, except magma?
07:00 < jason-> sure.
07:00 < jason-> most of these people don't know about magma/can't afford to run magma, etc.
07:00 < jason-> (especially the undergrad students)
07:00 < jason-> is there a way we could have a function that returns the echelon_form over the fraction field?
07:00 < wstein> One option is that the implicit choice of base ring for  matrix(...) would be QQ instead of ZZ.
07:00 < jason-> That would be really nice.
07:00 < jason-> I was afraid of suggesting that, though
07:01 < jason-> for fear that too much stuff would break
07:01 < wstein> But if one explicitly writes matrix(ZZ,...) then it's over ZZ.
07:01 < jason-> I would support the implicit choice being over QQ
07:01 < wstein> I think most anything where the ZZ really matters is explicit.
07:01 < jason-> Do you want me to make that change, then?
07:01 < wstein> Can you suggest it on sage-devel?
07:01 < jason-> That way, if someone *knows* what they want, they can explicitly say over ZZ
07:01 < wstein> Yep.
07:02 < wstein> Could you suggest it on sage-devel.
07:02 < jason-> otherwise it's more what people generally expect
07:02 < jason-> yes.
07:02 < wstein> I don't make changes like this (or like your #3211) by dictatorship.
07:02 < jason-> and I'll hold off on the dubious rref function
```



---

Comment by was created at 2008-05-15 14:03:59


```
07:03 < wstein> If you do implicit QQ instead of ZZ you *have* to do implicit QQ(x) instead of QQ[x], by the way.
07:03 < wstein> I.e., if Frac(R) is defined, it has to be used.
07:03 < wstein> Otherwise matrix(...) will be to weird.
```



---

Comment by jason created at 2008-05-15 14:25:54

See http://groups.google.com/group/sage-devel/browse_thread/thread/6ca33dd59ef09bd4 , which probably should have been more properly titled "Changing it so that matrix() returns a matrix over a field, unless the ring is specified"


---

Comment by jason created at 2008-05-21 15:46:30

The conclusion from the thread from William was:


```
I think based on this whole discussion:

(1) matrix(3, range(9)) returning a matrix over QQ is *definitely* out.
If there is a trac ticket it should be marked invalid.

(2) The echelon_form command should be changed to always return
a result over the fraction field, thus making a break with Magma.

(3) Rewrite all the rest of code in Sage that depends on the current
behavior of echelon_form.  This code will have to call hermite_form
instead.  E.g., code in modules/free_module.py will have to change.
Code in a.kernel() will have to change, etc.

Doing (1), (2) is almost trivial.  Do (3) will be a little more difficult, and
could introduce bugs.

I'm very much against
   a.echelon_form(...)
being over ZZ or QQ depending on arguments to echelon_form.
If for no other reason than even if one does that then it will
still be necessary to do all of (3) above.

I've cc'd David Kohel on this email, since he is 100% responsible
for the current state of affairs regarding echelon form, and I want
to give him a chance to speak up before we do (1)-(3) above.
```



---

Comment by jason created at 2008-05-23 16:39:55

This ticket has now morphed into doing:

Rename echelon_form to hermite_form, and make a 
new echelon_form function that computes hermite_form over the fraction field of the base ring.

Rewrite all the rest of code in Sage that depends on the current
behavior of echelon_form.  This code will have to call hermite_form
instead.  E.g., code in modules/free_module.py will have to change.
Code in a.kernel() will have to change, etc.


---

Comment by jason created at 2008-12-06 07:26:32

Changing status from new to assigned.


---

Comment by jason created at 2008-12-06 07:26:32

Changing assignee from was to jason.


---

Comment by jason created at 2009-09-19 03:28:54

See #5014 for one issue which could be solved by this ticket.


---

Comment by robertwb created at 2009-09-22 04:37:58

More discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/5f247122fce6a129/cf753d838b969b8c , this is still considered a good idea.


---

Comment by jason created at 2009-09-22 04:59:31

Also, I've been working (yet again) on a patch...


---

Attachment

unfinished


---

Comment by jason created at 2009-10-01 08:08:21

I'm attaching the work-in-progress so that it's archived somewhere other than my computer.


---

Attachment

apply instead of previous patch.


---

Comment by jason created at 2009-12-03 14:07:47

apply on top of previous patch


---

Attachment


---

Comment by jason created at 2009-12-03 14:08:45

The previous two patches are a *rough draft* of a patch.  I had them applied to sage-4.1.2.alpha2.


---

Comment by jason created at 2010-01-19 18:55:06

apply instead of previous patches


---

Attachment

Okay, I've posted a single rebased patch which applies on top of 4.3.1.rc1.


---

Comment by kcrisman created at 2010-01-19 19:22:46

I realize this isn't ready for review yet, but at the very least we would want to put in a DeprecationWarning for the missing echelon_form etc. methods :)  How hard will it be to make echelon_form = hermite_form(quotient field)?


---

Comment by mvngu created at 2010-03-02 21:55:51

Close as fixed by #8008.


---

Comment by mvngu created at 2010-03-02 21:55:51

Resolution: fixed
