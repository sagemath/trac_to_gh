# Issue 4357: modualr forms -- new subspace used to work and now broken

archive/issues_004357.json:
```json
{
    "body": "Assignee: craigcitro\n\nThis used to work and is now broken.  It is used in my modular forms book.\n\n\n```\nsage: CuspForms(45).new_subspace()\nTraceback (most recent call last):\n...\nNotImplementedError: computation of new submodule not yet implemented\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4357\n\n",
    "created_at": "2008-10-24T02:04:23Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "modualr forms -- new subspace used to work and now broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4357",
    "user": "was"
}
```
Assignee: craigcitro

This used to work and is now broken.  It is used in my modular forms book.


```
sage: CuspForms(45).new_subspace()
Traceback (most recent call last):
...
NotImplementedError: computation of new submodule not yet implemented
```


Issue created by migration from https://trac.sagemath.org/ticket/4357





---

archive/issue_comments_032000.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-27T19:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32000",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032001.json:
```json
{
    "body": "This functionality was removed because it was broken. Indeed, the result returned in William's book is incorrect -- it **should** be:\n\n\n```\nCuspForms(Gamma0(45), 2, prec=14).new_subspace().basis()\n(q + q^2 - q^4 - q^5 - 3*q^8 - q^10 + 4*q^11 - 2*q^13 + O(q^14),)\n```\n\n\nWilliam and I have discussed a fix for this, which I'll take care of soon, unless William beats me to it.",
    "created_at": "2008-10-27T19:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32001",
    "user": "craigcitro"
}
```

This functionality was removed because it was broken. Indeed, the result returned in William's book is incorrect -- it **should** be:


```
CuspForms(Gamma0(45), 2, prec=14).new_subspace().basis()
(q + q^2 - q^4 - q^5 - 3*q^8 - q^10 + 4*q^11 - 2*q^13 + O(q^14),)
```


William and I have discussed a fix for this, which I'll take care of soon, unless William beats me to it.



---

archive/issue_comments_032002.json:
```json
{
    "body": "patch against 3.4.2.alpha0",
    "created_at": "2009-04-30T18:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32002",
    "user": "davidloeffler"
}
```

patch against 3.4.2.alpha0



---

archive/issue_comments_032003.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-04-30T18:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32003",
    "user": "davidloeffler"
}
```

Changing status from assigned to new.



---

archive/issue_comments_032004.json:
```json
{
    "body": "Changing assignee from craigcitro to davidloeffler.",
    "created_at": "2009-04-30T18:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32004",
    "user": "davidloeffler"
}
```

Changing assignee from craigcitro to davidloeffler.



---

archive/issue_comments_032005.json:
```json
{
    "body": "Attachment\n\nI have uploaded a patch which I think fixes this -- it certainly gives the above result for level 45 and weight 2.",
    "created_at": "2009-04-30T18:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32005",
    "user": "davidloeffler"
}
```

Attachment

I have uploaded a patch which I think fixes this -- it certainly gives the above result for level 45 and weight 2.



---

archive/issue_comments_032006.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-30T18:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32006",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032007.json:
```json
{
    "body": "REFEREE REPORT:\n\nLooks good! I'm happy to see this code get merged, modulo a few really tiny things:\n\n* On line 238 of `modular/modform/ambient.py`, I think a line needs to be split.\n\n* In the same file, at line 521, I think we should reverse the order of the cuspidal and Eisenstein parts, so that it matches the order we have for the basis of the modular forms space itself. (Of course, there's no real reason it should be one order over another, but it should be consistent, and the basis code has been around much longer.)\n\n* Note that there's an issue with the `atkin_lehner_eigenvalue` code, but this is fixed in your patch at #5262, so I'm not worried. (I'm about to review that one.)\n\n* On this last one, I mostly have a question -- I could just be confused. You've added a new argument `t` to all the `_degeneracy_raising_matrix` functions, which makes sense with the other changes you've made. But why do you raise a `RuntimeError` if the value isn't 1? Shouldn't it be something like a `NotImplementedError`, or am I missing something? Or if no argument but `t=1` makes sense (for a reason I don't see), then I think it should be a `ValueError`.\n\nOnce those get fixed, I'm happy to see this code go in.",
    "created_at": "2009-05-08T07:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32007",
    "user": "craigcitro"
}
```

REFEREE REPORT:

Looks good! I'm happy to see this code get merged, modulo a few really tiny things:

* On line 238 of `modular/modform/ambient.py`, I think a line needs to be split.

