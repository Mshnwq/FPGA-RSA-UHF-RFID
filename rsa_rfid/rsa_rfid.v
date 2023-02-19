module rsa_rfid
	#(parameter WordSize = 32) 
	(  
	// Top Level  I/O
	input clk, reset,
	
	// Data Path  I/O	
	output [WordSize-1:0] output_text,
	output tx,
	input rx,

	// Controller I/O
	input wire go,       // enablers
	output wire done     // flags
	);
	
	wire load, running, over, rd_uart, wr_uart, tx_full, rx_empty;
	wire  [7:0] r_data;
	wire 	[7:0] w_data;
	wire  [WordSize-1:0] input_text;
	wire  [WordSize-1:0] key;
	wire  [WordSize-1:0] mod;
	
	
//	dataPath DP(clk, reset, input_text, key, mod, output_text, load, running, over);
dataPath dataPath_rsa (
    .clk(clk),
    .reset(reset),
    .uart_in(r_data),
    .output_text(w_data),
	 .cipherFull(output_text),
    .nextByte_in(rd_uart),
    .nextByte_out(wr_uart),
	 .empty_fifo(rx_empty),
    .load(go),
    .running(running),
    .over(over)
  );
	controlUnit CU_rsa(clk, reset, go, load, running, done, over);
	uart #(
    .DBIT(8), 
    .SB_TICK(16)
  ) uart_rsa (
    .clk(clk),
    .reset_n(reset),
    .r_data(r_data),
    .rd_uart(rd_uart),
    .rx_empty(rx_empty),
    .rx(rx),
    .w_data(w_data),
    .wr_uart(wr_uart),
    .tx_full(tx_full),
    .tx(tx),
    .TIMER_FINAL_VALUE(324)
  );


endmodule 