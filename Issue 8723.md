# Issue 8723: Change to return type of E.multiplcation_by_m(m,True)

archive/issues_008723.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nAs reported to sage-nt:\n\nIf E is an elliptic curve over K and m is a nonzero integer, then E.multiplication_by_m(m) returns a tuple (X,Y) where X and Y are both in K(x,y) and give the \"formula\" for the multiplcation-by-m map on E.  Of course, mathematically, X is in K(x), but it is returned with the same parent as Y, namely K(x,y) (i.e. the fraction field of the 2-variable polynomial ring over K).\n\nThere is an optional parameter x_only which by default is False, but if True the return value is just X as above, an element of K(x,y) which happens not to involve y.\n\nI propose to change the function so that there is no change when x_only is False (the default), but when it is True the rational function returned would be in K(x) and not in K(x,y);  in this case one would not need to construct any bivariate polynomial rings or fields at all.\n\nWould anyone be unhappy about this?  The only issue which I can see is that if you construct phi to be the multiplcation-by-m isogeny, then phi.rational_maps() is currently of the form (X,Y) as above, so now one can check that\n\nphi.rational_maps()[0] == E.multiplication_by_m(m,True)\n\nwhile after my proposed change this would be False (I think, unless coercion would magically embed K(x) into K(x,y), which I have not checked).  \n\nImplementation and checking would be very easy.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8723\n\n",
    "created_at": "2010-04-20T10:53:54Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.1",
    "title": "Change to return type of E.multiplcation_by_m(m,True)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8723",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

As reported to sage-nt:

If E is an elliptic curve over K and m is a nonzero integer, then E.multiplication_by_m(m) returns a tuple (X,Y) where X and Y are both in K(x,y) and give the "formula" for the multiplcation-by-m map on E.  Of course, mathematically, X is in K(x), but it is returned with the same parent as Y, namely K(x,y) (i.e. the fraction field of the 2-variable polynomial ring over K).

There is an optional parameter x_only which by default is False, but if True the return value is just X as above, an element of K(x,y) which happens not to involve y.

I propose to change the function so that there is no change when x_only is False (the default), but when it is True the rational function returned would be in K(x) and not in K(x,y);  in this case one would not need to construct any bivariate polynomial rings or fields at all.

Would anyone be unhappy about this?  The only issue which I can see is that if you construct phi to be the multiplcation-by-m isogeny, then phi.rational_maps() is currently of the form (X,Y) as above, so now one can check that

phi.rational_maps()[0] == E.multiplication_by_m(m,True)

while after my proposed change this would be False (I think, unless coercion would magically embed K(x) into K(x,y), which I have not checked).  

Implementation and checking would be very easy.


Issue created by migration from https://trac.sagemath.org/ticket/8723





---

archive/issue_comments_079527.json:
```json
{
    "body": "here is a proposal, if this is still wanted after so many years",
    "created_at": "2013-08-20T14:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79527",
    "user": "https://github.com/fchapoton"
}
```

here is a proposal, if this is still wanted after so many years



---

archive/issue_comments_079528.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-20T14:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79528",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079529.json:
```json
{
    "body": "So now I really am going to have to learn how to use the new git system!",
    "created_at": "2013-08-20T14:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79529",
    "user": "https://github.com/JohnCremona"
}
```

So now I really am going to have to learn how to use the new git system!



---

archive/issue_comments_079530.json:
```json
{
    "body": "well, sooner or later...  =)\n\nthere are some explanations here  :\n\nhttp://sagemath.github.io/git-developer-guide/walk_through.html#section-walkthrough-review",
    "created_at": "2013-08-20T14:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79530",
    "user": "https://github.com/fchapoton"
}
```

well, sooner or later...  =)

there are some explanations here  :

http://sagemath.github.io/git-developer-guide/walk_through.html#section-walkthrough-review



---

