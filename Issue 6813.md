# Issue 6813: [with patch, needs review] The whole world in a graph

archive/issues_006813.json:
```json
{
    "body": "Assignee: @rlmill\n\nsee http://groups.google.com/group/sage-devel/browse_thread/thread/25e57b8421c0ae9c/5ed13d13bc41b370#5ed13d13bc41b370\n\nThis patch adds a function WorldMap to graph_generators.py, which lets the user load the graph in which vertices are countries and links denote a shared boundary between two of them. The data I used to build this comes from The Cia Factbook ( mentionned in the docstring )\n\nTo use it, you need to apply the patch, but also to move the file graph_world.sobj to SAGE_ROOT/data/graphs/\n\nThank you for your help ! :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6813\n\n",
    "created_at": "2009-08-23T08:43:18Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] The whole world in a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6813",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

see http://groups.google.com/group/sage-devel/browse_thread/thread/25e57b8421c0ae9c/5ed13d13bc41b370#5ed13d13bc41b370

This patch adds a function WorldMap to graph_generators.py, which lets the user load the graph in which vertices are countries and links denote a shared boundary between two of them. The data I used to build this comes from The Cia Factbook ( mentionned in the docstring )

To use it, you need to apply the patch, but also to move the file graph_world.sobj to SAGE_ROOT/data/graphs/

Thank you for your help ! :-)

Issue created by migration from https://trac.sagemath.org/ticket/6813





---

archive/issue_comments_056082.json:
```json
{
    "body": "Attachment [graph_world.sobj](tarball://root/attachments/some-uuid/ticket6813/graph_world.sobj) by @nathanncohen created at 2009-08-23 08:44:25",
    "created_at": "2009-08-23T08:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56082",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [graph_world.sobj](tarball://root/attachments/some-uuid/ticket6813/graph_world.sobj) by @nathanncohen created at 2009-08-23 08:44:25



---

archive/issue_comments_056083.json:
```json
{
    "body": "Attachment [worldmap.patch](tarball://root/attachments/some-uuid/ticket6813/worldmap.patch) by @jasongrout created at 2009-09-22 16:13:35\n\nI get errors.  At the bottom, I copy the md5 digest to check my download:\n\n\n```\nsage: g=graphs.WorldMap() \n---------------------------------------------------------------------------\nUnpicklingError                           Traceback (most recent call last)\n\n/home/jason/.sage/temp/littleone/13542/_home_jason__sage_init_sage_0.py in <module>()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/graphs/graph_generators.pyc in WorldMap(self)\n   2985         from sage.structure.sage_object import load\n   2986         from sage.misc.misc import SAGE_DATA\n-> 2987         return load(SAGE_DATA+\"graphs/graph_world.sobj\")\n   2988 \n   2989 ################################################################################\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7173)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8769)()\n\nUnpicklingError: invalid load key, '<'.\nsage: load sage.misc.misc.SAGE_DATA + 'graphs/graph_world.sobj'\n---------------------------------------------------------------------------\nUnpicklingError                           Traceback (most recent call last)\n\n/home/jason/.sage/temp/littleone/13542/_home_jason__sage_init_sage_0.py in <module>()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7173)()\n\n/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8769)()\n\nUnpicklingError: invalid load key, '<'.\nsage: os.listdir(sage.misc.misc.SAGE_DATA + 'graphs/')\n['graph_world.sobj', 'graphs.db']\nsage: import md5 \nsage: md5.md5(sage.misc.misc.SAGE_DATA + 'graphs/graph_world.sobj').hexdigest()\n'0ae838b9de40596827c6e674b733f489'\n```\n",
    "created_at": "2009-09-22T16:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56083",
    "user": "https://github.com/jasongrout"
}
```

Attachment [worldmap.patch](tarball://root/attachments/some-uuid/ticket6813/worldmap.patch) by @jasongrout created at 2009-09-22 16:13:35

I get errors.  At the bottom, I copy the md5 digest to check my download:


```
sage: g=graphs.WorldMap() 
---------------------------------------------------------------------------
UnpicklingError                           Traceback (most recent call last)

/home/jason/.sage/temp/littleone/13542/_home_jason__sage_init_sage_0.py in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/graphs/graph_generators.pyc in WorldMap(self)
   2985         from sage.structure.sage_object import load
   2986         from sage.misc.misc import SAGE_DATA
-> 2987         return load(SAGE_DATA+"graphs/graph_world.sobj")
   2988 
   2989 ################################################################################

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7173)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8769)()

UnpicklingError: invalid load key, '<'.
sage: load sage.misc.misc.SAGE_DATA + 'graphs/graph_world.sobj'
---------------------------------------------------------------------------
UnpicklingError                           Traceback (most recent call last)

/home/jason/.sage/temp/littleone/13542/_home_jason__sage_init_sage_0.py in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7173)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:8769)()

