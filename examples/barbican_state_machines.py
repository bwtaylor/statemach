###########
# >>> execfile('examples/barbican_state_machines.py')

from visitors.template import Template

execfile('examples/barbican/state_machines/order.py')

systemschema = Template('system_schema.xml')
graphviz = Template('graphviz.dot')

order_state_machine.do(systemschema)
order_state_machine.do(graphviz)

import os
os.system("dot -Tsvg output/barbican/order/graphviz.dot > output/barbican/order/vip-graphviz.svg")
