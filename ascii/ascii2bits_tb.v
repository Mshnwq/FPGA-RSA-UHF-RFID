/////////////////////////////////////////////////////////////////////////////
// File : ascii2bits_tb.v
// Author : Hayan Al-Machnouk
// Date : 15/11/2022
// This is a testbench for ASCII to Binary conversion.
/////////////////////////////////////////////////////////////////////////////
module ascii2bits_tb();
	reg [7:0] in;
	//reg clk,rst,w_RX_dv;
	reg clk;
	wire [7:0] out;

	stringDivider UUT(in,clk,out); 
	
		always
		#5 clk = ~clk;
		
	initial begin 	
		
		@(posedge clk);
		in = "AAAB";
		
		@(posedge clk);
		
		#260; // let ir run for 26 cycles
		$stop;
	end
	
endmodule	


//	initial begin
//		#10;
//		rst = 1;
//		#60;
//		rst = 0;
//		#60;
//		w_RX_dv = 1;
//		in = 8'h45;  
//		#60;
//		in = 8'h4a;
//		in = "dD"
//		#60;
//		in = 8'b00110001;
//		#60;
//		w_RX_dv = 0;
//		#60;
//	end
	
	
