# Issue 4304: [with patch, needs review] split up NTL's decl.pxi

archive/issues_004304.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  robertwb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4304\n\n",
    "created_at": "2008-10-15T17:44:13Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs review] split up NTL's decl.pxi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4304",
    "user": "malb"
}
```
Assignee: cwitty

CC:  robertwb



Issue created by migration from https://trac.sagemath.org/ticket/4304





---

archive/issue_comments_031492.json:
```json
{
    "body": "Attachment [ntl_decl_refactor.patch](tarball://root/attachments/some-uuid/ticket4304/ntl_decl_refactor.patch) by zimmerma created at 2008-10-15 19:32:23\n\nI could not apply the patch:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.3, Release Date: 2008-10-14                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: hg_scripts.import_patch(\"/tmp/ntl_decl_refactor.patch\")\ncd \"/usr/local/sage-3.1.3/sage/local/bin\" && hg status\ncd \"/usr/local/sage-3.1.3/sage/local/bin\" && hg status\ncd \"/usr/local/sage-3.1.3/sage/local/bin\" && hg import   \"/tmp/ntl_decl_refactor\n.patch\"\napplying /tmp/ntl_decl_refactor.patch\nunable to find 'sage/libs/ntl/decl.pxi' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/decl.pxi.rej\nunable to find 'sage/libs/ntl/ntl_ZZX.pyx' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_ZZX.pyx.rej\nunable to find 'sage/libs/ntl/ntl_ZZ_pX.pxd' for patching\n2 out of 2 hunks FAILED -- saving rejects to file sage/libs/ntl/ntl_ZZ_pX.pxd.rej\nunable to find 'sage/libs/ntl/ntl_lzz_p.pxd' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_lzz_p.pxd.rej\nunable to find 'sage/libs/ntl/ntl_lzz_pX.pxd' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_lzz_pX.pxd.rej\nunable to find 'sage/rings/padics/pow_computer_ext.pxd' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/padics/pow_computer_ext.pxd.rej\nunable to find 'sage/rings/polynomial/polynomial_integer_dense_flint.pyx' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_integer_dense_flint.pyx.rej\nunable to find 'sage/rings/polynomial/polynomial_integer_dense_ntl.pyx' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_integer_dense_ntl.pyx.rej\nunable to find 'sage/rings/polynomial/polynomial_modn_dense_ntl.pxd' for patching\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_modn_dense_ntl.pxd.rej\nunable to find 'sage/rings/polynomial/polynomial_modn_dense_ntl.pyx' for patching\n5 out of 5 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_modn_dense_ntl.pyx.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2008-10-15T19:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4304#issuecomment-31492",
    "user": "zimmerma"
}
```

Attachment [ntl_decl_refactor.patch](tarball://root/attachments/some-uuid/ticket4304/ntl_decl_refactor.patch) by zimmerma created at 2008-10-15 19:32:23

I could not apply the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.3, Release Date: 2008-10-14                       |
| Type notebook() for the GUI, and license() for information.        |
sage: hg_scripts.import_patch("/tmp/ntl_decl_refactor.patch")
cd "/usr/local/sage-3.1.3/sage/local/bin" && hg status
cd "/usr/local/sage-3.1.3/sage/local/bin" && hg status
cd "/usr/local/sage-3.1.3/sage/local/bin" && hg import   "/tmp/ntl_decl_refactor
.patch"
applying /tmp/ntl_decl_refactor.patch
unable to find 'sage/libs/ntl/decl.pxi' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/decl.pxi.rej
unable to find 'sage/libs/ntl/ntl_ZZX.pyx' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_ZZX.pyx.rej
unable to find 'sage/libs/ntl/ntl_ZZ_pX.pxd' for patching
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/ntl/ntl_ZZ_pX.pxd.rej
unable to find 'sage/libs/ntl/ntl_lzz_p.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_lzz_p.pxd.rej
unable to find 'sage/libs/ntl/ntl_lzz_pX.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/libs/ntl/ntl_lzz_pX.pxd.rej
unable to find 'sage/rings/padics/pow_computer_ext.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/padics/pow_computer_ext.pxd.rej
unable to find 'sage/rings/polynomial/polynomial_integer_dense_flint.pyx' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_integer_dense_flint.pyx.rej
unable to find 'sage/rings/polynomial/polynomial_integer_dense_ntl.pyx' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_integer_dense_ntl.pyx.rej
unable to find 'sage/rings/polynomial/polynomial_modn_dense_ntl.pxd' for patching
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/polynomial/polynomial_modn_dense_ntl.pxd.rej
unable to find 'sage/rings/polynomial/polynomial_modn_dense_ntl.pyx' for patching
5 out of 5 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_modn_dense_ntl.pyx.rej
abort: patch failed to apply
```




---

archive/issue_comments_031493.json:
```json
{
    "body": "Hi Paul,\n\nyou did apply the patch to the scripts repo, but you need to apply the patch to the hg_sage repo. I just tested and the patch applies fine against 3.1.3 as well as 3.1.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-15T19:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4304#issuecomment-31493",
    "user": "mabshoff"
}
```

Hi Paul,

you did apply the patch to the scripts repo, but you need to apply the patch to the hg_sage repo. I just tested and the patch applies fine against 3.1.3 as well as 3.1.4.

Cheers,

Michael



---

archive/issue_comments_031494.json:
```json
{
    "body": "Merges fine, building right now, but the code looks good and should help speed up build time and make things much cleaner.",
    "created_at": "2008-10-15T20:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4304#issuecomment-31494",
    "user": "robertwb"
}
```

Merges fine, building right now, but the code looks good and should help speed up build time and make things much cleaner.



---

archive/issue_comments_031495.json:
```json
{
    "body": "Doctests pass, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-17T23:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4304#issuecomment-31495",
    "user": "mabshoff"
}
```

Doctests pass, positive review.

Cheers,

Michael



---

archive/issue_comments_031496.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T00:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4304#issuecomment-31496",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031497.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-18T00:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4304",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4304#issuecomment-31497",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha0
