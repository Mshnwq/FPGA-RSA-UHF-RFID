/////////////////////////////////////////////////////////////////////////////
// File : stringDivider.v
// Author : Hayan Al-Machnouk
// Date : 15/11/2022
// Divides a string to its ascii values.
/////////////////////////////////////////////////////////////////////////////
module stringDivider
	#(parameter stringLength = 4)
	(
	input str,	                                    //string input
	input clk,	                                    //Clock Signal
	output reg ascii_array //ASCII Array output
	);
	
	reg [7:0] select;
	reg [7:0] out;
	integer i;
	
	//$display("str= %s",str);
	always@(*) 
	begin

		for (i=0; i<stringLength; i=i+1)
		begin
			select = string[(8*(i+1))-1:(8*i)]; // indexing the string
			//$display("select= %s", select);
			  case (select)
			  	"A": out = 8'h01; //selectA
			  	"B": out = 8'h02; //selectB
			  endcase
			//ascii_array[i] = out;
			//$display("ascii_array[i]= %s", ascii_array[i]);
		end
	end
endmodule 