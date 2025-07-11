# # Data word size
# word_size = 16
# # Number of words in the memory
# num_words = 256
# words_per_row = 4

# # Technology to use in $OPENRAM_TECH
# tech_name = "sky130"
# Process corners to characterize
process_corners = [ "TT" ]
# Voltage corners to characterize
supply_voltages = [ 1.8 ]
# Temperature corners to characterize
temperatures = [ 25 ]

# Output directory for the results
output_path = "testsky130"
# Output file base name
output_name = "sky130_16x2"

# Disable analytical models for full characterization (WARNING: slow!)
# analytical_delay = False

# # To force this to use magic and netgen for DRC/LVS/PEX
# # Could be calibre for FreePDK45
# drc_name = "magic"
# lvs_name = "netgen"
# pex_name = "magic"

# Additional configuration for proper bitline extraction and spare rows/columns
# num_spare_cols = 1
# num_spare_rows = 1

# Smaller dual-port SRAM
word_size = 8
num_words = 1024
write_size = 8

# Dual port configuration
num_rw_ports = 1
num_r_ports = 1
num_w_ports = 0

# Technology
tech_name = "sky130"

# Other settings
analytical_delay = True
check_lvsdrc = False

