# Issue 7675: shortest_path in c_graph should have an optional flag distance=False to return only the distance

archive/issues_007675.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @dimpase @dcoudert\n\nThis modification would avoid the building of the shortest path, which is interesting for a function so often used !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7675\n\n",
    "created_at": "2009-12-13T11:05:00Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.1",
    "title": "shortest_path in c_graph should have an optional flag distance=False to return only the distance",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7675",
    "user": "@nathanncohen"
}
```
Assignee: @rlmill

CC:  @dimpase @dcoudert

This modification would avoid the building of the shortest path, which is interesting for a function so often used !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7675





---

archive/issue_comments_065785.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65785",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_065786.json:
```json
{
    "body": "Hi\n\nI am Lokesh. I wanted to work on this ticket. I have made the changes in c_graph.pyx and generic_graph.py . I had an issue that changes I have made in generic_graph.py do not appear in the git status output. Further the shortest_paths function in generic_graph.py uses functions from boost_graph.pyx . Am I supposed to make the changes in boost_graph.pyx functions as well because internally they call boost library functions. For networkx I replaced the function call to an appropriate one which returns the distance. Should I try to do something similar here as well?",
    "created_at": "2017-05-17T18:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65786",
    "user": "@lokeshj1703"
}
```

Hi

I am Lokesh. I wanted to work on this ticket. I have made the changes in c_graph.pyx and generic_graph.py . I had an issue that changes I have made in generic_graph.py do not appear in the git status output. Further the shortest_paths function in generic_graph.py uses functions from boost_graph.pyx . Am I supposed to make the changes in boost_graph.pyx functions as well because internally they call boost library functions. For networkx I replaced the function call to an appropriate one which returns the distance. Should I try to do something similar here as well?



---

archive/issue_comments_065787.json:
```json
{
    "body": "Replying to [comment:6 jlokesh]:\n> Hi\n> \n> I am Lokesh.\nWelcome to Sagemath\n\n> I wanted to work on this ticket. I have made the changes in c_graph.pyx and generic_graph.py . I had an issue that changes I have made in generic_graph.py do not appear in the git status output. \nI'm not a git guru, so others may have better ideas of what's going on\n* Have you created a new branch first?\n* Do you see your changes with `git diff` ?\n* To commit your changes, I recommend to write `git commit -m \"trac #7675: short and relevant description of this commit\" -a`\n* then push your branch for instance in `u/jlokesh/7675`\n* the page http://doc.sagemath.org/html/en/developer/manual_git.html is very useful\n\nAlso, to test your changes, you can do (other methods might also be good/better)\n* `./sage -btp src/sage/graphs/` or `./sage -btp src/sage/graphs/generic_graph.py` to both compile the code and check if it passes all tests\n* `./sage -docbuild reference/graphs html` to rebuild the documentation of the graph module only. Be aware that from time to time you will be forced to rebuild the doc from scratch with `make doc-clean && make`\n\n\n> Further the shortest_paths function in generic_graph.py uses functions from boost_graph.pyx . Am I supposed to make the changes in boost_graph.pyx functions as well because internally they call boost library functions. For networkx I replaced the function call to an appropriate one which returns the distance. Should I try to do something similar here as well?\n\nThe changes you do should be consistent for all algorithms.",
    "created_at": "2017-05-18T07:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65787",
    "user": "@dcoudert"
}
```

Replying to [comment:6 jlokesh]:
> Hi
> 
> I am Lokesh.
Welcome to Sagemath

> I wanted to work on this ticket. I have made the changes in c_graph.pyx and generic_graph.py . I had an issue that changes I have made in generic_graph.py do not appear in the git status output. 
I'm not a git guru, so others may have better ideas of what's going on
* Have you created a new branch first?
* Do you see your changes with `git diff` ?
* To commit your changes, I recommend to write `git commit -m "trac #7675: short and relevant description of this commit" -a`
* then push your branch for instance in `u/jlokesh/7675`
* the page http://doc.sagemath.org/html/en/developer/manual_git.html is very useful

Also, to test your changes, you can do (other methods might also be good/better)
* `./sage -btp src/sage/graphs/` or `./sage -btp src/sage/graphs/generic_graph.py` to both compile the code and check if it passes all tests
* `./sage -docbuild reference/graphs html` to rebuild the documentation of the graph module only. Be aware that from time to time you will be forced to rebuild the doc from scratch with `make doc-clean && make`


> Further the shortest_paths function in generic_graph.py uses functions from boost_graph.pyx . Am I supposed to make the changes in boost_graph.pyx functions as well because internally they call boost library functions. For networkx I replaced the function call to an appropriate one which returns the distance. Should I try to do something similar here as well?

The changes you do should be consistent for all algorithms.



---

archive/issue_comments_065788.json:
```json
{
    "body": "I have added the distance_flag parameter to the shortest_path function of generic_graph.py and all the functions which are called from this function. I couldn't add it to boost_graph.pyx function as it returns both distance and path dictionaries in a list. Any changes to these functions lead to failure of doctests as they are used by other functions.\nIf distance_flag is True and u,v are not connected then the shortest_path function returns None or an exception based on the algorithm used. Networkx returns an exception. Should I also raise an exception for such a case?\n----\nNew commits:",
    "created_at": "2017-05-20T09:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65788",
    "user": "@lokeshj1703"
}
```

I have added the distance_flag parameter to the shortest_path function of generic_graph.py and all the functions which are called from this function. I couldn't add it to boost_graph.pyx function as it returns both distance and path dictionaries in a list. Any changes to these functions lead to failure of doctests as they are used by other functions.
If distance_flag is True and u,v are not connected then the shortest_path function returns None or an exception based on the algorithm used. Networkx returns an exception. Should I also raise an exception for such a case?
----
New commits:



---

archive/issue_comments_065789.json:
```json
{
    "body": "Hello,\n\nYou have apparently not seen that we have methods like `shortest_path_length` and `shortest_path_lengths` to get the shortest path length from `u` to `v` and from `u` to all reachable vertices. So you should not add `distance_flag` to `shortest_path` in `generic_graph`.\n\nThe original motivation for this ticket is to get a faster method for computing shortest path length(s) with `c_graph`, avoiding to first compute and return the shortest path and then compute its length as is currently done in `shortest_path_length` and `shortest_path_lengths` (except for boost methods).\n\nThis said, in `c_graph.pyx`:\n* in method `shortest_path`, you don't need to add a `else`. Indeed, if `distance_flag==True`, then you return the distance. Otherwise you continue. So don't change the indentation of subsequent lines.\n* I don't understand why you condition the operation `pred_current, pred_other = pred_other, pred_current` to the value of `distance_flag`. This is only a exchange of pointers, no?\n* Same remarks for `bidirectional_dijkstra`\n* Concerning method `shortest_path_all_vertices`, you should use the variable `d` (but move it's +1 earlier in the loop) to write `distances_int[self.vertex_label(v_int)] = d`\n\nIn `generic_graph.py`:\n* don't modify methods `shortest_path` and `shortest_paths`\n* do the appropriate changes in methods `shortest_path_length` and `shortest_path_lengths`\n\nFinally, please use a shorter name for the branch like `u/jlokesh/7675` and adopt the good practice of `git commit -m \"trac #7675: short but relevant description of this commit\" -a`. You can also make multiple commits.",
    "created_at": "2017-05-20T10:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65789",
    "user": "@dcoudert"
}
```

Hello,

You have apparently not seen that we have methods like `shortest_path_length` and `shortest_path_lengths` to get the shortest path length from `u` to `v` and from `u` to all reachable vertices. So you should not add `distance_flag` to `shortest_path` in `generic_graph`.

The original motivation for this ticket is to get a faster method for computing shortest path length(s) with `c_graph`, avoiding to first compute and return the shortest path and then compute its length as is currently done in `shortest_path_length` and `shortest_path_lengths` (except for boost methods).

This said, in `c_graph.pyx`:
* in method `shortest_path`, you don't need to add a `else`. Indeed, if `distance_flag==True`, then you return the distance. Otherwise you continue. So don't change the indentation of subsequent lines.
* I don't understand why you condition the operation `pred_current, pred_other = pred_other, pred_current` to the value of `distance_flag`. This is only a exchange of pointers, no?
* Same remarks for `bidirectional_dijkstra`
* Concerning method `shortest_path_all_vertices`, you should use the variable `d` (but move it's +1 earlier in the loop) to write `distances_int[self.vertex_label(v_int)] = d`

In `generic_graph.py`:
* don't modify methods `shortest_path` and `shortest_paths`
* do the appropriate changes in methods `shortest_path_length` and `shortest_path_lengths`

Finally, please use a shorter name for the branch like `u/jlokesh/7675` and adopt the good practice of `git commit -m "trac #7675: short but relevant description of this commit" -a`. You can also make multiple commits.



---

archive/issue_comments_065790.json:
```json
{
    "body": "I just wanted to point out that there are cases where a one-line commit message is not appropriate, and you would add a multi-line explanation there (without using `-m` flag, \nbut letting git pop-up an editor to write the commit message in).\n\nAnother handy thing is `git commit --amend` to change the last commit (can be only the message, or also actual changes).",
    "created_at": "2017-05-20T10:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65790",
    "user": "@dimpase"
}
```

I just wanted to point out that there are cases where a one-line commit message is not appropriate, and you would add a multi-line explanation there (without using `-m` flag, 
but letting git pop-up an editor to write the commit message in).

Another handy thing is `git commit --amend` to change the last commit (can be only the message, or also actual changes).



---

archive/issue_comments_065791.json:
```json
{
    "body": "Hi\n\nThanks for the review. I have incorporated the changes in c_graph.pyx. For generic_graph.py I had made the changes for networkx function calls for example I had replaced networkx.single_source_dijkstra_path(G, u) with networkx.single_source_dijkstra_path_length(G, u). Similarly for boost function call I had done away with the code which builds the path in shortest_paths. If you want these changes as well I can just call shortest_path in shortest_path_length with distance_flag as True or I can include all these changes of networkx in shortest_path_length and shortest_path_lengths.",
    "created_at": "2017-05-20T12:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65791",
    "user": "@lokeshj1703"
}
```

Hi

Thanks for the review. I have incorporated the changes in c_graph.pyx. For generic_graph.py I had made the changes for networkx function calls for example I had replaced networkx.single_source_dijkstra_path(G, u) with networkx.single_source_dijkstra_path_length(G, u). Similarly for boost function call I had done away with the code which builds the path in shortest_paths. If you want these changes as well I can just call shortest_path in shortest_path_length with distance_flag as True or I can include all these changes of networkx in shortest_path_length and shortest_path_lengths.



---

archive/issue_comments_065792.json:
```json
{
    "body": "I'm not sure to understand what you have changed or not.\n\nFor sure, you should not modify the `shortest_path` method in `generic_graph`, but change the `shortest_path_length` method.",
    "created_at": "2017-05-20T15:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65792",
    "user": "@dcoudert"
}
```

I'm not sure to understand what you have changed or not.

For sure, you should not modify the `shortest_path` method in `generic_graph`, but change the `shortest_path_length` method.



---

archive/issue_comments_065793.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-05-21T10:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65793",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065794.json:
```json
{
    "body": "Hi\n\nI have uploaded changes for shortest_path_length and shortest_path_lengths. Sorry, I couldn't figure out the command for changing the remote branch name.",
    "created_at": "2017-05-21T10:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65794",
    "user": "@lokeshj1703"
}
```

Hi

I have uploaded changes for shortest_path_length and shortest_path_lengths. Sorry, I couldn't figure out the command for changing the remote branch name.



---

archive/issue_comments_065795.json:
```json
{
    "body": "Replying to [comment:15 jlokesh]:\n> Hi\n> \n> I have uploaded changes for shortest_path_length and shortest_path_lengths. Sorry, I couldn't figure out the command for changing the remote branch name.\n\nread on remote branches in git.\ne.g you can remove a remote branch via `git push` with --delete option.",
    "created_at": "2017-05-21T11:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65795",
    "user": "@dimpase"
}
```

Replying to [comment:15 jlokesh]:
> Hi
> 
> I have uploaded changes for shortest_path_length and shortest_path_lengths. Sorry, I couldn't figure out the command for changing the remote branch name.

read on remote branches in git.
e.g you can remove a remote branch via `git push` with --delete option.



---

archive/issue_comments_065796.json:
```json
{
    "body": "This is much better. It passes all tests (graphs, matroid, sandpile, knots) and the doc builds properly.\n\nCould you adopt the following convention:\n\n```\n        - ``distance_flag`` -- boolean (default: ``False``). When set to ``True``, the\n          shortest path distance from ``x`` to ``y`` is returned instead of the path.\n```\n\n\n\nAlso, I'm wondering if we could return 5 instead of 5.0. May be Dima can answer this question ?\n----\nNew commits:",
    "created_at": "2017-05-21T15:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65796",
    "user": "@dcoudert"
}
```

This is much better. It passes all tests (graphs, matroid, sandpile, knots) and the doc builds properly.

Could you adopt the following convention:

```
        - ``distance_flag`` -- boolean (default: ``False``). When set to ``True``, the
          shortest path distance from ``x`` to ``y`` is returned instead of the path.
