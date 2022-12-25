# Issue 2103: equivalence classes of cusps for congruence subgroups

archive/issues_002103.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  alexghitza @craigcitro @JohnCremona m.t.aranes@warwick.ac.uk\n\nGiven a congruence subgroup G, return a list of representatives for the G-equivalence classes of cusps.\n\nSample wished-for session:\n\n\n```\nsage: C = Cusps\nsage: G = Gamma0(5)\nsage: C(G)\n[Infinity, 0]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2103\n\n",
    "created_at": "2008-02-08T07:46:52Z",
    "labels": [
        "component: modular forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "equivalence classes of cusps for congruence subgroups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2103",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

CC:  alexghitza @craigcitro @JohnCremona m.t.aranes@warwick.ac.uk

Given a congruence subgroup G, return a list of representatives for the G-equivalence classes of cusps.

Sample wished-for session:


```
sage: C = Cusps
sage: G = Gamma0(5)
sage: C(G)
[Infinity, 0]
```



Issue created by migration from https://trac.sagemath.org/ticket/2103





---

archive/issue_comments_013671.json:
```json
{
    "body": "I'd also like this. I'll have a go at it.",
    "created_at": "2008-09-21T18:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13671",
    "user": "https://github.com/loefflerd"
}
```

I'd also like this. I'll have a go at it.



---

archive/issue_comments_013672.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2008-09-21T18:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13672",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_013673.json:
```json
{
    "body": "Attachment [2103.patch](tarball://root/attachments/some-uuid/ticket2103/2103.patch) by @loefflerd created at 2008-09-22 18:25:18\n\npatch against 3.1.2",
    "created_at": "2008-09-22T18:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13673",
    "user": "https://github.com/loefflerd"
}
```

Attachment [2103.patch](tarball://root/attachments/some-uuid/ticket2103/2103.patch) by @loefflerd created at 2008-09-22 18:25:18

patch against 3.1.2



---

archive/issue_comments_013674.json:
```json
{
    "body": "The above patch adds a cusps() method for all congruence subgroups; this accepts an optional boolean keyword argument \"bdmap\". \n\nIf \"bdmap\" is true, then the method creates the space of modular symbols for the congruence subgroup and calls the .cusps() method on this, which triggers computation of the boundary map; the existing code for computing the boundary map also gives the set of cusps as a side-effect. They aren't computed in reduced form, though, so we reduce them and pass them back to the user.\n\nIf \"bdmap\" is false (the default), the method finds all cusps by directly calculating the appropriate list of rational numbers -- there are two hidden helper methods, one to do this for Gamma0 and another for Gamma1 and GammaH. This is *much* faster than computing the boundary map if N is large. \n\nI've also added a reduce_cusp method, which is essentially a wrapper around Craig Citro's _reduce_cusp method but throws away the extra output of a sign, since that's not so important\noutside the specific context of modular symbol boundary maps.\n\nIn the course of fixing this, I've also made some other changes: I found that existing code gives\n\n``` \nsage: Gamma1(11) == GammaH(11, [])\nFalse\nsage: Gamma0(11) == GammaH(11, [2])\nFalse\n```\n\ndespite the fact that in both cases the two groups are the same.\n\nHence I've adjusted things so that Gamma0 and Gamma1 inherit from GammaH, and use the GammaH __cmp__ methods. Things are now much more consistent, but there was a slight side-effect of breaking a doctest in abvar/abvar.py as the sort order of congruence subgroups has changed -- there is no way to avoid this, because at the moment we have the following: \n\n```\nsage: Gamma1(11) < Gamma0(11)\nFalse\nsage: GammaH(11, []) < GammaH(11, [2])\nTrue\n```\n\n\nI know that having cusps() as a method of congruence subgroups isn't the syntax originally proposed, but I don't like the idea of using Cusps_class.__call__(). If anyone feels strongly about this I'll happily add methods to Cusps_class so one can say\n\n```\nsage: Cusps.orbit_reps(Gamma1(11))\n...\n```\n\nor whatever.",
    "created_at": "2008-09-22T19:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13674",
    "user": "https://github.com/loefflerd"
}
```

The above patch adds a cusps() method for all congruence subgroups; this accepts an optional boolean keyword argument "bdmap". 

If "bdmap" is true, then the method creates the space of modular symbols for the congruence subgroup and calls the .cusps() method on this, which triggers computation of the boundary map; the existing code for computing the boundary map also gives the set of cusps as a side-effect. They aren't computed in reduced form, though, so we reduce them and pass them back to the user.

If "bdmap" is false (the default), the method finds all cusps by directly calculating the appropriate list of rational numbers -- there are two hidden helper methods, one to do this for Gamma0 and another for Gamma1 and GammaH. This is *much* faster than computing the boundary map if N is large. 

I've also added a reduce_cusp method, which is essentially a wrapper around Craig Citro's _reduce_cusp method but throws away the extra output of a sign, since that's not so important
outside the specific context of modular symbol boundary maps.

In the course of fixing this, I've also made some other changes: I found that existing code gives

``` 
sage: Gamma1(11) == GammaH(11, [])
False
sage: Gamma0(11) == GammaH(11, [2])
False
```

despite the fact that in both cases the two groups are the same.

Hence I've adjusted things so that Gamma0 and Gamma1 inherit from GammaH, and use the GammaH __cmp__ methods. Things are now much more consistent, but there was a slight side-effect of breaking a doctest in abvar/abvar.py as the sort order of congruence subgroups has changed -- there is no way to avoid this, because at the moment we have the following: 

```
sage: Gamma1(11) < Gamma0(11)
False
sage: GammaH(11, []) < GammaH(11, [2])
True
```


I know that having cusps() as a method of congruence subgroups isn't the syntax originally proposed, but I don't like the idea of using Cusps_class.__call__(). If anyone feels strongly about this I'll happily add methods to Cusps_class so one can say

```
sage: Cusps.orbit_reps(Gamma1(11))
...
```

or whatever.



---

archive/issue_comments_013675.json:
```json
{
    "body": "I've added myself on the CC list for this.  My student Maite Aranes is in the process of implementing cusps for general number fields, by the way, but I have not yet made a ticket for it.",
    "created_at": "2008-09-23T11:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13675",
    "user": "https://github.com/JohnCremona"
}
```

I've added myself on the CC list for this.  My student Maite Aranes is in the process of implementing cusps for general number fields, by the way, but I have not yet made a ticket for it.



---

archive/issue_comments_013676.json:
```json
{
    "body": "For the patch **2103.patch**, here's a possible fix for improving the documentation:\n\n\n\n```\n-Since Gamma0(N) always, contains the matrix -1, this always\n+Since Gamma0(N) always contains the matrix -1, this always\n```\n\nAfter applying that diff, you'd get:\n\n```\nReturn True precisely if this subgroup contains the matrix -1. \n\nSince Gamma0(N) always contains the matrix -1, this always \nreturns True.\n```\n",
    "created_at": "2008-10-27T12:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13676",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

For the patch **2103.patch**, here's a possible fix for improving the documentation:



```
-Since Gamma0(N) always, contains the matrix -1, this always
+Since Gamma0(N) always contains the matrix -1, this always
```

After applying that diff, you'd get:

```
Return True precisely if this subgroup contains the matrix -1. 

Since Gamma0(N) always contains the matrix -1, this always 
returns True.
```




---

archive/issue_comments_013677.json:
```json
{
    "body": "\n```\napplying /local/jec/2103.patch\npatching file sage/modular/congroup.py\nHunk #3 FAILED at 589\n1 out of 10 hunks FAILED -- saving rejects to file sage/modular/congroup.py.rej\nabort: patch failed to apply\n```\n\n\nSame on both 3.1.4 and 3.2.apha0.  David, could you rebase this?  Then I'll review it.\n\nWhile I'm here: am I right in thinking that there's quite a lot of code which is just moved from one place to another?  (Judging by the amount of red and blue I see when viewing the patch).\n\nI certainly like the code from looking at it by eye but it needs to be able to be applied...\n\nMy guess is that the code for giving a complete set of cusp representatives is not very efficient, but I also think it unlikely that that function would be needed for large N anyway.  I never wrote down explicit representatives even for Gamma_0(N), but think that you should have all a/d where 0<d|N and a runs through invertible residues mod gcd(d,N/d) lifted to be coprime to d.",
    "created_at": "2008-10-27T12:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13677",
    "user": "https://github.com/JohnCremona"
}
```


```
applying /local/jec/2103.patch
patching file sage/modular/congroup.py
Hunk #3 FAILED at 589
1 out of 10 hunks FAILED -- saving rejects to file sage/modular/congroup.py.rej
abort: patch failed to apply
```


Same on both 3.1.4 and 3.2.apha0.  David, could you rebase this?  Then I'll review it.

While I'm here: am I right in thinking that there's quite a lot of code which is just moved from one place to another?  (Judging by the amount of red and blue I see when viewing the patch).

I certainly like the code from looking at it by eye but it needs to be able to be applied...

My guess is that the code for giving a complete set of cusp representatives is not very efficient, but I also think it unlikely that that function would be needed for large N anyway.  I never wrote down explicit representatives even for Gamma_0(N), but think that you should have all a/d where 0<d|N and a runs through invertible residues mod gcd(d,N/d) lifted to be coprime to d.



---

archive/issue_comments_013678.json:
```json
{
    "body": "Attachment [2103-rebased.patch](tarball://root/attachments/some-uuid/ticket2103/2103-rebased.patch) by @loefflerd created at 2008-10-28 11:14:51\n\nrebased to 3.1.4 (also works in 3.2.alpha1)",
    "created_at": "2008-10-28T11:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13678",
    "user": "https://github.com/loefflerd"
}
```

Attachment [2103-rebased.patch](tarball://root/attachments/some-uuid/ticket2103/2103-rebased.patch) by @loefflerd created at 2008-10-28 11:14:51

rebased to 3.1.4 (also works in 3.2.alpha1)



---

archive/issue_comments_013679.json:
```json
{
    "body": "It was conflicting with mhansen's changeset 10648, deprecating is_blah() functions. I've uploaded a new patch (also incorporating mvngu's docstring fix), which was created under 3.1.4 and seems to apply fine to 3.2.alpha1 as well.",
    "created_at": "2008-10-28T11:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13679",
    "user": "https://github.com/loefflerd"
}
```

It was conflicting with mhansen's changeset 10648, deprecating is_blah() functions. I've uploaded a new patch (also incorporating mvngu's docstring fix), which was created under 3.1.4 and seems to apply fine to 3.2.alpha1 as well.



---

archive/issue_comments_013680.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-28T11:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13680",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013681.json:
```json
{
    "body": "FYI: With the patch applied against 3.2.alpha1+merges all doctests with -long pass.\n\nA couple docstrings and doctests are missing for\n\n* def dimension_modular_forms_H(X, k=2) in line 1488 of sage/modular/dims.py\n* def dimension_modular_forms_H(X, k=2) in line 1534 of sage/modular/dims.py\n\nMathematically I am not qualified to review :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T17:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13681",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: With the patch applied against 3.2.alpha1+merges all doctests with -long pass.

A couple docstrings and doctests are missing for

* def dimension_modular_forms_H(X, k=2) in line 1488 of sage/modular/dims.py
* def dimension_modular_forms_H(X, k=2) in line 1534 of sage/modular/dims.py

Mathematically I am not qualified to review :)

