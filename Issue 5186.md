# Issue 5186: mpir build-time CPU detection fails in kvm/qemu amd64 virtual machine

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2009-02-05 08:39:01

Assignee: mabshoff

When building the mpir shipped with sage 3.3.alpha5 on a kvm/qemu amd64 virtual machine I get a 32-bit libgmp.so.


```
[root`@`localhost src]# bash config.guess
athlon-unknown-linux-gnu
[root`@`localhost src]# bash configfsf.guess
x86_64-unknown-linux-gnu
```


config.log and cpuinfo available at:

```
http://www.math.leidenuniv.nl/~wpalenst/sage/kvm_amd64_config.log
http://www.math.leidenuniv.nl/~wpalenst/sage/kvm_amd64_cpuinfo
```



---

Comment by mabshoff created at 2009-02-05 08:42:43

For the record from the above urls:

```
processor	: 0
vendor_id	: AuthenticAMD
cpu family	: 6
model		: 2
model name	: QEMU Virtual CPU version 0.9.1
stepping	: 3
cpu MHz		: 2411.119
cache size	: 512 KB
fpu		: yes
fpu_exception	: yes
cpuid level	: 2
wp		: yes
flags		: fpu de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx lm up pni
bogomips	: 4828.63
TLB size	: 1024 4K pages
clflush size	: 64
cache_alignment	: 64
address sizes	: 40 bits physical, 48 bits virtual
power management:
```

and

```
[root`@`localhost src]# bash config.guess
athlon-unknown-linux-gnu
[root`@`localhost src]# bash configfsf.guess
x86_64-unknown-linux-gnu
```


Cheers,

Michael


---

Comment by wjp created at 2010-01-17 02:10:21

Resolution: fixed


---

Comment by wjp created at 2010-01-17 02:10:21

This has been fixed in the meantime.
