import xml.etree.ElementTree as ET
import sys
import workstationfactory as wf 

tree = ET.parse( 'workspace.xml' )
root = tree.getroot()

factory = wf.WorkstationFactory() 

for child in root:
	workspace1 = factory.createWorkstation()
	if child.get('name') is None:
		print ('EEROR: no name defined for this workstation')
		sys.exit()
	workspace1.setName(child.get('name'))
	if child.get('type') is None:
		print ('EEROR: no type defined for this workstation')
		sys.exit()
	workspace1.setType(child.get('type'))
	if not(child.get('replicate') is None):
		workspace1.setReplicates(int(child.get('replicate')))
	for gchild in child:
		if gchild.tag == 'flavor':
			workspace1.setflavor(gchild.text)
		if gchild.tag == 'os':
			workspace1.setOStype(gchild.text)
	factory.addWorkstation(workspace1)
w2= factory.searchWorkstation('name1')
w2.Print()
	#workspace1.Print()