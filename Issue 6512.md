# Issue 6512: [with patch, needs review] Link to jsMath's easy/load.js only if the documentation is built with --jsmath

archive/issues_006512.json:
```json
{
    "body": "Assignee: tba\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cb1687577bf5843e/b453af3a0750ba23?#b453af3a0750ba23).\n\n`sage -docbuild tutorial html` renders all mathematics as images, but if the jsMath library is present, its processor hides all display equations.\n\nThis is a follow-up to #5799.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6512\n\n",
    "created_at": "2009-07-11T16:21:35Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, needs review] Link to jsMath's easy/load.js only if the documentation is built with --jsmath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6512",
    "user": "https://github.com/qed777"
}
```
Assignee: tba

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cb1687577bf5843e/b453af3a0750ba23?#b453af3a0750ba23).

`sage -docbuild tutorial html` renders all mathematics as images, but if the jsMath library is present, its processor hides all display equations.

This is a follow-up to #5799.

Issue created by migration from https://trac.sagemath.org/ticket/6512





---

archive/issue_comments_052954.json:
```json
{
    "body": "Attachment [trac_6512_jsmath_fix.patch](tarball://root/attachments/some-uuid/ticket6512/trac_6512_jsmath_fix.patch) by @qed777 created at 2009-07-11 16:23:58",
    "created_at": "2009-07-11T16:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6512#issuecomment-52954",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6512_jsmath_fix.patch](tarball://root/attachments/some-uuid/ticket6512/trac_6512_jsmath_fix.patch) by @qed777 created at 2009-07-11 16:23:58



---

archive/issue_comments_052955.json:
```json
{
    "body": "The patch removes a redundant link to jsMath.  Sphinx should now include references to jsMath in its output only if `--jsmath` is part of the command-line.  For example,\n\n`sage -docbuild reference html --jsmath`",
    "created_at": "2009-07-11T16:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6512#issuecomment-52955",
    "user": "https://github.com/qed777"
}
```

The patch removes a redundant link to jsMath.  Sphinx should now include references to jsMath in its output only if `--jsmath` is part of the command-line.  For example,

`sage -docbuild reference html --jsmath`



---

archive/issue_events_015367.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2009-07-11T16:30:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "milestone": "sage-4.1.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6512#event-15367"
}
```



---

archive/issue_comments_052956.json:
```json
{
    "body": "This works for me: with the patch installed, it loads jsMath when it's needed, and doesn't load it when it isn't. Positive review.",
    "created_at": "2009-07-13T16:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6512#issuecomment-52956",
    "user": "https://github.com/loefflerd"
}
```

This works for me: with the patch installed, it loads jsMath when it's needed, and doesn't load it when it isn't. Positive review.



---

