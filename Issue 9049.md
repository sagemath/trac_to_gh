# Issue 9049: v4.4.1 bug in variety() over finite field extensions of Q?

archive/issues_009049.json:
```json
{
    "body": "Assignee: @aghitza\n\nI'm interested in computing the 0-dimensional variety of an ideal over finite field extensions of Q. I've tried the following code both on my copy (v4.4.1) of sage and online and it produces an error message. My friend tried the same code on his v4.2 sage and it worked fine. Is it possible there's a bug in the newer version?\n\n\n```\nS.<t>=PolynomialRing(QQ)\nF.<q>=QQ.extension(t^4+1)\nR.<x,y>=PolynomialRing(F)\nI=R.ideal(x,y^4+1)\nI.variety()\n```\n\n\nThis produces the following error message:\n          \t\n\nTraceback (click to the left of this block for traceback)\n...\nValueError: Length must be equal to the degree of this number field\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_11.py\", line 10, in <module>\n    exec compile(u'open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"Uy48dD49UG9seW5vbWlhbFJpbmcoUVEpCkYuPHE+PVFRLmV4dGVuc2lvbih0XjQrMSkKUi48eCx5Pj1Qb2x5bm9taWFsUmluZyhGKQpJPVIuaWRlYWwoeCx5XjQrMSkKSS52YXJpZXR5KCk=\"),globals())+\"\\\\n\"); execfile(os.path.abspath(\"___code___.py\"))\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpZcwb0q/___code___.py\", line 7, in <module>\n    exec compile(u'I.variety()\n  File \"\", line 1, in <module>\n    \n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 407, in __call__\n    return self.f(self._instance, *args, **kwds)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 2094, in variety\n    TI = self.triangular_decomposition('singular:triangLfak')\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 407, in __call__\n    return self.f(self._instance, *args, **kwds)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 901, in triangular_decomposition\n    is_groebner = self.basis_is_groebner()\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/cachefunc.py\", line 322, in __call__\n    return self._cachedmethod._instance_call(self._instance, *args, **kwds)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/cachefunc.py\", line 466, in _instance_call\n    cache[key] = self._cachedfunc.f(inst, *args, **kwds)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1666, in basis_is_groebner\n    F = matrix(R, 1, self.ngens(), self.gens())\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/constructor.py\", line 652, in matrix\n    return matrix_space.MatrixSpace(ring, nrows, ncols, sparse=sparse)(entries)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py\", line 405, in __call__\n    return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py\", line 1136, in matrix\n    return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce) \n  File \"matrix_generic_dense.pyx\", line 68, in sage.matrix.matrix_generic_dense.Matrix_generic_dense.__init__ (sage/matrix/matrix_generic_dense.c:1997)\n  File \"multi_polynomial_libsingular.pyx\", line 758, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7176)\n  File \"parent.pyx\", line 854, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)\n  File \"coerce_maps.pyx\", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)\n  File \"coerce_maps.pyx\", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/number_field/number_field.py\", line 1023, in _element_constructor_\n    raise ValueError, \"Length must be equal to the degree of this number field\"\nValueError: Length must be equal to the degree of this number field\n\nIssue created by migration from https://trac.sagemath.org/ticket/9049\n\n",
    "created_at": "2010-05-25T20:37:38Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "v4.4.1 bug in variety() over finite field extensions of Q?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9049",
    "user": "https://trac.sagemath.org/admin/accounts/users/cynthia_vinzant"
}
```
Assignee: @aghitza

I'm interested in computing the 0-dimensional variety of an ideal over finite field extensions of Q. I've tried the following code both on my copy (v4.4.1) of sage and online and it produces an error message. My friend tried the same code on his v4.2 sage and it worked fine. Is it possible there's a bug in the newer version?


```
S.<t>=PolynomialRing(QQ)
F.<q>=QQ.extension(t^4+1)
R.<x,y>=PolynomialRing(F)
I=R.ideal(x,y^4+1)
I.variety()
```


This produces the following error message:
          	

