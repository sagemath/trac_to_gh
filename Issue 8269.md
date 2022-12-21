# Issue 8269: cygwin: maxima does not build on cygwin due to ECL bug.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-15 06:56:48

Assignee: tbd

CC:  jdemeyer

Trying to build the maxima-5.20.1.spkg fails on Cygwin.  The error is


```
;;; Loading "/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1/src/src/binary-ecl/init-cl.fas"
;  - Providing system maxima
An error occurred during initialization:
C::BUILDER does not accept a file "binary-ecl/init-cl.fas" of kind :FASL.
```


See this possibly very relevant thread for a discussion about this: http://groups.google.com/group/sage-devel/browse_thread/thread/cecd40138ed552b9




---

Comment by was created at 2010-02-15 18:44:19

Even after upgrading to the latested released ECL (10.2.1), 

      http://wstein.org/home/wstein/ports/cygwin/ecl-10.2.1.spkg

we still have:

```
;;;   gcc -o "/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1/src/src/binary-ecl/init-cl.fas" -L"/home/wstein/build/sage-4.3.3.alpha0/local/lib/" "/cygdrive/c/WINDOWS/TEMP/ECLINITzVlCF0.o" "/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1/src/src/binary-ecl/init-cl.o"   -shared  -L/home/wstein/build/sage-4.3.3.alpha0/local/lib  -L/home/wstein/build/sage-4.3.3.alpha0/local/lib  -lecl  -lgmp -lgc   -lm
;      - Loading binary file "binary-ecl/init-cl.fas"
;;; Loading "/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1/src/src/binary-ecl/init-cl.fas"
;  - Providing system maxima
An error occurred during initialization:
C::BUILDER does not accept a file "binary-ecl/init-cl.fas" of kind :FASL.
make[1]: *** [binary-ecl/maxima] Error 1
make[1]: Leaving directory `/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1/src/src'
make: *** [all-recursive] Error 1
```



---

Comment by was created at 2010-02-20 23:28:25

Juan-Jose had the following suggestion:

```
It is no wonder Maxima does not build in Cygwin. Someone had introduced, who knows why, different build commands for that platform in maxima.system. The offending function looks as follows (maxima/src/maxima.system)

