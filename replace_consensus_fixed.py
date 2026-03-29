html_blob = """
        <section id="consensus" className="w-full relative z-10 font-sans bg-[#000]">
          <div className="max-w-[1100px] mx-auto w-full relative border-x border-[#1a1a1a] pb-24 px-6 md:px-12">
            
            {/* Horizontal Grid Lines */}
            <div className="absolute top-[160px] md:top-[180px] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-0"></div>
            <div className="absolute top-[480px] md:top-[620px] left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none z-0"></div>

            <div className="relative z-10 pt-16 md:pt-20">
              <h2 className="text-[36px] sm:text-[46px] md:text-[54px] font-bold text-white tracking-tight leading-[1.1]">
                Threshold signatures.<br />
                <span className="text-[#888]">No single validator.</span>
              </h2>
            </div>

            <div className="relative z-10 mt-12 md:mt-16 grid lg:grid-cols-[1fr_480px] gap-12 lg:gap-8 items-center">
              
              {/* Graphical representation of the consensus model */}
              <div className="relative flex flex-col items-center justify-center">
                <div className="relative w-[280px] h-[280px]">
                  
                  {/* Central Faint Blue Box */}
                  <div className="absolute inset-[35px] bg-[#0c1f26] flex items-center justify-center">
                    
                    {/* Glowing Cyan Shield & Circle */}
                    <div className="w-[86px] h-[86px] rounded-full border-[1.5px] border-[#00d2ff] flex items-center justify-center z-10 shadow-[0_0_20px_rgba(0,210,255,0.2)]">
                      <svg className="w-[38px] h-[38px] text-[#00d2ff]" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                      </svg>
                    </div>

                    {/* Faint corner lines pointing perfectly strictly to the 4 corners of the box */}
                    <div className="absolute -top-[16px] -left-[16px] w-[32px] h-[1px] bg-[#555] rotate-45"></div>
                    <div className="absolute -top-[16px] -right-[16px] w-[32px] h-[1px] bg-[#555] -rotate-45"></div>
                    <div className="absolute -bottom-[16px] -left-[16px] w-[32px] h-[1px] bg-[#555] -rotate-45"></div>
                    <div className="absolute -bottom-[16px] -right-[16px] w-[32px] h-[1px] bg-[#555] rotate-45"></div>
                  </div>

                  {/* V1 - Top center */}
                  <div className="absolute top-[0px] left-1/2 -translate-x-1/2 w-[34px] h-[34px] rounded-full border border-[#ff1a66] bg-[#000] text-[#ccc] text-[10px] sm:text-[11px] font-mono flex items-center justify-center z-20 hover:bg-[#ff1a66]/20 transition-colors">V1</div>
                  
                  {/* V2 - Top right */}
                  <div className="absolute top-[60px] right-[-4px] w-[34px] h-[34px] rounded-full border border-[#ff1a66] bg-[#000] text-[#ccc] text-[10px] sm:text-[11px] font-mono flex items-center justify-center z-20 hover:bg-[#ff1a66]/20 transition-colors">V2</div>
                  
                  {/* V3 - Bottom right */}
                  <div className="absolute bottom-[30px] right-[10px] w-[34px] h-[34px] rounded-full border border-[#ff1a66] bg-[#000] text-[#ccc] text-[10px] sm:text-[11px] font-mono flex items-center justify-center z-20 hover:bg-[#ff1a66]/20 transition-colors">V3</div>
                  
                  {/* V4 - Bottom left */}
                  <div className="absolute bottom-[30px] left-[10px] w-[34px] h-[34px] rounded-full border border-[#ff1a66] bg-[#000] text-[#ccc] text-[10px] sm:text-[11px] font-mono flex items-center justify-center z-20 hover:bg-[#ff1a66]/20 transition-colors">V4</div>
                  
                  {/* V5 - Top left */}
                  <div className="absolute top-[60px] left-[-4px] w-[34px] h-[34px] rounded-full border border-[#ff1a66] bg-[#000] text-[#ccc] text-[10px] sm:text-[11px] font-mono flex items-center justify-center z-20 hover:bg-[#ff1a66]/20 transition-colors">V5</div>
                </div>

                <div className="mt-8 text-center text-[#555] tracking-[0.2em] text-[10px] font-mono">
                  N-OF-M CONSENSUS MODEL
                </div>
              </div>

              {/* Stacked Highlighted Cards */}
              <div className="flex flex-col bg-[#050505] shadow-[0_0_60px_rgba(0,0,0,0.8)] border border-[#ffffff0a]">
                
                {/* Multi-Chain Signatures */}
                <div className="border-b border-[#ffffff0a] border-l-[3px] border-l-[#ff1a66] p-7 md:p-9 bg-[#040404]">
                  <h3 className="text-white text-[17px] font-bold mb-5 tracking-wide">Multi-Chain Signatures</h3>
                  <div className="text-[14px]">
                    <div className="mb-2">
                      <span className="text-white">EVM:</span> <span className="bg-[#0b1d26] text-[#00d2ff] px-2 py-0.5 rounded text-[13px] mx-1 border border-[#00d2ff]/10 font-mono">secp256k1</span> <span className="text-[#888]">/ ecrecover</span>
                    </div>
                    <div>
                      <span className="text-white inline-block mt-0.5">Non-EVM:</span> <span className="bg-[#0b1d26] text-[#00d2ff] px-2 py-0.5 rounded text-[13px] mx-1 border border-[#00d2ff]/10 font-mono">ed25519</span> <span className="text-[#888]">(Solana, SUI, Cosmos)</span>
                    </div>
                  </div>
                </div>

                {/* On-Chain Verification */}
                <div className="border-b border-[#ffffff0a] border-l-[3px] border-l-[#00d2ff] p-7 md:p-9 bg-[#040404]">
                  <h3 className="text-white text-[17px] font-bold mb-4 tracking-wide">On-Chain Verification</h3>
                  <p className="text-[#888] text-[14px] mb-5">Smart contracts enforce cryptographic proofs.</p>
                  <div className="bg-[#0b1d26] border border-[#00d2ff]/10 text-[#00d2ff] font-mono text-[13px] px-3 py-1.5 inline-block rounded">
                    verifyMessage(msg_hash, sig_bundle)
                  </div>
                </div>

                {/* Trust Minimized */}
                <div className="border-l-[3px] border-l-[#cccccc] p-7 md:p-9 bg-[#040404]">
                  <h3 className="text-white text-[17px] font-bold mb-4 tracking-wide">Trust Minimized</h3>
                  <p className="text-[#888] text-[14px] leading-relaxed max-w-sm">
                    No single validator can authorize a delivery.<br />
                    Consensus threshold required for all ops.
                  </p>
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

start_marker = '<section id="consensus"'
start_idx = text.find(start_marker)

if start_idx == -1:
    sys.exit("Section not found")

end_idx = text.find('</section>', start_idx)
if end_idx == -1:
    sys.exit("Section close not found")

end_idx += len("</section>\n")

final_text = text[:start_idx] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
