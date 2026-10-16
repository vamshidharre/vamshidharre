import os

OUTPUT_DIR = r"C:\Users\vamsh\.gemini\antigravity\scratch\vamshidharre\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def write_svg(filename, content):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated {filename}")

# Shared Font Stacks - Modern, Clean, High-Legibility Engineering Hierarchy
SANS = '-apple-system, BlinkMacSystemFont, "Segoe UI", Inter, Roboto, "Helvetica Neue", Arial, sans-serif'
MONO = 'ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace'

# =============================================================
# 1. Section Titles (viewBox 1200x120)
# =============================================================
def generate_title(num, tag, title_main, title_bold, right_mono, prefix):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="{num} {tag}: {title_main} {title_bold}">
  <defs>
    <linearGradient id="{prefix}-line" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">
      <stop offset="0" stop-color="#3B82F6"/>
      <stop offset=".4" stop-color="#1D4ED8"/>
      <stop offset=".8" stop-color="#1E3A8A"/>
      <stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="{prefix}-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".6" stop-color="#93C5FD"/>
      <stop offset="1" stop-color="#60A5FA"/>
    </linearGradient>
    <radialGradient id="{prefix}-pulse">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".5" stop-color="#60A5FA" stop-opacity=".7"/>
      <stop offset="1" stop-color="#1D4ED8" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .{prefix}-sans {{ font-family: {SANS}; }}
    .{prefix}-mono {{ font-family: {MONO}; }}
    .{prefix}-in {{ animation: {prefix}-in 1.1s cubic-bezier(.16,1,.3,1) both; }}
    .{prefix}-d2 {{ animation-delay: .2s; }} .{prefix}-d3 {{ animation-delay: .45s; }}
    .{prefix}-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: {prefix}-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes {prefix}-in {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes {prefix}-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .{prefix}-in {{ animation: none; }} .{prefix}-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g class="{prefix}-in">
    <text class="{prefix}-mono" x="40" y="34" font-size="11.5" font-weight="700" letter-spacing="2.6" fill="#60A5FA"><tspan fill="#93C5FD">{num}</tspan>   {tag}</text>
  </g>
  <g class="{prefix}-in {prefix}-d2">
    <text class="{prefix}-sans" x="38" y="82" font-size="38" font-weight="800" letter-spacing="-0.5" fill="#FFFFFF">{title_main} <tspan fill="url(#{prefix}-sheen)">{title_bold}</tspan></text>
  </g>
  <g class="{prefix}-in {prefix}-d3">
    <text class="{prefix}-mono" x="1160" y="34" text-anchor="end" font-size="10.5" font-weight="600" letter-spacing="2.2" fill="#94A3B8">{right_mono}</text>
  </g>
  <path class="{prefix}-draw" d="M40 104 H1160" stroke="url(#{prefix}-line)" stroke-width="1.4"/>
  <circle cx="40" cy="104" r="5" fill="url(#{prefix}-pulse)" opacity="0">
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

# =============================================================
# 2. Hero Banner (viewBox 1200x480) - Crisp, Zero Blurring/Overlaps
# =============================================================
hero_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">Vamshidhar Reddy — Computational Mechanics, Structural Dynamics &amp; Scientific ML</title>
  <desc id="hero-desc">CAE &amp; Structural Dynamics Engineer, Scientific ML Researcher. M.Sc. in Computational Engineering at FAU Erlangen-Nürnberg.</desc>

  <defs>
    <radialGradient id="hero-bg" cx="72%" cy="38%" r="80%">
      <stop offset="0" stop-color="#111726"/>
      <stop offset=".55" stop-color="#0B0F17"/>
      <stop offset="1" stop-color="#06080D"/>
    </radialGradient>
    <radialGradient id="hero-light-a" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".55"/>
      <stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-light-b" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#2563EB" stop-opacity=".35"/>
      <stop offset="1" stop-color="#1E40AF" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hero-name-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".45" stop-color="#E2E8F0"/>
      <stop offset=".80" stop-color="#93C5FD"/>
      <stop offset="1" stop-color="#60A5FA"/>
    </linearGradient>
    <linearGradient id="hero-scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#60A5FA" stop-opacity="0"/>
      <stop offset=".5" stop-color="#60A5FA" stop-opacity=".06"/>
      <stop offset="1" stop-color="#60A5FA" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#60A5FA" stop-opacity="0"/>
      <stop offset=".15" stop-color="#93C5FD"/>
      <stop offset=".75" stop-color="#1D4ED8"/>
      <stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-orbit-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#60A5FA" stop-opacity=".75"/>
      <stop offset=".5" stop-color="#1D4ED8" stop-opacity=".4"/>
      <stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </linearGradient>
    <pattern id="hero-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#60A5FA" stroke-opacity=".05" stroke-width="1"/>
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
    .hero-sans {{ font-family: {SANS}; }}
    .hero-mono {{ font-family: {MONO}; }}

    .hero-rise {{ animation: hero-rise 1.4s cubic-bezier(.16,1,.3,1) both; }}
    .hero-fade {{ animation: hero-fade 1.6s cubic-bezier(.16,1,.3,1) both; }}
    .d1 {{ animation-delay: .15s; }} .d2 {{ animation-delay: .35s; }} .d3 {{ animation-delay: .6s; }}
    .d4 {{ animation-delay: .85s; }} .d5 {{ animation-delay: 1.1s; }} .d6 {{ animation-delay: 1.35s; }}

    .hero-draw {{ stroke-dasharray: 900; stroke-dashoffset: 900; animation: hero-draw 2.4s cubic-bezier(.65,0,.35,1) .9s forwards; }}

    @keyframes hero-rise {{ from {{ opacity: 0; transform: translateY(18px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes hero-fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes hero-draw {{ to {{ stroke-dashoffset: 0; }} }}

    @media (prefers-reduced-motion: reduce) {{
      .hero-rise, .hero-fade {{ animation: none; }}
      .hero-draw {{ animation: none; stroke-dashoffset: 0; }}
    }}
  </style>

  <g clip-path="url(#hero-clip)">
    <!-- Canvas Background -->
    <rect width="1200" height="480" fill="url(#hero-bg)"/>

    <!-- Ambient Lighting Glows -->
    <ellipse cx="940" cy="140" rx="420" ry="300" fill="url(#hero-light-a)">
      <animateTransform attributeName="transform" type="translate" values="0 0; -60 30; 0 0" dur="22s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>
    <ellipse cx="180" cy="460" rx="360" ry="220" fill="url(#hero-light-b)">
      <animateTransform attributeName="transform" type="translate" values="0 0; 70 -25; 0 0" dur="28s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>

    <!-- Technical Grid -->
    <rect width="1200" height="480" fill="url(#hero-grid)" mask="url(#hero-grid-mask)"/>

    <!-- Subtle Scan Line -->
    <rect x="0" y="-140" width="1200" height="140" fill="url(#hero-scan)">
      <animate attributeName="y" values="-140;480" dur="11s" begin="2s" repeatCount="indefinite"/>
    </rect>

    <!-- Drifting Computational Sparks -->
    <g fill="#93C5FD">
      <circle cx="540" cy="110" r="1.3"><animate attributeName="opacity" values="0;.85;0" dur="4.2s" repeatCount="indefinite"/><animate attributeName="cy" values="110;86" dur="4.2s" repeatCount="indefinite"/></circle>
      <circle cx="680" cy="65" r="1.0"><animate attributeName="opacity" values="0;.75;0" dur="5.6s" begin="1s" repeatCount="indefinite"/><animate attributeName="cy" values="65;43" dur="5.6s" begin="1s" repeatCount="indefinite"/></circle>
      <circle cx="1120" cy="380" r="1.5"><animate attributeName="opacity" values="0;.85;0" dur="4.8s" begin="2s" repeatCount="indefinite"/><animate attributeName="cy" values="380;352" dur="4.8s" begin="2s" repeatCount="indefinite"/></circle>
      <circle cx="760" cy="410" r="1.1"><animate attributeName="opacity" values="0;.65;0" dur="6s" begin=".5s" repeatCount="indefinite"/><animate attributeName="cy" values="410;386" dur="6s" begin=".5s" repeatCount="indefinite"/></circle>
    </g>

    <!-- Right Side: 3D FEA Structural Mesh & Orbital Telemetry (NO PHOTO) -->
    <!-- Positioned safely at x=940, y=215, radius 165 with plenty of clearance from text -->
    <g transform="translate(940 215)" class="hero-fade d3">
      <!-- Outer Telemetry Coordinate Rings -->
      <circle r="165" fill="none" stroke="#60A5FA" stroke-opacity=".12" stroke-dasharray="2 10">
        <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="140s" repeatCount="indefinite"/>
      </circle>
      <circle r="140" fill="none" stroke="url(#hero-orbit-grad)" stroke-width="1.3"/>
      <circle r="112" fill="none" stroke="#60A5FA" stroke-opacity=".18" stroke-dasharray="3 7"/>

      <!-- Orbiting Satellite Indicator -->
      <g>
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="75s" repeatCount="indefinite"/>
        <circle cx="140" cy="0" r="4.5" fill="#93C5FD" filter="url(#hero-glow)"/>
        <circle cx="-99" cy="-99" r="3" fill="#3B82F6"/>
      </g>

      <!-- 3D FEA Structural Mesh in Center -->
      <g transform="translate(0 0)">
        <polygon points="-65,45 0,80 65,45 0,10" fill="#0C1322" stroke="#1D4ED8" stroke-width="1.5"/>
        <polygon points="-65,45 -65,58 0,93 0,80" fill="#070C16" stroke="#1D4ED8" stroke-width="1.2"/>
        <polygon points="0,80 0,93 65,58 65,45" fill="#050810" stroke="#1D4ED8" stroke-width="1.2"/>

        <polygon points="-30,26 0,42 0,-45 -30,-60" fill="#101D36" stroke="#3B82F6" stroke-width="1.3"/>
        <polygon points="0,42 30,26 30,-60 0,-45" fill="#0A1426" stroke="#3B82F6" stroke-width="1.3"/>
        <polygon points="-30,-60 0,-45 30,-60 0,-76" fill="#1D4ED8" stroke="#93C5FD" stroke-width="1.5"/>

        <line x1="-30" y1="-17" x2="0" y2="-2" stroke="#60A5FA" stroke-opacity=".35" stroke-width="1"/>
        <line x1="0" y1="-2" x2="30" y2="-17" stroke="#60A5FA" stroke-opacity=".35" stroke-width="1"/>
        <line x1="-15" y1="-53" x2="-15" y2="34" stroke="#60A5FA" stroke-opacity=".25" stroke-width="1"/>
        <line x1="15" y1="-53" x2="15" y2="34" stroke="#60A5FA" stroke-opacity=".25" stroke-width="1"/>

        <!-- Dynamic Modal Waveform -->
        <path d="M0 -45 C 22 -26, 26 10, 0 42" stroke="#60A5FA" stroke-width="2.5" fill="none" filter="url(#hero-glow)">
          <animate attributeName="d" values="M0 -45 C 24 -26, 28 10, 0 42; M0 -45 C -24 -26, -28 10, 0 42; M0 -45 C 24 -26, 28 10, 0 42" dur="2.8s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
        </path>

        <circle cx="0" cy="0" r="5" fill="#FFFFFF" filter="url(#hero-glow)"/>
        <circle cx="0" cy="0" r="14" fill="none" stroke="#60A5FA" stroke-width="1.2" stroke-opacity=".8">
          <animate attributeName="r" values="8;32" dur="3s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values=".9;0" dur="3s" repeatCount="indefinite"/>
        </circle>
      </g>

      <!-- Engineering Pillar Node Badges (Cleanly separated from any lines) -->
      <g class="hero-mono" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#94A3B8">
        <g transform="translate(-115 -125)"><circle r="3.5" fill="#3B82F6"/><text x="10" y="4" fill="#F8FAFC">CAE / FEA</text></g>
        <g transform="translate(125 -85)"><circle r="3.5" fill="#3B82F6"/><text x="10" y="4" fill="#F8FAFC">SciML</text></g>
        <g transform="translate(125 95)"><circle r="3.5" fill="#3B82F6"/><text x="10" y="4" fill="#F8FAFC">NVH</text></g>
        <g transform="translate(-135 75)"><circle r="3.5" fill="#3B82F6"/><text x="-12" y="4" text-anchor="end" fill="#F8FAFC">AGENTIC</text></g>
      </g>
    </g>

    <!-- Left Column: Terminal Pill -->
    <g class="hero-fade d1" transform="translate(72 50)">
      <rect width="320" height="34" rx="17" fill="#0E131E" stroke="#3B82F6" stroke-opacity=".4" stroke-width="1.2"/>
      <circle cx="18" cy="17" r="4" fill="#3B82F6">
        <animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/>
      </circle>
      <text class="hero-mono" x="32" y="21.5" font-size="12" font-weight="600" fill="#94A3B8">~/vamshidhar<tspan fill="#60A5FA"> $ </tspan><tspan fill="#F8FAFC">run --simulation</tspan></text>
      <rect x="286" y="10" width="7" height="14" fill="#93C5FD">
        <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- Eyebrow -->
    <g class="hero-rise d2" transform="translate(72 118)">
      <line x1="0" y1="0" x2="28" y2="0" stroke="#3B82F6" stroke-width="2"/>
      <text class="hero-mono" x="38" y="4" font-size="11.5" font-weight="700" letter-spacing="2.2" fill="#60A5FA">COMPUTATIONAL MECHANICS · SCIENTIFIC ML</text>
    </g>

    <!-- Name (Two Clean High-Contrast Lines, Single Text Node per Line - No Ghosting) -->
    <text class="hero-sans hero-rise d3" x="70" y="195" font-size="68" font-weight="800" letter-spacing="-1" fill="#FFFFFF">Vamshidhar</text>
    <text class="hero-sans hero-rise d4" x="70" y="265" font-size="68" font-weight="800" letter-spacing="-1" fill="url(#hero-name-grad)">Reddy<tspan fill="#60A5FA">.</tspan></text>

    <!-- Glowing Underline Rule -->
    <path class="hero-draw" d="M72 295 H560" fill="none" stroke="url(#hero-rule)" stroke-width="2.2" stroke-linecap="round" filter="url(#hero-glow)"/>

    <!-- Roles & Positioning (Two Clean Lines) -->
    <g class="hero-rise d5" transform="translate(72 332)">
      <text class="hero-sans" font-size="15" font-weight="700" letter-spacing="1.2" fill="#FFFFFF">CAE &amp; STRUCTURAL DYNAMICS ENGINEER</text>
      <text class="hero-sans" y="24" font-size="13.5" font-weight="600" letter-spacing="1.2" fill="#93C5FD">SCIENTIFIC ML &amp; SIMULATION AUTOMATION</text>
    </g>

    <!-- Tagline (Two Clean Lines) -->
    <g class="hero-rise d6" transform="translate(72 388)">
      <text class="hero-sans" font-size="15" font-weight="400" fill="#E2E8F0">Engineering physics with rigorous computation.</text>
      <text class="hero-sans" y="22" font-size="13.5" font-weight="400" fill="#94A3B8">Accelerating simulations with scientific intelligence.</text>
    </g>

    <!-- Meta Strip at Bottom -->
    <g class="hero-fade d6">
      <line x1="72" y1="446" x2="1128" y2="446" stroke="#3B82F6" stroke-opacity=".18"/>
      <text class="hero-mono" x="72" y="466" font-size="11" font-weight="600" letter-spacing="1.5" fill="#94A3B8">M.SC COMPUTATIONAL ENGINEERING · FAU</text>
      <text class="hero-mono" x="1128" y="466" text-anchor="end" font-size="11" font-weight="600" letter-spacing="1.5" fill="#60A5FA">MERCEDES-BENZ (SCIML) · VALEO (NVH)</text>
    </g>

    <!-- Frame -->
    <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="#3B82F6" stroke-opacity=".22"/>
    <path d="M22 2 h28 M2 22 v28 M1178 2 h-28 M1198 22 v28 M22 478 h28 M2 458 v-28 M1178 478 h-28 M1198 458 v-28" stroke="#60A5FA" stroke-width="1.8" stroke-opacity=".7" fill="none"/>
  </g>
</svg>"""
write_svg("hero-portrait.svg", hero_svg)

# =============================================================
# 3. About Intro (viewBox 1200x420) - 100% Instantly Visible Text
# =============================================================
about_intro_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ab-t ab-d">
  <title id="ab-t">About Vamshidhar Reddy</title>
  <desc id="ab-d">CAE &amp; Structural Dynamics Engineer, Scientific ML Researcher. M.Sc. Computational Engineering at FAU Erlangen-Nürnberg. Experience at Mercedes-Benz (SciML surrogates) and Valeo eAutomotive (Master Thesis NVH). Specialized in Ansys Mechanical, NASTRAN, Simcenter 3D, PyTorch, and Claude MCP agentic simulation.</desc>
  <defs>
    <linearGradient id="ab-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0E131E"/><stop offset="1" stop-color="#06080D"/></linearGradient>
    <radialGradient id="ab-glow" cx="80%" cy="20%" r="70%"><stop offset="0" stop-color="#1D4ED8" stop-opacity=".4"/><stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/></radialGradient>
    <pattern id="ab-scan" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#F8FAFC" opacity=".025"/></pattern>
  </defs>
  <style>
    .ab-sans {{ font-family: {SANS}; }}
    .ab-mono {{ font-family: {MONO}; }}
    .ab-card {{ animation: ab-in 1s cubic-bezier(.16,1,.3,1) both; }}
    .ab-fade {{ animation: ab-fade 1s ease both; }}
    @keyframes ab-in {{ from {{ opacity: 0; transform: translateX(24px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ab-fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ab-card, .ab-fade {{ animation: none; }} }}
  </style>
  <rect width="1200" height="420" rx="20" fill="url(#ab-bg)"/>
  <rect width="1200" height="420" rx="20" fill="url(#ab-glow)"/>
  <rect x=".5" y=".5" width="1199" height="419" rx="19.5" fill="none" stroke="#3B82F6" stroke-opacity=".2"/>

  <!-- Terminal Window (Left: x=40 to 770, width=730) -->
  <g class="ab-fade">
    <rect x="40" y="36" width="730" height="348" rx="14" fill="#070A10" stroke="#1E293B" stroke-width="1.3"/>
    <rect x="40" y="36" width="730" height="348" rx="14" fill="url(#ab-scan)"/>
    <path d="M40 50 a14 14 0 0 1 14 -14 H756 a14 14 0 0 1 14 14 V72 H40 Z" fill="#0F141F"/>
    <line x1="40" y1="72" x2="770" y2="72" stroke="#1E293B" stroke-width="1.2"/>
    <circle cx="62" cy="54" r="4.5" fill="#EF4444"/><circle cx="78" cy="54" r="4.5" fill="#F59E0B"/><circle cx="94" cy="54" r="4.5" fill="#10B981"/>
    <text class="ab-mono" x="405" y="58" text-anchor="middle" font-size="11.5" font-weight="600" letter-spacing="1.2" fill="#CBD5E1">vamshidhar@cae-lab: ~</text>
  </g>

  <!-- Terminal Content: 100% Instantly Readable, High Contrast -->
  <g class="ab-mono" font-size="13">
    <!-- Line 1 -->
    <text x="68" y="118" fill="#60A5FA" font-weight="700">$</text>
    <text x="88" y="118" fill="#FFFFFF" font-weight="600">whoami</text>
    <!-- Line 2 -->
    <text x="68" y="142" fill="#3B82F6" font-weight="700">→</text>
    <text x="88" y="142" fill="#E2E8F0">Vamshidhar Reddy · CAE &amp; Structural Dynamics Engineer</text>
    <!-- Line 3 -->
    <text x="68" y="168" fill="#60A5FA" font-weight="700">$</text>
    <text x="88" y="168" fill="#FFFFFF" font-weight="600">cat education.txt</text>
    <!-- Line 4 -->
    <text x="68" y="192" fill="#3B82F6" font-weight="700">→</text>
    <text x="88" y="192" fill="#E2E8F0">M.Sc. Computational Engineering · FAU Erlangen-Nürnberg</text>
    <!-- Line 5 -->
    <text x="68" y="218" fill="#60A5FA" font-weight="700">$</text>
    <text x="88" y="218" fill="#FFFFFF" font-weight="600">cat experience.txt</text>
    <!-- Line 6 -->
    <text x="68" y="242" fill="#3B82F6" font-weight="700">→</text>
    <text x="88" y="242" fill="#E2E8F0">Mercedes-Benz (SciML) · Valeo (E-Motor NVH Thesis)</text>
    <!-- Line 7 -->
    <text x="68" y="268" fill="#60A5FA" font-weight="700">$</text>
    <text x="88" y="268" fill="#FFFFFF" font-weight="600">ls ./automated</text>
    <!-- Line 8 -->
    <text x="68" y="292" fill="#3B82F6" font-weight="700">→</text>
    <text x="88" y="292" fill="#E2E8F0">ansys-claude-mcp  nastran-surrogate  simcenter-acoustics</text>
    <!-- Line 9 -->
    <text x="68" y="318" fill="#60A5FA" font-weight="700">$</text>
    <text x="88" y="318" fill="#FFFFFF" font-weight="600">echo $MISSION</text>
    <!-- Line 10 -->
    <text x="68" y="342" fill="#3B82F6" font-weight="700">→</text>
    <text x="88" y="342" fill="#E2E8F0">physics-grounded simulations · zero-compromise precision</text>
  </g>

  <!-- Blinking Terminal Cursor -->
  <rect x="68" y="354" width="8" height="15" fill="#60A5FA">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
  </rect>

  <!-- Right Stacked Cards (x=800 to 1160, width=360) -->
  <g class="ab-card" style="animation-delay:0.2s"><g transform="translate(800 48)">
    <rect width="360" height="96" rx="14" fill="#0F141F" stroke="#2563EB" stroke-opacity=".35" stroke-width="1.2"/>
    <rect x="0" y="0" width="4" height="96" rx="2" fill="#3B82F6"/>
    <text class="ab-mono" x="22" y="26" font-size="10.5" font-weight="700" letter-spacing="2" fill="#60A5FA">CORE DOMAIN</text>
    <text class="ab-sans" x="22" y="54" font-size="22" font-weight="800" fill="#FFFFFF">CAE &amp; FEA Solvers</text>
    <text class="ab-sans" x="22" y="74" font-size="12.5" font-weight="500" fill="#CBD5E1">Ansys Mechanical (APDL, PyMechanical)</text>
    <text class="ab-sans" x="22" y="89" font-size="11.5" font-weight="400" fill="#94A3B8">NASTRAN · Simcenter 3D · HyperMesh</text>
  </g></g>
  <g class="ab-card" style="animation-delay:0.4s"><g transform="translate(800 162)">
    <rect width="360" height="96" rx="14" fill="#0F141F" stroke="#2563EB" stroke-opacity=".35" stroke-width="1.2"/>
    <rect x="0" y="0" width="4" height="96" rx="2" fill="#3B82F6"/>
    <text class="ab-mono" x="22" y="26" font-size="10.5" font-weight="700" letter-spacing="2" fill="#60A5FA">WHERE ML ACCELERATES</text>
    <text class="ab-sans" x="22" y="54" font-size="22" font-weight="800" fill="#FFFFFF">Scientific ML</text>
    <text class="ab-sans" x="22" y="74" font-size="12.5" font-weight="500" fill="#CBD5E1">Physics-Informed ML &amp; FRF Surrogates</text>
    <text class="ab-sans" x="22" y="89" font-size="11.5" font-weight="400" fill="#94A3B8">PINNs · DIMGP · PyTorch · scikit-learn</text>
  </g></g>
  <g class="ab-card" style="animation-delay:0.6s"><g transform="translate(800 276)">
    <rect width="360" height="96" rx="14" fill="#0F141F" stroke="#2563EB" stroke-opacity=".35" stroke-width="1.2"/>
    <rect x="0" y="0" width="4" height="96" rx="2" fill="#3B82F6"/>
    <text class="ab-mono" x="22" y="26" font-size="10.5" font-weight="700" letter-spacing="2" fill="#60A5FA">AUTOMATION EDGE</text>
    <text class="ab-sans" x="22" y="54" font-size="22" font-weight="800" fill="#FFFFFF">Agentic Simulation</text>
    <text class="ab-sans" x="22" y="74" font-size="12.5" font-weight="500" fill="#CBD5E1">Claude MCP Autonomous Simulation</text>
    <text class="ab-sans" x="22" y="89" font-size="11.5" font-weight="400" fill="#94A3B8">PyMechanical API · NX Open · SLURM</text>
  </g></g>
</svg>"""
write_svg("about-intro.svg", about_intro_svg)

# =============================================================
# 4. Recognition & Achievements (viewBox 1200x430) - Sushmita Layout
# =============================================================
achieve_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 430" width="1200" height="430" role="img" aria-labelledby="ach-title ach-desc">
  <title id="ach-title">Recognition &amp; Impact</title>
  <desc id="ach-desc">Mercedes-Benz Scientific ML Surrogates: cut NASTRAN solve times from ~6 hours to milliseconds. Valeo eAutomotive Master Thesis: E-Motor NVH &amp; Stator resonance isolation with experimental correlation. M.Sc. Computational Engineering at FAU Erlangen-Nürnberg.</desc>

  <defs>
    <linearGradient id="ach-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0E131E"/>
      <stop offset="1" stop-color="#06080D"/>
    </linearGradient>
    <radialGradient id="ach-glow-a" cx="85%" cy="0%" r="90%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".65"/>
      <stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ach-glow-b" cx="90%" cy="0%" r="90%">
      <stop offset="0" stop-color="#2563EB" stop-opacity=".35"/>
      <stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ach-outline" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#60A5FA" stop-opacity=".15"/>
      <stop offset="1" stop-color="#1D4ED8" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ach-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".06"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="ach-clip-a"><rect x="0" y="0" width="700" height="250" rx="16"/></clipPath>
    <clipPath id="ach-clip-b"><rect x="0" y="0" width="476" height="250" rx="16"/></clipPath>
  </defs>

  <style>
    .ach-sans {{ font-family: {SANS}; }}
    .ach-mono {{ font-family: {MONO}; }}
    .ach-in {{ animation: ach-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .a1 {{ animation-delay: .1s; }} .a2 {{ animation-delay: .35s; }} .a3 {{ animation-delay: .6s; }}
    .ach-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: ach-draw 2.6s cubic-bezier(.65,0,.35,1) .8s forwards; }}
    @keyframes ach-in {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ach-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .ach-in {{ animation: none; }}
      .ach-draw {{ animation: none; stroke-dashoffset: 0; }}
    }}
  </style>

  <rect width="1200" height="430" rx="20" fill="url(#ach-bg)"/>
  <rect x=".5" y=".5" width="1199" height="429" rx="19.5" fill="none" stroke="#3B82F6" stroke-opacity=".2"/>

  <!-- Card 1: Mercedes-Benz (x=24, width=700, height=250) -->
  <g class="ach-in a1"><g transform="translate(24 24)">
    <g clip-path="url(#ach-clip-a)">
      <rect width="700" height="250" fill="#0F141F"/>
      <rect width="700" height="250" fill="url(#ach-glow-a)"/>
      <!-- Soft Watermark safely in upper right corner, completely clear of text -->
      <text class="ach-sans" x="680" y="115" text-anchor="end" font-size="95" font-weight="900" letter-spacing="-3" fill="url(#ach-outline)">3,600×</text>
      <rect x="-300" y="0" width="260" height="250" fill="url(#ach-sheen)" transform="skewX(-18)">
        <animate attributeName="x" values="-300;900;900" keyTimes="0;.35;1" dur="9s" begin="2s" repeatCount="indefinite"/>
      </rect>
    </g>
    <rect width="700" height="250" rx="16" fill="none" stroke="#2563EB" stroke-opacity=".35" stroke-width="1.2"/>

    <!-- Content strictly located in the lower half (y >= 154) - ZERO collision with watermark -->
    <text class="ach-mono" x="36" y="154" font-size="11.5" font-weight="700" letter-spacing="2.4" fill="#60A5FA">SCIENTIFIC ML · MERCEDES-BENZ</text>
    <text class="ach-sans" x="34" y="200" font-size="38" font-weight="800" letter-spacing="-0.5" fill="#FFFFFF">6h FEA Solves to Milliseconds</text>
    <text class="ach-sans" x="36" y="228" font-size="14" font-weight="400" fill="#CBD5E1">Benchmarked deep learning &amp; surrogate architectures predicting structural FRFs</text>
  </g></g>

  <!-- Card 2: Valeo (x=748, width=428, height=250) -->
  <g class="ach-in a2"><g transform="translate(748 24)">
    <g clip-path="url(#ach-clip-b)">
      <rect width="428" height="250" fill="#0F141F"/>
      <rect width="428" height="250" fill="url(#ach-glow-b)"/>
      <text class="ach-sans" x="410" y="115" text-anchor="end" font-size="80" font-weight="900" letter-spacing="-3" fill="url(#ach-outline)">VALEO</text>
      <rect x="-300" y="0" width="260" height="250" fill="url(#ach-sheen)" transform="skewX(-18)">
        <animate attributeName="x" values="-300;700;700" keyTimes="0;.35;1" dur="9s" begin="3.5s" repeatCount="indefinite"/>
      </rect>
    </g>
    <rect width="428" height="250" rx="16" fill="none" stroke="#2563EB" stroke-opacity=".35" stroke-width="1.2"/>

    <!-- Content strictly in lower half -->
    <text class="ach-mono" x="32" y="154" font-size="11.5" font-weight="700" letter-spacing="2.4" fill="#60A5FA">MASTER THESIS · VALEO EAUTOMOTIVE</text>
    <text class="ach-sans" x="30" y="200" font-size="38" font-weight="800" letter-spacing="-0.5" fill="#FFFFFF">E-Motor Stator NVH</text>
    <text class="ach-sans" x="32" y="228" font-size="14" font-weight="400" fill="#CBD5E1">Resonance isolation correlated with physical test benches</text>
  </g></g>

  <!-- Animated Hairline Divider across Score Strip -->
  <path class="ach-draw" d="M24 300 H1176" stroke="#2563EB" stroke-opacity=".35" stroke-width="1.2"/>

  <!-- Score Strip: 5 Spacious Pillars with Big Stats, Zero Clutter -->
  <g class="ach-in a3 ach-sans">
    <!-- Pillar 1: Solve Speedup -->
    <g transform="translate(36 300)">
      <circle cx="0" cy="0" r="3.5" fill="#60A5FA"/>
      <text class="ach-mono" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">SOLVE SPEEDUP</text>
      <text class="ach-sans" y="78" font-size="38" font-weight="800" fill="#FFFFFF">3,600×</text>
      <text class="ach-sans" y="102" font-size="13" font-weight="400" fill="#94A3B8">6h NASTRAN to ms</text>
    </g>
    <!-- Pillar 2: Skill Score -->
    <g transform="translate(266 300)">
      <circle cx="0" cy="0" r="3.5" fill="#60A5FA"/>
      <text class="ach-mono" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">SKILL SCORE</text>
      <text class="ach-sans" y="78" font-size="38" font-weight="800" fill="#FFFFFF">0.982</text>
      <text class="ach-sans" y="102" font-size="13" font-weight="400" fill="#94A3B8">FRF curve prediction</text>
    </g>
    <!-- Pillar 3: Bench Correlation -->
    <g transform="translate(496 300)">
      <circle cx="0" cy="0" r="3.5" fill="#60A5FA"/>
      <text class="ach-mono" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">BENCH ACCURACY</text>
      <text class="ach-sans" y="78" font-size="38" font-weight="800" fill="#FFFFFF">96.4%</text>
      <text class="ach-sans" y="102" font-size="13" font-weight="400" fill="#94A3B8">stator NVH correlation</text>
    </g>
    <!-- Pillar 4: Autonomous FEA -->
    <g transform="translate(726 300)">
      <circle cx="0" cy="0" r="3.5" fill="#60A5FA"/>
      <text class="ach-mono" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">AUTONOMOUS FEA</text>
      <text class="ach-sans" y="78" font-size="38" font-weight="800" fill="#FFFFFF">100%</text>
      <text class="ach-sans" y="102" font-size="13" font-weight="400" fill="#94A3B8">Claude MCP + Ansys</text>
    </g>
    <!-- Pillar 5: Education -->
    <g transform="translate(956 300)">
      <circle cx="0" cy="0" r="3.5" fill="#60A5FA"/>
      <text class="ach-mono" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">ACADEMIC DEGREE</text>
      <text class="ach-sans" y="78" font-size="38" font-weight="800" fill="#FFFFFF">M.Sc.</text>
      <text class="ach-sans" y="102" font-size="13" font-weight="400" fill="#94A3B8">FAU Computational Eng.</text>
    </g>
  </g>
</svg>"""
write_svg("achievement-motif.svg", achieve_svg)

# =============================================================
# 5. Project 1: Agentic FEA (viewBox 1200x370) - Wrapped Text
# =============================================================
project_1_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p1-t">
  <title id="p1-t">Agentic FEA: 3D Aerospace Bracket Modal Analysis via Claude MCP &amp; Ansys 2026 R1</title>
  <defs>
    <linearGradient id="p1-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0E131E"/><stop offset="1" stop-color="#06080D"/>
    </linearGradient>
    <radialGradient id="p1-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".55"/><stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p1-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#60A5FA" stroke-opacity=".06"/>
    </pattern>
    <filter id="p1-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p1-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p1-sans {{ font-family: {SANS}; }}
    .p1-mono {{ font-family: {MONO}; }}
    .p1-in {{ animation: p1-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .p1-d1 {{ animation-delay: .15s; }} .p1-d2 {{ animation-delay: .4s; }}
    .p1-chip {{ animation: p1-chip .7s cubic-bezier(.34,1.56,.64,1) both; }}
    .p1-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: p1-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes p1-in {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p1-chip {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p1-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p1-in, .p1-chip {{ animation: none; }} .p1-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g clip-path="url(#p1-clip)">
    <rect width="1200" height="370" fill="url(#p1-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p1-grid)"/>
    <rect width="1200" height="370" fill="url(#p1-glow)"/>

    <!-- Left Column (x=50 to 660, safe width 610px) -->
    <g class="p1-in p1-d1">
      <text class="p1-mono" x="50" y="56" font-size="11.5" font-weight="700" letter-spacing="2.4" fill="#60A5FA">01 · AGENTIC CAE · ANSYS 2026 R1 · MCP</text>
      <text class="p1-sans" x="48" y="98" font-size="34" font-weight="800" letter-spacing="-0.5" fill="#FFFFFF">Agentic FEA: Modal Analysis</text>
      <text class="p1-sans" x="50" y="130" font-size="14.5" font-weight="400" fill="#E2E8F0">Autonomous 3D aerospace bracket modal vibration analysis</text>
      <text class="p1-sans" x="50" y="150" font-size="13.5" font-weight="400" fill="#CBD5E1">orchestrated via Claude MCP &amp; PyMechanical on Ansys 2026 R1.</text>

      <text class="p1-mono" x="50" y="182" font-size="12" font-weight="600" fill="#93C5FD"><tspan fill="#60A5FA">BUILT ›</tspan> CAD import → solid meshing → contact pairs</text>
      <text class="p1-mono" x="50" y="200" font-size="12" font-weight="600" fill="#93C5FD">        → Block Lanczos eigenvalue solve → contour plots</text>

      <line class="p1-draw" x1="50" y1="222" x2="660" y2="222" stroke="#2563EB" stroke-opacity=".4" stroke-width="1.2"/>

      <!-- Metrics -->
      <g transform="translate(50 262)"><text class="p1-sans" font-size="28" font-weight="800" fill="#FFFFFF">6 Modes</text><text class="p1-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Eigenvalue extraction</text></g>
      <g transform="translate(240 262)"><text class="p1-sans" font-size="28" font-weight="800" fill="#FFFFFF">100%</text><text class="p1-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Autonomous simulation</text></g>
      <g transform="translate(440 262)"><text class="p1-sans" font-size="28" font-weight="800" fill="#FFFFFF">Zero-Click</text><text class="p1-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">CAD to contour plots</text></g>

      <!-- Chips (Safely fitted inside 610px width) -->
      <g class="p1-chip" style="animation-delay:1.00s"><rect x="50" y="312" width="126" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p1-mono" x="113" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Ansys 2026 R1</text></g>
      <g class="p1-chip" style="animation-delay:1.12s"><rect x="186" y="312" width="112" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p1-mono" x="242" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">PyMechanical</text></g>
      <g class="p1-chip" style="animation-delay:1.24s"><rect x="308" y="312" width="100" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p1-mono" x="358" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Claude MCP</text></g>
      <g class="p1-chip" style="animation-delay:1.36s"><rect x="418" y="312" width="112" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p1-mono" x="474" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Block Lanczos</text></g>
      <g class="p1-chip" style="animation-delay:1.48s"><rect x="540" y="312" width="76" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p1-mono" x="578" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Python</text></g>
    </g>

    <!-- Right Side 3D FEA Bracket Visual Artwork (x=760 to 1150) -->
    <g class="p1-in p1-d2" transform="translate(760 40)">
      <g stroke="#3B82F6" stroke-width="1.3" fill="none">
        <polygon points="50,220 180,270 330,210 200,160" fill="#0C1322" stroke="#1D4ED8" stroke-width="1.5"/>
        <polygon points="50,220 50,240 180,290 180,270" fill="#080D17" stroke="#1D4ED8"/>
        <polygon points="180,270 180,290 330,230 330,210" fill="#050810" stroke="#1D4ED8"/>

        <polygon points="120,185 180,205 180,85 120,65" fill="#101D36" stroke="#3B82F6"/>
        <polygon points="180,205 240,185 240,65 180,85" fill="#0B1424" stroke="#3B82F6"/>
        
        <polygon points="120,65 180,85 240,65 180,45" fill="#1D4ED8" stroke="#93C5FD" stroke-width="1.5"/>

        <line x1="50" y1="220" x2="200" y2="160" stroke="#3B82F6" stroke-opacity=".25"/>
        <line x1="180" y1="270" x2="330" y2="210" stroke="#3B82F6" stroke-opacity=".25"/>
        <line x1="120" y1="65" x2="180" y2="205" stroke="#3B82F6" stroke-opacity=".25"/>
        <line x1="240" y1="65" x2="180" y2="205" stroke="#3B82F6" stroke-opacity=".25"/>
        <line x1="150" y1="75" x2="150" y2="195" stroke="#3B82F6" stroke-opacity=".25"/>
        <line x1="210" y1="75" x2="210" y2="195" stroke="#3B82F6" stroke-opacity=".25"/>

        <path d="M180 85 C 210 85, 230 140, 200 205" stroke="#60A5FA" stroke-width="2.5" filter="url(#p1-glowf)">
          <animate attributeName="d" values="M180 85 C 210 85, 230 140, 200 205; M180 85 C 150 85, 130 140, 160 205; M180 85 C 210 85, 230 140, 200 205" dur="3s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
        </path>
      </g>

      <circle cx="95" cy="235" r="6" fill="#06080D" stroke="#EF4444" stroke-width="1.5"/>
      <circle cx="280" cy="225" r="6" fill="#06080D" stroke="#EF4444" stroke-width="1.5"/>
      <circle cx="180" cy="65" r="7" fill="#06080D" stroke="#10B981" stroke-width="1.8"/>

      <g transform="translate(245 28)" class="p1-mono">
        <rect width="135" height="26" rx="6" fill="#0B111C" stroke="#2563EB" stroke-opacity=".5"/>
        <circle cx="14" cy="13" r="3.5" fill="#60A5FA"/>
        <text x="26" y="17" font-size="11" font-weight="600" fill="#F8FAFC">f₁: 142.8 Hz</text>
      </g>
      <g transform="translate(255 64)" class="p1-mono">
        <rect width="135" height="26" rx="6" fill="#0B111C" stroke="#1D4ED8" stroke-opacity=".5"/>
        <circle cx="14" cy="13" r="3.5" fill="#3B82F6"/>
        <text x="26" y="17" font-size="11" font-weight="600" fill="#CBD5E1">f₂: 284.1 Hz</text>
      </g>
      <g transform="translate(245 100)" class="p1-mono">
        <rect width="135" height="26" rx="6" fill="#0B111C" stroke="#1E3A8A" stroke-opacity=".5"/>
        <circle cx="14" cy="13" r="3.5" fill="#1E3A8A"/>
        <text x="26" y="17" font-size="11" font-weight="600" fill="#CBD5E1">f₃: 412.5 Hz</text>
      </g>
    </g>
  </g>
</svg>"""
write_svg("project-modal-analysis.svg", project_1_svg)

# =============================================================
# 6. Project 2: SciML Surrogate (viewBox 1200x370) - Wrapped Text
# =============================================================
project_2_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p2-t">
  <title id="p2-t">Powertrain Structural FRF Surrogate: Machine Learning replacing NASTRAN</title>
  <defs>
    <linearGradient id="p2-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0E131E"/><stop offset="1" stop-color="#06080D"/>
    </linearGradient>
    <radialGradient id="p2-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".55"/><stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p2-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#60A5FA" stroke-opacity=".06"/>
    </pattern>
    <clipPath id="p2-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p2-sans {{ font-family: {SANS}; }}
    .p2-mono {{ font-family: {MONO}; }}
    .p2-in {{ animation: p2-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .p2-d1 {{ animation-delay: .15s; }} .p2-d2 {{ animation-delay: .4s; }}
    .p2-chip {{ animation: p2-chip .7s cubic-bezier(.34,1.56,.64,1) both; }}
    .p2-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: p2-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes p2-in {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p2-chip {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p2-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p2-in, .p2-chip {{ animation: none; }} .p2-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g clip-path="url(#p2-clip)">
    <rect width="1200" height="370" fill="url(#p2-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p2-grid)"/>
    <rect width="1200" height="370" fill="url(#p2-glow)"/>

    <!-- Left Column (x=50 to 660, safe width 610px) -->
    <g class="p2-in p2-d1">
      <text class="p2-mono" x="50" y="56" font-size="11.5" font-weight="700" letter-spacing="2.4" fill="#60A5FA">02 · SCIENTIFIC ML · MERCEDES-BENZ BENCHMARK</text>
      <text class="p2-sans" x="48" y="98" font-size="34" font-weight="800" letter-spacing="-0.5" fill="#FFFFFF">Structural FRF Surrogate</text>
      <text class="p2-sans" x="50" y="130" font-size="14.5" font-weight="400" fill="#E2E8F0">Deep learning &amp; surrogate architectures replacing computationally</text>
      <text class="p2-sans" x="50" y="150" font-size="13.5" font-weight="400" fill="#CBD5E1">heavy NASTRAN frequency response function (FRF) solves.</text>

      <text class="p2-mono" x="50" y="182" font-size="12" font-weight="600" fill="#93C5FD"><tspan fill="#60A5FA">BUILT ›</tspan> Trained HistGradientBoosting &amp; DIMGP models</text>
      <text class="p2-mono" x="50" y="200" font-size="12" font-weight="600" fill="#93C5FD">        on complex DOE structural frequency sweeps</text>

      <line class="p2-draw" x1="50" y1="222" x2="660" y2="222" stroke="#2563EB" stroke-opacity=".4" stroke-width="1.2"/>

      <!-- Metrics -->
      <g transform="translate(50 262)"><text class="p2-sans" font-size="28" font-weight="800" fill="#FFFFFF">6h → ms</text><text class="p2-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Inference speedup</text></g>
      <g transform="translate(240 262)"><text class="p2-sans" font-size="28" font-weight="800" fill="#FFFFFF">0.982</text><text class="p2-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Skill score on FRF peaks</text></g>
      <g transform="translate(440 262)"><text class="p2-sans" font-size="28" font-weight="800" fill="#FFFFFF">Full DOE</text><text class="p2-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Parametric sweeps</text></g>

      <!-- Chips -->
      <g class="p2-chip" style="animation-delay:1.00s"><rect x="50" y="312" width="90" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p2-mono" x="95" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">NASTRAN</text></g>
      <g class="p2-chip" style="animation-delay:1.12s"><rect x="150" y="312" width="80" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p2-mono" x="190" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">PyTorch</text></g>
      <g class="p2-chip" style="animation-delay:1.24s"><rect x="240" y="312" width="105" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p2-mono" x="292" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">scikit-learn</text></g>
      <g class="p2-chip" style="animation-delay:1.36s"><rect x="355" y="312" width="72" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p2-mono" x="391" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">DIMGP</text></g>
      <g class="p2-chip" style="animation-delay:1.48s"><rect x="437" y="312" width="105" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p2-mono" x="489" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">SLURM HPC</text></g>
    </g>

    <!-- Right Side Dynamic Bode FRF Curve Artwork -->
    <g class="p2-in p2-d2" transform="translate(760 40)">
      <rect width="390" height="280" rx="12" fill="#070A10" stroke="#1E293B" stroke-width="1.2"/>
      <line x1="40" y1="40" x2="350" y2="40" stroke="#1E293B" stroke-dasharray="3 3"/>
      <line x1="40" y1="100" x2="350" y2="100" stroke="#1E293B" stroke-dasharray="3 3"/>
      <line x1="40" y1="160" x2="350" y2="160" stroke="#1E293B" stroke-dasharray="3 3"/>
      <line x1="40" y1="220" x2="350" y2="220" stroke="#2563EB" stroke-opacity=".5"/>
      <line x1="40" y1="40" x2="40" y2="220" stroke="#2563EB" stroke-opacity=".5"/>

      <text class="p2-mono" x="40" y="242" font-size="10" font-weight="600" fill="#94A3B8">10 Hz</text>
      <text class="p2-mono" x="180" y="242" font-size="10" font-weight="600" fill="#94A3B8">100 Hz</text>
      <text class="p2-mono" x="320" y="242" font-size="10" font-weight="600" fill="#94A3B8">1 kHz</text>
      <text class="p2-mono" x="30" y="50" font-size="10" font-weight="600" text-anchor="end" fill="#94A3B8">dB</text>

      <path d="M50 200 C 90 195, 110 95, 130 95 C 150 95, 170 185, 200 185 C 230 185, 250 55, 270 55 C 290 55, 310 170, 340 160 L 340 180 C 310 190, 290 75, 270 75 C 250 75, 230 205, 200 205 C 170 205, 150 115, 130 115 C 110 115, 90 215, 50 220 Z" fill="#2563EB" fill-opacity=".15"/>

      <path d="M50 210 C 90 205, 110 105, 130 105 C 150 105, 170 195, 200 195 C 230 195, 250 65, 270 65 C 290 65, 310 180, 340 170" fill="none" stroke="#64748B" stroke-width="1.8" stroke-dasharray="4 3"/>

      <path d="M50 210 C 90 205, 110 105, 130 105 C 150 105, 170 195, 200 195 C 230 195, 250 65, 270 65 C 290 65, 310 180, 340 170" fill="none" stroke="#60A5FA" stroke-width="2.5">
        <animate attributeName="stroke-dasharray" values="400;0;400" dur="8s" repeatCount="indefinite"/>
      </path>

      <line x1="270" y1="35" x2="270" y2="220" stroke="#93C5FD" stroke-width="1" stroke-dasharray="2 2">
        <animate attributeName="x1" values="50;340;50" dur="6s" repeatCount="indefinite"/>
        <animate attributeName="x2" values="50;340;50" dur="6s" repeatCount="indefinite"/>
      </line>

      <g transform="translate(140 18)" class="p2-mono" font-size="10.5" font-weight="600">
        <line x1="0" y1="0" x2="20" y2="0" stroke="#64748B" stroke-dasharray="3 2" stroke-width="1.5"/>
        <text x="26" y="4" fill="#94A3B8">NASTRAN</text>
        <line x1="100" y1="0" x2="120" y2="0" stroke="#60A5FA" stroke-width="2.5"/>
        <text x="126" y="4" fill="#60A5FA">ML Surrogate</text>
      </g>
    </g>
  </g>
</svg>"""
write_svg("project-sciml-surrogate.svg", project_2_svg)

# =============================================================
# 7. Project 3: Acoustics & NVH (viewBox 1200x370) - Wrapped Text
# =============================================================
project_3_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p3-t">
  <title id="p3-t">Automated Simcenter 3D Vibroacoustics &amp; SPL Field Solver</title>
  <defs>
    <linearGradient id="p3-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0E131E"/><stop offset="1" stop-color="#06080D"/>
    </linearGradient>
    <radialGradient id="p3-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".55"/><stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p3-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#60A5FA" stroke-opacity=".06"/>
    </pattern>
    <clipPath id="p3-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p3-sans {{ font-family: {SANS}; }}
    .p3-mono {{ font-family: {MONO}; }}
    .p3-in {{ animation: p3-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .p3-d1 {{ animation-delay: .15s; }} .p3-d2 {{ animation-delay: .4s; }}
    .p3-chip {{ animation: p3-chip .7s cubic-bezier(.34,1.56,.64,1) both; }}
    .p3-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: p3-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes p3-in {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p3-chip {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p3-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p3-in, .p3-chip {{ animation: none; }} .p3-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g clip-path="url(#p3-clip)">
    <rect width="1200" height="370" fill="url(#p3-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p3-grid)"/>
    <rect width="1200" height="370" fill="url(#p3-glow)"/>

    <!-- Left Column (x=50 to 660, safe width 610px) -->
    <g class="p3-in p3-d1">
      <text class="p3-mono" x="50" y="56" font-size="11.5" font-weight="700" letter-spacing="2.4" fill="#60A5FA">03 · VIBROACOUSTICS · NX OPEN API AUTOMATION</text>
      <text class="p3-sans" x="48" y="98" font-size="34" font-weight="800" letter-spacing="-0.5" fill="#FFFFFF">Acoustic &amp; SPL Field Solver</text>
      <text class="p3-sans" x="50" y="130" font-size="14.5" font-weight="400" fill="#E2E8F0">Scripted acoustic environment simulation &amp; virtual microphone</text>
      <text class="p3-sans" x="50" y="150" font-size="13.5" font-weight="400" fill="#CBD5E1">array processing in Simcenter 3D with NX Open API.</text>

      <text class="p3-mono" x="50" y="182" font-size="12" font-weight="600" fill="#93C5FD"><tspan fill="#60A5FA">BUILT ›</tspan> Automated Simcenter 3D setups with NX Open API;</text>
      <text class="p3-mono" x="50" y="200" font-size="12" font-weight="600" fill="#93C5FD">        simulated airborne noise &amp; ultrasonic fields</text>

      <line class="p3-draw" x1="50" y1="222" x2="660" y2="222" stroke="#2563EB" stroke-opacity=".4" stroke-width="1.2"/>

      <!-- Metrics -->
      <g transform="translate(50 262)"><text class="p3-sans" font-size="28" font-weight="800" fill="#FFFFFF">120+ Mics</text><text class="p3-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Virtual spherical array</text></g>
      <g transform="translate(240 262)"><text class="p3-sans" font-size="28" font-weight="800" fill="#FFFFFF">85%</text><text class="p3-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Setup time reduction</text></g>
      <g transform="translate(440 262)"><text class="p3-sans" font-size="28" font-weight="800" fill="#FFFFFF">Full SPL</text><text class="p3-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Automated radiation maps</text></g>

      <!-- Chips -->
      <g class="p3-chip" style="animation-delay:1.00s"><rect x="50" y="312" width="118" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p3-mono" x="109" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Simcenter 3D</text></g>
      <g class="p3-chip" style="animation-delay:1.12s"><rect x="178" y="312" width="76" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p3-mono" x="216" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Python</text></g>
      <g class="p3-chip" style="animation-delay:1.24s"><rect x="264" y="312" width="116" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p3-mono" x="322" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">NX Open API</text></g>
      <g class="p3-chip" style="animation-delay:1.36s"><rect x="390" y="312" width="112" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p3-mono" x="446" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Acoustic BEM</text></g>
      <g class="p3-chip" style="animation-delay:1.48s"><rect x="512" y="312" width="116" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p3-mono" x="570" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Sound Power</text></g>
    </g>

    <!-- Right Side Acoustic Wavefront Radiation Visual -->
    <g class="p3-in p3-d2" transform="translate(760 40)">
      <rect width="390" height="280" rx="12" fill="#070A10" stroke="#1E293B" stroke-width="1.2"/>

      <g transform="translate(195 140)">
        <circle r="14" fill="#1D4ED8" stroke="#60A5FA" stroke-width="2"/>
        <circle r="4" fill="#F8FAFC"/>

        <circle r="35" fill="none" stroke="#60A5FA" stroke-width="1.8" stroke-opacity=".85">
          <animate attributeName="r" values="20;125" dur="3.5s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="3.5s" repeatCount="indefinite"/>
        </circle>
        <circle r="60" fill="none" stroke="#3B82F6" stroke-width="1.5" stroke-opacity=".65">
          <animate attributeName="r" values="20;125" dur="3.5s" begin="1.2s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="3.5s" begin="1.2s" repeatCount="indefinite"/>
        </circle>
        <circle r="85" fill="none" stroke="#1E3A8A" stroke-width="1.2" stroke-opacity=".45">
          <animate attributeName="r" values="20;125" dur="3.5s" begin="2.4s" repeatCount="indefinite"/>
          <animate attributeName="opacity" values="1;0" dur="3.5s" begin="2.4s" repeatCount="indefinite"/>
        </circle>

        <g stroke="#3B82F6" stroke-width="1" stroke-dasharray="2 3" fill="none">
          <circle r="105"/>
        </g>
        <g fill="#93C5FD">
          <circle cx="105" cy="0" r="3.5"/><circle cx="-105" cy="0" r="3.5"/>
          <circle cx="0" cy="105" r="3.5"/><circle cx="0" cy="-105" r="3.5"/>
          <circle cx="74" cy="74" r="3.5"/><circle cx="-74" cy="74" r="3.5"/>
          <circle cx="74" cy="-74" r="3.5"/><circle cx="-74" cy="-74" r="3.5"/>
        </g>
      </g>

      <g transform="translate(24 240)" class="p3-mono" font-size="10.5" font-weight="600">
        <text fill="#60A5FA">SPL Radiation Field: 84 dB(A)</text>
      </g>
    </g>
  </g>
</svg>"""
write_svg("project-simcenter-acoustics.svg", project_3_svg)

# =============================================================
# 8. Project 4: Interactive 3D Portfolio (viewBox 1200x370) - Wrapped Text
# =============================================================
project_4_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p4-t">
  <title id="p4-t">Interactive 3D Portfolio: Modern WebGL developer experience</title>
  <defs>
    <linearGradient id="p4-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0E131E"/><stop offset="1" stop-color="#06080D"/>
    </linearGradient>
    <radialGradient id="p4-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".55"/><stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p4-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#60A5FA" stroke-opacity=".06"/>
    </pattern>
    <clipPath id="p4-clip"><rect width="1200" height="370" rx="18"/></clipPath>
  </defs>
  <style>
    .p4-sans {{ font-family: {SANS}; }}
    .p4-mono {{ font-family: {MONO}; }}
    .p4-in {{ animation: p4-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .p4-d1 {{ animation-delay: .15s; }} .p4-d2 {{ animation-delay: .4s; }}
    .p4-chip {{ animation: p4-chip .7s cubic-bezier(.34,1.56,.64,1) both; }}
    .p4-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: p4-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes p4-in {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p4-chip {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p4-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p4-in, .p4-chip {{ animation: none; }} .p4-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g clip-path="url(#p4-clip)">
    <rect width="1200" height="370" fill="url(#p4-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p4-grid)"/>
    <rect width="1200" height="370" fill="url(#p4-glow)"/>

    <!-- Left Column (x=50 to 660, safe width 610px) -->
    <g class="p4-in p4-d1">
      <text class="p4-mono" x="50" y="56" font-size="11.5" font-weight="700" letter-spacing="2.4" fill="#60A5FA">04 · WEBGL · INTERACTIVE 3D · THREE.JS</text>
      <text class="p4-sans" x="48" y="98" font-size="34" font-weight="800" letter-spacing="-0.5" fill="#FFFFFF">Interactive 3D Portfolio</text>
      <text class="p4-sans" x="50" y="130" font-size="14.5" font-weight="400" fill="#E2E8F0">Physics-inspired developer portfolio with real-time 3D rendering,</text>
      <text class="p4-sans" x="50" y="150" font-size="13.5" font-weight="400" fill="#CBD5E1">interactive simulation scenes, and responsive GSAP animations.</text>

      <text class="p4-mono" x="50" y="182" font-size="12" font-weight="600" fill="#93C5FD"><tspan fill="#60A5FA">BUILT ›</tspan> Modern WebGL engineering visualizations,</text>
      <text class="p4-mono" x="50" y="200" font-size="12" font-weight="600" fill="#93C5FD">        Three.js shaders &amp; responsive React performance</text>

      <line class="p4-draw" x1="50" y1="222" x2="660" y2="222" stroke="#2563EB" stroke-opacity=".4" stroke-width="1.2"/>

      <!-- Metrics -->
      <g transform="translate(50 262)"><text class="p4-sans" font-size="28" font-weight="800" fill="#FFFFFF">60 FPS</text><text class="p4-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">WebGL rendering</text></g>
      <g transform="translate(240 262)"><text class="p4-sans" font-size="28" font-weight="800" fill="#FFFFFF">Three.js</text><text class="p4-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Custom shader scenes</text></g>
      <g transform="translate(440 262)"><text class="p4-sans" font-size="28" font-weight="800" fill="#FFFFFF">Global</text><text class="p4-sans" y="22" font-size="12" font-weight="500" fill="#94A3B8">Netlify deployment</text></g>

      <!-- Chips -->
      <g class="p4-chip" style="animation-delay:1.00s"><rect x="50" y="312" width="70" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p4-mono" x="85" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">React</text></g>
      <g class="p4-chip" style="animation-delay:1.12s"><rect x="130" y="312" width="102" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p4-mono" x="181" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">TypeScript</text></g>
      <g class="p4-chip" style="animation-delay:1.24s"><rect x="242" y="312" width="86" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p4-mono" x="285" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Three.js</text></g>
      <g class="p4-chip" style="animation-delay:1.36s"><rect x="338" y="312" width="66" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p4-mono" x="371" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">GSAP</text></g>
      <g class="p4-chip" style="animation-delay:1.48s"><rect x="414" y="312" width="112" height="26" rx="13" fill="#111726" stroke="#2563EB" stroke-opacity=".5"/><text class="p4-mono" x="470" y="329" text-anchor="middle" font-size="11.5" font-weight="600" fill="#93C5FD">Tailwind CSS</text></g>
    </g>

    <!-- Right Side 3D Geometry Rendering Artwork -->
    <g class="p4-in p4-d2" transform="translate(760 40)">
      <rect width="390" height="280" rx="12" fill="#070A10" stroke="#1E293B" stroke-width="1.2"/>

      <g transform="translate(195 140)">
        <circle r="95" fill="none" stroke="#2563EB" stroke-opacity=".2" stroke-dasharray="4 6">
          <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="40s" repeatCount="indefinite"/>
        </circle>
        <ellipse rx="85" ry="35" fill="none" stroke="#60A5FA" stroke-opacity=".6" stroke-width="1.4">
          <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="25s" repeatCount="indefinite"/>
        </ellipse>
        <ellipse rx="85" ry="35" fill="none" stroke="#1D4ED8" stroke-opacity=".4" stroke-width="1.2" transform="rotate(60)"/>

        <g stroke="#93C5FD" stroke-width="1.6" fill="#0E1628" fill-opacity=".65">
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

# =============================================================
# 9. Tech Constellation (viewBox 1200x500) - Zero Overlaps, Clean Hierarchy
# =============================================================
tech_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="1200" height="500" role="img" aria-labelledby="tc-title tc-desc">
  <title id="tc-title">Computational Stack &amp; Tooling</title>
  <desc id="tc-desc">CAE &amp; FEA Solvers: Ansys Mechanical, NASTRAN, Simcenter 3D, HyperMesh. Scientific ML: PyTorch, scikit-learn, PINNs, DIMGP. Vibroacoustics: Modal, Harmonic, FFT, SPL. Agentic &amp; Automation: Claude MCP, PyMechanical, NX Open API. Languages: Python, C++, TypeScript.</desc>
  <defs>
    <linearGradient id="tc-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0E131E"/><stop offset="1" stop-color="#06080D"/>
    </linearGradient>
    <radialGradient id="tc-glow" cx="50%" cy="50%" r="60%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".35"/><stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="tc-pulse">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".5" stop-color="#60A5FA" stop-opacity=".7"/>
      <stop offset="1" stop-color="#1D4ED8" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .tc-sans {{ font-family: {SANS}; }}
    .tc-mono {{ font-family: {MONO}; }}
    .tc-panel {{ animation: tc-in 1.1s cubic-bezier(.16,1,.3,1) both; }}
    .tc-p1 {{ animation-delay: .05s; }} .tc-p2 {{ animation-delay: .2s; }} .tc-p3 {{ animation-delay: .35s; }}
    .tc-p4 {{ animation-delay: .5s; }} .tc-p5 {{ animation-delay: .65s; }} .tc-p6 {{ animation-delay: .8s; }}
    .tc-web {{ stroke-dasharray: 1800; stroke-dashoffset: 1800; animation: tc-draw 3s cubic-bezier(.65,0,.35,1) 1s forwards; }}
    @keyframes tc-in {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes tc-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .tc-panel {{ animation: none; }}
      .tc-web {{ animation: none; stroke-dashoffset: 0; }}
    }}
  </style>

  <rect width="1200" height="500" rx="20" fill="url(#tc-bg)"/>
  <rect width="1200" height="500" rx="20" fill="url(#tc-glow)"/>
  <rect x=".5" y=".5" width="1199" height="499" rx="19.5" fill="none" stroke="#3B82F6" stroke-opacity=".2"/>

  <!-- Constellation: Gutters Linking Six Groups -->
  <path class="tc-web" d="M24 250 H1176 M406 24 V476 M794 24 V476" fill="none" stroke="#2563EB" stroke-opacity=".25"/>
  <circle cx="0" cy="250" r="7" fill="url(#tc-pulse)" opacity="0">
    <animate attributeName="cx" values="24;1176" dur="9s" begin="3s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.9;1" dur="9s" begin="3s" repeatCount="indefinite"/>
  </circle>
  <g fill="#070A10" stroke="#3B82F6">
    <rect x="400" y="244" width="12" height="12" transform="rotate(45 406 250)"/>
    <rect x="788" y="244" width="12" height="12" transform="rotate(45 794 250)"/>
  </g>

  <!-- Panel 1: CAE & FEA Solvers (width 360, safe text width 310) -->
  <g class="tc-panel tc-p1"><g transform="translate(30 30)">
    <rect width="360" height="200" rx="14" fill="#0F141F" fill-opacity=".85" stroke="#2563EB" stroke-opacity=".25"/>
    <text class="tc-mono" x="22" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">01  CAE &amp; FEA SOLVERS</text>
    <text class="tc-sans" x="22" y="74" font-size="22" font-weight="800" fill="#FFFFFF">Ansys Mechanical</text>
    <text class="tc-sans" x="22" y="112" font-size="17" font-weight="600" fill="#E2E8F0">NASTRAN · Simcenter 3D</text>
    <text class="tc-sans" x="22" y="144" font-size="13.5" font-weight="400" fill="#94A3B8">HyperMesh · Abaqus · OpenCFS</text>
    <g transform="translate(22 162)">
      <rect width="170" height="22" rx="11" fill="#111726" stroke="#2563EB" stroke-opacity=".4"/>
      <text class="tc-mono" x="85" y="15" text-anchor="middle" font-size="10.5" font-weight="600" fill="#93C5FD">APDL · PyMechanical API</text>
    </g>
  </g></g>

  <!-- Panel 2: Scientific ML & Surrogates -->
  <g class="tc-panel tc-p2"><g transform="translate(420 30)">
    <rect width="360" height="200" rx="14" fill="#0F141F" fill-opacity=".85" stroke="#2563EB" stroke-opacity=".25"/>
    <text class="tc-mono" x="22" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">02  SCIENTIFIC ML</text>
    <text class="tc-sans" x="22" y="74" font-size="22" font-weight="800" fill="#FFFFFF">PyTorch · scikit-learn</text>
    <text class="tc-sans" x="22" y="112" font-size="17" font-weight="600" fill="#E2E8F0">FRF Surrogates · PINNs</text>
    <text class="tc-sans" x="22" y="144" font-size="13.5" font-weight="400" fill="#94A3B8">DIMGP · Neural Operators</text>
    <g transform="translate(22 162)">
      <rect width="180" height="22" rx="11" fill="#111726" stroke="#2563EB" stroke-opacity=".4"/>
      <text class="tc-mono" x="90" y="15" text-anchor="middle" font-size="10.5" font-weight="600" fill="#93C5FD">Surrogate Modeling · DOE</text>
    </g>
  </g></g>

  <!-- Panel 3: Vibroacoustics & NVH -->
  <g class="tc-panel tc-p3"><g transform="translate(810 30)">
    <rect width="360" height="200" rx="14" fill="#0F141F" fill-opacity=".85" stroke="#2563EB" stroke-opacity=".25"/>
    <text class="tc-mono" x="22" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">03  VIBROACOUSTICS &amp; NVH</text>
    <text class="tc-sans" x="22" y="74" font-size="22" font-weight="800" fill="#FFFFFF">Modal &amp; Harmonic</text>
    <text class="tc-sans" x="22" y="112" font-size="17" font-weight="600" fill="#E2E8F0">FFT &amp; Order Tracking</text>
    <text class="tc-sans" x="22" y="144" font-size="13.5" font-weight="400" fill="#94A3B8">SPL Acoustic Fields · Maxwell</text>
    <g transform="translate(22 162)">
      <rect width="180" height="22" rx="11" fill="#111726" stroke="#2563EB" stroke-opacity=".4"/>
      <text class="tc-mono" x="90" y="15" text-anchor="middle" font-size="10.5" font-weight="600" fill="#93C5FD">Stator Resonance Isolation</text>
    </g>
  </g></g>

  <!-- Panel 4: Agentic & Automation -->
  <g class="tc-panel tc-p4"><g transform="translate(30 270)">
    <rect width="360" height="200" rx="14" fill="#0F141F" fill-opacity=".85" stroke="#2563EB" stroke-opacity=".25"/>
    <text class="tc-mono" x="22" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">04  AGENTIC &amp; SIMULATION AI</text>
    <text class="tc-sans" x="22" y="74" font-size="22" font-weight="800" fill="#FFFFFF">Claude MCP Protocol</text>
    <text class="tc-sans" x="22" y="112" font-size="17" font-weight="600" fill="#E2E8F0">PyMechanical · NX Open</text>
    <text class="tc-sans" x="22" y="144" font-size="13.5" font-weight="400" fill="#94A3B8">SLURM HPC · Linux Bash · Git</text>
    <g transform="translate(22 162)">
      <rect width="170" height="22" rx="11" fill="#111726" stroke="#2563EB" stroke-opacity=".4"/>
      <text class="tc-mono" x="85" y="15" text-anchor="middle" font-size="10.5" font-weight="600" fill="#93C5FD">Autonomous FEA Pipeline</text>
    </g>
  </g></g>

  <!-- Panel 5: Software & Computation -->
  <g class="tc-panel tc-p5"><g transform="translate(420 270)">
    <rect width="360" height="200" rx="14" fill="#0F141F" fill-opacity=".85" stroke="#2563EB" stroke-opacity=".25"/>
    <text class="tc-mono" x="22" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">05  PROGRAMMING &amp; WEB</text>
    <text class="tc-sans" x="22" y="74" font-size="22" font-weight="800" fill="#FFFFFF">Python &amp; C++</text>
    <text class="tc-sans" x="22" y="112" font-size="17" font-weight="600" fill="#E2E8F0">TypeScript · React</text>
    <text class="tc-sans" x="22" y="144" font-size="13.5" font-weight="400" fill="#94A3B8">Three.js · Docker · FastAPI</text>
    <g transform="translate(22 162)">
      <rect width="160" height="22" rx="11" fill="#111726" stroke="#2563EB" stroke-opacity=".4"/>
      <text class="tc-mono" x="80" y="15" text-anchor="middle" font-size="10.5" font-weight="600" fill="#93C5FD">Scientific Computing</text>
    </g>
  </g></g>

  <!-- Panel 6: Affiliations & Credentials -->
  <g class="tc-panel tc-p6"><g transform="translate(810 270)">
    <rect width="360" height="200" rx="14" fill="#0F141F" fill-opacity=".85" stroke="#2563EB" stroke-opacity=".25"/>
    <text class="tc-mono" x="22" y="34" font-size="11" font-weight="700" letter-spacing="2" fill="#60A5FA">06  AFFILIATIONS &amp; CREDS</text>
    <text class="tc-sans" x="22" y="74" font-size="22" font-weight="800" fill="#FFFFFF">FAU Erlangen-Nürnberg</text>
    <text class="tc-sans" x="22" y="112" font-size="17" font-weight="600" fill="#E2E8F0">Mercedes-Benz · Valeo</text>
    <text class="tc-sans" x="22" y="144" font-size="13.5" font-weight="400" fill="#94A3B8">English C2 · German B2 · Class B</text>
    <g transform="translate(22 162)">
      <rect width="150" height="22" rx="11" fill="#111726" stroke="#2563EB" stroke-opacity=".4"/>
      <text class="tc-mono" x="75" y="15" text-anchor="middle" font-size="10.5" font-weight="600" fill="#93C5FD">M.Sc. Computational Eng</text>
    </g>
  </g></g>
</svg>"""
write_svg("tech-constellation.svg", tech_svg)

# =============================================================
# 10. Footer Signature (viewBox 1200x230) - Centered & Balanced
# =============================================================
footer_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 230" width="1200" height="230" role="img" aria-labelledby="sig-title">
  <title id="sig-title">Vamshidhar Reddy — Engineering physics with computational rigor.</title>
  <defs>
    <linearGradient id="sig-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#06080D"/>
      <stop offset="1" stop-color="#0E131E"/>
    </linearGradient>
    <radialGradient id="sig-glow" cx="50%" cy="100%" r="70%">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity=".45"/>
      <stop offset="1" stop-color="#1E3A8A" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sig-line" gradientUnits="userSpaceOnUse" x1="150" y1="0" x2="1050" y2="0">
      <stop offset="0" stop-color="#1D4ED8" stop-opacity="0"/>
      <stop offset=".5" stop-color="#60A5FA"/>
      <stop offset="1" stop-color="#1D4ED8" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .sig-sans {{ font-family: {SANS}; }}
    .sig-mono {{ font-family: {MONO}; }}
    .sig-rule {{ stroke-dasharray: 900; stroke-dashoffset: 900; animation: sig-draw 2.4s cubic-bezier(.65,0,.35,1) .6s forwards; }}
    .sig-in {{ animation: sig-in 1.4s ease 1.2s both; }}
    @keyframes sig-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes sig-in {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: none; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .sig-rule {{ animation: none; stroke-dashoffset: 0; }}
      .sig-in {{ animation: none; }}
      .sig-sparks {{ display: none; }}
    }}
  </style>

  <rect width="1200" height="230" rx="20" fill="url(#sig-bg)"/>
  <rect width="1200" height="230" rx="20" fill="url(#sig-glow)"/>

  <!-- Subtle Ascending Sparks -->
  <g class="sig-sparks" fill="#93C5FD" opacity=".8">
    <circle cx="451" cy="230" r="1.0"><animate attributeName="cy" values="232;108" dur="7.3s" begin="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="7.3s" begin="2.4s" repeatCount="indefinite"/></circle>
    <circle cx="216" cy="230" r="1.4"><animate attributeName="cy" values="232;44" dur="5.3s" begin="0.3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="5.3s" begin="0.3s" repeatCount="indefinite"/></circle>
    <circle cx="716" cy="230" r="1.3"><animate attributeName="cy" values="232;68" dur="7.3s" begin="3.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="7.3s" begin="3.5s" repeatCount="indefinite"/></circle>
    <circle cx="915" cy="230" r="1.4"><animate attributeName="cy" values="232;78" dur="5.1s" begin="3.5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.85;0" dur="5.1s" begin="3.5s" repeatCount="indefinite"/></circle>
  </g>

  <!-- Modern Bold Title -->
  <text class="sig-sans sig-in" x="600" y="88" text-anchor="middle" font-size="36" font-weight="900" letter-spacing="3" fill="#FFFFFF">VAMSHIDHAR REDDY</text>

  <path class="sig-rule" d="M150 120 H1050" stroke="url(#sig-line)" stroke-width="1.4"/>
  <circle cx="600" cy="120" r="3.5" fill="#F8FAFC" class="sig-in">
    <animate attributeName="r" values="3.5;5.5;3.5" dur="3.2s" repeatCount="indefinite"/>
  </circle>

  <g class="sig-in">
    <text class="sig-sans" x="600" y="160" text-anchor="middle" font-size="18" font-weight="500" fill="#E2E8F0">Engineering physics with computational rigor.</text>
    <text class="sig-mono" x="600" y="192" text-anchor="middle" font-size="11" font-weight="600" letter-spacing="2" fill="#94A3B8">CAE &amp; STRUCTURAL DYNAMICS · SCIENTIFIC MACHINE LEARNING · AGENTIC SIMULATION</text>
  </g>
</svg>"""
write_svg("footer-signature.svg", footer_svg)

print("All meticulously refined, zero-overlap, high-readability SVGs generated successfully!")
