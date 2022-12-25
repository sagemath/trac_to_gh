# Issue 9758: Addition of SI prefixes capabilities to the units module

archive/issues_009758.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @rbeezer @williamstein\n\nKeywords: sd40.5\n\nAlthough the units module already has a si_prefixes component, it's not very convenient, since you have to do units.si_prefixes.nano*units.mass.gram, and you get something like \"gram*nano\" that doesn't look very well.\nThis ticket is a modification that adds properties named as the components of units.si_prefixes, so that calling something like units.mass.gram.nano will create a units.mass.nanogram element and return it.\n\nDuplicate of #9778.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9759\n\n",
    "closed_at": "2012-06-02T12:47:05Z",
    "created_at": "2010-08-17T22:51:22Z",
    "labels": [
        "component: symbolics",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Addition of SI prefixes capabilities to the units module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9758",
    "user": "https://github.com/cousteaulecommandant"
}
```
Assignee: @burcin

CC:  @rbeezer @williamstein

Keywords: sd40.5

Although the units module already has a si_prefixes component, it's not very convenient, since you have to do units.si_prefixes.nano*units.mass.gram, and you get something like "gram*nano" that doesn't look very well.
This ticket is a modification that adds properties named as the components of units.si_prefixes, so that calling something like units.mass.gram.nano will create a units.mass.nanogram element and return it.

Duplicate of #9778.

Issue created by migration from https://trac.sagemath.org/ticket/9759





---

archive/issue_comments_095421.json:
```json
{
    "body": "Attachment [trac_9759_si_prefixes.patch](tarball://root/attachments/some-uuid/ticket9759/trac_9759_si_prefixes.patch) by @cousteaulecommandant created at 2010-08-17 23:07:29\n\nPatch that adds components of units.si_prefixes as properties on the UnitExpression class",
    "created_at": "2010-08-17T23:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95421",
    "user": "https://github.com/cousteaulecommandant"
}
```

Attachment [trac_9759_si_prefixes.patch](tarball://root/attachments/some-uuid/ticket9759/trac_9759_si_prefixes.patch) by @cousteaulecommandant created at 2010-08-17 23:07:29

Patch that adds components of units.si_prefixes as properties on the UnitExpression class



---

archive/issue_comments_095422.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-17T23:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95422",
    "user": "https://github.com/cousteaulecommandant"
}
```

Changing status from new to needs_review.



---

archive/issue_events_024452.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2011-05-10T18:54:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9758#event-24452"
}
```



---

archive/issue_comments_095423.json:
```json
{
    "body": "The patch looks good to me. It is a hack and I am not really happy with the use of `sage_eval()`, but this seems to be used everywhere in `sage/symbolic/units.py`. I'm ready to give a positive review, though it would be better if somebody who actually uses this module comments on the improvement.\n\nWhy does the new function name start with an underscore? Wouldn't it be easier to find it if was just named `si_prefix()`?",
    "created_at": "2011-05-10T18:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95423",
    "user": "https://github.com/burcin"
}
```

The patch looks good to me. It is a hack and I am not really happy with the use of `sage_eval()`, but this seems to be used everywhere in `sage/symbolic/units.py`. I'm ready to give a positive review, though it would be better if somebody who actually uses this module comments on the improvement.

Why does the new function name start with an underscore? Wouldn't it be easier to find it if was just named `si_prefix()`?



---

archive/issue_comments_095424.json:
```json
{
    "body": "The truth is that this patch was created as a suggestion done in #sage-devel; it was done pretty fast and probably not elegantly. I later submitted another patch with a better implementation (see ticket #9778), which also added the basics for `LaTeX` representation of the units.\n\n(I also made the alternate \"metrology\" module on #9763, which also has LaTeX and units support)",
    "created_at": "2011-05-10T19:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95424",
    "user": "https://github.com/cousteaulecommandant"
}
```

The truth is that this patch was created as a suggestion done in #sage-devel; it was done pretty fast and probably not elegantly. I later submitted another patch with a better implementation (see ticket #9778), which also added the basics for `LaTeX` representation of the units.

(I also made the alternate "metrology" module on #9763, which also has LaTeX and units support)



---

archive/issue_comments_095425.json:
```json
{
    "body": "I agree with Burcin that this is a bit hackish.  \n> The truth is that this patch was created as a suggestion done in #sage-devel; it was done pretty fast and probably not elegantly. I later submitted another patch with a better implementation (see ticket #9778), which also added the basics for `LaTeX` representation of the units.\n\nSo should this be closed in favor of #9778?\n\nAlso, \n\n```\ndef _add_si_property_(prefix): \n \t    setattr(UnitExpression, prefix, property(lambda self: self._si_prefix_(prefix))) \n \nfor prefix in unitdict['si_prefixes']: \n     _add_si_property_(prefix) \n```\nseems to be missing a doctest in the underscore function.",
    "created_at": "2012-05-26T07:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95425",
    "user": "https://github.com/kcrisman"
}
```

I agree with Burcin that this is a bit hackish.  
> The truth is that this patch was created as a suggestion done in #sage-devel; it was done pretty fast and probably not elegantly. I later submitted another patch with a better implementation (see ticket #9778), which also added the basics for `LaTeX` representation of the units.

So should this be closed in favor of #9778?

Also, 

```
def _add_si_property_(prefix): 
 	    setattr(UnitExpression, prefix, property(lambda self: self._si_prefix_(prefix))) 
 
for prefix in unitdict['si_prefixes']: 
     _add_si_property_(prefix) 
```
seems to be missing a doctest in the underscore function.



---

archive/issue_comments_095426.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-05-26T07:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95426",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095427.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-26T07:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95427",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_095428.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> So should this be closed in favor of #9778?\n\nI think it'd be a good idea.",
    "created_at": "2012-05-28T14:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95428",
    "user": "https://github.com/cousteaulecommandant"
}
```

Replying to [comment:6 kcrisman]:
> So should this be closed in favor of #9778?

I think it'd be a good idea.



---

archive/issue_comments_095429.json:
```json
{
    "body": "> > So should this be closed in favor of #9778?\n\n> I think it'd be a good idea.\nOkay, I'll make a comment there to that effect.",
    "created_at": "2012-05-28T15:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95429",
    "user": "https://github.com/kcrisman"
}
```

> > So should this be closed in favor of #9778?

> I think it'd be a good idea.
Okay, I'll make a comment there to that effect.



---

archive/issue_comments_095430.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-28T15:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95430",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_024453.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-05-28T15:49:43Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9758#event-24453"
}
```



---

archive/issue_events_024454.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-05-28T15:49:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9758#event-24454"
}
```



---

archive/issue_events_024455.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-02T12:47:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9758#event-24455"
}
```



---

archive/issue_comments_095431.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-02T12:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9758",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9758#issuecomment-95431",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
