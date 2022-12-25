# Issue 582: bug in cubegroup? (syntax in RubiksCube)

archive/issues_000582.json:
```json
{
    "body": "Assignee: wdj or Robert Bradshaw\n\nAgain, a confusing error message. If group elements are allowed \nas arguments, what syntax should be used? Square bracketed list\nof tuples? This element [(1,2)] is not in the Rubik's cube group, so \nshouldn't the error be something other than\n`'list' object has no attribute 'strip'` ?\n\n\n```\nsage: C = RubiksCube().move([(1,2)])\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()\n\n/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py\nin move(self, g)\n  1090     def move(self, g):\n  1091         if not g in self._group:\n-> 1092             g = self._group.move(g)[0]\n  1093         return RubiksCube(self._state * g, self._history +\n[g], self.colors)\n  1094\n\n/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py\nin move(self, mv)\n   730\n   731         \"\"\"\n--> 732         mv = mv.strip().replace(\" \",\"*\").replace(\"**\",\n\"*\").replace(\"'\", \"^(-1)\")\n   733         m = mv.split(\"*\")\n   734         M = [x.split(\"^\") for x in m]\n\n<type 'exceptions.AttributeError'>: 'list' object has no attribute 'strip'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/582\n\n",
    "created_at": "2007-09-03T16:43:37Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "bug in cubegroup? (syntax in RubiksCube)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/582",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: wdj or Robert Bradshaw

Again, a confusing error message. If group elements are allowed 
as arguments, what syntax should be used? Square bracketed list
of tuples? This element [(1,2)] is not in the Rubik's cube group, so 
shouldn't the error be something other than
`'list' object has no attribute 'strip'` ?


```
sage: C = RubiksCube().move([(1,2)])
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()

/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
in move(self, g)
  1090     def move(self, g):
  1091         if not g in self._group:
-> 1092             g = self._group.move(g)[0]
  1093         return RubiksCube(self._state * g, self._history +
[g], self.colors)
  1094

/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
in move(self, mv)
   730
   731         """
--> 732         mv = mv.strip().replace(" ","*").replace("**",
"*").replace("'", "^(-1)")
   733         m = mv.split("*")
   734         M = [x.split("^") for x in m]

<type 'exceptions.AttributeError'>: 'list' object has no attribute 'strip'
```


Issue created by migration from https://trac.sagemath.org/ticket/582





---

archive/issue_comments_002998.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T19:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/582#issuecomment-2998",
    "user": "https://github.com/robertwb"
}
```

Resolution: fixed



---

archive/issue_events_001553.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2007-09-06T19:26:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/582",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/582#event-1553"
}
```



---

archive/issue_comments_002999.json:
```json
{
    "body": "See CubeGroup.parse() for all possible input formats, see #570",
    "created_at": "2007-09-06T19:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/582#issuecomment-2999",
    "user": "https://github.com/robertwb"
}
```

See CubeGroup.parse() for all possible input formats, see #570



---

archive/issue_events_001554.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-06T20:08:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/582",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/582#event-1554"
}
```
