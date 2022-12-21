# Issue 5628: a little sage-flags.txt issue

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-29 03:29:59

Assignee: was


```
On Sat, Mar 28, 2009 at 9:05 PM, Gonzalo Tornaria:
>
> I did an upgrade from 3.4 as follows:
>
> 1. sage -br main  ---> switch to main, which is CLEAN
> 2. sage -upgrade
> http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.1/sage-3.4.1.alpha0
> 3. once that was finished, I pulled  the new changes into my sage-brandt branch
> 4. applied the rebased 5520 + my tiny patch
> 5. sage -br brandt
>
> But now, "sage -br main" (which is now clean 3.4.1.alpha0) causes the
> same issue.
>
> Gonzalo

Just delete 
   local/lib/sage-flags.txt

Also, I've opened a blocker ticket about this, since everybody who upgrades will run into exactly the same problem.  

The problem is that the new version of the script that checks the flags doesn't see sse4_1 anymore (nothing in Sage specifically uses that), but it's still in your old sage-flags.txt file.  Two possible solutions:
   (1) delete sage-flags.txt as part of "sage -upgrade"
   (2) make it so sse4_1 is specifically ignored.

I like (1). 
```



---

Attachment


---

Comment by tornaria created at 2009-03-29 04:51:42

The issue with this patch is that the `sage-flags.txt` file will not be regenerated unless sage install directory changes (because `write_flags_file()` is only called from within `install_moved()`.

Maybe the flags file should also be created from the `check_processor_flags()` function. But then, this only works if sage is run at least once after an upgrade.

Otherwise, doing `sage -upgrade` followed by `sage -bdist` ends up with a sage binary with no `sage-flags.txt`, defeating the purpose of the flags file.


---

Comment by tornaria created at 2009-03-29 04:54:40

I have an alternative fix:

```
diff -r 804879ae0134 sage-location
--- a/sage-location     Thu Mar 26 16:43:48 2009 -0700
+++ b/sage-location     Sat Mar 28 22:32:50 2009 -0700
`@``@` -77,7 +77,7 `@``@`
     if not os.path.exists(flags_file): return
     # We check that the processor flags of the original build are a
     # subset of the new machine.  If not, we print a massive warning.
-    X = set(open(flags_file).read().split())
+    X = set(open(flags_file).read().split()).intersection(FLAGS)
     Y = set(get_flags_info().split())
     if not X.issubset(Y):
         print ""
```


This makes it so that only the flags listed in FLAGS are relevant for `check_processor_flags()`. Thus, after an upgrade, the flag `sse4_1` will still be in the flags file, but it won't be required at runtime.


---

Comment by mabshoff created at 2009-04-06 00:54:15

I actually like Gonzalo's fix better than William's - not sure what to do about this yet.

Cheers,

Michael


---

Comment by was created at 2009-04-06 17:24:54

I'm fine with either version.


---

Comment by mabshoff created at 2009-04-06 18:33:33

This is a 3.4.1 blocker.

Cheers,

Michael


---

Attachment

Positive review for trac_5628.patch. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 01:49:58

Resolution: fixed


---

Comment by mabshoff created at 2009-04-11 01:49:58

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