Traceback (click to the left of this block for traceback)
...
ValueError: Length must be equal to the degree of this number field

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_11.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("Uy48dD49UG9seW5vbWlhbFJpbmcoUVEpCkYuPHE+PVFRLmV4dGVuc2lvbih0XjQrMSkKUi48eCx5Pj1Qb2x5bm9taWFsUmluZyhGKQpJPVIuaWRlYWwoeCx5XjQrMSkKSS52YXJpZXR5KCk="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpZcwb0q/___code___.py", line 7, in <module>
    exec compile(u'I.variety()
  File "", line 1, in <module>
    
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 407, in __call__
    return self.f(self._instance, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 2094, in variety
    TI = self.triangular_decomposition('singular:triangLfak')
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 407, in __call__
    return self.f(self._instance, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 901, in triangular_decomposition
    is_groebner = self.basis_is_groebner()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/cachefunc.py", line 322, in __call__
    return self._cachedmethod._instance_call(self._instance, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/cachefunc.py", line 466, in _instance_call
    cache[key] = self._cachedfunc.f(inst, *args, **kwds)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1666, in basis_is_groebner
    F = matrix(R, 1, self.ngens(), self.gens())
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/constructor.py", line 652, in matrix
    return matrix_space.MatrixSpace(ring, nrows, ncols, sparse=sparse)(entries)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 405, in __call__
    return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix_space.py", line 1136, in matrix
    return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce) 
  File "matrix_generic_dense.pyx", line 68, in sage.matrix.matrix_generic_dense.Matrix_generic_dense.__init__ (sage/matrix/matrix_generic_dense.c:1997)
  File "multi_polynomial_libsingular.pyx", line 758, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:7176)
  File "parent.pyx", line 854, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3108)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3010)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/number_field/number_field.py", line 1023, in _element_constructor_
    raise ValueError, "Length must be equal to the degree of this number field"
ValueError: Length must be equal to the degree of this number field

Issue created by migration from https://trac.sagemath.org/ticket/9049





---

archive/issue_comments_083641.json:
```json
{
    "body": "I just made the error message to be a code block.",
    "created_at": "2010-05-26T01:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83641",
    "user": "https://github.com/novoselt"
}
```

I just made the error message to be a code block.



---

archive/issue_comments_083642.json:
```json
{
    "body": "I can verify that the bug still exists in v4.4.3.\nThis seems to be because of I.gens() is returning a tuple, while I.basis_is_groebner,  specifically the line\n\n```\n F = matrix(R, 1, self.ngens(), self.gens())\n```\n\nexpects I.gens() to be a list. Did I.gens() change its return type recently? A quick hack converting self.gens() to a list solves the problem. Should I provide that patch?",
    "created_at": "2010-06-23T17:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83642",
    "user": "https://github.com/syazdani77"
}
```

I can verify that the bug still exists in v4.4.3.
This seems to be because of I.gens() is returning a tuple, while I.basis_is_groebner,  specifically the line

```
 F = matrix(R, 1, self.ngens(), self.gens())
```

expects I.gens() to be a list. Did I.gens() change its return type recently? A quick hack converting self.gens() to a list solves the problem. Should I provide that patch?



---

archive/issue_comments_083643.json:
```json
{
    "body": ">Should I provide that patch? \n\nThat would be great. Thanks!",
    "created_at": "2010-06-24T18:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83643",
    "user": "https://trac.sagemath.org/admin/accounts/users/cynthia_vinzant"
}
```

>Should I provide that patch? 

That would be great. Thanks!



---

archive/issue_comments_083644.json:
```json
{
    "body": "Attachment [trac_9049_fix_is_groebner.patch](tarball://root/attachments/some-uuid/ticket9049/trac_9049_fix_is_groebner.patch) by @syazdani77 created at 2010-06-25 15:27:59\n\nconverts a tuple to a list so matrix constructor isn't confused.",
    "created_at": "2010-06-25T15:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83644",
    "user": "https://github.com/syazdani77"
}
```

Attachment [trac_9049_fix_is_groebner.patch](tarball://root/attachments/some-uuid/ticket9049/trac_9049_fix_is_groebner.patch) by @syazdani77 created at 2010-06-25 15:27:59

converts a tuple to a list so matrix constructor isn't confused.



---

archive/issue_comments_083645.json:
```json
{
    "body": "Thanks very much -- it works wonderfully.",
    "created_at": "2010-06-25T17:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83645",
    "user": "https://trac.sagemath.org/admin/accounts/users/cynthia_vinzant"
}
```

Thanks very much -- it works wonderfully.



---

archive/issue_comments_083646.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T12:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83646",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083647.json:
```json
{
    "body": "While the previous patch works for the problem of this ticket, it does not solve the real issue - you can construct a matrix from a list, but not from a tuple of the same elements, which does not make much sense. The new patch changes the relevant matrix constructor to allow tuples.",
    "created_at": "2010-09-24T16:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83647",
    "user": "https://github.com/novoselt"
}
```

While the previous patch works for the problem of this ticket, it does not solve the real issue - you can construct a matrix from a list, but not from a tuple of the same elements, which does not make much sense. The new patch changes the relevant matrix constructor to allow tuples.



---

archive/issue_comments_083648.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2010-09-24T16:45:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83648",
    "user": "https://github.com/novoselt"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_083649.json:
```json
{
    "body": "Can you provide a more direct test to check the case when `entries` is a `tuple`?\n\nPerhaps the example given in this ticket should be placed in the `.variety()` method of the ideal class. It is not guaranteed that we will always use the `Matrix_generic_dense` class in the future.",
    "created_at": "2010-09-24T17:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83649",
    "user": "https://github.com/burcin"
}
```

Can you provide a more direct test to check the case when `entries` is a `tuple`?

Perhaps the example given in this ticket should be placed in the `.variety()` method of the ideal class. It is not guaranteed that we will always use the `Matrix_generic_dense` class in the future.



---

archive/issue_comments_083650.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-24T17:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83650",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083651.json:
```json
{
    "body": "Apply this patch only: allow construction of matrices from tuples.",
    "created_at": "2010-09-24T18:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83651",
    "user": "https://github.com/novoselt"
}
```

Apply this patch only: allow construction of matrices from tuples.



---

archive/issue_comments_083652.json:
```json
{
    "body": "Attachment [trac_9049_bug_in_matrices_from_tuples.patch](tarball://root/attachments/some-uuid/ticket9049/trac_9049_bug_in_matrices_from_tuples.patch) by @novoselt created at 2010-09-24 18:20:58\n\nDone!",
    "created_at": "2010-09-24T18:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83652",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_9049_bug_in_matrices_from_tuples.patch](tarball://root/attachments/some-uuid/ticket9049/trac_9049_bug_in_matrices_from_tuples.patch) by @novoselt created at 2010-09-24 18:20:58

Done!



---

archive/issue_comments_083653.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-24T18:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83653",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083654.json:
```json
{
    "body": "Attachment [trac_9049_bug_in_matrices_from_tuples.take2.patch](tarball://root/attachments/some-uuid/ticket9049/trac_9049_bug_in_matrices_from_tuples.take2.patch) by @burcin created at 2010-09-24 21:18:45\n\nalternative patch",
    "created_at": "2010-09-24T21:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83654",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9049_bug_in_matrices_from_tuples.take2.patch](tarball://root/attachments/some-uuid/ticket9049/trac_9049_bug_in_matrices_from_tuples.take2.patch) by @burcin created at 2010-09-24 21:18:45

alternative patch



---

archive/issue_comments_083655.json:
```json
{
    "body": "Thanks! That was quick. :)\n\nI suggest to replace the check\n\n```\nif not isinstance(entries, list):\n```\n\nwith\n\n```\nif not isinstance(entries, (list, tuple)):\n```\n\ninstead of accepting `ValueError`s as well.\n\nattachment:trac_9049_bug_in_matrices_from_tuples.take2.patch includes this alternative approach.\n\nPlease switch this to `positive_review` if you agree with my changes.",
    "created_at": "2010-09-24T21:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83655",
    "user": "https://github.com/burcin"
}
```

Thanks! That was quick. :)

I suggest to replace the check

```
if not isinstance(entries, list):
```

with

```
if not isinstance(entries, (list, tuple)):
```

instead of accepting `ValueError`s as well.

attachment:trac_9049_bug_in_matrices_from_tuples.take2.patch includes this alternative approach.

Please switch this to `positive_review` if you agree with my changes.



---

archive/issue_comments_083656.json:
```json
{
    "body": "I thought about it, but I was not sure if it is necessary somewhere later to have exactly list, rather than tuple. Also, since the point of this try-block is to see whether or not it is possible to perform certain conversion, I think that any exception resulting from \"wrong\" conversion can be intercepted. If we just skip it for tuples, will we need later to skip it for, say, sequences? So I would prefer to stick with my patch as I think it is more universal. What do you think?",
    "created_at": "2010-09-24T21:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83656",
    "user": "https://github.com/novoselt"
}
```

I thought about it, but I was not sure if it is necessary somewhere later to have exactly list, rather than tuple. Also, since the point of this try-block is to see whether or not it is possible to perform certain conversion, I think that any exception resulting from "wrong" conversion can be intercepted. If we just skip it for tuples, will we need later to skip it for, say, sequences? So I would prefer to stick with my patch as I think it is more universal. What do you think?



---

archive/issue_comments_083657.json:
```json
{
    "body": "`Sequence`s are lists:\n\n```\nsage: t = Sequence([1..5])\nsage: isinstance(t, list)\nTrue\n```\n\n\nExplicitly checking for the condition you are testing is better than trial and error. You cannot know the meaning of the `ValueError` returned from the base rings `__call__` method, especially in such a generic setting. \n\nIMHO, that `try` & `except` block should be cleaned up. However it's hard to do so as it is, since this is a generic constructor, there are no doctests or specification of what the acceptable input is and doctesting the whole sage library takes hours on my laptop.\n\nPlease reconsider my suggestion, with the \"better safe then sorry\" motto in mind.",
    "created_at": "2010-09-24T21:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83657",
    "user": "https://github.com/burcin"
}
```

`Sequence`s are lists:

```
sage: t = Sequence([1..5])
sage: isinstance(t, list)
True
```


Explicitly checking for the condition you are testing is better than trial and error. You cannot know the meaning of the `ValueError` returned from the base rings `__call__` method, especially in such a generic setting. 

IMHO, that `try` & `except` block should be cleaned up. However it's hard to do so as it is, since this is a generic constructor, there are no doctests or specification of what the acceptable input is and doctesting the whole sage library takes hours on my laptop.

Please reconsider my suggestion, with the "better safe then sorry" motto in mind.



---

archive/issue_comments_083658.json:
```json
{
    "body": "OK, let's use the alternative patch! Switching to positive review.",
    "created_at": "2010-09-24T22:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83658",
    "user": "https://github.com/novoselt"
}
```

OK, let's use the alternative patch! Switching to positive review.



---

archive/issue_comments_083659.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-24T22:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83659",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083660.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9049#issuecomment-83660",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009200.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-28T10:57:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9049",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9049#event-9200"
}
```
