# Issue 3651: elliptic curves -- bug in L_ratio()

Issue created by migration from https://trac.sagemath.org/ticket/3651

Original creator: cremona

Original creation time: 2008-07-13 19:35:49

Assignee: was

CC:  nbruin@cecm.sfu.ca

Nils Bruin reports:

"I ran into the following problem in sage, and I suspect it might be your code:

```
sage: EllipticCurve([0,0,0,-193^2,0]).sha().an()
[...]
NameError: global name 'misc' is not defined
```

Was this tested at all?"

It's a problem in L_ratio().



---

Attachment

After the attached patch (based on 3.0.4) it works fine:

```
sage: EllipticCurve([0,0,0,-193^2,0]).sha().an()
4
```



---

Comment by mabshoff created at 2008-07-13 19:49:01

See http://groups.google.com/group/sage-devel/t/60a62f8337e4de3a for details.

Cheers,

Michael


---

Comment by wuthrich created at 2008-07-14 10:14:09

Does not work with me, did you mean 
import sage.misc.misc as misc
?


---

Comment by wuthrich created at 2008-07-14 12:14:58

Sorry, my mistake; it works of course.


---

Comment by mabshoff created at 2008-07-16 04:09:51

Taking Chris' remark into account I am giving this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-16 04:24:26

Merged in Sage 3.0.6.alpha0


---

Comment by mabshoff created at 2008-07-16 04:24:26

Resolution: fixed
