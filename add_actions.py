html_blob = """
        <section id="actions" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#111111] pt-16 pb-32 px-6 md:px-12 overflow-hidden">
            
            <div className="absolute top-[120px] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-0"></div>

            <div className="relative z-10 mb-16 pt-10">
              <h2 className="text-[48px] md:text-[54px] font-bold text-white tracking-tight leading-[1.1] mb-5">
                Start Building. Start Earning.
              </h2>
            </div>

            {/* 3 Columns architecture grid */}
            <div className="relative z-10 w-full max-w-[1020px] mx-auto flex flex-col lg:flex-row shadow-[0_30px_60px_rgba(0,0,0,0.8)] border-x border-b border-[#111111] rounded-b-[4px] bg-[#020202]">
              
              {/* Vertical Dividers for Desktop */}
              <div className="hidden lg:block absolute top-[0] bottom-0 left-[33.333%] w-[1px] bg-[#1a1a1a] pointer-events-none z-20"></div>
              <div className="hidden lg:block absolute top-[0] bottom-0 left-[66.666%] w-[1px] bg-[#1a1a1a] pointer-events-none z-20"></div>

              {/* 1. Developers */}
              <div className="flex-1 border-t-[3px] border-[#00d2ff] p-8 lg:p-10 flex flex-col relative z-10 border-b border-[#111] lg:border-b-0">
                 <div className="w-[50px] h-[50px] rounded-full bg-[#00d2ff]/10 flex items-center justify-center mb-8">
                    <svg className="w-5 h-5 text-[#00d2ff]" fill="none" stroke="currentColor" strokeWidth="2.5" viewBox="0 0 24 24" strokeLinecap="round" strokeLinejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                 </div>
                 <div className="text-white text-[28px] font-bold mb-4 tracking-tight">Developers</div>
                 <div className="text-[#888] text-[15px] leading-[1.7] mb-8 flex-grow">
                    Integrate omnichain messaging in minutes. One SDK for EVM, Solana, and Cosmos.
                 </div>
                 
                 <div className="font-mono text-[11px] text-[#777] leading-[1.8] mb-8">
                    <div><span className="text-[#00d2ff]">&gt;</span> npm install @entangle/sdk</div>
                    <div><span className="text-[#00d2ff]">&gt;</span> import {'{'} Entangle {'}'}</div>
                 </div>

                 <button className="w-full bg-[#00d2ff] hover:bg-[#00b0d9] text-black font-bold text-[11px] uppercase tracking-widest py-4 px-4 rounded-[4px] transition-colors mb-8 shadow-[0_0_20px_rgba(0,210,255,0.3)]">
                    READ THE DOCS
                 </button>
                 
                 <div className="text-[#888] text-[11px] font-mono uppercase tracking-widest hover:text-white cursor-pointer transition-colors flex items-center justify-center gap-2">
                    <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.699-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.462-1.11-1.462-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.564 9.564 0 0112 6.844c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.137 20.161 22 16.418 22 12c0-5.523-4.477-10-10-10z"/></svg> 
                    VIEW GITHUB
                 </div>
              </div>

              {/* 2. Operators */}
              <div className="flex-1 bg-[#020000] border-t-[3px] border-[#ff1a66] p-8 lg:p-10 flex flex-col relative z-10 border-b border-[#111] lg:border-b-0">
                 <div className="w-[50px] h-[50px] rounded-full bg-[#ff1a66]/10 flex items-center justify-center mb-8">
                    <svg className="w-5 h-5 text-[#ff1a66]" fill="currentColor" viewBox="0 0 24 24"><path d="M4 6h16v4H4zm0 8h16v4H4zm2-6h2v2H6zm0 8h2v2H6z"/></svg>
                 </div>
                 <div className="text-white text-[28px] font-bold mb-4 tracking-tight">Operators</div>
                 <div className="text-[#888] text-[15px] leading-[1.7] mb-8 flex-grow">
                    Secure the network and earn dual rewards. Run Validators, Scanners, or Relay Miners.
                 </div>
                 
                 <div className="font-mono text-[11px] text-[#777] leading-[1.8] mb-8">
                    <div><span className="text-[#ff1a66]">$</span> 70% Relay Rewards</div>
                    <div><span className="text-[#ff1a66]">$</span> 30% Scanner Rewards</div>
                 </div>

                 <button className="w-full bg-[#ff1a66] hover:bg-[#e01458] text-black font-bold text-[11px] uppercase tracking-widest py-4 px-4 rounded-[4px] transition-colors mb-8 shadow-[0_0_20px_rgba(255,26,102,0.3)]">
                    RUN A NODE
                 </button>
                 
                 <div className="text-[#888] text-[11px] font-mono uppercase tracking-widest hover:text-white cursor-pointer transition-colors flex items-center justify-center gap-2">
                    <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M5 9h4v12H5zm7-5h4v17h-4zm7 8h4v9h-4z"/></svg>
                    SUBNET STATS
                 </div>
              </div>

              {/* 3. Community */}
              <div className="flex-1 border-t-[3px] border-[#ffffff] p-8 lg:p-10 flex flex-col relative z-10 border-b lg:border-b-0 border-[#111]">
                 <div className="w-[50px] h-[50px] rounded-full bg-[#222] flex items-center justify-center mb-8">
                    <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05.02.01.03.03.04.04 1.14.83 1.93 1.94 1.93 3.41V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>
                 </div>
                 <div className="text-white text-[28px] font-bold mb-4 tracking-tight">Community</div>
                 <div className="text-[#888] text-[15px] leading-[1.7] mb-8 flex-grow">
                    Join the conversation. Governance proposals, ecosystem updates, and support.
                 </div>
                 
                 <div className="font-mono text-[11px] text-[#777] leading-[1.8] mb-8">
                    <div><span className="text-white">#</span> announcements</div>
                    <div><span className="text-white">#</span> governance</div>
                 </div>

                 <button className="w-full bg-white hover:bg-gray-200 text-black font-bold text-[11px] uppercase tracking-widest py-4 px-4 rounded-[4px] transition-colors mb-8 shadow-[0_0_20px_rgba(255,255,255,0.3)]">
                    JOIN DISCORD
                 </button>
                 
                 <div className="text-[#888] text-[11px] font-mono uppercase tracking-widest hover:text-white cursor-pointer transition-colors flex items-center justify-center text-center">
                    FOLLOW US
                 </div>
              </div>

            </div>

"""

import sys

file_path = "/Users/sumangiri/Desktop/entangle/src/app/page.tsx"
with open(file_path, "r") as f:
    text = f.read()

# Locate the starting boundary of the old actions section
start_marker = '<section id="actions"'
start_idx = text.find(start_marker)

if start_idx == -1:
    sys.exit("The keyword <section id=\"actions\" not found.")

# Locate the end boundary which is the Roadmap div
end_marker = '<div className="mt-16">' # the wrapper for roadmap
end_idx = text.find(end_marker, start_idx)
if end_idx == -1:
    sys.exit("End section not found")
    
final_text = text[:start_idx] + html_blob + "\n            " + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