UnpicklingError: invalid load key, '<'.
sage: os.listdir(sage.misc.misc.SAGE_DATA + 'graphs/')
['graph_world.sobj', 'graphs.db']
sage: import md5 
sage: md5.md5(sage.misc.misc.SAGE_DATA + 'graphs/graph_world.sobj').hexdigest()
'0ae838b9de40596827c6e674b733f489'
```




---

archive/issue_comments_056084.json:
```json
{
    "body": "that was with 4.1.2.alpha2",
    "created_at": "2009-09-22T16:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56084",
    "user": "https://github.com/jasongrout"
}
```

that was with 4.1.2.alpha2



---

archive/issue_comments_056085.json:
```json
{
    "body": "I get a totally different checksum..... Good job noticing it !!!\n\nI just retried to load the graph with a version of the file graph_world downloaded from the TRAC server and it worked for me. My checksum is the following :\n\n```\nsage: sage: g=graphs.WorldMap() \nsage: g\nGraph on 251 vertices\nsage: import md5 \nsage: sage: md5.md5(sage.misc.misc.SAGE_DATA + 'graphs/graph_world.sobj').hexdigest()\n'805fdf0227e964c41f3892c6979f62dc'\n```\n\n\nAs I suspect it may come from some weird encoding, here is a .rar version of the file : http://www-sop.inria.fr/members/Nathann.Cohen/world.rar\n\nI also copied the file on sagemath in the directory as ~/ncohen/graph_world.sobj\n\nOn my machine \n\n```\n~$ md5sum  /usr/local/sage/data/graphs/graph_world.sobj\n438bc195a9486caebeb47442ff8b8d8c  /usr/local/sage/data/graphs/graph_world.sobj\n```\n\nOn sagemath \n\n```\nncohen@sage:~$ md5sum graph_world.sobj \n438bc195a9486caebeb47442ff8b8d8c  graph_world.sobj\n```\n\n\nCould you check if this version works, and if the checksum is correct ? Thank you !!!\n\nNathann",
    "created_at": "2009-09-26T15:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56085",
    "user": "https://github.com/nathanncohen"
}
```

I get a totally different checksum..... Good job noticing it !!!

I just retried to load the graph with a version of the file graph_world downloaded from the TRAC server and it worked for me. My checksum is the following :

```
sage: sage: g=graphs.WorldMap() 
sage: g
Graph on 251 vertices
sage: import md5 
sage: sage: md5.md5(sage.misc.misc.SAGE_DATA + 'graphs/graph_world.sobj').hexdigest()
'805fdf0227e964c41f3892c6979f62dc'
```


As I suspect it may come from some weird encoding, here is a .rar version of the file : http://www-sop.inria.fr/members/Nathann.Cohen/world.rar

I also copied the file on sagemath in the directory as ~/ncohen/graph_world.sobj

On my machine 

```
~$ md5sum  /usr/local/sage/data/graphs/graph_world.sobj
438bc195a9486caebeb47442ff8b8d8c  /usr/local/sage/data/graphs/graph_world.sobj
```

On sagemath 

```
ncohen@sage:~$ md5sum graph_world.sobj 
438bc195a9486caebeb47442ff8b8d8c  graph_world.sobj
```


Could you check if this version works, and if the checksum is correct ? Thank you !!!

Nathann



---

archive/issue_comments_056086.json:
```json
{
    "body": "I get the same checksum as you do. \n\n\n```\n$ md5sum data/graphs/graph_world.sobj\n438bc195a9486caebeb47442ff8b8d8c  data/graphs/graph_world.sobj\n```\n\nI was unable to apply the patch to sage-4.1.2.rc0. I guess a rebase is needed. Once I had the patch applied there were some warnings when I tried to do sage -docbuild. I made some changes to fix that. Specifically, I changed the reference so that it was similar to other ones on the same page. I hope that it is still fine. Otherwise, if you are happy with my small changes than I would give it a positive review.\n\nAdam",
    "created_at": "2009-10-10T11:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56086",
    "user": "https://github.com/maxthemouse"
}
```

I get the same checksum as you do. 


```
$ md5sum data/graphs/graph_world.sobj
438bc195a9486caebeb47442ff8b8d8c  data/graphs/graph_world.sobj
```

I was unable to apply the patch to sage-4.1.2.rc0. I guess a rebase is needed. Once I had the patch applied there were some warnings when I tried to do sage -docbuild. I made some changes to fix that. Specifically, I changed the reference so that it was similar to other ones on the same page. I hope that it is still fine. Otherwise, if you are happy with my small changes than I would give it a positive review.

Adam



---

archive/issue_comments_056087.json:
```json
{
    "body": "applies to sage-4.1.2.rc0",
    "created_at": "2009-10-10T11:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56087",
    "user": "https://github.com/maxthemouse"
}
```

applies to sage-4.1.2.rc0



---

archive/issue_comments_056088.json:
```json
{
    "body": "Attachment [6813-worldmap.patch](tarball://root/attachments/some-uuid/ticket6813/6813-worldmap.patch) by @maxthemouse created at 2009-10-10 12:00:04",
    "created_at": "2009-10-10T12:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56088",
    "user": "https://github.com/maxthemouse"
}
```

Attachment [6813-worldmap.patch](tarball://root/attachments/some-uuid/ticket6813/6813-worldmap.patch) by @maxthemouse created at 2009-10-10 12:00:04



---

archive/issue_comments_056089.json:
```json
{
    "body": "These changes are perfect for me ! Thank for your help :-)",
    "created_at": "2009-10-10T12:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56089",
    "user": "https://github.com/nathanncohen"
}
```

These changes are perfect for me ! Thank for your help :-)



---

archive/issue_comments_056090.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-10T13:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56090",
    "user": "https://github.com/maxthemouse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056091.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T04:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56091",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_016054.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-29T04:50:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6813#event-16054"
}
```



---

archive/issue_comments_056092.json:
```json
{
    "body": "I had to add the .sobj file to the graphs-20070722 spkg.",
    "created_at": "2009-12-06T08:57:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6813",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6813#issuecomment-56092",
    "user": "https://github.com/mwhansen"
}
```

I had to add the .sobj file to the graphs-20070722 spkg.
