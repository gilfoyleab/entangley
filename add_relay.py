html_blob = """
        <section id="relay-miner" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#111111] pb-32 px-6 md:px-12">
            
            {/* Horizontal Line separating sections */}
            <div className="absolute top-[100px] left-[-20vw] right-[-20vw] h-[1px] bg-[#111111] pointer-events-none z-0"></div>

            <div className="relative z-10 mb-10 pt-16">
              <h2 className="text-[40px] md:text-[52px] font-bold text-white tracking-tight leading-[1.1]">
                Relay Miner
              </h2>
            </div>

            <div className="relative z-10 w-full max-w-[850px] border border-[#1a1a1a] rounded-[10px] bg-[#0c080a] shadow-[0_0_80px_rgba(0,0,0,1)] overflow-hidden mt-16 md:mt-24 mx-auto md:ml-0">
              {/* Pink top bar */}
              <div className="absolute top-0 left-0 right-0 h-[3px] bg-[#ff1a66] shadow-[0_0_20px_rgba(255,26,102,0.4)]"></div>
              
              <div className="flex flex-col md:flex-row relative">
                 {/* Faint internal vertical divider for desktop */}
                 <div className="hidden md:block absolute left-[38%] top-[10%] bottom-[10%] w-[1px] bg-[#ffffff08]"></div>

                 {/* Left Column Component */}
                 <div className="w-full md:w-[38%] pt-16 pb-14 px-8 flex flex-col items-center text-center">
                    <div className="w-[96px] h-[96px] rounded-full border-[1.5px] border-[#ff1a66] bg-[#ff1a66]/[0.05] flex items-center justify-center shadow-[0_0_30px_rgba(255,26,102,0.2)] mb-8">
                        <svg className="w-[38px] h-[38px] text-[#ff1a66]" fill="currentColor" viewBox="0 0 24 24">
                          <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
                        </svg>
                    </div>
                    
                    <div className="text-[72px] font-bold text-[#ff1a66] leading-none tracking-tighter mb-4 shadow-[#ff1a66] drop-shadow-[0_0_15px_rgba(255,26,102,0.6)]">~70%</div>
                    <div className="text-[10px] font-semibold text-[#ff1a66] tracking-[0.2em] mb-4 font-mono">Subnet TAO Emissions</div>
                    
                    <p className="text-[#666] text-[13px] leading-relaxed max-w-[200px]">
                       Rewards earned by winning auctions and successfully executing deliveries.
                    </p>
                 </div>

                 {/* Right Column Component */}
                 <div className="w-full md:w-[62%] pt-16 pb-14 px-10 md:pr-14 md:pl-12">
                    <h3 className="text-white text-[25px] font-bold mb-3 tracking-wide">Execution Mechanism</h3>
                    <p className="text-[#a1a1a1] text-[15px] leading-[1.6] mb-10 w-[95%]">
                       Relay Miners actively compete to physically deliver messages across chains with speed and security.
                    </p>
                    
                    <div className="space-y-6">
                      <div className="flex items-start gap-4">
                         <svg className="w-[14px] h-[14px] text-[#ff1a66] mt-1 shrink-0" fill="currentColor" viewBox="0 0 24 24">
                           <path d="M14 6l4 4L7 21l-4-4L14 6z" />
                           <path d="M18 2l4 4-3 3-4-4 3-3z" />
                         </svg>
                         <div className="text-[#a1a1a1] text-[14px] leading-relaxed">
                            <span className="text-white font-medium">Sealed Auctions:</span> Bids latency & gas in 2s windows. Fastest + cheapest wins.
                         </div>
                      </div>

                      <div className="flex items-start gap-4">
                         <svg className="w-[16px] h-[16px] text-[#ff1a66] mt-0.5 shrink-0 -ml-0.5" fill="currentColor" viewBox="0 0 24 24">
                           <path d="M20 8h-3V4H3v13h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM8 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm12 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM17.5 9.5l1.96 2.5H17.5v-2.5z" />
                         </svg>
                         <div className="text-[#a1a1a1] text-[14px] leading-relaxed">
                            <span className="text-white font-medium">Cross-Chain Delivery:</span> Executes transaction on destination contract immediately.
                         </div>
                      </div>

                      <div className="flex items-start gap-4">
                         <svg className="w-[14px] h-[14px] text-[#ff1a66] mt-1 shrink-0 px-[1px]" fill="currentColor" viewBox="0 0 24 24">
                           <path d="M3 2v20l3-3 3 3 3-3 3 3 3-3 3 3V2H3zm14 14H7v-2h10v2zm0-4H7v-2h10v2zm0-4H7V6h10v2z" />
                         </svg>
                         <div className="text-[#a1a1a1] text-[14px] leading-relaxed">
                            <span className="text-white font-medium">Proof Submission:</span> Returns delivery proof on-chain to unlock fees & TAO.
                         </div>
                      </div>
                    </div>
                 </div>
              </div>
              
              {/* Footer Panel */}
              <div className="border-t border-[#1a1a1a] bg-[#140b0e] px-10 py-5 flex items-center w-full">
                 <svg className="w-[16px] h-[16px] text-[#ff1a66] mr-3" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24">
                   <polyline points="16 18 22 12 16 6"></polyline>
                   <polyline points="8 6 2 12 8 18"></polyline>
                 </svg>
                 <span className="text-[#ff1a66] text-[10px] font-bold font-mono tracking-widest mt-[1px]">Verified Delivery: &lt; 10s Latency</span>
              </div>
            </div>
            
          </div>
        </section>
"""

import sys

file_path = "/Users/sumangiri/Desktop/entangle/src/app/page.tsx"
with open(file_path, "r") as f:
    text = f.read()

# I will find the end of the <section id="scanner-miner"> tag.
ops_id = '<section id="scanner-miner"'
start_idx = text.find(ops_id)
if start_idx == -1:
    sys.exit("scanner miner section not found")

end_idx = text.find("</section>", start_idx)
if end_idx == -1:
    sys.exit("Section close not found for scanner miner")

end_idx += len("</section>\n")

# Inject the new section
final_text = text[:end_idx] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
