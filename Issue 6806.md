# Issue 6806: typo in patch of ticket #6396: primes_of_degree_one is broken for relative extensions

archive/issues_006806.json:
```json
{
    "body": "Assignee: tba\n\nCC:  davidloeffler ncalexan\n\nThe patch trac_6396-deg1primes.patch at ticket #6396 has this docstring:\n\n```\n201             We test that #6396 is fixed. Note that the doctest is flagged as random\n202             since the string representation of ideals is somewhat unpredictable.::\n203\n204                 sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])\n205                 sage: ids = N.primes_of_degree_one_list(10); a # random\n206                 [Fractional ideal ((-1/2*b + 1/2)*a + 2),\n207                  Fractional ideal (-b*a + 1/2*b + 1/2),\n208                  Fractional ideal ((1/2*b + 3/2)*a - b),\n209                  Fractional ideal ((-1/2*b - 3/2)*a + b - 1),\n210                  Fractional ideal (-b*a - b + 1),\n211                  Fractional ideal (3*a + 1/2*b - 1/2),\n212                  Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),\n213                  Fractional ideal ((-1/2*b - 5/2)*a - b + 1),\n214                  Fractional ideal (2*a - 3/2*b - 1/2),\n215                  Fractional ideal (3*a + 1/2*b + 5/2)]\n```\n\nIn particular, note line 205:\n\n```\nsage: ids = N.primes_of_degree_one_list(10); a # random\n```\n\nwhich the docstring flags as random. But I think the \"a\" on that line is a typo, because with Sage 4.1.1 this is what I get:\n\n```\nsage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])\nsage: ids = N.primes_of_degree_one_list(10)\nsage: ids\n[Fractional ideal (2*a + 1/2*b - 1/2),\n Fractional ideal ((-1/2*b - 1/2)*a - b),\n Fractional ideal (b*a + 1/2*b + 3/2),\n Fractional ideal ((-1/2*b - 3/2)*a + b - 1),\n Fractional ideal ((-b + 1)*a + b),\n Fractional ideal (3*a + 1/2*b - 1/2),\n Fractional ideal ((1/2*b - 1/2)*a + 3/2*b - 1/2),\n Fractional ideal ((-1/2*b - 5/2)*a - b + 1),\n Fractional ideal (2*a - 3/2*b - 1/2),\n Fractional ideal (3*a + 1/2*b + 5/2)]\n```\n\nThat is, I replaced the \"a\" with \"ids\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/6806\n\n",
    "created_at": "2009-08-22T20:26:11Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "typo in patch of ticket #6396: primes_of_degree_one is broken for relative extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6806",
    "user": "mvngu"
}
```
Assignee: tba

CC:  davidloeffler ncalexan

The patch trac_6396-deg1primes.patch at ticket #6396 has this docstring:

```
201             We test that #6396 is fixed. Note that the doctest is flagged as random
202             since the string representation of ideals is somewhat unpredictable.::
203
204                 sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
205                 sage: ids = N.primes_of_degree_one_list(10); a # random
206                 [Fractional ideal ((-1/2*b + 1/2)*a + 2),
207                  Fractional ideal (-b*a + 1/2*b + 1/2),
208                  Fractional ideal ((1/2*b + 3/2)*a - b),
209                  Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
210                  Fractional ideal (-b*a - b + 1),
211                  Fractional ideal (3*a + 1/2*b - 1/2),
212                  Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),
213                  Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
214                  Fractional ideal (2*a - 3/2*b - 1/2),
215                  Fractional ideal (3*a + 1/2*b + 5/2)]
```

In particular, note line 205:

```
sage: ids = N.primes_of_degree_one_list(10); a # random
```

which the docstring flags as random. But I think the "a" on that line is a typo, because with Sage 4.1.1 this is what I get:

```
sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
sage: ids = N.primes_of_degree_one_list(10)
sage: ids
[Fractional ideal (2*a + 1/2*b - 1/2),
 Fractional ideal ((-1/2*b - 1/2)*a - b),
 Fractional ideal (b*a + 1/2*b + 3/2),
 Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
 Fractional ideal ((-b + 1)*a + b),
 Fractional ideal (3*a + 1/2*b - 1/2),
 Fractional ideal ((1/2*b - 1/2)*a + 3/2*b - 1/2),
 Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
 Fractional ideal (2*a - 3/2*b - 1/2),
 Fractional ideal (3*a + 1/2*b + 5/2)]
```

That is, I replaced the "a" with "ids".

Issue created by migration from https://trac.sagemath.org/ticket/6806





---

archive/issue_comments_056036.json:
```json
{
    "body": "based on Sage 4.1.1",
    "created_at": "2009-08-22T21:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6806#issuecomment-56036",
    "user": "mvngu"
}
```

based on Sage 4.1.1



---

archive/issue_comments_056037.json:
```json
{
    "body": "Attachment [trac_6806-typo-in-patch-of-6396.patch](tarball://root/attachments/some-uuid/ticket6806/trac_6806-typo-in-patch-of-6396.patch) by mvngu created at 2009-08-22 21:54:54",
    "created_at": "2009-08-22T21:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6806#issuecomment-56037",
    "user": "mvngu"
}
```

Attachment [trac_6806-typo-in-patch-of-6396.patch](tarball://root/attachments/some-uuid/ticket6806/trac_6806-typo-in-patch-of-6396.patch) by mvngu created at 2009-08-22 21:54:54



---

archive/issue_comments_056038.json:
```json
{
    "body": "This is clearly what's going on.  Positive review.",
    "created_at": "2009-09-14T21:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6806#issuecomment-56038",
    "user": "kcrisman"
}
```

This is clearly what's going on.  Positive review.



---

archive/issue_comments_056039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-16T01:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6806#issuecomment-56039",
    "user": "mvngu"
}
```

Resolution: fixed
