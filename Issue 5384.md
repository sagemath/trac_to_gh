# Issue 5384: pynac symbolics gives very wrong simplifications for simple expressions

archive/issues_005384.json:
```json
{
    "body": "In sage 3.4.alpha0 (and sage 3.3):\n\n```\nsage: var('y', ns=1)\ny\nsage: (y-1)*(y-2)\n(y - 2)^2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5384\n\n",
    "created_at": "2009-02-26T05:19:16Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "pynac symbolics gives very wrong simplifications for simple expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5384",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
In sage 3.4.alpha0 (and sage 3.3):

```
sage: var('y', ns=1)
y
sage: (y-1)*(y-2)
(y - 2)^2
```


Issue created by migration from https://trac.sagemath.org/ticket/5384





---

archive/issue_comments_041386.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-02-26T05:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41386",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Set assignee to @burcin.



---

archive/issue_comments_041387.json:
```json
{
    "body": "doctests for the fix",
    "created_at": "2009-02-26T13:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41387",
    "user": "https://github.com/burcin"
}
```

doctests for the fix



---

archive/issue_comments_041388.json:
```json
{
    "body": "Attachment [trac_5384-pynac_compare_add.patch](tarball://root/attachments/some-uuid/ticket5384/trac_5384-pynac_compare_add.patch) by @burcin created at 2009-02-26 13:25:27\n\nThere is a new pynac package which includes the fix for this here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.3.spkg\n\nTo make the review easier, here is the patch for pynac\n\n\n```\ndiff --git a/ginac/expairseq.cpp b/ginac/expairseq.cpp\n--- a/ginac/expairseq.cpp\n+++ b/ginac/expairseq.cpp\n@@ -510,13 +510,6 @@\n \tif (seq.size() != o.seq.size())\n \t\treturn (seq.size()<o.seq.size()) ? -1 : 1;\n \n-\t// compare overall_coeff\n-\t/*\n-\tcmpval = overall_coeff.compare(o.overall_coeff);\n-\tif (cmpval!=0)\n-\t\treturn cmpval;\n-\t\t*/\n-\t\n #if EXPAIRSEQ_USE_HASHTAB\n \tGINAC_ASSERT(hashtabsize==o.hashtabsize);\n \tif (hashtabsize==0) {\n@@ -534,6 +527,11 @@\n \t\tGINAC_ASSERT(cit1==last1);\n \t\tGINAC_ASSERT(cit2==last2);\n \t\n+\t\t// compare overall_coeff\n+\t\tcmpval = overall_coeff.compare(o.overall_coeff);\n+\t\tif (cmpval!=0)\n+\t\t\treturn cmpval;\n+\t\n \t\treturn 0;\n #if EXPAIRSEQ_USE_HASHTAB\n \t}\n```\n\n\nattachment:trac_5384-pynac_compare_add.patch adds the example in the description as a doctest.",
    "created_at": "2009-02-26T13:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41388",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_5384-pynac_compare_add.patch](tarball://root/attachments/some-uuid/ticket5384/trac_5384-pynac_compare_add.patch) by @burcin created at 2009-02-26 13:25:27

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

archive/issue_comments_041389.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-26T13:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41389",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041390.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **trac_5384-pynac_compare_add.patch** applied OK against 3.4.alpha0. I upgraded to the new Pynac spkg with this command\n\n```\nsage -i -f /path/to/pynac-0.1.3.spkg\n```\n\nand ran all doctests with\n\n```\nsage -t -long -optional /path/to/devel/sage-main/sage/symbolic/\n```\n\nand received these results:\n\n```\nsage -t -long -optional \"devel/sage-main/sage/symbolic/pynac.pyx\"\n         [2.8 s]\nsage -t -long -optional \"devel/sage-main/sage/symbolic/expression.pyx\"\n         [9.0 s]\nsage -t -long -optional \"devel/sage-main/sage/symbolic/constants.pyx\"\n         [0.1 s]\nsage -t -long -optional \"devel/sage-main/sage/symbolic/ring.pyx\"\n         [2.1 s]\nsage -t -long -optional \"devel/sage-main/sage/symbolic/function.pyx\"\n         [3.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 17.0 seconds\n```\n\nThe above patch adds this new doctest:\n\n```\n# check if comparison of constant terms in pynac add objects work \nsage: (y-1)*(y-2) \n(y - 2)*(y - 1)\n```\n\nto `sage.symbolic.expression.pyx`, but on #5384 I see this reported bug:\n\n```\nsage: var('y', ns=1)\ny\nsage: (y-1)*(y-2)\n(y - 2)^2\n```\n\nJust to make sure, again I tested the last 2 lines after having applied the patch and upgraded to the new spkg:\n\n```\nsage: var(\"y\", ns=1)\ny\nsage: (y - 1) * (y - 2)\n(y - 2)*(y - 1)\n```\n\nLooks to me that the patch and the new spkg fixes the reported problem. So positive review on my part.",
    "created_at": "2009-02-28T03:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



The patch **trac_5384-pynac_compare_add.patch** applied OK against 3.4.alpha0. I upgraded to the new Pynac spkg with this command

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

archive/issue_comments_041391.json:
```json
{
    "body": "I should add that I'm not familiar with Pynac's internals, so someone else should definitely take a look at the diff against the previous version of the Pynac spkg. Because of this, I'm reverting to giving this ticket a partial review, instead of my previous positive review.",
    "created_at": "2009-02-28T03:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I should add that I'm not familiar with Pynac's internals, so someone else should definitely take a look at the diff against the previous version of the Pynac spkg. Because of this, I'm reverting to giving this ticket a partial review, instead of my previous positive review.



---

archive/issue_comments_041392.json:
```json
{
    "body": "There is no partial reviews, so change it back to \"needs review\" so it is picked up by the right reports again.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T03:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41392",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is no partial reviews, so change it back to "needs review" so it is picked up by the right reports again.

Cheers,

Michael



---

archive/issue_comments_041393.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T06:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_041394.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-01T06:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041395.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T06:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5384#issuecomment-41395",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_events_012551.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-01T06:30:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5384",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5384#event-12551"
}
```
