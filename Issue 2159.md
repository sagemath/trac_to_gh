# Issue 2159: Gröbner bases over any field (cont'd)

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2008-02-14 17:25:14

Assignee: malb

This is a followup of {#2111}.

```
R.<x,y> = PolynomialRing(GF(2147483659),order='lex')
I=ideal([x^3-2*y^2,3*x+y^4])
I.dimension()
...
   ? no ring active
   ? `ideal` is undefined
   ? error occurred in STDIN line 170: `ideal sage85=[x + 1431655773*y^4, y^12 + 54*y^2];
sage: I.variety()
...
   ? `2147483659` greater than 2147483647(max. integer representation)
   ? error occurred in STDIN line 172: `ring sage86=2147483659,(x, y),lp;`
   ? expected ring-expression. type 'help ring;'
```



---

Comment by malb created at 2008-09-20 15:52:51

Changing status from new to assigned.


---

Comment by john_perry created at 2009-01-24 10:56:36

patch for dimension() to work in fields of large prime characteristic


---

Attachment

I'll submit a separate patch for variety, hopefully tomorrow.


---

Comment by malb created at 2009-01-24 11:35:54

*Review*
 * the doctest output of `verbose` should be changed to ignore the line numbers:

```
verbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation. 
```

 * `deg_lms` is referenced in a comment but doesn't exist;
 * could you give a reference for the algorithm implemented?


---

Comment by john_perry created at 2009-01-24 18:05:54

Sorry, addressed all the issues you raised now. I was very surprised to learn that I had not cited the algorithm...


---

Attachment


---

Comment by john_perry created at 2009-01-25 03:20:54

`variety` will take quite a bit of work. We should split that into a separate ticket & commit the patch for `dimension`, assuming that passes review.


---

Comment by malb created at 2009-01-25 19:05:28

Changing status from assigned to new.


---

Comment by malb created at 2009-01-25 19:05:28

Changing assignee from malb to john_perry.


---

Comment by malb created at 2009-01-31 18:04:45

positive review for `dimension_mods.2.patch`


---

Comment by malb created at 2009-01-31 18:06:49

The variety stuff is now #5146


---

Comment by mabshoff created at 2009-02-02 02:57:28

Merged dimension_mods.2.patch in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 06:03:55

Merged dimension_mods.2.patch in Sage 3.3.alpha4 and this time also closed the ticket :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 06:03:55

Resolution: fixed
