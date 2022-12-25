# Issue 9936: PARI real precision is broken in many ways

archive/issues_009936.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: pari gp real precision set_real_precision\n\nThe following do not work as they should (try these examples with a freshly started copy of Sage, such that everything is default). \n\nThis is definately a bug with the initialization of the precision:\n\n```\n# Default: 2 significant words (while we really should get only 1)\nsage: pari('Pi').debug()\n[&=0000000004fc9620] REAL(lg=4):0400000000000004 (+,expo=1):6000000000000001 c90fdaa22168c234 c4c6628b80dc1cd1\n\n# Change precision and then change it back: we get 1 word\nsage: n = pari.get_real_precision(); pari.set_real_precision(100); pari.set_real_precision(n);\nsage: pari('Pi').debug()\n[&=00000000012bf200] REAL(lg=3):0400000000000003 (+,expo=1):6000000000000001 c90fdaa22168c235\n```\n\n`set_real_precision()` seems to affect essentially only the precision for evaluating strings in PARI and not much else:\n\n```\nsage: pari.set_real_precision(50);\nsage: pari('Euler')   # Precision changes\n0.57721566490153286060651209008240243104215933593992\nsage: pari.euler()    # Precision does NOT change\n0.5772156649015328607\n```\n\nThis last behaviour is actually documented in `sage/libs/pari/gen.pyx`:\n> Unless otherwise indicated in the docstring, most Pari functions\n> that return inexact objects use the precision of their arguments to\n> decide the precision of the computation. However, if some of these\n> arguments happen to be exact numbers (integers, rationals, etc.),\n> an optional parameter indicates the precision (in bits) to which\n> these arguments should be converted before the computation. If this\n> precision parameter is missing, the **default precision of 53 bits** is\n> used.\n\n\nIn other words, the default precision is an unchangable 53 bits. I would expect `set_real_precision()` to change this.  This is also trivial to implement since the global variable `prec` is already there (and initialized once and for all to 53).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9937\n\n",
    "closed_at": "2017-02-21T07:56:21Z",
    "created_at": "2010-09-17T20:48:18Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "PARI real precision is broken in many ways",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9936",
    "user": "https://github.com/jdemeyer"
}
```
Assignee: @williamstein

Keywords: pari gp real precision set_real_precision

The following do not work as they should (try these examples with a freshly started copy of Sage, such that everything is default). 

This is definately a bug with the initialization of the precision:

```
# Default: 2 significant words (while we really should get only 1)
sage: pari('Pi').debug()
[&=0000000004fc9620] REAL(lg=4):0400000000000004 (+,expo=1):6000000000000001 c90fdaa22168c234 c4c6628b80dc1cd1

# Change precision and then change it back: we get 1 word
sage: n = pari.get_real_precision(); pari.set_real_precision(100); pari.set_real_precision(n);
sage: pari('Pi').debug()
[&=00000000012bf200] REAL(lg=3):0400000000000003 (+,expo=1):6000000000000001 c90fdaa22168c235
```

`set_real_precision()` seems to affect essentially only the precision for evaluating strings in PARI and not much else:

```
sage: pari.set_real_precision(50);
sage: pari('Euler')   # Precision changes
0.57721566490153286060651209008240243104215933593992
sage: pari.euler()    # Precision does NOT change
0.5772156649015328607
```

This last behaviour is actually documented in `sage/libs/pari/gen.pyx`:
> Unless otherwise indicated in the docstring, most Pari functions
> that return inexact objects use the precision of their arguments to
> decide the precision of the computation. However, if some of these
> arguments happen to be exact numbers (integers, rationals, etc.),
> an optional parameter indicates the precision (in bits) to which
> these arguments should be converted before the computation. If this
> precision parameter is missing, the **default precision of 53 bits** is
> used.


In other words, the default precision is an unchangable 53 bits. I would expect `set_real_precision()` to change this.  This is also trivial to implement since the global variable `prec` is already there (and initialized once and for all to 53).

Issue created by migration from https://trac.sagemath.org/ticket/9937





---

archive/issue_comments_098759.json:
```json
{
    "body": "Changing keywords from \"pari gp real precision\" to \"pari gp real precision set_real_precision\".",
    "created_at": "2010-09-17T21:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9936#issuecomment-98759",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "pari gp real precision" to "pari gp real precision set_real_precision".



---

archive/issue_comments_098760.json:
```json
{
    "body": "There's a lot of relevant information written by Alex Ghitza and me a couple of years ago in the file gen.pyx.  Yes, it is counterintuitive;  but not undocumented.",
    "created_at": "2010-09-21T20:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9936#issuecomment-98760",
    "user": "https://github.com/JohnCremona"
}
```

There's a lot of relevant information written by Alex Ghitza and me a couple of years ago in the file gen.pyx.  Yes, it is counterintuitive;  but not undocumented.



---

archive/issue_comments_098761.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> There's a lot of relevant information written by Alex Ghitza and me a couple of years ago in the file gen.pyx.  Yes, it is counterintuitive;  but not undocumented.\n\n\nI know it is documented (although not too clearly), but the question is: does it make sense?  (In my opinion: no).",
    "created_at": "2010-09-21T20:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9936#issuecomment-98761",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:3 cremona]:
> There's a lot of relevant information written by Alex Ghitza and me a couple of years ago in the file gen.pyx.  Yes, it is counterintuitive;  but not undocumented.


I know it is documented (although not too clearly), but the question is: does it make sense?  (In my opinion: no).



---

archive/issue_comments_098762.json:
```json
{
    "body": "More precisely: this is counter-intuitive:\n\n```\nsage: pari.set_real_precision(100);\nsage: pari('Euler')   # Precision changes\n0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495\nsage: pari.euler()    # Precision does NOT change\n0.5772156649015328607\n```",
    "created_at": "2010-09-21T20:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9936#issuecomment-98762",
    "user": "https://github.com/jdemeyer"
}
```

More precisely: this is counter-intuitive:

```
sage: pari.set_real_precision(100);
sage: pari('Euler')   # Precision changes
0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495
sage: pari.euler()    # Precision does NOT change
0.5772156649015328607
```



---

archive/issue_comments_098763.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-04-14T20:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9936#issuecomment-98763",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_events_025064.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-30T21:40:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9936#event-25064"
}
```



---

archive/issue_comments_098764.json:
```json
{
    "body": "Attachment [9937_pari_prec.patch](tarball://root/attachments/some-uuid/ticket9937/9937_pari_prec.patch) by @jdemeyer created at 2012-04-29 14:01:45",
    "created_at": "2012-04-29T14:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9936#issuecomment-98764",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9937_pari_prec.patch](tarball://root/attachments/some-uuid/ticket9937/9937_pari_prec.patch) by @jdemeyer created at 2012-04-29 14:01:45



---

archive/issue_comments_098765.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-02-21T07:56:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9936#issuecomment-98765",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_events_025065.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-02-21T07:56:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9936#event-25065"
}
```



---

archive/issue_events_025066.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-02-21T07:56:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9936#event-25066"
}
```



---

archive/issue_events_025067.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-02-21T07:56:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9936",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9936#event-25067"
}
```
