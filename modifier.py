html_blob = """
        <section id="simple-integration" className="py-24 w-full relative z-10 my-16 font-sans">
          {/* The faint grid background */}
          <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.03)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.03)_1px,transparent_1px)] bg-[size:4rem_4rem] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_100%,transparent_100%)] pointer-events-none -z-10"></div>

          <motion.div initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeUpVariant} className="relative max-w-5xl mx-auto px-6 md:px-12">
            <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold text-white tracking-tight mb-20">
              Simple Integration.
            </h2>

            <div className="relative max-w-4xl mx-auto flex flex-col md:flex-row gap-6 md:gap-10">
              
              {/* Connector Line left side (Desktop) */}
              <div className="w-4 shrink-0 relative hidden md:block">
                <div className="absolute left-1/2 top-[70px] bottom-[70px] w-[2px] bg-gradient-to-b from-[#00d2ff] via-[#333] to-[#ff1a66] -translate-x-1/2 flex flex-col justify-between items-center z-10">
                  <div className="w-[10px] h-[10px] rounded-full bg-[#00d2ff] -mt-1 shadow-[0_0_10px_rgba(0,210,255,0.8)]"></div>
                  <div className="w-[10px] h-[10px] rounded-full bg-[#ff1a66] -mb-1 shadow-[0_0_10px_rgba(255,26,102,0.8)]"></div>
                </div>
              </div>

              <div className="flex-1 flex flex-col gap-6 relative">

                {/* Source Block Wrapper */}
                <div className="relative pt-6">
                  <div className="absolute right-0 top-0 text-[#00d2ff] text-[10px] md:text-[11px] font-mono tracking-widest font-semibold uppercase flex items-center gap-2">
                    SOURCE <span className="text-sm md:text-lg leading-none">&rarr;</span>
                  </div>

                  <div className="rounded-[12px] border border-[#00d2ff]/20 bg-[#000000] shadow-[0_0_30px_rgba(0,0,0,0.4)] w-full font-mono text-[12px] sm:text-[13px] md:text-[14px]">
                    <div className="bg-[#050505] border-b border-[#ffffff10] py-3 px-5 flex items-center gap-3">
                      <div className="flex gap-2 shrink-0">
                        <div className="w-3 h-3 rounded-full bg-[#ff5f56]" />
                        <div className="w-3 h-3 rounded-full bg-[#ffbd2e]" />
                        <div className="w-3 h-3 rounded-full bg-[#27c93f]" />
                      </div>
                      <div className="text-gray-500 ml-2 overflow-hidden text-ellipsis whitespace-nowrap">Sender.sol (Source Chain)</div>
                    </div>
                    
                    <pre className="p-6 md:p-8 leading-relaxed text-[#c9c9d1] overflow-x-auto">
                      <code>
        <span className="text-[#ff1a66]">function</span> <span className="text-[#00d2ff]">sendCrossChain</span>(<span className="text-gray-400">uint256</span> amount) <span className="text-[#ff1a66]">external payable</span> {"{"}
        {"\\n  "}<span className="text-[#00d2ff]">bytes</span> <span className="text-[#ff1a66]">memory</span> payload = abi.<span className="text-[#00d2ff]">encode</span>(amount);
        {"\\n  "}<span className="text-[#00d2ff]">uint256</span> fee = entangle.<span className="text-[#00d2ff]">getRequiredFee</span>(dstChainId, payload.length);
        {"\\n\\n  "}<span className="text-gray-500">// 1. Dispatch Message</span>
        {"\\n  "}entangle.<span className="text-[#00d2ff]">sendMessage</span>{"{"}<span className="text-[#ff1a66]">value</span>: fee{"}"}(dstChainId, dstAddr, payload);
        {"\\n"}{"}"}
                      </code>
                    </pre>
                  </div>
                </div>

                {/* Arrow down */}
                <div className="flex justify-center -my-2 relative z-10 py-2">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#666" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <line x1="12" y1="5" x2="12" y2="19"></line>
                    <polyline points="19 12 12 19 5 12"></polyline>
                  </svg>
                </div>

                {/* Destination Block Wrapper */}
                <div className="relative pt-6">
                  <div className="absolute right-0 top-0 text-[#ff1a66] text-[10px] md:text-[11px] font-mono tracking-widest font-semibold uppercase flex items-center gap-2">
                    DESTINATION <span className="text-sm md:text-lg leading-none">&rarr;</span>
                  </div>

                  <div className="rounded-[12px] border border-[#ff1a66]/20 bg-[#000000] shadow-[0_0_30px_rgba(0,0,0,0.4)] w-full font-mono text-[12px] sm:text-[13px] md:text-[14px]">
                    <div className="bg-[#050505] border-b border-[#ffffff10] py-3 px-5 flex items-center gap-3">
                      <div className="flex gap-2 shrink-0">
                        <div className="w-3 h-3 rounded-full bg-[#ff5f56]" />
                        <div className="w-3 h-3 rounded-full bg-[#ffbd2e]" />
                        <div className="w-3 h-3 rounded-full bg-[#27c93f]" />
                      </div>
                      <div className="text-gray-500 ml-2 overflow-hidden text-ellipsis whitespace-nowrap">Receiver.sol (Destination Chain)</div>
                    </div>
                    
                    <pre className="p-6 md:p-8 leading-relaxed text-[#c9c9d1] overflow-x-auto">
                      <code>
        <span className="text-[#ff1a66]">function</span> <span className="text-[#00d2ff]">receiveEntangleMessage</span>(
        {"\\n  "}<span className="text-[#00d2ff]">bytes</span> <span className="text-[#ff1a66]">memory</span> payload, <span className="text-[#00d2ff]">bytes</span> <span className="text-[#ff1a66]">memory</span> sigs, ...
        {"\\n"}) <span className="text-[#ff1a66]">external payable</span> {"{"}
        {"\\n  "}<span className="text-gray-500">// 2. Verify Origin (Security)</span>
        {"\\n  "}<span className="text-[#00d2ff]">require</span>(<span className="text-[#ff1a66]">msg.sender</span> == <span className="text-[#00d2ff]">address</span>(entangle), "Only Entangle");
        {"\\n\\n  "}<span className="text-gray-500">// 3. Execute Logic</span>
        {"\\n  "}<span className="text-[#00d2ff]">uint256</span> amount = abi.<span className="text-[#00d2ff]">decode</span>(payload, (<span className="text-[#00d2ff]">uint256</span>));
        {"\\n  "}<span className="text-[#00d2ff]">_mint</span>(amount);
        {"\\n"}{"}"}
                      </code>
                    </pre>
                  </div>
                </div>

              </div>
            </div>
          </motion.div>
        </section>
"""

import sys

file_path = "/Users/sumangiri/Desktop/entangle/src/app/page.tsx"
with open(file_path, "r") as f:
    text = f.read()

simple_start = text.find("{/* --- SIMPLE INTEGRATION SECTION MATCHING SCREENSHOT --- */}")
if simple_start != -1:
    simple_end = text.find("        </section>", simple_start) + len("        </section>\n")
    if text.find("        </section>", simple_start) != -1:
        text = text[:simple_start] + text[simple_end:]

alt_simple_start = text.find('<section id="simple-integration"')
if alt_simple_start != -1:
    simple_end = text.find("</section>", alt_simple_start) + len("</section>\n")
    text = text[:alt_simple_start] + text[simple_end:]

chain_support_start = text.find('<section id="chain-support"')
if chain_support_start == -1:
    sys.exit("Chain support not found")

chain_support_end = text.find("</section>", chain_support_start) + len("</section>\n")

final_text = text[:chain_support_end] + "\n" + html_blob + "\n" + text[chain_support_end:]

with open(file_path, "w") as f:
    f.write(final_text)

print("Done")
