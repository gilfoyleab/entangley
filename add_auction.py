html_blob = """
        <section id="the-auction" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#111111] pt-16 pb-32 px-6 md:px-12 overflow-visible">
            
            {/* Horizontal Line separating sections */}
            <div className="absolute top-[170px] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-0"></div>

            <div className="relative z-10 mb-20 pt-10">
              <div className="text-[11px] font-mono tracking-[0.3em] text-[#ff1a66] mb-5 font-bold">The Auction</div>
              <h2 className="text-[44px] md:text-[54px] font-bold text-white tracking-tight leading-[1.1] mb-5">
                Sealed-Bid Velocity.
              </h2>
              <p className="text-[#888] text-[18px]">
                Fastest & cheapest miner wins execution rights.
              </p>
            </div>

            {/* Diagram container */}
            <div className="relative flex flex-col xl:flex-row items-center xl:items-stretch justify-center gap-[60px] xl:gap-[80px] w-full mt-16 max-w-[900px] mx-auto xl:mr-auto xl:ml-0">
              
              {/* 1. RELAY MINERS column */}
              <div className="flex flex-col gap-4 relative w-full sm:w-[240px] xl:w-[200px] shrink-0 xl:justify-center">
                <div className="text-[#666] text-[10px] font-mono tracking-widest text-center xl:text-left mb-2">Relay Miners</div>
                
                {/* Desktop connection lines drawn behind the items */}
                <div className="hidden xl:block absolute left-[100%] top-[45px] w-[30px] h-[155px] border-t border-b border-l-0 border-r border-[#333] translate-y-[0px] rounded-r-[6px] z-0"></div>
                <div className="hidden xl:block absolute left-[100%] ml-[30px] top-1/2 -translate-y-[2px] w-[40px] h-[1px] bg-[#333] z-0"></div>
                {/* Arrow head */}
                <div className="hidden xl:block absolute left-[100%] ml-[66px] top-1/2 -translate-y-[6px] w-[0] h-[0] border-t-[5px] border-b-[5px] border-l-[6px] border-transparent border-l-[#333]"></div>

                {[
                  { id: 'A' },
                  { id: 'B' },
                  { id: 'C' }
                ].map((miner) => (
                  <div key={miner.id} className="w-full bg-[#080808] border border-[#1f1f1f] rounded-[8px] p-4 py-4 flex items-center gap-4 relative z-10 shadow-lg">
                     <svg className="w-[18px] h-[18px] text-[#666] shrink-0" fill="currentColor" viewBox="0 0 24 24">
                       <path d="M4 6h16v4H4zm2 1h2v2H6z"/>
                       <path d="M4 14h16v4H4zm2 1h2v2H6z"/>
                     </svg>
                     <div>
                        <div className="text-white text-[13px] font-bold font-sans">Miner {miner.id}</div>
                        <div className="text-[#555] text-[10px] font-mono mt-[2px] whitespace-nowrap flex items-center">
                          Sealed Bid 
                          <svg className="w-[9px] h-[9px] ml-1.5 text-[#444] shrink-0" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM9 6c0-1.66 1.34-3 3-3s3 1.34 3 3v2H9V6zm9 14H6V10h12v10zm-6-3c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2z"/>
                          </svg>
                        </div>
                     </div>
                  </div>
                ))}
              </div>

              {/* 2. SCORING FORMULA container */}
              <div className="relative bg-[#050505] border border-[#222] rounded-[12px] p-8 md:p-10 w-full max-w-[440px] xl:w-[440px] shadow-[0_20px_60px_rgba(0,0,0,0.8)] z-10 shrink-0">
                
                {/* Top Floating Badge */}
                <div className="absolute -top-[16px] left-1/2 -translate-x-1/2 bg-[#020e14] border border-[#00d2ff] rounded-[30px] px-5 py-1.5 flex items-center justify-center gap-2 shadow-[0_0_15px_rgba(0,210,255,0.15)] whitespace-nowrap z-20">
                  <svg className="w-3.5 h-3.5 text-[#00d2ff]" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M15 1H9v2h6V1zm-4 13h2V8h-2v6zm8.03-6.61l1.42-1.42c-.43-.51-.9-.99-1.41-1.41l-1.42 1.42A8.962 8.962 0 0012 4c-4.97 0-9 4.03-9 9s4.03 9 9 9 9-4.03 9-9c0-2.12-.74-4.07-1.97-5.61zM12 20c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"/>
                  </svg>
                  <span className="text-[#00d2ff] font-bold text-[11px] font-mono tracking-wide mt-[1px]">2s Window</span>
                </div>

                <div className="text-center text-[#444] text-[10px] font-mono tracking-[0.2em] mb-7 mt-2">Scoring Formula</div>

                <div className="flex justify-between items-center gap-6">
                  <div className="text-[20px] font-bold font-mono tracking-tight leading-[2.2]">
                    <div className="text-[#888] mb-1 font-sans text-[22px] tracking-normal font-semibold">Score = </div>
                    <div>
                      <span className="text-[#00d2ff]">0.40</span> <span className="text-[#444] mx-[2px] text-[14px]">×</span> <span className="text-white">Latency</span>
                    </div>
                    <div>
                      <span className="text-[#555] mr-[5px] text-[14px]">+</span><span className="text-[#ff1a66]">0.40</span> <span className="text-[#444] mx-[2px] text-[14px]">×</span> <span className="text-white">Gas Cost</span>
                    </div>
                    <div>
                      <span className="text-[#555] mr-[5px] text-[14px]">+</span><span className="text-white">0.20</span> <span className="text-[#444] mx-[2px] text-[14px]">×</span> <span className="text-white">Accuracy</span>
                    </div>
                  </div>

                  <div className="w-[70px] h-[70px] shrink-0 mt-5 relative">
                     <svg className="w-[70px] h-[70px] transform -rotate-90" viewBox="0 0 36 36">
                        {/* Background Accuracy 20% (gray ring part) */}
                        <path
                          className="text-[#2a2a2a]"
                          strokeWidth="3.5"
                          stroke="currentColor"
                          fill="none"
                          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                        />
                        {/* Pink 40% (bottom part) */}
                        <path
                          className="text-[#ff1a66]"
                          strokeWidth="3.5"
                          strokeDasharray="40 100"
                          strokeDashoffset="-40"
                          strokeLinecap="round"
                          stroke="currentColor"
                          fill="none"
                          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                        />
                        {/* Cyan 40% (top right part) */}
                        <path
                          className="text-[#00d2ff]"
                          strokeWidth="3.5"
                          strokeDasharray="40 100"
                          strokeLinecap="round"
                          stroke="currentColor"
                          fill="none"
                          d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                        />
                     </svg>
                  </div>
                </div>

                {/* Arrow pointing to Winner Executes */}
                <div className="hidden xl:block absolute left-[100%] top-1/2 -translate-y-[2px] w-[35px] h-[1px] bg-[#333] z-0"></div>
                <div className="hidden xl:block absolute left-[100%] ml-[33px] top-1/2 -translate-y-[6px] w-[0] h-[0] border-t-[5px] border-b-[5px] border-l-[6px] border-transparent border-l-[#333]"></div>
              </div>

              {/* 3. WINNER EXECUTES */}
              <div className="w-full sm:w-[240px] xl:w-[150px] bg-[#020d15] border-[1.5px] border-[#00d2ff] rounded-[8px] p-6 lg:p-7 flex flex-col items-center justify-center gap-4 relative z-10 shadow-[0_0_25px_rgba(0,210,255,0.15)] shrink-0 xl:self-center">
                 <svg className="w-[30px] h-[30px] text-[#00d2ff]" fill="currentColor" viewBox="0 0 24 24">
                   <path d="M19 5h-2V3a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v2H5a1 1 0 0 0-1 1v2.22A4.78 4.78 0 0 0 8.78 13h.14a4.98 4.98 0 0 0 2.08 3h-2a1 1 0 0 0-1 1v2h-2v2h12v-2h-2v-2a1 1 0 0 0-1-1h-2a4.98 4.98 0 0 0 2.08-3h.14A4.78 4.78 0 0 0 19 8.22V6a1 1 0 0 0-1-1zM6 8.22V7h1v4.61A2.78 2.78 0 0 1 6 8.22zM17 7v1.22A2.78 2.78 0 0 1 14.39 12H18V7z"/>
                 </svg>
                 <div className="text-white text-[12px] font-bold text-center leading-tight tracking-wide">
                   Winner<br/>Executes
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

# Locate the starting boundary
start_marker = "eyebrow=\"THE AUCTION\""
start_idx = text.find(start_marker)

if start_idx == -1:
    sys.exit("The keyword THE AUCTION not found.")

# Backtrack to the section containing it
section_start = text.rfind("<section", 0, start_idx)
if section_start == -1:
    sys.exit("Start section not found")

# Locate the end boundary
end_marker = "</section>"
end_idx = text.find(end_marker, start_idx)
if end_idx == -1:
    sys.exit("End section not found")
    
end_idx += len("</section>\n")

# Inject
final_text = text[:section_start] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
