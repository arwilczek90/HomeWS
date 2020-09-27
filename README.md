# HomeWS
A home cloud controller for homelabs to replicate AWS services.

## Why?
I like the idea of having a home datacenter. I've run into too many limitations with proxmox and openstack and said, I wish I had aws but at home. 

## Goals
* Small enough to run on minipcs but powerful enough to run an entire Rack of servers.
* Atleast 1 host configuration
* Runs on any linux
* Simple boot 
* New hardware adoption to allow new nodes to associate and leave at will to support people who turn hardware off.
* AWS compatible API for terraforming
* Support for different sized nodes because homelabs are usually a combination of old hardware.
* node local storage for api data, this makes shutting down nodes easier because you can shut down a node and everything on it goes down too.


## Service Support Goals
- [ ] Dashboard
- [ ] IAM
- [ ] ebs <- Going to follow in openebs's footsteps on this one and use iscsi + zfs.
- [ ] lambda
- [ ] s3 <- Object storage on a specified "ebs" volume
- [ ] ec2 <- KVM ec2 adapter
- [ ] EKS <- kubernetes running on a hidden kvm instance on the master node
- [ ] SQS
- [ ] SNS
- [ ] ElasticTranscoder <- run transcode jobs on the master using ffmpeg
- [ ] dynamo (maybe just run localdynamodb backed by block store under the hood.)

## Extras
- Configuration settings both api and console


## Supporting Tools
* iscsi
* zfs
* KVM

