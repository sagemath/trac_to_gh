# Issue 6901: follow-up to #6839: fix warnings when building reference manual

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-07 17:22:31

Assignee: tba

CC:  sage-combinat

As the subject says.


---

Attachment

fix warnings when building reference manual


---

Comment by mvngu created at 2009-09-08 03:18:28

The patch `trac_6839-crystal-E7-as.patch` results in two warnings when building the reference manual:

```
WARNING: /scratch/mvngu/sage-4.1.2.alpha1-sage.math/local/lib/python2.6/site-packages/sage/combinat/crystals/letters.py:docstring of sage.combinat.crystals.letters.Crystal_of_letters_type_E7_element:6: (WARNING/2) Literal block expected; none found.
WARNING: /scratch/mvngu/sage-4.1.2.alpha1-sage.math/local/lib/python2.6/site-packages/sage/combinat/crystals/letters.py:docstring of sage.combinat.crystals.letters.Crystal_of_letters_type_E7_element.weight:5: (WARNING/2) Literal block expected; none found.
```

Here is the relevant patch snippet that causes the warnings:

```
1287	    TESTS:: 
1288	 
1289	    sage: C = CrystalOfLetters(['E',7]) 
1290	    sage: C.module_generators 
1291	    [This is the Trac macro *7* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#7-macro) 
1292	    sage: C.list() 
1293	    [[7], [-7, 6], [-6, 5], [-5, 4], [-4, 2, 3], [-2, 3], [-3, 1, 2], [-1, 
1294	    2], [-3, -2, 1, 4], [-1, -2, 4], [-4, 1, 5], [-4, -1, 3, 5], [-3, 5], 
1295	    [-5, 6, 1], [-5, -1, 3, 6], [-5, -3, 4, 6], [-4, 2, 6], [-2, 6], [-6, 7, 
1296	    1], [-1, -6, 3, 7], [-6, -3, 7, 4], [-6, -4, 2, 7, 5], [-6, -2, 7, 5], 
1297	    [-5, 7, 2], [-5, -2, 4, 7], [-4, 7, 3], [-3, 1, 7], [-1, 7], [-7, 1], 
1298	    [-1, -7, 3], [-7, -3, 4], [-4, -7, 2, 5], [-7, -2, 5], [-5, -7, 6, 2], 
1299	    [-5, -2, -7, 4, 6], [-7, -4, 6, 3], [-3, -7, 1, 6], [-7, -1, 6], [-6, 
1300	    2], [-2, -6, 4], [-6, -4, 5, 3], [-3, -6, 1, 5], [-6, -1, 5], [-5, 3], 
1301	    [-3, -5, 4, 1], [-5, -1, 4], [-4, 1, 2], [-1, -4, 3, 2], [-3, 2], [-2, 
1302	    -3, 4], [-4, 5], [-5, 6], [-6, 7], [-7], [-2, 1], [-2, -1, 3]] 
1303	    sage: C.check() 
1304	    True 
1305	    sage: all(b.f(i).e(i) == b for i in C.index_set() for b in C if b.f(i) is not None) 
1306	    True 
1307	    sage: all(b.e(i).f(i) == b for i in C.index_set() for b in C if b.e(i) is not None) 
1308	    True 
1309	    sage: G = C.digraph() 
1310	    sage: G.show(edge_labels=true, figsize=12, vertex_size=1)


1317	        EXAMPLES:: 
1318	         
1319	        sage: [v.weight() for v in CrystalOfLetters(['E',7])] 
1320	        [(0, 0, 0, 0, 0, 1, -1/2, 1/2), (0, 0, 0, 0, 1, 0, -1/2, 1/2), (0, 0, 0, 
1321	        1, 0, 0, -1/2, 1/2), (0, 0, 1, 0, 0, 0, -1/2, 1/2), (0, 1, 0, 0, 0, 0, 
1322	        -1/2, 1/2), (-1, 0, 0, 0, 0, 0, -1/2, 1/2), (1, 0, 0, 0, 0, 0, -1/2, 
1323	        1/2), (1/2, 1/2, 1/2, 1/2, 1/2, 1/2, 0, 0), (0, -1, 0, 0, 0, 0, -1/2, 
1324	        1/2), (-1/2, -1/2, 1/2, 1/2, 1/2, 1/2, 0, 0), (0, 0, -1, 0, 0, 0, -1/2, 
1325	        1/2), (-1/2, 1/2, -1/2, 1/2, 1/2, 1/2, 0, 0), (1/2, -1/2, -1/2, 1/2, 
1326	        1/2, 1/2, 0, 0), (0, 0, 0, -1, 0, 0, -1/2, 1/2), (-1/2, 1/2, 1/2, -1/2, 
1327	        1/2, 1/2, 0, 0), (1/2, -1/2, 1/2, -1/2, 1/2, 1/2, 0, 0), (1/2, 1/2, 
1328	        -1/2, -1/2, 1/2, 1/2, 0, 0), (-1/2, -1/2, -1/2, -1/2, 1/2, 1/2, 0, 0), 
1329	        (0, 0, 0, 0, -1, 0, -1/2, 1/2), (-1/2, 1/2, 1/2, 1/2, -1/2, 1/2, 0, 0), 
1330	        (1/2, -1/2, 1/2, 1/2, -1/2, 1/2, 0, 0), (1/2, 1/2, -1/2, 1/2, -1/2, 1/2, 
1331	        0, 0), (-1/2, -1/2, -1/2, 1/2, -1/2, 1/2, 0, 0), (1/2, 1/2, 1/2, -1/2, 
1332	        -1/2, 1/2, 0, 0), (-1/2, -1/2, 1/2, -1/2, -1/2, 1/2, 0, 0), (-1/2, 1/2, 
1333	        -1/2, -1/2, -1/2, 1/2, 0, 0), (1/2, -1/2, -1/2, -1/2, -1/2, 1/2, 0, 0), 
1334	        (0, 0, 0, 0, 0, 1, 1/2, -1/2), (0, 0, 0, 0, 0, -1, -1/2, 1/2), (-1/2, 
1335	        1/2, 1/2, 1/2, 1/2, -1/2, 0, 0), (1/2, -1/2, 1/2, 1/2, 1/2, -1/2, 0, 0), 
1336	        (1/2, 1/2, -1/2, 1/2, 1/2, -1/2, 0, 0), (-1/2, -1/2, -1/2, 1/2, 1/2, 
1337	        -1/2, 0, 0), (1/2, 1/2, 1/2, -1/2, 1/2, -1/2, 0, 0), (-1/2, -1/2, 1/2, 
1338	        -1/2, 1/2, -1/2, 0, 0), (-1/2, 1/2, -1/2, -1/2, 1/2, -1/2, 0, 0), (1/2, 
1339	        -1/2, -1/2, -1/2, 1/2, -1/2, 0, 0), (0, 0, 0, 0, 1, 0, 1/2, -1/2), (1/2, 
1340	        1/2, 1/2, 1/2, -1/2, -1/2, 0, 0), (-1/2, -1/2, 1/2, 1/2, -1/2, -1/2, 0, 
1341	        0), (-1/2, 1/2, -1/2, 1/2, -1/2, -1/2, 0, 0), (1/2, -1/2, -1/2, 1/2, 
1342	        -1/2, -1/2, 0, 0), (0, 0, 0, 1, 0, 0, 1/2, -1/2), (-1/2, 1/2, 1/2, -1/2, 
1343	        -1/2, -1/2, 0, 0), (1/2, -1/2, 1/2, -1/2, -1/2, -1/2, 0, 0), (0, 0, 1, 
1344	        0, 0, 0, 1/2, -1/2), (1/2, 1/2, -1/2, -1/2, -1/2, -1/2, 0, 0), (0, 1, 0, 
1345	        0, 0, 0, 1/2, -1/2), (1, 0, 0, 0, 0, 0, 1/2, -1/2), (0, -1, 0, 0, 0, 0, 
1346	        1/2, -1/2), (0, 0, -1, 0, 0, 0, 1/2, -1/2), (0, 0, 0, -1, 0, 0, 1/2, 
1347	        -1/2), (0, 0, 0, 0, -1, 0, 1/2, -1/2), (0, 0, 0, 0, 0, -1, 1/2, -1/2), 
1348	        (-1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 0, 0), (-1, 0, 0, 0, 0, 0, 1/2, 
1349	        -1/2)] 
```

The warnings should now be fixed by `trac_6901-fix-warnings.patch`, which is based on Sage 4.1.2.alpha1.


---

Comment by jhpalmieri created at 2009-09-23 04:32:09

Tests pass, no warnings for this file when building the reference manual.


---

Comment by mvngu created at 2009-09-23 07:08:51

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:50:11

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
