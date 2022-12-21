# Issue 2137: implement loading of pyx files when loading .sage files (probably relatively easy; in sage/misc/*)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-10 06:38:47

Assignee: was

CC:  mvngu


```


On Feb 9, 2008 7:58 PM, mb <bestvina`@`gmail.com> wrote:
> 
> Hello,
> 
> I have a basic question about using pyrex from a sage script. Suppose
> I have a file "test.pyx":
> 
> def f(int n):
>         return n
> 
> Then from the sage interpreter I can use it:
> 
> sage: load "test.pyx"
> Compiling test.pyx...
> sage: f(3)
> 3
> 
> But I'd like to use it from a script, e.g. "main.sage":
> 
> load "test.pyx"
> print f(3)
> 
> Then I get:
> 
> mb`@`hvar:~$ sage main.sage
> Traceback (most recent call last):
>   File "main.py", line 4, in <module>
>     print f(Integer(3))
> NameError: name 'f' is not defined
> 
> I tried modifying test.pyx by inserting the word "public" after "def"
> but it didn't help. Is there any way of doing this?

This is not implemented yet, though it will be implemented.   
There is a partial workaround that might be enough for you now.

(1) Create test.pyx and main.sage as follows:
teragon:tmp was$ more test.pyx
def f(int n):
    return n
teragon:tmp was$ more main.sage
print f(3)

(2) You can use main.sage if you do the following:
sage: load test.pyx
Compiling test.pyx...
sage: load main.sage
3

William
```



---

Comment by AlexGhitza created at 2009-01-23 07:10:11

Changing type from defect to enhancement.


---

Comment by mpatel created at 2010-02-14 20:00:45

I think this is fixed, since the example in the description works for me:

```sh
$ sage main.sage 
Compiling test.pyx...
3
```


Should we close this ticket?


---

Comment by mpatel created at 2010-02-14 20:00:45

Changing status from new to needs_info.


---

Comment by mvngu created at 2010-02-15 06:50:53

Closing this ticket as fixed:

```
[mvngu`@`sage sage-4.3.3.alpha0]$ cat test.pyx
def f(int n):
    return n
[mvngu`@`sage sage-4.3.3.alpha0]$ cat main.sage
load("test.pyx")
print f(3)
[mvngu`@`sage sage-4.3.3.alpha0]$ ./sage -version
* Warning: this is a prerelease version, and it may be unstable.     *
[mvngu`@`sage sage-4.3.3.alpha0]$ ./sage main.sage
Compiling test.pyx...
3
```



---

Comment by mvngu created at 2010-02-15 06:50:53

Resolution: fixed
