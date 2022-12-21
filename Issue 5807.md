# Issue 5807: dsage with @parallel doesn't work at all

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-17 01:27:50

Assignee: yi

I tried to use dsage with the `@`parallel directory and sage-3.4, and it's 100% broken.  The log just spews forever:

```

2009-04-16 18:25:05-0700 [-] [Worker: 0] Restarting...
2009-04-16 18:25:05-0700 [-] [Worker 0] Started...
2009-04-16 18:25:05-0700 [-] [Worker 1] Job vISI9r9Dzs failed!
2009-04-16 18:25:05-0700 [-] Traceback: 
         execfile('/scratch/wstein/sage/dsage/tmp_worker_files/vISI9r9Dzs/f.py')
        re
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "/scratch/wstein/sage/dsage/tmp_worker_files/vISI9r9Dzs/f.py", line 8, in <module>
            f = unpickle_function(p_f)
        NameError: name 'p_f' is not defined

2009-04-16 18:25:05-0700 [-] [Worker: 1] Restarting...
2009-04-16 18:25:05-0700 [-] [Worker 1] Started...
2009-04-16 18:25:05-0700 [Broker,client] [Worker 0] Starting job 5pzNNCImcd 
2009-04-16 18:25:05-0700 [Broker,client] [Worker 1] Starting job vISI9r9Dzs 
```


Using `@`parallel and multiprocessing for what I want to do (just some simple no-pexpect C library stuff involving modular symbols) doesn't work either, since I get weird pari_trap error exceptions.

It is so sad, that after all these years and all this work to write code to run things in parallel, that even the most trivial basic thing that I would like to do in parallel, which is evaluate a function on a bunch of integer inputs, still doesn't work robustly.


---

Comment by was created at 2010-01-18 12:48:01

Note that dsage is so broken that it isn't even possible to test this out.  See #7975.


---

Comment by was created at 2010-01-19 07:41:26

Dsage is now deprecated.


---

Comment by was created at 2010-01-19 07:41:26

Resolution: wontfix
