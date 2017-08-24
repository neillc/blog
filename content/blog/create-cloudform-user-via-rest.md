Title: Creating a CloudForms user via the REST API
Slug: Creating a CloudForms user via the REST API
Date: 2017-08-22 19:00
Category: CloudForms

CloudForms is a bit of a pain to setup. We're looking to automate as much as possible, but CF would like us to do things through menus or its web interface. The most irritating part of this is that I haven't been able to find a way to stand up a CF instance except by ssh'ing in an running the appliance_console script and then manually going through the configuration options to create a database.  I did consider using Ansible's expect module but my co-workers talked me down from that ledge.

Slightly better news is that CF seems to expose a lot of its functionality through a REST API.  I haven't explored too much of this yet, but here's a little example of using curl to add a new user:

    curl -k --user admin:smartvm -X POST -d '{"name":"neill", "group":{"id":"3000000000002"}, "userid":"neill", "password":"smartvm"}' https://127.0.0.1:8443/api/users | jq

