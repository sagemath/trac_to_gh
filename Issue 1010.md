# Issue 1010: upgrade gfan to version 0.3

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-27 05:38:02

Assignee: was


```
Dear Mike and William,

I am writing this email to let you know about the changes in the new
Gfan version 0.3.
Unfortunately the improvements to Gfan introduce some compatibility
problems, but hopefully we will have less of these problems in the future.
You may simply ignore this mail if you are not interested in
compatibility issues now.

Some of the changes are good:
---------------------------------------
The user now has the option to be very specific about what polynomial
ring the computations should take place in. The first line of the input
can now be a polynomial ring. For example
Q[x,y,t1,t2]
or
Z/7Z[a]
This change breaks compatibility in the following two ways:
1) the output now typically contains the polynomial ring in its first
line!!!!!
2) the --modp option has been removed.

Changes that affect how commands are logically combined:
---------------------------------------------------------------------------
The major change is that when Gfan outputs polyhedral data it is done in
a Polymake compatible way. Thus the output is a Polymake file typically
describing a polyhedral fan. Notice that the there is no official
Polyhedral fan format in Polymake at the moment. The only other software
that uses this format is TrIm by Josephine Yu.
Working with polyhedral fans turns out to be much nicer when there is an
appropriate format.

Here are two examples:
1) To compute a  Groebner cone from a marked reduced Groebner basis in
the old Gfan one would use gfan_groebnercone | gfan_facets , where
gfan_groebner cone computes inequalities and gfan_facets removes
redundant ones. In the new version the output of gfan_groebnercone is
either a polyhedral cone or its face complex as a the polyhedral fan. In
the first case the facets can be read off directly from the output.
2) To compute a weight vector for a reduced Groebner basis in the old
Gfan one would use gfan_weightvector . Now this is simply done by
gfan_groebnercone .

I don't know to what extend the above changes will affect your interfaces.
I guess I could have kept Gfan backward compatible but that would have
meant that more ugly code would have to be maintained.
I am pretty satisfied with the input/output format now.
If you wish to adjust your interfaces to Gfan and need help please let
me know.

Best regards,
```



---

Comment by mhampton created at 2008-02-27 19:15:13

Changing assignee from was to mhampton.


---

Comment by mhampton created at 2008-02-27 19:15:13

I'll try to do this.


---

Comment by mhampton created at 2008-02-29 10:27:10

A preliminary spkg for gfan-0.3 can be found at:

http://www.d.umn.edu/~mhampton/gfan-0.3.p1.spkg

Its not ready for inclusion yet though.  I did not provide the debian package information, since I have no idea how to do that yet.  This compiles OK on OS X, 10.4.11, but should be tested on other platforms. 

I have not rewritten the interface to deal with Anders' changes in output, that is my next goal.


---

Comment by mhampton created at 2008-02-29 10:27:10

Changing priority from major to minor.


---

Comment by cwitty created at 2008-03-14 02:08:13

The spkg compiles and installes on my 32 bit x86 Debian testing box.  (I don't know how to test it, so I didn't do any tests.)

The spkg does have some OSX junk (.DS_Store, etc.)


---

Comment by mhampton created at 2008-03-19 15:39:08

Changing assignee from mhampton to mabshoff.


---

Attachment

I tried to remove the OS X junk referred to by cwitty.  I am also attaching a patch for sage/interfaces/gfan.py and sage/rings/polynomial/groebner_fan.py.  Some functionality has changed, some has been added: most notably the tropical intersection command and changes to the render method so that it uses Sage graphics.  Things remain to be done, but this now passes tests with gfan-0.3 and I am happy to respond to review comments.


---

Comment by mhampton created at 2008-03-19 15:43:04

Updated spkg is at:

http://www.d.umn.edu/~mhampton/gfan-0.3.p2.spkg


---

Comment by cwitty created at 2008-03-21 01:18:45

The new spkg compiled and installed fine for me (it does still have two .DS_Store files, though).  With the above patch, tests pass in interfaces/gfan.py and rings/polynomial/groebner_fan.py .

This is 32-bit x86 Debian testing.

