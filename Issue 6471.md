# Issue 6471: clarify differences between c.abs() and c.norm() for complex c

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-07 04:15:30

Assignee: tbd

If `c` is of type `CC`, then `c.abs()` returns the absolute value of a complex number and `c.norm()` returns the norm of a complex number. One problem with this is that the absolute value of a complex number is also referred to as the complex norm. This problem was noticed in IRC:

```
15:32 < greg> the sage command norm() returns the modulus squared of complex
             numbers, is this the desired behavior?
15:44 < mvngu> greg: If c is a complex number (type CC), then c.norm() returns
              the complex norm of c. That is, if c = a + bi then c.norm()
              returns a^2 + b^2.
15:44 < mvngu> Is that what you mean?
15:46 < greg> isn't the complex norm typicaly sqrt(a^2 + b^2)
15:50 < mvngu> greg: That's the absolute value. In that case, use c.abs().
15:53 < mvngu> And I agree that there's various names for this: modulue of
              complex number, absolute value of complex number, complex norm.
15:54 < greg> mvngu: okay thanks
15:54 < mvngu> So it clarifies for you?
15:56 < greg> yeah, I think so.
15:56 < greg> out of curiosity, where is a^2 + b^2 typically used as the norm?
             I'm checking mathworld and wikipedia and my complex analysis
             books and they all use the L2 norm
15:58 < mvngu> You know Gaussian integers?
15:58 < greg> yeah
15:58 < greg> okay i see that
15:58 < greg> cool thanks
15:58 < mvngu> yeah... the norm of a Gaussian integer is defined like that.
15:59 < greg> okay i see
```



---

Attachment

based on Sage 4.1.rc0


---

Comment by mvngu created at 2009-07-07 06:08:01

Changing assignee from tbd to tba.


---

Comment by mvngu created at 2009-07-07 06:08:01

Changing type from defect to enhancement.


---

Comment by mvngu created at 2009-07-07 06:08:01

Changing component from algebra to documentation.


---

Comment by mvngu created at 2009-07-07 06:08:01

Changing keywords from "" to "absolute value, complex norm".


---

Comment by AlexGhitza created at 2009-07-11 09:22:34

Looks good.


---

Comment by cremona created at 2009-07-11 15:30:58

I agree.  Blame the number theorists!  In number theory there are lots of norms with different norm-alizations (joke) which causes a lot of confusion.   In the implementation of local and global heights for number field elements the same issue arose (see #6046, now merged): for complex embeddings there is an issue of whether or not to multiply by 2 (which is the logarithmic equivalent of the current discussion) and I allowed both, with a boolean "weighted" parameter to switch between them.


---

Comment by mvngu created at 2009-07-17 08:21:27

Resolution: fixed
