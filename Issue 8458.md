# Issue 8458: iterator for graphs() doesn't return independent graphs

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-03-06 19:18:00

Assignee: rlm

CC:  brunellus

From [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/4f822bba45432f7b):

```
So, what you are saying is that the iterator for graphs() does not
return independent graphs which can be changed without affecting the
others.
That does explain what I am seeing and is consistent with Pat
LeSmith's suggested workaround.

Should this property of the iterators to the generated graphs be
documented?

So, I think I will try making a copy of just the graphs I want to
change or use the list() trick. 
```



---

Comment by rlm created at 2010-03-06 19:27:39

This is an unintended consequence of the fact that when the `graphs(n)` iterator yields a graph, it does not first make a copy. The method of generating graphs is to add on to previously generated graphs in a well-chosen way, and I did not think to make a copy of the graph before having the iterator yield it.

This shouldn't just be documented, but in fact I think this should be an option to `graphs(n)`. If someone will not modify the graphs in the loop, they can get the speed advantage of not making copies, and someone else who wants to modify them can have the iterator make copies on the fly.


---

Comment by jason created at 2010-03-09 03:36:41

I agree with rlm.  I think the default should be to return a copy of the graph, with an optional argument to return the actual graph.


---

Comment by brunellus created at 2012-01-03 23:10:53

Changing status from new to needs_review.


---

Attachment

I corrected the main generator. There are several specialized (e.g. tree generator) but I don't think the same problem arises in any of them. Do you agree?


---

Comment by ncohen created at 2012-01-29 18:15:22

Changing status from needs_review to needs_info.


---

Comment by ncohen created at 2012-01-29 18:15:22

Helloooooo !!!

This is a good patch, but I do not think the documentation is very clear. What would you think of changing the new argument's name to "return_copies" or "graph_copy" ? To be honest I took me 2 minutes to understand that this message's title did not mean "The independent graph is not returned by graphs(n)" `:-p`

Either way, with a name like "independent" it is not very clear that there may be performances issues hidden in this argument.

Here's what I would write. Of course, it's just my advice, so take or leave whatever you want :


```
- ``copy_graphs`` (boolean) -- If set to ``True`` (default) this method makes copies of the graphs before returning them. If set to ``False`` the method returns the graph it is working on. The second alternative is faster, but modifying any of the graph instances returned by the method may break the function's behaviour, as it is using these graphs to compute the next ones : only use ``copy_graph = False`` when you stick to *reading* the graphs returned.
```


Please tell me what you think `:-)`

Nathann


---

Comment by ncohen created at 2012-01-29 18:16:12

Arg.... It's all written on one line. Stupid me. Here it is :

```
- ``copy_graphs`` (boolean) -- If set to ``True`` (default)
   this method makes copies of the graphs before returning 
   them. If set to ``False`` the method returns the graph it
   is working on. The second alternative is faster, but modifying
   any of the graph instances returned by the method may break
   the function's behaviour, as it is using these graphs to 
   compute the next ones : only use ``copy_graph = False`` when
   you stick to *reading* the graphs returned.
```



---

Comment by jason created at 2012-01-30 12:38:49

Can I suggest `copy=True`, which is shorter and just as clear in the context?


---

Comment by ncohen created at 2012-01-30 12:39:36

> Can I suggest `copy=True`, which is shorter and just as clear in the context?

`>_<`

Of course... Much more natural `:-D`

Thanks !!

Nathann


---

Attachment

If you think that "copy" is better, I don't mind. I thought that a consumer of the library doesn't care about what is the way we create the graphs (that we copy them), so the relevant property of the output is rather independence. The proposed description is also good.


---

Comment by brunellus created at 2012-01-31 12:34:03

Changing status from needs_info to needs_review.


---

Comment by ncohen created at 2012-01-31 14:53:54

Hellooooooo !!!

Well, with a keyword like "independent" the user needs to read the documentation to understand what it precisely means. And with "copy" he also knows that there is some complexity question hidden in there `:-)`


---

Comment by ncohen created at 2012-01-31 17:41:58

(for me the patch is ok, but it does not apply on 5.0-beta1. I just reinstalled it, so it seems genuine `:-)`)

Nathann


---

Comment by ncohen created at 2012-01-31 17:41:58

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2012-01-31 17:44:34

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2012-01-31 17:44:34

Well, I do not like to set tickets back to "needs work" in such cases... Here is the same patch rebased on beta1. If it's fine with you too, you can set the ticket to positive_review `:-)`

Nathann


---

Attachment


---

Comment by brunellus created at 2012-02-03 13:18:04

Changing status from needs_review to positive_review.


---

Comment by brunellus created at 2012-02-03 13:18:04

Thank you. :-)


---

Comment by jdemeyer created at 2012-02-06 15:58:40

Lukáš: in the future try to remember to add yourself as Author.


---

Comment by jdemeyer created at 2012-02-06 21:22:29

Resolution: fixed