```



Also, I'm wondering if we could return 5 instead of 5.0. May be Dima can answer this question ?
----
New commits:



---

archive/issue_comments_065797.json:
```json
{
    "body": "I think it's actually a bug introduced in the branch of this ticket that makes `Dijkstra_Bid` return `float` (there is `cdef float...` there). While I cannot find explicit documentation on the type of weights allowed, I cannot imagine `float` being the right type. This type depends upon the type of weight of a particular graph. \nBy common sense, one needs weights to satisfy certain basic properties: one should be able to add them, and to compare them for `<`, and there should be `0` in this type, but that's all; e.g. certainly `float` is a wrong type to use if weights are, say, rational numbers.\n\nIt would be good to dig up whether the code does any kind of checking on weights, and document this. If there are no checks done, i.e. you can get weird results, or perhaps even crashes, by using weights which are, say, integers mod 3, this ought to be documented as well.",
    "created_at": "2017-05-22T09:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65797",
    "user": "@dimpase"
}
```

I think it's actually a bug introduced in the branch of this ticket that makes `Dijkstra_Bid` return `float` (there is `cdef float...` there). While I cannot find explicit documentation on the type of weights allowed, I cannot imagine `float` being the right type. This type depends upon the type of weight of a particular graph. 
By common sense, one needs weights to satisfy certain basic properties: one should be able to add them, and to compare them for `<`, and there should be `0` in this type, but that's all; e.g. certainly `float` is a wrong type to use if weights are, say, rational numbers.

It would be good to dig up whether the code does any kind of checking on weights, and document this. If there are no checks done, i.e. you can get weird results, or perhaps even crashes, by using weights which are, say, integers mod 3, this ought to be documented as well.



---

archive/issue_comments_065798.json:
```json
{
    "body": "One certain thing to check in doctests is whether cycles of negative length in the graph lead to a crash---if an implementation does not check whether it creates loops in \"shortest\" paths it is building, then it would not terminate (normally).",
    "created_at": "2017-05-22T09:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65798",
    "user": "@dimpase"
}
```

One certain thing to check in doctests is whether cycles of negative length in the graph lead to a crash---if an implementation does not check whether it creates loops in "shortest" paths it is building, then it would not terminate (normally).



---

archive/issue_comments_065799.json:
```json
{
    "body": "Hello,\n\n* The goal of this ticket is to speed up some calls when asking for the distance and not the path. We do not change the behavior of the algorithms. That is, if the algorithm was not able to detect negative cycles before, it will be the same after. If it was able to detect negative cycles, then it will continue to do so. If a correction of a shortest path algorithm has to be performed, it must be done in another ticket.\n* Concerning the use of `float` in `bidirectional_dijkstra`. I agree it is certainly not the good type here. May be we should simply remove the type for variables `distance` and `f_tmp` and let Python/Cython decide ? Or may be there is a more suitable type to use here ? Who should we ask ?\n* Concerning the possibility edge labels are integer mod 3. Yes, one can certainly do it and as far as I know, no graph algorithm is protected against such weird use. If one wants to protect graphs against such weird use, a specific ticket should be opened, for instance to improve method `_check_weight_function` or to add an extra method like `_check_edge_labels`",
    "created_at": "2017-05-22T10:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65799",
    "user": "@dcoudert"
}
```

Hello,

* The goal of this ticket is to speed up some calls when asking for the distance and not the path. We do not change the behavior of the algorithms. That is, if the algorithm was not able to detect negative cycles before, it will be the same after. If it was able to detect negative cycles, then it will continue to do so. If a correction of a shortest path algorithm has to be performed, it must be done in another ticket.
* Concerning the use of `float` in `bidirectional_dijkstra`. I agree it is certainly not the good type here. May be we should simply remove the type for variables `distance` and `f_tmp` and let Python/Cython decide ? Or may be there is a more suitable type to use here ? Who should we ask ?
* Concerning the possibility edge labels are integer mod 3. Yes, one can certainly do it and as far as I know, no graph algorithm is protected against such weird use. If one wants to protect graphs against such weird use, a specific ticket should be opened, for instance to improve method `_check_weight_function` or to add an extra method like `_check_edge_labels`



---

archive/issue_comments_065800.json:
```json
{
    "body": "Hi\n\nAre the documentation changes the only changes required for this ticket currently?",
    "created_at": "2017-05-31T04:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65800",
    "user": "@lokeshj1703"
}
```

Hi

Are the documentation changes the only changes required for this ticket currently?



---

archive/issue_comments_065801.json:
```json
{
    "body": "can you try to fix the tyep float issue discussed above ?",
    "created_at": "2017-05-31T10:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65801",
    "user": "@dcoudert"
}
```

can you try to fix the tyep float issue discussed above ?



---

archive/issue_comments_065802.json:
```json
{
    "body": "It should suffice to remove the declaration of that `float` variable.\nThen its type will be handled dynamically by Python.",
    "created_at": "2017-05-31T14:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65802",
    "user": "@dimpase"
}
```

It should suffice to remove the declaration of that `float` variable.
Then its type will be handled dynamically by Python.



---

archive/issue_comments_065803.json:
```json
{
    "body": "I have removed the declarations and it is working correctly now. Its also able to handle rational numbers as weights.",
    "created_at": "2017-05-31T14:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65803",
    "user": "@lokeshj1703"
}
```

I have removed the declarations and it is working correctly now. Its also able to handle rational numbers as weights.



---

archive/issue_comments_065804.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-01T17:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65804",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065805.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2017-06-02T00:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65805",
    "user": "@dimpase"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_065806.json:
```json
{
    "body": "OK, this looks good. Please do not forget to fill in \"Authors:\" field next time (I copied the name from your email, hopefully it's the way prefer it written).",
    "created_at": "2017-06-02T00:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65806",
    "user": "@dimpase"
}
```

OK, this looks good. Please do not forget to fill in "Authors:" field next time (I copied the name from your email, hopefully it's the way prefer it written).



---

archive/issue_comments_065807.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2017-06-03T06:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65807",
    "user": "@tscrim"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_065808.json:
```json
{
    "body": "Sorry to post a little late with comments, but there are a few small things I think need to be addressed.\n\nI don't see the need or desire to have a separate dict `distances_int` in `shortest_path_all_vertices`. Just add an extra `if` statement when initializing `distances[v]`. IMO it is cleaner code and doesn't require allocating an unnecessary object.\n\nThis is both the wrong type of error (for the message) and the wrong statement:\n\n```\n            raise ValueError(\"Algorithm \" + algorithm + \" not yet \" +\n                             \"implemented. Please, contribute!\")\n```\n\nFor example, `algorithm='foobar'` says we should implement a fictitious algorithm. A `ValueError` is the correct error message, but it should say something like `'unknown algorithm \"{}\"'.format(algorithm)`. (Edit: Yes, no capital letter. Bad splicing of my post.)\n\nMinor point, but for easier readability (PEP8), use `a == b` instead of `a==b` and similarly:\n\n```\ndef shortest_path_all_vertices(self, v, cutoff=None, distance_flag=False):\n```\n",
    "created_at": "2017-06-03T06:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65808",
    "user": "@tscrim"
}
```

Sorry to post a little late with comments, but there are a few small things I think need to be addressed.

I don't see the need or desire to have a separate dict `distances_int` in `shortest_path_all_vertices`. Just add an extra `if` statement when initializing `distances[v]`. IMO it is cleaner code and doesn't require allocating an unnecessary object.

This is both the wrong type of error (for the message) and the wrong statement:

```
            raise ValueError("Algorithm " + algorithm + " not yet " +
                             "implemented. Please, contribute!")
