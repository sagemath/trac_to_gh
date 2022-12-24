# Issue 7408: Improve the speed of RSK

archive/issues_007408.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  hivert\n\nThe implementation of RSK in Sage has a number of inefficiencies which add up when dealing with large permutations.  The main improvement comes from using a binary search to figure out where to insert the number.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7408\n\n",
    "created_at": "2009-11-07T19:43:20Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Improve the speed of RSK",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7408",
    "user": "mhansen"
}
```
Assignee: mhansen

CC:  hivert

The implementation of RSK in Sage has a number of inefficiencies which add up when dealing with large permutations.  The main improvement comes from using a binary search to figure out where to insert the number.

Issue created by migration from https://trac.sagemath.org/ticket/7408





---

archive/issue_comments_062341.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-07T19:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62341",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062342.json:
```json
{
    "body": "I like this commentary of yours:\n\n```\n                #Swtich x and y\n```\n\nYou should have called you variables `t` and `i` :-)\n\n\nFlorent",
    "created_at": "2009-11-07T20:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62342",
    "user": "hivert"
}
```

I like this commentary of yours:

```
                #Swtich x and y
```

You should have called you variables `t` and `i` :-)


Florent



---

archive/issue_comments_062343.json:
```json
{
    "body": "A last slight improvement would be to avoid the burden of keeping maxes and lenths.\n\nA row version would then be:\n\n\n```\n    def robinson_schensted(self):\n        from bisect import bisect\n        p = []       #the \"left\" tableau\n        q = []       #the \"recording\" tableau\n\n        #For each x in self, insert x into the tableau p.\n        for i,x in enumerate(self):\n            row_counter = 0\n            for r in p:\n                if r[-1] > x:\n                    y_pos = bisect(r, x)\n                    x, r[y_pos] = r[y_pos], x\n                    row_counter += 1\n                else:\n                    break\n            if row_counter == len(p):\n                p.append([x])\n                q.append([i+1])\n            else:\n                r.append(x)\n                q[row_counter].append(i+1)\n\n        return [tableau.Tableau(p),tableau.Tableau(q)]\n```\n\n\nThis gives me something like a 15% speedup.",
    "created_at": "2009-11-07T23:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62343",
    "user": "ylchapuy"
}
```

A last slight improvement would be to avoid the burden of keeping maxes and lenths.

A row version would then be:


```
    def robinson_schensted(self):
        from bisect import bisect
        p = []       #the "left" tableau
        q = []       #the "recording" tableau

        #For each x in self, insert x into the tableau p.
        for i,x in enumerate(self):
            row_counter = 0
            for r in p:
                if r[-1] > x:
                    y_pos = bisect(r, x)
                    x, r[y_pos] = r[y_pos], x
                    row_counter += 1
                else:
                    break
            if row_counter == len(p):
                p.append([x])
                q.append([i+1])
            else:
                r.append(x)
                q[row_counter].append(i+1)

        return [tableau.Tableau(p),tableau.Tableau(q)]
```


This gives me something like a 15% speedup.



---

archive/issue_comments_062344.json:
```json
{
    "body": "I've put up a new patch which incorporates Yann's ideas as well as gets rid of the row_counter bookkeeping.",
    "created_at": "2009-11-08T07:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62344",
    "user": "mhansen"
}
```

I've put up a new patch which incorporates Yann's ideas as well as gets rid of the row_counter bookkeeping.



---

archive/issue_comments_062345.json:
```json
{
    "body": "Attachment [trac_7408-rsk.patch](tarball://root/attachments/some-uuid/ticket7408/trac_7408-rsk.patch) by mhansen created at 2009-11-08 07:13:28",
    "created_at": "2009-11-08T07:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62345",
    "user": "mhansen"
}
```

Attachment [trac_7408-rsk.patch](tarball://root/attachments/some-uuid/ticket7408/trac_7408-rsk.patch) by mhansen created at 2009-11-08 07:13:28



---

archive/issue_comments_062346.json:
```json
{
    "body": "Changing keywords from \"\" to \"Robinson-Schensted\".",
    "created_at": "2009-11-08T11:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62346",
    "user": "hivert"
}
```

Changing keywords from "" to "Robinson-Schensted".



---

archive/issue_comments_062347.json:
```json
{
    "body": "This patch greatly improve the speed of RSK even for small permutations:\n\n```\nsage: p4 = Permutations(4).list()\nsage: timeit(\"map(attrcall('robinson_schensted'), p4)\")\n625 loops, best of 3: 1.22 ms per loop\nsage: p = Permutations(1000).random_element()\nsage: timeit(\"p.robinson_schensted()\")\n25 loops, best of 3: 19.5 ms per loop\n```\n\nwhereas we had:\n\n```\nsage: timeit(\"map(attrcall('robinson_schensted'), p4)\")\n625 loops, best of 3: 1.34 ms per loop\nsage: p = Permutations(1000).random_element()\nsage: timeit(\"p.robinson_schensted()\")\n5 loops, best of 3: 265 ms per loop\n```\n\nHowever, I was not sure that bisect cut the thing correctly in case of repeated letters so I had to write another test. I'd rather see it integrated into sage.\nPlease review this minor change. \n\nOtherwise you can put a postive review. \n\nCheers,\n\nFlorent",
    "created_at": "2009-11-08T11:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62347",
    "user": "hivert"
}
```

This patch greatly improve the speed of RSK even for small permutations:

```
sage: p4 = Permutations(4).list()
sage: timeit("map(attrcall('robinson_schensted'), p4)")
625 loops, best of 3: 1.22 ms per loop
sage: p = Permutations(1000).random_element()
sage: timeit("p.robinson_schensted()")
25 loops, best of 3: 19.5 ms per loop
```

whereas we had:

```
sage: timeit("map(attrcall('robinson_schensted'), p4)")
625 loops, best of 3: 1.34 ms per loop
sage: p = Permutations(1000).random_element()
sage: timeit("p.robinson_schensted()")
5 loops, best of 3: 265 ms per loop
```

However, I was not sure that bisect cut the thing correctly in case of repeated letters so I had to write another test. I'd rather see it integrated into sage.
Please review this minor change. 

Otherwise you can put a postive review. 

Cheers,

Florent



---

archive/issue_comments_062348.json:
```json
{
    "body": "Attachment [trac_7408-rsk-review.patch](tarball://root/attachments/some-uuid/ticket7408/trac_7408-rsk-review.patch) by ylchapuy created at 2009-11-08 14:06:10\n\nI give it a positive review.",
    "created_at": "2009-11-08T14:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62348",
    "user": "ylchapuy"
}
```

Attachment [trac_7408-rsk-review.patch](tarball://root/attachments/some-uuid/ticket7408/trac_7408-rsk-review.patch) by ylchapuy created at 2009-11-08 14:06:10

I give it a positive review.



---

archive/issue_comments_062349.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-08T14:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62349",
    "user": "ylchapuy"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7408#issuecomment-62350",
    "user": "mhansen"
}
```

Resolution: fixed
