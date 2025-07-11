# Data word size
word_size = 32
# Number of words in the memory
num_words = 128  # Much smaller - test with 64 words instead of 512
num_banks = 1  # <-- Set this to the number of banks you want

# Technology to use in $OPENRAM_TECH
tech_name = "scn4m_subm"  # or "sky130"
# Process corners for characterization
process_corners = ["TT", "FF", "SS"]
supply_voltages = [1.0]
temperatures = [25]

# Output directory for the results
output_path = "test-4banks"
# Output file base name
output_name = "test-4banks"

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
check_lvsdrc = False
inline_lvsdrc = False  # Disable inline LVS to avoid duplicate circuit definition errors

# Use KLayout for DRC/LVS/PEX (works with freepdk45)
# drc_name = "klayout"
# lvs_name = "klayout"
# pex_name = "klayout"