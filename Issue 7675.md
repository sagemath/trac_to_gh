# Issue 7675: shortest_path in c_graph should have an optional flag distance=False to return only the distance

Issue created by migration from https://trac.sagemath.org/ticket/7675

Original creator: ncohen

Original creation time: 2009-12-13 11:05:00

Assignee: rlm

CC:  dimpase dcoudert

This modification would avoid the building of the shortest path, which is interesting for a function so often used !

Nathann


---

Comment by ncohen created at 2010-06-06 11:00:47

Changing status from new to needs_work.


---

Comment by jlokesh created at 2017-05-17 18:06:39

Hi

I am Lokesh. I wanted to work on this ticket. I have made the changes in c_graph.pyx and generic_graph.py . I had an issue that changes I have made in generic_graph.py do not appear in the git status output. Further the shortest_paths function in generic_graph.py uses functions from boost_graph.pyx . Am I supposed to make the changes in boost_graph.pyx functions as well because internally they call boost library functions. For networkx I replaced the function call to an appropriate one which returns the distance. Should I try to do something similar here as well?


---

Comment by dcoudert created at 2017-05-18 07:01:29

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

Comment by jlokesh created at 2017-05-20 09:29:59

I have added the distance_flag parameter to the shortest_path function of generic_graph.py and all the functions which are called from this function. I couldn't add it to boost_graph.pyx function as it returns both distance and path dictionaries in a list. Any changes to these functions lead to failure of doctests as they are used by other functions.
If distance_flag is True and u,v are not connected then the shortest_path function returns None or an exception based on the algorithm used. Networkx returns an exception. Should I also raise an exception for such a case?
----
New commits:


---

Comment by dcoudert created at 2017-05-20 10:37:51

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

Comment by dimpase created at 2017-05-20 10:53:25

I just wanted to point out that there are cases where a one-line commit message is not appropriate, and you would add a multi-line explanation there (without using `-m` flag, 
but letting git pop-up an editor to write the commit message in).

Another handy thing is `git commit --amend` to change the last commit (can be only the message, or also actual changes).


---

Comment by jlokesh created at 2017-05-20 12:41:39

Hi

Thanks for the review. I have incorporated the changes in c_graph.pyx. For generic_graph.py I had made the changes for networkx function calls for example I had replaced networkx.single_source_dijkstra_path(G, u) with networkx.single_source_dijkstra_path_length(G, u). Similarly for boost function call I had done away with the code which builds the path in shortest_paths. If you want these changes as well I can just call shortest_path in shortest_path_length with distance_flag as True or I can include all these changes of networkx in shortest_path_length and shortest_path_lengths.


---

Comment by dcoudert created at 2017-05-20 15:19:21

I'm not sure to understand what you have changed or not.

For sure, you should not modify the `shortest_path` method in `generic_graph`, but change the `shortest_path_length` method.


---

Comment by git created at 2017-05-21 10:04:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jlokesh created at 2017-05-21 10:10:04

Hi

I have uploaded changes for shortest_path_length and shortest_path_lengths. Sorry, I couldn't figure out the command for changing the remote branch name.


---

Comment by dimpase created at 2017-05-21 11:09:21

Replying to [comment:15 jlokesh]:
> Hi
> 
> I have uploaded changes for shortest_path_length and shortest_path_lengths. Sorry, I couldn't figure out the command for changing the remote branch name.

read on remote branches in git.
e.g you can remove a remote branch via `git push` with --delete option.


---

Comment by dcoudert created at 2017-05-21 15:25:12

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

Comment by dimpase created at 2017-05-22 09:01:01

I think it's actually a bug introduced in the branch of this ticket that makes `Dijkstra_Bid` return `float` (there is `cdef float...` there). While I cannot find explicit documentation on the type of weights allowed, I cannot imagine `float` being the right type. This type depends upon the type of weight of a particular graph. 
By common sense, one needs weights to satisfy certain basic properties: one should be able to add them, and to compare them for `<`, and there should be `0` in this type, but that's all; e.g. certainly `float` is a wrong type to use if weights are, say, rational numbers.

It would be good to dig up whether the code does any kind of checking on weights, and document this. If there are no checks done, i.e. you can get weird results, or perhaps even crashes, by using weights which are, say, integers mod 3, this ought to be documented as well.


---

Comment by dimpase created at 2017-05-22 09:05:44

One certain thing to check in doctests is whether cycles of negative length in the graph lead to a crash---if an implementation does not check whether it creates loops in "shortest" paths it is building, then it would not terminate (normally).


---

Comment by dcoudert created at 2017-05-22 10:51:47

Hello,

* The goal of this ticket is to speed up some calls when asking for the distance and not the path. We do not change the behavior of the algorithms. That is, if the algorithm was not able to detect negative cycles before, it will be the same after. If it was able to detect negative cycles, then it will continue to do so. If a correction of a shortest path algorithm has to be performed, it must be done in another ticket.
* Concerning the use of `float` in `bidirectional_dijkstra`. I agree it is certainly not the good type here. May be we should simply remove the type for variables `distance` and `f_tmp` and let Python/Cython decide ? Or may be there is a more suitable type to use here ? Who should we ask ?
* Concerning the possibility edge labels are integer mod 3. Yes, one can certainly do it and as far as I know, no graph algorithm is protected against such weird use. If one wants to protect graphs against such weird use, a specific ticket should be opened, for instance to improve method `_check_weight_function` or to add an extra method like `_check_edge_labels`


