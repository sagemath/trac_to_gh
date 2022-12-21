# Issue 2196: Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-02-17 19:09:35

Assignee: was

The code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.

Note that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.

The patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).


---

Attachment


---

Comment by ncalexan created at 2008-02-17 19:24:55

There are some typos.  Lines 964 and 965 don't line up, and line 968 should say "Sextic twist".


```
	963	 
956	964	        if self.j_invariant() !=K(0): 
957	965	            raise ValueError, "Sextic twist not defined when j!=1728" 
 	966	 
 	967	        if D.is_zero(): 
 	968	            raise ValueError, "quartic twist requires a nonzero argument" 
```



---

Attachment

to be applied after 8313.patch


---

Comment by cremona created at 2008-02-17 20:22:01

Patch 8314.patch fixes the typo and improved docstrings, but I could not see the non-lining up of lines.


---

Comment by ncalexan created at 2008-02-17 20:29:39

This should be applied.  What I meant by 'not line up' was that they are incongruous:

```
if self.j_invariant() !=K(0): raise ValueError, "Sextic twist not defined when j!=1728"
```

The test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix?


---

Attachment

and finally....


---

Comment by cremona created at 2008-02-17 20:36:02

Replying to [comment:4 ncalexan]:
> This should be applied.  What I meant by 'not line up' was that they are incongruous:
> {{{
> if self.j_invariant() !=K(0): raise ValueError, "Sextic twist not defined when j!=1728"
> }}}
> The test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix? 

 You are quite right, the error message should have had 0 instead of 1728.  Patch 8315.patch fizes that.  Sorry.


---

Comment by ncalexan created at 2008-02-17 20:54:47

Apply every patch.


---

Comment by mabshoff created at 2008-02-17 20:59:05

Merged 8313.patch, 8314.patch and 8315.patch in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-17 20:59:05

Resolution: fixed
