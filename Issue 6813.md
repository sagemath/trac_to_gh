# Issue 6813: [with patch, needs review] The whole world in a graph

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-08-23 08:43:18

Assignee: rlm

see http://groups.google.com/group/sage-devel/browse_thread/thread/25e57b8421c0ae9c/5ed13d13bc41b370#5ed13d13bc41b370

This patch adds a function WorldMap to graph_generators.py, which lets the user load the graph in which vertices are countries and links denote a shared boundary between two of them. The data I used to build this comes from The Cia Factbook ( mentionned in the docstring )

To use it, you need to apply the patch, but also to move the file graph_world.sobj to SAGE_ROOT/data/graphs/

Thank you for your help ! :-)


---

Attachment


---

Attachment

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

Comment by jason created at 2009-09-22 16:14:04

that was with 4.1.2.alpha2


---

Comment by ncohen created at 2009-09-26 15:36:57

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
ncohen`@`sage:~$ md5sum graph_world.sobj 
438bc195a9486caebeb47442ff8b8d8c  graph_world.sobj
```


Could you check if this version works, and if the checksum is correct ? Thank you !!!

Nathann


---

Comment by awebb created at 2009-10-10 11:47:56

I get the same checksum as you do. 

{{{$ md5sum data/graphs/graph_world.sobj
438bc195a9486caebeb47442ff8b8d8c  data/graphs/graph_world.sobj
}}}
I was unable to apply the patch to sage-4.1.2.rc0. I guess a rebase is needed. Once I had the patch applied there were some warnings when I tried to do sage -docbuild. I made some changes to fix that. Specifically, I changed the reference so that it was similar to other ones on the same page. I hope that it is still fine. Otherwise, if you are happy with my small changes than I would give it a positive review.

Adam


---

Comment by awebb created at 2009-10-10 11:59:38

applies to sage-4.1.2.rc0


---

Attachment


---

Comment by ncohen created at 2009-10-10 12:02:11

These changes are perfect for me ! Thank for your help :-)


---

Comment by awebb created at 2009-10-10 13:22:12

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-29 04:50:40

Resolution: fixed


---

Comment by mhansen created at 2009-12-06 08:57:08

I had to add the .sobj file to the graphs-20070722 spkg.
