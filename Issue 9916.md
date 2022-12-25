# Issue 9916: ECL has too few arguments and two many on file dpp.c

archive/issues_009916.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jhpalmieri\n\nKeywords: ecl\n\nWhen I'm building ecl-10.2.1 as part of Sage I get too warning messages from gcc. \n\n/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p2/src/src/c/dpp.c: In function 'put_declaration':\n/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p2/src/src/c/dpp.c:678:5: warning: too few arguments for format\n/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p2/src/src/c/dpp.c:680:13: warning: too many arguments for format\n\n\nLooking at line 678 of dpp.c, I see:\n\n    fprintf(out, \"\\tif (ecl_unlikely(narg!=%d))\");\n\nSo there's a %d, but what is associate with the %d? There should be an integer, but there is not one. So it seems to me gcc is right to complain there are too few arguments for format. \n\nLikewise, on line 680, I see:\n\n    fprintf(out, \"\\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\\n\",\n            nreq, function_code);\n\nThere's one two arguments supplied, but only one %d is there. That does not make any sense to me. Both \"nreq\" and \"function_code\" are declared as integers, so should there not two %d's and not one? \n\nAgain, it seems gcc is right to complain that. \n\nThere are thousands of warning messages in Sage, but I'm a bit concerned about resolving those in ecl, as the ecl library being built has text relocation problems - see #9840\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9917\n\n",
    "created_at": "2010-09-16T10:27:54Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "ECL has too few arguments and two many on file dpp.c",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9916",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jhpalmieri

Keywords: ecl

When I'm building ecl-10.2.1 as part of Sage I get too warning messages from gcc. 

/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p2/src/src/c/dpp.c: In function 'put_declaration':
/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p2/src/src/c/dpp.c:678:5: warning: too few arguments for format
/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p2/src/src/c/dpp.c:680:13: warning: too many arguments for format


Looking at line 678 of dpp.c, I see:

    fprintf(out, "\tif (ecl_unlikely(narg!=%d))");

So there's a %d, but what is associate with the %d? There should be an integer, but there is not one. So it seems to me gcc is right to complain there are too few arguments for format. 

Likewise, on line 680, I see:

    fprintf(out, "\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\n",
            nreq, function_code);

There's one two arguments supplied, but only one %d is there. That does not make any sense to me. Both "nreq" and "function_code" are declared as integers, so should there not two %d's and not one? 

Again, it seems gcc is right to complain that. 

There are thousands of warning messages in Sage, but I'm a bit concerned about resolving those in ecl, as the ecl library being built has text relocation problems - see #9840

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9917





---

archive/issue_comments_098509.json:
```json
{
    "body": "Perhaps temporarily fix this in Sage's 10.2.1 by patching it to the obvious:\n\n```C\n    fprintf(out, \"\\tif (ecl_unlikely(narg!=%d))\", nreq);\n```\n\nand\n\n```C\n    fprintf(out, \"\\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\\n\",\n            function_code);\n```\n\n\n(You **don't** have to report this upstream since it is already fixed.)",
    "created_at": "2010-09-16T16:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98509",
    "user": "https://github.com/nexttime"
}
```

Perhaps temporarily fix this in Sage's 10.2.1 by patching it to the obvious:

```C
    fprintf(out, "\tif (ecl_unlikely(narg!=%d))", nreq);
```

and

```C
    fprintf(out, "\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\n",
            function_code);
```


(You **don't** have to report this upstream since it is already fixed.)



---

archive/issue_comments_098510.json:
```json
{
    "body": "Yes, I just downloaded the latest ecl using \"git\" and it is indeed fixed upstream. I'll create a package with the upstream fixes to these two lines of code. It will remove two warnings. I doubt it is the cause of my relocation problems, but at least it will not leave me wondering if it is.",
    "created_at": "2010-09-16T23:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98510",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Yes, I just downloaded the latest ecl using "git" and it is indeed fixed upstream. I'll create a package with the upstream fixes to these two lines of code. It will remove two warnings. I doubt it is the cause of my relocation problems, but at least it will not leave me wondering if it is.



---

archive/issue_comments_098511.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-09-17T00:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98511",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_098512.json:
```json
{
    "body": "Now when this is compiled, the warnings messages have gone:\n\n\n```\n        gcc -I/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/src/c -I/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/build -I./ /export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/src/c/dpp.c  -I/export/home/drkirkby/sage-4.6.alpha0/local/include  -O2  -g  -Wall  -fPIC  -Dsun4sol2 -o dpp \n```\n\n\nAn updated package can be found at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p3.spkg\n\nThis needs further testing, as I've only currently tested this on OpenSolaris, but I think it is as safe as a bank vault. Hence for now I've marked it \"needs info\" until such time as I can confirm it works fully on other systems. \n\nDave",
    "created_at": "2010-09-17T00:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98512",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Now when this is compiled, the warnings messages have gone:


```
        gcc -I/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/src/c -I/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/build -I./ /export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/src/c/dpp.c  -I/export/home/drkirkby/sage-4.6.alpha0/local/include  -O2  -g  -Wall  -fPIC  -Dsun4sol2 -o dpp 
```


An updated package can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p3.spkg

This needs further testing, as I've only currently tested this on OpenSolaris, but I think it is as safe as a bank vault. Hence for now I've marked it "needs info" until such time as I can confirm it works fully on other systems. 

Dave



---

archive/issue_comments_098513.json:
```json
{
    "body": "Attachment [9917-makes-changes-to-dpp.c.patch](tarball://root/attachments/some-uuid/ticket9917/9917-makes-changes-to-dpp.c.patch) by drkirkby created at 2010-09-17 00:04:57\n\nMakes acouple of changes to the file dpp.c, which will remove a couple of compiler warnings which looked potentially harmful.",
    "created_at": "2010-09-17T00:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98513",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9917-makes-changes-to-dpp.c.patch](tarball://root/attachments/some-uuid/ticket9917/9917-makes-changes-to-dpp.c.patch) by drkirkby created at 2010-09-17 00:04:57

Makes acouple of changes to the file dpp.c, which will remove a couple of compiler warnings which looked potentially harmful.



---

archive/issue_comments_098514.json:
```json
{
    "body": "I've checked this now on OpenSolaris, Solaris 10 on SPARC (t2). Linux (sage.math) and OS X (bsd.math). \n\nECL installed ok on all of them. Maxima failed on OS X, but the failure is already known - see #8645. \n\nAs such, I'm now marking this for review. I don't know whether fixing these compiler warnings will solve the problems on Solaris (I doubt it will), but its not a good idea to have code like it was before. \n\nSince this is already fixed upstream in their git repository, I've marked it as such. \n\nDave",
    "created_at": "2010-09-17T01:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98514",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've checked this now on OpenSolaris, Solaris 10 on SPARC (t2). Linux (sage.math) and OS X (bsd.math). 

ECL installed ok on all of them. Maxima failed on OS X, but the failure is already known - see #8645. 

As such, I'm now marking this for review. I don't know whether fixing these compiler warnings will solve the problems on Solaris (I doubt it will), but its not a good idea to have code like it was before. 

Since this is already fixed upstream in their git repository, I've marked it as such. 

Dave



---

archive/issue_comments_098515.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-17T01:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98515",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_098516.json:
```json
{
    "body": "In the spkg, the file dpp.c.patch is empty.  That should be fixed.  Other than that, the changes look fine.  I'll test it on a few systems, but I can't imagine there being a problem.\n\nRegarding\n\n```\n    fprintf(out, \"\\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\\n\",\n            nreq, function_code);\n```\n\nI find it amusing that this problem occurs in a line containing \"wrong_num_arguments\"...",
    "created_at": "2010-09-17T01:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98516",
    "user": "https://github.com/jhpalmieri"
}
```

In the spkg, the file dpp.c.patch is empty.  That should be fixed.  Other than that, the changes look fine.  I'll test it on a few systems, but I can't imagine there being a problem.

Regarding

```
    fprintf(out, "\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\n",
            nreq, function_code);
```

I find it amusing that this problem occurs in a line containing "wrong_num_arguments"...



---

archive/issue_comments_098517.json:
```json
{
    "body": "It's also fixed in 10.4.1, which I think is a *stable* release.\n\n----\n\nThat's called *\"Literal programming\"* I think, self-referential.",
    "created_at": "2010-09-17T01:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98517",
    "user": "https://github.com/nexttime"
}
```

It's also fixed in 10.4.1, which I think is a *stable* release.

----

That's called *"Literal programming"* I think, self-referential.



---

archive/issue_comments_098518.json:
```json
{
    "body": "\n```diff\ndiff -Nu ecl-10.2.1.p1/src/src/c/dpp.c ecl-10.4.1/src/src/c/dpp.c\n--- ecl-10.2.1.p1/src/src/c/dpp.c\t2010-02-13 15:04:41.000000000 +0100\n+++ ecl-10.4.1/src/src/c/dpp.c\t2010-04-04 16:31:27.000000000 +0200\n@@ -251,13 +251,26 @@\n }\n \n char *\n-search_symbol(char *name, int *symbol_code)\n+search_symbol(char *name, int *symbol_code, int code)\n {\n \tint i;\n \tfor (i = 0; cl_symbols[i].name != NULL; i++) {\n \t\tif (!strcasecmp(name, cl_symbols[i].name)) {\n \t\t\tname = poolp;\n-\t\t\tif (i == 0) {\n+                        if (code) {\n+                                pushstr(\"MAKE_FIXNUM(/*\");\n+                                pushstr(cl_symbols[i].name);\n+\t\t\t\tpushstr(\"*/\");\n+\t\t\t\tif (i >= 1000)\n+\t\t\t\t\tpushc((i / 1000) % 10 + '0');\n+\t\t\t\tif (i >= 100)\n+\t\t\t\t\tpushc((i / 100) % 10 + '0');\n+\t\t\t\tif (i >= 10)\n+\t\t\t\t\tpushc((i / 10) % 10 + '0');\n+\t\t\t\tpushc(i % 10 + '0');\n+\t\t\t\tpushstr(\")\");\n+\t\t\t\tpushc(0);\n+                        } else if (i == 0) {\n \t\t\t\tpushstr(\"Cnil\");\n \t\t\t\tpushc(0);\n \t\t\t} else {\n@@ -283,19 +296,20 @@\n }\n \n char *\n-read_symbol()\n+read_symbol(int code)\n {\n \tchar c, *name = poolp;\n+        char end = code? ']' : '\\'';\n \n \tc = readc();\n-\twhile (c != '\\'') {\n+\twhile (c != end) {\n \t\tif (c == '_') c = '-';\n \t\tpushc(c); \n \t\tc = readc();\n \t}\n \tpushc(0);\n \n-\tname = search_symbol(poolp = name, 0);\n+\tname = search_symbol(poolp = name, 0, code);\n \tif (name == NULL) {\n \t\tname = poolp;\n \t\tprintf(\"\\nUnknown symbol: %s\\n\", name);\n@@ -387,7 +401,10 @@\n \t\t} else if (c == '@') {\n \t\t\tc = readc();\n \t\t\tif (c == '\\'') {\n-\t\t\t\t(void)read_symbol();\n+\t\t\t\t(void)read_symbol(0);\n+\t\t\t\tpoolp--;\n+\t\t\t} else if (c == '[') {\n+\t\t\t\t(void)read_symbol(1);\n \t\t\t\tpoolp--;\n \t\t\t} else if (c == '@') {\n \t\t\t\tpushc(c);\n@@ -448,7 +465,7 @@\n get_function(void)\n {\n \tfunction = read_function();\n-\tfunction_symbol = search_symbol(function, &function_code);\n+\tfunction_symbol = search_symbol(function, &function_code, 0);\n \tif (function_symbol == NULL) {\n \t\tfunction_symbol = poolp;\n \t\tpushstr(\"Cnil\");\n@@ -675,9 +692,9 @@\n   }\n   if (nopt == 0 && !rest_flag && !key_flag) {\n     put_lineno();\n-    fprintf(out, \"\\tif (ecl_unlikely(narg!=%d))\");\n+    fprintf(out, \"\\tif (ecl_unlikely(narg!=%d))\", nreq);\n     fprintf(out, \"\\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\\n\",\n-            nreq, function_code);\n+            function_code);\n   } else {\n     simple_varargs = !rest_flag && !key_flag && ((nreq + nopt) < 32);\n     if (key_flag) {\n@@ -833,7 +850,14 @@\n \t} else if (c == '\\'') {\n \t\tchar *p;\n \t\tpoolp = pool;\n-\t\tp = read_symbol();\n+\t\tp = read_symbol(0);\n+\t\tpushc('\\0');\n+\t\tfprintf(out,\"%s\",p);\n+\t\tgoto LOOP;\n+\t}  else if (c == '[') {\n+\t\tchar *p;\n+\t\tpoolp = pool;\n+\t\tp = read_symbol(1);\n \t\tpushc('\\0');\n \t\tfprintf(out,\"%s\",p);\n \t\tgoto LOOP;\n```\n\n\nIf that convinces you more.",
    "created_at": "2010-09-17T01:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98518",
    "user": "https://github.com/nexttime"
}
```


```diff
diff -Nu ecl-10.2.1.p1/src/src/c/dpp.c ecl-10.4.1/src/src/c/dpp.c
--- ecl-10.2.1.p1/src/src/c/dpp.c	2010-02-13 15:04:41.000000000 +0100
+++ ecl-10.4.1/src/src/c/dpp.c	2010-04-04 16:31:27.000000000 +0200
@@ -251,13 +251,26 @@
 }
 
 char *
-search_symbol(char *name, int *symbol_code)
+search_symbol(char *name, int *symbol_code, int code)
 {
 	int i;
 	for (i = 0; cl_symbols[i].name != NULL; i++) {
 		if (!strcasecmp(name, cl_symbols[i].name)) {
 			name = poolp;
-			if (i == 0) {
+                        if (code) {
+                                pushstr("MAKE_FIXNUM(/*");
+                                pushstr(cl_symbols[i].name);
+				pushstr("*/");
+				if (i >= 1000)
+					pushc((i / 1000) % 10 + '0');
+				if (i >= 100)
+					pushc((i / 100) % 10 + '0');
+				if (i >= 10)
+					pushc((i / 10) % 10 + '0');
+				pushc(i % 10 + '0');
+				pushstr(")");
+				pushc(0);
+                        } else if (i == 0) {
 				pushstr("Cnil");
 				pushc(0);
 			} else {
@@ -283,19 +296,20 @@
 }
 
 char *
-read_symbol()
+read_symbol(int code)
 {
 	char c, *name = poolp;
+        char end = code? ']' : '\'';
 
 	c = readc();
-	while (c != '\'') {
+	while (c != end) {
 		if (c == '_') c = '-';
 		pushc(c); 
 		c = readc();
 	}
 	pushc(0);
 
-	name = search_symbol(poolp = name, 0);
+	name = search_symbol(poolp = name, 0, code);
 	if (name == NULL) {
 		name = poolp;
 		printf("\nUnknown symbol: %s\n", name);
@@ -387,7 +401,10 @@
 		} else if (c == '@') {
 			c = readc();
 			if (c == '\'') {
-				(void)read_symbol();
+				(void)read_symbol(0);
+				poolp--;
+			} else if (c == '[') {
+				(void)read_symbol(1);
 				poolp--;
 			} else if (c == '@') {
 				pushc(c);
@@ -448,7 +465,7 @@
 get_function(void)
 {
 	function = read_function();
-	function_symbol = search_symbol(function, &function_code);
+	function_symbol = search_symbol(function, &function_code, 0);
 	if (function_symbol == NULL) {
 		function_symbol = poolp;
 		pushstr("Cnil");
@@ -675,9 +692,9 @@
   }
   if (nopt == 0 && !rest_flag && !key_flag) {
     put_lineno();
-    fprintf(out, "\tif (ecl_unlikely(narg!=%d))");
+    fprintf(out, "\tif (ecl_unlikely(narg!=%d))", nreq);
     fprintf(out, "\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\n",
-            nreq, function_code);
+            function_code);
   } else {
     simple_varargs = !rest_flag && !key_flag && ((nreq + nopt) < 32);
     if (key_flag) {
@@ -833,7 +850,14 @@
 	} else if (c == '\'') {
 		char *p;
 		poolp = pool;
-		p = read_symbol();
+		p = read_symbol(0);
+		pushc('\0');
+		fprintf(out,"%s",p);
+		goto LOOP;
+	}  else if (c == '[') {
+		char *p;
+		poolp = pool;
+		p = read_symbol(1);
 		pushc('\0');
 		fprintf(out,"%s",p);
 		goto LOOP;
```


If that convinces you more.



---

archive/issue_comments_098519.json:
```json
{
    "body": "s/literal/literate/\n\nIt's getting late...",
    "created_at": "2010-09-17T01:59:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98519",
    "user": "https://github.com/nexttime"
}
```

s/literal/literate/

It's getting late...



---

archive/issue_comments_098520.json:
```json
{
    "body": "Attachment [9917-non-empty-patch-file.patch](tarball://root/attachments/some-uuid/ticket9917/9917-non-empty-patch-file.patch) by drkirkby created at 2010-09-17 07:15:09\n\nSomehow the previous patch file I made was empty - this corrects that.",
    "created_at": "2010-09-17T07:15:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98520",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9917-non-empty-patch-file.patch](tarball://root/attachments/some-uuid/ticket9917/9917-non-empty-patch-file.patch) by drkirkby created at 2010-09-17 07:15:09

Somehow the previous patch file I made was empty - this corrects that.



---

archive/issue_comments_098521.json:
```json
{
    "body": "I've updated the patch file - I've no idea how I managed to make it empty before! \n\nThere are of course several changes to the upstream code, but since the snapshot I took was an unstable release, I think it is wise to limit the changes to just what were causing a problem in Sage. \n\nI'm not sure if there is a later stable release available or not - I've found the version number at the top right of the ECL web site rarely agrees with the version number one can actually download. I think we probably have the latest stable release due to a comment made by Juanjo on the ECL mailing list in my response to my question about this matter. \n\n''Sage cannot rely on unstable releases, which is why I was slowly working on\nanother stable release -- unfortunately actual work got in the way.\n\nJuanjo''\n\nI've updated the .spkg at \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p3.spkg\n\nDave",
    "created_at": "2010-09-17T07:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98521",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've updated the patch file - I've no idea how I managed to make it empty before! 

There are of course several changes to the upstream code, but since the snapshot I took was an unstable release, I think it is wise to limit the changes to just what were causing a problem in Sage. 

I'm not sure if there is a later stable release available or not - I've found the version number at the top right of the ECL web site rarely agrees with the version number one can actually download. I think we probably have the latest stable release due to a comment made by Juanjo on the ECL mailing list in my response to my question about this matter. 

''Sage cannot rely on unstable releases, which is why I was slowly working on
another stable release -- unfortunately actual work got in the way.

Juanjo''

I've updated the .spkg at 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p3.spkg

Dave



---

archive/issue_comments_098522.json:
```json
{
    "body": "Replying to [comment:6 jhpalmieri]:\n\n> I find it amusing that this problem occurs in a line containing \"wrong_num_arguments\"...\n\nYes the line in ECL is rather funny. It's a bit like that ATLAS file `make_correct_shared.sh`, which seems to screw up making the shared libraries! \n\nDave",
    "created_at": "2010-09-18T12:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98522",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:6 jhpalmieri]:

> I find it amusing that this problem occurs in a line containing "wrong_num_arguments"...

Yes the line in ECL is rather funny. It's a bit like that ATLAS file `make_correct_shared.sh`, which seems to screw up making the shared libraries! 

Dave



---

archive/issue_comments_098523.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-18T15:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98523",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_025008.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-29T08:39:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9916#event-25008"
}
```



---

archive/issue_comments_098524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9916",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9916#issuecomment-98524",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
