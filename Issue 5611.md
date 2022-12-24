# Issue 5611: [with spkg; needs review] blackboard bold font for jsMath

archive/issues_005611.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @jasongrout\n\nTo create this spkg, I took the file [http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/bbold10/bbold10.zip](http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/bbold10/bbold10.zip) and unzipped it.  The resulting directory gets installed into SAGE_LOCAL/notebook/javascript/jsMath/fonts; thus jsMath must be installed first.\n\nI've never submitted an spkg before, so let me know what I need to fix.  (For example, there is no mercurial repository here; does it need one?)\n\nThis is intended to be a required part of the Sage install; it is necessary for #5610.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5611\n\n",
    "created_at": "2009-03-25T21:54:28Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with spkg; needs review] blackboard bold font for jsMath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5611",
    "user": "@jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  @jasongrout

To create this spkg, I took the file [http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/bbold10/bbold10.zip](http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/bbold10/bbold10.zip) and unzipped it.  The resulting directory gets installed into SAGE_LOCAL/notebook/javascript/jsMath/fonts; thus jsMath must be installed first.

I've never submitted an spkg before, so let me know what I need to fix.  (For example, there is no mercurial repository here; does it need one?)

This is intended to be a required part of the Sage install; it is necessary for #5610.


Issue created by migration from https://trac.sagemath.org/ticket/5611





---

archive/issue_comments_043815.json:
```json
{
    "body": "Two things:\n\n* this might be better to put in the jsmath.spkg - it is certainly simpler\n* please do not attach spkgs to trac since it will be backed up daily until the end of time and a 0.5 MB spkg is rather large and does not compress well.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T00:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43815",
    "user": "mabshoff"
}
```

Two things:

* this might be better to put in the jsmath.spkg - it is certainly simpler
* please do not attach spkgs to trac since it will be backed up daily until the end of time and a 0.5 MB spkg is rather large and does not compress well.

Cheers,

Michael



---

archive/issue_comments_043816.json:
```json
{
    "body": "John's spkg can now be found at\n\n http://sage.math.washington.edu/home/mabshoff/SPKG/jsmath-bbold10-0.1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T00:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43816",
    "user": "mabshoff"
}
```

John's spkg can now be found at

 http://sage.math.washington.edu/home/mabshoff/SPKG/jsmath-bbold10-0.1.spkg

Cheers,

Michael



---

archive/issue_comments_043817.json:
```json
{
    "body": "Okay, if you want an updated jsMath package instead, it's here: [http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6a.p1.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6a.p1.spkg)\n\n(I just renamed it from ...p0.spkg to ...p1.spkg. Is that the right thing to do?)",
    "created_at": "2009-03-26T02:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43817",
    "user": "@jhpalmieri"
}
```

Okay, if you want an updated jsMath package instead, it's here: [http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6a.p1.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6a.p1.spkg)

(I just renamed it from ...p0.spkg to ...p1.spkg. Is that the right thing to do?)



---

archive/issue_comments_043818.json:
```json
{
    "body": "In case we also want to upgrade jsMath from 3.6a to 3.6b (see [jsMath change log](http://www.math.union.edu/~dpvc/jsMath/changes.html)), here's another jsMath package:\n\n[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg)\n\n(I'll keep both the 3.6a and the 3.6b versions around for a while.)",
    "created_at": "2009-03-27T17:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43818",
    "user": "@jhpalmieri"
}
```

