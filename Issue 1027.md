# Issue 1027: problems with extcode spkg

Issue created by migration from https://trac.sagemath.org/ticket/1027

Original creator: cwitty

Original creation time: 2007-10-29 04:38:14

Assignee: was

There are a couple of problems with the extcode spkg:

1) the spkg-dist script does not copy .hgtags or .hgignore, so every "sage -sdist" ends up with those files missing from the spkg (although they're still in the repository).

2) There are many non-revision-controlled files in the spkg.

This shows both problems (the '!' means the file is missing):

```
cwitty@comet:~/spkg/extcode-2.8.10$ hg status
! .hgignore
! .hgtags
? extcode-2006-12-11.hg
? extcode.hg
? javascript/jsmath/COPYING.txt
? javascript/jsmath/blank.gif
? javascript/jsmath/extensions/AMSsymbols.js
? javascript/jsmath/extensions/HTML.js
? javascript/jsmath/extensions/bbox.js
? javascript/jsmath/extensions/boldsymbol.js
? javascript/jsmath/extensions/double-click.js
? javascript/jsmath/extensions/fbox.js
? javascript/jsmath/extensions/font.js
? javascript/jsmath/extensions/leaders.js
? javascript/jsmath/extensions/mathchoice.js
? javascript/jsmath/extensions/mimeTeX.js
? javascript/jsmath/extensions/moreArrows.js
? javascript/jsmath/extensions/newcommand.js
? javascript/jsmath/extensions/underset-overset.js
? javascript/jsmath/jsMath-BaKoMa-fonts.js
? javascript/jsmath/jsMath-autoload.html
? javascript/jsmath/jsMath-controls.html
? javascript/jsmath/jsMath-fallback-mac-mozilla.js
? javascript/jsmath/jsMath-fallback-mac-msie.js
? javascript/jsmath/jsMath-fallback-mac.js
? javascript/jsmath/jsMath-fallback-pc.js
? javascript/jsmath/jsMath-fallback-symbols.js
? javascript/jsmath/jsMath-fallback-unix.js
? javascript/jsmath/jsMath-global-controls.html
? javascript/jsmath/jsMath-global.html
? javascript/jsmath/jsMath-loader-omniweb4.js
? javascript/jsmath/jsMath-loader.html
? javascript/jsmath/jsMath-msie-mac.js
? javascript/jsmath/jsMath-old-browsers.js
? javascript/jsmath/jsMath.js
? javascript/jsmath/plugins/CHMmode.js
? javascript/jsmath/plugins/autoload.js
? javascript/jsmath/plugins/global.js
? javascript/jsmath/plugins/mimeTeX.js
? javascript/jsmath/plugins/noCache.js
? javascript/jsmath/plugins/noGlobal.js
? javascript/jsmath/plugins/noImageFonts.js
? javascript/jsmath/plugins/smallFonts.js
? javascript/jsmath/plugins/spriteImageFonts.js
? javascript/jsmath/plugins/tex2math.js
? javascript/jsmath/uncompressed/def.js
? javascript/jsmath/uncompressed/font.js
? javascript/jsmath/uncompressed/jsMath-fallback-mac.js
? javascript/jsmath/uncompressed/jsMath-fallback-pc.js
? javascript/jsmath/uncompressed/jsMath-fallback-symbols.js
? javascript/jsmath/uncompressed/jsMath-fallback-unix.js
? javascript/jsmath/uncompressed/jsMath.js
? magma/ell_padic/examples.m
? magma/ell_padic/gl2.m
? magma/ell_padic/kedlaya.m
? magma/ell_padic/myl.m
? magma/ell_padic/padic_height.m
? magma/ell_padic/shark.m
? magma/padic_height/kedlaya.m
? magma/padic_height/padic_height.m
? magma/stoll/polys
? notebook/javascript/highlight/prettify.css
? notebook/templates/login.template~
? octave/user/a.png
? octave/user/octave-core
? pari/.DS_Store
? pari/dokchitser/.DS_Store
? sage-push~
```




---

Comment by mabshoff created at 2007-12-18 10:34:58

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-12-18 10:34:58

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-12-20 22:30:09

The problem has been fixed before 2.9.1.alph1:

```
extcode-2.9.1.alpha1$ hg status
extcode-2.9.1.alpha1$
```


Cheers,

Michael


---

Comment by rlm created at 2007-12-20 23:25:03

Resolution: worksforme
