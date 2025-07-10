# Data word size
word_size = 8
# Number of words in the memory
num_words = 128

# Technology to use in $OPENRAM_TECH
tech_name = "scn4m_subm"  # More mature technology with better DRC compliance
# Process corners for characterization
process_corners = ["TT", "FF", "SS"]
supply_voltages = [1.0]
temperatures = [25]

# Output directory for the results
output_path = "scn4m_subm-spice-710-128x8"
# Output file base name
output_name = "scn4m_subm-spice-710-128x8"

# Disable analytical models for full characterization (WARNING: slow!)
analytical_delay = True
# # Specify SPICE simulator
# spice_name = "ngspice"  # or "hspice", "spectre", "xyce"
# # Number of simulation threads
# num_sim_threads = 4

# Load and slew scales for characterization tables
load_scales = [1, 4]     # Only 2 load points
slew_scales = [1, 4]     # Only 2 slew points

# Re-enable DRC/LVS verification
check_lvsdrc = True
inline_lvsdrc = False  # Disable inline LVS to avoid scn4m_subm KLayout LVS issues

# Use KLayout for DRC/LVS/PEX (works with scn4m_subm)
drc_name = "klayout"
lvs_name = "klayout"
pex_name = "klayout"