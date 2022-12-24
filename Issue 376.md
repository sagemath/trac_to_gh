# Issue 376: finite field homomorphisms don't work

archive/issues_000376.json:
```json
{
    "body": "Assignee: somebody\n\nThe following should work and define a homomorphism.\nI don't remember actually implementing finite field homomorphisms, so it's\nno surprise they don't just magically work.  This is very useful though, so\nit needs to get done. \n\n```\nk = GF(73^2,'a')\nf = k.modulus()\nr = f.change_ring(k).roots()\nk.hom([r[0][0]])\n///\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/was/edu/2007/bsd/sage_notebook/worksheets/_scratch_/code/15.py\", line 4, in <module>\n    exec compile(ur'k.hom([r[Integer(0)][Integer(0)]])' + '\\n', '', 'single')\n  File \"/home/was/edu/2007/bsd/\", line 1, in <module>\n    \n  File \"parent_gens.pyx\", line 505, in parent_gens.ParentWithGens.hom\n  File \"/home/was/s/local/lib/python2.5/site-packages/sage/rings/homset.py\", line 80, in __call__\n    raise TypeError, \"images do not define a valid homomorphism\"\nTypeError: images do not define a valid homomorphism\n```\n\n\n\n```\nk.hom([r[1][0]])\n///\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/was/edu/2007/bsd/sage_notebook/worksheets/_scratch_/code/16.py\", line 4, in <module>\n    exec compile(ur'k.hom([r[Integer(1)][Integer(0)]])' + '\\n', '', 'single')\n  File \"/home/was/edu/2007/bsd/\", line 1, in <module>\n    \n  File \"parent_gens.pyx\", line 505, in parent_gens.ParentWithGens.hom\n  File \"/home/was/s/local/lib/python2.5/site-packages/sage/rings/homset.py\", line 80, in __call__\n    raise TypeError, \"images do not define a valid homomorphism\"\nTypeError: images do not define a valid homomorphism\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/376\n\n",
    "created_at": "2007-05-23T17:04:26Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "finite field homomorphisms don't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/376",
    "user": "was"
}
```
Assignee: somebody

The following should work and define a homomorphism.
I don't remember actually implementing finite field homomorphisms, so it's
no surprise they don't just magically work.  This is very useful though, so
it needs to get done. 

```
k = GF(73^2,'a')
f = k.modulus()
r = f.change_ring(k).roots()
k.hom([r[0][0]])
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/was/edu/2007/bsd/sage_notebook/worksheets/_scratch_/code/15.py", line 4, in <module>
    exec compile(ur'k.hom([r[Integer(0)][Integer(0)]])' + '\n', '', 'single')
  File "/home/was/edu/2007/bsd/", line 1, in <module>
    
  File "parent_gens.pyx", line 505, in parent_gens.ParentWithGens.hom
  File "/home/was/s/local/lib/python2.5/site-packages/sage/rings/homset.py", line 80, in __call__
    raise TypeError, "images do not define a valid homomorphism"
TypeError: images do not define a valid homomorphism
```



```
k.hom([r[1][0]])
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/was/edu/2007/bsd/sage_notebook/worksheets/_scratch_/code/16.py", line 4, in <module>
    exec compile(ur'k.hom([r[Integer(1)][Integer(0)]])' + '\n', '', 'single')
  File "/home/was/edu/2007/bsd/", line 1, in <module>
    
  File "parent_gens.pyx", line 505, in parent_gens.ParentWithGens.hom
  File "/home/was/s/local/lib/python2.5/site-packages/sage/rings/homset.py", line 80, in __call__
    raise TypeError, "images do not define a valid homomorphism"
TypeError: images do not define a valid homomorphism
```


Issue created by migration from https://trac.sagemath.org/ticket/376





---

archive/issue_comments_001793.json:
```json
{
    "body": "Changing assignee from somebody to craigcitro.",
    "created_at": "2007-09-07T02:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/376#issuecomment-1793",
    "user": "craigcitro"
}
```

Changing assignee from somebody to craigcitro.



---

archive/issue_comments_001794.json:
```json
{
    "body": "I think this patch fixes this bug. Turns out that the whole morphism system depends on the field having a method called _is_valid_homomorphism_ ... sadly, the way errors are caught and handled, this isn't the easiest to track down.",
    "created_at": "2007-09-07T02:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/376#issuecomment-1794",
    "user": "craigcitro"
}
```

I think this patch fixes this bug. Turns out that the whole morphism system depends on the field having a method called _is_valid_homomorphism_ ... sadly, the way errors are caught and handled, this isn't the easiest to track down.



---

archive/issue_comments_001795.json:
```json
{
    "body": "Attachment [trac_376.hg](tarball://root/attachments/some-uuid/ticket376/trac_376.hg) by was created at 2007-09-07 02:51:26",
    "created_at": "2007-09-07T02:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/376#issuecomment-1795",
    "user": "was"
}
```

Attachment [trac_376.hg](tarball://root/attachments/some-uuid/ticket376/trac_376.hg) by was created at 2007-09-07 02:51:26



---

archive/issue_comments_001796.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T02:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/376",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/376#issuecomment-1796",
    "user": "was"
}
```

Resolution: fixed
