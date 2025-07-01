* Delay stimulus for period of 0n load=0fF slew=0ns

* TT process corner
.include "/Users/fuyaozhou/OpenRAM/technology/freepdk45/models/tran_models/models_nom/PMOS_VTG.inc"
.include "/Users/fuyaozhou/OpenRAM/technology/freepdk45/models/tran_models/models_nom/NMOS_VTG.inc"
.include "/tmp/openram_fuyaozhou_47048_temp/trimmed.sp"

* Global Power Supplies
Vvdd vdd 0 5

*Nodes gnd and 0 are the same global ground node in ngspice/hspice/xa. Otherwise, this source may be needed.
*Vgnd gnd 0 0.0

* Instantiation of the SRAM
Xfreepdk45_16x2 din0_0 din0_1 a0_0 a0_1 a0_2 a0_3 CSB0 WEB0 clk0 dout0_0 dout0_1 vdd gnd freepdk45_16x2

* SRAM output loads
CD00 dout0_0 0 0f
CD01 dout0_1 0 0f

* Generation of data and address signals
* (time, data): [(0, 0), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
Vdin0_0  din0_0  0 PWL (0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v )
* (time, data): [(0, 0), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
Vdin0_1  din0_1  0 PWL (0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v )
* (time, data): [(0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 1), (0, 1)]
Va0_0 a0_0 0 PWL (0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v )
* (time, data): [(0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 1), (0, 1)]
Va0_1 a0_1 0 PWL (0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v )
* (time, data): [(0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 1), (0, 1)]
Va0_2 a0_2 0 PWL (0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v )
* (time, data): [(0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 0), (0, 0), (0, 0), (0, 1), (0, 1)]
Va0_3 a0_3 0 PWL (0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v )

* Generation of control signals
* (time, data): [(0, 1), (0, 0), (0, 0), (0, 1), (0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 1), (0, 0), (0, 1), (0, 0), (0, 0), (0, 1)]
VCSB0 CSB0 0 PWL (0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v )
* (time, data): [(0, 1), (0, 0), (0, 0), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 0), (0, 1), (0, 0), (0, 1), (0, 1), (0, 1), (0, 1)]
VWEB0 WEB0 0 PWL (0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 0v 0.0n 0v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v 0.0n 5v )

* Generation of Port clock signal
* PULSE: period=0
VCLK0 CLK0 0 PULSE (0 5 0n 0n 0n 0.0n 0n)
.include /Users/fuyaozhou/OpenRAM/tempfreepdk45spice/delay_meas.sp
* Measure statements for delay and power

.TEMP 25
.TRAN 10p 0n 0n 10p UIC
.OPTIONS POST=1 RELTOL=0.001 PROBE method=gear ACCT
* probe is used for hspice/xa, while plot is used in ngspice
*.probe V(*)
*.plot V(*)
.end

