module dataPath
	#(parameter WordSize = 8)
	(  
	input clk, reset,
	
	// Data Path I/O
	input  [WordSize-1:0] x,
	output [WordSize-1:0] freq,
	
	// Controller I/O
	input wire load, incFreq, running, // enablers
	output wire equal, over           // flags
	);
	
	wire [WordSize-1:0]   inMux; // from input
	wire [WordSize-1:0]  outMux; // to output
	
	wire [WordSize-1:0] dataIn;  // from ROM
	wire [WordSize  :0] address; // to ROM
	
	wire [WordSize-1:0] ground; 
	wire [WordSize  :0] ground9;
	staticValue #(8, 'hzzzz) outDefValue(ground);
	//staticValue #(9, 'hzzzz) outDefValue9(ground9);
	
	mux2to1 doneMux(ground, outMux, over, freq);
	mux2to1 loadMux(ground, x, load, inMux);
	
	countRegister #(9)addr(clk, running, reset, address, over);      // increments to next address
	
	arrayROM     a      (clk, address, dataIn);              // retreive value at address
	
	wire [WordSize-1:0] compIn1, compIn2;
	
	regModule valX      (inMux, load, reset, clk, compIn1);  // holds users input value
	regModule valA      (dataIn, running, reset, clk, compIn2);  // holds retrieved ROM value
	
	comparator comp      (clk, compIn1, compIn2, equal);           // handle equal flag         
	
	countRegister freqCount (clk, incFreq, reset, outMux);       // holds frequency value
	

endmodule 