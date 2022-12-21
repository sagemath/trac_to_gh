# Issue 2126: [with patch, needs review] small fixes to eisenstein_series_qexp()

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-02-09 09:41:48

Assignee: AlexGhitza

The attached patch fixes a small typo and adds a small clarification to the docstring (specifying which normalization of the Eisenstein series is returned).



---

Comment by robertwb created at 2008-02-14 06:30:11

The last line should probably read


```
raise ValueError, "-(2*k)/B_k (=%s) must be invertible in the %r"%(a0inv, K) 
```


rather than


```
raise ValueError, "-(2*k)/B_k (=%s) must be invertible in the %s"%(a0inv, K._repr_()) 
```


Other than that, I approve.


---

Attachment

I've incorporated Robert's suggested change and resubmitted the patch.


---

Comment by mabshoff created at 2008-02-17 21:28:03

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 21:28:03

Merged in Sage 2.10.2.alpha1
