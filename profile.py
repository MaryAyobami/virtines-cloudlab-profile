# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context, needed to defined parameters
pc = portal.Context()
# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

NODE_TYPES = [
    ("c6525-25g", "c6525-25g"),
    ("c6525-100g", "c6525-100g"),
]


pc.defineParameter("NODE_TYPE", "Node type",
                    portal.ParameterType.NODETYPE, NODE_TYPES[0][0],
                    NODE_TYPES,
                    longDescription="Select one node.")

params = pc.bindParameters()

# Add a raw PC to the request.
node = request.RawPC("node")
# Set the OS image for the node.
node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
node.hardware_type = params.NODE_TYPE

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