```

For example, `algorithm='foobar'` says we should implement a fictitious algorithm. A `ValueError` is the correct error message, but it should say something like `'unknown algorithm "{}"'.format(algorithm)`. (Edit: Yes, no capital letter. Bad splicing of my post.)

Minor point, but for easier readability (PEP8), use `a == b` instead of `a==b` and similarly:

```
def shortest_path_all_vertices(self, v, cutoff=None, distance_flag=False):
```




---

archive/issue_comments_065809.json:
```json
{
    "body": "I agree that we can safely get ride of the `distances_int` dict using an extra `if`. It will be cleaner.\n\nFor the error message, the convention to follow is `raise ValueError('unknown algorithm \"{}\"'.format(algorithm))`, so without capital letter for the first word and no `.` at the end.\n\nSo you also have to change `raise ValueError(\"The 'BFS_Bid' algorithm does not work on weighted graphs.\"` to `raise ValueError(\"the 'BFS_Bid' algorithm does not work on weighted graphs\")`",
    "created_at": "2017-06-03T11:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65809",
    "user": "@dcoudert"
}
```

I agree that we can safely get ride of the `distances_int` dict using an extra `if`. It will be cleaner.

For the error message, the convention to follow is `raise ValueError('unknown algorithm "{}"'.format(algorithm))`, so without capital letter for the first word and no `.` at the end.

So you also have to change `raise ValueError("The 'BFS_Bid' algorithm does not work on weighted graphs."` to `raise ValueError("the 'BFS_Bid' algorithm does not work on weighted graphs")`



---

archive/issue_comments_065810.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-03T15:18:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65810",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065811.json:
```json
{
    "body": "One last thing (well, in 2 places):\n\n```diff\n-distance_flag = False):\n+distance_flag=False):\n```\n",
    "created_at": "2017-06-03T22:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65811",
    "user": "@tscrim"
}
```

One last thing (well, in 2 places):

```diff
-distance_flag = False):
+distance_flag=False):
```




---

archive/issue_comments_065812.json:
```json
{
    "body": "Hi\n\n\n\n```\nraise ValueError(\"Algorithm \" + algorithm + \" not yet \" +\n                             \"implemented. Please, contribute!\")\n```\n\nis used by other algorithms like triangles_count, shortest_paths and shortest_path_all_pairs. Should I make the corresponding change in those algorithms as well?",
    "created_at": "2017-06-04T07:03:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65812",
    "user": "@lokeshj1703"
}
```

Hi



```
raise ValueError("Algorithm " + algorithm + " not yet " +
                             "implemented. Please, contribute!")