archive/issue_comments_079531.json:
```json
{
    "body": "Replying to [comment:5 chapoton]:\n> well, sooner or later...  =)\n> \n> there are some explanations here  :\n> \n> http://sagemath.github.io/git-developer-guide/walk_through.html#section-walkthrough-review\n> \n\nI have a clone of the git repository and pulled in all the commits on trac (using git pull trac master followed by make), and have a working version (./sage runs ok and shows 5.12.beta2 in the banner).  But ./sage -dev fails (unknown option).  Does that mean that I should do the \"manual git\" as in Git the Hard Way, using git fetch trac ...?  I can do that, of course, but thought that the scripts made it unnecessary.\n\nMeanwhile I looked at the diff for your commit and looks reasonable, though I would of course want to check it.",
    "created_at": "2013-08-21T19:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79531",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 chapoton]:
> well, sooner or later...  =)
> 
> there are some explanations here  :
> 
> http://sagemath.github.io/git-developer-guide/walk_through.html#section-walkthrough-review
> 

I have a clone of the git repository and pulled in all the commits on trac (using git pull trac master followed by make), and have a working version (./sage runs ok and shows 5.12.beta2 in the banner).  But ./sage -dev fails (unknown option).  Does that mean that I should do the "manual git" as in Git the Hard Way, using git fetch trac ...?  I can do that, of course, but thought that the scripts made it unnecessary.

Meanwhile I looked at the diff for your commit and looks reasonable, though I would of course want to check it.



---

archive/issue_comments_079532.json:
```json
{
    "body": "well, I must admit that I have never done a review for a git branch. \n\nIf I would try, I would go for the \"hard way\".\n\nBut I would really like to know how to use the dev script manner too.",
    "created_at": "2013-08-21T19:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79532",
    "user": "https://github.com/fchapoton"
}
```

well, I must admit that I have never done a review for a git branch. 

If I would try, I would go for the "hard way".

But I would really like to know how to use the dev script manner too.



---

archive/issue_comments_079533.json:
```json
{
    "body": "I have made a second commit, trying to improve the documentation",
    "created_at": "2013-08-30T19:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79533",
    "user": "https://github.com/fchapoton"
}
```

I have made a second commit, trying to improve the documentation



---

archive/issue_comments_079534.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2013-12-02T20:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79534",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079535.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2013-12-02T21:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79535",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079536.json:
```json
{
    "body": "I am attempting to review this as my first real venture into the new world of reviewing using the git model...",
    "created_at": "2013-12-17T11:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79536",
    "user": "https://github.com/JohnCremona"
}
```

I am attempting to review this as my first real venture into the new world of reviewing using the git model...



---

archive/issue_comments_079537.json:
```json
{
    "body": "See the discussion on sage-git here: https://groups.google.com/d/topic/sage-git/mbAH7xAia3Y/discussion\n\nMy plan now is to merge this branch with the current master, which I think will make it easier to see what has now changed with this ticket.  There are some problems caused by the fact that this branch was forked off the master branch rather along time ago.  An alternative to merging would be to use git's cherry-pick or rebase procedure to apply the changes made by the commits in this branch to the current master branch.  I think that would be better: it would be like pretending that the work on this ticket all happened right now.\n\nWould you like to do that or shall I try?",
    "created_at": "2013-12-17T15:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79537",
    "user": "https://github.com/JohnCremona"
}
```

See the discussion on sage-git here: https://groups.google.com/d/topic/sage-git/mbAH7xAia3Y/discussion

My plan now is to merge this branch with the current master, which I think will make it easier to see what has now changed with this ticket.  There are some problems caused by the fact that this branch was forked off the master branch rather along time ago.  An alternative to merging would be to use git's cherry-pick or rebase procedure to apply the changes made by the commits in this branch to the current master branch.  I think that would be better: it would be like pretending that the work on this ticket all happened right now.

Would you like to do that or shall I try?



---

archive/issue_comments_079538.json:
```json
{
    "body": "Well, I am rather busy right now, and I am really not enough git-confident and knowledgeable to do that. Please do it yourself if you can.\n\nFrederic",
    "created_at": "2013-12-17T15:39:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79538",
    "user": "https://github.com/fchapoton"
}
```

Well, I am rather busy right now, and I am really not enough git-confident and knowledgeable to do that. Please do it yourself if you can.

Frederic



---

archive/issue_comments_079539.json:
```json
{
    "body": "Replying to [comment:14 chapoton]:\n> Well, I am rather busy right now, and I am really not enough git-confident and knowledgeable to do that. Please do it yourself if you can.\n> \n> Frederic\n\nIt turns out that I am not allowed to (see further discussion on sage-git).  I cannot rebase, since that is rewriting history and not allowed (by convention) on commits that have been made public (as on this ticket) since there might be people who have taken those commits as a base for something else.  (Clearly not likeliy in this case.)  And whle I can merge the current master, as a way of seeing what changes you have made (by comparing the merged current-master + your changes to the current-master by itself), which helps me see the cumulative effect of what you did, I am not supposed to upload that merged commit back to this ticket.\n\nThis makes it rather complicated for me to something which used to be so simple, i.e. to make some small \"reviewer patch\" additional changes.  I have to first unmerge the current master, then make my edits and a new commit whose parent is the one downloaded from this ticket and push that back up to the ticket.\n\nOf course, that will not be necessary if I find your changes perfect ;)",
    "created_at": "2013-12-17T16:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79539",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:14 chapoton]:
