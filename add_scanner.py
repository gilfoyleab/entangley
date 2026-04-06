html_blob = """
        <section id="scanner-miner" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#111111] pt-16 pb-24 px-6 md:px-12">
            
            {/* Horizontal Line separating sections */}
            <div className="absolute top-[100px] left-[-20vw] right-[-20vw] h-[1px] bg-[#111111] pointer-events-none z-0"></div>

            <div className="relative z-10 mb-10">
              <h2 className="text-[40px] md:text-[52px] font-bold text-white tracking-tight leading-[1.1]">
                Scanner Miner
              </h2>
            </div>

            <div className="relative z-10 w-full max-w-[850px] border border-[#1a1a1a] rounded-[10px] bg-[#0c1216] shadow-[0_0_80px_rgba(0,0,0,1)] overflow-hidden mt-16 md:mt-24">
              {/* Cyan top bar */}
              <div className="absolute top-0 left-0 right-0 h-[3px] bg-[#00d2ff] shadow-[0_0_20px_rgba(0,210,255,0.4)]"></div>
              
              <div className="flex flex-col md:flex-row relative">
                 {/* Faint internal vertical divider for desktop */}
                 <div className="hidden md:block absolute left-[38%] top-[10%] bottom-[10%] w-[1px] bg-[#ffffff08]"></div>

                 {/* Left Column Component */}
                 <div className="w-full md:w-[38%] pt-16 pb-14 px-8 flex flex-col items-center text-center">
                    <div className="w-[96px] h-[96px] rounded-full border-[1.5px] border-[#00d2ff] bg-[#00d2ff]/[0.05] flex items-center justify-center shadow-[0_0_30px_rgba(0,210,255,0.2)] mb-8">
                        <svg className="w-[38px] h-[38px] text-[#00d2ff]" fill="currentColor" viewBox="0 0 24 24">
                          <path d="M12 11c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm6 2c0-3.31-2.69-6-6-6s-6 2.69-6 6c0 2.22 1.21 4.15 3 5.19l1-1.74c-1.19-.7-2-1.97-2-3.45 0-2.21 1.79-4 4-4s4 1.79 4 4c0 1.48-.81 2.75-2 3.45l1 1.74c1.79-1.04 3-2.97 3-5.19zM12 3C7.03 3 3 7.03 3 12c0 3.32 1.8 6.22 4.5 7.79l1-1.73C6.39 16.89 5 14.61 5 12c0-3.86 3.14-7 7-7s7 3.14 7 7c0 2.61-1.39 4.89-3.5 6.06l1 1.73C19.2 18.22 21 15.32 21 12c0-4.97-4.03-9-9-9z"/>
                        </svg>
                    </div>
                    
                    <div className="text-[72px] font-bold text-[#00d2ff] leading-none tracking-tighter mb-4 shadow-[#00d2ff] drop-shadow-[0_0_15px_rgba(0,210,255,0.6)]">~30%</div>
                    <div className="text-[10px] font-semibold text-[#00d2ff] tracking-[0.2em] mb-4 font-mono">Subnet TAO Emissions</div>
                    
                    <p className="text-[#666] text-[13px] leading-relaxed max-w-[200px]">
                       Rewards distributed per epoch based on discovery speed and accuracy.
                    </p>
                 </div>

                 {/* Right Column Component */}
                 <div className="w-full md:w-[62%] pt-16 pb-14 px-10 md:pr-14 md:pl-12">
                    <h3 className="text-white text-[25px] font-bold mb-3 tracking-wide">Discovery Mechanism</h3>
                    <p className="text-[#a1a1a1] text-[15px] leading-[1.6] mb-10 w-[95%]">
                       The Scanner Miner constantly monitor connected blockchains for activity.
                    </p>
                    
                    <div className="space-y-6">
                      <div className="flex items-start gap-4">
                         <svg className="w-[14px] h-[14px] text-[#00d2ff] mt-1 shrink-0" fill="currentColor" viewBox="0 0 24 24">
                           <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
                         </svg>
                         <div className="text-[#a1a1a1] text-[14px] leading-relaxed">
                            <span className="text-white font-medium">Real-time Polling:</span> Queries RPC nodes every block to detect <span className="font-mono text-[12px] bg-[#1a1a1a]/80 text-[#ccc] px-1.5 py-0.5 rounded">MessageDispatched</span> events.
                         </div>
                      </div>

                      <div className="flex items-start gap-4">
                         <svg className="w-[14px] h-[14px] text-[#00d2ff] mt-1 shrink-0" fill="currentColor" viewBox="0 0 24 24">
                           <path d="M3 4c0-.55.45-1 1-1h16c.55 0 1 .45 1 1v2.59c0 .27-.11.52-.29.71L15 13.41V20c0 .35-.2.66-.51.84l-4 2.33A.996.996 0 019 22v-8.59L3.29 7.3A1 1 0 013 6.59V4z" />
                         </svg>
                         <div className="text-[#a1a1a1] text-[14px] leading-relaxed">
                            <span className="text-white font-medium">Event Filtering:</span> Validates payload structure and ensures correct source contract emission.
                         </div>
                      </div>

                      <div className="flex items-start gap-4">
                         <svg className="w-[14px] h-[14px] text-[#00d2ff] mt-1 shrink-0" fill="currentColor" viewBox="0 0 24 24">
                           <circle cx="18" cy="5" r="3" />
                           <circle cx="6" cy="12" r="3" />
                           <circle cx="18" cy="19" r="3" />
                           <path d="M8.59 13.51l6.83 3.98m-.01-10.98l-6.82 3.98" stroke="currentColor" strokeWidth="2" />
                         </svg>
                         <div className="text-[#a1a1a1] text-[14px] leading-relaxed">
                            <span className="text-white font-medium">Validator Feed:</span> Propagates verified events to the Validator set for consensus.
                         </div>
                      </div>
                    </div>
                 </div>
              </div>
              
              {/* Footer Panel */}
              <div className="border-t border-[#1a1a1a] bg-[#071013] px-10 py-5 flex items-center w-full">
                 <svg className="w-[16px] h-[16px] text-[#00d2ff] mr-3" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24">
                   <polyline points="16 18 22 12 16 6"></polyline>
                   <polyline points="8 6 2 12 8 18"></polyline>
                 </svg>
                 <span className="text-[#00d2ff] text-[10px] font-bold font-mono tracking-widest mt-[1px]">Required Stake: 100 TAO to register UID</span>
              </div>
            </div>
            
          </div>
        </section>
"""

import sys

file_path = "/Users/sumangiri/Desktop/entangle/src/app/page.tsx"
with open(file_path, "r") as f:
    text = f.read()

# I will find the end of the <section id="operators"> tag.
ops_id = '<section id="operators"'
start_idx = text.find(ops_id)
if start_idx == -1:
    sys.exit("Operators section not found")

end_idx = text.find("</section>", start_idx)
if end_idx == -1:
    sys.exit("Section close not found")

end_idx += len("</section>\n")

# Inject the new section
final_text = text[:end_idx] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
