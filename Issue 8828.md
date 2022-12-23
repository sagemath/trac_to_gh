# Issue 8828: Lower height bound for elliptic curves

archive/issues_008828.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  pbruin\n\nImplements Cremona and and Samir Siksek's algorithm for computing lower bounds on canonical heights, with Nook's extensions to number fields. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8828\n\n",
    "created_at": "2010-04-30T06:44:34Z",
    "labels": [
        "elliptic curves",
        "major",
        "enhancement"
    ],
    "title": "Lower height bound for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8828",
    "user": "robertwb"
}
```
Assignee: cremona

CC:  pbruin

Implements Cremona and and Samir Siksek's algorithm for computing lower bounds on canonical heights, with Nook's extensions to number fields. 

Issue created by migration from https://trac.sagemath.org/ticket/8828





---

archive/issue_comments_081062.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-30T06:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81062",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_081063.json:
```json
{
    "body": "It works fine, but is still missing documentation and doctests.",
    "created_at": "2010-04-30T06:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81063",
    "user": "robertwb"
}
```

It works fine, but is still missing documentation and doctests.



---

archive/issue_comments_081064.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-30T06:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81064",
    "user": "robertwb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081065.json:
```json
{
    "body": "Depends on #8535 and #8818 at least.",
    "created_at": "2010-04-30T06:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81065",
    "user": "robertwb"
}
```

Depends on #8535 and #8818 at least.



---

archive/issue_comments_081066.json:
```json
{
    "body": "I am about to convert this patch to a new git branch based on the 6.1 develop branch, in an attempt to revive the code and get it finished.  Note that this is a prerequisite for the related #8829.",
    "created_at": "2014-01-02T12:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81066",
    "user": "cremona"
}
```

I am about to convert this patch to a new git branch based on the 6.1 develop branch, in an attempt to revive the code and get it finished.  Note that this is a prerequisite for the related #8829.



---

archive/issue_comments_081067.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-02T13:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81067",
    "user": "cremona"
}
```

New commits:



---

archive/issue_comments_081068.json:
```json
{
    "body": "Here is a commit which make essentially the same changes as the patch.  I omitted some low-level stuff which seems to have been included anyway in the intervening 4 years.  I changed the QQ.residue_field() function to be even more like the number field version.",
    "created_at": "2014-01-02T13:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81068",
    "user": "cremona"
}
```

Here is a commit which make essentially the same changes as the patch.  I omitted some low-level stuff which seems to have been included anyway in the intervening 4 years.  I changed the QQ.residue_field() function to be even more like the number field version.



---

archive/issue_comments_081069.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-03T11:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81069",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081070.json:
```json
{
    "body": "The two commits up to 307891b implement the original patch with one small additional rebasing edit.  This now passes all tests, but that is not saying a lot since there are very few doctests in the new code.\n\nMy next job: add docstrings and doctests.",
    "created_at": "2014-01-03T11:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81070",
    "user": "cremona"
}
```

The two commits up to 307891b implement the original patch with one small additional rebasing edit.  This now passes all tests, but that is not saying a lot since there are very few doctests in the new code.

My next job: add docstrings and doctests.



---

archive/issue_comments_081071.json:
```json
{
    "body": "I started adding doctests. \n----\nNew commits:",
    "created_at": "2014-03-02T10:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81071",
    "user": "robertwb"
}
```

I started adding doctests. 
----
New commits:



---

archive/issue_comments_081072.json:
```json
{
    "body": "Robert, I spent some time on this a mnth or two ago (how do you find out when a branch was last modified?) and I'm sure some of what I did will be useful -- certain, in fact, since at least one doctest revealed a bug.\n\nWhat is the best way of sharing my branch with you?  There are 2 or 3 commits on top of 6.1.beta2.",
    "created_at": "2014-03-02T20:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81072",
    "user": "cremona"
}
```

Robert, I spent some time on this a mnth or two ago (how do you find out when a branch was last modified?) and I'm sure some of what I did will be useful -- certain, in fact, since at least one doctest revealed a bug.

What is the best way of sharing my branch with you?  There are 2 or 3 commits on top of 6.1.beta2.



---

