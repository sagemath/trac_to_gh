# Issue 4578: optimize modular symbols decomposition algorithm

archive/issues_004578.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  georgsweber alexghitza\n\nIn short, the decomposition function on spaces of modular symbols is mysteriously way slower than it should be.  Why?\n\nConsider this:\n\n```\nsage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()\nsage: time d = M.decomposition(3)\nCPU times: user 3.21 s, sys: 0.11 s, total: 3.33 s\nWall time: 3.37 s\nsage: t3 = M.hecke_matrix(3)\nsage: time d = t3.decomposition()\nCPU times: user 0.11 s, sys: 0.00 s, total: 0.11 s\nWall time: 0.11 s\nsage: time d = t3.decomposition(algorithm='multimodular', height_guess=1)\nCPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s\nWall time: 0.06 s\n```\n\n\nThis huge timing discrepancy isn't due to caching:\n\n```\n^bsd:matrix was$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.2, Release Date: 2008-11-20                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()\nsage: t3 = M.hecke_matrix(3)\nsage: time d = t3.decomposition(algorithm='multimodular', height_guess=1)\nCPU times: user 0.07 s, sys: 0.01 s, total: 0.08 s\nWall time: 0.08 s\n```\n\n\nFor comparison:\n\n```\nsage: magma.eval(\"M := ModularSymbols(1000,2,1);\")\n''\nsage: magma.eval(\"S := NewSubspace(CuspidalSubspace(M)); time D := Decomposition(S, 3);\")\n'Time: 0.050'\n```\n\n\nSo Sage is nearly the same as Magma at the decomposition part of the computation, but is getting totally killed by using the wrong algorithm or doing something really dumb that it shouldn't even bother doing.  I.e., above 3.2 seconds is spent doing something probably unnecessary, and only 0.08 is spent doing what should be the dominant step. \n\nThere are of course numerous other similar examples.   For concreteness, I think to close this ticket one should just worry about making it so that the above example completes in < 0.2 seconds instead of 3.3 seconds.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4578\n\n",
    "created_at": "2008-11-22T00:28:40Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "optimize modular symbols decomposition algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4578",
    "user": "@williamstein"
}
```
Assignee: @craigcitro

CC:  georgsweber alexghitza

In short, the decomposition function on spaces of modular symbols is mysteriously way slower than it should be.  Why?

Consider this:

```
sage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()
sage: time d = M.decomposition(3)
CPU times: user 3.21 s, sys: 0.11 s, total: 3.33 s
Wall time: 3.37 s
sage: t3 = M.hecke_matrix(3)
sage: time d = t3.decomposition()
CPU times: user 0.11 s, sys: 0.00 s, total: 0.11 s
Wall time: 0.11 s
sage: time d = t3.decomposition(algorithm='multimodular', height_guess=1)
CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
Wall time: 0.06 s
```


This huge timing discrepancy isn't due to caching:

```
^bsd:matrix was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2, Release Date: 2008-11-20                         |
| Type notebook() for the GUI, and license() for information.        |
sage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()
sage: t3 = M.hecke_matrix(3)
sage: time d = t3.decomposition(algorithm='multimodular', height_guess=1)
CPU times: user 0.07 s, sys: 0.01 s, total: 0.08 s
Wall time: 0.08 s
```


For comparison:

```
sage: magma.eval("M := ModularSymbols(1000,2,1);")
''
sage: magma.eval("S := NewSubspace(CuspidalSubspace(M)); time D := Decomposition(S, 3);")
'Time: 0.050'
```


So Sage is nearly the same as Magma at the decomposition part of the computation, but is getting totally killed by using the wrong algorithm or doing something really dumb that it shouldn't even bother doing.  I.e., above 3.2 seconds is spent doing something probably unnecessary, and only 0.08 is spent doing what should be the dominant step. 

There are of course numerous other similar examples.   For concreteness, I think to close this ticket one should just worry about making it so that the above example completes in < 0.2 seconds instead of 3.3 seconds.

Issue created by migration from https://trac.sagemath.org/ticket/4578





---

archive/issue_comments_034323.json:
```json
{
    "body": "There are two reasons why this is much slower than we expect it to be:\nFirst, the restriction of subspaces, when decomposing them, is checked. This is not necessary and already this increases the performance.\nSecond, sorting the resulting Hecke modules depends on computing several Hecke matrices. This we cannot change without introducing major incompatibilities. But I added an option, that sorts the modules by their basis structure. This makes the function again much fast.\n\n\n```\nsage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()\nsage: %time d  = M.decomposition(3)\nCPU times: user 1.62 s, sys: 0.00 s, total: 1.63 s\nWall time: 1.92 s\n```\n\n\nand\n\n\n```\nsage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()\nsage: %time d  = M.decomposition(3, sort_by_basis = True)\nCPU times: user 0.94 s, sys: 0.00 s, total: 0.94 s\nWall time: 1.59 s\n```\n\n\nNote, that the bare decomposition given in the description is not sufficient: We need at least compute two further decompositions, since two of the resulting modules are not irreducible with respect to T(2).",
    "created_at": "2011-03-22T21:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34323",
    "user": "mraum"
}
```

There are two reasons why this is much slower than we expect it to be:
First, the restriction of subspaces, when decomposing them, is checked. This is not necessary and already this increases the performance.
Second, sorting the resulting Hecke modules depends on computing several Hecke matrices. This we cannot change without introducing major incompatibilities. But I added an option, that sorts the modules by their basis structure. This makes the function again much fast.


```
sage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()
sage: %time d  = M.decomposition(3)
CPU times: user 1.62 s, sys: 0.00 s, total: 1.63 s
Wall time: 1.92 s
```


and


```
sage: M = ModularSymbols(1000,2,sign=1).new_subspace().cuspidal_subspace()
sage: %time d  = M.decomposition(3, sort_by_basis = True)
CPU times: user 0.94 s, sys: 0.00 s, total: 0.94 s
Wall time: 1.59 s
```


Note, that the bare decomposition given in the description is not sufficient: We need at least compute two further decompositions, since two of the resulting modules are not irreducible with respect to T(2).



---

archive/issue_comments_034324.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-22T21:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34324",
    "user": "mraum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_034325.json:
```json
{
    "body": "Hang on. Surely this patch doesn't remotely match the ticket description? If called with the default arguments this patch is a complete no-op! \n\nDid you perhaps want to call `decomposition_of_subspace` with the argument `\"check_restrict=False\"`? Because Sage's Hecke algebras are always commutative, this check is probably redundant. That would, I imagine, result in a substantial speedup.",
    "created_at": "2011-04-10T08:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34325",
    "user": "@loefflerd"
}
```

Hang on. Surely this patch doesn't remotely match the ticket description? If called with the default arguments this patch is a complete no-op! 

Did you perhaps want to call `decomposition_of_subspace` with the argument `"check_restrict=False"`? Because Sage's Hecke algebras are always commutative, this check is probably redundant. That would, I imagine, result in a substantial speedup.



---

archive/issue_comments_034326.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-04-10T08:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34326",
    "user": "@loefflerd"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_034327.json:
```json
{
    "body": "Attachment [trac-4578-optimize_modular_symbols_decomposition-doctest.patch](tarball://root/attachments/some-uuid/ticket4578/trac-4578-optimize_modular_symbols_decomposition-doctest.patch) by mraum created at 2011-04-13 18:28:37\n\nYou're completely right. Thank you for catching this! I replaced the old patch with the right one. Doing this it turned out, that I needed to change one doctest. The change is justified as the element alpha - 1 and 1/2 alpha + 1/2 have the same minpolys. They are, thought, elements of number fields defined with completely different polynomial (They are isomorphic!). This happens because the number field is now generated by a different piece of code in the linalg modules of Sage.\n\nThe old and new parent are for me\n\n```\nOLD:\nNumber Field in alpha with defining polynomial x^2 + 4*x + 1\n\nNEW:\nNumber Field in alpha with defining polynomial x^2 - 2*x - 11\n```\n",
    "created_at": "2011-04-13T18:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34327",
    "user": "mraum"
}
```

Attachment [trac-4578-optimize_modular_symbols_decomposition-doctest.patch](tarball://root/attachments/some-uuid/ticket4578/trac-4578-optimize_modular_symbols_decomposition-doctest.patch) by mraum created at 2011-04-13 18:28:37

You're completely right. Thank you for catching this! I replaced the old patch with the right one. Doing this it turned out, that I needed to change one doctest. The change is justified as the element alpha - 1 and 1/2 alpha + 1/2 have the same minpolys. They are, thought, elements of number fields defined with completely different polynomial (They are isomorphic!). This happens because the number field is now generated by a different piece of code in the linalg modules of Sage.

The old and new parent are for me

```
OLD:
Number Field in alpha with defining polynomial x^2 + 4*x + 1