archive/issue_comments_052957.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-17T09:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6512#issuecomment-52957",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015368.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-17T09:21:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6512#event-15368"
}
```



---

archive/issue_comments_052958.json:
```json
{
    "body": "Mitesh, thank you very much for fixing this.",
    "created_at": "2009-07-17T09:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6512#issuecomment-52958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Mitesh, thank you very much for fixing this.



---

archive/issue_comments_052959.json:
```json
{
    "body": "I agree that the change above looks like the correct one.  Another option was to have jsmath automatically typeset the stuff in the alt parameter of the img files.  Davide Cervone sent me a message with a way to do that:\n\n```\n\nJason:\n\nI've attached a javascript file that should do the preprocessing that you need.  It implements the suggestion I made to you about making span's with display:none so that the images show until jsMath reprocesses them.  You can load it just before jsMath/easy/load.js, or you could add it to the loadFiles list in easy/load.js.  Let me know if this doesn't do the trick for you.\n\nDavide\n\nOn Jul 13, 2009, at 11:34 PM, jason-sage@creativetrax.com wrote:\n\n> Davide P. Cervone wrote:\n>> Jason:\n>>\n>> Here's what's going on:  jsMath looks for DIV's and SPAN's that are marked by CLASS=\"math\" and treats their contents as TeX source code to process.  It replaces the original contents of the DIV or SPAN with the typeset version of the TeX code.  Because the image's are not DIV's or SPAN's jsMath ignores them (even though they are CLASS=\"math\"), but the <DIV CLASS=\"math\"> that contains an image is processed by jsMath.  It takes the text content of the DIV (empty in this case) and typesets it (the result is blank).  Thus the image disappears and is replaced by nothing.\n>\n> Thanks!  Your explanation and suggestions below are very appreciated!\n>\n> Jason \n\n```\n\nThe javascript code is:\n\n```\n\n(function () {\n  var PREPROCESS = function () {\n    var parent, span, i;\n    var img = document.getElementsByTagName(\"img\");\n    for (i = 0; i < img.length; i++) {\n      if (img[i].alt) {\n        parent = img[i].parentNode.parentNode;\n        if (img[i].className === \"math\") {\n          span = img[i].parentNode.insertBefore(document.createElement(\"span\"),img[i]);\n          span.className = \"math\";\n          span.appendChild(img[i]);\n          span = span.appendChild(document.createElement(\"span\"));\n          span.style.display = \"none\";\n          span.appendChild(document.createTextNode(img[i].alt));\n        } else if (parent && parent.tagName.toLowerCase() === \"div\" && parent.className === \"math\") {\n          span = img[i].parentNode.appendChild(document.createElement(\"span\"));\n          span.style.display = \"none\";\n          span.appendChild(document.createTextNode(img[i].alt));\n        }\n      }\n    }\n  };\n  \n  if (window.addEventListener) {window.addEventListener(\"load\",PREPROCESS,false)}\n  else if (window.attachEvent) {window.attachEvent(\"onload\",PREPROCESS)}\n  else {window.onload = PREPROCESS}\n})();\n\n\n```",
    "created_at": "2009-07-18T20:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6512#issuecomment-52959",
    "user": "https://github.com/jasongrout"
}
```

I agree that the change above looks like the correct one.  Another option was to have jsmath automatically typeset the stuff in the alt parameter of the img files.  Davide Cervone sent me a message with a way to do that:

```

Jason:

I've attached a javascript file that should do the preprocessing that you need.  It implements the suggestion I made to you about making span's with display:none so that the images show until jsMath reprocesses them.  You can load it just before jsMath/easy/load.js, or you could add it to the loadFiles list in easy/load.js.  Let me know if this doesn't do the trick for you.

Davide

On Jul 13, 2009, at 11:34 PM, jason-sage@creativetrax.com wrote:

> Davide P. Cervone wrote:
>> Jason:
>>
>> Here's what's going on:  jsMath looks for DIV's and SPAN's that are marked by CLASS="math" and treats their contents as TeX source code to process.  It replaces the original contents of the DIV or SPAN with the typeset version of the TeX code.  Because the image's are not DIV's or SPAN's jsMath ignores them (even though they are CLASS="math"), but the <DIV CLASS="math"> that contains an image is processed by jsMath.  It takes the text content of the DIV (empty in this case) and typesets it (the result is blank).  Thus the image disappears and is replaced by nothing.
>
> Thanks!  Your explanation and suggestions below are very appreciated!
>
> Jason 

```

The javascript code is:

```

(function () {
  var PREPROCESS = function () {
    var parent, span, i;
    var img = document.getElementsByTagName("img");
    for (i = 0; i < img.length; i++) {
      if (img[i].alt) {
        parent = img[i].parentNode.parentNode;
        if (img[i].className === "math") {
          span = img[i].parentNode.insertBefore(document.createElement("span"),img[i]);
          span.className = "math";
          span.appendChild(img[i]);
          span = span.appendChild(document.createElement("span"));
          span.style.display = "none";
          span.appendChild(document.createTextNode(img[i].alt));
        } else if (parent && parent.tagName.toLowerCase() === "div" && parent.className === "math") {
          span = img[i].parentNode.appendChild(document.createElement("span"));
          span.style.display = "none";
          span.appendChild(document.createTextNode(img[i].alt));
        }
      }
    }
  };
  
  if (window.addEventListener) {window.addEventListener("load",PREPROCESS,false)}
  else if (window.attachEvent) {window.attachEvent("onload",PREPROCESS)}
  else {window.onload = PREPROCESS}
})();


```
