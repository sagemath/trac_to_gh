# Issue 3974: [with patch, needs review] renaming of integral_weierstrass_model to integral_short_weierstrass_model

archive/issues_003974.json:
```json
{
    "body": "Assignee: @williamstein\n\nI propose a trivial change in the name of integral_weierstrass_model. According to ell_generic.py the terminology is chosen as\n\n> Elliptic curves are always represented by `Weierstass Models' with\n> five coefficients $[a_1,a_2,a_3,a_4,a_6]$ in standard notation.  In\n> Magma, `Weierstrass Model' means a model with a1=a2=a3=0, which is\n> called `Short Weierstrass Model' in Sage; \n\nso consequently the integral_weierstrass_model which gives back a Short Weierstrass Model should be called integral_short_weierstrass_model.\n\nThat is maybe pedantic and a matter of taste, but I believe it would be better.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3974\n\n",
    "created_at": "2008-08-28T12:10:36Z",
    "labels": [
        "number theory",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] renaming of integral_weierstrass_model to integral_short_weierstrass_model",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3974",
    "user": "@categorie"
}
```
Assignee: @williamstein

I propose a trivial change in the name of integral_weierstrass_model. According to ell_generic.py the terminology is chosen as

> Elliptic curves are always represented by `Weierstass Models' with
> five coefficients $[a_1,a_2,a_3,a_4,a_6]$ in standard notation.  In
> Magma, `Weierstrass Model' means a model with a1=a2=a3=0, which is
> called `Short Weierstrass Model' in Sage; 

so consequently the integral_weierstrass_model which gives back a Short Weierstrass Model should be called integral_short_weierstrass_model.

That is maybe pedantic and a matter of taste, but I believe it would be better.

Issue created by migration from https://trac.sagemath.org/ticket/3974





---

archive/issue_comments_028552.json:
```json
{
    "body": "Attachment [sage_trac3974.patch](tarball://root/attachments/some-uuid/ticket3974/sage_trac3974.patch) by @categorie created at 2008-08-28 12:10:49",
    "created_at": "2008-08-28T12:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28552",
    "user": "@categorie"
}
```

Attachment [sage_trac3974.patch](tarball://root/attachments/some-uuid/ticket3974/sage_trac3974.patch) by @categorie created at 2008-08-28 12:10:49



---

archive/issue_comments_028553.json:
```json
{
    "body": "Chris,\n\nintegral_weierstrass_model is part of the public API, so the rename requires that the old function is still available, but using it should throw a deprecation warning. One example is:\n\n```\ndef dynkin_diagram(t):\n    \"\"\"\n    Returns the Dynkin diagram of type t.  \n\n    Note that this function is deprecated, and that you should use DynkinDiagram \n    instead as this will be disappearing in the near future.\n\n    EXAMPLES:\n        sage: dynkin_diagram([\"A\", 3])\n        doctest:1: DeprecationWarning: dynkin_diagram is deprecated, use DynkinDiagram instead!\n        Dynkin diagram of type ['A', 3]\n\n    \"\"\"\n    from sage.misc.misc import deprecation\n    deprecation(\"dynkin_diagram is deprecated, use DynkinDiagram instead!\")\n    return DynkinDiagram(t)\n```\n\nfrom sage/combinat/root_system/dynkin_diagram.py\n\nCheers,\n\nMichael",
    "created_at": "2008-08-28T12:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28553",
    "user": "mabshoff"
}
```

Chris,

integral_weierstrass_model is part of the public API, so the rename requires that the old function is still available, but using it should throw a deprecation warning. One example is:

```
def dynkin_diagram(t):
    """
    Returns the Dynkin diagram of type t.  

    Note that this function is deprecated, and that you should use DynkinDiagram 
    instead as this will be disappearing in the near future.

    EXAMPLES:
        sage: dynkin_diagram(["A", 3])
        doctest:1: DeprecationWarning: dynkin_diagram is deprecated, use DynkinDiagram instead!
        Dynkin diagram of type ['A', 3]

    """
    from sage.misc.misc import deprecation
    deprecation("dynkin_diagram is deprecated, use DynkinDiagram instead!")
    return DynkinDiagram(t)
