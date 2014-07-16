###########
# >>> execfile('examples/vip_system_schema.py')

import visitors.template as t

execfile('examples/cloud_load_balancers/state_machines/vip.py')

systemschema = t.Template('system_schema.xml')
dot2svg_cmd = 'dot -Tsvg {path}/graphviz.dot > {path}/vip-graphviz.svg'
graphviz = t.TemplateAndCommand('graphviz.dot', dot2svg_cmd)

vip_state_machine.do(systemschema)
vip_state_machine.do(graphviz)


