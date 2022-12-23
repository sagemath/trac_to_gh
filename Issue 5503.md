# Issue 5503: "cmp" method failing on objects in the pickle jar

archive/issues_005503.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  jakobkroeker\n\nKeywords: universal comparison, transitivity, coercion\n\nThe following piece of code loads the pickle jar and tries to compare each pair of members. In my 3.4, it currently segfaults.\n\nIf sage is to have universal comparison, these comparisons should all occur without error. The next step would be to ensure that results are consistent with transitivity.\n\n\n```\nL=[]\nM=[]\n#change this location to point to your own pickle jar\npath=\"/usr/local/sage/default/tmp/pickle_jar-3.4\"\n\nfor n in sorted(os.listdir(path)):\n  if n.endswith(\".sobj\") and not(n in M):\n    print n\n    L.append(load(path+\"/\"+n))\n\nfor i in [1..len(L)-1]:\n    for j in range(i):\n        try:\n            _=cmp(L[i],L[j])\n        except:\n            print [i,j]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5503\n\n",
    "created_at": "2009-03-12T20:23:26Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "\"cmp\" method failing on objects in the pickle jar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5503",
    "user": "nbruin"
}
```
Assignee: cwitty

CC:  jakobkroeker

Keywords: universal comparison, transitivity, coercion

The following piece of code loads the pickle jar and tries to compare each pair of members. In my 3.4, it currently segfaults.

If sage is to have universal comparison, these comparisons should all occur without error. The next step would be to ensure that results are consistent with transitivity.


```
L=[]
M=[]
#change this location to point to your own pickle jar
path="/usr/local/sage/default/tmp/pickle_jar-3.4"

for n in sorted(os.listdir(path)):
  if n.endswith(".sobj") and not(n in M):
    print n
    L.append(load(path+"/"+n))

for i in [1..len(L)-1]:
    for j in range(i):
        try:
            _=cmp(L[i],L[j])
        except:
            print [i,j]
```


Issue created by migration from https://trac.sagemath.org/ticket/5503





---

archive/issue_comments_042750.json:
```json
{
    "body": "Duplicate of #16311.",
    "created_at": "2017-03-08T13:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5503#issuecomment-42750",
    "user": "jdemeyer"
}
```

Duplicate of #16311.



---

archive/issue_comments_042751.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2017-03-08T13:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5503#issuecomment-42751",
    "user": "jdemeyer"
}
```

Resolution: duplicate
