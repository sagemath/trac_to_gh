# Issue 6512: [with patch, needs review] Link to jsMath's easy/load.js only if the documentation is built with --jsmath

Issue created by migration from https://trac.sagemath.org/ticket/6512

Original creator: mpatel

Original creation time: 2009-07-11 16:21:35

Assignee: tba

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cb1687577bf5843e/b453af3a0750ba23?#b453af3a0750ba23).

`sage -docbuild tutorial html` renders all mathematics as images, but if the jsMath library is present, its processor hides all display equations.

This is a follow-up to #5799.


---

Attachment


---

Comment by mpatel created at 2009-07-11 16:30:07

The patch removes a redundant link to jsMath.  Sphinx should now include references to jsMath in its output only if `--jsmath` is part of the command-line.  For example,

`sage -docbuild reference html --jsmath`


---

Comment by davidloeffler created at 2009-07-13 16:16:29

This works for me: with the patch installed, it loads jsMath when it's needed, and doesn't load it when it isn't. Positive review.


---

Comment by davidloeffler created at 2009-07-13 16:19:57

Changing priority from minor to major.


---

Comment by mvngu created at 2009-07-17 09:21:27

Resolution: fixed


---

Comment by mvngu created at 2009-07-17 09:21:27

Mitesh, thank you very much for fixing this.


---

Comment by jason created at 2009-07-18 20:28:10

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

