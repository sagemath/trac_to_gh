# Issue 5487: Content function for tableaux

Issue created by migration from Trac.

Original creator: andrew.mathas

Original creation time: 2009-03-11 14:12:29

Assignee: mhansen

CC:  sage-combinat

Keywords: tableaux content

Simple patch adding a content function for tableaux to tableau.py.

[Mostly just a test to see if I can push a patch to the combinat server.]

---------

```
diff -r c6382e76a5e5 sage/combinat/tableau.py
--- a/sage/combinat/tableau.py  Thu Mar 12 01:07:21 2009 +1100
+++ b/sage/combinat/tableau.py  Thu Mar 12 01:07:52 2009 +1100
`@``@` -480,6 +480,21 `@``@`
             s += [ (i,j) for j in range(len(self[i])) ]
         return s
 
+    def content(self, k):
+        """
+        Returns the content of <k> in <self>. That is, if <k> appears in
+        row r and column c of the tableau <self> then we return c-r.
+
+        EXAMPLES:
+            sage: Tableau([[1,2],[3,4]]).content(3)
+            -1
+
+        """
+        for r in range(len(self)):
+          for c in range(len(self[r])):
+            if self[r][c]==k: return c-r
+        return False
+
     def k_weight(self, k):
         """
         Returns the k-weight of self.
```



---

Comment by saliola created at 2009-03-12 12:35:08

A few comments:

0. Patches should be included as attachments.

1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?

```
sage: Tableau([[3,3],[3,3]])
[[3, 3], [3, 3]]
```


2. In case k does not appear in the tableau, perhaps it is better to raise an error?

3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section.


---

Comment by hivert created at 2009-03-12 23:55:24

Replying to [comment:1 saliola]:

> 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?
> {{{
> sage: Tableau([[3,3],[3,3]])
> [[3, 3], [3, 3]]
> }}}

This is not exactly a tableau ! :-) I don't know if it's standard but there is a notion of content associated to semi-standard tableau. 

> 2. In case k does not appear in the tableau, perhaps it is better to raise an error?
> 
> 3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section. 

4. I think parameters should be written ```n``` (raw sage code) instead of ``n`` (latex code) or `<n>` (no particular meaning in rest) see http://wiki.sagemath.org/combinat/HelpOnTheDoc


---

Comment by andrew.mathas created at 2009-03-13 06:58:01

Replying to [comment:2 hivert]:
> Replying to [comment:1 saliola]:
> 
> > 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?

When pushing this patch I described it as a content function on standard tableau and then added it to the Tableau class...I'll move it into the StandardTableau class and then all will be well.

The obvious "generalization" of the definition to semistandard tableau is used in the literature but writing the corresponding function is slightly cumbersome because in the classical case you add up the contents of all of nodes labelled k whereas for the q-analogue you add up the q-contents. Perhaps the nicest solution is to define

```
def content(self, k, q=1):
...
```

I have never used contents for tableaux which are not (semi)standard.

> > 2. In case k does not appear in the tableau, perhaps it is better to raise an error?

OK
 
> > 3. Whatever is decided for 2, it should be documented. You can do this with an OUTPUT section. 
> 
> 4. I think parameters should be written ```n``` (raw sage code) instead of ``n`` (latex code) or `<n>` (no particular meaning in rest) see http://wiki.sagemath.org/combinat/HelpOnTheDoc

Thanks.

One last question: is there an easy way to "update" the patch and push it back to the server? Or do I have to somehow delete this patch and then reapply?

Cheers,
Andrew


---

Comment by andrew.mathas created at 2009-03-13 06:58:01

Changing assignee from mhansen to andrew.mathas.


---

Comment by saliola created at 2009-03-13 07:21:52

Replying to [comment:3 andrew.mathas]:
> Replying to [comment:2 hivert]:
> > Replying to [comment:1 saliola]:
> > 
> > > 1. content is only well-defined if k appears exactly once in the tableau. How should it work for the following tableau?
> 
> When pushing this patch I described it as a content function on standard tableau and then added it to the Tableau class...I'll move it into the StandardTableau class and then all will be well.

