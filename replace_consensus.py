html_blob = """
        <section id="consensus" className="w-full relative z-10 font-sans bg-[#020202]">
          {/* Faint crosshair grid borders matching the image background structure */}
          <div className="max-w-6xl mx-auto relative border-x border-[#1a1a1a] pt-24 pb-32 px-6 md:px-16">
            <div className="absolute top-24 left-[-20vw] right-[-20vw] h-[1px] bg-[#1a1a1a] pointer-events-none"></div>

            <motion.div initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUpVariant} className="relative z-10 pt-8">
              
              <div className="mb-20">
                <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight leading-tight">
                  Threshold signatures.<br />
                  <span className="text-[#888888]">No single validator.</span>
                </h2>
              </div>
              
              <div className="grid lg:grid-cols-[1.2fr_1fr] gap-12 lg:gap-20 items-center">
                
                {/* Left side Graphic */}
                <div className="relative flex flex-col items-center justify-center pt-10">
                  <div className="relative w-[340px] h-[340px]">
                    {/* The central dark square with glowing edges */}
                    <div className="absolute inset-[50px] bg-[#071317] border border-[#00d2ff]/20 flex items-center justify-center overflow-visible">
                      {/* Central shield in glowing circle */}
                      <div className="w-[100px] h-[100px] rounded-full border-[1.5px] border-[#00d2ff] flex items-center justify-center shadow-[0_0_40px_rgba(0,210,255,0.15)] relative z-10">
                        <svg className="w-10 h-10 text-[#00d2ff]" viewBox="0 0 24 24" fill="currentColor">
                          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                        </svg>
                      </div>
                      
                      {/* The 4 corner diagonal lines */}
                      <div className="absolute -top-[1px] -left-[1px] w-[30px] h-[1px] bg-[#444] rotate-45 origin-top-left -translate-x-[20px] -translate-y-[20px]"></div>
                      <div className="absolute -top-[1px] -right-[1px] w-[30px] h-[1px] bg-[#444] -rotate-45 origin-top-right translate-x-[20px] -translate-y-[20px]"></div>
                      <div className="absolute -bottom-[1px] -left-[1px] w-[30px] h-[1px] bg-[#444] -rotate-45 origin-bottom-left -translate-x-[20px] translate-y-[20px]"></div>
                      <div className="absolute -bottom-[1px] -right-[1px] w-[30px] h-[1px] bg-[#444] rotate-45 origin-bottom-right translate-x-[20px] translate-y-[20px]"></div>
                    </div>

                    {/* V1 - Top center */}
                    <div className="absolute top-[0px] left-1/2 -translate-x-1/2 w-12 h-12 rounded-full border-[1.5px] border-[#ff1a66] bg-[#050103] flex items-center justify-center text-[#ddd] text-xs font-mono z-10 shadow-[0_0_20px_rgba(255,26,102,0.15)]">V1</div>
                    
                    {/* V2 - Top right */}
                    <div className="absolute top-[60px] right-[10px] w-[46px] h-[46px] rounded-full border-[1.5px] border-[#ff1a66] bg-[#050103] flex items-center justify-center text-[#ddd] text-xs font-mono z-10 shadow-[0_0_20px_rgba(255,26,102,0.15)]">V2</div>
                    
                    {/* V3 - Bottom right */}
                    <div className="absolute bottom-[40px] right-[15px] w-[46px] h-[46px] rounded-full border-[1.5px] border-[#ff1a66] bg-[#050103] flex items-center justify-center text-[#ddd] text-xs font-mono z-10 shadow-[0_0_20px_rgba(255,26,102,0.15)]">V3</div>
                    
                    {/* V4 - Bottom left */}
                    <div className="absolute bottom-[40px] left-[15px] w-[46px] h-[46px] rounded-full border-[1.5px] border-[#ff1a66] bg-[#050103] flex items-center justify-center text-[#ddd] text-xs font-mono z-10 shadow-[0_0_20px_rgba(255,26,102,0.15)]">V4</div>

                    {/* V5 - Top left */}
                    <div className="absolute top-[60px] left-[10px] w-[46px] h-[46px] rounded-full border-[1.5px] border-[#ff1a66] bg-[#050103] flex items-center justify-center text-[#ddd] text-xs font-mono z-10 shadow-[0_0_20px_rgba(255,26,102,0.15)]">V5</div>
                  </div>

                  <div className="text-center mt-6 text-[#555] tracking-[0.2em] text-[10px] sm:text-[11px] font-mono">
                    N-OF-M CONSENSUS MODEL
                  </div>
                </div>

                {/* Right side Cards */}
                <div className="flex flex-col bg-[#050505] border border-[#ffffff0a] shadow-[0_0_50px_rgba(0,0,0,0.8)]">
                  
                  {/* Card 1 */}
                  <div className="p-8 md:p-10 border-b border-[#ffffff0a] border-l-[3px] border-l-[#ff1a66] bg-[#080809]">
                    <h3 className="text-white text-[19px] font-bold mb-5 tracking-wide">Multi-Chain Signatures</h3>
                    <div className="text-[#999] text-[14px] leading-[1.8] space-y-1">
                      <div>
                        <span className="text-white font-medium">EVM:</span> <span className="text-[#00d2ff] bg-[#00d2ff]/10 px-1.5 py-0.5 rounded font-mono text-[13px] border border-[#00d2ff]/10">secp256k1</span> / ecrecover
                      </div>
                      <div>
                        <span className="text-white font-medium">Non-EVM:</span> <span className="text-[#00d2ff] bg-[#00d2ff]/10 px-1.5 py-0.5 rounded font-mono text-[13px] border border-[#00d2ff]/10">ed25519</span> (Solana, SUI, Cosmos)
                      </div>
                    </div>
                  </div>

                  {/* Card 2 */}
                  <div className="p-8 md:p-10 border-b border-[#ffffff0a] border-l-[3px] border-l-[#00d2ff] bg-[#080809]">
                    <h3 className="text-white text-[19px] font-bold mb-5 tracking-wide">On-Chain Verification</h3>
                    <div className="text-[#888] text-[15px] mb-4">
                      Smart contracts enforce cryptographic proofs.
                    </div>
                    <div className="text-[#00d2ff] font-mono text-[13px] bg-[#00d2ff]/[0.08] border border-[#00d2ff]/10 py-1.5 px-3 rounded inline-block">
                      verifyMessage(msg_hash, sig_bundle)
                    </div>
                  </div>

                  {/* Card 3 */}
                  <div className="p-8 md:p-10 border-l-[3px] border-l-[#aaaaaa] bg-[#080809]">
                    <h3 className="text-white text-[19px] font-bold mb-5 tracking-wide">Trust Minimized</h3>
                    <div className="text-[#888] text-[15px] leading-relaxed max-w-[95%]">
                      No single validator can authorize a delivery.<br/>Consensus threshold required for all ops.
                    </div>
                  </div>

                </div>

              </div>
            </motion.div>
          </div>
        </section>
"""

import sys

file_path = "/Users/sumangiri/Desktop/entangle/src/app/page.tsx"
with open(file_path, "r") as f:
    text = f.read()

start_marker = "        <section className=\"my-32 py-16 px-6 md:px-12 max-w-7xl mx-auto w-full relative z-10\">\n          <motion.div initial=\"hidden\" whileInView=\"visible\" viewport={{ once: true }} variants={fadeUpVariant}>\n            <SectionHeader\n              eyebrow=\"Threshold signatures. No single validator.\""
start_idx = text.find(start_marker)

if start_idx == -1:
    # try slightly different search
    start_idx = text.find('eyebrow="Threshold signatures. No single validator."')
    if start_idx != -1:
        # backup to section
        start_idx = text.rfind("<section", 0, start_idx)

if start_idx == -1:
    sys.exit("Section not found")

# find end boundary for operators
end_idx = text.find('<section id="operators"', start_idx)
if end_idx == -1:
    sys.exit("Operators section not found")

final_text = text[:start_idx] + html_blob + "\n" + text[end_idx:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