```

is used by other algorithms like triangles_count, shortest_paths and shortest_path_all_pairs. Should I make the corresponding change in those algorithms as well?



---

archive/issue_comments_065813.json:
```json
{
    "body": "While we should be wary of \"ticket creep\", I think in this case it isn't so bad to change it across the board in graphs here for simplicity.",
    "created_at": "2017-06-04T08:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65813",
    "user": "@tscrim"
}
```

While we should be wary of "ticket creep", I think in this case it isn't so bad to change it across the board in graphs here for simplicity.



---

archive/issue_comments_065814.json:
```json
{
    "body": "It should be ok to do so, but be aware that some tickets like #23124 are currently modifying many files in `graphs`.\n\nIn `shortest_paths`, please change \n`if self.num_verts()==1 and self.vertices()[0]==u` to\n`if self.order() == 1 and self.has_vertex(u):`",
    "created_at": "2017-06-04T08:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65814",
    "user": "@dcoudert"
}
```

It should be ok to do so, but be aware that some tickets like #23124 are currently modifying many files in `graphs`.

In `shortest_paths`, please change 
`if self.num_verts()==1 and self.vertices()[0]==u` to
`if self.order() == 1 and self.has_vertex(u):`



---

archive/issue_comments_065815.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-05T17:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65815",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065816.json:
```json
{
    "body": "don't forget to update the tests with the new error message.",
    "created_at": "2017-06-05T17:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65816",
    "user": "@dcoudert"
}
```

don't forget to update the tests with the new error message.



---

archive/issue_comments_065817.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-05T18:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65817",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065818.json:
```json
{
    "body": "I forgot to update the tests for the changes made to the error message. The second commit makes those changes.",
    "created_at": "2017-06-05T18:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65818",
    "user": "@lokeshj1703"
}
```

I forgot to update the tests for the changes made to the error message. The second commit makes those changes.



---

archive/issue_comments_065819.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2017-06-06T00:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65819",
    "user": "@tscrim"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_065820.json:
```json
{
    "body": "LGTM.",
    "created_at": "2017-06-06T00:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65820",
    "user": "@tscrim"
}
```

LGTM.



---

archive/issue_comments_065821.json:
```json
{
    "body": "Looking at the code, I realize that we have the following problem:\n\n```\nsage: G = Graph()\nsage: 2 in G\nFalse\nsage: G.shortest_path(2,2)\n[2]\nsage: G.shortest_path_length(2,2)\n0\n```\n\nI don't know why it has not been reported before.\n\nCan you add necessary tests to check that u and v are in the graph and raise an error if it is not the case.\n\nThanks.",
    "created_at": "2017-06-06T07:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65821",
    "user": "@dcoudert"
}
```

Looking at the code, I realize that we have the following problem:

```
sage: G = Graph()
sage: 2 in G
False
sage: G.shortest_path(2,2)
[2]
sage: G.shortest_path_length(2,2)
0
```

I don't know why it has not been reported before.

Can you add necessary tests to check that u and v are in the graph and raise an error if it is not the case.

Thanks.



---

archive/issue_comments_065822.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2017-06-06T07:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65822",
    "user": "@dcoudert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_065823.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-06T18:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65823",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065824.json:
```json
{
    "body": "In the diff, I see the following modifications that must be cancelled.\n\n```\n-.. csv-table::\n+ v\\sv-table::\n```\n\n\n```\n-    :meth:`~GenericGraph.add_vertex` | Create an isolated vertex.\n+*-* :meth:`~GenericGraph.add_vertex` | Create an isolated vertex.\n```\n\n\nIn case, you can \"quickly\" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.\n\n\nConcerning the tests, I would prefer something like that (and \n\n```\nif not self.has_vertex(u):\n    raise ValueError(\"vertex '{}' is not in the (di)graph\".format(u))\nif not self.has_vertex(v):\n    raise ValueError(\"vertex '{}' is not in the (di)graph\".format(v))\n```\n",
    "created_at": "2017-06-06T21:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65824",
    "user": "@dcoudert"
}
```

In the diff, I see the following modifications that must be cancelled.

```
-.. csv-table::
+ v\sv-table::
```


```
-    :meth:`~GenericGraph.add_vertex` | Create an isolated vertex.
+*-* :meth:`~GenericGraph.add_vertex` | Create an isolated vertex.
```


In case, you can "quickly" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.


Concerning the tests, I would prefer something like that (and 

```
if not self.has_vertex(u):
    raise ValueError("vertex '{}' is not in the (di)graph".format(u))