One slight problem: there doesn't seem to be a StandardTableau or SemistandardTableau class, just a Tableau class. So you'll have to create it, which is not a big deal.

> One last question: is there an easy way to "update" the patch and push it back to the server? Or do I have to somehow delete this patch and then reapply?

In you sage-combinat branch, you can type `hg qpop tableau-content-5487-AM.patch`, which will unapply all the patches up until you get to your patch. (Or you might have to qpush instead of qpop above depending on where you are in the stack.) Then you do your modifications. To save your modifications into the top patch (in this case, tableau-content-5487-AM.patch), you do `hg qrefresh`. To see which patch is at the top of your stack, use the command `hg qtop`. Once you are done with your modifications, you proceed as normal. That is: change into the patches directory, commit, then push.


---

Comment by andrew.mathas created at 2009-04-10 22:06:46

I have moved the function into the StandardTableaux_n class and fixed the doc string problems.


---

Comment by hivert created at 2009-04-13 10:13:42

Dear Andrew,

Sorry for bothering you with this first simple patch but before giving a positive review I'd rather see the following first problem fixed. I leave these to you because I understand that you want test the patch workflow. If you want me to fix these please ask. 

1. I agree with Franco's first message: I'd rather raise an error than return False silently. Those `False` or `None` tends to crawl into the programs and to eventually trigger an error at the wrong place. You can always catch the exception if you want. I think `ValueError` is the correct exception (see the similar behavior for list below).

2. I case you don't know, in python, when you have a list `l` the call `l.index(k)` either returns the first position of `k` if it is in the list or raise a

```
ValueError: list.index(x): x not in list
```

maybe it's worth using it ? 

cheers,

Florent


---

Attachment

Dear Florent,

I have changed the function to use index() and added an exception. More importantly, I have also created a StandardTableau_class class and a StandardTableau() function for holding and creating standard tableau...previously I was confused and thought that the StandardTableaux class  did this. I discovered my error when I tested the new version (which I confess I had previously just moved into StandardTableaux and not tested...I promise to test properly in future!).

Hopefully the new patch also removes my unintended change to kschur.py.

Regards,
Andrew


---

Comment by hivert created at 2009-04-13 21:47:37

Review patch


---

Attachment

I Added a review patch which:

- add some more doctests

- correct the ReST syntax for doctests

- Specifies which exception is caught.

I'm giving the positive review though someone should probably reread my trivial review patch... 

Michael: please tell me if I should not give the review and ask for a formal review of my patch.   

Cheers,

Florent


---

Comment by mabshoff created at 2009-04-13 22:04:48

Replying to [comment:9 hivert]:
> I Added a review patch which:

<SNIP>

> I'm giving the positive review though someone should probably reread my trivial review patch... 

Yep. 

> Michael: please tell me if I should not give the review and ask for a formal review of my patch.   

I would consider this review patch non-trivial enough to have someone else take a look since it adds more than a doctest. I looked at the patch and it looks good to me, but I will run doctests before mergin.

Cheers,

Michael

> Cheers,
> 
> Florent
>


---

Comment by nthiery created at 2009-04-13 23:24:14

Positive review on Andrew and Florent's patches.


---

Comment by mabshoff created at 2009-04-15 00:10:10

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 00:10:10

Resolution: fixed


---

Attachment

This is the same as the first patch, but instead of a diff it has been commited in Andrew's name


---

Comment by mabshoff created at 2009-04-15 00:16:59

Andrew,

I attached trac_5487_tableau-content-5487-AM.patch which is your patch checked in in your name. You attached a diff, but when you used hg queues you to export the patch after committing so that you get credited properly. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 02:55:50

Oops, reassign to 3.4.1 since it was merged in that timeframe.

Cheers,

Michael
