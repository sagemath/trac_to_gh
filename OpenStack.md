# OpenStack

TODO: Fill in more useful information here.  For now I'm just dumping some notes here:

```
docker-machine create -d openstack
    --openstack-domain-name=stratuslab \
    --openstack-username=embray --openstack-password=******** \
    --openstack-auth-url=https://keystone.lal.in2p3.fr:5000/v3 \
    --openstack-flavor-name=os.4 --openstack-image-name=debian-9.4-20180319 \
    --openstack-tenant-id=d593d7819b6f42d09a5f89339cdfcfc5 \
    --openstack-region=lal --openstack-insecure \
    --openstack-ssh-user=debian --engine-storage-driver=overlay2
```