if not self.has_vertex(v):
    raise ValueError("vertex '{}' is not in the (di)graph".format(v))
```




---

archive/issue_comments_065825.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2017-06-07T02:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65825",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_065826.json:
```json
{
    "body": "Sorry for the modifications. I have deleted the previous commit.\n\n> \n> In case, you can \"quickly\" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.\n> \nI have built the documentation. Is there anything specific I need to do with it?",
    "created_at": "2017-06-07T02:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65826",
    "user": "@lokeshj1703"
}
```

Sorry for the modifications. I have deleted the previous commit.

> 
> In case, you can "quickly" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.
> 
I have built the documentation. Is there anything specific I need to do with it?



---

archive/issue_comments_065827.json:
```json
{
    "body": "Replying to [comment:46 jlokesh]:\n> Sorry for the modifications. I have deleted the previous commit.\n\nok, but you have not put the tests ;)\n\n> > In case, you can \"quickly\" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.\n> > \n> I have built the documentation. Is there anything specific I need to do with it?\n\nFirst it tells you that it builds correctly. Then, since you have a local version of the full html documentation, you can check that the pages generated for the files you have modified display properly / look nice. If it is the case, you have nothing else to do.",
    "created_at": "2017-06-07T07:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65827",
    "user": "@dcoudert"
}
```

Replying to [comment:46 jlokesh]:
> Sorry for the modifications. I have deleted the previous commit.

ok, but you have not put the tests ;)

> > In case, you can "quickly" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.
> > 
> I have built the documentation. Is there anything specific I need to do with it?

First it tells you that it builds correctly. Then, since you have a local version of the full html documentation, you can check that the pages generated for the files you have modified display properly / look nice. If it is the case, you have nothing else to do.



---

archive/issue_comments_065828.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-06-07T16:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65828",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_065829.json:
```json
{
    "body": "I have committed the tests. I hope there are no errors this time :)",
    "created_at": "2017-06-07T16:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65829",
    "user": "@lokeshj1703"
}
```

I have committed the tests. I hope there are no errors this time :)



---

archive/issue_comments_065830.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2017-06-07T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65830",
    "user": "@dcoudert"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_065831.json:
```json
{
    "body": "For me it is now good to go (passes all tests, docbuild). Let's hope we are done this time and congratulation for your first contribution to Sagemath.",
    "created_at": "2017-06-07T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65831",
    "user": "@dcoudert"
}
```

For me it is now good to go (passes all tests, docbuild). Let's hope we are done this time and congratulation for your first contribution to Sagemath.



---

archive/issue_comments_065832.json:
```json
{
    "body": "Thanks.",
    "created_at": "2017-06-07T17:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65832",
    "user": "@lokeshj1703"
}
```

Thanks.



---

archive/issue_comments_065833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-06-09T18:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7675#issuecomment-65833",
    "user": "@vbraun"
}
```

Resolution: fixed
