# Issue 9916: ECL has too few arguments and two many on file dpp.c

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-16 10:27:54

Assignee: GeorgSWeber

CC:  jhpalmieri

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


---

Comment by leif created at 2010-09-16 16:18:04

Perhaps temporarily fix this in Sage's 10.2.1 by patching it to the obvious:

```C
    fprintf(out, "\tif (ecl_unlikely(narg!=%d))", nreq);
```

and

```C
    fprintf(out, "\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\n",
            function_code);
```


(You *don't* have to report this upstream since it is already fixed.)


---

Comment by drkirkby created at 2010-09-16 23:29:55

Yes, I just downloaded the latest ecl using "git" and it is indeed fixed upstream. I'll create a package with the upstream fixes to these two lines of code. It will remove two warnings. I doubt it is the cause of my relocation problems, but at least it will not leave me wondering if it is.


---

Comment by drkirkby created at 2010-09-17 00:03:54

Changing status from new to needs_info.


---

Comment by drkirkby created at 2010-09-17 00:03:54

Now when this is compiled, the warnings messages have gone:


```
        gcc -I/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/src/c -I/export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/build -I./ /export/home/drkirkby/sage-4.6.alpha0/spkg/build/ecl-10.2.1.p3/src/src/c/dpp.c  -I/export/home/drkirkby/sage-4.6.alpha0/local/include  -O2  -g  -Wall  -fPIC  -Dsun4sol2 -o dpp 
```


An updated package can be found at 

http://boxen.math.washington.edu/home/kirkby/patches/ecl-10.2.1.p3.spkg

This needs further testing, as I've only currently tested this on OpenSolaris, but I think it is as safe as a bank vault. Hence for now I've marked it "needs info" until such time as I can confirm it works fully on other systems. 

Dave


---

Attachment

Makes acouple of changes to the file dpp.c, which will remove a couple of compiler warnings which looked potentially harmful.


---

Comment by drkirkby created at 2010-09-17 01:30:34

I've checked this now on OpenSolaris, Solaris 10 on SPARC (t2). Linux (sage.math) and OS X (bsd.math). 

ECL installed ok on all of them. Maxima failed on OS X, but the failure is already known - see #8645. 

As such, I'm now marking this for review. I don't know whether fixing these compiler warnings will solve the problems on Solaris (I doubt it will), but its not a good idea to have code like it was before. 

Since this is already fixed upstream in their git repository, I've marked it as such. 

Dave


---

Comment by drkirkby created at 2010-09-17 01:30:34

Changing status from needs_info to needs_review.


---

Comment by jhpalmieri created at 2010-09-17 01:40:12

In the spkg, the file dpp.c.patch is empty.  That should be fixed.  Other than that, the changes look fine.  I'll test it on a few systems, but I can't imagine there being a problem.

Regarding

```
    fprintf(out, "\t   FEwrong_num_arguments(MAKE_FIXNUM(%d));\n",
            nreq, function_code);
```

I find it amusing that this problem occurs in a line containing "wrong_num_arguments"...


---

Comment by leif created at 2010-09-17 01:45:28

It's also fixed in 10.4.1, which I think is a _stable_ release.

----

That's called _"Literal programming"_ I think, self-referential.


---

Comment by leif created at 2010-09-17 01:55:09


```diff
diff -Nu ecl-10.2.1.p1/src/src/c/dpp.c ecl-10.4.1/src/src/c/dpp.c
--- ecl-10.2.1.p1/src/src/c/dpp.c	2010-02-13 15:04:41.000000000 +0100
+++ ecl-10.4.1/src/src/c/dpp.c	2010-04-04 16:31:27.000000000 +0200
`@``@` -251,13 +251,26 `@``@`
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
`@``@` -283,19 +296,20 `@``@`
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
`@``@` -387,7 +401,10 `@``@`
 		} else if (c == '`@`') {
 			c = readc();
 			if (c == '\'') {
-				(void)read_symbol();
+				(void)read_symbol(0);
+				poolp--;
+			} else if (c == '[') {
+				(void)read_symbol(1);
 				poolp--;
 			} else if (c == '`@`') {
 				pushc(c);
`@``@` -448,7 +465,7 `@``@`
 get_function(void)
 {
 	function = read_function();
-	function_symbol = search_symbol(function, &function_code);
+	function_symbol = search_symbol(function, &function_code, 0);
 	if (function_symbol == NULL) {
 		function_symbol = poolp;
 		pushstr("Cnil");
`@``@` -675,9 +692,9 `@``@`
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
`@``@` -833,7 +850,14 `@``@`
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

Comment by leif created at 2010-09-17 01:59:50

s/literal/literate/

It's getting late...


---

Attachment

Somehow the previous patch file I made was empty - this corrects that.


---

Comment by drkirkby created at 2010-09-17 07:40:00

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

Comment by drkirkby created at 2010-09-18 12:23:07

Replying to [comment:6 jhpalmieri]:

> I find it amusing that this problem occurs in a line containing "wrong_num_arguments"...

Yes the line in ECL is rather funny. It's a bit like that ATLAS file `make_correct_shared.sh`, which seems to screw up making the shared libraries! 

Dave


---

Comment by jhpalmieri created at 2010-09-18 15:36:16

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-29 08:39:54

Resolution: fixed
