# Issue 9055: Moving/cleaning enumeration functions for points on schemes

Issue created by migration from Trac.

Original creator: cturner

Original creation time: 2010-05-26 11:34:42

Assignee: AlexGhitza

CC:  cremona wdj

Keywords: rational points enumeration

I think it would be sensible to move the functions


enum_projective_rational_field


enum_projective_finite_field


enum_affine_rational_field


enum_affine_finite field



from their current position at the top of sage.schemes.generic.homset, and to clean up their code to make it easier to read whilst (I believe) keeping the timing about the same.

I have started work on a patch that does this, putting them into a new file sage.schemes.generic.rational_point and using the cartesian_product_iterator function to make the code much more readable.

This is a preamble to putting other (more efficient) functions that find rational points in specific cases into the same file - I am currently working on this, and will make a separate ticket for it.


---

Comment by cturner created at 2010-05-26 11:35:01

Changing status from new to needs_work.


---

Comment by novoselt created at 2010-05-26 15:17:38

I support the idea of moving these functions - I was a bit surprised to see them when I was going over homset file. And of course nobody should be against making them more readable ;-)


---

Comment by cturner created at 2010-06-08 09:14:49

I have uploaded a patch. It does the following:

1. Moves the functions mentioned to a new file, rational_point
2. Changed enum_projective_rational_field, enum_projective_finite_field, enum_affine_finite_field to be, I hope, more readable, but to run no faster. I have also added a sort at the end.
I did not change enum_affine_rational_field in the end because I couldn't see a simpler way to do it.
3. Added docstrings for these four functions.
4. Changed some doctests for the rational_points function (which use these functions) in the algebraic_scheme file. This is because the old functions returned an unsorted list and the new ones sort before returning, so the ordering has changed but the set of points has not.


---

Comment by cturner created at 2010-06-08 09:14:49

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-06-08 15:05:34

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2010-06-08 15:05:34

I just glanced at the patch, but I have the following comments:

1) "Set of homomorphisms between two schemes" should stay in the original file, it is the docstring of the module describing what does it do.

2) There should be a new description (hopefully, more informative) in the new module. The first line is how this module will be listed in the documentation, the rest can be any text. Also, there should be the copyright/license notice and AUTHORS field in the module docline (stating who has written these functions initially and that you have improved and documented them).

3) There are some doctests with very long output strings. This leads to not very good looking formatting of the documentation. You can insert line breaks in the output and doctests still will run fine. I would suggest doing it to keep line length under 80 (or even 60, excluding leading spaces,) characters.

4) Did you try to compile a documentation with this module? I didn't, but it seems to me that there are quite a few problems with indentations and "::"s. Also, now that you have actually added the docstrings to these functions, it would make sense to include this module into the auto-generated documentation tree.

5) Is there any specific reason for importing these functions in the homset module right before their use? It is my strong belief that all imports should be in the beginning of the file to avoid repetitions and to make it clear what is used by this module.

I think that 1), 2), and 4) are mandatory, while 3) and 5) may reflect my personal taste (although I tried to explain why do I think that they make sense).


---

Comment by cturner created at 2010-06-11 20:15:42

1) I (believe I have) fixed the issues flagged by novoselt. Thank you novoselt for your help in pointing them out.

2) I have improved the code so that it can take either a scheme or an abstract set of rational points of a scheme as input.

THERE IS A KNOWN DOCTEST FAIL with this patch;

The following tests failed:

sage/coding/code_constructions.py
sage/coding/linear_code.py 
sage/coding/decoder.py
doc/en/constructions/linear_codes.rst

I think this is because the coding modules use the enum_projective_finite_field function. This causes the same problem as point 4. of my previous comment (circa 8th June). The new versions of each of these functions sort points but the old ones did not. I suspect that the coding functions depend on the order of the output of enum_projective_finite_field and so fail now that that order has changed. I am not proficient with codes and do not feel able to fix this issue. I wonder if someone who does understand coding could help and fix this? I CC David Joyner, who originally wrote these modules. Perhaps it is simply a matter of adapting the doctests to take into account the new ordering. I believe that this is the right way round; that the ordering of the output of the "enum" functions should not depend on the algorithm used.

Because of this, I suggest that the patch be reviewed ignoring these problems with coding modules, and in the meantime a coding person might be able to help solve the problems.


---

Comment by cturner created at 2010-06-11 20:15:42

Changing status from needs_work to needs_review.


---

Comment by cturner created at 2010-06-15 12:33:49

Both patches (so far!) are based on sage 4.4.3


---

Comment by cturner created at 2010-06-16 15:53:05

We (John Cremona, David Joyner and myself) believe we have identified what needs to be done to fix the issues with the coding modules and we will return to it after sage days 22!


---

