# Issue 3242: [with patch, needs review] Fix little bug in G.relabel() for G a graph...

archive/issues_003242.json:
```json
{
    "body": "Assignee: @rlmill\n\nReported by Chris Godsil:\n\n```\n\"\"\"\nbad4.txt\n\nCreated by Chris Godsil on 2008-05-14.\n\n\"\"\"\n\nI construct a graph P on 8 vertices from the Petersen graph.\n\nPROBLEMS:\n\t(1) The command P.relabel() raises an error as shown, but seems to work.\n\t(2) An attempt to get the automorphism group again raises an error, as shown.\n\t(3) P.is_planar() raises an exceptions.KeyError.\n\t(4) Attempting to get the group before relabelling raises an error too.\n\t(5) Ditto for P.girth()\n\t\nVERSION:\n\tsage: version()\n\t'SAGE Version 3.0, Release Date: 2008-04-21'\n\nGRAPH CONSTRUCTION:\nP = graphs.PetersenGraph()\nP.delete_edge([0,1])\nP.add_edge([4,5])\nP.add_edge([2,6])\nP.delete_vertices([0,1])\n\nsage: P.degree()  \n[3, 3, 3, 3, 3, 3, 3, 3]\n\nsage: P.vertices()\n[2, 3, 4, 5, 6, 7, 8, 9]\n\n\nERRORS:\nsage: P.relabel()\n---------------------------------------------------------------------------\n<type 'exceptions.KeyError'>              Traceback (most recent call last)\n\n/Users/chrisgodsil/Documents/sgwork/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in relabel(self, perm, inplace, return_map)\n   5791             new_pos = {}\n   5792             for v in self._pos:\n-> 5793                 new_pos[perm[v]] = self._pos[v]\n   5794             self._pos = new_pos\n   5795         self._boundary = [perm[v] for v in self._boundary]\n\n<type 'exceptions.KeyError'>: 0\n\nsage: P.vertices()\n[0, 1, 2, 3, 4, 5, 6, 7]\n\n\nsage: P.automorphism_group()\n---------------------------------------------------------------------------\n<type 'exceptions.KeyError'>              Traceback (most recent call last)\n\n/Users/chrisgodsil/Documents/sgwork/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in automorphism_group(self, partition, translation, verbosity, edge_labels, order, return_group, orbits)\n   6159                     a,b = A\n   6160             else:\n-> 6161                 a = search_tree(self, partition, dict_rep=False, lab=False, dig=dig, verbosity=verbosity, order=order)\n   6162                 if order:\n   6163                     a,c = a\n\n/Users/chrisgodsil/Documents/sgwork/graph_isom.pyx in sage.graphs.graph_isom.search_tree (sage/graphs/graph_isom.c:8990)()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in relabel(self, perm, inplace, return_map)\n   5791             new_pos = {}\n   5792             for v in self._pos:\n-> 5793                 new_pos[perm[v]] = self._pos[v]\n   5794             self._pos = new_pos\n   5795         self._boundary = [perm[v] for v in self._boundary]\n\n<type 'exceptions.KeyError'>: 8\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3242\n\n",
    "created_at": "2008-05-17T19:14:18Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, needs review] Fix little bug in G.relabel() for G a graph...",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3242",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

Reported by Chris Godsil:

```
"""
bad4.txt

Created by Chris Godsil on 2008-05-14.

"""

I construct a graph P on 8 vertices from the Petersen graph.

PROBLEMS:
	(1) The command P.relabel() raises an error as shown, but seems to work.
	(2) An attempt to get the automorphism group again raises an error, as shown.
	(3) P.is_planar() raises an exceptions.KeyError.
	(4) Attempting to get the group before relabelling raises an error too.
	(5) Ditto for P.girth()
	
VERSION:
	sage: version()
	'SAGE Version 3.0, Release Date: 2008-04-21'

GRAPH CONSTRUCTION:
P = graphs.PetersenGraph()
P.delete_edge([0,1])
P.add_edge([4,5])
P.add_edge([2,6])
P.delete_vertices([0,1])

sage: P.degree()  
[3, 3, 3, 3, 3, 3, 3, 3]

sage: P.vertices()
[2, 3, 4, 5, 6, 7, 8, 9]


ERRORS:
sage: P.relabel()
---------------------------------------------------------------------------
<type 'exceptions.KeyError'>              Traceback (most recent call last)

/Users/chrisgodsil/Documents/sgwork/<ipython console> in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in relabel(self, perm, inplace, return_map)
   5791             new_pos = {}
   5792             for v in self._pos:
-> 5793                 new_pos[perm[v]] = self._pos[v]
   5794             self._pos = new_pos
   5795         self._boundary = [perm[v] for v in self._boundary]

<type 'exceptions.KeyError'>: 0

sage: P.vertices()
[0, 1, 2, 3, 4, 5, 6, 7]


sage: P.automorphism_group()
---------------------------------------------------------------------------
<type 'exceptions.KeyError'>              Traceback (most recent call last)

/Users/chrisgodsil/Documents/sgwork/<ipython console> in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in automorphism_group(self, partition, translation, verbosity, edge_labels, order, return_group, orbits)
   6159                     a,b = A
   6160             else:
-> 6161                 a = search_tree(self, partition, dict_rep=False, lab=False, dig=dig, verbosity=verbosity, order=order)
   6162                 if order:
   6163                     a,c = a

/Users/chrisgodsil/Documents/sgwork/graph_isom.pyx in sage.graphs.graph_isom.search_tree (sage/graphs/graph_isom.c:8990)()

/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in relabel(self, perm, inplace, return_map)
   5791             new_pos = {}
   5792             for v in self._pos:
-> 5793                 new_pos[perm[v]] = self._pos[v]
   5794             self._pos = new_pos
   5795         self._boundary = [perm[v] for v in self._boundary]

<type 'exceptions.KeyError'>: 8
```


Issue created by migration from https://trac.sagemath.org/ticket/3242





---

archive/issue_comments_022403.json:
```json
{
    "body": "Attachment [trac-3242-graph_relabel.patch](tarball://root/attachments/some-uuid/ticket3242/trac-3242-graph_relabel.patch) by @rlmill created at 2008-05-22 15:25:40",
    "created_at": "2008-05-22T15:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3242#issuecomment-22403",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-3242-graph_relabel.patch](tarball://root/attachments/some-uuid/ticket3242/trac-3242-graph_relabel.patch) by @rlmill created at 2008-05-22 15:25:40



---

archive/issue_comments_022404.json:
```json
{
    "body": "looks good to me, passes doctests in graph/",
    "created_at": "2008-05-22T17:11:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3242#issuecomment-22404",
    "user": "https://github.com/jasongrout"
}
```

looks good to me, passes doctests in graph/



---

archive/issue_comments_022405.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-22T20:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3242#issuecomment-22405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022406.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-22T20:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3242#issuecomment-22406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.rc0
