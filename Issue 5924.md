# Issue 5924: Proposed new method for the OverconvergentModularForms class

Issue created by migration from https://trac.sagemath.org/ticket/5924

Original creator: ljpk

Original creation time: 2009-04-28 22:55:05

Assignee: craigcitro

I would like to propose the addition of a method which will give the slopes of the U_p operator acting on a space of overconvergent modular forms. Here is my suggested code:

```
 def slopes(self, n, use_recurrence=False):
        r"""
        Compute the slopes of the `U_p` operator acting on self, using an n x n matrix.

        EXAMPLES::
             sage: OverconvergentModularForms(5,2,1/3,base_ring=Qp(5),prec=100).slopes(5)
             [0, 2, 5, 6, 9]
             sage: sage: OverconvergentModularForms(2,1,1/3,char=DirichletGroup(4,QQ).0)
             [0, 2, 4, 6, 8]
        """ 
        if self.base_ring() == QQ:
             slopelist=self.cps_u(n).truncate().newton_slopes(self.prime())
        elif is_pAdicField(self.base_ring()):
             slopelist=self.cps_u(n).truncate().newton_slopes()
        else:
             print "slopes are only defined for base field QQ or a p-adic field"
        return [-i for i in slopelist]
```



---

Comment by davidloeffler created at 2009-05-01 08:02:31

Changing assignee from craigcitro to davidloeffler.


---

Comment by davidloeffler created at 2009-05-01 08:02:31

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-05-01 11:13:28

patch against 3.4.2.rc0


---

Attachment

Positive review. The above code works fine for me (modulo a tiny typo fix), so I've made a proper patch for it. Note that although this has my mercurial username on the patch, credit should go to Lloyd.


---

Comment by mabshoff created at 2009-05-07 23:57:15

Lloyd,

next time you open a ticket please use a descriptive summary. "Proposed new methord ..." is next to useless ;)

Cheers,

Michael


---

Comment by davidloeffler created at 2009-05-08 07:27:03

Lloyd's summary is a little mysterious, but there was already functionality for computing the U_p operator -- that's what the entire overconvergent forms class is there for -- it was just an easy shortcut to access the list of slopes that was missing.


---

Comment by mabshoff created at 2009-05-12 22:15:26

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 22:15:26

Resolution: fixed
