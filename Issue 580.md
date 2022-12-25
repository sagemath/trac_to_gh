# Issue 580: bug in cubegroup (group action)

archive/issues_000580.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt seems from the cubegroup.py code that RubiksCube().move\naccepts a group element as an argument. Even if it doesn't the\nerror below seems confusing.\n\n\n```\nsage: rubik = CubeGroup()\nsage: G = rubik.group()\nsage: Z = G.center()\nsage: superflip = Z.list()[1]\nsage: superflip\n\n(2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,\n47)\nsage: r = rubik.R(); l = rubik.L(); f = rubik.F()\nsage: b = rubik.B(); u = rubik.U(); d = rubik.D()\nsage: superflip in G\nTrue\nsage: C = RubiksCube().move(superflip)\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()\n\n/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py\nin move(self, g)\n  1090     def move(self, g):\n  1091         if not g in self._group:\n-> 1092             g = self._group.move(g)[0]\n  1093         return RubiksCube(self._state * g, self._history +\n[g], self.colors)\n  1094\n\n/home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py\nin move(self, mv)\n   730\n   731         \"\"\"\n--> 732         mv = mv.strip().replace(\" \",\"*\").replace(\"**\",\n\"*\").replace(\"'\", \"^(-1)\")\n   733         m = mv.split(\"*\")\n   734         M = [x.split(\"^\") for x in m]\n\n<type 'exceptions.AttributeError'>: 'PermutationGroupElement' object\nhas no attribute 'strip'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/580\n\n",
    "created_at": "2007-09-03T16:37:33Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "bug in cubegroup (group action)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/580",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

It seems from the cubegroup.py code that RubiksCube().move
accepts a group element as an argument. Even if it doesn't the
error below seems confusing.


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
sage: C = RubiksCube().move(superflip)
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

<type 'exceptions.AttributeError'>: 'PermutationGroupElement' object
has no attribute 'strip'
```


Issue created by migration from https://trac.sagemath.org/ticket/580





---

archive/issue_comments_002988.json:
```json
{
    "body": "Robert Bradshaw or I can try to work on this when we get time.\nThe ticket was automatically assigned to was (William).\n\nReplying to [ticket:580 wdj]:\n> It seems from the cubegroup.py code that RubiksCube().move\n> accepts a group element as an argument. Even if it doesn't the\n> error below seems confusing.\n> \n> {{{\n> sage: rubik = CubeGroup()\n> sage: G = rubik.group()\n> sage: Z = G.center()\n> sage: superflip = Z.list()[1]\n> sage: superflip\n> \n> (2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,\n> 47)\n> sage: r = rubik.R(); l = rubik.L(); f = rubik.F()\n> sage: b = rubik.B(); u = rubik.U(); d = rubik.D()\n> sage: superflip in G\n> True\n> sage: C = RubiksCube().move(superflip)\n> ---------------------------------------------------------------------------\n> <type 'exceptions.AttributeError'>        Traceback (most recent call last)\n> \n> /mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()\n> \n> /home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py\n> in move(self, g)\n>   1090     def move(self, g):\n>   1091         if not g in self._group:\n> -> 1092             g = self._group.move(g)[0]\n>   1093         return RubiksCube(self._state * g, self._history +\n> [g], self.colors)\n>   1094\n> \n> /home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py\n> in move(self, mv)\n>    730\n>    731         \"\"\"\n> --> 732         mv = mv.strip().replace(\" \",\"*\").replace(\"**\",\n> \"*\").replace(\"'\", \"^(-1)\")\n>    733         m = mv.split(\"*\")\n>    734         M = [x.split(\"^\") for x in m]\n> \n> <type 'exceptions.AttributeError'>: 'PermutationGroupElement' object\n> has no attribute 'strip'\n> }}}",
    "created_at": "2007-09-03T16:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/580#issuecomment-2988",
    "user": "https://github.com/wdjoyner"
}
```

Robert Bradshaw or I can try to work on this when we get time.
The ticket was automatically assigned to was (William).

Replying to [ticket:580 wdj]:
> It seems from the cubegroup.py code that RubiksCube().move
> accepts a group element as an argument. Even if it doesn't the
> error below seems confusing.
> 
> {{{
> sage: rubik = CubeGroup()
> sage: G = rubik.group()
> sage: Z = G.center()
> sage: superflip = Z.list()[1]
> sage: superflip
> 
> (2,34)(4,10)(5,26)(7,18)(12,37)(13,20)(15,44)(21,28)(23,42)(29,36)(31,45)(39,
> 47)
> sage: r = rubik.R(); l = rubik.L(); f = rubik.F()
> sage: b = rubik.B(); u = rubik.U(); d = rubik.D()
> sage: superflip in G
> True
> sage: C = RubiksCube().move(superflip)
> ---------------------------------------------------------------------------
> <type 'exceptions.AttributeError'>        Traceback (most recent call last)
> 
> /mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()
> 
> /home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
> in move(self, g)
>   1090     def move(self, g):
>   1091         if not g in self._group:
> -> 1092             g = self._group.move(g)[0]
>   1093         return RubiksCube(self._state * g, self._history +
> [g], self.colors)
>   1094
> 
> /home/wdj/sagefiles/sage-2.8.3.rc3/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py
> in move(self, mv)
>    730
>    731         """
> --> 732         mv = mv.strip().replace(" ","*").replace("**",
> "*").replace("'", "^(-1)")
>    733         m = mv.split("*")
>    734         M = [x.split("^") for x in m]
> 
> <type 'exceptions.AttributeError'>: 'PermutationGroupElement' object
> has no attribute 'strip'
> }}}



---

archive/issue_comments_002989.json:
```json
{
    "body": "Changing assignee from @williamstein to @wdjoyner.",
    "created_at": "2007-09-03T16:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/580#issuecomment-2989",
    "user": "https://github.com/wdjoyner"
}
```

Changing assignee from @williamstein to @wdjoyner.



---

archive/issue_comments_002990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T19:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/580#issuecomment-2990",
    "user": "https://github.com/robertwb"
}
```

Resolution: fixed



---

archive/issue_events_001550.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2007-09-06T19:28:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/580",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/580#event-1550"
}
```



---

archive/issue_comments_002991.json:
```json
{
    "body": "This code now works, see #570.",
    "created_at": "2007-09-06T19:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/580#issuecomment-2991",
    "user": "https://github.com/robertwb"
}
```

This code now works, see #570.



---

archive/issue_events_001551.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-06T20:08:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/580",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/580#event-1551"
}
```
