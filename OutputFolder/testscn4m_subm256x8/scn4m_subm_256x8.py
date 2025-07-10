# Data word size
word_size = 8
# Number of words in the memory
num_words = 256

# Technology to use in $OPENRAM_TECH
tech_name = "scn4m_subm"
# Process corners to characterize
process_corners = [ "TT" ]
# Voltage corners to characterize
supply_voltages = [ 3.3 ]
# Temperature corners to characterize
temperatures = [ 25 ]

# Output directory for the results
output_path = "testscn4m_subm256x8"
# Output file base name
output_name = "scn4m_subm_256x8"

# Disable analytical models for full characterization (WARNING: slow!)
# analytical_delay = False

# # To force this to use magic and netgen for DRC/LVS/PEX
# # Could be calibre for FreePDK45
# drc_name = "magic"
# lvs_name = "netgen"
# pex_name = "magic"