I'm not marking this as a positive review because I haven't read the patch (and don't plan to).


---

Comment by malb created at 2008-03-21 14:57:21

The spkg installs fine in my 2.10.4 on Debian/testing AMD64. The patch applies cleanly. doctests pass for `sage.rings.polynomial.*`. 

*SPKG:*
 * Michael volunteered to take a deeper look
 * Carl reported the redundant `.DS_Store` files

*Patch*
 * I haven't read the patch yet but I'm planing to so during Easter break.
 * I'm happy if somebody beats me to a review but I'll definitely have something in a couple of days.
 * Sorry for the delay.


---

Comment by malb created at 2008-03-21 15:03:53

Some quick remarks:
 * not all new methods/classes/functions have documentation and doctests
 * "MH: I think this is now irrelevant since gfan can accept the original ring variables" shouldn't that not just be checked to be sure?
 * "Rewrote various functions to use gfan-0.3. This is still a work in progress, comments are appreciated on trac (ticket 1010) or sage-devel`@`googlegroups.com (or personally at hamptontio`@`gmail.com)." please don't refer to the ticket, it will be closed (hopefully) soon.


---

Comment by malb created at 2008-03-22 14:30:11

Some more comments (some repetitions):
 * "MH: I think this is now irrelevant" check this and remove the comment if appropriate 
 * please drop the reference to ticket 1010, it will be closed hopefully soon
 * shouldn't `PolyhedralCone._repr_` be more specific about the object?
 * `PolyhedralCone` is undocumented
 * `PolyhedralFan` is almost undocumented
 * shouldn't `PolyhedralFan._repr_` be more specific about the object?
 * "#should fix this so it handles allowed finite fields", we used to support these, so it shouldn't be dropped
 * render talks about xfig but outputs a png
 * it might be a good ideal to compute the Gröbner basis using Singular by default rather than leaving that to GFan. I bet it is much faster than GFan, but that could be another ticket.
 * btw. the docstring of Ideal.groebner_fan is pretty useless:

```  
  "symmetry -- default: None; if not None, describes symmetries of the ideal"
}}} 
  how is the symmetry described?


---

Attachment


---

Comment by mhampton created at 2008-03-25 02:02:12

The attached patch addresses most of the comments.  Using Singular would be a big project, I will bring it up with Anders Jensen (author of gfan).  I have not fixed the docstring of Ideal.groebner_fan regarding symmetry; that needs some more work but it wasn't well implemented before anyway so I am not breaking anything that worked before, and this patch adds a lot of functionality.


---

Comment by malb created at 2008-03-25 13:39:40

Replying to [comment:12 mhampton]:
> The attached patch addresses most of the comments.  Using Singular would be a big project, I will bring it up with Anders Jensen (author of gfan). 

Hi, sorry for not being precise about this. `MPolynomialIdeal.groebner_fan` has this signature:


```
def groebner_fan(self, is_groebner_basis=False, symmetry=None, verbose=False)
```


My proposal was to replace `is_groebner_basis` either by calling `I.basis_is_groebner` or by simply computing the Gröbner basis is Sage before passing the generators to GFan. Also `verbose` should be replace with a `get_verbose` call. 

In any case, this is directly related to this ticket (sorry for going OT) and I'll review the new patch soon-ish if noone beats me to it.


---

Attachment


---

Attachment


---

Attachment

Review of the `post_review` patch:
 * The docstrings don't obey Sage's style conventions (indentation
   etc.), I've attached a patch for that (`gfan_docstyle.patch`).
 * man newly introduced methods/functions still don't have any
   documentation and no doctests. Sage now has a
   nothing-new-without-doctests policy, so this needs to be addressed
   before this can go in.
 * I've also attached `coverage_before.txt` and `coverage_after.txt`
   with coverage information before and after the patch was applied.
 * I'm not sure if this is related to the rewrite:

```
sage: P = PolynomialRing(GF(127),10,'x')
sage: I = sage.rings.ideal.FieldIdeal(P)
sage: gf = I.groebner_fan()
sage: gb = gf.reduced_groebner_bases()
[This is the Trac macro *x9^127 - x9, x8^127 - x8, x7^127 - x7, x6^127 - x6, x5^127 - x5, x4^127 - x4, x3^127 - x3, x2^127 - x2, x1^127 - x1, x0^127 - x0* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#x9^127 - x9, x8^127 - x8, x7^127 - x7, x6^127 - x6, x5^127 - x5, x4^127 - x4, x3^127 - x3, x2^127 - x2, x1^127 - x1, x0^127 - x0-macro)

sage: P = PolynomialRing(GF(127),11,'x')
sage: I = sage.rings.ideal.FieldIdeal(P)
sage: gf = I.groebner_fan()
sage: gf.reduced_groebner_bases()
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)
...
<type 'exceptions.RuntimeError'>: gfan: parser.cpp:405: PolynomialSet CharacterBasedParser::parsePolynomialSet(const PolynomialRing&): Assertion `isRightBracket(c)' failed.
```

 * Also, some methods do have examples but no explanation what they do. IMHO this should be addressed too.


---

Comment by mhampton created at 2008-03-27 02:58:19

patch against 2.10.4 addressing almost all review comments


---

Attachment

The latest patch addresses almost all of the review comments.  Coverage is now 100%; the doctest on the "interactive" command is bogus because of the nature of the command.  Documentation and doctests should conform to Sage's style conventions - (btw where is this laid out precisely?).  More explanation has been added, although I'm sure more could be, but I feel that really anyone interested should read the gfan manual and maybe even Anders Jensen's thesis if they want serious explanation. 

I have also addressed the bug pointed out by Martin - this arises because gfan cannot handle variables whose names are prefixes of other variables, and the variables names are not remapped anymore.  So I raise an explicit error and explanation for that case.  This could be fixed, but I think it is acceptable for the moment.  

I have working prototype code for 3D rendering of Groebner fans, but I would like this work included in Sage as soon as possible, and then I will prepare another enhancement ticket, probably for Sage-3.0.


---

Comment by malb created at 2008-03-27 13:57:38

some (whitespace) improvements for the docstrings in groebner_fan.py


---

Attachment

*Review of `trac_1010_post_review_2.patch`*:
 * as said before almost all concerns were addressed and also the coverage was raised to 100% (more than could be asked for)
 * I've got one doctest failure in `sage -t  devel/doc-main/tut/tut.tex`. It wasn't immediately clear to me how to fix this:

```
File "tut.py", line 2362:
    : F.fvector()
Exception raised:
    Traceback (most recent call last):
      File "/usr/local/sage-2.10.3.rc2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_103[4]>", line 1, in <module>
        F.fvector()###line 2362:
    : F.fvector()
    AttributeError: 'GroebnerFan' object has no attribute 'fvector'
```

 * I've attached a tiny patch which adds a reference to the GFan website and some trivial whitespace changes (if the author doesn't like it, it can be left out)
 * Once the `tut.tex` doctest passed (and there is word on whether my proposed fixes shall go in) I'd happily give it a positive review.
 * *Good job mhampton*!


