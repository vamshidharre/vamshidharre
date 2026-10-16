import os

OUTPUT_DIR = r"C:\Users\vamsh\.gemini\antigravity\scratch\vamshidharre\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def write_svg(filename, content):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated {filename}")

# ==========================================
# 1. Section Titles (viewBox 1200x120)
# ==========================================
def generate_title(num, tag, title_main, title_italic, right_mono, prefix):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="{num} {tag}: {title_main} {title_italic}">
  <defs>
    <linearGradient id="{prefix}-line" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">
      <stop offset="0" stop-color="#38BDF8"/>
      <stop offset=".6" stop-color="#0284C7"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="{prefix}-sheen" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#7DD3FC"/>
      <stop offset=".5" stop-color="#F8FAFC"/>
      <stop offset="1" stop-color="#7DD3FC"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1500 0;1500 0" keyTimes="0;.4;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="{prefix}-pulse">
      <stop offset="0" stop-color="#F8FAFC"/>
      <stop offset=".5" stop-color="#38BDF8" stop-opacity=".6"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .{prefix}-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .{prefix}-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .{prefix}-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .{prefix}-in {{ animation: {prefix}-in 1.1s cubic-bezier(.16,1,.3,1) both; }}
    .{prefix}-d2 {{ animation-delay: .2s; }} .{prefix}-d3 {{ animation-delay: .45s; }}
    .{prefix}-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: {prefix}-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes {prefix}-in {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes {prefix}-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .{prefix}-in {{ animation: none; }} .{prefix}-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g class="{prefix}-in">
    <text class="{prefix}-mono" x="40" y="34" font-size="12" letter-spacing="3" fill="#38BDF8"><tspan fill="#BAE6FD">{num}</tspan>   {tag}</text>
  </g>
  <g class="{prefix}-in {prefix}-d2">
    <text class="{prefix}-serif" x="38" y="84" font-size="44" font-weight="300" letter-spacing="-1" fill="#F8FAFC">{title_main} <tspan font-style="italic" fill="url(#{prefix}-sheen)">{title_italic}</tspan></text>
  </g>
  <g class="{prefix}-in {prefix}-d3">
    <text class="{prefix}-mono" x="1160" y="34" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#94A3B8">{right_mono}</text>
  </g>
  <path class="{prefix}-draw" d="M40 106 H1160" stroke="url(#{prefix}-line)" stroke-width="1"/>
  <circle cx="40" cy="106" r="7" fill="url(#{prefix}-pulse)" opacity="0">
    <animate attributeName="cx" values="40;1160" dur="6s" begin="2.3s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
    <animate attributeName="opacity" values="0;1;0" keyTimes="0;.15;1" dur="6s" begin="2.3s" repeatCount="indefinite"/>
  </circle>
</svg>"""

write_svg("title-about.svg", generate_title("01", "ABOUT", "Hello, I'm", "Vamshidhar.", "WHO I AM", "ta"))
write_svg("title-recognition.svg", generate_title("02", "RECOGNITION", "Proof, on the", "record.", "IMPACT &amp; TRACK RECORD", "tr"))
write_svg("title-work.svg", generate_title("03", "SELECTED WORK", "Simulations, not", "assignments.", "FOUR PIPELINES · REAL RIGOR", "tw"))
write_svg("title-toolkit.svg", generate_title("04", "TOOLKIT", "The tools I", "reach for.", "COMPUTATIONAL STACK", "tk"))
write_svg("title-commits.svg", generate_title("05", "COMMIT LOG", "A year of", "engineering.", "ACTIVITY &amp; VELOCITY", "tc"))
write_svg("title-connect.svg", generate_title("06", "CONNECT", "Let's build something", "rigorous.", "GET IN TOUCH", "tn"))

# ==========================================
# 2. Hero Banner (viewBox 1200x480)
# ==========================================
hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">Vamshidhar Reddy — Computational Mechanics, Structural Dynamics &amp; Scientific ML</title>
  <desc id="hero-desc">CAE &amp; Structural Dynamics Engineer, Scientific ML Researcher. M.Sc. in Computational Engineering at FAU Erlangen-Nürnberg.</desc>

  <defs>
    <radialGradient id="hero-bg" cx="72%" cy="38%" r="80%">
      <stop offset="0" stop-color="#0E1A36"/>
      <stop offset=".55" stop-color="#0A1122"/>
      <stop offset="1" stop-color="#050811"/>
    </radialGradient>
    <radialGradient id="hero-light-a" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".65"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-light-b" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#1E40AF" stop-opacity=".45"/>
      <stop offset="1" stop-color="#1E40AF" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hero-name-grad" gradientUnits="userSpaceOnUse" x1="60" y1="0" x2="420" y2="0">
      <stop offset="0" stop-color="#F8FAFC"/>
      <stop offset=".55" stop-color="#BAE6FD"/>
      <stop offset="1" stop-color="#38BDF8"/>
    </linearGradient>
    <linearGradient id="hero-sheen" gradientUnits="userSpaceOnUse" x1="-260" y1="0" x2="-40" y2="0">
      <stop offset="0" stop-color="#F8FAFC" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".85"/>
      <stop offset="1" stop-color="#F8FAFC" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;760 0;760 0" keyTimes="0;.35;1" dur="8s" begin="3s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#38BDF8" stop-opacity="0"/>
      <stop offset=".5" stop-color="#38BDF8" stop-opacity=".08"/>
      <stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#38BDF8" stop-opacity="0"/>
      <stop offset=".2" stop-color="#7DD3FC"/>
      <stop offset=".75" stop-color="#0284C7"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-orbit-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#38BDF8" stop-opacity=".7"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity=".05"/>
    </linearGradient>
    <pattern id="hero-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#38BDF8" stroke-opacity=".07" stroke-width="1"/>
    </pattern>
    <radialGradient id="hero-grid-fade" cx="68%" cy="45%" r="55%">
      <stop offset="0" stop-color="#fff"/>
      <stop offset="1" stop-color="#000"/>
    </radialGradient>
    <mask id="hero-grid-mask">
      <rect width="1200" height="480" fill="url(#hero-grid-fade)"/>
    </mask>
    <filter id="hero-glow" x="-20%" y="-200%" width="140%" height="500%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="hero-clip"><rect width="1200" height="480" rx="20"/></clipPath>
  </defs>

  <style>
    .hero-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .hero-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .hero-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }

    .hero-rise { animation: hero-rise 1.4s cubic-bezier(.16,1,.3,1) both; }
    .hero-fade { animation: hero-fade 1.6s cubic-bezier(.16,1,.3,1) both; }
    .d1 { animation-delay: .15s; } .d2 { animation-delay: .35s; } .d3 { animation-delay: .6s; }
    .d4 { animation-delay: .9s; } .d5 { animation-delay: 1.2s; } .d6 { animation-delay: 1.5s; }

    .hero-draw { stroke-dasharray: 900; stroke-dashoffset: 900; animation: hero-draw 2.4s cubic-bezier(.65,0,.35,1) .9s forwards; }
    .hero-signal { stroke-dasharray: 500; stroke-dashoffset: 500; animation: hero-draw 2.2s cubic-bezier(.65,0,.35,1) 2.2s forwards; }

    @keyframes hero-rise { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }
    @keyframes hero-fade { from { opacity: 0; } to { opacity: 1; } }
    @keyframes hero-draw { to { stroke-dashoffset: 0; } }

    @media (prefers-reduced-motion: reduce) {
      .hero-rise, .hero-fade { animation: none; }
      .hero-draw, .hero-signal { animation: none; stroke-dashoffset: 0; }
    }
  </style>

  <g clip-path="url(#hero-clip)">
    <!-- Canvas -->
    <rect width="1200" height="480" fill="url(#hero-bg)"/>

    <!-- Slow ambient light fields -->
    <ellipse cx="920" cy="140" rx="420" ry="300" fill="url(#hero-light-a)">
      <animateTransform attributeName="transform" type="translate" values="0 0; -60 30; 0 0" dur="22s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>
    <ellipse cx="180" cy="460" rx="360" ry="220" fill="url(#hero-light-b)">
      <animateTransform attributeName="transform" type="translate" values="0 0; 70 -25; 0 0" dur="28s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>

    <!-- Technical grid -->
    <rect width="1200" height="480" fill="url(#hero-grid)" mask="url(#hero-grid-mask)"/>

    <!-- Slow scan line across the grid -->
    <rect x="0" y="-140" width="1200" height="140" fill="url(#hero-scan)">
      <animate attributeName="y" values="-140;480" dur="11s" begin="2s" repeatCount="indefinite"/>
    </rect>

    <!-- Drifting computational particles -->
    <g fill="#38BDF8">
      <circle cx="560" cy="120" r="1.4"><animate attributeName="opacity" values="0;.9;0" dur="4.2s" repeatCount="indefinite"/><animate attributeName="cy" values="120;96" dur="4.2s" repeatCount="indefinite"/></circle>
      <circle cx="700" cy="70" r="1.1"><animate attributeName="opacity" values="0;.8;0" dur="5.6s" begin="1s" repeatCount="indefinite"/><animate attributeName="cy" values="70;48" dur="5.6s" begin="1s" repeatCount="indefinite"/></circle>
      <circle cx="1120" cy="380" r="1.6"><animate attributeName="opacity" values="0;.9;0" dur="4.8s" begin="2s" repeatCount="indefinite"/><animate attributeName="cy" values="380;352" dur="4.8s" begin="2s" repeatCount="indefinite"/></circle>
      <circle cx="760" cy="420" r="1.2"><animate attributeName="opacity" values="0;.7;0" dur="6s" begin=".5s" repeatCount="indefinite"/><animate attributeName="cy" values="420;396" dur="6s" begin=".5s" repeatCount="indefinite"/></circle>
      <circle cx="1060" cy="60" r="1.3"><animate attributeName="opacity" values="0;.85;0" dur="5s" begin="3s" repeatCount="indefinite"/><animate attributeName="cy" values="60;40" dur="5s" begin="3s" repeatCount="indefinite"/></circle>
      <circle cx="640" cy="250" r="1"><animate attributeName="opacity" values="0;.7;0" dur="4.4s" begin="2.5s" repeatCount="indefinite"/><animate attributeName="cy" values="250;226" dur="4.4s" begin="2.5s" repeatCount="indefinite"/></circle>
    </g>

    <!-- Right-side Orbital Computational Rig -->
    <g transform="translate(970 232)" class="hero-fade d3">
      <circle r="212" fill="none" stroke="#38BDF8" stroke-opacity=".12" stroke-dasharray="2 10">
        <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="140s" repeatCount="indefinite"/>
      </circle>
      <circle r="185" fill="none" stroke="url(#hero-orbit-grad)" stroke-width="1.2"/>
      <circle r="150" fill="none" stroke="#38BDF8" stroke-opacity=".18" stroke-dasharray="3 8"/>

      <!-- FEA Coordinate Wireframe Glyph at Center -->
      <g stroke="#38BDF8" stroke-opacity=".6" stroke-width="1.2" fill="none">
        <polygon points="0,-70 60,-35 60,35 0,70 -60,35 -60,-35" stroke-dasharray="4 4"/>
        <line x1="0" y1="-70" x2="0" y2="70"/>
        <line x1="-60" y1="-35" x2="60" y2="35"/>
        <line x1="-60" y1="35" x2="60" y2="-35"/>
        <circle cx="0" cy="0" r="5" fill="#38BDF8" filter="url(#hero-glow)"/>
        <!-- Mode contour waves radiating from center -->
        <circle cx="0" cy="0" r="26" stroke="#0284C7" stroke-width="1.5" stroke-opacity=".7">
          <animate attributeName="r" values="20;90" dur="4.5s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values=".9;0" dur="4.5s" repeatCount="indefinite"/>
        </circle>
        <circle cx="0" cy="0" r="45" stroke="#7DD3FC" stroke-width="1.2" stroke-opacity=".5">
          <animate attributeName="r" values="35;120" dur="4.5s" begin="1.5s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values=".8;0" dur="4.5s" begin="1.5s" repeatCount="indefinite"/>
        </circle>
      </g>

      <!-- Rotating node stations with labels -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="80s" repeatCount="indefinite"/>
        <circle cx="185" cy="0" r="4.5" fill="#38BDF8" filter="url(#hero-glow)"/>
        <circle cx="0" cy="185" r="3.5" fill="#0284C7"/>
        <circle cx="-185" cy="0" r="4" fill="#38BDF8"/>
        <circle cx="0" cy="-185" r="3" fill="#BAE6FD"/>
      </g>

      <!-- Fixed technical labels for the engineering pillars -->
      <g class="hero-mono" font-size="10.5" letter-spacing="1.6" fill="#94A3B8">
        <g transform="translate(-140 -150)"><circle r="3" fill="#38BDF8"/><text x="10" y="4" fill="#F8FAFC">CAE / FEA</text></g>
        <g transform="translate(130 -110)"><circle r="3" fill="#38BDF8"/><text x="10" y="4" fill="#F8FAFC">SciML</text></g>
        <g transform="translate(130 120)"><circle r="3" fill="#38BDF8"/><text x="10" y="4" fill="#F8FAFC">NVH</text></g>
        <g transform="translate(-150 50)"><circle r="3" fill="#38BDF8"/><text x="-12" y="4" text-anchor="end" fill="#F8FAFC">AGENTIC</text></g>
      </g>
    </g>

    <!-- Signal path drawing itself through the composition -->
    <path class="hero-signal" d="M600 342 C 680 338, 740 330, 780 318 S 828 300, 847 300" fill="none" stroke="#38BDF8" stroke-opacity=".5" stroke-width="1.2"/>
    <circle cx="600" cy="342" r="3" fill="#F8FAFC" filter="url(#hero-glow)" opacity=".9">
      <animateMotion dur="5s" repeatCount="indefinite" begin="4.4s" path="M600 342 C 680 338, 740 330, 780 318 S 828 300, 847 300" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".45 0 .55 1"/>
    </circle>

    <!-- Terminal indicator -->
    <g class="hero-fade d1" transform="translate(72 64)">
      <rect width="348" height="34" rx="17" fill="#0A1122" stroke="#38BDF8" stroke-opacity=".3"/>
      <circle cx="20" cy="17" r="4" fill="#38BDF8">
        <animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/>
      </circle>
      <text class="hero-mono" x="34" y="21.5" font-size="12" fill="#94A3B8">~/vamshidhar<tspan fill="#38BDF8"> $ </tspan><tspan fill="#F8FAFC">run --simulation --rigor</tspan></text>
      <rect x="324" y="10" width="7" height="14" fill="#38BDF8">
        <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- Eyebrow -->
    <g class="hero-rise d2">
      <line x1="72" y1="136" x2="104" y2="136" stroke="#38BDF8"/>
      <text class="hero-mono" x="116" y="140" font-size="12.5" letter-spacing="3.4" fill="#38BDF8">COMPUTATIONAL MECHANICS · SCIENTIFIC ML · CAE AUTOMATION</text>
    </g>

    <!-- Name -->
    <text class="hero-serif hero-rise d3" x="68" y="230" font-size="92" font-weight="300" letter-spacing="-2.5" fill="#F8FAFC">Vamshidhar</text>
    <text class="hero-serif hero-rise d4" x="68" y="318" font-size="92" font-style="italic" font-weight="300" letter-spacing="-2.5" fill="url(#hero-name-grad)">Reddy<tspan fill="#38BDF8">.</tspan></text>

    <!-- Light sweeping across the name -->
    <g class="hero-fade d6" pointer-events="none">
      <text class="hero-serif" x="68" y="230" font-size="92" font-weight="300" letter-spacing="-2.5" fill="url(#hero-sheen)">Vamshidhar</text>
      <text class="hero-serif" x="68" y="318" font-size="92" font-style="italic" font-weight="300" letter-spacing="-2.5" fill="url(#hero-sheen)">Reddy.</text>
    </g>

    <!-- Glowing underline -->
    <path class="hero-draw" d="M72 346 C 220 340, 420 352, 600 342" fill="none" stroke="url(#hero-rule)" stroke-width="2" stroke-linecap="round" filter="url(#hero-glow)"/>

    <!-- Positioning -->
    <text class="hero-mono hero-rise d5" x="72" y="384" font-size="13" letter-spacing="2.6" fill="#F8FAFC">CAE &amp; STRUCTURAL DYNAMICS ENGINEER  ·  SCIENTIFIC ML RESEARCHER</text>
    <text class="hero-serif hero-rise d6" x="72" y="420" font-size="19" font-style="italic" fill="#94A3B8">Engineering physics. Accelerating simulation with computational intelligence.</text>

    <!-- Meta strip -->
    <g class="hero-fade d6">
      <line x1="72" y1="446" x2="1128" y2="446" stroke="#38BDF8" stroke-opacity=".15"/>
      <text class="hero-mono" x="72" y="466" font-size="10.5" letter-spacing="2" fill="#94A3B8">M.SC COMPUTATIONAL ENGINEERING · FAU ERLANGEN-NÜRNBERG</text>
      <text class="hero-mono" x="1128" y="466" text-anchor="end" font-size="10.5" letter-spacing="2" fill="#38BDF8">MERCEDES-BENZ (SCIML) · VALEO EAUTOMOTIVE (NVH THESIS)</text>
    </g>

    <!-- Outer Frame -->
    <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="#38BDF8" stroke-opacity=".2"/>
    <path d="M20 2 h30 M2 20 v30 M1180 2 h-30 M1198 20 v30 M20 478 h30 M2 460 v-30 M1180 478 h-30 M1198 460 v-30" stroke="#38BDF8" stroke-width="1.5" stroke-opacity=".7" fill="none"/>
  </g>
</svg>"""
write_svg("hero-portrait.svg", hero_svg)

# ==========================================
# 3. About Intro (viewBox 1200x420)
# ==========================================
about_intro_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ab-t ab-d">
  <title id="ab-t">About Vamshidhar Reddy</title>
  <desc id="ab-d">CAE &amp; Structural Dynamics Engineer, Scientific ML Researcher. M.Sc. Computational Engineering at FAU Erlangen-Nürnberg. Experience at Mercedes-Benz (SciML surrogates) and Valeo eAutomotive (Master Thesis NVH). Specialized in Ansys Mechanical, NASTRAN, Simcenter 3D, PyTorch, and Claude MCP agentic simulation.</desc>
  <defs>
    <linearGradient id="ab-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0A1122"/><stop offset="1" stop-color="#050811"/></linearGradient>
    <radialGradient id="ab-glow" cx="80%" cy="20%" r="70%"><stop offset="0" stop-color="#0284C7" stop-opacity=".45"/><stop offset="1" stop-color="#0284C7" stop-opacity="0"/></radialGradient>
    <pattern id="ab-scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#F8FAFC" opacity=".025"/></pattern>
    <clipPath id="ab-c0"><rect class="ab-type" x="68" y="112" width="89" height="22" style="animation-delay:0.60s;animation-duration:0.41s;animation-timing-function:steps(6)"/></clipPath>
    <clipPath id="ab-c1"><rect class="ab-type" x="68" y="137" width="560" height="22" style="animation-delay:1.16s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c2"><rect class="ab-type" x="68" y="162" width="179" height="22" style="animation-delay:2.04s;animation-duration:0.56s;animation-timing-function:steps(17)"/></clipPath>
    <clipPath id="ab-c3"><rect class="ab-type" x="68" y="187" width="580" height="22" style="animation-delay:2.75s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c4"><rect class="ab-type" x="68" y="212" width="188" height="22" style="animation-delay:3.63s;animation-duration:0.59s;animation-timing-function:steps(18)"/></clipPath>
    <clipPath id="ab-c5"><rect class="ab-type" x="68" y="237" width="580" height="22" style="animation-delay:4.37s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c6"><rect class="ab-type" x="68" y="262" width="138" height="22" style="animation-delay:5.25s;animation-duration:0.41s;animation-timing-function:steps(12)"/></clipPath>
    <clipPath id="ab-c7"><rect class="ab-type" x="68" y="287" width="580" height="22" style="animation-delay:5.81s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
    <clipPath id="ab-c8"><rect class="ab-type" x="68" y="312" width="163" height="22" style="animation-delay:6.69s;animation-duration:0.49s;animation-timing-function:steps(15)"/></clipPath>
    <clipPath id="ab-c9"><rect class="ab-type" x="68" y="337" width="580" height="22" style="animation-delay:7.34s;animation-duration:0.53s;animation-timing-function:steps(1)"/></clipPath>
  </defs>
  <style>
    .ab-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .ab-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .ab-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .ab-type { transform-box: fill-box; transform-origin: left center; animation-name: ab-type; animation-fill-mode: both; }
    .ab-card { animation: ab-in 1s cubic-bezier(.16,1,.3,1) both; }
    .ab-fade { animation: ab-fade 1s ease both; }
    @keyframes ab-type { 0% { transform: scaleX(0); } 85%, 100% { transform: scaleX(1); } }
    @keyframes ab-in { from { opacity: 0; transform: translateX(24px); } to { opacity: 1; transform: none; } }
    @keyframes ab-fade { from { opacity: 0; } to { opacity: 1; } }
    @media (prefers-reduced-motion: reduce) { .ab-type, .ab-card, .ab-fade { animation: none; } }
  </style>
  <rect width="1200" height="420" rx="20" fill="url(#ab-bg)"/>
  <rect width="1200" height="420" rx="20" fill="url(#ab-glow)"/>
  <rect x=".5" y=".5" width="1199" height="419" rx="19.5" fill="none" stroke="#38BDF8" stroke-opacity=".18"/>

  <!-- Terminal window -->
  <g class="ab-fade">
    <rect x="40" y="40" width="760" height="340" rx="14" fill="#060A14" stroke="#38BDF8" stroke-opacity=".3"/>
    <rect x="40" y="40" width="760" height="340" rx="14" fill="url(#ab-scan)"/>
    <path d="M40 54 a14 14 0 0 1 14 -14 H786 a14 14 0 0 1 14 14 V76 H40 Z" fill="#0D162B"/>
    <line x1="40" y1="76" x2="800" y2="76" stroke="#38BDF8" stroke-opacity=".2"/>
    <circle cx="62" cy="58" r="5" fill="#EF4444"/><circle cx="80" cy="58" r="5" fill="#F59E0B"/><circle cx="98" cy="58" r="5" fill="#10B981"/>
    <text class="ab-mono" x="420" y="62" text-anchor="middle" font-size="11" letter-spacing="1.5" fill="#94A3B8">vamshidhar@cae-lab: ~</text>
  </g>
  <g class="ab-mono" font-size="13.5">
      <g clip-path="url(#ab-c0)"><text x="72" y="128" fill="#38BDF8">$</text><text x="94" y="128" fill="#F8FAFC">whoami</text></g>
      <g clip-path="url(#ab-c1)"><text x="72" y="153" fill="#0284C7">→</text><text x="94" y="153" fill="#94A3B8">Vamshidhar Reddy · CAE, Structural Dynamics &amp; Scientific ML</text></g>
      <g clip-path="url(#ab-c2)"><text x="72" y="178" fill="#38BDF8">$</text><text x="94" y="178" fill="#F8FAFC">cat education.txt</text></g>
      <g clip-path="url(#ab-c3)"><text x="72" y="203" fill="#0284C7">→</text><text x="94" y="203" fill="#94A3B8">M.Sc. Computational Engineering · FAU Erlangen-Nürnberg</text></g>
      <g clip-path="url(#ab-c4)"><text x="72" y="228" fill="#38BDF8">$</text><text x="94" y="228" fill="#F8FAFC">cat experience.txt</text></g>
      <g clip-path="url(#ab-c5)"><text x="72" y="253" fill="#0284C7">→</text><text x="94" y="253" fill="#94A3B8">Mercedes-Benz (SciML Surrogates) · Valeo (E-Motor NVH Thesis)</text></g>
      <g clip-path="url(#ab-c6)"><text x="72" y="278" fill="#38BDF8">$</text><text x="94" y="278" fill="#F8FAFC">ls ./automated</text></g>
      <g clip-path="url(#ab-c7)"><text x="72" y="303" fill="#0284C7">→</text><text x="94" y="303" fill="#94A3B8">ansys-claude-mcp  nastran-surrogate  simcenter-acoustics</text></g>
      <g clip-path="url(#ab-c8)"><text x="72" y="328" fill="#38BDF8">$</text><text x="94" y="328" fill="#F8FAFC">echo $MISSION</text></g>
      <g clip-path="url(#ab-c9)"><text x="72" y="353" fill="#0284C7">→</text><text x="94" y="353" fill="#94A3B8">physics-grounded simulations · zero-compromise engineering precision</text></g>
  </g>
  <rect x="72" y="364" width="8" height="16" fill="#38BDF8" class="ab-fade" style="animation-delay:8.2s">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>

  <!-- Right side cards -->
  <g class="ab-card" style="animation-delay:1.2s"><g transform="translate(836 70)">
    <rect width="324" height="88" rx="14" fill="#0D162B" stroke="#38BDF8" stroke-opacity=".28"/>
    <rect x="0" y="0" width="3" height="88" rx="1.5" fill="#38BDF8"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#38BDF8">CORE DOMAIN</text>
    <text class="ab-serif" x="22" y="58" font-size="28" font-weight="300" fill="#F8FAFC">CAE &amp; FEA</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#94A3B8">Ansys Mechanical · NASTRAN · Simcenter 3D</text>
  </g></g>
  <g class="ab-card" style="animation-delay:1.7s"><g transform="translate(836 174)">
    <rect width="324" height="88" rx="14" fill="#0D162B" stroke="#38BDF8" stroke-opacity=".28"/>
    <rect x="0" y="0" width="3" height="88" rx="1.5" fill="#38BDF8"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#38BDF8">WHERE ML ACCELERATES</text>
    <text class="ab-serif" x="22" y="58" font-size="28" font-weight="300" fill="#F8FAFC">Scientific ML</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#94A3B8">FRF Surrogates · PINNs · DIMGP · PyTorch</text>
  </g></g>
  <g class="ab-card" style="animation-delay:2.2s"><g transform="translate(836 278)">
    <rect width="324" height="88" rx="14" fill="#0D162B" stroke="#38BDF8" stroke-opacity=".28"/>
    <rect x="0" y="0" width="3" height="88" rx="1.5" fill="#38BDF8"/>
    <text class="ab-mono" x="22" y="26" font-size="10" letter-spacing="2" fill="#38BDF8">AUTOMATION EDGE</text>
    <text class="ab-serif" x="22" y="58" font-size="28" font-weight="300" fill="#F8FAFC">Agentic Simulation</text>
    <text class="ab-sans" x="22" y="78" font-size="12" fill="#94A3B8">Claude MCP · PyMechanical · NX Open API</text>
  </g></g>
</svg>"""
write_svg("about-intro.svg", about_intro_svg)

# ==========================================
# 4. Recognition & Achievements (viewBox 1200x430)
# ==========================================
achieve_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 430" width="1200" height="430" role="img" aria-labelledby="ach-title ach-desc">
  <title id="ach-title">Recognition &amp; Impact</title>
  <desc id="ach-desc">Mercedes-Benz Scientific ML Surrogates: cut NASTRAN solve times from ~6 hours to milliseconds. Valeo eAutomotive Master Thesis: E-Motor NVH &amp; Stator resonance isolation with experimental correlation. M.Sc. Computational Engineering at FAU Erlangen-Nürnberg.</desc>

  <defs>
    <linearGradient id="ach-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0A1122"/>
      <stop offset="1" stop-color="#050811"/>
    </linearGradient>
    <radialGradient id="ach-glow-a" cx="85%" cy="0%" r="90%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".75"/>
      <stop offset="1" stop-color="#1E40AF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ach-glow-b" cx="90%" cy="0%" r="90%">
      <stop offset="0" stop-color="#38BDF8" stop-opacity=".35"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ach-outline" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#38BDF8" stop-opacity=".45"/>
      <stop offset="1" stop-color="#38BDF8" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ach-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#F8FAFC" stop-opacity="0"/>
      <stop offset=".5" stop-color="#F8FAFC" stop-opacity=".08"/>
      <stop offset="1" stop-color="#F8FAFC" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="ach-clip-a"><rect x="0" y="0" width="700" height="250" rx="16"/></clipPath>
    <clipPath id="ach-clip-b"><rect x="0" y="0" width="476" height="250" rx="16"/></clipPath>
    <linearGradient id="ach-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <style>
    .ach-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .ach-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .ach-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .ach-in { animation: ach-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .a1 { animation-delay: .1s; } .a2 { animation-delay: .35s; } .a3 { animation-delay: .6s; }
    .ach-draw { stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: ach-draw 2.6s cubic-bezier(.65,0,.35,1) .8s forwards; }
    @keyframes ach-in { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }
    @keyframes ach-draw { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) {
      .ach-in { animation: none; }
      .ach-draw { animation: none; stroke-dashoffset: 0; }
    }
  </style>

  <rect width="1200" height="430" rx="20" fill="url(#ach-bg)"/>
  <rect x=".5" y=".5" width="1199" height="429" rx="19.5" fill="none" stroke="#38BDF8" stroke-opacity=".18"/>

  <!-- Card 1: Mercedes-Benz SciML Breakthrough (Left 700px) -->
  <g class="ach-in a1"><g transform="translate(24 24)">
    <g clip-path="url(#ach-clip-a)">
      <rect width="700" height="250" fill="#0D162B"/>
      <rect width="700" height="250" fill="url(#ach-glow-a)"/>
      <text class="ach-serif" x="684" y="115" text-anchor="end" font-size="110" font-weight="300" letter-spacing="-4" fill="url(#ach-outline)">6h → ms</text>
      <rect x="-300" y="0" width="260" height="250" fill="url(#ach-sheen)" transform="skewX(-18)">
        <animate attributeName="x" values="-300;900;900" keyTimes="0;.35;1" dur="9s" begin="2s" repeatCount="indefinite"/>
      </rect>
    </g>
    <rect width="700" height="250" rx="16" fill="none" stroke="#38BDF8" stroke-opacity=".3"/>

    <text class="ach-mono" x="32" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">SCIENTIFIC ML · MERCEDES-BENZ</text>
    <text class="ach-serif" x="32" y="82" font-size="34" font-weight="300" letter-spacing="-0.8" fill="#F8FAFC">6-Hour FEA Solves to Milliseconds</text>
    <text class="ach-sans" x="32" y="112" font-size="14.5" fill="#94A3B8">Benchmarked deep learning &amp; surrogate architectures predicting powertrain structural FRFs from NASTRAN.</text>
    <text class="ach-mono" x="32" y="136" font-size="12" fill="#BAE6FD">Achieved highest curve-prediction skill score with HistGradientBoosting &amp; DIMGP.</text>

    <!-- Stat Pillars -->
    <g transform="translate(32 176)">
      <text class="ach-serif" font-size="32" font-weight="300" fill="#F8FAFC">3,600×</text>
      <text class="ach-sans" y="22" font-size="11.5" fill="#94A3B8">Simulation Speedup</text>
    </g>
    <g transform="translate(240 176)">
      <text class="ach-serif" font-size="32" font-weight="300" fill="#F8FAFC">0.982</text>
      <text class="ach-sans" y="22" font-size="11.5" fill="#94A3B8">FRF Curve Skill Score</text>
    </g>
    <g transform="translate(450 176)">
      <text class="ach-serif" font-size="32" font-weight="300" fill="#F8FAFC">100%</text>
      <text class="ach-sans" y="22" font-size="11.5" fill="#94A3B8">DOE Dynamic Fidelity</text>
    </g>
  </g></g>

  <!-- Card 2: Valeo Master Thesis NVH (Right 476px) -->
  <g class="ach-in a2"><g transform="translate(748 24)">
    <g clip-path="url(#ach-clip-b)">
      <rect width="428" height="250" fill="#0D162B"/>
      <rect width="428" height="250" fill="url(#ach-glow-b)"/>
      <text class="ach-serif" x="412" y="115" text-anchor="end" font-size="95" font-weight="300" letter-spacing="-4" fill="url(#ach-outline)">VALEO</text>
      <rect x="-300" y="0" width="260" height="250" fill="url(#ach-sheen)" transform="skewX(-18)">
        <animate attributeName="x" values="-300;700;700" keyTimes="0;.35;1" dur="9s" begin="3.5s" repeatCount="indefinite"/>
      </rect>
    </g>
    <rect width="428" height="250" rx="16" fill="none" stroke="#38BDF8" stroke-opacity=".3"/>

    <text class="ach-mono" x="28" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">MASTER THESIS · VALEO EAUTOMOTIVE</text>
    <text class="ach-serif" x="28" y="82" font-size="30" font-weight="300" letter-spacing="-0.8" fill="#F8FAFC">E-Motor Stator NVH Isolation</text>
    <text class="ach-sans" x="28" y="112" font-size="13.5" fill="#94A3B8">FEA modal &amp; harmonic response correlating stator natural frequencies with physical test benches.</text>

    <!-- Stat Pillars -->
    <g transform="translate(28 176)">
      <text class="ach-serif" font-size="32" font-weight="300" fill="#F8FAFC">16 Orders</text>
      <text class="ach-sans" y="22" font-size="11.5" fill="#94A3B8">Electromagnetic Harmonics</text>
    </g>
    <g transform="translate(220 176)">
      <text class="ach-serif" font-size="32" font-weight="300" fill="#F8FAFC">96.4%</text>
      <text class="ach-sans" y="22" font-size="11.5" fill="#94A3B8">Test Bench Correlation</text>
    </g>
  </g></g>

  <!-- Bottom Metric Strip (4 columns) -->
  <g class="ach-in a3" transform="translate(24 298)">
    <rect width="1152" height="106" rx="14" fill="#080E1C" stroke="#38BDF8" stroke-opacity=".2"/>
    <g transform="translate(32 24)">
      <text class="ach-mono" font-size="10.5" letter-spacing="2" fill="#38BDF8">FAU ERLANGEN-NÜRNBERG</text>
      <text class="ach-serif" y="28" font-size="20" font-weight="300" fill="#F8FAFC">M.Sc. Computational Eng.</text>
      <text class="ach-sans" y="50" font-size="12" fill="#94A3B8">Structural Mechanics · Scientific Computing</text>
    </g>
    <line x1="310" y1="18" x2="310" y2="88" stroke="#38BDF8" stroke-opacity=".15"/>
    <g transform="translate(330 24)">
      <text class="ach-mono" font-size="10.5" letter-spacing="2" fill="#38BDF8">AGENTIC FEA PROTOCOL</text>
      <text class="ach-serif" y="28" font-size="20" font-weight="300" fill="#F8FAFC">Claude MCP + Ansys 2026</text>
      <text class="ach-sans" y="50" font-size="12" fill="#94A3B8">Autonomous Modal Vibration Analysis</text>
    </g>
    <line x1="610" y1="18" x2="610" y2="88" stroke="#38BDF8" stroke-opacity=".15"/>
    <g transform="translate(630 24)">
      <text class="ach-mono" font-size="10.5" letter-spacing="2" fill="#38BDF8">FORMULA STUDENT RACING</text>
      <text class="ach-serif" y="28" font-size="20" font-weight="300" fill="#F8FAFC">CFK Monocoque Layup</text>
      <text class="ach-sans" y="50" font-size="12" fill="#94A3B8">FAU High Voltage Motorsports Chassis</text>
    </g>
    <line x1="910" y1="18" x2="910" y2="88" stroke="#38BDF8" stroke-opacity=".15"/>
    <g transform="translate(930 24)">
      <text class="ach-mono" font-size="10.5" letter-spacing="2" fill="#38BDF8">STATUS &amp; MOBILITY</text>
      <text class="ach-serif" y="28" font-size="20" font-weight="300" fill="#F8FAFC">English C2 · German B2</text>
      <text class="ach-sans" y="50" font-size="12" fill="#94A3B8">Driving License Class B · DACH &amp; Worldwide</text>
    </g>
  </g>
</svg>"""
write_svg("achievement-motif.svg", achieve_svg)

# ==========================================
# 5. Project 1: Agentic FEA (viewBox 1200x370)
# ==========================================
project_1_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p1-t">
  <title id="p1-t">Agentic FEA: 3D Aerospace Bracket Modal Analysis via Claude MCP &amp; Ansys 2026 R1</title>
  <defs>
    <linearGradient id="p1-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0A1122"/><stop offset="1" stop-color="#050811"/>
    </linearGradient>
    <radialGradient id="p1-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".65"/><stop offset="1" stop-color="#1E40AF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p1-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <filter id="p1-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p1-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p1-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .p1-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .p1-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .p1-in { animation: p1-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p1-d1 { animation-delay: .15s; } .p1-d2 { animation-delay: .4s; }
    .p1-chip { animation: p1-chip .7s cubic-bezier(.34,1.56,.64,1) both; }
    .p1-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p1-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p1-in { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
    @keyframes p1-chip { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
    @keyframes p1-draw { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p1-in, .p1-chip { animation: none; } .p1-draw { animation: none; stroke-dashoffset: 0; } }
  </style>
  <g clip-path="url(#p1-clip)">
    <rect width="1200" height="370" fill="url(#p1-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p1-grid)"/>
    <rect width="1200" height="370" fill="url(#p1-glow)"/>

    <g class="p1-in p1-d1">
      <text class="p1-mono" x="56" y="62" font-size="12" letter-spacing="2.6" fill="#38BDF8">01 · AGENTIC CAE · ANSYS 2026 R1 · MCP</text>
      <text class="p1-serif" x="54" y="126" font-size="50" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">Agentic FEA: Modal Analysis</text>
      <text class="p1-sans" x="56" y="166" font-size="17" fill="#94A3B8">3D aerospace bracket modal vibration analysis via Claude MCP &amp; PyMechanical.</text>
      <text class="p1-mono" x="56" y="200" font-size="12.5" fill="#BAE6FD"><tspan fill="#38BDF8">PIPELINE ›</tspan> CAD import → solid meshing → contact pairs → Block Lanczos eigenvalue solve → contour plots</text>
      <line class="p1-draw" x1="56" y1="226" x2="680" y2="226" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(56 266)"><text class="p1-serif" font-size="34" font-weight="300" fill="#F8FAFC">6 Modes</text><text class="p1-sans" y="24" font-size="12.5" fill="#94A3B8">Eigenvalue extraction</text></g>
      <g transform="translate(261 266)"><text class="p1-serif" font-size="34" font-weight="300" fill="#F8FAFC">100%</text><text class="p1-sans" y="24" font-size="12.5" fill="#94A3B8">Autonomous simulation</text></g>
      <g transform="translate(466 266)"><text class="p1-serif" font-size="34" font-weight="300" fill="#F8FAFC">Zero-Click</text><text class="p1-sans" y="24" font-size="12.5" fill="#94A3B8">CAD to contour plots</text></g>

      <!-- Chips -->
      <g class="p1-chip" style="animation-delay:1.00s"><rect x="56" y="314" width="130" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p1-mono" x="121" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Ansys 2026 R1</text></g>
      <g class="p1-chip" style="animation-delay:1.12s"><rect x="194" y="314" width="105" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p1-mono" x="246" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">PyMechanical</text></g>
      <g class="p1-chip" style="animation-delay:1.24s"><rect x="307" y="314" width="95" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p1-mono" x="354" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Claude MCP</text></g>
      <g class="p1-chip" style="animation-delay:1.36s"><rect x="410" y="314" width="105" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p1-mono" x="462" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Block Lanczos</text></g>
      <g class="p1-chip" style="animation-delay:1.48s"><rect x="523" y="314" width="70" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p1-mono" x="558" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Python</text></g>
    </g>

    <!-- Right Side 3D FEA Bracket Visual Artwork -->
    <g class="p1-in p1-d2" transform="translate(760 40)">
      <!-- 3D Bracket Isometric Projection Mesh -->
      <g stroke="#38BDF8" stroke-width="1.3" fill="none">
        <!-- Isometric Base Flange -->
        <polygon points="50,220 180,270 330,210 200,160" fill="#0E1A33" stroke="#0284C7" stroke-width="1.5"/>
        <polygon points="50,220 50,240 180,290 180,270" fill="#091224" stroke="#0284C7"/>
        <polygon points="180,270 180,290 330,230 330,210" fill="#060C1A" stroke="#0284C7"/>

        <!-- Vertical Rib / Bracket Body -->
        <polygon points="120,185 180,205 180,85 120,65" fill="#13274F" stroke="#38BDF8"/>
        <polygon points="180,205 240,185 240,65 180,85" fill="#0A1630" stroke="#38BDF8"/>
        
        <!-- Top Mounting Lug -->
        <polygon points="120,65 180,85 240,65 180,45" fill="#1E3A8A" stroke="#7DD3FC" stroke-width="1.5"/>

        <!-- FEA Solid Mesh Tessellation lines -->
        <line x1="50" y1="220" x2="200" y2="160" stroke="#38BDF8" stroke-opacity=".3"/>
        <line x1="180" y1="270" x2="330" y2="210" stroke="#38BDF8" stroke-opacity=".3"/>
        <line x1="120" y1="65" x2="180" y2="205" stroke="#38BDF8" stroke-opacity=".3"/>
        <line x1="240" y1="65" x2="180" y2="205" stroke="#38BDF8" stroke-opacity=".3"/>
        <line x1="150" y1="75" x2="150" y2="195" stroke="#38BDF8" stroke-opacity=".3"/>
        <line x1="210" y1="75" x2="210" y2="195" stroke="#38BDF8" stroke-opacity=".3"/>

        <!-- Modal Displacement Wave Contour (f1) -->
        <path d="M180 85 C 210 85, 230 140, 200 205" stroke="#00F2FE" stroke-width="2.5" filter="url(#p1-glowf)">
          <animate attributeName="d" values="M180 85 C 210 85, 230 140, 200 205; M180 85 C 150 85, 130 140, 160 205; M180 85 C 210 85, 230 140, 200 205" dur="3s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
        </path>
      </g>

      <!-- Bolt Hole Fixations -->
      <circle cx="95" cy="235" r="7" fill="#060B14" stroke="#EF4444" stroke-width="1.5"/>
      <circle cx="280" cy="225" r="7" fill="#060B14" stroke="#EF4444" stroke-width="1.5"/>
      <circle cx="180" cy="65" r="8" fill="#060B14" stroke="#10B981" stroke-width="1.8"/>

      <!-- Floating Mode Frequency Badges -->
      <g transform="translate(250 30)" class="p1-mono">
        <rect width="130" height="28" rx="6" fill="#0A1122" stroke="#38BDF8" stroke-opacity=".5"/>
        <circle cx="14" cy="14" r="3.5" fill="#38BDF8"/>
        <text x="26" y="18" font-size="11" fill="#F8FAFC">f₁: 142.8 Hz</text>
      </g>
      <g transform="translate(260 70)" class="p1-mono">
        <rect width="130" height="28" rx="6" fill="#0A1122" stroke="#0284C7" stroke-opacity=".5"/>
        <circle cx="14" cy="14" r="3.5" fill="#0284C7"/>
        <text x="26" y="18" font-size="11" fill="#94A3B8">f₂: 284.1 Hz</text>
      </g>
      <g transform="translate(250 110)" class="p1-mono">
        <rect width="130" height="28" rx="6" fill="#0A1122" stroke="#1E40AF" stroke-opacity=".5"/>
        <circle cx="14" cy="14" r="3.5" fill="#1E40AF"/>
        <text x="26" y="18" font-size="11" fill="#94A3B8">f₃: 412.5 Hz</text>
      </g>
    </g>
  </g>
</svg>"""
write_svg("project-modal-analysis.svg", project_1_svg)

# ==========================================
# 6. Project 2: SciML Surrogate (viewBox 1200x370)
# ==========================================
project_2_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p2-t">
  <title id="p2-t">Powertrain Structural FRF Surrogate: Machine Learning replacing NASTRAN</title>
  <defs>
    <linearGradient id="p2-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0A1122"/><stop offset="1" stop-color="#050811"/>
    </linearGradient>
    <radialGradient id="p2-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".65"/><stop offset="1" stop-color="#1E40AF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p2-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <clipPath id="p2-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p2-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .p2-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .p2-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .p2-in { animation: p2-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p2-d1 { animation-delay: .15s; } .p2-d2 { animation-delay: .4s; }
    .p2-chip { animation: p2-chip .7s cubic-bezier(.34,1.56,.64,1) both; }
    .p2-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p2-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p2-in { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
    @keyframes p2-chip { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
    @keyframes p2-draw { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p2-in, .p2-chip { animation: none; } .p2-draw { animation: none; stroke-dashoffset: 0; } }
  </style>
  <g clip-path="url(#p2-clip)">
    <rect width="1200" height="370" fill="url(#p2-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p2-grid)"/>
    <rect width="1200" height="370" fill="url(#p2-glow)"/>

    <g class="p2-in p2-d1">
      <text class="p2-mono" x="56" y="62" font-size="12" letter-spacing="2.6" fill="#38BDF8">02 · SCIENTIFIC ML · MERCEDES-BENZ BENCHMARK</text>
      <text class="p2-serif" x="54" y="126" font-size="50" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">Structural FRF Surrogate</text>
      <text class="p2-sans" x="56" y="166" font-size="17" fill="#94A3B8">Machine learning surrogates replacing computationally heavy NASTRAN runs.</text>
      <text class="p2-mono" x="56" y="200" font-size="12.5" fill="#BAE6FD"><tspan fill="#38BDF8">BUILT ›</tspan> Trained HistGradientBoosting &amp; DIMGP models predicting Frequency Response Functions (FRF)</text>
      <line class="p2-draw" x1="56" y1="226" x2="680" y2="226" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(56 266)"><text class="p2-serif" font-size="34" font-weight="300" fill="#F8FAFC">6h → ms</text><text class="p2-sans" y="24" font-size="12.5" fill="#94A3B8">Inference acceleration</text></g>
      <g transform="translate(261 266)"><text class="p2-serif" font-size="34" font-weight="300" fill="#F8FAFC">0.982</text><text class="p2-sans" y="24" font-size="12.5" fill="#94A3B8">Skill score on FRF peaks</text></g>
      <g transform="translate(466 266)"><text class="p2-serif" font-size="34" font-weight="300" fill="#F8FAFC">Full DOE</text><text class="p2-sans" y="24" font-size="12.5" fill="#94A3B8">Parametric design sweep</text></g>

      <!-- Chips -->
      <g class="p2-chip" style="animation-delay:1.00s"><rect x="56" y="314" width="85" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p2-mono" x="98" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">NASTRAN</text></g>
      <g class="p2-chip" style="animation-delay:1.12s"><rect x="149" y="314" width="75" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p2-mono" x="186" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">PyTorch</text></g>
      <g class="p2-chip" style="animation-delay:1.24s"><rect x="232" y="314" width="100" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p2-mono" x="282" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">scikit-learn</text></g>
      <g class="p2-chip" style="animation-delay:1.36s"><rect x="340" y="314" width="65" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p2-mono" x="372" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">DIMGP</text></g>
      <g class="p2-chip" style="animation-delay:1.48s"><rect x="413" y="314" width="95" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p2-mono" x="460" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">SLURM HPC</text></g>
    </g>

    <!-- Right Side Dynamic Bode FRF Curve Artwork -->
    <g class="p2-in p2-d2" transform="translate(760 40)">
      <rect width="390" height="280" rx="12" fill="#070C18" stroke="#38BDF8" stroke-opacity=".25"/>
      <!-- Grid lines -->
      <line x1="40" y1="40" x2="350" y2="40" stroke="#38BDF8" stroke-opacity=".1" stroke-dasharray="3 3"/>
      <line x1="40" y1="100" x2="350" y2="100" stroke="#38BDF8" stroke-opacity=".1" stroke-dasharray="3 3"/>
      <line x1="40" y1="160" x2="350" y2="160" stroke="#38BDF8" stroke-opacity=".1" stroke-dasharray="3 3"/>
      <line x1="40" y1="220" x2="350" y2="220" stroke="#38BDF8" stroke-opacity=".15"/>
      <line x1="40" y1="40" x2="40" y2="220" stroke="#38BDF8" stroke-opacity=".15"/>

      <!-- Axis Labels -->
      <text class="p2-mono" x="40" y="242" font-size="9.5" fill="#94A3B8">10 Hz</text>
      <text class="p2-mono" x="180" y="242" font-size="9.5" fill="#94A3B8">100 Hz</text>
      <text class="p2-mono" x="320" y="242" font-size="9.5" fill="#94A3B8">1 kHz</text>
      <text class="p2-mono" x="30" y="50" font-size="9.5" text-anchor="end" fill="#94A3B8">dB</text>

      <!-- Confidence Envelope (Shaded Area) -->
      <path d="M50 200 C 90 195, 110 95, 130 95 C 150 95, 170 185, 200 185 C 230 185, 250 55, 270 55 C 290 55, 310 170, 340 160 L 340 180 C 310 190, 290 75, 270 75 C 250 75, 230 205, 200 205 C 170 205, 150 115, 130 115 C 110 115, 90 215, 50 220 Z" fill="#38BDF8" fill-opacity=".12"/>

      <!-- Ground Truth Curve (NASTRAN) -->
      <path d="M50 210 C 90 205, 110 105, 130 105 C 150 105, 170 195, 200 195 C 230 195, 250 65, 270 65 C 290 65, 310 180, 340 170" fill="none" stroke="#94A3B8" stroke-width="1.8" stroke-dasharray="4 3"/>

      <!-- ML Predicted Curve (HistGradientBoosting / Surrogate) -->
      <path d="M50 210 C 90 205, 110 105, 130 105 C 150 105, 170 195, 200 195 C 230 195, 250 65, 270 65 C 290 65, 310 180, 340 170" fill="none" stroke="#38BDF8" stroke-width="2.5">
        <animate attributeName="stroke-dasharray" values="400;0;400" dur="8s" repeatCount="indefinite"/>
      </path>

      <!-- Scanning Needle -->
      <line x1="270" y1="35" x2="270" y2="220" stroke="#00F2FE" stroke-width="1" stroke-dasharray="2 2">
        <animate attributeName="x1" values="50;340;50" dur="6s" repeatCount="indefinite"/>
        <animate attributeName="x2" values="50;340;50" dur="6s" repeatCount="indefinite"/>
      </line>

      <!-- Legend -->
      <g transform="translate(140 18)" class="p2-mono" font-size="10">
        <line x1="0" y1="0" x2="20" y2="0" stroke="#94A3B8" stroke-dasharray="3 2" stroke-width="1.5"/>
        <text x="26" y="3" fill="#94A3B8">NASTRAN</text>
        <line x1="100" y1="0" x2="120" y2="0" stroke="#38BDF8" stroke-width="2.5"/>
        <text x="126" y="3" fill="#38BDF8">ML Surrogate</text>
      </g>
    </g>
  </g>
</svg>"""
write_svg("project-sciml-surrogate.svg", project_2_svg)

# ==========================================
# 7. Project 3: Acoustics & NVH (viewBox 1200x370)
# ==========================================
project_3_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p3-t">
  <title id="p3-t">Automated Simcenter 3D Vibroacoustics &amp; SPL Field Solver</title>
  <defs>
    <linearGradient id="p3-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0A1122"/><stop offset="1" stop-color="#050811"/>
    </linearGradient>
    <radialGradient id="p3-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".65"/><stop offset="1" stop-color="#1E40AF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p3-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <clipPath id="p3-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p3-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .p3-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .p3-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .p3-in { animation: p3-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p3-d1 { animation-delay: .15s; } .p3-d2 { animation-delay: .4s; }
    .p3-chip { animation: p3-chip .7s cubic-bezier(.34,1.56,.64,1) both; }
    .p3-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p3-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p3-in { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
    @keyframes p3-chip { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
    @keyframes p3-draw { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p3-in, .p3-chip { animation: none; } .p3-draw { animation: none; stroke-dashoffset: 0; } }
  </style>
  <g clip-path="url(#p3-clip)">
    <rect width="1200" height="370" fill="url(#p3-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p3-grid)"/>
    <rect width="1200" height="370" fill="url(#p3-glow)"/>

    <g class="p3-in p3-d1">
      <text class="p3-mono" x="56" y="62" font-size="12" letter-spacing="2.6" fill="#38BDF8">03 · VIBROACOUSTICS · NX OPEN API AUTOMATION</text>
      <text class="p3-serif" x="54" y="126" font-size="50" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">Acoustic &amp; SPL Field Solver</text>
      <text class="p3-sans" x="56" y="166" font-size="17" fill="#94A3B8">Scripted acoustic environment simulation &amp; microphone array processing.</text>
      <text class="p3-mono" x="56" y="200" font-size="12.5" fill="#BAE6FD"><tspan fill="#38BDF8">BUILT ›</tspan> Automated Simcenter 3D setups with NX Open API; simulated airborne noise &amp; ultrasonic fields</text>
      <line class="p3-draw" x1="56" y1="226" x2="680" y2="226" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(56 266)"><text class="p3-serif" font-size="34" font-weight="300" fill="#F8FAFC">120+ Mics</text><text class="p3-sans" y="24" font-size="12.5" fill="#94A3B8">Virtual spherical array</text></g>
      <g transform="translate(261 266)"><text class="p3-serif" font-size="34" font-weight="300" fill="#F8FAFC">85%</text><text class="p3-sans" y="24" font-size="12.5" fill="#94A3B8">Setup time reduction</text></g>
      <g transform="translate(466 266)"><text class="p3-serif" font-size="34" font-weight="300" fill="#F8FAFC">Full SPL</text><text class="p3-sans" y="24" font-size="12.5" fill="#94A3B8">Automated radiation maps</text></g>

      <!-- Chips -->
      <g class="p3-chip" style="animation-delay:1.00s"><rect x="56" y="314" width="115" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p3-mono" x="113" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Simcenter 3D</text></g>
      <g class="p3-chip" style="animation-delay:1.12s"><rect x="179" y="314" width="70" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p3-mono" x="214" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Python</text></g>
      <g class="p3-chip" style="animation-delay:1.24s"><rect x="257" y="314" width="110" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p3-mono" x="312" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">NX Open API</text></g>
      <g class="p3-chip" style="animation-delay:1.36s"><rect x="375" y="314" width="105" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p3-mono" x="427" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Acoustic BEM</text></g>
      <g class="p3-chip" style="animation-delay:1.48s"><rect x="488" y="314" width="115" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p3-mono" x="545" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Sound Power</text></g>
    </g>

    <!-- Right Side Acoustic Wavefront Radiation Visual -->
    <g class="p3-in p3-d2" transform="translate(760 40)">
      <rect width="390" height="280" rx="12" fill="#070C18" stroke="#38BDF8" stroke-opacity=".25"/>

      <!-- Sound Source Center -->
      <g transform="translate(195 140)">
        <circle r="14" fill="#0284C7" stroke="#38BDF8" stroke-width="2"/>
        <circle r="4" fill="#F8FAFC"/>

        <!-- Expanding Pressure Waves -->
        <circle r="35" fill="none" stroke="#38BDF8" stroke-width="1.8" stroke-opacity=".9">
          <animate attributeName="r" values="20;125" dur="3.5s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="3.5s" repeatCount="indefinite"/>
        </circle>
        <circle r="60" fill="none" stroke="#00F2FE" stroke-width="1.5" stroke-opacity=".7">
          <animate attributeName="r" values="20;125" dur="3.5s" begin="1.2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="3.5s" begin="1.2s" repeatCount="indefinite"/>
        </circle>
        <circle r="85" fill="none" stroke="#1E40AF" stroke-width="1.2" stroke-opacity=".5">
          <animate attributeName="r" values="20;125" dur="3.5s" begin="2.4s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="3.5s" begin="2.4s" repeatCount="indefinite"/>
        </circle>

        <!-- Spherical Microphone Array Points -->
        <g stroke="#38BDF8" stroke-width="1" stroke-dasharray="2 3" fill="none">
          <circle r="105"/>
        </g>
        <g fill="#38BDF8">
          <circle cx="105" cy="0" r="3.5"/><circle cx="-105" cy="0" r="3.5"/>
          <circle cx="0" cy="105" r="3.5"/><circle cx="0" cy="-105" r="3.5"/>
          <circle cx="74" cy="74" r="3.5"/><circle cx="-74" cy="74" r="3.5"/>
          <circle cx="74" cy="-74" r="3.5"/><circle cx="-74" cy="-74" r="3.5"/>
        </g>
      </g>

      <!-- Overlay Legend -->
      <g transform="translate(24 240)" class="p3-mono" font-size="10">
        <text fill="#38BDF8">SPL Radiation Field: 84 dB(A)</text>
      </g>
    </g>
  </g>
</svg>"""
write_svg("project-simcenter-acoustics.svg", project_3_svg)

# ==========================================
# 8. Project 4: Interactive 3D Portfolio (viewBox 1200x370)
# ==========================================
project_4_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p4-t">
  <title id="p4-t">Interactive 3D Portfolio: Modern WebGL developer experience</title>
  <defs>
    <linearGradient id="p4-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0A1122"/><stop offset="1" stop-color="#050811"/>
    </linearGradient>
    <radialGradient id="p4-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".65"/><stop offset="1" stop-color="#1E40AF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p4-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#38BDF8" stroke-opacity=".08"/>
    </pattern>
    <clipPath id="p4-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p4-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .p4-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .p4-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
    .p4-in { animation: p4-in 1.2s cubic-bezier(.16,1,.3,1) both; }
    .p4-d1 { animation-delay: .15s; } .p4-d2 { animation-delay: .4s; }
    .p4-chip { animation: p4-chip .7s cubic-bezier(.34,1.56,.64,1) both; }
    .p4-draw { stroke-dasharray: 600; stroke-dashoffset: 600; animation: p4-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }
    @keyframes p4-in { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
    @keyframes p4-chip { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
    @keyframes p4-draw { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) { .p4-in, .p4-chip { animation: none; } .p4-draw { animation: none; stroke-dashoffset: 0; } }
  </style>
  <g clip-path="url(#p4-clip)">
    <rect width="1200" height="370" fill="url(#p4-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p4-grid)"/>
    <rect width="1200" height="370" fill="url(#p4-glow)"/>

    <g class="p4-in p4-d1">
      <text class="p4-mono" x="56" y="62" font-size="12" letter-spacing="2.6" fill="#38BDF8">04 · WEBGL · INTERACTIVE 3D · THREE.JS</text>
      <text class="p4-serif" x="54" y="126" font-size="50" font-weight="300" letter-spacing="-1.5" fill="#F8FAFC">Interactive 3D Portfolio</text>
      <text class="p4-sans" x="56" y="166" font-size="17" fill="#94A3B8">Physics-inspired developer portfolio with real-time 3D rendering.</text>
      <text class="p4-mono" x="56" y="200" font-size="12.5" fill="#BAE6FD"><tspan fill="#38BDF8">BUILT ›</tspan> Modern WebGL engineering visualizations, interactive simulation showcases, responsive GSAP animations</text>
      <line class="p4-draw" x1="56" y1="226" x2="680" y2="226" stroke="#38BDF8" stroke-opacity=".3"/>

      <!-- Metrics -->
      <g transform="translate(56 266)"><text class="p4-serif" font-size="34" font-weight="300" fill="#F8FAFC">60 FPS</text><text class="p4-sans" y="24" font-size="12.5" fill="#94A3B8">WebGL rendering</text></g>
      <g transform="translate(261 266)"><text class="p4-serif" font-size="34" font-weight="300" fill="#F8FAFC">Three.js</text><text class="p4-sans" y="24" font-size="12.5" fill="#94A3B8">Custom shader scenes</text></g>
      <g transform="translate(466 266)"><text class="p4-serif" font-size="34" font-weight="300" fill="#F8FAFC">Global</text><text class="p4-sans" y="24" font-size="12.5" fill="#94A3B8">Netlify live deployment</text></g>

      <!-- Chips -->
      <g class="p4-chip" style="animation-delay:1.00s"><rect x="56" y="314" width="65" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p4-mono" x="88" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">React</text></g>
      <g class="p4-chip" style="animation-delay:1.12s"><rect x="129" y="314" width="95" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p4-mono" x="176" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">TypeScript</text></g>
      <g class="p4-chip" style="animation-delay:1.24s"><rect x="232" y="314" width="80" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p4-mono" x="272" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Three.js</text></g>
      <g class="p4-chip" style="animation-delay:1.36s"><rect x="320" y="314" width="60" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p4-mono" x="350" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">GSAP</text></g>
      <g class="p4-chip" style="animation-delay:1.48s"><rect x="388" y="314" width="105" height="26" rx="13" fill="#0D1A36" stroke="#38BDF8" stroke-opacity=".35"/><text class="p4-mono" x="440" y="331" text-anchor="middle" font-size="11.5" fill="#BAE6FD">Tailwind CSS</text></g>
    </g>

    <!-- Right Side 3D Geometry Rendering Artwork -->
    <g class="p4-in p4-d2" transform="translate(760 40)">
      <rect width="390" height="280" rx="12" fill="#070C18" stroke="#38BDF8" stroke-opacity=".25"/>

      <!-- 3D Polyhedral Object Center -->
      <g transform="translate(195 140)">
        <!-- Rotating Rings -->
        <circle r="95" fill="none" stroke="#38BDF8" stroke-opacity=".2" stroke-dasharray="4 6">
          <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite"/>
        </circle>
        <ellipse rx="85" ry="35" fill="none" stroke="#00F2FE" stroke-opacity=".6" stroke-width="1.4">
          <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="25s" repeatCount="indefinite"/>
        </ellipse>
        <ellipse rx="85" ry="35" fill="none" stroke="#0284C7" stroke-opacity=".4" stroke-width="1.2" transform="rotate(60)"/>

        <!-- 3D Icosahedron / Cube Wireframe -->
        <g stroke="#38BDF8" stroke-width="1.6" fill="#0D1B38" fill-opacity=".6">
          <polygon points="0,-50 43,-25 43,25 0,50 -43,25 -43,-25"/>
          <line x1="0" y1="-50" x2="0" y2="50"/>
          <line x1="-43" y1="-25" x2="43" y2="25"/>
          <line x1="-43" y1="25" x2="43" y2="-25"/>
          <circle cx="0" cy="0" r="6" fill="#F8FAFC"/>
        </g>
      </g>
    </g>
  </g>
</svg>"""
write_svg("project-portfolio-3d.svg", project_4_svg)

# ==========================================
# 9. Tech Constellation (viewBox 1200x500)
# ==========================================
tech_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="1200" height="500" role="img" aria-labelledby="tc-title tc-desc">
  <title id="tc-title">Computational Stack &amp; Tooling</title>
  <desc id="tc-desc">CAE &amp; FEA Solvers: Ansys Mechanical, NASTRAN, Simcenter 3D, HyperMesh. Scientific ML: PyTorch, scikit-learn, PINNs, DIMGP. Vibroacoustics: Modal, Harmonic, FFT, SPL. Agentic &amp; Automation: Claude MCP, PyMechanical, NX Open API. Languages: Python, C++, TypeScript.</desc>
  <defs>
    <linearGradient id="tc-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0A1122"/><stop offset="1" stop-color="#050811"/>
    </linearGradient>
    <radialGradient id="tc-glow" cx="50%" cy="50%" r="60%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".4"/><stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="tc-pulse">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".5" stop-color="#38BDF8" stop-opacity=".6"/><stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="tc-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#F8FAFC"/><stop offset=".45" stop-color="#38BDF8"/><stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .tc-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .tc-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .tc-panel { animation: tc-in 1.1s cubic-bezier(.16,1,.3,1) both; }
    .tc-p1 { animation-delay: .05s; } .tc-p2 { animation-delay: .2s; } .tc-p3 { animation-delay: .35s; }
    .tc-p4 { animation-delay: .5s; } .tc-p5 { animation-delay: .65s; } .tc-p6 { animation-delay: .8s; }
    .tc-web { stroke-dasharray: 1800; stroke-dashoffset: 1800; animation: tc-draw 3s cubic-bezier(.65,0,.35,1) 1s forwards; }
    @keyframes tc-in { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
    @keyframes tc-draw { to { stroke-dashoffset: 0; } }
    @media (prefers-reduced-motion: reduce) {
      .tc-panel { animation: none; }
      .tc-web { animation: none; stroke-dashoffset: 0; }
    }
  </style>

  <rect width="1200" height="500" rx="20" fill="url(#tc-bg)"/>
  <rect width="1200" height="500" rx="20" fill="url(#tc-glow)"/>
  <rect x=".5" y=".5" width="1199" height="499" rx="19.5" fill="none" stroke="#38BDF8" stroke-opacity=".18"/>

  <!-- Constellation: gutters linking the six groups -->
  <path class="tc-web" d="M24 250 H1176 M406 24 V476 M794 24 V476" fill="none" stroke="#38BDF8" stroke-opacity=".22"/>
  <circle cx="0" cy="250" r="8" fill="url(#tc-pulse)" opacity="0">
    <animate attributeName="cx" values="24;1176" dur="9s" begin="3s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.9;1" dur="9s" begin="3s" repeatCount="indefinite"/>
  </circle>
  <g fill="#050811" stroke="#38BDF8">
    <rect x="400" y="244" width="12" height="12" transform="rotate(45 406 250)"/>
    <rect x="788" y="244" width="12" height="12" transform="rotate(45 794 250)"/>
  </g>

  <!-- Panel 1: CAE & FEA Solvers -->
  <g class="tc-panel tc-p1"><g transform="translate(32 32)">
    <rect width="360" height="200" rx="14" fill="#0D162B" fill-opacity=".85" stroke="#38BDF8" stroke-opacity=".22"/>
    <text class="tc-mono" x="24" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">01  CAE &amp; FEA SOLVERS</text>
    <text class="tc-serif" x="24" y="86" font-size="30" font-weight="300" fill="#F8FAFC">Ansys Mechanical <tspan font-size="11" class="tc-mono" fill="#38BDF8" dy="-14">CORE</tspan></text>
    <text class="tc-serif" x="24" y="130" font-size="26" font-weight="300" fill="#F8FAFC">NASTRAN · Simcenter 3D</text>
    <text class="tc-serif" x="24" y="170" font-size="20" font-weight="300" fill="#94A3B8">HyperMesh · Abaqus · OpenCFS</text>
  </g></g>

  <!-- Panel 2: Scientific ML & Surrogates -->
  <g class="tc-panel tc-p2"><g transform="translate(420 32)">
    <rect width="360" height="200" rx="14" fill="#0D162B" fill-opacity=".85" stroke="#38BDF8" stroke-opacity=".22"/>
    <text class="tc-mono" x="24" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">02  SCIENTIFIC ML &amp; SURROGATES</text>
    <text class="tc-serif" x="24" y="86" font-size="30" font-weight="300" fill="#F8FAFC">PyTorch · scikit-learn</text>
    <text class="tc-serif" x="24" y="130" font-size="26" font-weight="300" fill="#F8FAFC">FRF Surrogates · PINNs</text>
    <text class="tc-serif" x="24" y="170" font-size="20" font-weight="300" fill="#94A3B8">DIMGP · Neural Operators · POD-ROM</text>
  </g></g>

  <!-- Panel 3: Vibroacoustics & NVH -->
  <g class="tc-panel tc-p3"><g transform="translate(808 32)">
    <rect width="360" height="200" rx="14" fill="#0D162B" fill-opacity=".85" stroke="#38BDF8" stroke-opacity=".22"/>
    <text class="tc-mono" x="24" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">03  VIBROACOUSTICS &amp; NVH</text>
    <text class="tc-serif" x="24" y="86" font-size="30" font-weight="300" fill="#F8FAFC">Modal &amp; Harmonic Response</text>
    <text class="tc-serif" x="24" y="130" font-size="26" font-weight="300" fill="#F8FAFC">FFT &amp; Order Tracking</text>
    <text class="tc-serif" x="24" y="170" font-size="20" font-weight="300" fill="#94A3B8">SPL Sound Fields · Maxwell Mapping</text>
  </g></g>

  <!-- Panel 4: Agentic & Automation -->
  <g class="tc-panel tc-p4"><g transform="translate(32 268)">
    <rect width="360" height="200" rx="14" fill="#0D162B" fill-opacity=".85" stroke="#38BDF8" stroke-opacity=".22"/>
    <text class="tc-mono" x="24" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">04  AGENTIC &amp; SIMULATION AI</text>
    <text class="tc-serif" x="24" y="86" font-size="30" font-weight="300" fill="#F8FAFC">Claude MCP <tspan font-size="11" class="tc-mono" fill="#38BDF8" dy="-14">PROTOCOL</tspan></text>
    <text class="tc-serif" x="24" y="130" font-size="26" font-weight="300" fill="#F8FAFC">PyMechanical · NX Open API</text>
    <text class="tc-serif" x="24" y="170" font-size="20" font-weight="300" fill="#94A3B8">SLURM HPC · Linux Bash · Git</text>
  </g></g>

  <!-- Panel 5: Software & Computation -->
  <g class="tc-panel tc-p5"><g transform="translate(420 268)">
    <rect width="360" height="200" rx="14" fill="#0D162B" fill-opacity=".85" stroke="#38BDF8" stroke-opacity=".22"/>
    <text class="tc-mono" x="24" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">05  PROGRAMMING &amp; WEB</text>
    <text class="tc-serif" x="24" y="86" font-size="30" font-weight="300" fill="#F8FAFC">Python <tspan font-size="11" class="tc-mono" fill="#38BDF8" dy="-14">PRIMARY</tspan></text>
    <text class="tc-serif" x="24" y="130" font-size="26" font-weight="300" fill="#F8FAFC">C++ · TypeScript</text>
    <text class="tc-serif" x="24" y="170" font-size="20" font-weight="300" fill="#94A3B8">React · Three.js · Docker · FastAPI</text>
  </g></g>

  <!-- Panel 6: Affiliations & Credentials -->
  <g class="tc-panel tc-p6"><g transform="translate(808 268)">
    <rect width="360" height="200" rx="14" fill="#0D162B" fill-opacity=".85" stroke="#38BDF8" stroke-opacity=".22"/>
    <text class="tc-mono" x="24" y="38" font-size="11" letter-spacing="2.4" fill="#38BDF8">06  AFFILIATIONS &amp; CREDS</text>
    <text class="tc-serif" x="24" y="86" font-size="30" font-weight="300" fill="#F8FAFC">FAU Erlangen-Nürnberg</text>
    <text class="tc-serif" x="24" y="130" font-size="26" font-weight="300" fill="#F8FAFC">Mercedes-Benz · Valeo</text>
    <text class="tc-serif" x="24" y="170" font-size="20" font-weight="300" fill="#94A3B8">English C2 · German B2 · Class B</text>
  </g></g>
</svg>"""
write_svg("tech-constellation.svg", tech_svg)

# ==========================================
# 10. Footer Signature (viewBox 1200x230)
# ==========================================
footer_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 230" width="1200" height="230" role="img" aria-labelledby="sig-title">
  <title id="sig-title">Vamshidhar Reddy — Engineering physics with computational rigor.</title>
  <defs>
    <linearGradient id="sig-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#050811"/>
      <stop offset="1" stop-color="#0A1122"/>
    </linearGradient>
    <radialGradient id="sig-glow" cx="50%" cy="100%" r="70%">
      <stop offset="0" stop-color="#0284C7" stop-opacity=".55"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sig-line" gradientUnits="userSpaceOnUse" x1="100" y1="0" x2="1100" y2="0">
      <stop offset="0" stop-color="#0284C7" stop-opacity="0"/>
      <stop offset=".5" stop-color="#38BDF8"/>
      <stop offset="1" stop-color="#0284C7" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .sig-serif { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }
    .sig-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
    .sig-name {
      stroke: #38BDF8; stroke-width: 1; fill: #F8FAFC; fill-opacity: 0;
      stroke-dasharray: 900; stroke-dashoffset: 900;
      animation: sig-write 3.6s cubic-bezier(.65,0,.35,1) .3s forwards;
    }
    .sig-rule { stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: sig-draw 2.4s cubic-bezier(.65,0,.35,1) 1.6s forwards; }
    .sig-in { animation: sig-in 1.4s ease 2.6s both; }
    @keyframes sig-write { 70% { stroke-dashoffset: 0; fill-opacity: 0; } 100% { stroke-dashoffset: 0; fill-opacity: 1; } }
    @keyframes sig-draw { to { stroke-dashoffset: 0; } }
    @keyframes sig-in { from { opacity: 0; } to { opacity: 1; } }
    @media (prefers-reduced-motion: reduce) {
      .sig-name { animation: none; stroke-dashoffset: 0; fill-opacity: 1; }
      .sig-rule { animation: none; stroke-dashoffset: 0; }
      .sig-in { animation: none; }
      .sig-sparks { display: none; }
    }
  </style>

  <rect width="1200" height="230" rx="20" fill="url(#sig-bg)"/>
  <rect width="1200" height="230" rx="20" fill="url(#sig-glow)"/>

  <!-- Rising computational blue sparks -->
  <g class="sig-sparks" fill="#38BDF8" opacity=".9">
    <circle cx="451" cy="230" r="1.0"><animate attributeName="cy" values="232;108" dur="7.3s" begin="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="7.3s" begin="2.4s" repeatCount="indefinite"/></circle>
    <circle cx="216" cy="230" r="1.5"><animate attributeName="cy" values="232;44" dur="5.3s" begin="0.3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="5.3s" begin="0.3s" repeatCount="indefinite"/></circle>
    <circle cx="208" cy="230" r="1.1"><animate attributeName="cy" values="232;94" dur="5.5s" begin="0.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="5.5s" begin="0.4s" repeatCount="indefinite"/></circle>
    <circle cx="180" cy="230" r="1.2"><animate attributeName="cy" values="232;120" dur="6.9s" begin="0.7s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="6.9s" begin="0.7s" repeatCount="indefinite"/></circle>
    <circle cx="716" cy="230" r="1.4"><animate attributeName="cy" values="232;68" dur="7.3s" begin="3.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="7.3s" begin="3.5s" repeatCount="indefinite"/></circle>
    <circle cx="167" cy="230" r="1.4"><animate attributeName="cy" values="232;109" dur="5.9s" begin="0.8s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="5.9s" begin="0.8s" repeatCount="indefinite"/></circle>
    <circle cx="240" cy="230" r="1.7"><animate attributeName="cy" values="232;53" dur="6.0s" begin="3.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="6.0s" begin="3.4s" repeatCount="indefinite"/></circle>
    <circle cx="715" cy="230" r="1.1"><animate attributeName="cy" values="232;48" dur="6.0s" begin="1.1s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="6.0s" begin="1.1s" repeatCount="indefinite"/></circle>
    <circle cx="697" cy="230" r="1.7"><animate attributeName="cy" values="232;94" dur="4.2s" begin="1.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="4.2s" begin="1.2s" repeatCount="indefinite"/></circle>
    <circle cx="915" cy="230" r="1.5"><animate attributeName="cy" values="232;78" dur="5.1s" begin="3.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="5.1s" begin="3.5s" repeatCount="indefinite"/></circle>
    <circle cx="374" cy="230" r="1.2"><animate attributeName="cy" values="232;113" dur="6.8s" begin="4.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="6.8s" begin="4.2s" repeatCount="indefinite"/></circle>
    <circle cx="427" cy="230" r="1.7"><animate attributeName="cy" values="232;76" dur="5.8s" begin="5.3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="5.8s" begin="5.3s" repeatCount="indefinite"/></circle>
  </g>

  <text class="sig-serif sig-name" x="600" y="104" text-anchor="middle" font-size="70" font-style="italic" font-weight="300" letter-spacing="-1">Vamshidhar Reddy</text>

  <path class="sig-rule" d="M100 134 H1100" stroke="url(#sig-line)" stroke-width="1"/>
  <circle cx="600" cy="134" r="3" fill="#F8FAFC" class="sig-in">
    <animate attributeName="r" values="3;5;3" dur="3.2s" repeatCount="indefinite"/>
  </circle>

  <g class="sig-in">
    <text class="sig-serif" x="600" y="176" text-anchor="middle" font-size="20" font-style="italic" fill="#F8FAFC">Engineering physics with computational rigor.</text>
    <text class="sig-mono" x="600" y="206" text-anchor="middle" font-size="11" letter-spacing="3" fill="#94A3B8">CAE &amp; STRUCTURAL DYNAMICS · SCIENTIFIC MACHINE LEARNING · AGENTIC SIMULATION</text>
  </g>
</svg>"""
write_svg("footer-signature.svg", footer_svg)

print("All assets generated successfully!")
