html_blob = """
        <section id="realtime-fees" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#111111] pt-16 pb-32 px-6 md:px-12 overflow-hidden">
            
            {/* Horizontal Line separating sections */}
            <div className="absolute top-[200px] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-0"></div>
            {/* The faint vertical separator grid line */}
            <div className="absolute top-0 bottom-[100px] left-[35%] w-[1px] bg-[#1a1a1a] pointer-events-none z-0 hidden xl:block"></div>

            <div className="relative z-10 mb-20 pt-10">
              <h2 className="text-[44px] md:text-[54px] font-bold text-white tracking-tight leading-[1.1] mb-5">
                Real-time Fees. Real-time Rewards.
              </h2>
              <p className="text-[#888] text-[16px] max-w-[600px] leading-relaxed">
                A self-sustaining model earning native assets (ETH, SOL, USDC).<br/>
                Revenue is independent of TAO price.
              </p>
            </div>

            {/* Flow Diagram Container */}
            <div className="relative flex flex-col xl:flex-row items-center justify-center gap-[40px] xl:gap-[0px] w-full max-w-[950px] mx-auto z-10">
              
              {/* 1. Left Block: User / dApp */}
              <div className="w-full sm:w-[280px] xl:w-[260px] bg-[#0a0a0a] border border-[#222] rounded-[10px] p-6 relative z-10 shrink-0">
                 <div className="flex justify-between items-start mb-6 mt-1">
                    <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M21 7.28V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-2.28c.59-.35 1-.98 1-1.72V9c0-.74-.41-1.37-1-1.72zM20 9v6h-2V9h2zM5 19V5h14v2h-6c-1.1 0-2 .9-2 2v6c0 1.1.9 2 2 2h6v2H5z"/></svg>
                    <div className="flex gap-2 mt-0.5 items-center">
                       <svg className="w-[12px] h-[12px] text-[#627eea]" viewBox="0 0 32 32" fill="currentColor">
                         <path d="M15.925 23.969L15.823 24l-7.447-4.391 7.553 10.638 7.57-10.638-7.574 4.36zM15.986 0L8.358 12.67l7.625 4.542 7.643-4.542L15.986 0z" />
                       </svg>
                       <div className="w-[13px] h-[13px] rounded-full bg-[#00d2ff]"></div>
                    </div>
                 </div>
                 <div className="text-white text-[17px] font-bold tracking-tight mb-2">User / dApp</div>
                 <div className="text-[#666] text-[13px] mb-6 font-mono">Calls sendMessage()</div>
                 <div className="text-[#bbb] text-[13px] font-semibold tracking-wide">Pays Native Gas Fee</div>
                 
                 {/* Outbound connection line */}
                 <div className="hidden xl:block absolute right-[-40px] top-1/2 w-[40px] h-[1px] bg-[#333] -translate-y-[0.5px] z-0"></div>
                 <div className="hidden xl:block absolute right-[-44px] top-1/2 w-[0] h-[0] border-t-[4px] border-b-[4px] border-l-[6px] border-transparent border-l-[#333] -translate-y-[4px] z-10"></div>
              </div>

              {/* spacer */}
              <div className="hidden xl:block w-[40px] shrink-0"></div>

              {/* 2. Middle Block: ENTANGLE CORE */}
              <div className="w-[280px] bg-[#0c0c0c] border border-[#222] rounded-[8px] p-6 relative z-10 shrink-0 shadow-[0_20px_40px_rgba(0,0,0,0.6)]">
                 <div className="absolute top-[-1px] left-0 right-0 h-[3px] bg-white rounded-t-[8px] opacity-100 shadow-[0_0_15px_rgba(255,255,255,0.8)]"></div>

                 <div className="text-white text-[12px] font-bold font-mono tracking-widest uppercase mb-6 mt-1">ENTANGLE CORE</div>
                 
                 <div className="space-y-4">
                    {/* Gas Oracle */}
                    <div className="bg-[#141414] border border-[#222] rounded-[6px] p-3 flex gap-4 items-center">
                       <div className="bg-[#00d2ff]/10 p-2.5 rounded-[4px] border border-[#00d2ff]/20">
                         <svg className="w-[16px] h-[16px] text-[#00d2ff]" fill="currentColor" viewBox="0 0 24 24">
                           <path d="M19.77 7.23l.01-.01-3.72-3.72L15 4.56l2.11 2.11C16.17 7 15.5 7.93 15.5 9v11c0 .55-.45 1-1 1s-1-.45-1-1v-4c0-2.21-1.79-4-4-4h-1V7c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v13h8c0 1.66 1.34 3 3 3s3-1.34 3-3V9c0-.46.15-.88.4-1.22l3.37-3.37zM10 18H5V8h4.5c.28 0 .5.22.5.5v9z"/>
                         </svg>
                       </div>
                       <div>
                          <div className="text-white text-[13px] font-bold mb-0.5 tracking-wide leading-none">Gas Oracle</div>
                          <div className="text-[#666] text-[10px]">Median price every 2m</div>
                       </div>
                    </div>
                    
                    {/* Circuit Breaker */}
                    <div className="bg-[#141414] border border-[#222] rounded-[6px] p-3 flex gap-4 items-center">
                       <div className="bg-[#ff1a66]/10 p-2.5 rounded-[4px] border border-[#ff1a66]/20">
                         <svg className="w-[16px] h-[16px] text-[#ff1a66]" fill="currentColor" viewBox="0 0 24 24">
                           <path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM9 6c0-1.66 1.34-3 3-3s3 1.34 3 3v2H9V6zm9 14H6V10h12v10zm-6-3c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z"/>
                         </svg>
                       </div>
                       <div>
                          <div className="text-white text-[13px] font-bold mb-0.5 tracking-wide leading-none">Circuit Breaker</div>
                          <div className="text-[#666] text-[10px]">Staleness check &gt;50 blks</div>
                       </div>
                    </div>
                 </div>

                 {/* Outbound connection lines (Forking UP and DOWN) */}
                 {/* Top line up */}
                 <div className="hidden xl:block absolute right-[-50px] top-[50px] w-[50px] h-[1px] bg-[#333] transform rotate-[-25deg] origin-left z-0"></div>
                 {/* Bottom line down */}
                 <div className="hidden xl:block absolute right-[-50px] bottom-[50px] w-[50px] h-[1px] bg-[#333] transform rotate-[25deg] origin-left z-0"></div>
              </div>

              {/* gap for the branching lines */}
              <div className="hidden xl:block w-[50px] shrink-0 relative z-0"></div>

              {/* 3. Right Blocks Column */}
              <div className="flex flex-col gap-8 xl:gap-8 shrink-0 w-full sm:w-[320px] xl:w-[300px]">
                
                {/* Top: 30% Protocol Treasury */}
                <div className="bg-[#010a12] border border-[#111] border-l-[3px] border-l-[#00d2ff] rounded-[8px] p-6 shadow-[0_0_20px_rgba(0,210,255,0.06)] relative z-10 w-full overflow-hidden">
                   <div className="absolute inset-0 border border-[#00d2ff]/[0.05] rounded-[8px] pointer-events-none"></div>
                   <div className="text-[52px] font-bold text-[#00d2ff] tracking-tighter leading-none mb-2 mt-1 drop-shadow-[0_0_15px_rgba(0,210,255,0.3)]">30%</div>
                   <div className="text-white text-[15px] xl:text-[17px] font-bold tracking-tight mb-3">Protocol Treasury</div>
                   <div className="text-[#888] text-[11px] leading-relaxed mb-6 w-[95%]">
                     Accumulates native assets (ETH, SOL, ATOM). Funds operations and growth.
                   </div>
                   
                   <div className="inline-block bg-[#00d2ff]/10 text-[#00d2ff] text-[10px] font-mono px-2 py-1 rounded-[4px] uppercase tracking-widest font-bold">
                      ON-CHAIN
                   </div>
                </div>

                {/* Bottom: 70% Relay Reserve */}
                <div className="bg-[#120104] border border-[#111] border-l-[3px] border-l-[#ff1a66] rounded-[8px] p-6 shadow-[0_0_20px_rgba(255,26,102,0.06)] relative z-10 w-full overflow-hidden">
                   <div className="absolute inset-0 border border-[#ff1a66]/[0.05] rounded-[8px] pointer-events-none"></div>
                   <div className="text-[52px] font-bold text-[#ff1a66] tracking-tighter leading-none mb-2 mt-1 drop-shadow-[0_0_15px_rgba(255,26,102,0.3)]">70%</div>
                   <div className="text-white text-[15px] xl:text-[17px] font-bold tracking-tight mb-3">Relay Reserve</div>
                   <div className="text-[#888] text-[11px] leading-relaxed mb-6 w-[95%]">
                     Direct rewards for Relay Miners who successfully execute transactions.
                   </div>
                   
                   <div className="inline-block bg-[#ff1a66]/10 text-[#ff1a66] text-[10px] font-mono px-2 py-1 rounded-[4px] uppercase tracking-widest font-bold">
                      MINER REWARD
                   </div>
                </div>

              </div>
            </div>
          </div>
        </section>
"""

import sys

file_path = "/Users/sumangiri/Desktop/entangle/src/app/page.tsx"
with open(file_path, "r") as f:
    text = f.read()

# Locate the starting boundary of the old grid section
start_marker = "eyebrow=\"Real-time Fees. Real-time Rewards.\""
start_idx = text.find(start_marker)

if start_idx == -1:
    sys.exit("The keyword Real-time Fees not found.")

section_start = text.rfind("<section", 0, start_idx)
if section_start == -1:
    sys.exit("Start section not found")

end_idx = text.find("</section>", start_idx)
if end_idx == -1:
    sys.exit("End section not found")
    
end_idx += len("</section>\n")

final_text = text[:section_start] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
