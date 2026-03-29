html_blob = """
        <section id="scoring" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#111111] pt-12 pb-20 px-6 md:px-12">
            
            {/* The top crosshair grid line */}
            <div className="absolute top-[120px] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-0"></div>

            <div className="relative z-10 mb-16 pt-5 flex flex-col md:flex-row md:items-end justify-between gap-6 pb-6">
              <h2 className="text-[44px] md:text-[54px] font-bold text-white tracking-tight leading-[1.1]">
                5-Dimension Scoring.
              </h2>
              <p className="text-[#888] text-[15px] md:text-[16px] max-w-[280px] md:text-right leading-relaxed mb-1 md:mr-2">
                Quality drives rewards. Miners are scored on every delivery.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-y-16 mt-8 relative z-10 w-full max-w-[1020px] mx-auto">
              
              {/* Central vertical divider line on desktop underlying the grid */}
              <div className="absolute top-[30px] bottom-[-50px] left-1/2 -translate-x-1/2 w-[1px] bg-[#1a1a1a] pointer-events-none z-0 hidden lg:block"></div>
              {/* Second horizontal line slicing the grid */}
              <div className="absolute top-[50%] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-10 hidden lg:block translate-y-[20px]"></div>

              {/* 1. Latency (25%) */}
              <div className="relative border-l-[3px] border-l-[#00d2ff] bg-gradient-to-r from-[#00d2ff]/[0.05] to-transparent py-4 pl-6 pr-4 lg:pr-8 mx-0 mb-6 lg:mb-0 w-[90%]">
                <div className="absolute top-4 right-4 bg-[#1a1a1a] text-[#555] text-[10px] font-mono px-1.5 py-0.5 rounded leading-none">D1</div>
                <div className="text-white text-[20px] font-bold tracking-wide mb-1">Latency</div>
                <div className="text-[44px] font-bold text-[#00d2ff] tracking-tighter leading-none mb-4">25%</div>
                <div className="text-[#888] text-[13px] leading-relaxed max-w-[95%]">
                  Time from source dispatch to destination delivery measured in ms.
                </div>
              </div>

              {/* 2. Confirmation (25%) */}
              <div className="relative border-l-[3px] border-l-[#00d2ff] bg-gradient-to-r from-[#00d2ff]/[0.05] to-transparent py-4 pl-6 pr-4 lg:pr-8 mx-0 lg:ml-4 lg:mr-[20px] mb-6 lg:mb-0 z-20 w-[90%] lg:w-auto">
                <div className="absolute top-4 right-4 bg-[#1a1a1a] text-[#555] text-[10px] font-mono px-1.5 py-0.5 rounded leading-none">D2</div>
                <div className="text-white text-[20px] font-bold tracking-wide mb-1">Confirmation</div>
                <div className="text-[44px] font-bold text-[#00d2ff] tracking-tighter leading-none mb-4">25%</div>
                <div className="text-[#888] text-[13px] leading-relaxed max-w-[90%]">
                  Delivery within promised deadline.<br/>Missed deadlines = zero score.
                </div>
              </div>

              {/* 3. Gas Efficiency (20%) */}
              <div className="relative border-l-[3px] border-l-[#ff1a66] bg-[#050102] bg-gradient-to-r from-[#ff1a66]/[0.04] to-transparent py-8 pl-8 pr-4 lg:pr-8 mx-0 lg:ml-6 mb-6 lg:mb-0 z-20 overflow-hidden shadow-[0_10px_30px_rgba(0,0,0,0.5)]">
                <div className="absolute inset-0 border border-[#ffffff05] rounded-[4px] pointer-events-none"></div>
                <div className="absolute top-6 right-6 bg-[#1a1a1a] text-[#555] text-[10px] font-mono px-1.5 py-0.5 rounded leading-none">D3</div>
                <div className="text-white text-[20px] font-bold tracking-wide mb-1">Gas Efficiency</div>
                <div className="text-[44px] font-bold text-[#ff1a66] tracking-tighter leading-none mb-4">20%</div>
                <div className="text-[#888] text-[13px] leading-relaxed max-w-[90%] relative z-10">
                  Optimizing on-chain costs vs. oracle estimates.
                </div>
              </div>

              {/* 4. Integrity (15%) - NOTE 15% IS ON TOP */}
              <div className="relative border-l-[3px] border-l-[#ff1a66] bg-[#050102] bg-gradient-to-r from-[#ff1a66]/[0.04] to-transparent py-8 pl-8 pr-4 lg:pr-8 mx-0 mt-8 mb-6 lg:mb-0 w-[95%] z-20 shadow-[0_10px_30px_rgba(0,0,0,0.5)]">
                 <div className="absolute inset-0 border border-[#ffffff05] rounded-[4px] pointer-events-none"></div>
                <div className="absolute top-6 right-6 bg-[#1a1a1a] text-[#555] text-[10px] font-mono px-1.5 py-0.5 rounded leading-none">D4</div>
                <div className="text-[44px] font-bold text-[#ff1a66] tracking-tighter leading-none mb-1">15%</div>
                <div className="text-white text-[20px] font-bold tracking-wide mb-3">Integrity</div>
                <div className="text-[#888] text-[13px] leading-relaxed max-w-[85%] relative z-10">
                  Payload hash matching source event exactly.
                </div>
              </div>

              {/* 5. Reliability (15%) */}
              <div className="relative border-l-[3px] border-l-[#ff1a66] bg-gradient-to-r from-[#ff1a66]/[0.05] to-transparent py-4 pl-6 pr-4 lg:pr-8 mx-0 mt-8 lg:ml-4 lg:mr-[20px] mb-6 lg:mb-0 w-[90%] lg:w-auto z-20">
                <div className="absolute top-4 right-4 bg-[#1a1a1a] text-[#555] text-[10px] font-mono px-1.5 py-0.5 rounded leading-none">D5</div>
                <div className="text-white text-[20px] font-bold tracking-wide mb-1">Reliability</div>
                <div className="text-[44px] font-bold text-[#ff1a66] tracking-tighter leading-none mb-4">15%</div>
                <div className="text-[#888] text-[13px] leading-relaxed max-w-[90%]">
                  Historical uptime and successful delivery rate.
                </div>
              </div>

              {/* 6. Blended Score Box */}
              <div className="relative border border-[#222] bg-[#0c0c0c] rounded-[4px] p-6 lg:p-8 mt-12 mx-0 lg:ml-6 shadow-2xl z-20 lg:-mr-12">
                <div className="text-[#666] text-[10px] font-mono tracking-widest uppercase mb-6 font-bold">BLENDED SCORE</div>
                <div className="font-mono text-[14px] leading-[1.8]">
                   <div className="text-[#999] mb-2 font-sans tracking-wide">Score = </div>
                   <div><span className="text-[#00d2ff]">0.70</span> <span className="text-[#555] mx-1 text-xs px-0.5">×</span> <span className="text-[#ddd]">Exec +</span></div>
                   <div><span className="text-[#00d2ff]">0.30</span> <span className="text-[#555] mx-1 text-xs px-0.5">×</span> <span className="text-[#ddd]">Bid</span></div>
                </div>
              </div>

            </div>

            {/* Sub-footer scale line */}
            <div className="relative z-10 w-full max-w-[1020px] mx-auto mt-24 mb-6 flex pl-2 pr-2">
               {/* Exactly left side Cyan 50%, right side Pink 50% split */}
               <div className="h-[6px] w-[50%] bg-[#00d2ff] shadow-[0_0_20px_rgba(0,210,255,0.4)]"></div>
               <div className="h-[6px] w-[50%] bg-[#ff1a66] shadow-[0_0_20px_rgba(255,26,102,0.4)]"></div>
            </div>

          </div>
        </section>
"""

import sys

file_path = "/Users/sumangiri/Desktop/entangle/src/app/page.tsx"
with open(file_path, "r") as f:
    text = f.read()

# I will find the end of the <section id="the-auction"> tag.
ops_id = '<section id="the-auction"'
start_idx = text.find(ops_id)
if start_idx == -1:
    sys.exit("the-auction section not found")

end_idx = text.find("</section>", start_idx)
if end_idx == -1:
    sys.exit("Section close not found for the-auction")

end_idx += len("</section>\n")

# Inject the new section
final_text = text[:end_idx] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
