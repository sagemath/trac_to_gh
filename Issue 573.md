# Issue 573: word_problem bug in permgroup_element

archive/issues_000573.json:
```json
{
    "body": "Assignee: wdj\n\nCC:  sage-combinat\n\nKeywords: EpimorphismFromFreeGroup, PreImagesRepresentative, RubiksCube, CubeGroup\n\n\n```\nsage: rubik = CubeGroup()\nsage: G = rubik.group()\nsage: Z = G.center()\nsage: superflip = Z.list()[1]\nsage: superflip\n\n(2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,\n47)\nsage: r = rubik.R(); l = rubik.L(); f = rubik.F()\nsage: b = rubik.B(); u = rubik.U(); d = rubik.D()\nsage: superflip in G\nTrue\nsage: superflip.word_problem([b,d,f,l,r,u])\n          x1^-1\n          [['(33,35,40,38)(34,37,39,36)(3,9,46,32)(2,12,47,29)(1,14,48,27)', -1]]\n'(33,35,40,38)(34,37,39,36)(3,9,46,32)(2,12,47,29)(1,14,48,27)^-1'\nsage: ########## wrong #############\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/573\n\n",
    "created_at": "2007-09-03T11:40:55Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "word_problem bug in permgroup_element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/573",
    "user": "wdj"
}
```
Assignee: wdj

CC:  sage-combinat

Keywords: EpimorphismFromFreeGroup, PreImagesRepresentative, RubiksCube, CubeGroup


```
sage: rubik = CubeGroup()
sage: G = rubik.group()
sage: Z = G.center()
sage: superflip = Z.list()[1]
sage: superflip

(2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,
47)
sage: r = rubik.R(); l = rubik.L(); f = rubik.F()
sage: b = rubik.B(); u = rubik.U(); d = rubik.D()
sage: superflip in G
True
sage: superflip.word_problem([b,d,f,l,r,u])
          x1^-1
          [['(33,35,40,38)(34,37,39,36)(3,9,46,32)(2,12,47,29)(1,14,48,27)', -1]]
'(33,35,40,38)(34,37,39,36)(3,9,46,32)(2,12,47,29)(1,14,48,27)^-1'
sage: ########## wrong #############
```


Issue created by migration from https://trac.sagemath.org/ticket/573





---

archive/issue_comments_002976.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T20:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/573#issuecomment-2976",
    "user": "robertwb"
}
```

Resolution: fixed



---

archive/issue_comments_002977.json:
```json
{
    "body": "Attachment [permgroup-fix.hg](tarball://root/attachments/some-uuid/ticket573/permgroup-fix.hg) by robertwb created at 2007-09-06 20:18:08\n\nThis was due to superflip being viewed as an element of Z (with one generator). Obviously the solution was trivial. \n\nI've updated it so it now casts the element into the parent of words.",
    "created_at": "2007-09-06T20:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/573#issuecomment-2977",
    "user": "robertwb"
}
```

Attachment [permgroup-fix.hg](tarball://root/attachments/some-uuid/ticket573/permgroup-fix.hg) by robertwb created at 2007-09-06 20:18:08

This was due to superflip being viewed as an element of Z (with one generator). Obviously the solution was trivial. 

I've updated it so it now casts the element into the parent of words.



---

archive/issue_comments_002978.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-06T20:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/573#issuecomment-2978",
    "user": "robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002979.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-06T20:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/573#issuecomment-2979",
    "user": "robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/573#issuecomment-2980",
    "user": "was"
}
```

Resolution: fixed