#+ecl
(defun build-maxima-lib ()
  (labels ((list-all-objects (module)
             (if (eql (mk::component-type module) :file)
         (list (mk::component-full-pathname module :binary))
         (apply #'append (mapcar #'list-all-objects (mk::component-components module))))))
    (let* ((files (list-all-objects (mk:find-system 'maxima))))
      #+msvc
      (progn
         (c::build-static-library "binary-ecl/maxima-lib" :lisp-files (print files))
         (let ((c::*ld-format* (concatenate 'string c::*ld-format* " /LIBPATH:binary-ecl")))
           (c::build-fasl "binary-ecl/maxima" :lisp-files '(maxima-lib))))
      #+cygwin
      (c::build-fasl "binary-ecl/maxima" :lisp-files files)
      #-(or cygwin msvc)
      (let ((obj (mapcar #'(lambda (p)
                 ;; Convert dir/foo.fas to dir/foo.o
                 (make-pathname :type "o" :defaults p))
             files)))
   [.... ]

It is immediately obvious that the code for cygwin is too short to do anything useful. A possible fix is to remove the line #+cygwin and the following line and change #-(or cygwin msvc) to #-msvc However I can not guarantee that there are no other problems left.

Please note that this is not directly related to ECL.

Juanjo
```


I tried this with the following new spkg:

   http://wstein.org/home/wstein/ports/cygwin/maxima-5.20.1.p1.spkg
and it now fails as follows:

```
;;; Note: Invoking external command:
;;;   gcc "-I/home/wstein/build/sage-4.3.3.alpha0/local/include/"  -I/home/wstein/build/sage-4.3.3.alpha0/local/include  -O2  -g  -Wall    -Dcygwin -O -w -c "/cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.c" -o "/cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.o"
gcc: /cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.o: No such file or directory
An error occurred during initialization:
(SYSTEM "gcc -o \"/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1.p1/src/src/binary-ecl/numerical/slatec/dbesj0.fas\" -L\"/home/wstein/build/sage-4.3.3.alpha0/local/lib/\" \"/cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.o\" \"/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1.p1/src/src/binary-ecl/numerical/slatec/dbesj0.o\"   -shared  -L/home/wstein/build/sage-4.3.3.alpha0/local/lib  -L/home/wstein/build/sage-4.3.3.alpha0/local/lib  -lecl  -lgmp -lgc   -lm ") returned non-zero value 1.
;;; Note: Invoking external command:
;;;   gcc -o "/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1.p1/src/src/binary-ecl/numerical/slatec/dbesj0.fas" -L"/home/wstein/build/sage-4.3.3.alpha0/local/lib/" "/cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.o" "/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1.p1/src/src/binary-ecl/numerical/slatec/dbesj0.o"   -shared  -L/home/wstein/build/sage-4.3.3.alpha0/local/lib  -L/home/wstein/build/sage-4.3.3.alpha0/local/lib  -lecl  -lgmp -lgc   -lm make[1]: *** [binary-ecl/maxima] Error 1
make[1]: Leaving directory `/home/wstein/build/sage-4.3.3.alpha0/spkg/build/maxima-5.20.1.p1/src/src'
make: *** [all-recursive] Error 1
```


The failure happens during the "make" step.


---

Comment by was created at 2010-02-20 23:42:03

continuing...

```

I tried typing the above gcc line in directly and it seems to work fine:

sage subshell$  gcc "-I/home/wstein/build/sage-4.3.3.alpha0/local/include/"  -I/home/wstein/build/sage-4.3.3.alpha0/local/include  -O2  -g  -Wall    -Dcygwin -O -w -c "/cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.c" -o "/cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.o"
/home/wstein/build/sage-4.3.3.alpha0
sage subshell$ ls -lh /cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.o
-rw-r--r--+ 1 wstein None 15K 2010-02-20 15:29 /cygdrive/c/WINDOWS/TEMP/ECLINIT5NW89S.o
/home/wstein/build/sage-4.3.3.alpha0

Then I typed "make" again, and *amazingly*, Maxima builds.  That was a surprise. 

sage subshell$ binary-ecl/maxima.exe
;;; Loading #P"/home/wstein/build/sage-4.3.3.alpha0/local/lib/ecl/DEFSYSTEM.fas"
;;; Loading #P"/home/wstein/build/sage-4.3.3.alpha0/local/lib/ecl/cmp.fas"
;;; Loading #P"/home/wstein/build/sage-4.3.3.alpha0/local/lib/ecl/sysfun.lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) integrate(sin(x^2),x)
;
                                             (sqrt(2) %i + sqrt(2)) x
(%o1) (sqrt(%pi) ((sqrt(2) %i + sqrt(2)) erf(------------------------)
                                                        2
                                                  (sqrt(2) %i - sqrt(2)) x
                     + (sqrt(2) %i - sqrt(2)) erf(------------------------)))/8
                                                             2


----------

So any ideas about this?  I'm just curious if this happens for other people too.
```



---

Comment by mhansen created at 2010-03-13 07:16:08

I was able to get Maxima to build in Cygwin with ECL 10.3.1 and the spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/maxima-5.20.1.p0.spkg . Everything builds correctly except building maxima as a library at the end:


```
cd src
echo "building Maxima as an ecl library"
ecl -eval "(require 'asdf)" -eval '(load "maxima-build.lisp")' -eval  '(asdf:make-build :maxima :type :fasl)' -eval "(quit)"
ECLLIB=`ecl -eval "(princ (SI:GET-LIBRARY-PATHNAME))" -eval "(quit)"`
echo
echo "installing Maxima library as $ECLLIB/maxima.fas"
cp maxima.fasb $ECLLIB/maxima.fas
cd ..
```


All of the building commands run correctly, but there is no "maxima.fasb" file produced.


---

Comment by mhansen created at 2010-04-27 17:35:35

This can be fixed by using ECL from #8645 and Maxima from #8645 or #8731


---

Comment by kcrisman created at 2011-06-16 14:27:39

Mike, this one should be closed, right?  Note that in the mean time #11502 and #11260 seem to have raised different issues... aargh.


---

Comment by kcrisman created at 2011-06-26 03:34:52

Although Maxima continue to not build consistently on Cygwin, neither on XP nor Win7, this bug is now vague and old enough that we should go to the more current tickets mentioned in the previous comment, which have information relevant to more current spkgs.  In addition, it appears there was a fix of some kind which is now invalid due to other reasons, so this is really just too confusing now.

To release manager: please close this ticket.


---

Comment by kcrisman created at 2011-06-26 03:34:52

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-26 03:34:59

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-07-22 17:22:18

Resolution: invalid
