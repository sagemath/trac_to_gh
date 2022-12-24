# Issue 4739: [with patch, not ready for review] Add support for additive abelian groups

archive/issues_004739.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  robertwb\n\nKeywords: abelian group\n\nSee also #1849 and #3999.\n\nThe patch adds code to the AbelianGroups_class so that additive groups can be created, and are output with additive notation.\n\nFurther doctests are required to show examples of both additive and multiplicative type in every case.  Subgroup creation (which interfaces with GAP) does not yet work.\n\nAs an example (more to come), torsion subgroups of elliptic curves over number fields are now additive.\n\nrobertwb asked to have a look at this even though it is not yet finished, so here it is!\n\nNB I still think that the whole abelian group code needs rewriting (as was started in #1849)!\n\nIssue created by migration from https://trac.sagemath.org/ticket/4739\n\n",
    "created_at": "2008-12-07T22:39:42Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch, not ready for review] Add support for additive abelian groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4739",
    "user": "cremona"
}
```
Assignee: tbd

CC:  robertwb

Keywords: abelian group

See also #1849 and #3999.

The patch adds code to the AbelianGroups_class so that additive groups can be created, and are output with additive notation.

Further doctests are required to show examples of both additive and multiplicative type in every case.  Subgroup creation (which interfaces with GAP) does not yet work.

As an example (more to come), torsion subgroups of elliptic curves over number fields are now additive.

robertwb asked to have a look at this even though it is not yet finished, so here it is!

NB I still think that the whole abelian group code needs rewriting (as was started in #1849)!

Issue created by migration from https://trac.sagemath.org/ticket/4739





---

archive/issue_comments_035779.json:
```json
{
    "body": "Attachment [abgr.patch](tarball://root/attachments/some-uuid/ticket4739/abgr.patch) by cremona created at 2008-12-07 22:41:25\n\nApplies to 3.2.1 after #3810 and #4061 patches.",
    "created_at": "2008-12-07T22:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35779",
    "user": "cremona"
}
```

Attachment [abgr.patch](tarball://root/attachments/some-uuid/ticket4739/abgr.patch) by cremona created at 2008-12-07 22:41:25

Applies to 3.2.1 after #3810 and #4061 patches.



---

archive/issue_comments_035780.json:
```json
{
    "body": "Hi John,\n\nI haven't look at the code too seriously, but what would be your thoughts on having two subclasses (additive and multiplicative) of a common class for the abelian group elements so that one doesn't need to always do a check for the parent's op_symbol?\n\n--Mike",
    "created_at": "2008-12-08T01:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35780",
    "user": "mhansen"
}
```

Hi John,

I haven't look at the code too seriously, but what would be your thoughts on having two subclasses (additive and multiplicative) of a common class for the abelian group elements so that one doesn't need to always do a check for the parent's op_symbol?

--Mike



---

archive/issue_comments_035781.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> Hi John,\n> \n> I haven't look at the code too seriously, but what would be your thoughts on having two subclasses (additive and multiplicative) of a common class for the abelian group elements so that one doesn't need to always do a check for the parent's op_symbol?\n> \n> --Mike\nThat would be a very good idea indeed.  The way I see it, there is a base abstract class (in which elements are represented as integer vectors, operation is addition with a modulus for each coordinate corresponding to a generator of finite order);  and then there are two possible interfaces to that base class via user classes which are either additive or multiplicative.\n\nWe are surely in a position to provide this structure right now, using the exiting implementations for the base class.  Then the \"major rewrite\" which we keep on mentioning need only apply to the base class.\n\nI'll continue to think about this;  it does not sound any harder, and is probably easier, than what I have been doing so far.",
    "created_at": "2008-12-08T09:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35781",
    "user": "cremona"
}
```

Replying to [comment:1 mhansen]:
> Hi John,
> 
> I haven't look at the code too seriously, but what would be your thoughts on having two subclasses (additive and multiplicative) of a common class for the abelian group elements so that one doesn't need to always do a check for the parent's op_symbol?
> 
> --Mike
That would be a very good idea indeed.  The way I see it, there is a base abstract class (in which elements are represented as integer vectors, operation is addition with a modulus for each coordinate corresponding to a generator of finite order);  and then there are two possible interfaces to that base class via user classes which are either additive or multiplicative.

We are surely in a position to provide this structure right now, using the exiting implementations for the base class.  Then the "major rewrite" which we keep on mentioning need only apply to the base class.

I'll continue to think about this;  it does not sound any harder, and is probably easier, than what I have been doing so far.



---

archive/issue_comments_035782.json:
```json
{
    "body": "I agree with mhansen, always checking parent's op_symbol is probably slow, but I think this can be avoided. \n\nNote that we already have two classes, AdditiveGroupElement and MultiplicativeGroupElement. I think the code here is trying to unify them. both under MultiplicativeGroupElement. Also, note that no typechecking (or coercion) is done for the __add__ and __sub__ commands, so if the left and right operand are not the correct type (or, if both are abelian group elements, but in different groups) then either an error or nonsense will be returned. \n\nFor multiplication, do we really want `a * (1+5+O(5^2))` and `a * \"50\"` to work for a group element a?",
    "created_at": "2008-12-11T10:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35782",
    "user": "robertwb"
}
```

I agree with mhansen, always checking parent's op_symbol is probably slow, but I think this can be avoided. 

Note that we already have two classes, AdditiveGroupElement and MultiplicativeGroupElement. I think the code here is trying to unify them. both under MultiplicativeGroupElement. Also, note that no typechecking (or coercion) is done for the __add__ and __sub__ commands, so if the left and right operand are not the correct type (or, if both are abelian group elements, but in different groups) then either an error or nonsense will be returned. 

For multiplication, do we really want `a * (1+5+O(5^2))` and `a * "50"` to work for a group element a?



---

archive/issue_comments_035783.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-29T13:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35783",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_035784.json:
```json
{
    "body": "Can I propose we resolve this as \"fixed\" now that #6449 has gone in?",
    "created_at": "2010-07-29T13:13:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35784",
    "user": "davidloeffler"
}
```

Can I propose we resolve this as "fixed" now that #6449 has gone in?



---

archive/issue_comments_035785.json:
```json
{
    "body": "Replying to [comment:5 davidloeffler]:\n> Can I propose we resolve this as \"fixed\" now that #6449 has gone in? \n\nThat sounds reasonable to me.  There's no chance that this ancient patch would apply now anyway.",
    "created_at": "2010-07-30T02:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35785",
    "user": "cremona"
}
```

Replying to [comment:5 davidloeffler]:
> Can I propose we resolve this as "fixed" now that #6449 has gone in? 

That sounds reasonable to me.  There's no chance that this ancient patch would apply now anyway.



---

archive/issue_comments_035786.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-30T07:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35786",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_035787.json:
```json
{
    "body": "OK, I'm setting it to \"positive review\" to bring it to the attention of the release manager who can close it.",
    "created_at": "2010-07-30T07:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35787",
    "user": "davidloeffler"
}
```

OK, I'm setting it to "positive review" to bring it to the attention of the release manager who can close it.



---

archive/issue_comments_035788.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-07T06:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35788",
    "user": "mpatel"
}
```

Resolution: duplicate



---

archive/issue_comments_035789.json:
```json
{
    "body": "If no one objects, I'll close this ticket as a \"duplicate.\"",
    "created_at": "2010-08-07T06:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4739#issuecomment-35789",
    "user": "mpatel"
}
```

If no one objects, I'll close this ticket as a "duplicate."