Cheers,

Michael



---

archive/issue_comments_013682.json:
```json
{
    "body": "Attachment [2103-new.patch](tarball://root/attachments/some-uuid/ticket2103/2103-new.patch) by @loefflerd created at 2008-10-28 18:32:02",
    "created_at": "2008-10-28T18:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13682",
    "user": "https://github.com/loefflerd"
}
```

Attachment [2103-new.patch](tarball://root/attachments/some-uuid/ticket2103/2103-new.patch) by @loefflerd created at 2008-10-28 18:32:02



---

archive/issue_comments_013683.json:
```json
{
    "body": "Oops! The same function appears twice in dims.py, with identical code both times -- that was silly of me. I have recreated the patch with only one copy of dimension_modular_forms_H, and added a doctest for it.",
    "created_at": "2008-10-28T18:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13683",
    "user": "https://github.com/loefflerd"
}
```

Oops! The same function appears twice in dims.py, with identical code both times -- that was silly of me. I have recreated the patch with only one copy of dimension_modular_forms_H, and added a doctest for it.



---

archive/issue_comments_013684.json:
```json
{
    "body": "Ok, I'm in the process of reviewing this -- I'll have it done in a little bit.",
    "created_at": "2008-10-28T20:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13684",
    "user": "https://github.com/craigcitro"
}
```

Ok, I'm in the process of reviewing this -- I'll have it done in a little bit.



---

archive/issue_comments_013685.json:
```json
{
    "body": "Attachment [trac-2103-pt2.patch](tarball://root/attachments/some-uuid/ticket2103/trac-2103-pt2.patch) by @craigcitro created at 2008-10-29 09:41:52\n\nThis is an excellent patch. \n\nIn addition to adding the requested functionality, this patch performs some long-needed cleanup to the class hierarchy in `congroup.py`. In particular, `Gamma0` and `Gamma1` now inherit from `GammaH`, as makes sense. I should note that it might be a good project for someone to look at the code in `congroup.py`, and see how much of the code for `Gamma0` and `Gamma1` could be moved up to/unified with code in `GammaH`. \n\nI've added a small patch to apply on top of `2103-new.patch` which cleans up a few things. Most of it is documentation touch-ups. I replaced the `__cmp__` methods for `Gamma0` and `Gamma1` which the original patch removed, and rewrote them to do comparison without ever generating the corresponding lists of elements. \n\nSomeone should look over my additional patch, but after that, this is ready to go.",
    "created_at": "2008-10-29T09:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13685",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-2103-pt2.patch](tarball://root/attachments/some-uuid/ticket2103/trac-2103-pt2.patch) by @craigcitro created at 2008-10-29 09:41:52

This is an excellent patch. 

In addition to adding the requested functionality, this patch performs some long-needed cleanup to the class hierarchy in `congroup.py`. In particular, `Gamma0` and `Gamma1` now inherit from `GammaH`, as makes sense. I should note that it might be a good project for someone to look at the code in `congroup.py`, and see how much of the code for `Gamma0` and `Gamma1` could be moved up to/unified with code in `GammaH`. 

I've added a small patch to apply on top of `2103-new.patch` which cleans up a few things. Most of it is documentation touch-ups. I replaced the `__cmp__` methods for `Gamma0` and `Gamma1` which the original patch removed, and rewrote them to do comparison without ever generating the corresponding lists of elements. 

Someone should look over my additional patch, but after that, this is ready to go.



---

archive/issue_comments_013686.json:
```json
{
    "body": "Craig's additional patch looks good to me;  though I don't have time at the moment to check that everything works properly.",
    "created_at": "2008-10-29T09:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13686",
    "user": "https://github.com/JohnCremona"
}
```

Craig's additional patch looks good to me;  though I don't have time at the moment to check that everything works properly.



---

archive/issue_comments_013687.json:
```json
{
    "body": "1. Note that only the last two patches should be applied: 2103-new.patch and trac-2103-pt2.patch\n    2. They apply cleanly to 3.2.alpha1\n    3. All tests in sage/modular pass\n\nI am happy to give this a positive review, reinforcing Craig's.",
    "created_at": "2008-10-29T12:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13687",
    "user": "https://github.com/JohnCremona"
}
```

1. Note that only the last two patches should be applied: 2103-new.patch and trac-2103-pt2.patch
    2. They apply cleanly to 3.2.alpha1
    3. All tests in sage/modular pass

I am happy to give this a positive review, reinforcing Craig's.



---

archive/issue_comments_013688.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-29T13:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013689.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-29T13:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2103",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2103#issuecomment-13689",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2
