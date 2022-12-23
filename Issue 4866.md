# Issue 4866: hermes optional spkg totally broken in multiple ways

Issue created by migration from https://trac.sagemath.org/ticket/4866

Original creator: was

Original creation time: 2008-12-24 05:39:45

Assignee: mabshoff

The optional Hermes fails to install in any meaningful sense on both Linux 64-bit and OS X.  Maybe it's a binary -- I don't know.  Whatever it is, it should fail very gracefully on systems where it isn't supposed to work, and print a message saying "sorry, this is a binary for only XXX system."  

I'm unconvinced about the value of us hosting such binaries in the official optional spkg repo, by the way. 

On Linux (64-bit Sage.math):

```
sage: install_package('hermes-0.9.4-linux')
Force installing hermes-0.9.4-linux
Calling sage-spkg on hermes-0.9.4-linux
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
hermes-0.9.4-linux
Machine:
Linux sage 2.6.24-19-server #1 SMP Wed Aug 20 18:43:06 UTC 2008 x86_64 GNU/Linux
Deleting directories from past builds of previous/current versions of hermes-0.9.4-linux
Extracting package /usr/local/sage/spkg/optional/hermes-0.9.4-linux.spkg ...
-rw-r--r-- 1 root root 570854 2008-12-23 20:40 /usr/local/sage/spkg/optional/hermes-0.9.4-linux.spkg
hermes-0.9.4-linux/
hermes-0.9.4-linux/seed
hermes-0.9.4-linux/article.pub.xml
hermes-0.9.4-linux/hermes.l
hermes-0.9.4-linux/hermes.y
hermes-0.9.4-linux/article.s.aux
hermes-0.9.4-linux/article.s.dvi
hermes-0.9.4-linux/article.s.log
hermes-0.9.4-linux/article.s.tex
hermes-0.9.4-linux/dlt.tex
hermes-0.9.4-linux/ctop.xsl
hermes-0.9.4-linux/content.pub.xml
hermes-0.9.4-linux/article.lib.xml
hermes-0.9.4-linux/index.html
hermes-0.9.4-linux/makefile
hermes-0.9.4-linux/pmathmlcss.xsl
hermes-0.9.4-linux/lex.yy.c
hermes-0.9.4-linux/article.tex
hermes-0.9.4-linux/hermes
hermes-0.9.4-linux/content.lib.xml
hermes-0.9.4-linux/SAGE.txt
hermes-0.9.4-linux/pmathml.xsl
hermes-0.9.4-linux/content.tex
hermes-0.9.4-linux/seed.c
hermes-0.9.4-linux/content.s.aux
hermes-0.9.4-linux/content.s.dvi
hermes-0.9.4-linux/content.s.log
hermes-0.9.4-linux/content.s.tex
hermes-0.9.4-linux/pub.patch
hermes-0.9.4-linux/spkg-install
hermes-0.9.4-linux/hermes.tab.c
hermes-0.9.4-linux/hermes.tab.h
hermes-0.9.4-linux/mathml.xsl
hermes-0.9.4-linux/pub.xslt
Finished extraction
****************************************************
Host system
uname -a:
Linux sage 2.6.24-19-server #1 SMP Wed Aug 20 18:43:06 UTC 2008 x86_64 GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu3)
****************************************************
Building and installing hermes
latex content.s
This is pdfTeXk, Version 3.141592-1.40.3 (Web2C 7.5.6)
 %&-line parsing enabled.
entering extended mode
(./content.s.tex
LaTeX2e <2005/12/01>
Babel <v3.8h> and hyphenation patterns for english, usenglishmax, dumylang, noh
yphenation, croatian, ukrainian, russian, bulgarian, czech, slovak, danish, dut
ch, finnish, basque, french, german, ngerman, ibycus, greek, monogreek, ancient
greek, hungarian, italian, latin, mongolian, norsk, icelandic, interlingua, tur
kish, coptic, romanian, welsh, serbian, slovenian, estonian, esperanto, upperso
rbian, indonesian, polish, portuguese, spanish, catalan, galician, swedish, loa
ded.
(/usr/share/texmf-texlive/tex/latex/base/article.cls
Document Class: article 2005/09/16 v1.4f Standard LaTeX document class
(/usr/share/texmf-texlive/tex/latex/base/size10.clo)) (./dlt.tex)
(/usr/share/texmf-texlive/tex/latex/amsfonts/amsfonts.sty) (./content.s.aux)
(/usr/share/texmf-texlive/tex/latex/amsfonts/umsa.fd)
(/usr/share/texmf-texlive/tex/latex/amsfonts/umsb.fd) [1] [2] [3] [4] [5]
[6] [7] [8] [9] [10] [11] [12] [13] [14] (./content.s.aux) )
Output written on content.s.dvi (14 pages, 18936 bytes).
Transcript written on content.s.log.
./hermes content.s.dvi >content.lib.xml
/bin/sh: ./hermes: not found
make: *** [xml] Error 127
Error building Hermes

real	0m0.047s
user	0m0.030s
sys	0m0.010s
sage: An error occurred while installing hermes-0.9.4-linux
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /usr/local/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/usr/local/sage/spkg/build/hermes-0.9.4-linux and type 'make'.
Instead type "/usr/local/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/usr/local/sage/spkg/build/hermes-0.9.4-linux
(When you are done debugging, you can type "exit" to leave the
subshell.)

```


On OS X:

