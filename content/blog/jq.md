Title: jq - a lightweight and flexible command-line JSON processor.
Date: 2017-08-22 09:30
Category: JSON


My current job (as of all things a "Cloud Architect") means I spend a lot of 
time poking at things that like to talk JSON. Much as I prefer JSON to other
data interchange formats (e.g. YAML - I'm looking at you Ansible)[1] it's 
still not a particularly friendly thing to read when it comes at you as a wall
of text.

In the past I've written one liners in Python to pretty print the results, but
I keep forgetting to save them somewhere sensible and then I have to remember
the syntax.

Today, needing to do this again I decided to just use the other exo-brain,
Stack Overflow, and googled for "python json pretty print one liner". I did
indeed find a one liner, but also a link to jq which the poster suggested might
be a better alternative.

Turns out that [jq](https://stedolan.github.io/jq/) is installable as a 
package on Fedora so now instead of dragging my sad one liner around I can 
just:

dnf install jq

and then something like:

    curl -k --user admin:smartvm https://127.0.0.1:8443/api/ 

Which used to result in:

    {"name":"API","description":"REST API","version":"2.4.0","versions":[{"name":"2.4.0","href":"https://127.0.0.1:8443/api/v2.4.0"}],"settings":{"locale":"en","asynchronous_notifications":true},"identity":{"userid":"admin","name":"Administrator","user_href":"https://127.0.0.1:8443/api/users/1","group":"EvmGroup-super_administrator","group_href":"https://127.0.0.1:8443/api/groups/2","role":"EvmRole-super_administrator","role_href":"https://127.0.0.1:8443/api/roles/1","tenant":"My Company","groups":["EvmGroup-super_administrator"]},"server_info":{"version":"fine-3","build":"20170821012821_09b4f87","appliance":"EVM","server_href":"https://127.0.0.1:8443/api/servers/1","zone_href":"https://127.0.0.1:8443/api/zones/1","region_href":"https://127.0.0.1:8443/api/regions/1"},"product_info":{"name":"ManageIQ","name_full":"ManageIQ","copyright":"Copyright (c) 2017 ManageIQ. Sponsored by Red Hat Inc.","support_website":"http://www.manageiq.org","support_website_text":"ManageIQ.org"},"collections":[{"name":"actions","href":"https://127.0.0.1:8443/api/actions","description":"Actions"},{"name":"alert_definitions","href":"https://127.0.0.1:8443/api/alert_definitions","description":"Alert Definitions"},{"name":"alerts","href":"https://127.0.0.1:8443/api/alerts","description":"Alerts"},{"name":"arbitration_profiles","href":"https://127.0.0.1:8443/api/arbitration_profiles","description":"Arbitration Profiles"},{"name":"arbitration_rules","href":"https://127.0.0.1:8443/api/arbitration_rules","description":"Arbitration Rules"},{"name":"arbitration_settings","href":"https://127.0.0.1:8443/api/arbitration_settings","description":"Arbitration Settings"},{"name":"authentications","href":"https://127.0.0.1:8443/api/authentications","description":"Authentications"},{"name":"automate","href":"https://127.0.0.1:8443/api/automate","description":"Automate"},{"name":"automate_domains","href":"https://127.0.0.1:8443/api/automate_domains","description":"Automate Domains"},{"name":"automation_requests","href":"https://127.0.0.1:8443/api/automation_requests","description":"Automation Requests"},{"name":"availability_zones","href":"https://127.0.0.1:8443/api/availability_zones","description":"Availability Zones"},{"name":"blueprints","href":"https://127.0.0.1:8443/api/blueprints","description":"Blueprints"},{"name":"categories","href":"https://127.0.0.1:8443/api/categories","description":"Categories"},{"name":"chargebacks","href":"https://127.0.0.1:8443/api/chargebacks","description":"Chargebacks"},{"name":"cloud_networks","href":"https://127.0.0.1:8443/api/cloud_networks","description":"Cloud Networks"},{"name":"cloud_tenants","href":"https://127.0.0.1:8443/api/cloud_tenants","description":"Cloud Tenants"},{"name":"cloud_volumes","href":"https://127.0.0.1:8443/api/cloud_volumes","description":"Cloud Volumes"},{"name":"clusters","href":"https://127.0.0.1:8443/api/clusters","description":"Clusters"},{"name":"conditions","href":"https://127.0.0.1:8443/api/conditions","description":"Conditions"},{"name":"configuration_script_payloads","href":"https://127.0.0.1:8443/api/configuration_script_payloads","description":"Configuration Script Payloads"},{"name":"configuration_script_sources","href":"https://127.0.0.1:8443/api/configuration_script_sources","description":"Configuration Script Source"},{"name":"container_deployments","href":"https://127.0.0.1:8443/api/container_deployments","description":"Container Provider Deployment"},{"name":"currencies","href":"https://127.0.0.1:8443/api/currencies","description":"Currencies"},{"name":"data_stores","href":"https://127.0.0.1:8443/api/data_stores","description":"Datastores"},{"name":"events","href":"https://127.0.0.1:8443/api/events","description":"Events"},{"name":"features","href":"https://127.0.0.1:8443/api/features","description":"Product Features"},{"name":"flavors","href":"https://127.0.0.1:8443/api/flavors","description":"Flavors"},{"name":"groups","href":"https://127.0.0.1:8443/api/groups","description":"Groups"},{"name":"hosts","href":"https://127.0.0.1:8443/api/hosts","description":"Hosts"},{"name":"instances","href":"https://127.0.0.1:8443/api/instances","description":"Instances"},{"name":"load_balancers","href":"https://127.0.0.1:8443/api/load_balancers","description":"Load Balancers"},{"name":"measures","href":"https://127.0.0.1:8443/api/measures","description":"Measures"},{"name":"notifications","href":"https://127.0.0.1:8443/api/notifications","description":"User's past notifications"},{"name":"orchestration_templates","href":"https://127.0.0.1:8443/api/orchestration_templates","description":"Orchestration Template"},{"name":"pictures","href":"https://127.0.0.1:8443/api/pictures","description":"Pictures"},{"name":"policies","href":"https://127.0.0.1:8443/api/policies","description":"Policies"},{"name":"policy_actions","href":"https://127.0.0.1:8443/api/policy_actions","description":"Actions"},{"name":"policy_profiles","href":"https://127.0.0.1:8443/api/policy_profiles","description":"Policy Profiles"},{"name":"providers","href":"https://127.0.0.1:8443/api/providers","description":"Providers"},{"name":"provision_dialogs","href":"https://127.0.0.1:8443/api/provision_dialogs","description":"Provisioning Dialogs"},{"name":"provision_requests","href":"https://127.0.0.1:8443/api/provision_requests","description":"Provision Requests"},{"name":"rates","href":"https://127.0.0.1:8443/api/rates","description":"Chargeback Rates"},{"name":"regions","href":"https://127.0.0.1:8443/api/regions","description":"Regions"},{"name":"reports","href":"https://127.0.0.1:8443/api/reports","description":"Reports"},{"name":"request_tasks","href":"https://127.0.0.1:8443/api/request_tasks","description":"Request Tasks"},{"name":"requests","href":"https://127.0.0.1:8443/api/requests","description":"Requests"},{"name":"resource_pools","href":"https://127.0.0.1:8443/api/resource_pools","description":"Resource Pools"},{"name":"results","href":"https://127.0.0.1:8443/api/results","description":"Report Results"},{"name":"roles","href":"https://127.0.0.1:8443/api/roles","description":"Roles"},{"name":"security_groups","href":"https://127.0.0.1:8443/api/security_groups","description":"Security Groups"},{"name":"servers","href":"https://127.0.0.1:8443/api/servers","description":"EVM Servers"},{"name":"service_catalogs","href":"https://127.0.0.1:8443/api/service_catalogs","description":"Service Catalogs"},{"name":"service_dialogs","href":"https://127.0.0.1:8443/api/service_dialogs","description":"Service Dialogs"},{"name":"service_orders","href":"https://127.0.0.1:8443/api/service_orders","description":"Service Orders"},{"name":"service_requests","href":"https://127.0.0.1:8443/api/service_requests","description":"Service Requests"},{"name":"service_templates","href":"https://127.0.0.1:8443/api/service_templates","description":"Service Templates"},{"name":"services","href":"https://127.0.0.1:8443/api/services","description":"Services"},{"name":"settings","href":"https://127.0.0.1:8443/api/settings","description":"Settings"},{"name":"tags","href":"https://127.0.0.1:8443/api/tags","description":"Tags"},{"name":"tasks","href":"https://127.0.0.1:8443/api/tasks","description":"Tasks"},{"name":"templates","href":"https://127.0.0.1:8443/api/templates","description":"Templates"},{"name":"tenants","href":"https://127.0.0.1:8443/api/tenants","description":"Tenants"},{"name":"users","href":"https://127.0.0.1:8443/api/users","description":"Users"},{"name":"virtual_templates","href":"https://127.0.0.1:8443/api/virtual_templates","description":"Virtual Templates"},{"name":"vms","href":"https://127.0.0.1:8443/api/vms","description":"Virtual Machines"},{"name":"zones","href":"https://127.0.0.1:8443/api/zones","description":"Zones"}]}

Becomes:

    curl -k --user admin:smartvm https://127.0.0.1:8443/api/ | jq

and produces:


      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100  7739    0  7739    0     0   9832      0 --:--:-- --:--:-- --:--:--  9833

    {
      "name": "API",
      "description": "REST API",
      "version": "2.4.0",
      "versions": [
        {
          "name": "2.4.0",
          "href": "https://127.0.0.1:8443/api/v2.4.0"
        }
      ],
      "settings": {
        "locale": "en",
        "asynchronous_notifications": true
      },
      "identity": {
        "userid": "admin",
        "name": "Administrator",
        "user_href": "https://127.0.0.1:8443/api/users/1",
        "group": "EvmGroup-super_administrator",
        "group_href": "https://127.0.0.1:8443/api/groups/2",
        "role": "EvmRole-super_administrator",
        "role_href": "https://127.0.0.1:8443/api/roles/1",
        "tenant": "My Company",
        "groups": [
          "EvmGroup-super_administrator"
        ]
      },
      "server_info": {
        "version": "fine-3",
        "build": "20170821012821_09b4f87",
        "appliance": "EVM",
        "server_href": "https://127.0.0.1:8443/api/servers/1",
        "zone_href": "https://127.0.0.1:8443/api/zones/1",
        "region_href": "https://127.0.0.1:8443/api/regions/1"
      },
      "product_info": {
        "name": "ManageIQ",
        "name_full": "ManageIQ",
        "copyright": "Copyright (c) 2017 ManageIQ. Sponsored by Red Hat Inc.",
        "support_website": "http://www.manageiq.org",
        "support_website_text": "ManageIQ.org"
      },
      "collections": [
        {
          "name": "actions",
          "href": "https://127.0.0.1:8443/api/actions",
          "description": "Actions"
        },
        {
          "name": "alert_definitions",
          "href": "https://127.0.0.1:8443/api/alert_definitions",
          "description": "Alert Definitions"
        },
        {
          "name": "alerts",
          "href": "https://127.0.0.1:8443/api/alerts",
          "description": "Alerts"
        },
        {
          "name": "arbitration_profiles",
          "href": "https://127.0.0.1:8443/api/arbitration_profiles",
          "description": "Arbitration Profiles"
        },
        {
          "name": "arbitration_rules",
          "href": "https://127.0.0.1:8443/api/arbitration_rules",
          "description": "Arbitration Rules"
        },
        {
          "name": "arbitration_settings",
          "href": "https://127.0.0.1:8443/api/arbitration_settings",
          "description": "Arbitration Settings"
        },
        {
          "name": "authentications",
          "href": "https://127.0.0.1:8443/api/authentications",
          "description": "Authentications"
        },
        {
          "name": "automate",
          "href": "https://127.0.0.1:8443/api/automate",
          "description": "Automate"
        },
        {
          "name": "automate_domains",
          "href": "https://127.0.0.1:8443/api/automate_domains",
          "description": "Automate Domains"
        },
        {
          "name": "automation_requests",
          "href": "https://127.0.0.1:8443/api/automation_requests",
          "description": "Automation Requests"
        },
        {
          "name": "availability_zones",
          "href": "https://127.0.0.1:8443/api/availability_zones",
          "description": "Availability Zones"
        },
        {
          "name": "blueprints",
          "href": "https://127.0.0.1:8443/api/blueprints",
          "description": "Blueprints"
        },
        {
          "name": "categories",
          "href": "https://127.0.0.1:8443/api/categories",
          "description": "Categories"
        },
        {
          "name": "chargebacks",
          "href": "https://127.0.0.1:8443/api/chargebacks",
          "description": "Chargebacks"
        },
        {
          "name": "cloud_networks",
          "href": "https://127.0.0.1:8443/api/cloud_networks",
          "description": "Cloud Networks"
        },
        {
          "name": "cloud_tenants",
          "href": "https://127.0.0.1:8443/api/cloud_tenants",
          "description": "Cloud Tenants"
        },
        {
          "name": "cloud_volumes",
          "href": "https://127.0.0.1:8443/api/cloud_volumes",
          "description": "Cloud Volumes"
        },
        {
          "name": "clusters",
          "href": "https://127.0.0.1:8443/api/clusters",
          "description": "Clusters"
        },
        {
          "name": "conditions",
          "href": "https://127.0.0.1:8443/api/conditions",
          "description": "Conditions"
        },
        {
          "name": "configuration_script_payloads",
          "href": "https://127.0.0.1:8443/api/configuration_script_payloads",
          "description": "Configuration Script Payloads"
        },
        {
          "name": "configuration_script_sources",
          "href": "https://127.0.0.1:8443/api/configuration_script_sources",
          "description": "Configuration Script Source"
        },
        {
          "name": "container_deployments",
          "href": "https://127.0.0.1:8443/api/container_deployments",
          "description": "Container Provider Deployment"
        },
        {
          "name": "currencies",
          "href": "https://127.0.0.1:8443/api/currencies",
          "description": "Currencies"
        },
        {
          "name": "data_stores",
          "href": "https://127.0.0.1:8443/api/data_stores",
          "description": "Datastores"
        },
        {
          "name": "events",
          "href": "https://127.0.0.1:8443/api/events",
          "description": "Events"
        },
        {
          "name": "features",
          "href": "https://127.0.0.1:8443/api/features",
          "description": "Product Features"
        },
        {
          "name": "flavors",
          "href": "https://127.0.0.1:8443/api/flavors",
          "description": "Flavors"
        },
        {
          "name": "groups",
          "href": "https://127.0.0.1:8443/api/groups",
          "description": "Groups"
        },
        {
          "name": "hosts",
          "href": "https://127.0.0.1:8443/api/hosts",
          "description": "Hosts"
        },
        {
          "name": "instances",
          "href": "https://127.0.0.1:8443/api/instances",
          "description": "Instances"
        },
        {
          "name": "load_balancers",
          "href": "https://127.0.0.1:8443/api/load_balancers",
          "description": "Load Balancers"
        },
        {
          "name": "measures",
          "href": "https://127.0.0.1:8443/api/measures",
          "description": "Measures"
        },
        {
          "name": "notifications",
          "href": "https://127.0.0.1:8443/api/notifications",
          "description": "User's past notifications"
        },
        {
          "name": "orchestration_templates",
          "href": "https://127.0.0.1:8443/api/orchestration_templates",
          "description": "Orchestration Template"
        },
        {
          "name": "pictures",
          "href": "https://127.0.0.1:8443/api/pictures",
          "description": "Pictures"
        },
        {
          "name": "policies",
          "href": "https://127.0.0.1:8443/api/policies",
          "description": "Policies"
        },
        {
          "name": "policy_actions",
          "href": "https://127.0.0.1:8443/api/policy_actions",
          "description": "Actions"
        },
        {
          "name": "policy_profiles",
          "href": "https://127.0.0.1:8443/api/policy_profiles",
          "description": "Policy Profiles"
        },
        {
          "name": "providers",
          "href": "https://127.0.0.1:8443/api/providers",
          "description": "Providers"
        },
        {
          "name": "provision_dialogs",
          "href": "https://127.0.0.1:8443/api/provision_dialogs",
          "description": "Provisioning Dialogs"
        },
        {
          "name": "provision_requests",
          "href": "https://127.0.0.1:8443/api/provision_requests",
          "description": "Provision Requests"
        },
        {
          "name": "rates",
          "href": "https://127.0.0.1:8443/api/rates",
          "description": "Chargeback Rates"
        },
        {
          "name": "regions",
          "href": "https://127.0.0.1:8443/api/regions",
          "description": "Regions"
        },
        {
          "name": "reports",
          "href": "https://127.0.0.1:8443/api/reports",
          "description": "Reports"
        },
        {
          "name": "request_tasks",
          "href": "https://127.0.0.1:8443/api/request_tasks",
          "description": "Request Tasks"
        },
        {
          "name": "requests",
          "href": "https://127.0.0.1:8443/api/requests",
          "description": "Requests"
        },
        {
          "name": "resource_pools",
          "href": "https://127.0.0.1:8443/api/resource_pools",
          "description": "Resource Pools"
        },
        {
          "name": "results",
          "href": "https://127.0.0.1:8443/api/results",
          "description": "Report Results"
        },
        {
          "name": "roles",
          "href": "https://127.0.0.1:8443/api/roles",
          "description": "Roles"
        },
        {
          "name": "security_groups",
          "href": "https://127.0.0.1:8443/api/security_groups",
          "description": "Security Groups"
        },
        {
          "name": "servers",
          "href": "https://127.0.0.1:8443/api/servers",
          "description": "EVM Servers"
        },
        {
          "name": "service_catalogs",
          "href": "https://127.0.0.1:8443/api/service_catalogs",
          "description": "Service Catalogs"
        },
        {
          "name": "service_dialogs",
          "href": "https://127.0.0.1:8443/api/service_dialogs",
          "description": "Service Dialogs"
        },
        {
          "name": "service_orders",
          "href": "https://127.0.0.1:8443/api/service_orders",
          "description": "Service Orders"
        },
        {
          "name": "service_requests",
          "href": "https://127.0.0.1:8443/api/service_requests",
          "description": "Service Requests"
        },
        {
          "name": "service_templates",
          "href": "https://127.0.0.1:8443/api/service_templates",
          "description": "Service Templates"
        },
        {
          "name": "services",
          "href": "https://127.0.0.1:8443/api/services",
          "description": "Services"
        },
        {
          "name": "settings",
          "href": "https://127.0.0.1:8443/api/settings",
          "description": "Settings"
        },
        {
          "name": "tags",
          "href": "https://127.0.0.1:8443/api/tags",
          "description": "Tags"
        },
        {
          "name": "tasks",
          "href": "https://127.0.0.1:8443/api/tasks",
          "description": "Tasks"
        },
        {
          "name": "templates",
          "href": "https://127.0.0.1:8443/api/templates",
          "description": "Templates"
        },
        {
          "name": "tenants",
          "href": "https://127.0.0.1:8443/api/tenants",
          "description": "Tenants"
        },
        {
          "name": "users",
          "href": "https://127.0.0.1:8443/api/users",
          "description": "Users"
        },
        {
          "name": "virtual_templates",
          "href": "https://127.0.0.1:8443/api/virtual_templates",
          "description": "Virtual Templates"
        },
        {
          "name": "vms",
          "href": "https://127.0.0.1:8443/api/vms",
          "description": "Virtual Machines"
        },
        {
          "name": "zones",
          "href": "https://127.0.0.1:8443/api/zones",
          "description": "Zones"
        }
      ]
    }
    

[1] Personally I think the best you can say about YAML is that it's not XML
which makes this incomprehensible to me: https://www.ibm.com/support/knowledgecenter/SS9H2Y_7.5.0/com.ibm.dp.doc/json_jsonx.html
