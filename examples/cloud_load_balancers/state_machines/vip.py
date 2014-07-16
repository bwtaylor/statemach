from state_machinery import *

vip_state_machine = StateMachine("CloudLoadBalancers","VIP",1,
  "System events for Lbaas Virtual IPs")

vip_state_machine.state("allocated", "A VIP is allocated to the load balancer")

##### ATTRIBUTES ######

address = Attribute("address","string", "address of the node")

ipVersion = Attribute("ipVersion", "string")
ipVersion.constraint(Enumeration({
    "IPv4":"Version 4 of the Internet Protocol. Defined by RFC 791.",
    "IPv6":"Version 6 of the Internet Protocol. Defined by RFC 2460."
}))

ipVersionType = Attribute("ipVersionType", "string")
ipVersionType.constraint(Enumeration({
    "PUBLIC":"An address that is routable on the public Internet.",
    "SERVICENET":"An address that is routable only on ServiceNet. "
}))

virtualIpAttributes = AttributeGroup("virtualIpAttributes", [address, ipVersion, ipVersionType])

vip_state_machine.transition("enable","start","allocated", virtualIpAttributes)
vip_state_machine.transition("disable","allocated","end")



