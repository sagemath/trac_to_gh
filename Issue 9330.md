# Issue 9330: Documentation for sha_tate.py not quite looking right

archive/issues_009330.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @jhpalmieri\n\nWhen you look at [this](http://www.sagemath.org/doc/reference/sage/schemes/elliptic_curves/sha_tate.html), there are a number of things wrong or confusing in the documentation.\n\nMost importantly, several instances of Sha should have ticks, probably.  But are they referring to the mathematical object \n\n```\n`Sha`\n```\nor the computer structure of the class\n\n```\n``Sha``\n```\n?  If I knew what was intended (given that the distinction is quite small), I would do this patch myself.  But it looks like sometimes the group is intended, other times the class object.\n\nIn line 198, \n\n```\n You can increase the `descent_second_limit` (in the above example\n```\nshould have double ticks.\n\nWe also get the following warning:\n\n```\nsage-4.4.4/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.py:docstring of sage.schemes.elliptic_curves.sha_tate.Sha.bound_kato:12: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n```\nthis probably refers to \n\n```\n       THEOREM (Kato): Suppose `L(E,1) \\neq 0` and `p \\neq 2, 3` is a prime such that\n            - `E` does not have additive reduction at `p`,\n            - the mod-`p` representation is surjective.\n       Then `{ord}_p(\\#Sha(E))` divides `{ord}_p(L(E,1)\\cdot\\#E(\\QQ)_{tor}^2/(\\Omega_E \\cdot \\prod c_q))`.\n```\nbut I'm not sure.\n\nIn line 756 we have \n\n```\nWe get no information the curve has rank 2.::\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9330\n\n",
    "created_at": "2010-06-24T15:55:55Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Documentation for sha_tate.py not quite looking right",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9330",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @JohnCremona

CC:  @jhpalmieri

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

archive/issue_comments_087865.json:
```json
{
    "body": "Is there any reason we cannot use the proper cyrillic font for Sha?\n\n\\newcommand{\\Sha}{{\\mbox{\\textcyr{Sh}}}}",
    "created_at": "2010-06-24T16:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87865",
    "user": "https://github.com/JohnCremona"
}
```

Is there any reason we cannot use the proper cyrillic font for Sha?

\newcommand{\Sha}{{\mbox{\textcyr{Sh}}}}



---

archive/issue_comments_087866.json:
```json
{
    "body": "Does jsmath support this?  Otherwise one would have to do the right encoding.  Anyway, it looks like my job here is done - interest has been piqued ;)",
    "created_at": "2010-06-24T16:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87866",
    "user": "https://github.com/kcrisman"
}
```

Does jsmath support this?  Otherwise one would have to do the right encoding.  Anyway, it looks like my job here is done - interest has been piqued ;)



---

archive/issue_comments_087867.json:
```json
{
    "body": "See #9442 for the warning when building the reference manual.",
    "created_at": "2010-07-06T22:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87867",
    "user": "https://github.com/jhpalmieri"
}
```

See #9442 for the warning when building the reference manual.



---

archive/issue_comments_087868.json:
```json
{
    "body": "Attachment [trac_9330.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330.patch) by @categorie created at 2010-07-28 15:36:22\n\nexported against 4.5.2.alpha1",
    "created_at": "2010-07-28T15:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87868",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9330.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330.patch) by @categorie created at 2010-07-28 15:36:22

exported against 4.5.2.alpha1



---

archive/issue_comments_087869.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T15:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87869",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087870.json:
```json
{
    "body": "I changed Sha to `Sha` thoughout the document as it should be. There should be a better solution for this. Alas the unicode letter \u0428 does not work in the pdf version (it works fine in the html). The \\textcyr does not seem to work with LaTeX either. Probably it needs addtional fonts or so and I would object to include them just because of this one letter.\n\nSo I think this is as far as I can do the changes.\n\nI also renamed constistantly the group as Tate-Shafarevich and not Shafarevich-Tate. (There is a debate about this, which I do not want to see repeated here. google tells me that T-S is more frequent.)",
    "created_at": "2010-07-28T15:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87870",
    "user": "https://github.com/categorie"
}
```

I changed Sha to `Sha` thoughout the document as it should be. There should be a better solution for this. Alas the unicode letter Ш does not work in the pdf version (it works fine in the html). The \textcyr does not seem to work with LaTeX either. Probably it needs addtional fonts or so and I would object to include them just because of this one letter.

So I think this is as far as I can do the changes.

I also renamed constistantly the group as Tate-Shafarevich and not Shafarevich-Tate. (There is a debate about this, which I do not want to see repeated here. google tells me that T-S is more frequent.)



---

archive/issue_comments_087871.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-28T15:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87871",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087872.json:
```json
{
    "body": "There are a few other things in the Description which need to be taken care of; in the first case, it's to add double ticks, and in the second it's (probably) to add the word 'when'.   \n\nI removed the issue from #9442 from the Description since that is already merged in rc0 - one will probably have to rebase (very slightly) against 4.5.2.rc0 or 4.5.2, since that has been merged.  Once that's done (and once I build one of those) I'll also check whether it looks right, but from a cursory glance this looks like a great improvement (and in consistency!).  Or jhpalmieri can do it :)",
    "created_at": "2010-07-28T15:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87872",
    "user": "https://github.com/kcrisman"
}
```

There are a few other things in the Description which need to be taken care of; in the first case, it's to add double ticks, and in the second it's (probably) to add the word 'when'.   

I removed the issue from #9442 from the Description since that is already merged in rc0 - one will probably have to rebase (very slightly) against 4.5.2.rc0 or 4.5.2, since that has been merged.  Once that's done (and once I build one of those) I'll also check whether it looks right, but from a cursory glance this looks like a great improvement (and in consistency!).  Or jhpalmieri can do it :)



---

archive/issue_comments_087873.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-28T16:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87873",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087874.json:
```json
{
    "body": "I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.\n\nIt should always be `Sha` never ``Sha``.\n\nI believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.",
    "created_at": "2010-07-28T16:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87874",
    "user": "https://github.com/categorie"
}
```

I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.

It should always be `Sha` never ``Sha``.

I believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.



---

archive/issue_comments_087875.json:
```json
{
    "body": "Oops the ` went away. I meant\n\nIt should always be ``Sha`` never ```Sha```",
    "created_at": "2010-07-28T16:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87875",
    "user": "https://github.com/categorie"
}
```

Oops the ` went away. I meant

