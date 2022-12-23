# Issue 5094: Delete/Change SageX references to Cython

archive/issues_005094.json:
```json
{
    "body": "Assignee: tba\n\nIn 3.3.alpha0, there is still a reference to SageX in COPYING.txt.  Any others should also be reported here.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5094\n\n",
    "created_at": "2009-01-25T03:45:34Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "title": "Delete/Change SageX references to Cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5094",
    "user": "kcrisman"
}
```
Assignee: tba

In 3.3.alpha0, there is still a reference to SageX in COPYING.txt.  Any others should also be reported here.

Issue created by migration from https://trac.sagemath.org/ticket/5094





---

archive/issue_comments_038848.json:
```json
{
    "body": "This is not a duplicate of #857; the reference is in the second line of the document.",
    "created_at": "2009-01-25T03:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38848",
    "user": "kcrisman"
}
```

This is not a duplicate of #857; the reference is in the second line of the document.



---

archive/issue_comments_038849.json:
```json
{
    "body": "Attachment\n\nThis is a one-word change of SageX to Cython from the 3.3.alpha0 version of this file.",
    "created_at": "2009-01-29T15:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38849",
    "user": "kcrisman"
}
```

Attachment

This is a one-word change of SageX to Cython from the 3.3.alpha0 version of this file.



---

archive/issue_comments_038850.json:
```json
{
    "body": "Here are the others I have found.  Most would be trivial to fix, but I don't know if all these files are long for this world.\n\nmisc/cython.py\n\tIn addition to one that should be there, there is one that it not!\n\nrings/integer_mod_ring.py\n\tAn author credit should have Cython added\n\nrings/padics/tutorial.py\n\tBrief ref\n\ncalculus/var.pyx\n\tTwo references at G = globals()\n\ngraphs/graph_fast.pyx\n\tThe title refers to it\n\nmisc/reset.pyx\n\tTwo references at G = globals()\n\nmisc/sagex_ds.pyx \n\tIncludes references but of course is NAMED after it\n\tIt appears to be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory\n\nrings/integer.pyx\n\tAgain a couple\n\nrings/laurent_series_ring_element.pyx\n\tBrief ref\n\nrings/power_series_ring_element.pyx\n\tBrief ref\n\nrings/polynomial/polynomial_element.pyx\n\tA couple references\n\next/python.pxi\n\tQuite a few references at the top\n\nrings/real_rqdf.pyx\n\tOne ref, if this is even being kept\n\nstructure/parent_old.pyx\n\tSeveral references, is this worth fixing?\n\nlibs/pari/gen.pyx\n\tBrief ref\n\nThere were some in docs, but presumably that is not worth changing until after the Sphinx change:\nref/module-sage.rings.integer-mod-ring.html\nref/module-sage.rings.laurent-series-ring-element.html\nref/module-sage.rings.padics.tutorial.html\nref/module-sage.rings.polynomial.polynomial-element.html\nref/module-sage.rings.power-series-ring-element.html\nref/node343.html\ntut/node53.html (two examples, in SAGE_ROOT/examples/programming/sagex - should that directory be renamed as well?)",
    "created_at": "2009-01-29T15:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38850",
    "user": "kcrisman"
}
```

Here are the others I have found.  Most would be trivial to fix, but I don't know if all these files are long for this world.

misc/cython.py
	In addition to one that should be there, there is one that it not!

rings/integer_mod_ring.py
	An author credit should have Cython added

rings/padics/tutorial.py
	Brief ref

calculus/var.pyx
	Two references at G = globals()

graphs/graph_fast.pyx
	The title refers to it

misc/reset.pyx
	Two references at G = globals()

misc/sagex_ds.pyx 
	Includes references but of course is NAMED after it
	It appears to be used in misc/all.py and rings/polynomial/polynomial_compiled.pyx/.pxd, so need to change those in theory

rings/integer.pyx
	Again a couple

rings/laurent_series_ring_element.pyx
	Brief ref

rings/power_series_ring_element.pyx
	Brief ref

rings/polynomial/polynomial_element.pyx
	A couple references

ext/python.pxi
	Quite a few references at the top

rings/real_rqdf.pyx
	One ref, if this is even being kept

structure/parent_old.pyx
	Several references, is this worth fixing?

libs/pari/gen.pyx
	Brief ref

There were some in docs, but presumably that is not worth changing until after the Sphinx change:
ref/module-sage.rings.integer-mod-ring.html
ref/module-sage.rings.laurent-series-ring-element.html
ref/module-sage.rings.padics.tutorial.html
ref/module-sage.rings.polynomial.polynomial-element.html
ref/module-sage.rings.power-series-ring-element.html
ref/node343.html
tut/node53.html (two examples, in SAGE_ROOT/examples/programming/sagex - should that directory be renamed as well?)



---

archive/issue_comments_038851.json:
```json
{
    "body": "Based on 3.3.alpha0",
    "created_at": "2009-02-02T16:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38851",
    "user": "kcrisman"
}
```

Based on 3.3.alpha0



---

archive/issue_comments_038852.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-02T16:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38852",
    "user": "kcrisman"
}
```

Attachment



---

archive/issue_comments_038853.json:
```json
{
    "body": "Positive review. That it touches python.pxi is rather unfortunate, but oh well ....\n\nI guess in the long term we need to convert python.pxi to a pxd.\n\nOne last thing: The \"[with patch, needs review]\" goes to the front of the summary.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T17:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38853",
    "user": "mabshoff"
}
```

Positive review. That it touches python.pxi is rather unfortunate, but oh well ....

I guess in the long term we need to convert python.pxi to a pxd.

One last thing: The "[with patch, needs review]" goes to the front of the summary.

Cheers,

Michael



---

archive/issue_comments_038854.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T17:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38854",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_comments_038855.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T17:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5094",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5094#issuecomment-38855",
    "user": "mabshoff"
}
```

Resolution: fixed
