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
    ("r6615", "r6615"),
    ("sm110p", "sm110p"),
    ("c6620", "c6620"),
    ("d760p", "d760p"),
]

OS_IMAGES = [
    ("urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD",
     "Ubuntu 20.04"),
    ("urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD",
     "Ubuntu 22.04"),
]
pc.defineParameter("NODE_TYPE", "Node type",
                    portal.ParameterType.STRING, NODE_TYPES[0][0],
                    NODE_TYPES,
                    longDescription="Select the node type.")

pc.defineParameter(
    "OS_IMAGE", "OS Image",
    portal.ParameterType.IMAGE, OS_IMAGES[0][0], OS_IMAGES,
    longDescription="Select an image.")


params = pc.bindParameters()

# Add a raw PC to the request.
node = request.RawPC("node")
# Set the OS image for the node.
node.disk_image = params.OS_IMAGE
node.hardware_type = params.NODE_TYPE

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
