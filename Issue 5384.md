# Issue 5384: pynac symbolics gives very wrong simplifications for simple expressions

Issue created by migration from https://trac.sagemath.org/ticket/5384

Original creator: cwitty

Original creation time: 2009-02-26 05:19:16

In sage 3.4.alpha0 (and sage 3.3):

```
sage: var('y', ns=1)
y
sage: (y-1)*(y-2)
(y - 2)^2
```



---

Comment by cwitty created at 2009-02-26 05:19:54

Set assignee to burcin.


---

Comment by burcin created at 2009-02-26 13:06:31

doctests for the fix


---

Attachment

There is a new pynac package which includes the fix for this here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.3.spkg

To make the review easier, here is the patch for pynac


```
diff --git a/ginac/expairseq.cpp b/ginac/expairseq.cpp
--- a/ginac/expairseq.cpp
+++ b/ginac/expairseq.cpp
@@ -510,13 +510,6 @@
 	if (seq.size() != o.seq.size())
 		return (seq.size()<o.seq.size()) ? -1 : 1;
 
-	// compare overall_coeff
-	/*
-	cmpval = overall_coeff.compare(o.overall_coeff);
-	if (cmpval!=0)
-		return cmpval;
-		*/
-	
 #if EXPAIRSEQ_USE_HASHTAB
 	GINAC_ASSERT(hashtabsize==o.hashtabsize);
 	if (hashtabsize==0) {
@@ -534,6 +527,11 @@
 		GINAC_ASSERT(cit1==last1);
 		GINAC_ASSERT(cit2==last2);
 	
+		// compare overall_coeff
+		cmpval = overall_coeff.compare(o.overall_coeff);
+		if (cmpval!=0)
+			return cmpval;
+	
 		return 0;
 #if EXPAIRSEQ_USE_HASHTAB
 	}
```


attachment:trac_5384-pynac_compare_add.patch adds the example in the description as a doctest.


---

Comment by burcin created at 2009-02-26 13:25:27

Changing status from new to assigned.


---

Comment by mvngu created at 2009-02-28 03:15:18

REFEREE REPORT



The patch *trac_5384-pynac_compare_add.patch* applied OK against 3.4.alpha0. I upgraded to the new Pynac spkg with this command

```
sage -i -f /path/to/pynac-0.1.3.spkg
```

and ran all doctests with

```
sage -t -long -optional /path/to/devel/sage-main/sage/symbolic/
```

and received these results:

```
sage -t -long -optional "devel/sage-main/sage/symbolic/pynac.pyx"
         [2.8 s]
sage -t -long -optional "devel/sage-main/sage/symbolic/expression.pyx"
         [9.0 s]
sage -t -long -optional "devel/sage-main/sage/symbolic/constants.pyx"
         [0.1 s]
sage -t -long -optional "devel/sage-main/sage/symbolic/ring.pyx"
         [2.1 s]
sage -t -long -optional "devel/sage-main/sage/symbolic/function.pyx"
         [3.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 17.0 seconds
```

The above patch adds this new doctest:

```
# check if comparison of constant terms in pynac add objects work 
sage: (y-1)*(y-2) 
(y - 2)*(y - 1)
```

to `sage.symbolic.expression.pyx`, but on #5384 I see this reported bug:

```
sage: var('y', ns=1)
y
sage: (y-1)*(y-2)
(y - 2)^2
```

Just to make sure, again I tested the last 2 lines after having applied the patch and upgraded to the new spkg:

```
sage: var("y", ns=1)
y
sage: (y - 1) * (y - 2)
(y - 2)*(y - 1)
```

Looks to me that the patch and the new spkg fixes the reported problem. So positive review on my part.


---

Comment by mvngu created at 2009-02-28 03:31:42

I should add that I'm not familiar with Pynac's internals, so someone else should definitely take a look at the diff against the previous version of the Pynac spkg. Because of this, I'm reverting to giving this ticket a partial review, instead of my previous positive review.


---

Comment by mabshoff created at 2009-02-28 03:34:41

There is no partial reviews, so change it back to "needs review" so it is picked up by the right reports again.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 06:30:13

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 06:30:31

Resolution: fixed


---

Comment by mabshoff created at 2009-03-01 06:30:31

Merged in Sage 3.4.rc0.

Cheers,

Michael
