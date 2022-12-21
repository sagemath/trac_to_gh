# Issue 594: Teach the MAGMA interface how to handle GF(q) conversions

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-09-05 16:27:33

Assignee: was

The attached patch implements conversion to/from MAGMA polynomials over non-prime finite fields.


---

Attachment

Forgot to mention:
* please review carefully, this includes a change to SageObject and FiniteField
* 'make test' passes (didn't try optional because I don't have all optional packages installed)


---

Comment by was created at 2007-09-05 21:34:29

The patch adds a couple of debug print statements, e.g.,

```
  +        print "INPUT",x
```



---

Comment by malb created at 2007-09-05 21:47:28

Replying to [comment:2 was]:
> The patch adds a couple of debug print statements, e.g.,
> {{{
>   +        print "INPUT",x
> }}}

and removes them again in the second patch in the file. `sage -upgrade` committed my unfinished business.


---

Comment by was created at 2007-09-06 17:50:05

Resolution: fixed