It should always be ``Sha`` never ```Sha```



---

archive/issue_comments_087876.json:
```json
{
    "body": "Replying to [comment:6 wuthrich]:\n> I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.\n\n\nYes, sorry I didn't see that - I've changed the description.  What is up with the \"We get no information the \" bit?  Maybe this is grammatically correct in the context of Tate-Shaf groups?  \n\nIncidentally, though you changed the references to T-S, the file is S-T :)  Oh well; maybe that's as it should be if there isn't agreement.\n\n> It should always be `Sha` never ``Sha``.\n> \n> I believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.\n\n\nUnfortunately I can't check this right now either, but if someone else doesn't, I'll do so soon.",
    "created_at": "2010-07-28T17:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87876",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_087877.json:
```json
{
    "body": "exported against 4.5.2.alpha1, to be apply after trac_9330.patch",
    "created_at": "2010-07-29T09:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87877",
    "user": "https://github.com/categorie"
}
```

exported against 4.5.2.alpha1, to be apply after trac_9330.patch



---

archive/issue_comments_087878.json:
```json
{
    "body": "Attachment [trac_9330_2.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330_2.patch) by @categorie created at 2010-07-29 10:06:37\n\nYop, sorry, I did not see that the 'when' was still missing. Here is an additional patch.\n\nLuckily the filename is not visible to the user, so I don't have to bother changing it. ... and it gives some voice to the other order.\n\nThere is no problem with the rebase, because the patches here are exported against 4.5.2.alpha1 and #9442 was merged in 4.5.alpha4 if I am not mistaken. At least the addition lines are clearly in the file before I edited it.",
    "created_at": "2010-07-29T10:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87878",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_9330_2.patch](tarball://root/attachments/some-uuid/ticket9330/trac_9330_2.patch) by @categorie created at 2010-07-29 10:06:37

Yop, sorry, I did not see that the 'when' was still missing. Here is an additional patch.

Luckily the filename is not visible to the user, so I don't have to bother changing it. ... and it gives some voice to the other order.

There is no problem with the rebase, because the patches here are exported against 4.5.2.alpha1 and #9442 was merged in 4.5.alpha4 if I am not mistaken. At least the addition lines are clearly in the file before I edited it.



---

archive/issue_comments_087879.json:
```json
{
    "body": "Unfortunately, I can't get this to work right when doing `sage-docbuild reference html` on my computer (probably due to latex not being in my PATH).  Someone else will have to review it, though it seems good!",
    "created_at": "2010-07-29T19:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87879",
    "user": "https://github.com/kcrisman"
}
```

Unfortunately, I can't get this to work right when doing `sage-docbuild reference html` on my computer (probably due to latex not being in my PATH).  Someone else will have to review it, though it seems good!



---

archive/issue_comments_087880.json:
```json
{
    "body": "I figured out how to get my latex in my PATH finally.  There are a few things which *could* be put in ticks or double ticks still, but not ones I feel are necessary at this point, more ambiguous - and none related to Sha.  Positive review",
    "created_at": "2010-08-11T19:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87880",
    "user": "https://github.com/kcrisman"
}
```

I figured out how to get my latex in my PATH finally.  There are a few things which *could* be put in ticks or double ticks still, but not ones I feel are necessary at this point, more ambiguous - and none related to Sha.  Positive review



---

archive/issue_comments_087881.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-11T19:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87881",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087882.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87882",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_022996.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T11:38:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9330#event-22996"
}
```



---

archive/issue_comments_087883.json:
```json
{
    "body": "These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).\n\nI don't know if there's a separate ticket for this.",
    "created_at": "2010-09-16T08:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87883",
    "user": "https://github.com/nexttime"
}
```

These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).

I don't know if there's a separate ticket for this.



---

archive/issue_comments_087884.json:
```json
{
    "body": "Replying to [comment:14 leif]:\n> These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).\n> \n> I don't know if there's a separate ticket for this.\n\n\nI've opened #9916 for that. Patch needs review.",
    "created_at": "2010-09-16T09:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9330#issuecomment-87884",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:14 leif]:
> These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (*Shafarevich-Tate* -> *Tate-Shafarevich*).
> 
> I don't know if there's a separate ticket for this.


I've opened #9916 for that. Patch needs review.
