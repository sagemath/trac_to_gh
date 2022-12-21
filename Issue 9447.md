# Issue 9447: "except:" count in sage too high

Issue created by migration from Trac.

Original creator: wjlaffin

Original creation time: 2010-07-07 09:48:31

Assignee: AlexGhitza

sage: len(search_src("except:",interact=False).splitlines())
312


This number should be much lower.


---

Comment by wjlaffin created at 2010-07-07 10:04:17

Changing assignee from AlexGhitza to jason.


---

Comment by wjlaffin created at 2010-07-07 10:04:17

Changing component from algebra to misc.


---

Comment by tscrim created at 2013-04-01 19:53:22

These all seem to be gone in `5.9.beta1`:

```
travis`@`travis-virtualbox:~/sage-5.9.beta1/devel/sage-main/sage$ grep -R "except:" .
./numerical/backends/glpk_backend.cpp:            /*except:*/ {
./structure/list_clone_timings_cy.c:        /*except:*/ {
./plot/plot3d/bugs.txt:        except:       # TODO -- this would catch control-C,etc. -- FIX THIS TO CATCH WHAT IS RAISED!!!!
./libs/singular/function.cpp:        /*except:*/ {

sage: len(search_src("except:",interact=False).splitlines())
0
```



---

Comment by tscrim created at 2013-04-01 19:53:22

Changing status from new to needs_review.


---

Comment by novoselt created at 2013-04-02 06:12:50

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-03 15:12:26

Resolution: worksforme
