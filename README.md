zookeeper
=========

![](http://zookeeper.apache.org/images/zookeeper_small.gif)

Installs and configures Apache ZooKeeper.

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://github.com/qubell-bazaar/component-zookeeper/raw/master/meta.yml)

Features
--------

 - Install and configure ZooKeeper on multiple compute

Configurations
--------------
 - ZooKeeper 3.4.5 (latest), CentOS 6.4 (us-east-1/ami-eb6b0182), AWS EC2 m1.small, root
 
Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
  - ZooKeeper distibution: ** (CentOS), ** (Ubuntu)
  - S3 bucket with Chef recipes: ** (TBD)
  - If Chef is not installed: ** (TBD)

Implementation notes
--------------------
 - Installation is based on Chef recipes from **

Example usage
-------------
**