In case we also want to upgrade jsMath from 3.6a to 3.6b (see [jsMath change log](http://www.math.union.edu/~dpvc/jsMath/changes.html)), here's another jsMath package:

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg)

(I'll keep both the 3.6a and the 3.6b versions around for a while.)



---

archive/issue_comments_043819.json:
```json
{
    "body": "This may be a duplicate of another ticket, or at least of work someone is doing which will appear in another ticket, so I'm marking this as \"not ready for review\".  Once the situation is worked out one way or the other, I'll change this to \"needs review\" or else mark it as a duplicate.",
    "created_at": "2009-03-27T17:48:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43819",
    "user": "@jhpalmieri"
}
```

This may be a duplicate of another ticket, or at least of work someone is doing which will appear in another ticket, so I'm marking this as "not ready for review".  Once the situation is worked out one way or the other, I'll change this to "needs review" or else mark it as a duplicate.



---

archive/issue_comments_043820.json:
```json
{
    "body": "I may have been wrong about what's needed for blackboard bold: I think I want the font msbm10, not bbold10. Here are two possible jsmath spkgs:\n\n[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-bbold10.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-bbold10.p0.spkg)  (old one: bbold10)\n\n[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-msbm10.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-msbm10.p0.spkg)  (new one: msbm10)\n\nAfter installing the spkg, test it by adding one line to the file sage/server/notebook/notebook.py:\n\n```\ndiff -r 0a59c5ea9cac -r 9d482703384d sage/server/notebook/notebook.py\n--- a/sage/server/notebook/notebook.py\tWed Mar 25 09:33:27 2009 -0700\n+++ b/sage/server/notebook/notebook.py\tWed Mar 25 14:07:43 2009 -0700\n@@ -1754,6 +1754,7 @@\n          jsMath.Extension.Require(\"verb\");\n          jsMath.Extension.Require(\"moreArrows\");\n          jsMath.Extension.Require(\"AMSmath\");\n+         jsMath.Extension.Require(\"AMSsymbols\");\n </script>'''\n \n         # import latex macros\n```\n\nThen in the notebook, try\n\n```\n%html\n$\\mathbb{R}$\n```\n",
    "created_at": "2009-04-01T00:37:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43820",
    "user": "@jhpalmieri"
}
```

I may have been wrong about what's needed for blackboard bold: I think I want the font msbm10, not bbold10. Here are two possible jsmath spkgs:

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-bbold10.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-bbold10.p0.spkg)  (old one: bbold10)

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-msbm10.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-msbm10.p0.spkg)  (new one: msbm10)

After installing the spkg, test it by adding one line to the file sage/server/notebook/notebook.py:

```
diff -r 0a59c5ea9cac -r 9d482703384d sage/server/notebook/notebook.py
--- a/sage/server/notebook/notebook.py	Wed Mar 25 09:33:27 2009 -0700
+++ b/sage/server/notebook/notebook.py	Wed Mar 25 14:07:43 2009 -0700
@@ -1754,6 +1754,7 @@
          jsMath.Extension.Require("verb");
          jsMath.Extension.Require("moreArrows");
          jsMath.Extension.Require("AMSmath");
+         jsMath.Extension.Require("AMSsymbols");
 </script>'''
 
         # import latex macros
```

Then in the notebook, try

```
%html
$\mathbb{R}$
```




---

archive/issue_comments_043821.json:
```json
{
    "body": "Attachment [jsmath-amssymbols.patch](tarball://root/attachments/some-uuid/ticket5611/jsmath-amssymbols.patch) by @jhpalmieri created at 2009-04-14 21:06:35",
    "created_at": "2009-04-14T21:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43821",
    "user": "@jhpalmieri"
}
```

Attachment [jsmath-amssymbols.patch](tarball://root/attachments/some-uuid/ticket5611/jsmath-amssymbols.patch) by @jhpalmieri created at 2009-04-14 21:06:35



---

archive/issue_comments_043822.json:
```json
{
    "body": "> After installing the spkg, test it by adding one line to the file sage/server/notebook/notebook.py:\n\nThe attached patch adds this single line.  So apply the patch, install the spkg (msbm version), and try\n\n```\n%html\n$\\mathbb{R}$\n```\n",
    "created_at": "2009-04-14T21:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43822",
    "user": "@jhpalmieri"
}
```

> After installing the spkg, test it by adding one line to the file sage/server/notebook/notebook.py:

The attached patch adds this single line.  So apply the patch, install the spkg (msbm version), and try

```
%html
$\mathbb{R}$
```




---

archive/issue_comments_043823.json:
```json
{
    "body": "I need to clear up one thing: the correct spkg to download is here:\n\n[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg)\n\nThis is the version with the msbm font.  (The one I mentioned earlier also has this font, but the name of the spkg is wrong -- it's not just \"jsmath-3.6b.p0\" -- and that confuses sage.  The correct one is just a renamed version of the earlier one.)\n\nInstall this, install the patch, and things should work...\n\n> This may be a duplicate of another ticket, or at least of work someone is doing which will appear in another ticket\n\nI think we've waited long enough for the other ticket to appear. I'm giving up and opening this one up for review.",
    "created_at": "2009-04-14T21:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43823",
    "user": "@jhpalmieri"
}
```

I need to clear up one thing: the correct spkg to download is here:

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg)

This is the version with the msbm font.  (The one I mentioned earlier also has this font, but the name of the spkg is wrong -- it's not just "jsmath-3.6b.p0" -- and that confuses sage.  The correct one is just a renamed version of the earlier one.)

Install this, install the patch, and things should work...

> This may be a duplicate of another ticket, or at least of work someone is doing which will appear in another ticket

I think we've waited long enough for the other ticket to appear. I'm giving up and opening this one up for review.



---

archive/issue_comments_043824.json:
```json
{
    "body": "I agree we've waited long enough (thanks for your patience!).  I'll review it.",
    "created_at": "2009-04-14T21:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43824",
    "user": "@jasongrout"
}
```

I agree we've waited long enough (thanks for your patience!).  I'll review it.



---

archive/issue_comments_043825.json:
```json
{
    "body": "I will review this tonight unless someone beats me to it ;). Either way - let's get this into 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T22:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43825",
    "user": "mabshoff"
}
```

I will review this tonight unless someone beats me to it ;). Either way - let's get this into 3.4.1.

Cheers,

Michael



---

archive/issue_comments_043826.json:
```json
{
    "body": "I cleaned up the spkg just a tiny bit (put the fonts directory in the src/ folder and split up the changelog).  The new spkg is here: http://sage.math.washington.edu/home/jason/jsmath-3.6b.p1.spkg\n\nPositive review on the spkg and patch.  It seems to work as advertised.",
    "created_at": "2009-04-16T08:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43826",
    "user": "@jasongrout"
}
```

I cleaned up the spkg just a tiny bit (put the fonts directory in the src/ folder and split up the changelog).  The new spkg is here: http://sage.math.washington.edu/home/jason/jsmath-3.6b.p1.spkg

Positive review on the spkg and patch.  It seems to work as advertised.



---

archive/issue_comments_043827.json:
```json
{
    "body": "Merged jsmath-3.6b.p1.spkg and jsmath-amssymbols.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T10:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43827",
    "user": "mabshoff"
}
```

Merged jsmath-3.6b.p1.spkg and jsmath-amssymbols.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_043828.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T10:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5611#issuecomment-43828",
    "user": "mabshoff"
}
```

Resolution: fixed
