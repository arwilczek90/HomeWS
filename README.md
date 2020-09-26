# HomeWS
A home cloud controller for homelabs to replicate AWS services.


## Goals
* Small enough to run on minipcs but powerful enough to run an entire Rack of servers.
* Atleast 1 host configuration
* Runs on any linux
* Simple boot 
* New hardware adoption to allow new nodes to associate and leave at will to support people who turn hardware off.
* AWS compatible API for terraforming


## Service Support Goals
[ ] Dashboard
[ ] IAM
[ ] ebs <- Going to follow in openebs's footsteps on this one and use iscsi.
[ ] lambda
[ ] s3
[ ] ec2
[ ] EKS
[ ] SQS
[ ] SNS
[ ] ElasticTranscoder
[ ] elasticache
[ ] dynamo (maybe just run localdynamodb backed by block store under the hood.)


## Supporting Tools
* iscsi
* KVM

