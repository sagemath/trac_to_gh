# Issue 9330: Documentation for sha_tate.py not quite looking right

archive/issues_009330.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  jhpalmieri\n\nWhen you look at [this](http://www.sagemath.org/doc/reference/sage/schemes/elliptic_curves/sha_tate.html), there are a number of things wrong or confusing in the documentation.\n\nMost importantly, several instances of Sha should have ticks, probably.  But are they referring to the mathematical object \n\n```\n`Sha`\n```\n\nor the computer structure of the class\n\n```\n``Sha``\n```\n\n?  If I knew what was intended (given that the distinction is quite small), I would do this patch myself.  But it looks like sometimes the group is intended, other times the class object.\n\nIn line 198, \n\n```\n You can increase the `descent_second_limit` (in the above example\n```\n\nshould have double ticks.\n\nWe also get the following warning:\n\n```\nsage-4.4.4/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.py:docstring of sage.schemes.elliptic_curves.sha_tate.Sha.bound_kato:12: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n```\n\nthis probably refers to \n\n```\n       THEOREM (Kato): Suppose `L(E,1) \\neq 0` and `p \\neq 2, 3` is a prime such that\n            - `E` does not have additive reduction at `p`,\n            - the mod-`p` representation is surjective.\n       Then `{ord}_p(\\#Sha(E))` divides `{ord}_p(L(E,1)\\cdot\\#E(\\QQ)_{tor}^2/(\\Omega_E \\cdot \\prod c_q))`.\n```\n\nbut I'm not sure.\n\nIn line 756 we have \n\n```\nWe get no information the curve has rank 2.::\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9330\n\n",
    "created_at": "2010-06-24T15:55:55Z",
    "labels": [
        "elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Documentation for sha_tate.py not quite looking right",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9330",
    "user": "kcrisman"
}
```
Assignee: cremona

CC:  jhpalmieri

When you look at [this](http://www.sagemath.org/doc/reference/sage/schemes/elliptic_curves/sha_tate.html), there are a number of things wrong or confusing in the documentation.

Most importantly, several instances of Sha should have ticks, probably.  But are they referring to the mathematical object 

```
`Sha`
```

or the computer structure of the class

```
``Sha``
```

?  If I knew what was intended (given that the distinction is quite small), I would do this patch myself.  But it looks like sometimes the group is intended, other times the class object.

In line 198, 

```
 You can increase the `descent_second_limit` (in the above example
```

should have double ticks.

We also get the following warning:

```
sage-4.4.4/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.py:docstring of sage.schemes.elliptic_curves.sha_tate.Sha.bound_kato:12: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```

this probably refers to 

```
       THEOREM (Kato): Suppose `L(E,1) \neq 0` and `p \neq 2, 3` is a prime such that
            - `E` does not have additive reduction at `p`,
            - the mod-`p` representation is surjective.
       Then `{ord}_p(\#Sha(E))` divides `{ord}_p(L(E,1)\cdot\#E(\QQ)_{tor}^2/(\Omega_E \cdot \prod c_q))`.
```

but I'm not sure.

In line 756 we have 

```
We get no information the curve has rank 2.::
```


Issue created by migration from https://trac.sagemath.org/ticket/9330





---

archive/issue_comments_088004.json:
```json
{
    "body": "Is there any reason we cannot use the proper cyrillic font for Sha?\n\n\\newcommand{\\Sha}{{\\mbox{\\textcyr{Sh}}}}",
    "created_at": "2010-06-24T16:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88004",
    "user": "cremona"
}
```

Is there any reason we cannot use the proper cyrillic font for Sha?

\newcommand{\Sha}{{\mbox{\textcyr{Sh}}}}



---

archive/issue_comments_088005.json:
```json
{
    "body": "Does jsmath support this?  Otherwise one would have to do the right encoding.  Anyway, it looks like my job here is done - interest has been piqued ;)",
    "created_at": "2010-06-24T16:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88005",
    "user": "kcrisman"
}
```

Does jsmath support this?  Otherwise one would have to do the right encoding.  Anyway, it looks like my job here is done - interest has been piqued ;)



---

archive/issue_comments_088006.json:
```json
{
    "body": "See #9442 for the warning when building the reference manual.",
    "created_at": "2010-07-06T22:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88006",
    "user": "jhpalmieri"
}
```

See #9442 for the warning when building the reference manual.



---

archive/issue_comments_088007.json:
```json
{
    "body": "Attachment [trac_9330.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330.patch) by wuthrich created at 2010-07-28 15:36:22\n\nexported against 4.5.2.alpha1",
    "created_at": "2010-07-28T15:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88007",
    "user": "wuthrich"
}
```

Attachment [trac_9330.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330.patch) by wuthrich created at 2010-07-28 15:36:22

exported against 4.5.2.alpha1



---

archive/issue_comments_088008.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T15:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88008",
    "user": "wuthrich"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088009.json:
```json
{
    "body": "I changed Sha to `Sha` thoughout the document as it should be. There should be a better solution for this. Alas the unicode letter \u0428 does not work in the pdf version (it works fine in the html). The \\textcyr does not seem to work with LaTeX either. Probably it needs addtional fonts or so and I would object to include them just because of this one letter.\n\nSo I think this is as far as I can do the changes.\n\nI also renamed constistantly the group as Tate-Shafarevich and not Shafarevich-Tate. (There is a debate about this, which I do not want to see repeated here. google tells me that T-S is more frequent.)",
    "created_at": "2010-07-28T15:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88009",
    "user": "wuthrich"
}
```

I changed Sha to `Sha` thoughout the document as it should be. There should be a better solution for this. Alas the unicode letter Ш does not work in the pdf version (it works fine in the html). The \textcyr does not seem to work with LaTeX either. Probably it needs addtional fonts or so and I would object to include them just because of this one letter.

So I think this is as far as I can do the changes.

I also renamed constistantly the group as Tate-Shafarevich and not Shafarevich-Tate. (There is a debate about this, which I do not want to see repeated here. google tells me that T-S is more frequent.)



---

archive/issue_comments_088010.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-28T15:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88010",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088011.json:
```json
{
    "body": "There are a few other things in the Description which need to be taken care of; in the first case, it's to add double ticks, and in the second it's (probably) to add the word 'when'.   \n\nI removed the issue from #9442 from the Description since that is already merged in rc0 - one will probably have to rebase (very slightly) against 4.5.2.rc0 or 4.5.2, since that has been merged.  Once that's done (and once I build one of those) I'll also check whether it looks right, but from a cursory glance this looks like a great improvement (and in consistency!).  Or jhpalmieri can do it :)",
    "created_at": "2010-07-28T15:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88011",
    "user": "kcrisman"
}
```

There are a few other things in the Description which need to be taken care of; in the first case, it's to add double ticks, and in the second it's (probably) to add the word 'when'.   

I removed the issue from #9442 from the Description since that is already merged in rc0 - one will probably have to rebase (very slightly) against 4.5.2.rc0 or 4.5.2, since that has been merged.  Once that's done (and once I build one of those) I'll also check whether it looks right, but from a cursory glance this looks like a great improvement (and in consistency!).  Or jhpalmieri can do it :)



---

archive/issue_comments_088012.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-28T16:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88012",
    "user": "wuthrich"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088013.json:
```json
{
    "body": "I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.\n\nIt should always be `Sha` never ``Sha``.\n\nI believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.",
    "created_at": "2010-07-28T16:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88013",
    "user": "wuthrich"
}
```

I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.

It should always be `Sha` never ``Sha``.

I believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.



---

archive/issue_comments_088014.json:
```json
{
    "body": "Oops the ` went away. I meant\n\nIt should always be ``Sha`` never ```Sha```",
    "created_at": "2010-07-28T16:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88014",
    "user": "wuthrich"
}
```

Oops the ` went away. I meant

It should always be ``Sha`` never ```Sha```



---

archive/issue_comments_088015.json:
```json
{
    "body": "Replying to [comment:6 wuthrich]:\n> I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.\n\nYes, sorry I didn't see that - I've changed the description.  What is up with the \"We get no information the \" bit?  Maybe this is grammatically correct in the context of Tate-Shaf groups?  \n\nIncidentally, though you changed the references to T-S, the file is S-T :)  Oh well; maybe that's as it should be if there isn't agreement.\n\n> It should always be `Sha` never ``Sha``.\n> \n> I believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.\n\nUnfortunately I can't check this right now either, but if someone else doesn't, I'll do so soon.",
    "created_at": "2010-07-28T17:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88015",
    "user": "kcrisman"
}
```

Replying to [comment:6 wuthrich]:
> I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.

Yes, sorry I didn't see that - I've changed the description.  What is up with the "We get no information the " bit?  Maybe this is grammatically correct in the context of Tate-Shaf groups?  

Incidentally, though you changed the references to T-S, the file is S-T :)  Oh well; maybe that's as it should be if there isn't agreement.

> It should always be `Sha` never ``Sha``.
> 
> I believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.

Unfortunately I can't check this right now either, but if someone else doesn't, I'll do so soon.



---

archive/issue_comments_088016.json:
```json
{
    "body": "exported against 4.5.2.alpha1, to be apply after trac_9330.patch",
    "created_at": "2010-07-29T09:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88016",
    "user": "wuthrich"
}
```

exported against 4.5.2.alpha1, to be apply after trac_9330.patch



---

archive/issue_comments_088017.json:
```json
{
    "body": "Attachment [trac_9330_2.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330_2.patch) by wuthrich created at 2010-07-29 10:06:37\n\nYop, sorry, I did not see that the 'when' was still missing. Here is an additional patch.\n\nLuckily the filename is not visible to the user, so I don't have to bother changing it. ... and it gives some voice to the other order.\n\nThere is no problem with the rebase, because the patches here are exported against 4.5.2.alpha1 and #9442 was merged in 4.5.alpha4 if I am not mistaken. At least the addition lines are clearly in the file before I edited it.",
    "created_at": "2010-07-29T10:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88017",
    "user": "wuthrich"
}
```

Attachment [trac_9330_2.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330_2.patch) by wuthrich created at 2010-07-29 10:06:37

Yop, sorry, I did not see that the 'when' was still missing. Here is an additional patch.

Luckily the filename is not visible to the user, so I don't have to bother changing it. ... and it gives some voice to the other order.

There is no problem with the rebase, because the patches here are exported against 4.5.2.alpha1 and #9442 was merged in 4.5.alpha4 if I am not mistaken. At least the addition lines are clearly in the file before I edited it.



---

archive/issue_comments_088018.json:
```json
{
    "body": "Unfortunately, I can't get this to work right when doing `sage-docbuild reference html` on my computer (probably due to latex not being in my PATH).  Someone else will have to review it, though it seems good!",
    "created_at": "2010-07-29T19:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88018",
    "user": "kcrisman"
}
```

Unfortunately, I can't get this to work right when doing `sage-docbuild reference html` on my computer (probably due to latex not being in my PATH).  Someone else will have to review it, though it seems good!



---

archive/issue_comments_088019.json:
```json
{
    "body": "I figured out how to get my latex in my PATH finally.  There are a few things which *could* be put in ticks or double ticks still, but not ones I feel are necessary at this point, more ambiguous - and none related to Sha.  Positive review",
    "created_at": "2010-08-11T19:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88019",
    "user": "kcrisman"
}
```

I figured out how to get my latex in my PATH finally.  There are a few things which *could* be put in ticks or double ticks still, but not ones I feel are necessary at this point, more ambiguous - and none related to Sha.  Positive review



---

archive/issue_comments_088020.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-11T19:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88020",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88021",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_088022.json:
```json
{
    "body": "These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).\n\nI don't know if there's a separate ticket for this.",
    "created_at": "2010-09-16T08:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88022",
    "user": "leif"
}
```

These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).

I don't know if there's a separate ticket for this.



---

archive/issue_comments_088023.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).\n> \n> I don't know if there's a separate ticket for this.\n\nI've opened #9916 for that. Patch needs review.",
    "created_at": "2010-09-16T09:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-88023",
    "user": "leif"
}
```

Replying to [comment:14 leif]:
> These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).
> 
> I don't know if there's a separate ticket for this.

I've opened #9916 for that. Patch needs review.
