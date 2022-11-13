module testRSA;

	//inputs
	reg [7:0] input_text;
	reg [7:0] key;
	reg [7:0] mod;
	reg go, reset, clk;
	
	//outputs
	wire done;
	wire [7:0] output_text;
	
	//module to test
	rsa_rfid RSA(clk, reset, go, input_text, key, mod, output_text, done);
	
	always
		#5 clk = ~clk;
	
	initial begin
		// intilaizing data
		input_text = 0;
		go = 0;
		reset = 0;
		clk = 0;
		
		///////////////
		@(posedge clk);
		input_text = 5;
		key        = 65537;
		mod        = 36349
		
		@(posedge clk);
		go = 1;
		
		@(posedge clk);
		go = 0;
		
		#100000; // let ir run for 10000 cycles
		$stop;
		
		
	end
	
endmodule
		
		
		