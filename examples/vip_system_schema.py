###########
# >>> execfile('examples/vip_system_schema.py')

from visitors.template import Template

execfile('examples/cloud_load_balancers/state_machines/vip.py')

systemschema = Template('system_schema.xml')
graphviz = Template('graphviz.dot')

vip_state_machine.do(systemschema)
vip_state_machine.do(graphviz)

import os
os.system("dot -Tsvg output/VIP/graphviz.dot > output/VIP/vip-graphviz.svg")
