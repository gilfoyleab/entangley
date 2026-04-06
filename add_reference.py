html_blob = """
        <section id="reference-run" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#111111] pt-12 pb-32 px-6 md:px-12 overflow-hidden">
            
            <div className="absolute top-[100px] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-0"></div>
            {/* Very faint vertical separator down the middle */}
            <div className="absolute top-0 bottom-0 left-[35%] w-[1px] bg-[#1a1a1a] pointer-events-none z-0 hidden lg:block"></div>

            <div className="relative z-10 mb-16 pt-5">
              <h2 className="text-[48px] md:text-[60px] font-bold text-white tracking-tight leading-[1.1] mb-5">
                It&apos;s Live.
              </h2>
            </div>

            {/* Top Metrics Row */}
            <div className="relative z-10 flex flex-col md:flex-row gap-6 mb-16 w-full max-w-[950px] mx-auto">
              {/* 8.3s */}
              <div className="flex-1 border-l-[3px] border-[#00d2ff] bg-[#02070c] p-6 shadow-lg">
                 <div className="text-[54px] font-bold text-[#00d2ff] tracking-tighter leading-none mb-3 drop-shadow-[0_0_15px_rgba(0,210,255,0.2)] mt-1">8.3s</div>
                 <div className="text-[#888] text-[10px] font-mono tracking-widest mb-1.5 font-semibold">Fastest Delivery</div>
                 <div className="text-[#555] text-[10px] font-mono tracking-widest leading-relaxed">Solana &rarr; Arbitrum</div>
              </div>

              {/* 8/8 */}
              <div className="flex-1 border-l-[3px] border-[#00e65b] bg-[#020b05] p-6 shadow-lg">
                 <div className="text-[54px] font-bold text-[#00e65b] tracking-tighter leading-none mb-3 drop-shadow-[0_0_15px_rgba(0,230,91,0.2)] mt-1">8/8</div>
                 <div className="text-[#888] text-[10px] font-mono tracking-widest mb-1.5 font-semibold">Consecutive Runs</div>
                 <div className="text-[#555] text-[10px] font-mono tracking-widest leading-relaxed">100% Success Rate</div>
              </div>

              {/* 213K */}
              <div className="flex-1 border-l-[3px] border-[#ff1a66] bg-[#0f0205] p-6 shadow-lg">
                 <div className="text-[54px] font-bold text-[#ff1a66] tracking-tighter leading-none mb-3 drop-shadow-[0_0_15px_rgba(255,26,102,0.2)] mt-1">213K</div>
                 <div className="text-[#888] text-[10px] font-mono tracking-widest mb-1.5 font-semibold">Gas Used</div>
                 <div className="text-[#555] text-[10px] font-mono tracking-widest leading-relaxed">Reference Delivery</div>
              </div>
            </div>

            {/* Main Reference Run Container */}
            <div className="relative z-10 w-full max-w-[950px] mx-auto border border-[#222] bg-[#0a0a0a] rounded-[10px] shadow-[0_20px_50px_rgba(0,0,0,0.8)] overflow-hidden">
              
              {/* Header Slice */}
              <div className="bg-[#121212] px-6 py-3 flex items-center justify-between border-b border-[#222]">
                <div className="font-mono text-[11px] tracking-widest">
                   <span className="text-[#666]">Reference Run ID:</span>
                   <span className="text-white font-bold ml-2">#TEST-2026-03-17-A</span>
                </div>
                <div className="bg-[#00e65b] text-black font-bold font-mono text-[10px] tracking-widest px-3 py-1.5 rounded-[4px] flex items-center gap-1.5 shadow-[0_0_15px_rgba(0,230,91,0.3)]">
                   <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" strokeWidth="3" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round"><path d="M5 13l4 4L19 7"></path></svg>
                   Verified
                </div>
              </div>

              {/* Execution Diagram */}
              <div className="relative px-6 py-16 md:py-24 flex flex-col md:flex-row items-center justify-between gap-10 md:gap-0">
                 
                 {/* Connecting Line (drawn in background) */}
                 <div className="hidden md:block absolute top-[132px] left-[18%] right-[18%] h-[1.5px] bg-gradient-to-r from-[#00d2ff]/80 via-[#111111] to-[#00d2ff]/80 z-0 shadow-[0_0_15px_rgba(0,210,255,0.4)]"></div>

                 {/* Left Node (Sepolia) */}
                 <div className="relative z-10 flex flex-col items-center text-center w-full md:w-[180px]">
                    <div className="w-[72px] h-[72px] rounded-full border-[2px] border-[#00d2ff] bg-[#020406] shadow-[0_0_20px_rgba(0,210,255,0.3)] flex items-center justify-center mb-6 z-10">
                       <svg className="w-[30px] h-[30px] text-white" viewBox="0 0 32 32" fill="currentColor">
                         <path d="M15.925 23.969L15.823 24l-7.447-4.391 7.553 10.638 7.57-10.638-7.574 4.36zM15.986 0L8.358 12.67l7.625 4.542 7.643-4.542L15.986 0z" />
                       </svg>
                    </div>
                    <div className="text-white text-[18px] font-bold tracking-wide mb-3">Sepolia</div>
                    <div className="text-[#666] text-[12px] mb-2 font-mono whitespace-nowrap tracking-tight">Message Dispatched</div>
                    <div className="bg-[#00d2ff]/10 text-[#00d2ff] border border-[#00d2ff]/20 rounded-[4px] px-3 py-1 font-mono text-[11px] mb-8 min-w-[140px]">
                       0x4f90576e...
                    </div>
                    <div className="text-[#555] text-[10px] bg-transparent font-mono tracking-widest mt-1">Block 10464665</div>
                 </div>

                 {/* Middle Node (ENTANGLE RELAY) */}
                 <div className="relative z-10 w-[170px] bg-[#141414] border border-[#2a2a2a] rounded-[8px] p-5 flex flex-col items-center text-center shadow-[0_0_40px_rgba(0,0,0,0.8)] mt-[-20px] md:mt-[-50px]">
                    <div className="text-[#777] text-[10px] font-mono tracking-widest mb-1">Entangle Relay</div>
                    <div className="text-white text-[28px] font-bold tracking-tight mb-0.5">8.3s</div>
                    <div className="flex items-center gap-1 text-[#00e65b] text-[9px] font-bold tracking-widest font-mono mt-1">
                       <svg className="w-2.5 h-2.5" fill="currentColor" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
                       Optimized
                    </div>
                 </div>

                 {/* Right Node (Arbitrum) */}
                 <div className="relative z-10 flex flex-col items-center text-center w-full md:w-[180px]">
                    <div className="w-[72px] h-[72px] rounded-full border-[2px] border-[#00d2ff] bg-[#020406] shadow-[0_0_20px_rgba(0,210,255,0.3)] flex items-center justify-center mb-6 z-10">
                       <svg className="w-[30px] h-[30px] text-white" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M12 2L2 7l10 5 10-5-10-5zm0 6l-10 5 10 5 10-5-10-5zm0 6l-10 5 10 5 10-5-10-5z"/>
                       </svg>
                    </div>
                    <div className="text-white text-[18px] font-bold tracking-wide mb-3 whitespace-nowrap">Arbitrum Sepolia</div>
                    <div className="text-[#666] text-[12px] mb-2 font-mono whitespace-nowrap tracking-tight">Message Received</div>
                    <div className="bg-[#00d2ff]/10 text-[#00d2ff] border border-[#00d2ff]/20 rounded-[4px] px-3 py-1 font-mono text-[11px] mb-8 min-w-[140px]">
                       0xf802b3b6...
                    </div>
                    <div className="text-[#555] text-[10px] bg-transparent font-mono tracking-widest mt-1">isRelayed = true</div>
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

# I will find the end of the <section id="realtime-fees"> tag to append this after it.
ops_id = '<section id="realtime-fees"'
start_idx = text.find(ops_id)
if start_idx == -1:
    sys.exit("realtime-fees section not found")

end_idx = text.find("</section>", start_idx)
if end_idx == -1:
    sys.exit("Section close not found for realtime-fees")

end_idx += len("</section>\n")

final_text = text[:end_idx] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