> Well, I am rather busy right now, and I am really not enough git-confident and knowledgeable to do that. Please do it yourself if you can.
> 
> Frederic

It turns out that I am not allowed to (see further discussion on sage-git).  I cannot rebase, since that is rewriting history and not allowed (by convention) on commits that have been made public (as on this ticket) since there might be people who have taken those commits as a base for something else.  (Clearly not likeliy in this case.)  And whle I can merge the current master, as a way of seeing what changes you have made (by comparing the merged current-master + your changes to the current-master by itself), which helps me see the cumulative effect of what you did, I am not supposed to upload that merged commit back to this ticket.

This makes it rather complicated for me to something which used to be so simple, i.e. to make some small "reviewer patch" additional changes.  I have to first unmerge the current master, then make my edits and a new commit whose parent is the one downloaded from this ticket and push that back up to the ticket.

Of course, that will not be necessary if I find your changes perfect ;)



---

archive/issue_comments_079540.json:
```json
{
    "body": "Very sorry, but checking that this works revealed a problem.  The function `multiplication_by_m` calls  `_multiple_x_numerator(m,x)` and the latter caches its results with a cache whose key is just m and not the tuple (m,x), which means that the x in the returned value of `E.multiplication_by_m` is not necessarily the x you defined in the function.  For example:\n\n```\nsage: E = EllipticCurve([0,0,0,0,1])\nsage: x2,y2 = E.multiplication_by_m(2)\nsage: x2.parent(), y2.parent()\n(Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field,\n Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field)\nsage: X2 = E.multiplication_by_m(2, x_only=True)\nsage: X2.parent()\nFraction Field of Multivariate Polynomial Ring in x, y over Rational Field\n```\n\nwhere the last parent is wrong, and in the other direction\n\n```\nsage: E = EllipticCurve([0,0,0,0,1])\nsage: X2 = E.multiplication_by_m(2, x_only=True)\nsage: X2.parent()\nFraction Field of Univariate Polynomial Ring in x over Rational Field\nsage: x2,y2 = E.multiplication_by_m(2)\nsage: x2.parent(), y2.parent()\n(Fraction Field of Univariate Polynomial Ring in x over Rational Field,\n Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field)\n```\n\nwhich is worse!\n\nI will fix this by changing the caching behaviour of the subsidiary function, and see if I can push the new commit onto this ticket.",
    "created_at": "2013-12-17T17:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79540",
    "user": "https://github.com/JohnCremona"
}
```

