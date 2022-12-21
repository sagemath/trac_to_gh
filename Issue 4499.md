# Issue 4499: Fix latex for sech and csch

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-11-12 01:16:42

Assignee: cwitty

Currently, we have


```
sage: latex(sech)
\sech
sage: latex(csch)
\csch
```


Apparently \sech and \csch are not recognized in LaTeX.  These should be


```
sage: latex(sech)
\text{sech}
sage: latex(csch)
\text{csch}
```



---

Comment by mhansen created at 2008-11-12 01:25:57

Changing assignee from cwitty to mhansen.


---

Attachment


---

Comment by mhansen created at 2008-11-12 01:25:57

Changing status from new to assigned.


---

Comment by mvngu created at 2008-11-12 03:07:27

I'm using sage-3.1.4 here, so I can't say anything about applying this patch against the latest alpha release of sage-3.2. Perhaps other folks can review the patch using the latest alpha release. Before applying the patch *trac_4499.patch* against sage-3.1.4, we'd get these:

```
sage: # sech and arcsech
sage: sech._latex_()
'\\sech'
sage: asech._latex_()
'\\sech^{-1}'
sage: arcsech._latex_()
'\\sech^{-1}'
sage: latex(sech)
\sech
sage: latex(asech)
\sech^{-1}
sage: latex(arcsech)
\sech^{-1}
sage:
sage: # csch and arccsch
sage: csch._latex_()
'\\csch'
sage: acsch._latex_()
'\\csch^{-1}'
sage: arccsch._latex_()
'\\csch^{-1}'
sage: latex(csch)
\csch
sage: latex(acsch)
\csch^{-1}
sage: latex(arccsch)
\csch^{-1}
```

As far as I know, the returned LaTeX strings would cause tex-live to go berserk and complain about "Undefined control sequence" even if we compile with or without the macro `\usepackage{amsmath,amssymb,amsthm`} in the preamble of a .tex file.



After applying the patch against sage-3.1.4, we get these:

```
sage: # sech and arcsech
sage: sech._latex_()
'\\text{sech}'
sage: asech._latex_()
'\\text{sech}^{-1}'
sage: arcsech._latex_()
'\\text{sech}^{-1}'
sage: latex(sech)
\text{sech}
sage: latex(asech)
\text{sech}^{-1}
sage: latex(arcsech)
\text{sech}^{-1}
sage: 
sage: # csch and arccsch
sage: csch._latex_()
'\\text{csch}'
sage: acsch._latex_()
'\\text{csch}^{-1}'
sage: arccsch._latex_()
'\\text{csch}^{-1}'
sage: 
sage: latex(csch)
\text{csch}
sage: latex(acsch)
\text{csch}^{-1}
sage: latex(arccsch)
\text{csch}^{-1}
```

The returned LaTeX strings now look reasonable to me and work as expected when embedded within math mode and using the macro `\usepackage{amsmath`}.


---

Comment by was created at 2008-11-12 17:16:43

Looks good to me too.


---

Comment by aginiewicz created at 2008-11-13 10:48:40

From pure LaTeX typesetting point of view I would except operators to be consistent with standard operators, that's something like ` \mathop {\operator`@`font csch}\nolimits ` instead of ` \text{csch} `, when paper/book is in last stages it might be useful to alter behaviour of `\operator`@`font` for example (that's used in all `\sin`, `\cos`, etc...) and then `\text` might be standing out, anyway the `\text` workaround seems to work if no style changes are applied


---

Comment by mabshoff created at 2008-11-14 03:30:33

Resolution: fixed


---

Comment by mabshoff created at 2008-11-14 03:30:33

Merged in Sage 3.1.rc1


---

Comment by mabshoff created at 2008-11-15 08:41:25

This should be 3.2.rc1
