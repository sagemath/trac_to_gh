# Issue 2767: error in elem.matrix(F) and elem.norm(F) for F == elem.parent() a number field

archive/issues_002767.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\nKeywords: number field norm matrix\n\n\n```\nsage: F.<z> = CyclotomicField(5)\nsage: F.<z> = CyclotomicField(5)\nsage: t = 3*z^3 + 4*z^2 + 2\nsage: t.norm()\n251\nsage: t.norm(F)\n2\nsage: t.matrix(F)\n[2]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2767\n\n",
    "created_at": "2008-04-02T04:54:31Z",
    "labels": [
        "number theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "error in elem.matrix(F) and elem.norm(F) for F == elem.parent() a number field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2767",
    "user": "@ncalexan"
}
```
Assignee: @williamstein

CC:  @ncalexan

Keywords: number field norm matrix


```
sage: F.<z> = CyclotomicField(5)
sage: F.<z> = CyclotomicField(5)
sage: t = 3*z^3 + 4*z^2 + 2
sage: t.norm()
251
sage: t.norm(F)
2
sage: t.matrix(F)
[2]
```


Issue created by migration from https://trac.sagemath.org/ticket/2767





---

archive/issue_comments_019004.json:
```json
{
    "body": "`ncalexan` and `wstein` looked at this for a few minutes, and discovered that the root cause was that my \"fix\" for #1083 really only worked in the case that the absolute extension was of degree 2. (Sloppy testing on my part.) So, I'm fixing this.\n\nThe bug is really in `sage/rings/number_field/maps.py`, around line 122. We are given an absolute polynomial, and we want to convert it into a relative polynomial. However, in this case, we want to return a polynomial of degree 0 in the generator for L/K. So if our original element is represented by the absolute polynomial a<sub>n</sub>x<sup>n</sup> + ... + a<sub>1</sub>x + a<sub>0</sub> , and our extension is defined by `x-m`, for `m` an element of K (note that one cannot currently define a relative extension by a non-monic polynomial), then we want to return a<sub>n</sub>m<sup>n</sup> + ... + a<sub>1</sub>m + a<sub>0</sub>. Now `m` is just `-1*L.pari_rnf()[0][0]`, so we just evaluate our polynomial there. This will always give us a constant polynomial that's exactly what we want.\n\nIf there's some case that I'm not thinking of here, let me know. I've tested it on various degrees, and with relative polynomials other than just `x-a`, and it works in every case I could come up with.",
    "created_at": "2008-04-02T07:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19004",
    "user": "@craigcitro"
}
```

`ncalexan` and `wstein` looked at this for a few minutes, and discovered that the root cause was that my "fix" for #1083 really only worked in the case that the absolute extension was of degree 2. (Sloppy testing on my part.) So, I'm fixing this.

The bug is really in `sage/rings/number_field/maps.py`, around line 122. We are given an absolute polynomial, and we want to convert it into a relative polynomial. However, in this case, we want to return a polynomial of degree 0 in the generator for L/K. So if our original element is represented by the absolute polynomial a<sub>n</sub>x<sup>n</sup> + ... + a<sub>1</sub>x + a<sub>0</sub> , and our extension is defined by `x-m`, for `m` an element of K (note that one cannot currently define a relative extension by a non-monic polynomial), then we want to return a<sub>n</sub>m<sup>n</sup> + ... + a<sub>1</sub>m + a<sub>0</sub>. Now `m` is just `-1*L.pari_rnf()[0][0]`, so we just evaluate our polynomial there. This will always give us a constant polynomial that's exactly what we want.

If there's some case that I'm not thinking of here, let me know. I've tested it on various degrees, and with relative polynomials other than just `x-a`, and it works in every case I could come up with.



---

archive/issue_comments_019005.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-04-02T07:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19005",
    "user": "@craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_019006.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-02T07:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19006",
    "user": "@craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019007.json:
```json
{
    "body": "Attachment [trac-2767.patch](tarball://root/attachments/some-uuid/ticket2767/trac-2767.patch) by @craigcitro created at 2008-04-02 07:23:13",
    "created_at": "2008-04-02T07:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19007",
    "user": "@craigcitro"
}
```

Attachment [trac-2767.patch](tarball://root/attachments/some-uuid/ticket2767/trac-2767.patch) by @craigcitro created at 2008-04-02 07:23:13



---

archive/issue_comments_019008.json:
```json
{
    "body": "Does this handle fields with unusual defining polynomials, such as F = L.extension(2*x - L.gen())?  I don't think it will.\n\nNick",
    "created_at": "2008-04-03T04:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19008",
    "user": "@ncalexan"
}
```

Does this handle fields with unusual defining polynomials, such as F = L.extension(2*x - L.gen())?  I don't think it will.

Nick



---

archive/issue_comments_019009.json:
```json
{
    "body": "After discussion on IRC, reviewed positive:\n\n\n```\ncraigcitro: hey ncalexan -- did you see i posted a patch for the thing you were looking at last night?\n[9:11pm] ncalexan: craigcitro: yes, I just commented on it.  I don't think it will handle polys like 2*x - a, will you check?\n[9:12pm] craigcitro: you're right -- but you can't create an extension with such a poly\n[9:12pm] craigcitro: (i checked it when i was looking at it)\n[9:12pm] ncalexan: Someday I hope to address that, but okay.\n[9:12pm] craigcitro: nod\n[9:12pm] ncalexan: Comment on the patch, then I'll review positive.\n[9:13pm] ncalexan: Actually, wait -- what about x - 2*a?\n[9:13pm] craigcitro: that works fine\n[9:13pm] craigcitro: i checked those\n[9:13pm] ncalexan: You're assuming that x = rel gen when you look at f(rel gen), right?\n[9:13pm] craigcitro: then i tried 2*x - a\n[9:13pm] craigcitro: and discovered it didn't work\n[9:14pm] craigcitro: if the rel poly is x-foo\n[9:14pm] ncalexan: Well, there's a test with x - a/2.\n[9:14pm] craigcitro: i just plug foo in.\n[9:14pm] ncalexan: Okay.  I'll review positive.\n```\n",
    "created_at": "2008-04-03T04:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19009",
    "user": "@ncalexan"
}
```

After discussion on IRC, reviewed positive:


```
craigcitro: hey ncalexan -- did you see i posted a patch for the thing you were looking at last night?
[9:11pm] ncalexan: craigcitro: yes, I just commented on it.  I don't think it will handle polys like 2*x - a, will you check?
[9:12pm] craigcitro: you're right -- but you can't create an extension with such a poly
[9:12pm] craigcitro: (i checked it when i was looking at it)
[9:12pm] ncalexan: Someday I hope to address that, but okay.
[9:12pm] craigcitro: nod
[9:12pm] ncalexan: Comment on the patch, then I'll review positive.
[9:13pm] ncalexan: Actually, wait -- what about x - 2*a?
[9:13pm] craigcitro: that works fine
[9:13pm] craigcitro: i checked those
[9:13pm] ncalexan: You're assuming that x = rel gen when you look at f(rel gen), right?
[9:13pm] craigcitro: then i tried 2*x - a
[9:13pm] craigcitro: and discovered it didn't work
[9:14pm] craigcitro: if the rel poly is x-foo
[9:14pm] ncalexan: Well, there's a test with x - a/2.
[9:14pm] craigcitro: i just plug foo in.
[9:14pm] ncalexan: Okay.  I'll review positive.
```




---

archive/issue_comments_019010.json:
```json
{
    "body": "Doctests pass for me.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T08:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19010",
    "user": "mabshoff"
}
```

Doctests pass for me.

Cheers,

Michael



---

archive/issue_comments_019011.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-03T08:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19011",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_019012.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T08:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2767#issuecomment-19012",
    "user": "mabshoff"
}
```

Resolution: fixed