Very sorry, but checking that this works revealed a problem.  The function `multiplication_by_m` calls  `_multiple_x_numerator(m,x)` and the latter caches its results with a cache whose key is just m and not the tuple (m,x), which means that the x in the returned value of `E.multiplication_by_m` is not necessarily the x you defined in the function.  For example:

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent(), y2.parent()
(Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field,
 Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field)
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
```

where the last parent is wrong, and in the other direction

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Univariate Polynomial Ring in x over Rational Field
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent(), y2.parent()
(Fraction Field of Univariate Polynomial Ring in x over Rational Field,
 Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field)
```

which is worse!

I will fix this by changing the caching behaviour of the subsidiary function, and see if I can push the new commit onto this ticket.



---

archive/issue_comments_079541.json:
```json
{
    "body": "Replying to [comment:16 cremona]:\n\n> \n> I will fix this by changing the caching behaviour of the subsidiary function, \n\nDone.  Now the output of that example is\n\n```\nsage: E = EllipticCurve([0,0,0,0,1])\nsage: X2 = E.multiplication_by_m(2, x_only=True)\nsage: X2.parent()\nFraction Field of Univariate Polynomial Ring in x over Rational Field\nsage: x2,y2 = E.multiplication_by_m(2)\nsage: x2.parent()\nFraction Field of Multivariate Polynomial Ring in x, y over Rational Field\nsage: y2.parent()\nFraction Field of Multivariate Polynomial Ring in x, y over Rational Field\nsage: E = EllipticCurve([0,0,0,0,1])\nsage: x2,y2 = E.multiplication_by_m(2)\nsage: x2.parent()\nFraction Field of Multivariate Polynomial Ring in x, y over Rational Field\nsage: y2.parent()\nFraction Field of Multivariate Polynomial Ring in x, y over Rational Field\nsage: X2 = E.multiplication_by_m(2, x_only=True)\nsage: X2.parent()\nFraction Field of Univariate Polynomial Ring in x over Rational Field\n```\n\n\n> and see if I can push the new commit onto this ticket.\n\nThis failed with\n\n```\nCounting objects: 136, done.\nDelta compression using up to 64 threads.\nCompressing objects: 100% (26/26), done.\nWriting objects: 100% (30/30), 4.47 KiB, done.\nTotal 30 (delta 20), reused 4 (delta 4)\nremote: FATAL: W refs/heads/master sage cremona DENIED by fallthru\nremote: error: hook declined to update refs/heads/master\nTo ssh://git@trac.sagemath.org:2222/sage.git\n ! [remote rejected] master -> master (hook declined)\nerror: failed to push some refs to 'ssh://git@trac.sagemath.org:2222/sage.git'\n```\n\n\nfor which I am seeking help on sage-git.",
    "created_at": "2013-12-17T17:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79541",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:16 cremona]:

> 
> I will fix this by changing the caching behaviour of the subsidiary function, 

Done.  Now the output of that example is

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Univariate Polynomial Ring in x over Rational Field
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: y2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: E = EllipticCurve([0,0,0,0,1])
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: y2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Univariate Polynomial Ring in x over Rational Field
```


> and see if I can push the new commit onto this ticket.

This failed with

```
Counting objects: 136, done.
Delta compression using up to 64 threads.
Compressing objects: 100% (26/26), done.
Writing objects: 100% (30/30), 4.47 KiB, done.
Total 30 (delta 20), reused 4 (delta 4)
remote: FATAL: W refs/heads/master sage cremona DENIED by fallthru
remote: error: hook declined to update refs/heads/master
To ssh://git@trac.sagemath.org:2222/sage.git
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to 'ssh://git@trac.sagemath.org:2222/sage.git'
```


for which I am seeking help on sage-git.



---

archive/issue_comments_079542.json:
```json
{
    "body": "I have pushed my new commit now:\n\n```\n * [new branch]      HEAD -> u/cremona/8723\n```\n\nthough I cannot see any sign of it here on trac.",
    "created_at": "2013-12-17T17:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79542",
    "user": "https://github.com/JohnCremona"
}
```

I have pushed my new commit now:

```
 * [new branch]      HEAD -> u/cremona/8723