Comment by cturner created at 2010-06-16 15:53:05

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2010-07-26 23:18:37

Replying to [comment:7 cturner]:
> We (John Cremona, David Joyner and myself) believe we have identified what 
> needs to be done to fix the issues with the coding modules and we will 
> return to it after sage days 22!

The new attachment (to be applied on top of the previous one) 
seems to fix the problems in the coding thry docstrings.


---

Comment by novoselt created at 2010-11-01 02:04:33

The second patch does not apply cleanly anymore, on sage-4.6.rc0 I am getting

```
applying trac-9055-coding-thry-docstring-fixes.patch
patching file sage/coding/linear_code.py
Hunk #13 FAILED at 2028
```



---

Comment by novoselt created at 2010-11-01 02:35:01

What exactly has happened to the broken doctests? It does not seem to me that the new output is merely a permutation of the old one. 

There are (sometimes) extra spaces in front of the output.

There are some notes/warnings in the documentation and it would be nice if they were formatted according to http://sagemath.org/doc/developer/conventions.html#documentation-strings


---

Comment by rlm created at 2010-12-01 13:07:08

Replying to [comment:10 novoselt]:
> What exactly has happened to the broken doctests? It does not seem to me that the new output is merely a permutation of the old one. 

The ordering of vector spaces over finite fields is used all over the place. In constructing the Hamming codes, etc. I think there is a echelon form involved afterward as well, so it is easy enough to seem like this isn't just a problem with order changing...

The new patch includes all previous ones, and fixes a docstring fix which needed to be rebased.


---

Comment by rlm created at 2010-12-01 13:07:08

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-12-01 13:17:05

I will simply mention for the record that things like

```
        G = self.gen_mat()
        F = self.base_ring()
        q = F.order()
        q0 = F0.order()
        a = log(q,q0)  # test if F/F0 is a field extension
        if not isinstance(a, Integer):
            raise ValueError,"Base field must be an extension of given field %s"%F0
        n = len(G.columns())
        k = len(G.rows())
        G0 = [[x**q0 for x in g.list()] for g in G.rows()]
        G1 = [[x for x in g.list()] for g in G.rows()]
        G2 = G0+G1
        MS = MatrixSpace(F,2*k,n)
        G3 = MS(G2)
        r = G3.rank()
        MS = MatrixSpace(F,r,n)
        Grref = G3.echelon_form()
        G = MS([Grref.row(i) for i in range(r)])
        return LinearCode(G)
```

(`galois_closure` in `linear_code.py`) can be vastly simplified, and probably sped up in the process.

Programming no-nos:
 1. Using logarithms to test whether one finite field is contained in another (why not just check whether the characteristics are the same and if one degree divides the other?).
 1. `G1 = [[x for x in g.list()] for g in G.rows()]` ... Why not `G1 = G.rows()` or at least `G1 = [g.list() for g in G.rows()]` etc.? This is a big waste of time (remember that Python is slow anyway...)
 1. This is also bad:

```
        MS = MatrixSpace(F,2*k,n)
        G3 = MS(G2)
        r = G3.rank()
        MS = MatrixSpace(F,r,n)
        Grref = G3.echelon_form()
        G = MS([Grref.row(i) for i in range(r)])
```

... why not just `G3 = Matrix(F, 2*k, n, G2); G = G3.row_space().basis_matrix()` or the equivalent? It's easier to follow and might be more efficient, too. 

(Not criticisms of code in this ticket at all, for the skimmer -- just an indication that `linear_code.py` needs more work...)


---

Attachment

Apply last


---

Comment by novoselt created at 2010-12-01 17:50:23

I've prettified documentation of the new module and improved exception handling, since there were several blocks like

```
try:
   ...
except:
   pass
```

which potentially can cause strange errors or results. In particular, such a code may be hard to interrupt if it is taking too long.

If someone can go over my patch and approve it, please switch this ticket to positive review. Tests pass.


---

Comment by rlm created at 2010-12-01 20:48:20

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-04 22:50:02

This will likely need to be rebased when sage-4.6.1.alpha3 will be released.


---

Comment by jdemeyer created at 2010-12-04 22:54:24

Changing status from positive_review to needs_work.


---

Attachment

rebased on sage-4.6.1.alpha2 + #6094


---

Comment by rlm created at 2010-12-05 10:41:10

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2011-01-12 06:32:17

Resolution: fixed


---

Comment by vbraun created at 2011-01-19 22:04:24

Depends on #9055


---

Comment by vbraun created at 2011-01-19 22:04:45

Sorry wrong ticket, my bad :(


---

Comment by jdemeyer created at 2011-01-19 22:15:26

Replying to [comment:20 vbraun]:
> Depends on #9055

Interesting, a recursive ticket :-)  Do you want to denial-of-service the patchbot?
