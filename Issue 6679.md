# Issue 6679: [with patch, needs review] Vertex Coloring, Edge Coloring (uses Linear Programming)

archive/issues_006679.json:
```json
{
    "body": "Assignee: @rlmill\n\nHello everybody !!!\n\nHere are two new functions for the Graph class in Sage : vertex_coloring and edge_coloring.\n\nThose new functions both use Linear programming, so to use them you will have to install the patches MIP-1 to MIP-5 in #6502 along with the package GLPK :\n\nhttp://trac.sagemath.org/sage_trac/ticket/6502\n\nIf you want them to be ever more efficient, you can also install COIN-OR/CBC ( from #6603 ) with this line :\n\nsage -f http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.spkg\n\nI hope I learned what I had to with my previous patch, as I hope you will find those functions sufficiently and correctly documented. These functions should be ---way--- more efficient than the previous ones, regardless of the Linear Solver you chose to use.\n\n( I have to add that I will be absent next week, but even though I will be able to answer any of your questions and to post fixes until tomorrow evening. I chosed to post these two functions now hoping they could be integrated with the patch for LP into the next release of Sage )\n\nIssue created by migration from https://trac.sagemath.org/ticket/6679\n\n",
    "created_at": "2009-08-06T15:10:42Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] Vertex Coloring, Edge Coloring (uses Linear Programming)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6679",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

Hello everybody !!!

Here are two new functions for the Graph class in Sage : vertex_coloring and edge_coloring.

Those new functions both use Linear programming, so to use them you will have to install the patches MIP-1 to MIP-5 in #6502 along with the package GLPK :

http://trac.sagemath.org/sage_trac/ticket/6502

If you want them to be ever more efficient, you can also install COIN-OR/CBC ( from #6603 ) with this line :

sage -f http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.spkg

I hope I learned what I had to with my previous patch, as I hope you will find those functions sufficiently and correctly documented. These functions should be ---way--- more efficient than the previous ones, regardless of the Linear Solver you chose to use.

( I have to add that I will be absent next week, but even though I will be able to answer any of your questions and to post fixes until tomorrow evening. I chosed to post these two functions now hoping they could be integrated with the patch for LP into the next release of Sage )

Issue created by migration from https://trac.sagemath.org/ticket/6679





---

archive/issue_comments_054787.json:
```json
{
    "body": "First patch !",
    "created_at": "2009-08-06T15:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54787",
    "user": "https://github.com/nathanncohen"
}
```

First patch !



---

archive/issue_comments_054788.json:
```json
{
    "body": "Attachment [coloring-1.2.patch](tarball://root/attachments/some-uuid/ticket6679/coloring-1.2.patch) by @nathanncohen created at 2009-08-06 15:11:44\n\nFirst patch !",
    "created_at": "2009-08-06T15:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54788",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [coloring-1.2.patch](tarball://root/attachments/some-uuid/ticket6679/coloring-1.2.patch) by @nathanncohen created at 2009-08-06 15:11:44

First patch !



---

archive/issue_comments_054789.json:
```json
{
    "body": "Hmmm... The two patches coloring-1 and coloring-1.2 are exactly identical, but I do not know how to remove the second one ^^;",
    "created_at": "2009-08-06T15:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54789",
    "user": "https://github.com/nathanncohen"
}
```

Hmmm... The two patches coloring-1 and coloring-1.2 are exactly identical, but I do not know how to remove the second one ^^;



---

archive/issue_comments_054790.json:
```json
{
    "body": "As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.\n\nSorry for the trouble, I'll try to make it quick !\n\nNathann",
    "created_at": "2009-08-31T15:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54790",
    "user": "https://github.com/nathanncohen"
}
```

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann



---

archive/issue_comments_054791.json:
```json
{
    "body": "Even shorter, even better, even more efficient... Here is the new version of these two functions, now using the symbolic version of MIP from #6869 !!!!",
    "created_at": "2009-09-03T17:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54791",
    "user": "https://github.com/nathanncohen"
}
```

Even shorter, even better, even more efficient... Here is the new version of these two functions, now using the symbolic version of MIP from #6869 !!!!



---

archive/issue_comments_054792.json:
```json
{
    "body": "Attachment [coloring-symbolic.patch](tarball://root/attachments/some-uuid/ticket6679/coloring-symbolic.patch) by @nathanncohen created at 2009-09-03 17:06:17",
    "created_at": "2009-09-03T17:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54792",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [coloring-symbolic.patch](tarball://root/attachments/some-uuid/ticket6679/coloring-symbolic.patch) by @nathanncohen created at 2009-09-03 17:06:17



---

archive/issue_comments_054793.json:
```json
{
    "body": "I have a question.  What is the relation to the already existing methods .chromatic_number() and .coloring()?\n\n```\nsage: G = graphs.PetersenGraph()\nsage: G.coloring()\n[[1, 3, 5, 9], [0, 2, 6], [4, 7, 8]]\nsage: G.chromatic_number()\n3\n```\n\nAt the very least it seems reasonable to modify .coloring() rather than add a new function, and perhaps keep the previous algorithm if that is useful.  I can't speak to which one is better, unfortunately, but it can be good to avoid a surfeit of methods.",
    "created_at": "2009-10-21T16:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54793",
    "user": "https://github.com/kcrisman"
}
```

I have a question.  What is the relation to the already existing methods .chromatic_number() and .coloring()?

```
sage: G = graphs.PetersenGraph()
sage: G.coloring()
[[1, 3, 5, 9], [0, 2, 6], [4, 7, 8]]
sage: G.chromatic_number()
3
```

At the very least it seems reasonable to modify .coloring() rather than add a new function, and perhaps keep the previous algorithm if that is useful.  I can't speak to which one is better, unfortunately, but it can be good to avoid a surfeit of methods.



---

archive/issue_comments_054794.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-10-21T16:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54794",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_054795.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-10-24T14:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54795",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_054796.json:
```json
{
    "body": "Hello !!!!\n\nI wrote this patch some time ago, and it needed an update because of some changes in class numerical.mip. Besides, your sound remark needs an answer :-)\n\nHere is what this new version of the patch does :\n\n* It creates two functions vertex_coloring and edge_coloring in the graph_coloring module.\n* I noticed there were methods defined in the graph_coloring module which were not used in the Graph class, even though they\n  were built just for that ! For example, the function Graph.chromatic_number computes the chromatic number through computing the whole Chromatic Polynomial (honestly, I do not know any worse way to compute it !), even though there is a chromnatic_number function in the graph_coloring module computing the same parameter with a different method. I updated the Graph.chromatic_number method to let the user chose one of the (now three) different ways to compute the chromatic polynomial. I set it to MILP by default ( so that it uses the new vertex_coloring method which is defined in this patch ) as I expect it to be the most efficient.\n* The same thing occured in the Graph.coloring() function. This method used a slower version of what was already available in the graph_coloring module.  It now uses the graph_coloring.first_coloring method, or the newly defined vertex_coloring method.\n* Functions graph_coloring.chromatic_number and graph_coloring.first_coloring compute things that can also be computed through the use of the newly created graph_coloring.vertex_coloring method. I think the way they compute their results is far too slow, as they compute ALL the colorings to return one, and so should be removed ( the function all_graph_colorings, which they all use, must obvously be kept ) some months from now, while they should be kept some time to compare their results with graph_coloring.vertex_coloring ( both speed and exactness )\n* Several docstring fixes, when I noticed them\n\nNathann",
    "created_at": "2009-10-24T14:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54796",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!!

I wrote this patch some time ago, and it needed an update because of some changes in class numerical.mip. Besides, your sound remark needs an answer :-)

Here is what this new version of the patch does :

* It creates two functions vertex_coloring and edge_coloring in the graph_coloring module.
* I noticed there were methods defined in the graph_coloring module which were not used in the Graph class, even though they
  were built just for that ! For example, the function Graph.chromatic_number computes the chromatic number through computing the whole Chromatic Polynomial (honestly, I do not know any worse way to compute it !), even though there is a chromnatic_number function in the graph_coloring module computing the same parameter with a different method. I updated the Graph.chromatic_number method to let the user chose one of the (now three) different ways to compute the chromatic polynomial. I set it to MILP by default ( so that it uses the new vertex_coloring method which is defined in this patch ) as I expect it to be the most efficient.
* The same thing occured in the Graph.coloring() function. This method used a slower version of what was already available in the graph_coloring module.  It now uses the graph_coloring.first_coloring method, or the newly defined vertex_coloring method.
* Functions graph_coloring.chromatic_number and graph_coloring.first_coloring compute things that can also be computed through the use of the newly created graph_coloring.vertex_coloring method. I think the way they compute their results is far too slow, as they compute ALL the colorings to return one, and so should be removed ( the function all_graph_colorings, which they all use, must obvously be kept ) some months from now, while they should be kept some time to compare their results with graph_coloring.vertex_coloring ( both speed and exactness )
* Several docstring fixes, when I noticed them

Nathann



---

archive/issue_comments_054797.json:
```json
{
    "body": "Added round_robin, and a more efficient coloring for complete graphs",
    "created_at": "2009-11-10T09:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54797",
    "user": "https://github.com/nathanncohen"
}
```

Added round_robin, and a more efficient coloring for complete graphs



---

archive/issue_comments_054798.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-25T04:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054799.json:
```json
{
    "body": "I assume that the patch `trac_6679.patch` is the one to review, so here goes. Here are some issues:\n\n1. For the function `chromatic_number()`, it's a bad idea to make \"MILP\" the default algorithm choice because that algorithm requires the installation of an optional package. Imagine the surprise (and confusion) when one uses the function `chromatic_number()` with the default value, but neither GLPK nor CBC is installed. You can make some algorithm a default choice provided that it's in a standard package or in the Sage library. If you have another algorithm that uses an optional package, you could still provide an interface to that algorithm and document uses of that algorithm in the docstring. So between \"CP\" and \"DLX\", choose one and make that algorithm the default choice. You have clearly documented how to use the \"MILP\" algorithm, which is good for those who want a better algorithm.\n2. You don't need to put spaces between the sign \"=\" if it occurs as part of assigning a value to an argument in a function call, like in `chromatic_number(algorithm=\"MILP\")`. To follow coding conventions, you should put spaces between operators. So instead of doing `algorithm==\"CP\"`, you should do `algorithm == \"CP\"`. You can read more about Python coding conventions in [PEP 8](http://www.python.org/dev/peps/pep-0008/).\n3. Use the style of raising exceptions that is compatible with Python 3.x. For example, the following is not recommended for being compatible with Python 3.x:\n {{{\nraise ValueError, \"The `algorithm` variable must be set to either `DLX`, `MILP` or `CP`.\"\n }}}\n However, the following style is compatible with Python 3.x:\n {{{\nraise ValueError(\"The `algorithm` variable must be set to either `DLX`, `MILP` or `CP`.\")\n }}}\n Lots of code in the Sage library still uses the old style of raising exceptions. This will come back to haunt us when the time comes to switch to Python 3.x.\n1. The formatting of docstring is inconsistent.",
    "created_at": "2009-11-25T04:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54799",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I assume that the patch `trac_6679.patch` is the one to review, so here goes. Here are some issues:

1. For the function `chromatic_number()`, it's a bad idea to make "MILP" the default algorithm choice because that algorithm requires the installation of an optional package. Imagine the surprise (and confusion) when one uses the function `chromatic_number()` with the default value, but neither GLPK nor CBC is installed. You can make some algorithm a default choice provided that it's in a standard package or in the Sage library. If you have another algorithm that uses an optional package, you could still provide an interface to that algorithm and document uses of that algorithm in the docstring. So between "CP" and "DLX", choose one and make that algorithm the default choice. You have clearly documented how to use the "MILP" algorithm, which is good for those who want a better algorithm.
2. You don't need to put spaces between the sign "=" if it occurs as part of assigning a value to an argument in a function call, like in `chromatic_number(algorithm="MILP")`. To follow coding conventions, you should put spaces between operators. So instead of doing `algorithm=="CP"`, you should do `algorithm == "CP"`. You can read more about Python coding conventions in [PEP 8](http://www.python.org/dev/peps/pep-0008/).
3. Use the style of raising exceptions that is compatible with Python 3.x. For example, the following is not recommended for being compatible with Python 3.x:
 {{{
raise ValueError, "The `algorithm` variable must be set to either `DLX`, `MILP` or `CP`."
 }}}
 However, the following style is compatible with Python 3.x:
 {{{
raise ValueError("The `algorithm` variable must be set to either `DLX`, `MILP` or `CP`.")
 }}}
 Lots of code in the Sage library still uses the old style of raising exceptions. This will come back to haunt us when the time comes to switch to Python 3.x.
1. The formatting of docstring is inconsistent.



---

archive/issue_comments_054800.json:
```json
{
    "body": "Patch updated ! I also noticed I had forgotten one \"optional\" tag in the docstrings, and I rewrote all the ValueError I was able to find in the whole file.\n\nI have a question though : I build the reference to check the docstrings and noticed the file graph_colouring.pyx was not included in them : should we change it ?\n\nThere are still many \"test\" functions in this file that may not be of interest to the user, though.... \n\nIn any case, thank you very much for your help :-)\n\nNathann",
    "created_at": "2009-11-25T08:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54800",
    "user": "https://github.com/nathanncohen"
}
```

Patch updated ! I also noticed I had forgotten one "optional" tag in the docstrings, and I rewrote all the ValueError I was able to find in the whole file.

I have a question though : I build the reference to check the docstrings and noticed the file graph_colouring.pyx was not included in them : should we change it ?

There are still many "test" functions in this file that may not be of interest to the user, though.... 

In any case, thank you very much for your help :-)

Nathann



---

archive/issue_comments_054801.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-25T08:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54801",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054802.json:
```json
{
    "body": "Attachment [trac_6679.patch](tarball://root/attachments/some-uuid/ticket6679/trac_6679.patch) by mvngu created at 2009-11-25 08:25:09\n\nReplying to [comment:14 ncohen]:\n> I have a question though : I build the reference to check the docstrings and noticed the file graph_colouring.pyx was not included in them : should we change it ?\nAn ultimate goal is to include all documentation of the Sage library in the reference manual. So, yes to your suggestion. Please open another ticket to include the file `sage/graph/graph_coloring.py` in the reference manual.",
    "created_at": "2009-11-25T08:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54802",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6679.patch](tarball://root/attachments/some-uuid/ticket6679/trac_6679.patch) by mvngu created at 2009-11-25 08:25:09

Replying to [comment:14 ncohen]:
> I have a question though : I build the reference to check the docstrings and noticed the file graph_colouring.pyx was not included in them : should we change it ?
An ultimate goal is to include all documentation of the Sage library in the reference manual. So, yes to your suggestion. Please open another ticket to include the file `sage/graph/graph_coloring.py` in the reference manual.



---

archive/issue_comments_054803.json:
```json
{
    "body": "based on trac_6679.patch",
    "created_at": "2009-12-01T18:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54803",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on trac_6679.patch



---

archive/issue_comments_054804.json:
```json
{
    "body": "Attachment [trac_6679-reviewer.patch](tarball://root/attachments/some-uuid/ticket6679/trac_6679-reviewer.patch) by mvngu created at 2009-12-01 18:21:26\n\nThe patch `trac_6679.patch` applies OK against Sage 4.3.alpha0. All doctests pass with the options `-t -long`, apart from the following known doctest failure:\n\n```\nsage -t -long devel/sage/sage/interfaces/maxima.py # 1 doctests failed\n```\n\nThe doctests also pass with the optional packages `cbc-2.3.p0` and `glpk-4.38.p2`, again with the above failure. In the function `first_coloring`(), the function signature states that `hex_colors=True`, which means that `hex_colors` is `True` by default. Yet, the documentation of this keyword claims otherwise. I have adjusted the documentation and value of `hex_colors` accordingly. However, it's crucial that you check my changes because in the function `coloring()` its default value is `False`. I have attached the reviewer patch `trac_6679-reviewer.patch`. Only my patch needs review. You should apply patches in this order:\n\n1. `trac_6679.patch`\n2. `trac_6679-reviewer.patch`",
    "created_at": "2009-12-01T18:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54804",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6679-reviewer.patch](tarball://root/attachments/some-uuid/ticket6679/trac_6679-reviewer.patch) by mvngu created at 2009-12-01 18:21:26

The patch `trac_6679.patch` applies OK against Sage 4.3.alpha0. All doctests pass with the options `-t -long`, apart from the following known doctest failure:

```
sage -t -long devel/sage/sage/interfaces/maxima.py # 1 doctests failed
```

The doctests also pass with the optional packages `cbc-2.3.p0` and `glpk-4.38.p2`, again with the above failure. In the function `first_coloring`(), the function signature states that `hex_colors=True`, which means that `hex_colors` is `True` by default. Yet, the documentation of this keyword claims otherwise. I have adjusted the documentation and value of `hex_colors` accordingly. However, it's crucial that you check my changes because in the function `coloring()` its default value is `False`. I have attached the reviewer patch `trac_6679-reviewer.patch`. Only my patch needs review. You should apply patches in this order:

1. `trac_6679.patch`
2. `trac_6679-reviewer.patch`



---

archive/issue_comments_054805.json:
```json
{
    "body": "Well, graph coloring may be used to plot graphs but most of the time, its output is used to do more interesting things, so I think settng the default behaviour to returning the partition of independent sets is safe :-)\n\nShort of this :\n* I'll remember to use xrange instead of range\n* I'll try not to go beyond 70 characters *even in the code*\n* I'll put more spaces in my code\n\nAnd I thank you very very very much for your help !!! I agreed with all of your changes while reading the patch file, you're doing a great job !! \n\nNathann",
    "created_at": "2009-12-01T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54805",
    "user": "https://github.com/nathanncohen"
}
```

Well, graph coloring may be used to plot graphs but most of the time, its output is used to do more interesting things, so I think settng the default behaviour to returning the partition of independent sets is safe :-)

Short of this :
* I'll remember to use xrange instead of range
* I'll try not to go beyond 70 characters *even in the code*
* I'll put more spaces in my code

And I thank you very very very much for your help !!! I agreed with all of your changes while reading the patch file, you're doing a great job !! 

Nathann



---

archive/issue_comments_054806.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-01T18:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54806",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006914.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-02T09:50:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6679#event-6914"
}
```



---

archive/issue_comments_054807.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-02T09:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6679#issuecomment-54807",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
