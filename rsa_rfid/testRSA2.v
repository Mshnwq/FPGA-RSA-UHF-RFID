`timescale 1ns / 1ps
module testRSA2;

	//inputs
	wire tx;
	reg go, reset, clk;
	reg rx;
	//outputs
	wire done;
	wire [31:0] output_text;
//	reg [119:0] rx_combo = {1'b1,8'b00000000,1'b0,1'b1,8'b10011000,1'b0,1'b1,8'b00101010,1'b0,1'b1,8'b11110010,1'b0,1'b1,8'b10101110,1'b0,1'b1,8'b00010111,1'b0,1'b1,8'b01110011,1'b0,1'b1,8'b00000101,1'b0,1'b1,8'b10100101,1'b0,1'b1,8'b00010001,1'b0,1'b1,8'b00100110,1'b0,1'b1,8'b11000001,1'b0};
	reg [119:0] rx_combo = {1'b1,8'b00000000,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000101,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b10001101,1'b0,1'b1,8'b11111101,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000001,1'b0,1'b1,8'b00000000,1'b0,1'b1,8'b00000001,1'b0};
	//module to test
	
	rsa_rfid RSA(
    .clk(clk),
    .reset(reset),
    .output_text(output_text),
    .tx(tx),
	 .rx(rx),
    .go(go),
    .done(done)
  );
	
	always
		#10 clk = ~clk;
	
	initial begin
		// intilaizing data
		go = 0;
		reset = 1;
		clk = 0;
		#20
		reset = 0;
		#20
		reset = 1;
		rx = 1;
		#104000
		///////////////
		
		repeat (122) begin
	  // Code to be executed in the loop
			@(posedge clk) begin
			 rx = rx_combo[0];
			 rx_combo = {1'b1, rx_combo[119:1]};
			 #104166;
			 end	
		end	


		@(posedge clk);
		go = 1;
	
		@(posedge clk);
		go = 0;
		
		
		
		#2000000; // let ir run for 10000 cycles
		$stop;
		
		
	end
	
endmodule
		
		
		