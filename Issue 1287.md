# Issue 1287: [with patch] wrappers for Dokchitser L-series

Issue created by migration from https://trac.sagemath.org/ticket/1287

Original creator: jen

Original creation time: 2007-11-27 04:17:26

Assignee: was

Wrappers for Dokchitser L-series for various types of modular forms, e.g.,:


```
        sage: L = delta_Lseries()
        sage: L(1)
        0.0374412812685155

        sage: f = CuspForms(2,8).0
        sage: L = f.cuspform_Lseries()
        sage: L(1)
        0.0884317737041015
        sage: L(0.5)
        0.0296568512531983

        sage: f = ModularForms(1,4).0
        sage: L = f.modform_Lseries()
        sage: L(1)
        -0.0304484570583933

        sage: L = eisenstein_series_Lseries(20)
        sage: L(2)
        -5.02355351645987 
```



---

Attachment


---

Comment by was created at 2007-12-02 06:35:23

Unfortunately there is a bug somewhere or some sort of mathematical contradiction going on here, as the following calculation illustrates:


```
sage: M = ModularSymbols(1,12)
sage: d = M.cuspidal_submodule().rational_period_mapping()
sage: for i in range(11):
...      print i, d(M.modular_symbol((i, 0,oo)))
0 (1620/691, 0)
1 (0, 1)
2 (-1, 0)
3 (0, -25/48)
4 (9/14, 0)
5 (0, 5/12)
6 (-9/14, 0)
7 (0, -25/48)
8 (1, 0)
9 (0, 1)
10 (-1620/691, 0)
sage: L = eisenstein_series_Lseries(12)
sage: L(3)
2.89830333000000e-17
sage: L(5)
7.35601685000000e-17
```


The modular symbols calculation verifies that L(i) for odd integers i=3,5, etc. is nonzero.  This also agrees with the Riemann Hypothesis for L(Delta, s).  However, for some strange reason the Dokchitser L that you're computing is 0 at some odd integers.  This means there is something wrong. 

I haven't figured out what yet.  I'll let Jen see if she can.

This can't go in sage as is though.


---

Comment by was created at 2007-12-02 18:29:21

*Doh* -- I was being stupid / confused between Eisenstein series and cusp form, since it was a long day.

Change this to a positive review!


---

Comment by mabshoff created at 2007-12-02 19:04:35

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 19:04:35

Resolution: fixed