archive/issue_comments_081073.json:
```json
{
    "body": "I merged your branch into mine, so you should be able to merge that in easily with whatever future work you do.",
    "created_at": "2014-03-06T22:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81073",
    "user": "robertwb"
}
```

I merged your branch into mine, so you should be able to merge that in easily with whatever future work you do.



---

archive/issue_comments_081074.json:
```json
{
    "body": "Replying to [comment:16 robertwb]:\n> I merged your branch into mine, so you should be able to merge that in easily with whatever future work you do.\n\nGit is not clever enough for you to lift by last commit off my own computer though.   I had one more commit with a lot of stuff.  I made a patch from it and put it in boxen:/home/cremona/8828.patch, and it might be worth looking at.",
    "created_at": "2014-03-06T22:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81074",
    "user": "cremona"
}
```

Replying to [comment:16 robertwb]:
> I merged your branch into mine, so you should be able to merge that in easily with whatever future work you do.

Git is not clever enough for you to lift by last commit off my own computer though.   I had one more commit with a lot of stuff.  I made a patch from it and put it in boxen:/home/cremona/8828.patch, and it might be worth looking at.



---

archive/issue_comments_081075.json:
```json
{
    "body": "Fair point :). You should be able to do \n\n\n```\n./sage --dev pull --ticket 8828\n./sage --dev push --ticket 8828\n```\n\n\nto pull these changes in and then push your changes out. This might involve a merge, but it shouldn't conflict. Alternatively, you could publish your repo somewhere (e.g. on github or even boxen) and I could merge it in.",
    "created_at": "2014-03-06T22:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81075",
    "user": "robertwb"
}
```

Fair point :). You should be able to do 


```
./sage --dev pull --ticket 8828
./sage --dev push --ticket 8828
```


to pull these changes in and then push your changes out. This might involve a merge, but it shouldn't conflict. Alternatively, you could publish your repo somewhere (e.g. on github or even boxen) and I could merge it in.



---

archive/issue_comments_081076.json:
```json
{
    "body": "Replying to [comment:18 robertwb]:\n> Fair point :). You should be able to do \n> \n> {{{\n> ./sage --dev pull --ticket 8828\n> ./sage --dev push --ticket 8828\n> }}}\n> \n> to pull these changes in and then push your changes out. This might involve a merge, but it shouldn't conflict. Alternatively, you could publish your repo somewhere (e.g. on github or even boxen) and I could merge it in. \n\nOK, but I don't have time to do that right now as I'm leaving for a conference tomorrow and have a lot to do before that...",
    "created_at": "2014-03-07T09:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81076",
    "user": "cremona"
}
```

Replying to [comment:18 robertwb]:
> Fair point :). You should be able to do 
> 
> {{{
> ./sage --dev pull --ticket 8828
> ./sage --dev push --ticket 8828
> }}}
> 
> to pull these changes in and then push your changes out. This might involve a merge, but it shouldn't conflict. Alternatively, you could publish your repo somewhere (e.g. on github or even boxen) and I could merge it in. 

OK, but I don't have time to do that right now as I'm leaving for a conference tomorrow and have a lot to do before that...



---