```

though I cannot see any sign of it here on trac.



---

archive/issue_comments_079543.json:
```json
{
    "body": "New commits:",
    "created_at": "2013-12-17T19:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79543",
    "user": "https://github.com/JohnCremona"
}
```

New commits:



---

archive/issue_comments_079544.json:
```json
{
    "body": "For info:  I added some edits to Frederic's and pushed the resulting commit to a branch owned by me called u/cremona/8723, using the command\n\n```\ngit push trac HEAD:u/cremona/8723 \n```\n\nThen I manually changed the Branch field on this ticket;  saving that updated the commit hash as well.\n\nTo see just my additional changes, pull the branch and do `git diff HEAD^ HEAD`.  It should be possible to see the changes since the parent's of Frederic's first commit, but I have not yet managed to do so.",
    "created_at": "2013-12-17T19:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79544",
    "user": "https://github.com/JohnCremona"
}
```

For info:  I added some edits to Frederic's and pushed the resulting commit to a branch owned by me called u/cremona/8723, using the command

```
git push trac HEAD:u/cremona/8723 
```

Then I manually changed the Branch field on this ticket;  saving that updated the commit hash as well.

To see just my additional changes, pull the branch and do `git diff HEAD^ HEAD`.  It should be possible to see the changes since the parent's of Frederic's first commit, but I have not yet managed to do so.



---

archive/issue_comments_079545.json:
```json
{
    "body": "Frederic, if you approve of my additional changes (see previous comment) then we can jointly give this a positive review.  It would be very nice to rebase this into one simple commit on top of the current develop branch, but we are not allowed to do that, simply because of the remote possibility that someone else has based a new branch on what we already have here.  So the sooner we can get this merged the better!",
    "created_at": "2014-01-02T15:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79545",
    "user": "https://github.com/JohnCremona"
}
```

Frederic, if you approve of my additional changes (see previous comment) then we can jointly give this a positive review.  It would be very nice to rebase this into one simple commit on top of the current develop branch, but we are not allowed to do that, simply because of the remote possibility that someone else has based a new branch on what we already have here.  So the sooner we can get this merged the better!



---

archive/issue_comments_079546.json:
```json
{
    "body": "There is a [x,0] to be replaced by [x] in sage/schemes/elliptic_curves/isogeny_small_degree.py\n\nBecause now the parent has only one variable\n\nOtherwise, the tests do not pass.",
    "created_at": "2014-01-02T17:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79546",
    "user": "https://github.com/fchapoton"
}
```

There is a [x,0] to be replaced by [x] in sage/schemes/elliptic_curves/isogeny_small_degree.py

Because now the parent has only one variable

Otherwise, the tests do not pass.



---

archive/issue_comments_079547.json:
```json
{
    "body": "Patience... I grabbed the top commit and after remaking Sage find doctest errors (in `ell_field.py` and {{{isogeny_small_degree.py}}) so this needs more work.  Since git is perfect I must have not done enough testing.",
    "created_at": "2014-01-02T17:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79547",
    "user": "https://github.com/JohnCremona"
}
```

Patience... I grabbed the top commit and after remaking Sage find doctest errors (in `ell_field.py` and {{{isogeny_small_degree.py}}) so this needs more work.  Since git is perfect I must have not done enough testing.



---

archive/issue_comments_079548.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-01-02T17:08:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79548",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079549.json:
```json
{
    "body": "Replying to [comment:23 chapoton]:\n> There is a [x,0] to be replaced by [x] in sage/schemes/elliptic_curves/isogeny_small_degree.py\n> \n> Because now the parent has only one variable\n> \n> Otherwise, the tests do not pass.\n\nYou are quite right, and by chance you were editing your comment at the same time as I was.  I have fixed that and will push a new commit in a few minutes.  Apologies.  I wrote the original patch on this ticket before that code existed, I think.",
    "created_at": "2014-01-02T17:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79549",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:23 chapoton]:
> There is a [x,0] to be replaced by [x] in sage/schemes/elliptic_curves/isogeny_small_degree.py
> 
> Because now the parent has only one variable
> 
> Otherwise, the tests do not pass.

You are quite right, and by chance you were editing your comment at the same time as I was.  I have fixed that and will push a new commit in a few minutes.  Apologies.  I wrote the original patch on this ticket before that code existed, I think.



---

archive/issue_comments_079550.json:
```json
{
    "body": "Note that the branch name has changed (it was non-standard, my fault).\n\nI have checked that from this branch, \"git merge develop\" works ok -- since this branched off the tree at around 5.13.beta4 I thought that would be helpful to know, since it means (I think) that merging this branch into develop will also work!  And for good measure I will also rebuild and test everything.\n----\nNew commits:",
    "created_at": "2014-01-02T17:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79550",
    "user": "https://github.com/JohnCremona"
}
```

Note that the branch name has changed (it was non-standard, my fault).

I have checked that from this branch, "git merge develop" works ok -- since this branched off the tree at around 5.13.beta4 I thought that would be helpful to know, since it means (I think) that merging this branch into develop will also work!  And for good measure I will also rebuild and test everything.
----
New commits:



---

archive/issue_comments_079551.json:
```json
{
    "body": "I can confirm that after merging the develop branch and rebuilding, all (long) test pass.\n\nNow the only question is, who gives this a positive review?",
    "created_at": "2014-01-02T18:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79551",
    "user": "https://github.com/JohnCremona"
}
```

I can confirm that after merging the develop branch and rebuilding, all (long) test pass.

Now the only question is, who gives this a positive review?



---

archive/issue_comments_079552.json:
```json
{
    "body": "Well, I am happy with your changes, so you can set a positive review if you want.",
    "created_at": "2014-01-02T19:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79552",
    "user": "https://github.com/fchapoton"
}
```

Well, I am happy with your changes, so you can set a positive review if you want.



---

archive/issue_comments_079553.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-01-02T19:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79553",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079554.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-02T22:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79554",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008893.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-01-05T06:54:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8723#event-8893"
}
```



---

archive/issue_comments_079555.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-05T06:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79555",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_079556.json:
```json
{
    "body": "I just stumbled upon this while working on #16129.\n\nReplying to [comment:20 cremona]:\n> New commits:\n> ||[1fec983](http://git.sagemath.org/sage.git/commit/?id=1fec983)||reviewer's patch, makes sure that the parents are correct even with caching||\n\nIf I understand correctly, this is to make sure that the returned elements live in the correct rings. Does this really work the way it is meant to? The `x` in a univariate/bivariate ring can not be distinguished in the cache:\n\n```\nsage: R.<x,y> = QQ[]\nsage: S.<x> = QQ[]\nsage: R(x) == S(x)\nTrue\nsage: hash(R(x))==hash(S(x))\nTrue\n```\n\n\nSo what actually makes the patch work is this explicit conversion back to the right ring:\n\n```\n- mx = self._multiple_x_numerator(m.abs(), x) / self._multiple_x_denominator(m.abs(), x)\n+ mx = (x.parent()(self._multiple_x_numerator(m.abs(), x))\n+ / x.parent()(self._multiple_x_denominator(m.abs(), x)))\n```\n\n\nIn other words, `_multiple_x_numerator/denominator` still return elements in the wrong ring. This is probably acceptable since they are marked as internal methods anyway:\n\n```\nsage: E = EllipticCurve([0,0,0,0,1])\nsage: R.<x,y> = QQ[]\nsage: E._multiple_x_numerator(2, x).parent()\nUnivariate Polynomial Ring in x, y over Rational Field\nsage: E._multiple_x_numerator(2).parent()\nUnivariate Polynomial Ring in x, y over Rational Field\n```\n\n\nShould I fix this in #16129?\n\nWhat causes actual trouble for me is that `x` has been added to the cache key in `division_polynomial_0`. Why is it necessary there? Is `division_polynomial_0` ever called with a different `x` but the same `cache`?",
    "created_at": "2014-04-11T12:38:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79556",
    "user": "https://github.com/saraedum"
}
```

I just stumbled upon this while working on #16129.

Replying to [comment:20 cremona]:
> New commits:
> ||[1fec983](http://git.sagemath.org/sage.git/commit/?id=1fec983)||reviewer's patch, makes sure that the parents are correct even with caching||

If I understand correctly, this is to make sure that the returned elements live in the correct rings. Does this really work the way it is meant to? The `x` in a univariate/bivariate ring can not be distinguished in the cache:

```
sage: R.<x,y> = QQ[]
sage: S.<x> = QQ[]
sage: R(x) == S(x)
True
sage: hash(R(x))==hash(S(x))
True
```


So what actually makes the patch work is this explicit conversion back to the right ring:

```
- mx = self._multiple_x_numerator(m.abs(), x) / self._multiple_x_denominator(m.abs(), x)
+ mx = (x.parent()(self._multiple_x_numerator(m.abs(), x))
+ / x.parent()(self._multiple_x_denominator(m.abs(), x)))
```


In other words, `_multiple_x_numerator/denominator` still return elements in the wrong ring. This is probably acceptable since they are marked as internal methods anyway:

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: R.<x,y> = QQ[]
sage: E._multiple_x_numerator(2, x).parent()
Univariate Polynomial Ring in x, y over Rational Field
sage: E._multiple_x_numerator(2).parent()
Univariate Polynomial Ring in x, y over Rational Field
```


