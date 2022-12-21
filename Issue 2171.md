# Issue 2171: [with patch; needs review] followup to #2169 -- (magma/sage interface) some further optimizations and fixes

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-15 08:11:04

Assignee: was

Apply the patches from #2169, then apply both these patches.  To test do

```
sage -t --optional SAGE_ROOT/devel/sage/sage/interfaces/magma.py
```


Conversion of Magma matrices over ZZ back to Sage should also be much faster now.


---

Attachment


---

Attachment

Apply all the attached files -- the sage- ones to hg_sage and the extcode ones to hg_extcode.


---

Comment by mhansen created at 2008-03-05 00:27:58

I get a reject with http://sagetrac.org/sage_trac/attachment/ticket/2171/sage-trac2171.patch on rc1.  It looks like it is depending on a patch that isn't there.  This is the failure:


```
--- expect.py
+++ expect.py
`@``@` -860,10 +860,15 `@``@` If this all works, you can then make cal
         return self.eval(var)
 
     def get_using_file(self, var):
-        """
+        r"""
         Return the string representation of the variable var in self
         using a file.  Use this if var has a huge string
         representation.  It'll be way faster.
+
+        WARNING: In fact unless a special derived class implements
+        this, it will \emph{not} be any faster.  This is the case for
+        this class if you're reading it through introspection and
+        seeing this.
         """
         return self.get(var)
```


and this is expect.py in rc1:


```
    def get_using_file(self, var):
        return self.get(var)
```



---

Comment by craigcitro created at 2008-05-10 11:16:03

The patch that this code depends on is attached to trac #2120. I guess this will have to wait until that patch is ready to go? Or should we pull over that part of the patch to this ticket so we can get it merged? William, what's the status of the Maple ticket?


---

Comment by craigcitro created at 2008-06-15 21:37:32

Changing keywords from "" to "editor_craigcitro".


---

Comment by mabshoff created at 2008-08-25 05:04:07

Craig, 

can you review this? It has been potentially bitrotting for a long, long time :)

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by was created at 2008-10-24 03:28:44

I rebased these patches against 3.2.alpha0 and got rid of the dependence on #2120.  This should be easy to apply and go into sage-3.2.


---

Comment by mabshoff created at 2008-10-27 02:51:32

In sage-trac2171-part1.patch there is still a change to sage/interfaces/maple.py. I will delete that hunk and test the patch. Other than that I expect a positive review assuming the doctests pass.

Cheers,

Michael


---

Comment by mvngu created at 2008-10-27 03:24:01

For the patch *extcode-trac2171-part2.patch*, here's a possible documentation fix:

```
-{Conver the ring of integers to Sage.}
+{Convert the ring of integers to Sage.}
```



---

Comment by mabshoff created at 2008-10-27 04:19:35

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 04:20:06

Resolution: fixed


---

Comment by mabshoff created at 2008-10-27 04:20:06

Merged sage-trac2171-part1.patch and sage-trac2171-part2.patch in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-30 23:44:07

Oops, I didn't merge extcode-trac2171.patch and extcode-trac2171-part2.patch. Those two patches have been merged in Sage 3.2.alpha2.

Cheers,

Michael
