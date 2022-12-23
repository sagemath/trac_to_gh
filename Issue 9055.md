# Issue 9055: Moving/cleaning enumeration functions for points on schemes

archive/issues_009055.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  cremona wdj\n\nKeywords: rational points enumeration\n\nI think it would be sensible to move the functions\n\n\nenum_projective_rational_field\n\n\nenum_projective_finite_field\n\n\nenum_affine_rational_field\n\n\nenum_affine_finite field\n\n\n\nfrom their current position at the top of sage.schemes.generic.homset, and to clean up their code to make it easier to read whilst (I believe) keeping the timing about the same.\n\nI have started work on a patch that does this, putting them into a new file sage.schemes.generic.rational_point and using the cartesian_product_iterator function to make the code much more readable.\n\nThis is a preamble to putting other (more efficient) functions that find rational points in specific cases into the same file - I am currently working on this, and will make a separate ticket for it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9055\n\n",
    "created_at": "2010-05-26T11:34:42Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "title": "Moving/cleaning enumeration functions for points on schemes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9055",
    "user": "cturner"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9055





---

archive/issue_comments_083981.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-26T11:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83981",
    "user": "cturner"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_083982.json:
```json
{
    "body": "I support the idea of moving these functions - I was a bit surprised to see them when I was going over homset file. And of course nobody should be against making them more readable ;-)",
    "created_at": "2010-05-26T15:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83982",
    "user": "novoselt"
}
```

I support the idea of moving these functions - I was a bit surprised to see them when I was going over homset file. And of course nobody should be against making them more readable ;-)



---

archive/issue_comments_083983.json:
```json
{
    "body": "I have uploaded a patch. It does the following:\n\n1. Moves the functions mentioned to a new file, rational_point\n2. Changed enum_projective_rational_field, enum_projective_finite_field, enum_affine_finite_field to be, I hope, more readable, but to run no faster. I have also added a sort at the end.\nI did not change enum_affine_rational_field in the end because I couldn't see a simpler way to do it.\n3. Added docstrings for these four functions.\n4. Changed some doctests for the rational_points function (which use these functions) in the algebraic_scheme file. This is because the old functions returned an unsorted list and the new ones sort before returning, so the ordering has changed but the set of points has not.",
    "created_at": "2010-06-08T09:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83983",
    "user": "cturner"
}
```

I have uploaded a patch. It does the following:

1. Moves the functions mentioned to a new file, rational_point
2. Changed enum_projective_rational_field, enum_projective_finite_field, enum_affine_finite_field to be, I hope, more readable, but to run no faster. I have also added a sort at the end.
I did not change enum_affine_rational_field in the end because I couldn't see a simpler way to do it.
3. Added docstrings for these four functions.
4. Changed some doctests for the rational_points function (which use these functions) in the algebraic_scheme file. This is because the old functions returned an unsorted list and the new ones sort before returning, so the ordering has changed but the set of points has not.



---

archive/issue_comments_083984.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-08T09:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83984",
    "user": "cturner"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083985.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-08T15:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83985",
    "user": "novoselt"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083986.json:
```json
{
    "body": "I just glanced at the patch, but I have the following comments:\n\n1) \"Set of homomorphisms between two schemes\" should stay in the original file, it is the docstring of the module describing what does it do.\n\n2) There should be a new description (hopefully, more informative) in the new module. The first line is how this module will be listed in the documentation, the rest can be any text. Also, there should be the copyright/license notice and AUTHORS field in the module docline (stating who has written these functions initially and that you have improved and documented them).\n\n3) There are some doctests with very long output strings. This leads to not very good looking formatting of the documentation. You can insert line breaks in the output and doctests still will run fine. I would suggest doing it to keep line length under 80 (or even 60, excluding leading spaces,) characters.\n\n4) Did you try to compile a documentation with this module? I didn't, but it seems to me that there are quite a few problems with indentations and \"::\"s. Also, now that you have actually added the docstrings to these functions, it would make sense to include this module into the auto-generated documentation tree.\n\n5) Is there any specific reason for importing these functions in the homset module right before their use? It is my strong belief that all imports should be in the beginning of the file to avoid repetitions and to make it clear what is used by this module.\n\nI think that 1), 2), and 4) are mandatory, while 3) and 5) may reflect my personal taste (although I tried to explain why do I think that they make sense).",
    "created_at": "2010-06-08T15:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83986",
    "user": "novoselt"
}
```