---

Comment by mabshoff created at 2008-03-28 08:50:17

Yeah, I agree with malb that this is a great job. But can somebody please delete all the no longer applicable patches? This ticket is getting really messy.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 08:53:53

I guess fixing the doctest failure in tut.tex might be as simple as the rename:

```
345	 	    def fvector(self): 
 	697	    def polyhedralfan(self): 
```

In case this is it I will merge the updated gfan.spkg and the associated patches in 2.11.alpha2. :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 09:26:51

ok, here we go. The updated spkg at

http://sage.math.washington.edu/home/mabshoff/SPKG/gfan-0.3.p3.spkg

fixes various issues:
 * put the missing .hgignore back in
 * cleaned up the SPKG.txt
 * checked in missing changes
 * removed missed .DS_store in the dist directory

It builds fine on OSX and Linux.

One more thing: src is supposed to be a vanilla distribution of the original source tarball. So gfan-0.3.p4.spkg ought to fix that. But we can do that on a follow up ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 10:10:29

This might be totally wrong, but we will see :)


---

Attachment

Merged trac_1010_post_review_2.patch, gfan_docstrings.patch and trac_1010-tut.tex-doctest-fix.patch in Sage 2.11.alpha0. There are two potential issues left to fix:
 
 * What happened to fvector? polyhedralfan certainly has nothing to do with fvector - it just happens to be in the former location of fvector.
 * a clean Makefile in src in the gfan.spkg

Both the issues should be addressed in follow up tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 10:13:49

Resolution: fixed
