# Issue 8513: Including documentation in the reference manual for some files related to graph theory

archive/issues_008513.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nathanncohen @rlmill\n\nKeywords: documentation, graph theory\n\nI noticed a few weeks ago while reviewing a patch that important files in the graph theory folder were not appearing anywhere in the reference manual. For instance, functions such as `vertex_cut` or `edge_cut` do not appear, as well as all functions defined only for directed graphs.\n\nAt that time, I thought about adding the missing files with the patch, but since there were a lot of warnings displayed by Sphinx while generating the documentation, I changed my mind.\n\nI think it would be a good idea to use this ticket to fix this, but since it touches many files of graph theory, it may be hard to do it in a clean way. Someone has an idea of what would be the best approach ?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8513\n\n",
    "closed_at": "2010-04-16T18:46:01Z",
    "created_at": "2010-03-12T23:52:07Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Including documentation in the reference manual for some files related to graph theory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8513",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```
Assignee: @rlmill

CC:  @nathanncohen @rlmill

Keywords: documentation, graph theory

I noticed a few weeks ago while reviewing a patch that important files in the graph theory folder were not appearing anywhere in the reference manual. For instance, functions such as `vertex_cut` or `edge_cut` do not appear, as well as all functions defined only for directed graphs.

At that time, I thought about adding the missing files with the patch, but since there were a lot of warnings displayed by Sphinx while generating the documentation, I changed my mind.

I think it would be a good idea to use this ticket to fix this, but since it touches many files of graph theory, it may be hard to do it in a clean way. Someone has an idea of what would be the best approach ?

Issue created by migration from https://trac.sagemath.org/ticket/8513





---

archive/issue_comments_076745.json:
```json
{
    "body": "Wait until Sage 4.3.4 is released. I expect that release to fix all the warnings relating to building the HTML and PDF versions of the Sage standard documentation. At least, I expect that release to fix such warnings for the reference manual.",
    "created_at": "2010-03-13T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Wait until Sage 4.3.4 is released. I expect that release to fix all the warnings relating to building the HTML and PDF versions of the Sage standard documentation. At least, I expect that release to fix such warnings for the reference manual.



---

archive/issue_comments_076746.json:
```json
{
    "body": "Here are the warnings I get on my computer:\n\n```\n[~/Applications/sage/devel/sage-combinat/doc/en/reference]$ sage -docbuild reference html\nsphinx-build -b html -d /Users/alexandre/Applications/sage/devel/sage/doc/output/doctrees/en/reference    /Users/alexandre/Applications/sage/devel/sage/doc/en/reference /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference\nRunning Sphinx v0.6.3\nloading pickled environment... done\nbuilding [html]: targets for 612 source files that are out of date\nupdating environment: 2 added, 612 changed, 0 removed\nreading sources... [100%] sage/symbolic/ring                   curve_morphismtorcfield\n/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph:3: (ERROR/3) Unexpected indentation.\n/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.minimum_outdegree_orientation:7: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.spanning_trees_count:18: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.spanning_trees_count:27: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7926: (WARNING/2) Duplicate explicit target name: \"krg96\".\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7930: (WARNING/2) Duplicate explicit target name: \"gyll93\".\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7926: WARNING: duplicate citation KRG96, other instance in /Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7930: WARNING: duplicate citation GYLL93, other instance in /Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [100%] structure                             urve_morphismtorcfield\nwriting additional files... genindex modindex search\ncopying images... media/homology/rp2.png media/homology/simplices.png media/homology/torus.png media/homology/klein.png media/homology/torus_labelled.png\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 8 warnings.\nBuild finished.  The built documents can be found in /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference\n```\n\nI'll try to fix them and upload a patch soon.",
    "created_at": "2010-03-22T17:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76746",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Here are the warnings I get on my computer:

```
[~/Applications/sage/devel/sage-combinat/doc/en/reference]$ sage -docbuild reference html
sphinx-build -b html -d /Users/alexandre/Applications/sage/devel/sage/doc/output/doctrees/en/reference    /Users/alexandre/Applications/sage/devel/sage/doc/en/reference /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 612 source files that are out of date
updating environment: 2 added, 612 changed, 0 removed
reading sources... [100%] sage/symbolic/ring                   curve_morphismtorcfield
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph:3: (ERROR/3) Unexpected indentation.
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.minimum_outdegree_orientation:7: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.spanning_trees_count:18: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.spanning_trees_count:27: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7926: (WARNING/2) Duplicate explicit target name: "krg96".
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7930: (WARNING/2) Duplicate explicit target name: "gyll93".
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7926: WARNING: duplicate citation KRG96, other instance in /Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7930: WARNING: duplicate citation GYLL93, other instance in /Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] structure                             urve_morphismtorcfield
writing additional files... genindex modindex search
copying images... media/homology/rp2.png media/homology/simplices.png media/homology/torus.png media/homology/klein.png media/homology/torus_labelled.png
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 8 warnings.
Build finished.  The built documents can be found in /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference
```

I'll try to fix them and upload a patch soon.



---

archive/issue_comments_076747.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-03-22T17:00:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76747",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_076748.json:
```json
{
    "body": "Attachment [trac_8513_graph_theory_documentation-abm.patch](tarball://root/attachments/some-uuid/ticket8513/trac_8513_graph_theory_documentation-abm.patch) by abmasse created at 2010-03-22 19:49:21\n\nAdds digraph.py and generic_graph.py in the doctree",
    "created_at": "2010-03-22T19:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76748",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Attachment [trac_8513_graph_theory_documentation-abm.patch](tarball://root/attachments/some-uuid/ticket8513/trac_8513_graph_theory_documentation-abm.patch) by abmasse created at 2010-03-22 19:49:21

Adds digraph.py and generic_graph.py in the doctree



---

archive/issue_comments_076749.json:
```json
{
    "body": "Finally, since there weren't too many warnings, I think it's worth trying to fix all of them. This is done in the patch I just submitted.\n\nTo summarize, this patch adds the two files digraph.py and generic_graph.py to the reference manual and correct the less than 10 warnings that Sphinx was displaying.\n\nNeeds review!",
    "created_at": "2010-03-22T19:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76749",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Finally, since there weren't too many warnings, I think it's worth trying to fix all of them. This is done in the patch I just submitted.

To summarize, this patch adds the two files digraph.py and generic_graph.py to the reference manual and correct the less than 10 warnings that Sphinx was displaying.

Needs review!



---

archive/issue_comments_076750.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-03-22T19:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76750",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing priority from major to minor.



---

archive/issue_comments_076751.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-22T19:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76751",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076752.json:
```json
{
    "body": "Excellent ! Now we appear in the doc, and there are no warnings anymore.\n\nReviewing your patch, I met a few things that needed fixing in the docs, so if you agree with my modifications, you can set this to positive review.. Thank you !! :-)\n\nNathann",
    "created_at": "2010-03-23T10:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76752",
    "user": "https://github.com/nathanncohen"
}
```

Excellent ! Now we appear in the doc, and there are no warnings anymore.

Reviewing your patch, I met a few things that needed fixing in the docs, so if you agree with my modifications, you can set this to positive review.. Thank you !! :-)

Nathann



---

archive/issue_comments_076753.json:
```json
{
    "body": "I agree with your changes ! I just hope it won't overlap with any other ticket.\n\nBy the way, did you test my patch ? When I created it, I used the sage-combinat queue and it worked fine, but here, when I tried to test your patch, I created a clone (with `hg -clone t8513`) to apply your patch on top of mine, but I got the following warning.\n\n```\n[~/Applications/sage/devel/sage-t8513]$ sage -docbuild reference html\nsphinx-build -b html -d /Users/alexandre/Applications/sage/devel/sage/doc/output/doctrees/en/reference    /Users/alexandre/Applications/sage/devel/sage/doc/en/reference /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference\nRunning Sphinx v0.6.3\nloading pickled environment... done\nbuilding [html]: targets for 2 source files that are out of date\nupdating environment: 0 added, 2 changed, 0 removed\nreading sources... [100%] sage/graphs/graph                          \n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/graphs.rst:4: (WARNING/2) toctree references unknown document u'sage/graphs/digraph'\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/graphs.rst:4: (WARNING/2) toctree references unknown document u'sage/graphs/generic_graph'\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [100%] sage/graphs/graph                           \nwriting additional files... genindex modindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 2 warnings.\n```\n\nIt's strange, it doesn't accept to add the two files to the doctree, as if the path was not correct when creating a clone, but was ok with sage-combinat. Does it work fine for you?",
    "created_at": "2010-03-23T13:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76753",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

I agree with your changes ! I just hope it won't overlap with any other ticket.

By the way, did you test my patch ? When I created it, I used the sage-combinat queue and it worked fine, but here, when I tried to test your patch, I created a clone (with `hg -clone t8513`) to apply your patch on top of mine, but I got the following warning.

```
[~/Applications/sage/devel/sage-t8513]$ sage -docbuild reference html
sphinx-build -b html -d /Users/alexandre/Applications/sage/devel/sage/doc/output/doctrees/en/reference    /Users/alexandre/Applications/sage/devel/sage/doc/en/reference /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 2 source files that are out of date
updating environment: 0 added, 2 changed, 0 removed
reading sources... [100%] sage/graphs/graph                          
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/graphs.rst:4: (WARNING/2) toctree references unknown document u'sage/graphs/digraph'
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/graphs.rst:4: (WARNING/2) toctree references unknown document u'sage/graphs/generic_graph'
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] sage/graphs/graph                           
writing additional files... genindex modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 2 warnings.
```

It's strange, it doesn't accept to add the two files to the doctree, as if the path was not correct when creating a clone, but was ok with sage-combinat. Does it work fine for you?



---

archive/issue_comments_076754.json:
```json
{
    "body": "O_o\n\nOdd.... I applied your patch as usual, and I mean by this not using sage-combinat. It applied fine, and passed all tests. After my modifications, same result O_o\n\nHave you tried cloning the branch using sage -clone instead of doing it manually with hg ?\n\nNathann",
    "created_at": "2010-03-23T13:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76754",
    "user": "https://github.com/nathanncohen"
}
```

O_o

Odd.... I applied your patch as usual, and I mean by this not using sage-combinat. It applied fine, and passed all tests. After my modifications, same result O_o

Have you tried cloning the branch using sage -clone instead of doing it manually with hg ?

Nathann



---

archive/issue_comments_076755.json:
```json
{
    "body": "No idea... Anyway, I'll try it with the sage-combinat queue to look at the documentation generated by your patch and it should be fine.",
    "created_at": "2010-03-23T14:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76755",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

No idea... Anyway, I'll try it with the sage-combinat queue to look at the documentation generated by your patch and it should be fine.



---

archive/issue_comments_076756.json:
```json
{
    "body": "Attachment [trac_8513_graph_theory_documentation-smallfixes.patch](tarball://root/attachments/some-uuid/ticket8513/trac_8513_graph_theory_documentation-smallfixes.patch) by mvngu created at 2010-04-12 19:59:48",
    "created_at": "2010-04-12T19:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76756",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8513_graph_theory_documentation-smallfixes.patch](tarball://root/attachments/some-uuid/ticket8513/trac_8513_graph_theory_documentation-smallfixes.patch) by mvngu created at 2010-04-12 19:59:48



---

archive/issue_comments_076757.json:
```json
{
    "body": "I have replaced ncohen's patch with one that has the ticket number in its commit message.",
    "created_at": "2010-04-12T20:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I have replaced ncohen's patch with one that has the ticket number in its commit message.



---

archive/issue_comments_076758.json:
```json
{
    "body": "I don't know much about graph theory, but is there any sense to the current order in the reference manual?  Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the \"Graph Theory\" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)",
    "created_at": "2010-04-12T21:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76758",
    "user": "https://github.com/jhpalmieri"
}
```

I don't know much about graph theory, but is there any sense to the current order in the reference manual?  Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the "Graph Theory" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)



---

archive/issue_comments_076759.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> I don't know much about graph theory, but is there any sense to the current order in the reference manual?  Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the \"Graph Theory\" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)\n\n\nI agree with you! There is some cleanup needed in the documentation. But maybe we should wait for it in another ticket. The goal of #8513 is to quickly make the graph documentation available so that one may check if Sphinx builds all right when reviewing related tickets. If it's ok for you, of course.\n\nSorry for being so late, by the way, Nathann, I'll try to finish this ticket today or at most, during the week.",
    "created_at": "2010-04-12T22:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76759",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Replying to [comment:9 jhpalmieri]:
> I don't know much about graph theory, but is there any sense to the current order in the reference manual?  Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the "Graph Theory" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)


I agree with you! There is some cleanup needed in the documentation. But maybe we should wait for it in another ticket. The goal of #8513 is to quickly make the graph documentation available so that one may check if Sphinx builds all right when reviewing related tickets. If it's ok for you, of course.

Sorry for being so late, by the way, Nathann, I'll try to finish this ticket today or at most, during the week.



---

archive/issue_comments_076760.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> I don't know much about graph theory, but is there any sense to the current order in the reference manual?\n\n\nNo, I don't think so. The current organization is a mess.\n\n\n\n\n\n> Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  \n\n\nYes. The current organization of the graph theory modules, as they appear in the reference manual, is rather unusual. For example, the interface to cliquer appears as the very first link. One would expect something along the following line to be more natural:\n\n   * undirected graph\n   * digraph\n   * generic graph\n   * applications of graph theory\n   * fast compiled graph\n   * etc. \n\nI have uploaded a reviewer patch that does something about this. With my reviewer patch, the organization of the graph theory modules should be more systematic.\n\n\n\n\n\n> I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the \"Graph Theory\" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)\n\n\nNod. This needs to wait for another ticket.\n\n\n\n\nAfter applying [trac_8513_graph_theory_documentation-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-abm.patch) and [trac_8513_graph_theory_documentation-smallfixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-smallfixes.patch), I then rebuilt the whole Sage documentation. A long doctest of the whole Sage library resulted in the following failure:\n\n```\nsage -t -long devel/sage-main/sage/misc/sagedoc.py\n**********************************************************************\nFile \"/dev/shm/mvngu/sandbox/sage-4.3.5-8513-graph-doc/devel/sage-main/sage/misc/sagedoc.py\", line 892:\n    sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 100\nExpected:\n    True\nGot:\n    False\n```\nThis is due to adding two new files to the reference manual that happen to be about graph theory, hence the above search returns more matches for the word \"tree\". My reviewer patch should fix this doctest failure. It needs reviewing by anyone but me. I'm happy with both abmasse and ncohen's patches. Apply patches in the following order:\n\n1. [trac_8513_graph_theory_documentation-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-abm.patch)\n2. [trac_8513_graph_theory_documentation-smallfixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-smallfixes.patch)\n3. [trac_8513-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513-reviewer.patch)",
    "created_at": "2010-04-12T22:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:9 jhpalmieri]:
> I don't know much about graph theory, but is there any sense to the current order in the reference manual?


No, I don't think so. The current organization is a mess.





> Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  


Yes. The current organization of the graph theory modules, as they appear in the reference manual, is rather unusual. For example, the interface to cliquer appears as the very first link. One would expect something along the following line to be more natural:

   * undirected graph
   * digraph
   * generic graph
   * applications of graph theory
   * fast compiled graph
   * etc. 

I have uploaded a reviewer patch that does something about this. With my reviewer patch, the organization of the graph theory modules should be more systematic.





> I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the "Graph Theory" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)


Nod. This needs to wait for another ticket.




After applying [trac_8513_graph_theory_documentation-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-abm.patch) and [trac_8513_graph_theory_documentation-smallfixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-smallfixes.patch), I then rebuilt the whole Sage documentation. A long doctest of the whole Sage library resulted in the following failure:

```
sage -t -long devel/sage-main/sage/misc/sagedoc.py
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.3.5-8513-graph-doc/devel/sage-main/sage/misc/sagedoc.py", line 892:
    sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 100
Expected:
    True
Got:
    False
```
This is due to adding two new files to the reference manual that happen to be about graph theory, hence the above search returns more matches for the word "tree". My reviewer patch should fix this doctest failure. It needs reviewing by anyone but me. I'm happy with both abmasse and ncohen's patches. Apply patches in the following order:

1. [trac_8513_graph_theory_documentation-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-abm.patch)
2. [trac_8513_graph_theory_documentation-smallfixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-smallfixes.patch)
3. [trac_8513-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513-reviewer.patch)



---

archive/issue_comments_076761.json:
```json
{
    "body": "I'm running the longtest on all sage right now. Giving some feedback later tonight.",
    "created_at": "2010-04-12T22:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76761",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

I'm running the longtest on all sage right now. Giving some feedback later tonight.



---

archive/issue_comments_076762.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-12T23:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76762",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076763.json:
```json
{
    "body": "> My reviewer patch should fix this doctest failure. It needs reviewing by anyone but me.\n\n\nYour patch fixes the problem, but it doesn't really fit in sagedoc.py: the doctests there are supposed to contrast what happens if `whole_word=True` is not used (more than 2000 matches) vs. when it is (used to be fewer than 100 matches).  How about changing it to `len(...) < 150` or `len(...) < 200`?",
    "created_at": "2010-04-12T23:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76763",
    "user": "https://github.com/jhpalmieri"
}
```

> My reviewer patch should fix this doctest failure. It needs reviewing by anyone but me.


Your patch fixes the problem, but it doesn't really fit in sagedoc.py: the doctests there are supposed to contrast what happens if `whole_word=True` is not used (more than 2000 matches) vs. when it is (used to be fewer than 100 matches).  How about changing it to `len(...) < 150` or `len(...) < 200`?



---

archive/issue_comments_076764.json:
```json
{
    "body": "Attachment [trac_8513-reviewer.patch](tarball://root/attachments/some-uuid/ticket8513/trac_8513-reviewer.patch) by mvngu created at 2010-04-12 23:32:02\n\nreviewer patch",
    "created_at": "2010-04-12T23:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8513-reviewer.patch](tarball://root/attachments/some-uuid/ticket8513/trac_8513-reviewer.patch) by mvngu created at 2010-04-12 23:32:02

reviewer patch



---

archive/issue_comments_076765.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-12T23:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76765",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076766.json:
```json
{
    "body": "Replying to [comment:13 jhpalmieri]:\n> Your patch fixes the problem, but it doesn't really fit in sagedoc.py: the doctests there are supposed to contrast what happens if `whole_word=True` is not used (more than 2000 matches) vs. when it is (used to be fewer than 100 matches).  How about changing it to `len(...) < 150` or `len(...) < 200`?\n\n\nI see what you mean. Performing a search with `whole_word=False` results in too many matches. When using `whole_word=True`, we want to provide an upper bound on the number of matches. I have modified the reviewer patch accordingly.",
    "created_at": "2010-04-12T23:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76766",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:13 jhpalmieri]:
> Your patch fixes the problem, but it doesn't really fit in sagedoc.py: the doctests there are supposed to contrast what happens if `whole_word=True` is not used (more than 2000 matches) vs. when it is (used to be fewer than 100 matches).  How about changing it to `len(...) < 150` or `len(...) < 200`?


I see what you mean. Performing a search with `whole_word=False` results in too many matches. When using `whole_word=True`, we want to provide an upper bound on the number of matches. I have modified the reviewer patch accordingly.



---

archive/issue_comments_076767.json:
```json
{
    "body": "I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?",
    "created_at": "2010-04-13T02:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76767",
    "user": "https://github.com/jhpalmieri"
}
```

I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?



---

archive/issue_comments_076768.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?\n\n\nSure, if you're ok with the result. It's even better if the final reviewer isn't Nathann nor me.",
    "created_at": "2010-04-13T13:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76768",
    "user": "https://trac.sagemath.org/admin/accounts/users/abmasse"
}
```

Replying to [comment:15 jhpalmieri]:
> I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?


Sure, if you're ok with the result. It's even better if the final reviewer isn't Nathann nor me.



---

archive/issue_comments_076769.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?\n\n\nI think so. Cleaning up the modules added by this ticket to the reference manual can be split off to an enhancement ticket.",
    "created_at": "2010-04-13T23:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:15 jhpalmieri]:
> I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?


I think so. Cleaning up the modules added by this ticket to the reference manual can be split off to an enhancement ticket.



---

archive/issue_comments_076770.json:
```json
{
    "body": "See #8684 for a follow-up ticket, the purpose of which is to organize the graph theory stuff in the reference manual.  I'm not going to do this myself, since I don't know enough about graph theory in general, or the graph theory in Sage, to know how to organize it.",
    "created_at": "2010-04-14T05:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76770",
    "user": "https://github.com/jhpalmieri"
}
```

See #8684 for a follow-up ticket, the purpose of which is to organize the graph theory stuff in the reference manual.  I'm not going to do this myself, since I don't know enough about graph theory in general, or the graph theory in Sage, to know how to organize it.



---

archive/issue_comments_076771.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-14T05:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76771",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076772.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76772",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_020438.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:46:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8513#event-20438"
}
```



---

archive/issue_comments_076773.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_8513_graph_theory_documentation-abm.patch\n- trac_8513_graph_theory_documentation-smallfixes.patch\n- trac_8513-reviewer.patch",
    "created_at": "2010-04-16T18:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8513#issuecomment-76773",
    "user": "https://github.com/jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_8513_graph_theory_documentation-abm.patch
- trac_8513_graph_theory_documentation-smallfixes.patch
- trac_8513-reviewer.patch
