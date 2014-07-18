from state_machinery import *

lbaas_state_machine = StateMachine("CloudLoadBalancers","LoadBalancer",1,
  "Cloud load balancer")

##### STATES #####

lbaas_state_machine.state("load_balancing","connections to the VIP are routed to nodes")

##### node_attributes ######
address = Attribute("address","string", "network address of the node")
port = Attribute("port","int", "port number of the service being load balanced")
port.constraint(RangeConstraint(1,65535))
weight = Attribute("weight","int","parameter used in some load balancing algorithms")

node_attributes = AttributeGroup("node_attributes", 
  [address, port, weight],
  "Attributes describing the node's network properties and load balancing algorithm")

##### vip_attributes ######
address = Attribute("address","string", "Network address of the node")
ip_version = Attribute("ip_version", "string", "Version of the IP protocal: IPv4 or IPv6")
ip_version.constraint(Enumeration({
    "IPv4":"Version 4 of the Internet Protocol. Defined by RFC 791.",
    "IPv6":"Version 6 of the Internet Protocol. Defined by RFC 2460."
}))
network = Attribute("network", "string", "Logical name for the network the VIP is routable from")
network.constraint(Enumeration({
    "PUBLIC":"An address that is routable on the public Internet.",
    "SERVICENET":"An address that is routable only on ServiceNet. "
}))

vip_attributes = AttributeGroup("vip_attributes", 
  [address, ip_version, network],
  "Attributes describing a virtual ip: address, ip_version, network")

##### lb_attributes ######

name = Attribute("name","string","The name of the load balancer")
protocol = Attribute("protocol","string","The protocol of connections through the load balancer")
protocol.constraint(Enumeration({
    "DNS_TCP":"DNS_TCP",
    "DNS_UDP":"DNS_UDP",
    "FTP":"FTP",
    "HTTP":"HTTP",
    "HTTPS":"HTTPS",
    "IMAPS":"IMAPS",
    "IMAPv2":"IMAP version 2",
    "IMAPv3":"IMAP version 3",
    "IMAPv4":"IMAP version 4",
    "LDAP":"LDAP",
    "LDAPS":"LDAPS",
    "MYSQL":"MYSQL",
    "POP3":"POP3",
    "POP3S":"POP3S",
    "SFTP":"SFTP",
    "SMTP":"SMTP",
    "TCP":"TCP",
    "TCP_CLIENT_FIRST": "TCP_CLIENT_FIRST",
    "UDP":"UDP",
    "UDP_STREAM":"UDP_STREAM"
}))        
half_closed = Attribute("half_closed","string",
  """Enables or disables Half-Closed support for the load balancer. Half-Closed 
  support provides the ability for one end of the connection to terminate its 
  output, while still receiving data from the other end. Only available for 
  TCP/TCP_CLIENT_FIRST protocols.""", "optional")
protocol.constraint(Enumeration({
    "true":"true",
    "false":"false"
}))
algorithm = Attribute("algorithm","string",
  "The algorithm that defines how traffic should be directed between back-end nodes.")
algorithm.constraint(Enumeration({
    "LEAST_CONNECTIONS":"",
    "RANDOM":"",
    "ROUND_ROBIN":"",
    "WEIGHTED_LEAST_CONNECTIONS":"",
    "WEIGHTED_ROUND_ROBIN":""
}))
# port is reused from node_atts
timeout = Attribute("timeout","string",
  """The timeout value for the load balancer and communications with its nodes. 
  Defaults to 30 seconds with a maximum of 120 seconds.""",
  "optional")
https_redirect = Attribute("https_redirect","string",
  """Enables or disables HTTP to HTTPS redirection for the load balancer. When 
  enabled, any HTTP request returns status code 301 (Moved Permanently), and 
  the requester is redirected to the requested URL via the HTTPS protocol on 
  port 443. For example, http://example.com/page.html would be redirected to 
  https://example.com/page.html. Only available for HTTPS protocol (port=443), 
  or HTTP protocol with a properly configured SSL termination 
  (secureTrafficOnly=true, securePort=443).""",
  "optional")

lb_attributes = AttributeGroup("lb_attributes",
  [name, protocol, half_closed, algorithm, port, timeout, https_redirect],
  "Common load balancer attributes defining connection behavior")


##### Transitions #####
lbaas_state_machine.transition("create","start","load_balancing",
  [node_attributes,vip_attributes,lb_attributes])

lbaas_state_machine.transition("update","load_balancing","load_balancing", lb_attributes)
# several skipped here (see below). What's the CADF action for seperate updates???
lbaas_state_machine.transition("delete","load_balancing","end")


#    <transition name="create"  from="Start" to="Loadbalancing"
#                attributeGroups="LBAtts, NodeAtts, VipAtts, SessionPersistenceAtts,
#                healthMonitorAtts, ConnectionLimitsAtts, ConnectionLoggingAtts"/>
#    <transition name="update"  from="Loadbalancing" to="Loadbalancing"
#                attributeGroups="LBAtts"/>
#    <transition name="session-persistence-update"  from="Loadbalancing" to="Loadbalancing"
#                attributeGroups="SessionPersistenceAtts"/>
#    <transition name="connection-throttle-update"  from="Loadbalancing" to="Loadbalancing"
#                attributeGroups="ConnectionLimitsAtts"/>
#    <transition name="connection-logging-update"  from="Loadbalancing" to="Loadbalancing"
#                attributeGroups="ConnectionLoggingAtts"/>
#    <transition name="health-monitor-update"  from="Loadbalancing" to="Loadbalancing"
#                attributeGroups="healthMonitorAtts"/>
#    <transition name="ssl-termination-update"  from="Loadbalancing" to="Loadbalancing"
#                attributeGroups="SSLTermAtts"/>
#    <transition name="delete"  from="Loadbalancing" to="End"/>