NEW:
Number Field in alpha with defining polynomial x^2 - 2*x - 11
```




---

archive/issue_comments_034328.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-04-13T18:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34328",
    "user": "mraum"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_034329.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-07-15T10:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34329",
    "user": "@loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_034330.json:
```json
{
    "body": "I'm happy with that change. As Martin has pointed out, the timing comparison with Magma is misleading: Sage is computing much more information than Magma (decomposing a bunch more Hecke operators). So I advocate merging Martin's patch and closing this ticket.",
    "created_at": "2011-07-15T10:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34330",
    "user": "@loefflerd"
}
```

I'm happy with that change. As Martin has pointed out, the timing comparison with Magma is misleading: Sage is computing much more information than Magma (decomposing a bunch more Hecke operators). So I advocate merging Martin's patch and closing this ticket.



---

archive/issue_comments_034331.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-08-03T09:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34331",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_034332.json:
```json
{
    "body": "There is an issue with the documentation:\n\n```\ndochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha1/local/lib/python2.6/site-packages/sage/modular/hecke/module.py:docstring of sage.modular.hecke.module.HeckeModule_free_module.T:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n```\n",
    "created_at": "2011-08-03T09:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34332",
    "user": "@jdemeyer"
}
```

There is an issue with the documentation:

```
dochtml.log:/mnt/usb1/scratch/jdemeyer/merger/sage-4.7.2.alpha1/local/lib/python2.6/site-packages/sage/modular/hecke/module.py:docstring of sage.modular.hecke.module.HeckeModule_free_module.T:7: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
```




---

archive/issue_comments_034333.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-08-03T15:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34333",
    "user": "mraum"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_034334.json:
```json
{
    "body": "Attachment [trac-4578-optimize_modular_symbols_decomposition-v2.patch](tarball://root/attachments/some-uuid/ticket4578/trac-4578-optimize_modular_symbols_decomposition-v2.patch) by mraum created at 2011-08-03 15:52:36\n\nThis was a very stupid typo. I have checked that it occurs with the old patch and does not occur with the new one. The only thing that I changes is two spaces, one added, one removed. So I set this back to positive review; Sorry for the inconvenience, Jeroen!",
    "created_at": "2011-08-03T15:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34334",
    "user": "mraum"
}
```

Attachment [trac-4578-optimize_modular_symbols_decomposition-v2.patch](tarball://root/attachments/some-uuid/ticket4578/trac-4578-optimize_modular_symbols_decomposition-v2.patch) by mraum created at 2011-08-03 15:52:36

This was a very stupid typo. I have checked that it occurs with the old patch and does not occur with the new one. The only thing that I changes is two spaces, one added, one removed. So I set this back to positive review; Sorry for the inconvenience, Jeroen!



---

archive/issue_comments_034335.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-08-18T22:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4578",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4578#issuecomment-34335",
    "user": "@jdemeyer"
}
```

Resolution: fixed
