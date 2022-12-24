# Issue 6886: Elliptic curve isogeny checking can be expensive

archive/issues_006886.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @categorie shumow\n\nKeywords: elliptic curve isogeny\n\nIn #6384, code was introduced to check whether the kernel polynomial provided by the user was valid, by checking that it divides the appropriate division polynomial.\n\nThis can be too expensive!  I have been working with isogenies of degree 163 over QQ, for which computing the 163-division polynomial takes many hours.  So I want to introduce a check parameter to the isogeny construction, default True, so that users (or other code) can switch off this check (when they \"know\" they are right!).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6886\n\n",
    "created_at": "2009-09-04T08:58:56Z",
    "labels": [
        "elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Elliptic curve isogeny checking can be expensive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6886",
    "user": "@JohnCremona"
}
```
Assignee: @loefflerd

CC:  @categorie shumow

Keywords: elliptic curve isogeny

In #6384, code was introduced to check whether the kernel polynomial provided by the user was valid, by checking that it divides the appropriate division polynomial.

This can be too expensive!  I have been working with isogenies of degree 163 over QQ, for which computing the 163-division polynomial takes many hours.  So I want to introduce a check parameter to the isogeny construction, default True, so that users (or other code) can switch off this check (when they "know" they are right!).


Issue created by migration from https://trac.sagemath.org/ticket/6886





---

archive/issue_comments_056896.json:
```json
{
    "body": "Attachment [trac_6886.patch](tarball://root/attachments/some-uuid/ticket6886/trac_6886.patch) by @categorie created at 2009-10-08 21:55:38\n\nAn optional argument 'check' is added to isogenies for elliptic curves.",
    "created_at": "2009-10-08T21:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56896",
    "user": "@categorie"
}
```

Attachment [trac_6886.patch](tarball://root/attachments/some-uuid/ticket6886/trac_6886.patch) by @categorie created at 2009-10-08 21:55:38

An optional argument 'check' is added to isogenies for elliptic curves.



---

archive/issue_comments_056897.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-08T21:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56897",
    "user": "@categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056898.json:
```json
{
    "body": "Thanks, Chris -- I will test the patch when I can.  Another situation where this will help is for curves over QQbar, where (at present) the order of points cannot be obtained.  [I was thinking of adding this by coercing everything into a suitable number field, though I fear it would be quite expensive.]",
    "created_at": "2009-10-08T22:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56898",
    "user": "@JohnCremona"
}
```

Thanks, Chris -- I will test the patch when I can.  Another situation where this will help is for curves over QQbar, where (at present) the order of points cannot be obtained.  [I was thinking of adding this by coercing everything into a suitable number field, though I fear it would be quite expensive.]



---

archive/issue_comments_056899.json:
```json
{
    "body": "documentation for it; to be applied after the first",
    "created_at": "2009-10-09T09:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56899",
    "user": "@categorie"
}
```

documentation for it; to be applied after the first



---

archive/issue_comments_056900.json:
```json
{
    "body": "Attachment [trac_6886_doc.patch](tarball://root/attachments/some-uuid/ticket6886/trac_6886_doc.patch) by @categorie created at 2009-10-09 09:06:23\n\nI forgot to add the documentation. The second patch (to be applied after the first) fixes that.\n\nIf check is false and a (or several) presumably-torsion points are given, the algorithm does not check if they are really torsion anymore. But it still needs the function .order(). I think we should open another ticket for this.\n\nChris.",
    "created_at": "2009-10-09T09:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56900",
    "user": "@categorie"
}
```

Attachment [trac_6886_doc.patch](tarball://root/attachments/some-uuid/ticket6886/trac_6886_doc.patch) by @categorie created at 2009-10-09 09:06:23

I forgot to add the documentation. The second patch (to be applied after the first) fixes that.

If check is false and a (or several) presumably-torsion points are given, the algorithm does not check if they are really torsion anymore. But it still needs the function .order(). I think we should open another ticket for this.

Chris.



---

archive/issue_comments_056901.json:
```json
{
    "body": "Remove assignee @loefflerd.",
    "created_at": "2009-10-09T09:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56901",
    "user": "@loefflerd"
}
```

Remove assignee @loefflerd.



---

archive/issue_comments_056902.json:
```json
{
    "body": "The patches look good, apply to 4.1.2.rc0 and all elliptic curves tests pass.  Even better, the patch I am currently working on for #6887 applies fine on top of these, and I will make anything I post at #6887 depend on this one.  It may happen that I further develop the checking code on that ticket, but this is good to go in now -- it can get into 4.1.2 while the new stuff in #6887 had better wait since it does a lot of new stuff.\n\nI have been thinking of a better way of testing the validity of a kernel polynomial, and currently have an idea (not implemented ) which would work in the case of a cyclic kernel.",
    "created_at": "2009-10-11T11:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56902",
    "user": "@JohnCremona"
}
```

The patches look good, apply to 4.1.2.rc0 and all elliptic curves tests pass.  Even better, the patch I am currently working on for #6887 applies fine on top of these, and I will make anything I post at #6887 depend on this one.  It may happen that I further develop the checking code on that ticket, but this is good to go in now -- it can get into 4.1.2 while the new stuff in #6887 had better wait since it does a lot of new stuff.

I have been thinking of a better way of testing the validity of a kernel polynomial, and currently have an idea (not implemented ) which would work in the case of a cyclic kernel.



---

archive/issue_comments_056903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-11T11:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56903",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-19T06:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6886#issuecomment-56904",
    "user": "@mwhansen"
}
```

Resolution: fixed