I just glanced at the patch, but I have the following comments:

1) "Set of homomorphisms between two schemes" should stay in the original file, it is the docstring of the module describing what does it do.

2) There should be a new description (hopefully, more informative) in the new module. The first line is how this module will be listed in the documentation, the rest can be any text. Also, there should be the copyright/license notice and AUTHORS field in the module docline (stating who has written these functions initially and that you have improved and documented them).

3) There are some doctests with very long output strings. This leads to not very good looking formatting of the documentation. You can insert line breaks in the output and doctests still will run fine. I would suggest doing it to keep line length under 80 (or even 60, excluding leading spaces,) characters.

4) Did you try to compile a documentation with this module? I didn't, but it seems to me that there are quite a few problems with indentations and "::"s. Also, now that you have actually added the docstrings to these functions, it would make sense to include this module into the auto-generated documentation tree.

5) Is there any specific reason for importing these functions in the homset module right before their use? It is my strong belief that all imports should be in the beginning of the file to avoid repetitions and to make it clear what is used by this module.

I think that 1), 2), and 4) are mandatory, while 3) and 5) may reflect my personal taste (although I tried to explain why do I think that they make sense).



---

archive/issue_comments_083987.json:
```json
{
    "body": "1) I (believe I have) fixed the issues flagged by novoselt. Thank you novoselt for your help in pointing them out.\n\n2) I have improved the code so that it can take either a scheme or an abstract set of rational points of a scheme as input.\n\nTHERE IS A KNOWN DOCTEST FAIL with this patch;\n\nThe following tests failed:\n\nsage/coding/code_constructions.py\nsage/coding/linear_code.py \nsage/coding/decoder.py\ndoc/en/constructions/linear_codes.rst\n\nI think this is because the coding modules use the enum_projective_finite_field function. This causes the same problem as point 4. of my previous comment (circa 8th June). The new versions of each of these functions sort points but the old ones did not. I suspect that the coding functions depend on the order of the output of enum_projective_finite_field and so fail now that that order has changed. I am not proficient with codes and do not feel able to fix this issue. I wonder if someone who does understand coding could help and fix this? I CC David Joyner, who originally wrote these modules. Perhaps it is simply a matter of adapting the doctests to take into account the new ordering. I believe that this is the right way round; that the ordering of the output of the \"enum\" functions should not depend on the algorithm used.\n\nBecause of this, I suggest that the patch be reviewed ignoring these problems with coding modules, and in the meantime a coding person might be able to help solve the problems.",
    "created_at": "2010-06-11T20:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83987",
    "user": "cturner"
}
```

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

archive/issue_comments_083988.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-11T20:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83988",
    "user": "cturner"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083989.json:
```json
{
    "body": "Both patches (so far!) are based on sage 4.4.3",
    "created_at": "2010-06-15T12:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83989",
    "user": "cturner"
}
```

Both patches (so far!) are based on sage 4.4.3



---

archive/issue_comments_083990.json:
```json
{
    "body": "We (John Cremona, David Joyner and myself) believe we have identified what needs to be done to fix the issues with the coding modules and we will return to it after sage days 22!",
    "created_at": "2010-06-16T15:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83990",
    "user": "cturner"
}
```

We (John Cremona, David Joyner and myself) believe we have identified what needs to be done to fix the issues with the coding modules and we will return to it after sage days 22!



---

archive/issue_comments_083991.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-16T15:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83991",
    "user": "cturner"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083992.json:
```json
{
    "body": "Replying to [comment:7 cturner]:\n> We (John Cremona, David Joyner and myself) believe we have identified what \n> needs to be done to fix the issues with the coding modules and we will \n> return to it after sage days 22!\n\nThe new attachment (to be applied on top of the previous one) \nseems to fix the problems in the coding thry docstrings.",
    "created_at": "2010-07-26T23:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83992",
    "user": "wdj"
}
```

Replying to [comment:7 cturner]:
> We (John Cremona, David Joyner and myself) believe we have identified what 
> needs to be done to fix the issues with the coding modules and we will 
> return to it after sage days 22!

The new attachment (to be applied on top of the previous one) 
seems to fix the problems in the coding thry docstrings.



---

archive/issue_comments_083993.json:
```json
{
    "body": "The second patch does not apply cleanly anymore, on sage-4.6.rc0 I am getting\n\n```\napplying trac-9055-coding-thry-docstring-fixes.patch\npatching file sage/coding/linear_code.py\nHunk #13 FAILED at 2028\n```\n",
    "created_at": "2010-11-01T02:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83993",
    "user": "novoselt"
}
```

The second patch does not apply cleanly anymore, on sage-4.6.rc0 I am getting

```
applying trac-9055-coding-thry-docstring-fixes.patch
patching file sage/coding/linear_code.py
Hunk #13 FAILED at 2028
```




---

archive/issue_comments_083994.json:
```json
{
    "body": "What exactly has happened to the broken doctests? It does not seem to me that the new output is merely a permutation of the old one. \n\nThere are (sometimes) extra spaces in front of the output.\n\nThere are some notes/warnings in the documentation and it would be nice if they were formatted according to http://sagemath.org/doc/developer/conventions.html#documentation-strings",
    "created_at": "2010-11-01T02:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83994",
    "user": "novoselt"
}
```

What exactly has happened to the broken doctests? It does not seem to me that the new output is merely a permutation of the old one. 

There are (sometimes) extra spaces in front of the output.

There are some notes/warnings in the documentation and it would be nice if they were formatted according to http://sagemath.org/doc/developer/conventions.html#documentation-strings



---

archive/issue_comments_083995.json:
```json
{
    "body": "Replying to [comment:10 novoselt]:\n> What exactly has happened to the broken doctests? It does not seem to me that the new output is merely a permutation of the old one. \n\nThe ordering of vector spaces over finite fields is used all over the place. In constructing the Hamming codes, etc. I think there is a echelon form involved afterward as well, so it is easy enough to seem like this isn't just a problem with order changing...\n\nThe new patch includes all previous ones, and fixes a docstring fix which needed to be rebased.",
    "created_at": "2010-12-01T13:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83995",
    "user": "rlm"
}
```

Replying to [comment:10 novoselt]:
> What exactly has happened to the broken doctests? It does not seem to me that the new output is merely a permutation of the old one. 

The ordering of vector spaces over finite fields is used all over the place. In constructing the Hamming codes, etc. I think there is a echelon form involved afterward as well, so it is easy enough to seem like this isn't just a problem with order changing...

The new patch includes all previous ones, and fixes a docstring fix which needed to be rebased.



---

archive/issue_comments_083996.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-01T13:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83996",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083997.json:
```json
{
    "body": "I will simply mention for the record that things like\n\n```\n        G = self.gen_mat()\n        F = self.base_ring()\n        q = F.order()\n        q0 = F0.order()\n        a = log(q,q0)  # test if F/F0 is a field extension\n        if not isinstance(a, Integer):\n            raise ValueError,\"Base field must be an extension of given field %s\"%F0\n        n = len(G.columns())\n        k = len(G.rows())\n        G0 = [[x**q0 for x in g.list()] for g in G.rows()]\n        G1 = [[x for x in g.list()] for g in G.rows()]\n        G2 = G0+G1\n        MS = MatrixSpace(F,2*k,n)\n        G3 = MS(G2)\n        r = G3.rank()\n        MS = MatrixSpace(F,r,n)\n        Grref = G3.echelon_form()\n        G = MS([Grref.row(i) for i in range(r)])\n        return LinearCode(G)\n```\n\n(`galois_closure` in `linear_code.py`) can be vastly simplified, and probably sped up in the process.\n\nProgramming no-nos:\n1. Using logarithms to test whether one finite field is contained in another (why not just check whether the characteristics are the same and if one degree divides the other?).\n2. `G1 = [[x for x in g.list()] for g in G.rows()]` ... Why not `G1 = G.rows()` or at least `G1 = [g.list() for g in G.rows()]` etc.? This is a big waste of time (remember that Python is slow anyway...)\n3. This is also bad:\n\n```\n        MS = MatrixSpace(F,2*k,n)\n        G3 = MS(G2)\n        r = G3.rank()\n        MS = MatrixSpace(F,r,n)\n        Grref = G3.echelon_form()\n        G = MS([Grref.row(i) for i in range(r)])\n```\n\n... why not just `G3 = Matrix(F, 2*k, n, G2); G = G3.row_space().basis_matrix()` or the equivalent? It's easier to follow and might be more efficient, too. \n\n(Not criticisms of code in this ticket at all, for the skimmer -- just an indication that `linear_code.py` needs more work...)",
    "created_at": "2010-12-01T13:17:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83997",
    "user": "rlm"
}
```

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
2. `G1 = [[x for x in g.list()] for g in G.rows()]` ... Why not `G1 = G.rows()` or at least `G1 = [g.list() for g in G.rows()]` etc.? This is a big waste of time (remember that Python is slow anyway...)
3. This is also bad:

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

archive/issue_comments_083998.json:
```json
{
    "body": "Attachment\n\nApply last",
    "created_at": "2010-12-01T17:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83998",
    "user": "novoselt"
}
```

Attachment

Apply last



---

archive/issue_comments_083999.json:
```json
{
    "body": "I've prettified documentation of the new module and improved exception handling, since there were several blocks like\n\n```\ntry:\n   ...\nexcept:\n   pass\n```\n\nwhich potentially can cause strange errors or results. In particular, such a code may be hard to interrupt if it is taking too long.\n\nIf someone can go over my patch and approve it, please switch this ticket to positive review. Tests pass.",
    "created_at": "2010-12-01T17:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-83999",
    "user": "novoselt"
}
```

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

archive/issue_comments_084000.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-01T20:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84000",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084001.json:
```json
{
    "body": "This will likely need to be rebased when sage-4.6.1.alpha3 will be released.",
    "created_at": "2010-12-04T22:50:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84001",
    "user": "jdemeyer"
}
```

This will likely need to be rebased when sage-4.6.1.alpha3 will be released.



---

archive/issue_comments_084002.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-12-04T22:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84002",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084003.json:
```json
{
    "body": "Attachment\n\nrebased on sage-4.6.1.alpha2 + #6094",
    "created_at": "2010-12-05T10:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84003",
    "user": "rlm"
}
```

Attachment

rebased on sage-4.6.1.alpha2 + #6094



---

archive/issue_comments_084004.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-12-05T10:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84004",
    "user": "rlm"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_084005.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:32:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84005",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_084006.json:
```json
{
    "body": "Depends on #9055",
    "created_at": "2011-01-19T22:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84006",
    "user": "vbraun"
}
```

Depends on #9055



---

archive/issue_comments_084007.json:
```json
{
    "body": "Sorry wrong ticket, my bad :(",
    "created_at": "2011-01-19T22:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84007",
    "user": "vbraun"
}
```

Sorry wrong ticket, my bad :(



---

archive/issue_comments_084008.json:
```json
{
    "body": "Replying to [comment:20 vbraun]:\n> Depends on #9055\n\nInteresting, a recursive ticket :-)  Do you want to denial-of-service the patchbot?",
    "created_at": "2011-01-19T22:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9055",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9055#issuecomment-84008",
    "user": "jdemeyer"
}
```

Replying to [comment:20 vbraun]:
> Depends on #9055

Interesting, a recursive ticket :-)  Do you want to denial-of-service the patchbot?