Should I fix this in #16129?

What causes actual trouble for me is that `x` has been added to the cache key in `division_polynomial_0`. Why is it necessary there? Is `division_polynomial_0` ever called with a different `x` but the same `cache`?



---

archive/issue_comments_079557.json:
```json
{
    "body": "I think the quick answer to the last question is \"yes\".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed, there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.  So there has to be a different cache for different values of x.\n\nIf your fix at #16129 does a better job while respecting this -- good!",
    "created_at": "2014-04-11T15:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79557",
    "user": "https://github.com/JohnCremona"
}
```

I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed, there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.  So there has to be a different cache for different values of x.

If your fix at #16129 does a better job while respecting this -- good!



---

archive/issue_comments_079558.json:
```json
{
    "body": "Replying to [comment:34 cremona]:\n> I think the quick answer to the last question is \"yes\".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,\nBut this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.\n\n```\nsage: E = EllipticCurve([0,0,0,0,1])\nsage: R.<x,y> = QQ[]\nsage: cache = {}\nsage: E.division_polynomial_0(1, cache=cache).parent()\nUnivariate Polynomial Ring in x over Rational Field\nsage: E.division_polynomial_0(1, x, cache=cache).parent()\nUnivariate Polynomial Ring in x over Rational Field\n```\n\n\n> there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.\nI see. But would you really want to store these in the same `cache` dictionary?\n\nIf I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?",
    "created_at": "2014-04-11T20:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79558",
    "user": "https://github.com/saraedum"
}
```

