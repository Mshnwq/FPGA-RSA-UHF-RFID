module controlUnit
	(
	input clk, reset, go,
	output reg done, load, running,
	input over
	);
	
	// Defining States
	localparam S0 = 2'b00; // idle
	localparam S1 = 2'b01; // running
	localparam S2 = 2'b10; // done
	
	// initializing state toggle
	reg [1:0] state = S0; 
	reg [1:0] nextState;
	
	always @(posedge clk, posedge reset)
		if (reset)
			state <= S0; //Synchronous reset
		else
			state <= nextState;
		
		
	// outputs of each state	
	always @(*) 
	begin
		// initialized variables
		done    = 0;
		load    = 0;
		running = 0; 
		nextState = state;
		
		case(state)
			S0:
				begin
				
					if(~go) 
					begin 
						nextState = S0;
					end
					
					else
					begin
						load      = 1;
						running   = 1; 
						nextState = S1;
					end
					
				end
			S1:
				begin
				
					if(~over) 
					begin
						running = 1;					
						nextState  = S1;
					end
					
					else
					begin
						done      = 1;
						nextState = S2;
					end
					
				end
			S2: 
				begin
				
					done      = 1;
					nextState = S0;
					
				end
		endcase
	end
	 
endmodule 