```

from sage/combinat/root_system/dynkin_diagram.py

Cheers,

Michael



---

archive/issue_comments_028554.json:
```json
{
    "body": "I shall change that. \n\nNevertheless, in my 3.1.1, I can't use\n\n\n```\nfrom sage.misc.misc import deprecation\ndeprecation(\"dynkin_diagram is deprecated, use DynkinDiagram instead!\")\n```\n\n\ninstead looking at dynkin_diagram.py suggests the lines\n\n\n```\nimport warnings\nwarnings.warn(\"integral_weierstrass_model is deprecated, use integral_short_weierstrass_model instead!\", DeprecationWarning, stacklevel=2)\n```\n      \nIs this the proper way of doing ?\nWhen is the 'near future' coming ? \nand do I have to remove it with another patch later ?\n\n(Thanks for the corrections and sorry for my stupid question, but it seems to me that this is the only way for me to learn these things.)\n\nChris.",
    "created_at": "2008-08-29T12:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28554",
    "user": "@categorie"
}
```

I shall change that. 

Nevertheless, in my 3.1.1, I can't use


```
from sage.misc.misc import deprecation
deprecation("dynkin_diagram is deprecated, use DynkinDiagram instead!")
```


instead looking at dynkin_diagram.py suggests the lines


```
import warnings
warnings.warn("integral_weierstrass_model is deprecated, use integral_short_weierstrass_model instead!", DeprecationWarning, stacklevel=2)
```
      
Is this the proper way of doing ?
When is the 'near future' coming ? 
and do I have to remove it with another patch later ?

(Thanks for the corrections and sorry for my stupid question, but it seems to me that this is the only way for me to learn these things.)

Chris.



---

archive/issue_comments_028555.json:
```json
{
    "body": "Sorry I just found the ticket 3654 which answers my question. \nChris.",
    "created_at": "2008-08-29T12:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28555",
    "user": "@categorie"
}
```

Sorry I just found the ticket 3654 which answers my question. 
Chris.



---

archive/issue_comments_028556.json:
```json
{
    "body": "new patch, erplaces the first patch !",
    "created_at": "2008-08-29T13:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28556",
    "user": "@categorie"
}
```

new patch, erplaces the first patch !



---

archive/issue_comments_028557.json:
```json
{
    "body": "Attachment [sage_trac3974_new.patch](tarball://root/attachments/some-uuid/ticket3974/sage_trac3974_new.patch) by @categorie created at 2008-08-29 13:28:56\n\nI changed the patch according to Michael's remark. It replaces the previous patch. This patch only works with the patch from ticket 3654.\n\n Chris.",
    "created_at": "2008-08-29T13:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28557",
    "user": "@categorie"
}
```

Attachment [sage_trac3974_new.patch](tarball://root/attachments/some-uuid/ticket3974/sage_trac3974_new.patch) by @categorie created at 2008-08-29 13:28:56

I changed the patch according to Michael's remark. It replaces the previous patch. This patch only works with the patch from ticket 3654.

 Chris.



---

archive/issue_comments_028558.json:
```json
{
    "body": "I approve of this, though I'm not familiar with how to do the deprecation thing.  Patch applies cleanly to 3.1.2.alpha3,  doctests in sage.schemes.elliptic_curves all ok.",
    "created_at": "2008-09-01T20:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28558",
    "user": "@JohnCremona"
}
```

I approve of this, though I'm not familiar with how to do the deprecation thing.  Patch applies cleanly to 3.1.2.alpha3,  doctests in sage.schemes.elliptic_curves all ok.



---

archive/issue_comments_028559.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-02T11:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28559",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028560.json:
```json
{
    "body": "Merged sage_trac3974_new.patch in Sage 3.1.2.alpha4",
    "created_at": "2008-09-02T11:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3974#issuecomment-28560",
    "user": "mabshoff"
}
```

Merged sage_trac3974_new.patch in Sage 3.1.2.alpha4
