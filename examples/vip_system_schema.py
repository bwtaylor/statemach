###########
# >>> execfile('examples/vip_system_schema.py')

import visitors.template as t

execfile('examples/cloud_load_balancers/state_machines/vip.py')

systemschema = t.Template('system_schema.xml')
cadf_xsd = t.Template('cadf_attachment.xsd')
dot2svg_cmd = 'dot -Tsvg {path}/graphviz.dot > {path}/vip-graphviz.svg'
graphviz = t.TemplateAndCommand('graphviz.dot', dot2svg_cmd)

def item_color(item,item_list):
  colors = ["black","red","green","blue","orange","purple"]
  return colors[item_list.index(item)]
  
graphviz.use_filter('actor_color',item_color)

vip_state_machine.do(systemschema)
vip_state_machine.do(cadf_xsd)
vip_state_machine.do(graphviz)

execfile('examples/cloud_load_balancers/state_machines/node.py')

lbaas_node.do(systemschema)
lbaas_node.do(cadf_xsd)
lbaas_node.do(graphviz)

execfile('examples/cloud_load_balancers/state_machines/load_balancer.py')
lbaas_state_machine.do(systemschema)
lbaas_state_machine.do(cadf_xsd)
lbaas_state_machine.do(graphviz)

