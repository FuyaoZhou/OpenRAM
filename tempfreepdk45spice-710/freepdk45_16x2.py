# Data word size
word_size = 2
# Number of words in the memory
num_words = 16

# Technology to use in $OPENRAM_TECH
tech_name = "freepdk45"
# Process corners for characterization
process_corners = ["TT", "FF", "SS"]
supply_voltages = [1.0]
temperatures = [25]

# Output directory for the results
output_path = "tempfreepdk45spice-710"
# Output file base name
output_name = "freepdk45_16x2"

# Disable analytical models for full characterization (WARNING: slow!)
analytical_delay = False
# Specify SPICE simulator
spice_name = "ngspice"  # or "hspice", "spectre", "xyce"
# Number of simulation threads
num_sim_threads = 4

# Load and slew scales for characterization tables
load_scales = [1, 4]     # Only 2 load points
slew_scales = [1, 4]     # Only 2 slew points

# # To force this to use magic and netgen for DRC/LVS/PEX
# # Could be calibre for FreePDK45
drc_name = "magic"
lvs_name = "netgen"
pex_name = "magic"