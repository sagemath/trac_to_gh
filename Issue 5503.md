# Issue 5503: "cmp" method failing on objects in the pickle jar

archive/issues_005503.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  jakobkroeker\n\nKeywords: universal comparison, transitivity, coercion\n\nThe following piece of code loads the pickle jar and tries to compare each pair of members. In my 3.4, it currently segfaults.\n\nIf sage is to have universal comparison, these comparisons should all occur without error. The next step would be to ensure that results are consistent with transitivity.\n\n```\nL=[]\nM=[]\n#change this location to point to your own pickle jar\npath=\"/usr/local/sage/default/tmp/pickle_jar-3.4\"\n\nfor n in sorted(os.listdir(path)):\n  if n.endswith(\".sobj\") and not(n in M):\n    print n\n    L.append(load(path+\"/\"+n))\n\nfor i in [1..len(L)-1]:\n    for j in range(i):\n        try:\n            _=cmp(L[i],L[j])\n        except:\n            print [i,j]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5503\n\n",
    "closed_at": "2017-03-08T13:19:48Z",
    "created_at": "2009-03-12T20:23:26Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"cmp\" method failing on objects in the pickle jar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5503",
    "user": "https://github.com/nbruin"
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

archive/issue_events_012872.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12872"
}
```



---

archive/issue_events_012873.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12873"
}
```



---

archive/issue_events_012874.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12874"
}
```



---

archive/issue_events_012875.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12875"
}
```



---

archive/issue_events_012876.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12876"
}
```



---

archive/issue_events_012877.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12877"
}
```



---

archive/issue_events_012878.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12878"
}
```



---

archive/issue_comments_042667.json:
```json
{
    "body": "Duplicate of #16311.",
    "created_at": "2017-03-08T13:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5503#issuecomment-42667",
    "user": "https://github.com/jdemeyer"
}
```

Duplicate of #16311.



---

archive/issue_events_012879.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-08T13:19:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12879"
}
```



---

archive/issue_events_012880.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-08T13:19:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12880"
}
```



---

archive/issue_comments_042668.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2017-03-08T13:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5503#issuecomment-42668",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_012881.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-08T13:19:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5503",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5503#event-12881"
}
```