Replying to [comment:34 cremona]:
> I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,
But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: R.<x,y> = QQ[]
sage: cache = {}
sage: E.division_polynomial_0(1, cache=cache).parent()
Univariate Polynomial Ring in x over Rational Field
sage: E.division_polynomial_0(1, x, cache=cache).parent()
Univariate Polynomial Ring in x over Rational Field
```


> there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.
I see. But would you really want to store these in the same `cache` dictionary?

If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?



---

archive/issue_comments_079559.json:
```json
{
    "body": "Replying to [comment:35 saraedum]:\n> Replying to [comment:34 cremona]:\n> > I think the quick answer to the last question is \"yes\".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,\n> But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.\n> {{{\n> sage: E = EllipticCurve([0,0,0,0,1])\n> sage: R.<x,y> = QQ[]\n> sage: cache = {}\n> sage: E.division_polynomial_0(1, cache=cache).parent()\n> Univariate Polynomial Ring in x over Rational Field\n> sage: E.division_polynomial_0(1, x, cache=cache).parent()\n> Univariate Polynomial Ring in x over Rational Field\n> }}}\n> \n> > there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.\n> I see. But would you really want to store these in the same `cache` dictionary?\n> \n> If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?\n\nNo, absolutely not.  The cache variable is not intended for use by users at all.  (I did not design this!).  It is for internal use so that the function for one value of n can re-use its values for smaller n and the same x.  I'm sure there are are other (and possibly better) ways to do it.",
    "created_at": "2014-04-11T20:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79559",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:35 saraedum]:
> Replying to [comment:34 cremona]:
> > I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,
> But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.
> {{{
> sage: E = EllipticCurve([0,0,0,0,1])
> sage: R.<x,y> = QQ[]
> sage: cache = {}
> sage: E.division_polynomial_0(1, cache=cache).parent()
> Univariate Polynomial Ring in x over Rational Field
> sage: E.division_polynomial_0(1, x, cache=cache).parent()
> Univariate Polynomial Ring in x over Rational Field
> }}}
> 
> > there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.
> I see. But would you really want to store these in the same `cache` dictionary?
> 
> If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?

No, absolutely not.  The cache variable is not intended for use by users at all.  (I did not design this!).  It is for internal use so that the function for one value of n can re-use its values for smaller n and the same x.  I'm sure there are are other (and possibly better) ways to do it.



---

archive/issue_comments_079560.json:
```json
{
    "body": "Replying to [comment:36 cremona]:\n> Replying to [comment:35 saraedum]:\n> > Replying to [comment:34 cremona]:\n> > > I think the quick answer to the last question is \"yes\".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,\n> > But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.\n> > {{{\n> > sage: E = EllipticCurve([0,0,0,0,1])\n> > sage: R.<x,y> = QQ[]\n> > sage: cache = {}\n> > sage: E.division_polynomial_0(1, cache=cache).parent()\n> > Univariate Polynomial Ring in x over Rational Field\n> > sage: E.division_polynomial_0(1, x, cache=cache).parent()\n> > Univariate Polynomial Ring in x over Rational Field\n> > }}}\n> > \n> > > there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.\n> > I see. But would you really want to store these in the same `cache` dictionary?\n> > \n> > If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?\n> \n> No, absolutely not.  The cache variable is not intended for use by users at all.  (I did not design this!).  It is for internal use so that the function for one value of n can re-use its values for smaller n and the same x.  I'm sure there are are other (and possibly better) ways to do it.\n\nGreat. Thanks for your answers. I will try to implement this in a different way at #16129 then.",
    "created_at": "2014-04-11T20:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8723#issuecomment-79560",
    "user": "https://github.com/saraedum"
}
```

Replying to [comment:36 cremona]:
> Replying to [comment:35 saraedum]:
> > Replying to [comment:34 cremona]:
> > > I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,
> > But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.
> > {{{
> > sage: E = EllipticCurve([0,0,0,0,1])
> > sage: R.<x,y> = QQ[]
> > sage: cache = {}
> > sage: E.division_polynomial_0(1, cache=cache).parent()
> > Univariate Polynomial Ring in x over Rational Field
> > sage: E.division_polynomial_0(1, x, cache=cache).parent()
> > Univariate Polynomial Ring in x over Rational Field
> > }}}
> > 
> > > there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.
> > I see. But would you really want to store these in the same `cache` dictionary?
> > 
> > If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?
> 
> No, absolutely not.  The cache variable is not intended for use by users at all.  (I did not design this!).  It is for internal use so that the function for one value of n can re-use its values for smaller n and the same x.  I'm sure there are are other (and possibly better) ways to do it.

Great. Thanks for your answers. I will try to implement this in a different way at #16129 then.