* In the same file, at line 521, I think we should reverse the order of the cuspidal and Eisenstein parts, so that it matches the order we have for the basis of the modular forms space itself. (Of course, there's no real reason it should be one order over another, but it should be consistent, and the basis code has been around much longer.)

* Note that there's an issue with the `atkin_lehner_eigenvalue` code, but this is fixed in your patch at #5262, so I'm not worried. (I'm about to review that one.)

* On this last one, I mostly have a question -- I could just be confused. You've added a new argument `t` to all the `_degeneracy_raising_matrix` functions, which makes sense with the other changes you've made. But why do you raise a `RuntimeError` if the value isn't 1? Shouldn't it be something like a `NotImplementedError`, or am I missing something? Or if no argument but `t=1` makes sense (for a reason I don't see), then I think it should be a `ValueError`.

Once those get fixed, I'm happy to see this code go in.



---

archive/issue_comments_032008.json:
```json
{
    "body": "As for the t argument thing: for modular symbols, where the raising matrices are complicated trace-like operators, the argument t is not used, since the degeneracy raising matrix for all values of t is calculated from the one for t = 1 by composing with a Hecke operator. But for modular forms, the degeneracy raising matrices are pretty easy (since we're working in a \"cohomological\" setup rather than a \"homological\" one) so it is easier to calculate them directly for each t.\n\nHence if _compute_degeneracy_raising matrix is getting called on a modular symbols space with t != 1, that's a runtime error, but on a modular forms space that's not the case. That should be explained in docstrings somewhere; I'll do a follow-up patch.\n\nDavid",
    "created_at": "2009-05-08T07:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32008",
    "user": "davidloeffler"
}
```

As for the t argument thing: for modular symbols, where the raising matrices are complicated trace-like operators, the argument t is not used, since the degeneracy raising matrix for all values of t is calculated from the one for t = 1 by composing with a Hecke operator. But for modular forms, the degeneracy raising matrices are pretty easy (since we're working in a "cohomological" setup rather than a "homological" one) so it is easier to calculate them directly for each t.

Hence if _compute_degeneracy_raising matrix is getting called on a modular symbols space with t != 1, that's a runtime error, but on a modular forms space that's not the case. That should be explained in docstrings somewhere; I'll do a follow-up patch.

David



---

archive/issue_comments_032009.json:
```json
{
    "body": "OK, here's a new patch. This makes absolutely no changes in functionality, but it moves stuff around a bit to clarify what's going on with this mysterious \"t\" argument -- the calculation of the other degeneracy maps from the t=1 one now happens entirely in modsym/ambient.py, which is only right and proper.\n\nI've swapped the order of the sum of cuspidal and Eisenstein parts, but this is solely cosmetic: addition of subspaces of vector spaces in Sage *is* commutative (because the subspace constructor echelon-reduces the basis vectors), and one can check that even with the old patch, for `ModularForms(9, 12).new_subspace()`, the single new Eisenstein series gets listed last, not first.",
    "created_at": "2009-05-08T10:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32009",
    "user": "davidloeffler"
}
```

OK, here's a new patch. This makes absolutely no changes in functionality, but it moves stuff around a bit to clarify what's going on with this mysterious "t" argument -- the calculation of the other degeneracy maps from the t=1 one now happens entirely in modsym/ambient.py, which is only right and proper.

I've swapped the order of the sum of cuspidal and Eisenstein parts, but this is solely cosmetic: addition of subspaces of vector spaces in Sage *is* commutative (because the subspace constructor echelon-reduces the basis vectors), and one can check that even with the old patch, for `ModularForms(9, 12).new_subspace()`, the single new Eisenstein series gets listed last, not first.



---

archive/issue_comments_032010.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-08T10:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32010",
    "user": "davidloeffler"
}
```

Attachment



---

archive/issue_comments_032011.json:
```json
{
    "body": "Excellent ... I'm very happy with all the changes. The `t` stuff is cleaner, and good point about the swapping being cosmetic -- I was reading it and thought \"oh, that should match the order for the ambient space\" without actually realizing that it was irrelevant, since the subspace will have an echelon basis.\n\nTwo thumbs way up.",
    "created_at": "2009-05-10T05:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32011",
    "user": "craigcitro"
}
```

Excellent ... I'm very happy with all the changes. The `t` stuff is cleaner, and good point about the swapping being cosmetic -- I was reading it and thought "oh, that should match the order for the ambient space" without actually realizing that it was irrelevant, since the subspace will have an echelon basis.

Two thumbs way up.



---

archive/issue_comments_032012.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T07:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32012",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032013.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T07:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4357",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4357#issuecomment-32013",
    "user": "mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
