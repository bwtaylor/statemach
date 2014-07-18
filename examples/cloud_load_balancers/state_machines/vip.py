from state_machinery import *

vip_state_machine = StateMachine("CloudLoadBalancers","VIP",1,
  "System events for Lbaas Virtual IPs")

vip_state_machine.state("allocated", "A VIP is allocated to the load balancer")

##### ATTRIBUTES ######

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

virtualIpAttributes = AttributeGroup("virtualIpAttributes", [address, ip_version, network],
  "Attributes describing a virtual ip: address, ip_version, network")

vip_state_machine.transition("enable","start","allocated", virtualIpAttributes)
  
vip_state_machine.transition("disable","allocated","end")



