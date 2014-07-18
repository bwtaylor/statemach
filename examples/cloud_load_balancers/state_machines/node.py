from state_machinery import *

lbaas_node = StateMachine("CloudLoadBalancers","Node",1,
  "Node behind a cloud load balancer")

##### STATES #####

lbaas_node.add_states(
 { 
   "enabled" : "The node actively receives connections through the load balancer",
   "draining": "The node receives no new connections, but existing ones remain",
   "disabled": "The node does not recieve any network traffic"
 }
)

##### ATTRIBUTES ######
address = Attribute("address","string", "network address of the node")

port = Attribute("port","int", "port number of the service being load balanced")
port.constraint(RangeConstraint(1,65535))

algorithm = Attribute("algorithm","string", "load balancing algorithm used to route requests to nodes"),
weight = Attribute("weight","int","parameter used in some load balancing algorithms")

##### Attribute Groups #####
nodeatts = AttributeGroup("NodeAtts", [address, port, algorithm, weight],
  "Attributes describing the node's network properties and load balancing algorithm")

##### Transitions #####
lbaas_node.transition("create","start","enabled",nodeatts)

lbaas_node.transition("update","enabled","enabled",nodeatts)
lbaas_node.transition("drain","enabled","draining",nodeatts)
lbaas_node.transition("disable","enabled","disabled",nodeatts)
lbaas_node.transition("disable","enabled","disabled",nodeatts,"system")
lbaas_node.transition("delete","enabled","end")

lbaas_node.transition("enable","draining","enabled",nodeatts)
lbaas_node.transition("update","draining","draining",nodeatts)
lbaas_node.transition("disable","draining","disabled",nodeatts)
lbaas_node.transition("disable","draining","disabled",nodeatts,"system")
lbaas_node.transition("delete","draining","end")

lbaas_node.transition("enable","disabled","enabled",nodeatts)
lbaas_node.transition("drain","disabled","draining",nodeatts)
lbaas_node.transition("update","disabled","disabled",nodeatts)
lbaas_node.transition("delete","disabled","end")