```
Last login: Tue Dec 23 20:48:37 on ttys005
teragon-2:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: install_package('hermes-0.9.4-linux')
Force installing hermes-0.9.4-linux
Calling sage-spkg on hermes-0.9.4-linux
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
hermes-0.9.4-linux
Machine:
Darwin teragon-2.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386
Deleting directories from past builds of previous/current versions of hermes-0.9.4-linux
/Users/wstein/sage/local/bin/sage-spkg: file hermes-0.9.4-linux does not exist
Attempting to download it.
http://www.sagemath.org//packages/optional/hermes-0.9.4-linux.spkg --> hermes-0.9.4-linux.spkg
[..................................................]
Extracting package /Users/wstein/sage/spkg/optional/hermes-0.9.4-linux.spkg ...
-rw-r--r--  1 wstein  staff  570854 Dec 23 21:32 /Users/wstein/sage/spkg/optional/hermes-0.9.4-linux.spkg
hermes-0.9.4-linux/
hermes-0.9.4-linux/seed
hermes-0.9.4-linux/article.pub.xml
hermes-0.9.4-linux/hermes.l
hermes-0.9.4-linux/hermes.y
hermes-0.9.4-linux/article.s.aux
hermes-0.9.4-linux/article.s.dvi
hermes-0.9.4-linux/article.s.log
hermes-0.9.4-linux/article.s.tex
hermes-0.9.4-linux/dlt.tex
hermes-0.9.4-linux/ctop.xsl
hermes-0.9.4-linux/content.pub.xml
hermes-0.9.4-linux/article.lib.xml
hermes-0.9.4-linux/index.html
hermes-0.9.4-linux/makefile
hermes-0.9.4-linux/pmathmlcss.xsl
hermes-0.9.4-linux/lex.yy.c
hermes-0.9.4-linux/article.tex
hermes-0.9.4-linux/hermes
hermes-0.9.4-linux/content.lib.xml
hermes-0.9.4-linux/SAGE.txt
hermes-0.9.4-linux/pmathml.xsl
hermes-0.9.4-linux/content.tex
hermes-0.9.4-linux/seed.c
hermes-0.9.4-linux/content.s.aux
hermes-0.9.4-linux/content.s.dvi
hermes-0.9.4-linux/content.s.log
hermes-0.9.4-linux/content.s.tex
hermes-0.9.4-linux/pub.patch
hermes-0.9.4-linux/spkg-install
hermes-0.9.4-linux/hermes.tab.c
hermes-0.9.4-linux/hermes.tab.h
hermes-0.9.4-linux/mathml.xsl
hermes-0.9.4-linux/pub.xslt
Finished extraction
****************************************************
Host system
uname -a:
Darwin teragon-2.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin9
Configured with: /var/tmp/gcc/gcc-5488~2/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=i686-apple-darwin9 --with-arch=apple --with-tune=generic --host=i686-apple-darwin9 --target=i686-apple-darwin9
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5488)
****************************************************
Building and installing hermes
latex content.s
./seed article.tex
./seed: ./seed: cannot execute binary file
make: *** [article] Error 126
make: *** Waiting for unfinished jobs....
This is pdfTeXk, Version 3.1415926-1.40.9 (Web2C 7.5.7)
 %&-line parsing enabled.
entering extended mode
(./content.s.tex
LaTeX2e <2005/12/01>
Babel <v3.8l> and hyphenation patterns for english, usenglishmax, dumylang, noh
yphenation, german-x-2008-06-18, ngerman-x-2008-06-18, ancientgreek, ibycus, ar
abic, basque, bulgarian, catalan, pinyin, coptic, croatian, czech, danish, dutc
h, esperanto, estonian, farsi, finnish, french, galician, german, ngerman, mono
greek, greek, hungarian, icelandic, indonesian, interlingua, irish, italian, la
tin, mongolian, mongolian2a, bokmal, nynorsk, polish, portuguese, romanian, rus
sian, sanskrit, serbian, slovak, slovenian, spanish, swedish, turkish, ukenglis
h, ukrainian, uppersorbian, welsh, loaded.
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/article.cls
Document Class: article 2005/09/16 v1.4f Standard LaTeX document class
(/usr/local/texlive/2008/texmf-dist/tex/latex/base/size10.clo)) (./dlt.tex)
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/amsfonts.sty)
(./content.s.aux)
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/local/texlive/2008/texmf-dist/tex/latex/amsfonts/umsb.fd) [1] [2]
[3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] (./content.s.aux) )
Output written on content.s.dvi (14 pages, 18936 bytes).
Transcript written on content.s.log.
./hermes content.s.dvi >content.lib.xml
/bin/sh: ./hermes: cannot execute binary file
make: *** [xml] Error 126
Error building Hermes
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
real	0m1.278s
user	0m0.214s
sys	0m0.122s
sage: An error occurred while installing hermes-0.9.4-linux
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wstein/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/wstein/sage/spkg/build/hermes-0.9.4-linux and type 'make'.
Instead type "/Users/wstein/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/wstein/sage/spkg/build/hermes-0.9.4-linux
(When you are done debugging, you can type "exit" to leave the
subshell.)
```



---

Comment by chapoton created at 2013-08-20 18:03:01

the package hermes is now an archived package. This ticket can maybe be closed as invalid ?


---

Comment by chapoton created at 2013-08-20 18:03:01

Changing status from new to needs_review.


---

Comment by chapoton created at 2013-08-21 08:42:02

Let us close this either as invalid or as wontfix.


---

Comment by chapoton created at 2013-08-21 08:42:02

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-08-30 08:43:08

Resolution: invalid