---

Comment by jlokesh created at 2017-05-31 04:32:43

Hi

Are the documentation changes the only changes required for this ticket currently?


---

Comment by dcoudert created at 2017-05-31 10:24:10

can you try to fix the tyep float issue discussed above ?


---

Comment by dimpase created at 2017-05-31 14:54:30

It should suffice to remove the declaration of that `float` variable.
Then its type will be handled dynamically by Python.


---

Comment by jlokesh created at 2017-05-31 14:56:13

I have removed the declarations and it is working correctly now. Its also able to handle rational numbers as weights.


---

Comment by git created at 2017-06-01 17:52:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dimpase created at 2017-06-02 00:01:06

Changing status from needs_work to positive_review.


---

Comment by dimpase created at 2017-06-02 00:01:06

OK, this looks good. Please do not forget to fill in "Authors:" field next time (I copied the name from your email, hopefully it's the way prefer it written).


---

Comment by tscrim created at 2017-06-03 06:09:13

Changing status from positive_review to needs_work.


---

Comment by tscrim created at 2017-06-03 06:09:13

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

Comment by dcoudert created at 2017-06-03 11:33:47

I agree that we can safely get ride of the `distances_int` dict using an extra `if`. It will be cleaner.

For the error message, the convention to follow is `raise ValueError('unknown algorithm "{}"'.format(algorithm))`, so without capital letter for the first word and no `.` at the end.

So you also have to change `raise ValueError("The 'BFS_Bid' algorithm does not work on weighted graphs."` to `raise ValueError("the 'BFS_Bid' algorithm does not work on weighted graphs")`


---

Comment by git created at 2017-06-03 15:18:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2017-06-03 22:19:11

One last thing (well, in 2 places):

```diff
-distance_flag = False):
+distance_flag=False):
```



---

Comment by jlokesh created at 2017-06-04 07:03:17

Hi



```
raise ValueError("Algorithm " + algorithm + " not yet " +
                             "implemented. Please, contribute!")
```

is used by other algorithms like triangles_count, shortest_paths and shortest_path_all_pairs. Should I make the corresponding change in those algorithms as well?


---

Comment by tscrim created at 2017-06-04 08:18:23

While we should be wary of "ticket creep", I think in this case it isn't so bad to change it across the board in graphs here for simplicity.


---

Comment by dcoudert created at 2017-06-04 08:28:02

It should be ok to do so, but be aware that some tickets like #23124 are currently modifying many files in `graphs`.

In `shortest_paths`, please change 
`if self.num_verts()==1 and self.vertices()[0]==u` to
`if self.order() == 1 and self.has_vertex(u):`


---

Comment by git created at 2017-06-05 17:45:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-06-05 17:47:15

don't forget to update the tests with the new error message.


---

Comment by git created at 2017-06-05 18:54:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jlokesh created at 2017-06-05 18:56:55

I forgot to update the tests for the changes made to the error message. The second commit makes those changes.


---

Comment by tscrim created at 2017-06-06 00:06:26

Changing status from needs_work to positive_review.


---

Comment by tscrim created at 2017-06-06 00:06:26

LGTM.


---

Comment by dcoudert created at 2017-06-06 07:35:50

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

Comment by dcoudert created at 2017-06-06 07:35:50

Changing status from positive_review to needs_work.


---

Comment by git created at 2017-06-06 18:02:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2017-06-06 21:22:20

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

Comment by git created at 2017-06-07 02:03:48

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jlokesh created at 2017-06-07 02:50:45

Sorry for the modifications. I have deleted the previous commit.

> 
> In case, you can "quickly" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.
> 
I have built the documentation. Is there anything specific I need to do with it?


---

Comment by dcoudert created at 2017-06-07 07:11:08

Replying to [comment:46 jlokesh]:
> Sorry for the modifications. I have deleted the previous commit.

ok, but you have not put the tests ;)

> > In case, you can "quickly" rebuild the html documentation of the graph module using `./sage -docbuild reference/graphs html`.
> > 
> I have built the documentation. Is there anything specific I need to do with it?

First it tells you that it builds correctly. Then, since you have a local version of the full html documentation, you can check that the pages generated for the files you have modified display properly / look nice. If it is the case, you have nothing else to do.


---

Comment by git created at 2017-06-07 16:14:06

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jlokesh created at 2017-06-07 16:16:45

I have committed the tests. I hope there are no errors this time :)


---

Comment by dcoudert created at 2017-06-07 16:27:04

Changing status from needs_work to positive_review.


---

Comment by dcoudert created at 2017-06-07 16:27:04

For me it is now good to go (passes all tests, docbuild). Let's hope we are done this time and congratulation for your first contribution to Sagemath.


---

Comment by jlokesh created at 2017-06-07 17:13:52

Thanks.


---

Comment by vbraun created at 2017-06-09 18:38:03

Resolution: fixed