archive/issue_comments_081077.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-03-07T14:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81077",
    "user": "cremona"
}
```

New commits:



---

archive/issue_comments_081078.json:
```json
{
    "body": "The automatic merge worked fine: the two new commits are my work + the merge commit.  This gives us a new basis for further work (adding doctests etc): I will not touch this again for 10 days or so at least!",
    "created_at": "2014-03-07T14:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81078",
    "user": "cremona"
}
```

The automatic merge worked fine: the two new commits are my work + the merge commit.  This gives us a new basis for further work (adding doctests etc): I will not touch this again for 10 days or so at least!



---

archive/issue_comments_081079.json:
```json
{
    "body": "This branch looks suspicious: according to the \"diffstat\" that appears when clicking on the branch name, it deletes three entire files (`rings/number_field/morphism.pyx`, `rings/rational_field.py`, `schemes/elliptic_curves/ell_local_data.py`).  Is this a Git (merge) accident?",
    "created_at": "2014-03-27T17:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81079",
    "user": "pbruin"
}
```

This branch looks suspicious: according to the "diffstat" that appears when clicking on the branch name, it deletes three entire files (`rings/number_field/morphism.pyx`, `rings/rational_field.py`, `schemes/elliptic_curves/ell_local_data.py`).  Is this a Git (merge) accident?



---

archive/issue_comments_081080.json:
```json
{
    "body": "Replying to [comment:22 pbruin]:\n> This branch looks suspicious: according to the \"diffstat\" that appears when clicking on the branch name, it deletes three entire files (`rings/number_field/morphism.pyx`, `rings/rational_field.py`, `schemes/elliptic_curves/ell_local_data.py`).  Is this a Git (merge) accident?\n\nThat is not what I see when I click on the brnaches, either the merge I did (756d0ee) or the \"work in progress\" commit b2bc066.",
    "created_at": "2014-03-27T17:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81080",
    "user": "cremona"
}
```

Replying to [comment:22 pbruin]:
> This branch looks suspicious: according to the "diffstat" that appears when clicking on the branch name, it deletes three entire files (`rings/number_field/morphism.pyx`, `rings/rational_field.py`, `schemes/elliptic_curves/ell_local_data.py`).  Is this a Git (merge) accident?

That is not what I see when I click on the brnaches, either the merge I did (756d0ee) or the "work in progress" commit b2bc066.



---

archive/issue_comments_081081.json:
```json
{
    "body": "It only occurs when you look at the whole branch, i.e. when you click on `u/cremona/ticket/8828` in the \"Branch:\" field.  I now tried to fetch the branch with `git fetch trac u/cremona/ticket/8828` and the output of `git diff develop...FETCH_HEAD` does not show anything like this, just normal changes.  Also merging with `develop` seems to work fine.  So it actually looks like a glitch in Trac's git plugin.",
    "created_at": "2014-03-27T17:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81081",
    "user": "pbruin"
}
```

It only occurs when you look at the whole branch, i.e. when you click on `u/cremona/ticket/8828` in the "Branch:" field.  I now tried to fetch the branch with `git fetch trac u/cremona/ticket/8828` and the output of `git diff develop...FETCH_HEAD` does not show anything like this, just normal changes.  Also merging with `develop` seems to work fine.  So it actually looks like a glitch in Trac's git plugin.



---

archive/issue_comments_081082.json:
```json
{
    "body": "Replying to [comment:24 pbruin]:\n> It only occurs when you look at the whole branch, i.e. when you click on `u/cremona/ticket/8828` in the \"Branch:\" field.  I now tried to fetch the branch with `git fetch trac u/cremona/ticket/8828` and the output of `git diff develop...FETCH_HEAD` does not show anything like this, just normal changes.  Also merging with `develop` seems to work fine.  So it actually looks like a glitch in Trac's git plugin.\n\nThat is a relief -- though I still have that branch on my own computer and presumably if and when I check it out again I will see a file with the changes I made.",
    "created_at": "2014-03-27T20:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81082",
    "user": "cremona"
}
```

Replying to [comment:24 pbruin]:
> It only occurs when you look at the whole branch, i.e. when you click on `u/cremona/ticket/8828` in the "Branch:" field.  I now tried to fetch the branch with `git fetch trac u/cremona/ticket/8828` and the output of `git diff develop...FETCH_HEAD` does not show anything like this, just normal changes.  Also merging with `develop` seems to work fine.  So it actually looks like a glitch in Trac's git plugin.

That is a relief -- though I still have that branch on my own computer and presumably if and when I check it out again I will see a file with the changes I made.



---

archive/issue_comments_081083.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-31T16:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81083",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081084.json:
```json
{
    "body": "The previous commit is simply merging the current develop branch (at commit 9db8c5c, tag 6.2.beta5) into my branch, which I now intend to resume work on.",
    "created_at": "2014-03-31T16:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81084",
    "user": "cremona"
}
```

The previous commit is simply merging the current develop branch (at commit 9db8c5c, tag 6.2.beta5) into my branch, which I now intend to resume work on.



---

archive/issue_comments_081085.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-03T12:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81085",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081086.json:
```json
{
    "body": "I have finished workin on height.py,  adding a large amount of documentation and examples.  There were some bugs revealed by this, which have been fixed.  One was in the function `non_neg_region` and was a simple slip, I forget the details.  The second was due to wrong normalisation of period lattice basis (for real embeddings):  L.basis() gives w1, w2 with w1 real, while L.normalised_basis() gives w1,w2 with w2 minimal and tau=w1/w2 in the fundamental region.  To avoid this catching people out in future I added a method tau() to the period lattice class.  The effect here is that in some of the tests the error is now better than it was;  but also the test results (for fk and wp) are different since they work with respect to the normalised lattice [1,tau] and so are different when the correct value of tau is used!\n\nI added more examples from the papers cited, and also give more specific references to those papers throughout, especially the paper [TT] by Nook (Thotsaphon Thonjungthug);  the theory here was developed by himself with me and Samir Siksek while Nook was our PhD student.\n\nIt seems to be four years since Robert Bradshaw implemented this (Nook himself implemented it too, in Magma) so it seem rather unreasonable to ask him to look at it again.  Peter Bruin would be a good person, since his own recent paper improves Nook's results (and makes some of this redundant perhaps?)\n\nI will set this to \"needs review\" as soon as I have added a couple of missing doctests in the file `period_lattice_region.pyx` to bring the two files up to 100%.",
    "created_at": "2014-04-03T12:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81086",
    "user": "cremona"
}
```

I have finished workin on height.py,  adding a large amount of documentation and examples.  There were some bugs revealed by this, which have been fixed.  One was in the function `non_neg_region` and was a simple slip, I forget the details.  The second was due to wrong normalisation of period lattice basis (for real embeddings):  L.basis() gives w1, w2 with w1 real, while L.normalised_basis() gives w1,w2 with w2 minimal and tau=w1/w2 in the fundamental region.  To avoid this catching people out in future I added a method tau() to the period lattice class.  The effect here is that in some of the tests the error is now better than it was;  but also the test results (for fk and wp) are different since they work with respect to the normalised lattice [1,tau] and so are different when the correct value of tau is used!

I added more examples from the papers cited, and also give more specific references to those papers throughout, especially the paper [TT] by Nook (Thotsaphon Thonjungthug);  the theory here was developed by himself with me and Samir Siksek while Nook was our PhD student.

It seems to be four years since Robert Bradshaw implemented this (Nook himself implemented it too, in Magma) so it seem rather unreasonable to ask him to look at it again.  Peter Bruin would be a good person, since his own recent paper improves Nook's results (and makes some of this redundant perhaps?)

I will set this to "needs review" as soon as I have added a couple of missing doctests in the file `period_lattice_region.pyx` to bring the two files up to 100%.



---

archive/issue_comments_081087.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-04-03T13:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81087",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081088.json:
```json
{
    "body": "Done!  Please review...",
    "created_at": "2014-04-03T13:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81088",
    "user": "cremona"
}
```

Done!  Please review...



---

archive/issue_comments_081089.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-04-03T13:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81089",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081090.json:
```json
{
    "body": "I'm now reading the code and documentation.  Apart from a number of small spelling/typographical things (for which I'll just make a reviewer patch), there are a few functions of which the documentation is missing:\n- `EllipticCurve_number_field.height_function()`\n- the functions `frame_data()` and `unframe_data()` in `period_lattice_region.pyx`\nBy the way, I don't think my paper of last year makes any of this redundant.  My method is almost certainly slower (I don't know by how much; it is only implemented as a PARI script and I did not make a lot of effort to make it fast, but I doubt it can beat the algorithms in this patch).  Which method is most suitable probably depends a lot on the curve.",
    "created_at": "2014-04-04T21:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81090",
    "user": "pbruin"
}
```

I'm now reading the code and documentation.  Apart from a number of small spelling/typographical things (for which I'll just make a reviewer patch), there are a few functions of which the documentation is missing:
- `EllipticCurve_number_field.height_function()`
- the functions `frame_data()` and `unframe_data()` in `period_lattice_region.pyx`
By the way, I don't think my paper of last year makes any of this redundant.  My method is almost certainly slower (I don't know by how much; it is only implemented as a PARI script and I did not make a lot of effort to make it fast, but I doubt it can beat the algorithms in this patch).  Which method is most suitable probably depends a lot on the curve.



---

archive/issue_comments_081091.json:
```json
{
    "body": "I just found out about #13125, which implements a `RealSet` class representing finite unions of real intervals and points.  Would it make sense to use this (and extend it where necessary) instead of the `UnionOfIntervals` introduced in this ticket?",
    "created_at": "2014-04-06T15:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81091",
    "user": "pbruin"
}
```

I just found out about #13125, which implements a `RealSet` class representing finite unions of real intervals and points.  Would it make sense to use this (and extend it where necessary) instead of the `UnionOfIntervals` introduced in this ticket?



---

archive/issue_comments_081092.json:
```json
{
    "body": "Maybe in future, but it would delay this (and the dependent tickets such as #8289), and the code here is tested.  I would say we should put in a reference to a new ticket to consider doing that in future.  But this is partly laziness, and not being familiar with the code at #13125.",
    "created_at": "2014-04-06T16:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81092",
    "user": "cremona"
}
```

Maybe in future, but it would delay this (and the dependent tickets such as #8289), and the code here is tested.  I would say we should put in a reference to a new ticket to consider doing that in future.  But this is partly laziness, and not being familiar with the code at #13125.



---

archive/issue_comments_081093.json:
```json
{
    "body": "Replying to [comment:34 cremona]:\n> Maybe in future, but it would delay this (and the dependent tickets such as #8289), and the code here is tested.  I would say we should put in a reference to a new ticket to consider doing that in future.\nOK, this is now #16063.",
    "created_at": "2014-04-06T18:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81093",
    "user": "pbruin"
}
```

Replying to [comment:34 cremona]:
> Maybe in future, but it would delay this (and the dependent tickets such as #8289), and the code here is tested.  I would say we should put in a reference to a new ticket to consider doing that in future.
OK, this is now #16063.



---

archive/issue_comments_081094.json:
```json
{
    "body": "A question about the new method `RationalField.places()`: is there a reason why the `prec` argument is handled differently than in `NumberField_absolute.places()`?  Here is a table of which fields are used for the embedding depending on `prec`:\n\n```\nprec      RationalField    NumberField\n------------------------------------------\nNone      RR/CC            RIF/CIF\nInfinity  not accepted     AA/QQbar\n53        RDF/CDF          RDF/CDF\nother     RealField(prec)  RealField(prec)\n```\n",
    "created_at": "2014-04-08T10:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81094",
    "user": "pbruin"
}
```

A question about the new method `RationalField.places()`: is there a reason why the `prec` argument is handled differently than in `NumberField_absolute.places()`?  Here is a table of which fields are used for the embedding depending on `prec`:

```
prec      RationalField    NumberField
------------------------------------------
None      RR/CC            RIF/CIF
Infinity  not accepted     AA/QQbar
53        RDF/CDF          RDF/CDF
other     RealField(prec)  RealField(prec)
```




---

archive/issue_comments_081095.json:
```json
{
    "body": "No reason.  If you are making some reviewer changes, please could you make this consistent?  Thanks.",
    "created_at": "2014-04-08T21:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81095",
    "user": "cremona"
}
```

No reason.  If you are making some reviewer changes, please could you make this consistent?  Thanks.



---

archive/issue_comments_081096.json:
```json
{
    "body": "Could you please check if you agree with the changes in the new branch (which is based on yours)?  Here is a summary of the changes:\n\n- The first commit (\"reviewer patch\") consists mostly of formatting changes, spelling fixes and Python style issues.  It also adds the new files to the reference manual.  Because of this I had to change one of the references [TT] to [T].  I also changed [Cremona2010] to [CT] to be more consistent.\n\n- The documentation of the existing method `NumberField_absolute.places()` is wrong; in fact it never returns an embedding into `RIF` or `CIF`, it just uses these to determine the required precision if `prec=None`.  I have not changed the documentation; it could be done in an additional commit here or in a new ticket.  For the new method `RationalField.places()`, I just added the `prec=Infinity` option.\n\n- For consistency, `RDF` is now used instead for all bounds (there were two places where `RR` was used).\n\n- The two coefficients of the Laurent series of the Weierstrass p-function that are needed can be obtained more easily as suitable multiples of the usual modular forms *c*<sub>4</sub> and *c*<sub>6</sub>.\n\n- Added documentation for the functions mentioned in comment:32.\n\nAll tests pass, so if you are happy with the changes you can set this to positive review.",
    "created_at": "2014-04-09T11:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81096",
    "user": "pbruin"
}
```

Could you please check if you agree with the changes in the new branch (which is based on yours)?  Here is a summary of the changes:

- The first commit ("reviewer patch") consists mostly of formatting changes, spelling fixes and Python style issues.  It also adds the new files to the reference manual.  Because of this I had to change one of the references [TT] to [T].  I also changed [Cremona2010] to [CT] to be more consistent.

- The documentation of the existing method `NumberField_absolute.places()` is wrong; in fact it never returns an embedding into `RIF` or `CIF`, it just uses these to determine the required precision if `prec=None`.  I have not changed the documentation; it could be done in an additional commit here or in a new ticket.  For the new method `RationalField.places()`, I just added the `prec=Infinity` option.

- For consistency, `RDF` is now used instead for all bounds (there were two places where `RR` was used).

- The two coefficients of the Laurent series of the Weierstrass p-function that are needed can be obtained more easily as suitable multiples of the usual modular forms *c*<sub>4</sub> and *c*<sub>6</sub>.

- Added documentation for the functions mentioned in comment:32.

All tests pass, so if you are happy with the changes you can set this to positive review.



---

archive/issue_comments_081097.json:
```json
{
    "body": "Thanks -- I will look at your patches carefully when I am back next week.",
    "created_at": "2014-04-09T20:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81097",
    "user": "cremona"
}
```

Thanks -- I will look at your patches carefully when I am back next week.



---

archive/issue_comments_081098.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-31T13:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81098",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081099.json:
```json
{
    "body": "Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.  I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).",
    "created_at": "2014-05-31T13:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81099",
    "user": "cremona"
}
```

Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.  I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).



---

archive/issue_comments_081100.json:
```json
{
    "body": "Replying to [comment:41 cremona]:\n> Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.\nThank you!\n> I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).\nIt is indeed red; this is because the blob shows the patchbot result for the latest stable release (6.2) instead of the latest development version, and the patchbot failed to build with 6.2, for reasons unrelated to this ticket.  Clicking on the blob will give you the result of all patchbot runs; the latest patchbot build (with 6.3.beta2) succeeded and passed tests.",
    "created_at": "2014-05-31T14:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81100",
    "user": "pbruin"
}
```

Replying to [comment:41 cremona]:
> Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.
Thank you!
> I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).
It is indeed red; this is because the blob shows the patchbot result for the latest stable release (6.2) instead of the latest development version, and the patchbot failed to build with 6.2, for reasons unrelated to this ticket.  Clicking on the blob will give you the result of all patchbot runs; the latest patchbot build (with 6.3.beta2) succeeded and passed tests.



---

archive/issue_comments_081101.json:
```json
{
    "body": "Replying to [comment:42 pbruin]:\n> Replying to [comment:41 cremona]:\n> > Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.\n> Thank you!\n> > I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).\n> It is indeed red; this is because the blob shows the patchbot result for the latest stable release (6.2) instead of the latest development version, and the patchbot failed to build with 6.2, for reasons unrelated to this ticket.  Clicking on the blob will give you the result of all patchbot runs; the latest patchbot build (with 6.3.beta2) succeeded and passed tests.\nYes, I saw that green one.  It makes the blob on the ticket itself rather misleading!",
    "created_at": "2014-05-31T14:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81101",
    "user": "cremona"
}
```

Replying to [comment:42 pbruin]:
> Replying to [comment:41 cremona]:
> > Peter, I am very sorry it took me so long to look at your reviewer's patches.  You should have reminded me!  I have looked at them and approve.
> Thank you!
> > I do not know why the coloured blob at the top is not green (it looks red to me but I am not good on colours).
> It is indeed red; this is because the blob shows the patchbot result for the latest stable release (6.2) instead of the latest development version, and the patchbot failed to build with 6.2, for reasons unrelated to this ticket.  Clicking on the blob will give you the result of all patchbot runs; the latest patchbot build (with 6.3.beta2) succeeded and passed tests.
Yes, I saw that green one.  It makes the blob on the ticket itself rather misleading!



---

archive/issue_comments_081102.json:
```json
{
    "body": "PDF docs don't build",
    "created_at": "2014-06-02T12:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81102",
    "user": "vbraun"
}
```

PDF docs don't build



---

archive/issue_comments_081103.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-06-02T12:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81103",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081104.json:
```json
{
    "body": "Replying to [comment:44 vbraun]:\n> PDF docs don't build\n\nPlease be more specific.  I don't know how to build the pdf docs for just the files created here, and a complete build (which I did do) produced such vast output that I cannot look for anything relevant in it.",
    "created_at": "2014-06-02T18:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81104",
    "user": "cremona"
}
```

Replying to [comment:44 vbraun]:
> PDF docs don't build

Please be more specific.  I don't know how to build the pdf docs for just the files created here, and a complete build (which I did do) produced such vast output that I cannot look for anything relevant in it.



---

archive/issue_comments_081105.json:
```json
{
    "body": "\n```\ngrep -A 3 \"Emergency stop\" logs/docpdf.log\n```\n",
    "created_at": "2014-06-02T20:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81105",
    "user": "vbraun"
}
```


```
grep -A 3 "Emergency stop" logs/docpdf.log
```




---

archive/issue_comments_081106.json:
```json
{
    "body": "Replying to [comment:46 vbraun]:\n> {{{\n> grep -A 3 \"Emergency stop\" logs/docpdf.log\n> }}}\n\nThis shows nothing, even after several rounds of make doc-clean and make doc-pdf etc.\nThe log shows that the build quits after\n\n```\nOSError: [combinat ] /home/jec/sage/src/doc/en/reference/combinat/algebra.rst:4: WARNING: toctree contains reference to nonexisting document u'sage/combinat/free_module'\n```\n\nwhich has nothing to do with this ticket!",
    "created_at": "2014-06-03T07:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81106",
    "user": "cremona"
}
```

Replying to [comment:46 vbraun]:
> {{{
> grep -A 3 "Emergency stop" logs/docpdf.log
> }}}

This shows nothing, even after several rounds of make doc-clean and make doc-pdf etc.
The log shows that the build quits after

```
OSError: [combinat ] /home/jec/sage/src/doc/en/reference/combinat/algebra.rst:4: WARNING: toctree contains reference to nonexisting document u'sage/combinat/free_module'
```

which has nothing to do with this ticket!



---

archive/issue_comments_081107.json:
```json
{
    "body": "Does `sage -sync-build` fix it? If not: `make distclean && make`.",
    "created_at": "2014-06-03T11:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81107",
    "user": "vbraun"
}
```

Does `sage -sync-build` fix it? If not: `make distclean && make`.



---

archive/issue_comments_081108.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-03T12:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81108",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081109.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-06-03T12:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81109",
    "user": "pbruin"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_081110.json:
```json
{
    "body": "I tried `make doc-pdf` and it TeX complained about being `\\eps` being an undefined control sequence.  I changed it to `\\epsilon`; hopefully that was the only problem.",
    "created_at": "2014-06-03T12:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81110",
    "user": "pbruin"
}
```

I tried `make doc-pdf` and it TeX complained about being `\eps` being an undefined control sequence.  I changed it to `\epsilon`; hopefully that was the only problem.



---

archive/issue_comments_081111.json:
```json
{
    "body": "Replying to [comment:50 pbruin]:\n> I tried `make doc-pdf` and it TeX complained about being `\\eps` being an undefined control sequence.  I changed it to `\\epsilon`; hopefully that was the only problem.\nActually it wasn't, there is also a `\\time` that should be a `\\times`, patch coming soon.",
    "created_at": "2014-06-03T14:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81111",
    "user": "pbruin"
}
```

Replying to [comment:50 pbruin]:
> I tried `make doc-pdf` and it TeX complained about being `\eps` being an undefined control sequence.  I changed it to `\epsilon`; hopefully that was the only problem.
Actually it wasn't, there is also a `\time` that should be a `\times`, patch coming soon.



---

archive/issue_comments_081112.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-06-03T14:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81112",
    "user": "pbruin"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081113.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-06-03T15:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81113",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_081114.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-06-03T15:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81114",
    "user": "pbruin"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_081115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-04T10:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81115",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_081116.json:
```json
{
    "body": "Please see #17088 for a follow-up.",
    "created_at": "2014-10-02T09:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8828#issuecomment-81116",
    "user": "jdemeyer"
}
```

Please see #17088 for a follow-up.
