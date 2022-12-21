# Issue 6332: optional doctest failure -- jones number field database tests fail

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 15:09:38

Assignee: tbd


```
sage -t -long --optional devel/sage/sage/databases/jones.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/databases/jones.py", line 21:
    sage: [(k.degree(), k.disc()) for k in J.unramified_outside([2])]    # optional - jones_database
Expected:
    [(1, 1), (2, 8), (2, -4), (2, -8), (4, 2048), (4, -1024), (4, 512), (4, -2048), (4, 256), (4, 2048), (4, 2048)]
Got:
    [(4, -2048), (2, 8), (4, -1024), (1, 1), (4, 256), (2, -4), (4, 2048), (4, 512), (4, 2048), (2, -8), (4, 2048)]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/databases/jones.py", line 27:
    sage: [k.disc() for k in J.unramified_outside([2],2)]                # optional - jones_database
Expected nothing
Got:
    [8, -4, -8]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/databases/jones.py", line 34:
    sage: [k.disc() for k in J.ramified_at([3,5],3)]                     # optional - jones_database
Expected nothing
Got:
    [-6075, -6075, -675, -135]
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/databases/jones.py", line 163:
    sage: J.unramified_outside([101,119]) # requires optional package
Expected:
    [Number Field in a with defining polynomial x - 1, Number Field in a with defining polynomial x^2 - 101, Number Field in a with defining polynomial x^4 - x^3 + 13*x^2 - 19*x + 361, Number Field in a with defining polynomial x^5 - x^4 - 40*x^3 - 93*x^2 - 21*x + 17, Number Field in a with defining polynomial x^5 + x^4 - 6*x^3 - x^2 + 18*x + 4, Number Field in a with defining polynomial x^5 + 2*x^4 + 7*x^3 + 4*x^2 + 11*x - 6]
Got:
    [Number Field in a with defining polynomial x^2 - 101, Number Field in a with defining polynomial x^5 + 2*x^4 + 7*x^3 + 4*x^2 + 11*x - 6, Number Field in a with defining polynomial x - 1, Number Field in a with defining polynomial x^5 + x^4 - 6*x^3 - x^2 + 18*x + 4, Number Field in a with defining polynomial x^5 - x^4 - 40*x^3 - 93*x^2 - 21*x + 17, Number Field in a with defining polynomial x^4 - x^3 + 13*x^2 - 19*x + 361]
**********************************************************************
2 items had failures:
   3 of  11 in __main__.example_0
   1 of   4 in __main__.example_2
***Test Failed*** 4 failures.

```



---

Comment by fwclarke created at 2009-06-18 22:08:01

The failures here were caused mainly by `unramified_outside` ordering its output.  Presumably the doctests weren't updated when the ordering was introduced.

Sorting the list of fields is a good idea, but the existing ordering was essentially random.  In the patch I've fixed it so that the fields are ordered primarily by degree and discriminant, and done the same for the other main function `ramified_at`.  The doctests have been adjusted accordingly.

At the same time the opportunity has been taken to tidy up a few things.  In particular I have included a check that the 'primes' are indeed prime.


---

Attachment


---

Attachment

apply after the first patch


---

Comment by AlexGhitza created at 2009-07-17 11:29:17

Looks good.  I've added a small patch replacing various instances of `# requires optional package` with the more precise `# optional - jones_database`.


---

Comment by mvngu created at 2009-07-19 16:38:26

Resolution: fixed


---

Comment by mvngu created at 2009-07-19 16:38:26

Merged both patches. However, I notice that some docstrings in `trac_6332.patch` aren't properly formatted. In particular:

```
164	        -  ``var'' - the name used for the generator of the number fields (default 'a').
203	        -  ``var'' - the name used for the generator of the number fields (default 'a').
246	        -  ``var'' - the name used for the generator of the number fields (default 'a').
```

These results in 3 warnings when building the HTML version of the reference manual. This docstring formatting issue is addressed in #6560.
