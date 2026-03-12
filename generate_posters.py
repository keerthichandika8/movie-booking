#!/usr/bin/env python3
"""Generate movie poster SVGs for Magic Movies"""

import os

OUT = os.path.join(os.path.dirname(__file__), "static", "images")
os.makedirs(OUT, exist_ok=True)

POSTERS = {
    "rrr": {
        "title": "RRR",
        "subtitle": "ROUDRAM RANAM RUDHIRAM",
        "year": "2022",
        "rating": "8.8",
        "bg1": "#1a0800", "bg2": "#5c1500", "bg3": "#ff4500",
        "accent": "#ff6b00",
        "art": """
        <!-- Fire background -->
        <defs>
          <radialGradient id="fire1" cx="50%" cy="100%" r="80%">
            <stop offset="0%" stop-color="#ff4500" stop-opacity="0.9"/>
            <stop offset="40%" stop-color="#cc2200" stop-opacity="0.7"/>
            <stop offset="100%" stop-color="#1a0800" stop-opacity="0"/>
          </radialGradient>
          <radialGradient id="glow1" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#ff8c00" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#1a0800" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#1a0800"/>
        <rect width="300" height="450" fill="url(#glow1)"/>
        <!-- Flame shapes -->
        <ellipse cx="150" cy="440" rx="180" ry="120" fill="#cc2200" opacity="0.6"/>
        <ellipse cx="150" cy="420" rx="140" ry="100" fill="#ff4500" opacity="0.5"/>
        <ellipse cx="150" cy="400" rx="100" ry="80" fill="#ff6b00" opacity="0.4"/>
        <!-- Water drop top -->
        <ellipse cx="150" cy="60" rx="80" ry="40" fill="#003366" opacity="0.5"/>
        <!-- Two figures silhouette -->
        <g opacity="0.9">
          <!-- Figure 1 (left) with weapon -->
          <ellipse cx="108" cy="200" rx="18" ry="22" fill="#0a1628"/>
          <rect x="98" y="220" width="22" height="80" rx="5" fill="#0a1628"/>
          <rect x="90" y="230" width="50" height="8" rx="3" fill="#cc2200"/>
          <rect x="105" y="300" width="8" height="50" rx="3" fill="#0a1628"/>
          <rect x="118" y="305" width="8" height="45" rx="3" fill="#0a1628"/>
          <!-- Weapon -->
          <line x1="140" y1="210" x2="100" y2="260" stroke="#ff8c00" stroke-width="3"/>
          <polygon points="140,210 145,218 136,215" fill="#ffd700"/>
        </g>
        <g opacity="0.9">
          <!-- Figure 2 (right) with bike chain -->
          <ellipse cx="192" cy="195" rx="18" ry="22" fill="#2d0a00"/>
          <rect x="182" y="215" width="22" height="85" rx="5" fill="#2d0a00"/>
          <rect x="175" y="225" width="52" height="8" rx="3" fill="#ff4500"/>
          <rect x="185" y="300" width="8" height="50" rx="3" fill="#2d0a00"/>
          <rect x="198" y="305" width="8" height="45" rx="3" fill="#2d0a00"/>
          <!-- Chain -->
          <path d="M192 230 Q220 245 215 280" stroke="#888" stroke-width="4" fill="none"/>
          <circle cx="218" cy="283" r="8" fill="#666" stroke="#888" stroke-width="2"/>
        </g>
        <!-- Water line -->
        <path d="M0 350 Q75 330 150 350 Q225 370 300 350 L300 450 L0 450 Z" fill="#003366" opacity="0.3"/>
        <!-- Fire on water -->
        <rect width="300" height="200" y="250" fill="url(#fire1)"/>
        <!-- Sparks -->
        <circle cx="80" cy="160" r="3" fill="#ffd700" opacity="0.8"/>
        <circle cx="220" cy="140" r="2" fill="#ffd700" opacity="0.6"/>
        <circle cx="50" cy="200" r="2" fill="#ff8c00" opacity="0.7"/>
        <circle cx="260" cy="180" r="3" fill="#ff6b00" opacity="0.5"/>
        <circle cx="140" cy="100" r="2" fill="#ffd700" opacity="0.9"/>
        """
    },
    "kgf2": {
        "title": "KGF",
        "subtitle": "CHAPTER 2",
        "year": "2022",
        "rating": "8.2",
        "bg1": "#0d0800", "bg2": "#3d2800", "bg3": "#c8860a",
        "accent": "#ffd700",
        "art": """
        <defs>
          <radialGradient id="goldGlow" cx="50%" cy="40%" r="60%">
            <stop offset="0%" stop-color="#c8860a" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#0d0800" stop-opacity="0"/>
          </radialGradient>
          <linearGradient id="goldBar" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#ffd700"/>
            <stop offset="50%" stop-color="#c8860a"/>
            <stop offset="100%" stop-color="#8b6914"/>
          </linearGradient>
        </defs>
        <rect width="300" height="450" fill="#0d0800"/>
        <rect width="300" height="450" fill="url(#goldGlow)"/>
        <!-- Gold bars background -->
        <rect x="20" y="260" width="50" height="30" rx="3" fill="url(#goldBar)" opacity="0.4"/>
        <rect x="80" y="275" width="50" height="30" rx="3" fill="url(#goldBar)" opacity="0.3"/>
        <rect x="170" y="265" width="50" height="30" rx="3" fill="url(#goldBar)" opacity="0.4"/>
        <rect x="230" y="278" width="50" height="30" rx="3" fill="url(#goldBar)" opacity="0.3"/>
        <!-- Rocky silhouette - iconic pose -->
        <ellipse cx="150" cy="155" rx="28" ry="32" fill="#1a1000"/>
        <!-- Hair detail -->
        <path d="M122 148 Q130 118 150 120 Q170 118 178 148" fill="#2a1800"/>
        <!-- Body -->
        <rect x="122" y="185" width="56" height="95" rx="8" fill="#1a1000"/>
        <!-- Arms spread wide -->
        <rect x="50" y="190" width="75" height="18" rx="8" fill="#1a1000"/>
        <rect x="175" y="190" width="75" height="18" rx="8" fill="#1a1000"/>
        <!-- Hands -->
        <ellipse cx="50" cy="199" rx="14" ry="11" fill="#1a1000"/>
        <ellipse cx="250" cy="199" rx="14" ry="11" fill="#1a1000"/>
        <!-- Legs -->
        <rect x="130" y="278" width="18" height="70" rx="5" fill="#1a1000"/>
        <rect x="152" y="278" width="18" height="70" rx="5" fill="#1a1000"/>
        <!-- Gold chains on body -->
        <path d="M130 200 Q150 215 170 200" stroke="#ffd700" stroke-width="2.5" fill="none"/>
        <path d="M130 210 Q150 228 170 210" stroke="#c8860a" stroke-width="2" fill="none"/>
        <!-- Eyes glow -->
        <ellipse cx="142" cy="158" rx="5" ry="4" fill="#c8860a" opacity="0.9"/>
        <ellipse cx="158" cy="158" rx="5" ry="4" fill="#c8860a" opacity="0.9"/>
        <!-- Ground gold dust -->
        <ellipse cx="150" cy="440" rx="200" ry="30" fill="#c8860a" opacity="0.2"/>
        <!-- Flying gold particles -->
        <circle cx="60" cy="120" r="3" fill="#ffd700" opacity="0.8"/>
        <circle cx="240" cy="100" r="4" fill="#ffd700" opacity="0.6"/>
        <circle cx="45" cy="200" r="2" fill="#ffd700" opacity="0.5"/>
        <circle cx="260" cy="250" r="3" fill="#c8860a" opacity="0.7"/>
        <circle cx="100" cy="80" r="2" fill="#ffd700" opacity="0.9"/>
        <circle cx="200" cy="70" r="3" fill="#ffd700" opacity="0.7"/>
        <!-- Axe/weapon glint -->
        <line x1="60" y1="199" x2="30" y2="170" stroke="#ffd700" stroke-width="4"/>
        <polygon points="30,170 38,178 22,178" fill="#ffd700"/>
        """
    },
    "pushpa2": {
        "title": "PUSHPA",
        "subtitle": "THE RULE — PART 2",
        "year": "2024",
        "rating": "8.0",
        "bg1": "#0a1200", "bg2": "#1a3300", "bg3": "#2d6e00",
        "accent": "#7bc600",
        "art": """
        <defs>
          <radialGradient id="forestGlow" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#2d6e00" stop-opacity="0.5"/>
            <stop offset="100%" stop-color="#0a1200" stop-opacity="0"/>
          </radialGradient>
          <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#4a9900"/>
            <stop offset="100%" stop-color="#1a4400"/>
          </linearGradient>
        </defs>
        <rect width="300" height="450" fill="#0a1200"/>
        <rect width="300" height="450" fill="url(#forestGlow)"/>
        <!-- Red sandalwood trees background -->
        <rect x="20" y="150" width="12" height="200" rx="4" fill="#3a1800" opacity="0.6"/>
        <rect x="55" y="120" width="14" height="230" rx="4" fill="#3a1800" opacity="0.5"/>
        <rect x="235" y="140" width="12" height="220" rx="4" fill="#3a1800" opacity="0.6"/>
        <rect x="270" y="110" width="14" height="250" rx="4" fill="#3a1800" opacity="0.5"/>
        <!-- Leaf canopy -->
        <ellipse cx="26" cy="140" rx="30" ry="22" fill="url(#leafGrad)" opacity="0.6"/>
        <ellipse cx="62" cy="110" rx="35" ry="25" fill="url(#leafGrad)" opacity="0.5"/>
        <ellipse cx="241" cy="130" rx="32" ry="22" fill="url(#leafGrad)" opacity="0.6"/>
        <ellipse cx="277" cy="100" rx="36" ry="26" fill="url(#leafGrad)" opacity="0.5"/>
        <!-- Pushpa - leaning iconic pose -->
        <ellipse cx="150" cy="160" rx="25" ry="30" fill="#2d1500"/>
        <!-- Lungi/dhoti -->
        <path d="M125 240 Q130 270 145 290 L155 290 Q170 270 175 240 Z" fill="#8b0000"/>
        <!-- Shirt open -->
        <path d="M125 190 L130 240 Q150 250 170 240 L175 190 Z" fill="#1a0000"/>
        <!-- Arms - relaxed confident -->
        <rect x="75" y="195" width="55" height="16" rx="7" fill="#2d1500"/>
        <rect x="170" y="195" width="55" height="16" rx="7" fill="#2d1500"/>
        <ellipse cx="75" cy="203" rx="13" ry="10" fill="#2d1500"/>
        <ellipse cx="225" cy="203" rx="13" ry="10" fill="#2d1500"/>
        <!-- Legs -->
        <rect x="133" y="288" width="15" height="65" rx="5" fill="#2d1500"/>
        <rect x="152" y="288" width="15" height="65" rx="5" fill="#2d1500"/>
        <!-- Red flower tucked in hair -->
        <circle cx="165" cy="138" r="8" fill="#cc0000"/>
        <circle cx="167" cy="136" r="4" fill="#ff3333"/>
        <!-- Attitude tilt - chin slightly raised -->
        <ellipse cx="150" cy="158" rx="5" ry="4" fill="#1a0a00" opacity="0.8"/>
        <!-- Forest floor -->
        <ellipse cx="150" cy="445" rx="200" ry="20" fill="#1a3300" opacity="0.4"/>
        <!-- Red sandalwood logs -->
        <rect x="50" y="390" width="60" height="16" rx="5" fill="#8b2500" opacity="0.7"/>
        <rect x="190" y="395" width="55" height="14" rx="5" fill="#8b2500" opacity="0.6"/>
        <!-- Firefly particles -->
        <circle cx="90" cy="180" r="2.5" fill="#ccff00" opacity="0.7"/>
        <circle cx="210" cy="160" r="2" fill="#ccff00" opacity="0.5"/>
        <circle cx="70" cy="290" r="2" fill="#7bc600" opacity="0.6"/>
        <circle cx="235" cy="300" r="2.5" fill="#7bc600" opacity="0.7"/>
        """
    },
    "kalki": {
        "title": "KALKI",
        "subtitle": "2898 AD",
        "year": "2024",
        "rating": "7.9",
        "bg1": "#000814", "bg2": "#001a3d", "bg3": "#0066cc",
        "accent": "#00ccff",
        "art": """
        <defs>
          <radialGradient id="sciFiGlow" cx="50%" cy="30%" r="70%">
            <stop offset="0%" stop-color="#0066cc" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#000814" stop-opacity="0"/>
          </radialGradient>
          <radialGradient id="techCircle" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#00ccff" stop-opacity="0.3"/>
            <stop offset="60%" stop-color="#0044aa" stop-opacity="0.1"/>
            <stop offset="100%" stop-color="#000814" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#000814"/>
        <rect width="300" height="450" fill="url(#sciFiGlow)"/>
        <!-- Futuristic city skyline bottom -->
        <rect x="0" y="380" width="300" height="70" fill="#001122"/>
        <rect x="10" y="340" width="20" height="40" fill="#001122"/>
        <rect x="40" y="320" width="25" height="60" fill="#001122"/>
        <rect x="75" y="350" width="15" height="30" fill="#001122"/>
        <rect x="200" y="330" width="22" height="50" fill="#001122"/>
        <rect x="235" y="310" width="28" height="70" fill="#001122"/>
        <rect x="270" y="345" width="18" height="35" fill="#001122"/>
        <!-- Building lights -->
        <rect x="15" y="345" width="4" height="3" fill="#00ccff" opacity="0.6"/>
        <rect x="47" y="328" width="4" height="3" fill="#00ccff" opacity="0.5"/>
        <rect x="240" y="318" width="4" height="3" fill="#00ccff" opacity="0.6"/>
        <!-- Tech circle behind figure -->
        <circle cx="150" cy="200" r="110" fill="none" stroke="#0066cc" stroke-width="1.5" opacity="0.5"/>
        <circle cx="150" cy="200" r="90" fill="none" stroke="#0044aa" stroke-width="1" opacity="0.4"/>
        <circle cx="150" cy="200" r="70" fill="none" stroke="#00ccff" stroke-width="0.5" opacity="0.3"/>
        <!-- Rotating marks on outer circle -->
        <line x1="150" y1="90" x2="150" y2="78" stroke="#00ccff" stroke-width="2" opacity="0.7"/>
        <line x1="260" y1="200" x2="272" y2="200" stroke="#00ccff" stroke-width="2" opacity="0.7"/>
        <line x1="150" y1="310" x2="150" y2="322" stroke="#00ccff" stroke-width="2" opacity="0.7"/>
        <line x1="40" y1="200" x2="28" y2="200" stroke="#00ccff" stroke-width="2" opacity="0.7"/>
        <!-- Kalki figure - futuristic warrior -->
        <ellipse cx="150" cy="155" rx="24" ry="28" fill="#000e2a"/>
        <!-- Helmet/crown -->
        <path d="M126 150 Q128 120 150 115 Q172 120 174 150 Z" fill="#001a3d"/>
        <path d="M138 118 L142 100 L150 108 L158 100 L162 118" fill="#0066cc" opacity="0.8"/>
        <!-- Suit body -->
        <rect x="126" y="181" width="48" height="90" rx="8" fill="#000e2a"/>
        <!-- Suit energy lines -->
        <line x1="150" y1="185" x2="150" y2="265" stroke="#00ccff" stroke-width="1.5" opacity="0.6"/>
        <line x1="130" y1="200" x2="170" y2="200" stroke="#00ccff" stroke-width="1" opacity="0.4"/>
        <line x1="128" y1="220" x2="172" y2="220" stroke="#00ccff" stroke-width="1" opacity="0.4"/>
        <!-- Arms with weapons -->
        <rect x="60" y="186" width="70" height="14" rx="6" fill="#000e2a"/>
        <rect x="170" y="186" width="70" height="14" rx="6" fill="#000e2a"/>
        <!-- Energy weapon glow -->
        <ellipse cx="62" cy="193" rx="14" ry="10" fill="#00ccff" opacity="0.3"/>
        <ellipse cx="238" cy="193" rx="14" ry="10" fill="#00ccff" opacity="0.3"/>
        <circle cx="55" cy="193" r="6" fill="#00ccff" opacity="0.6"/>
        <circle cx="245" cy="193" r="6" fill="#00ccff" opacity="0.6"/>
        <!-- Eye glow -->
        <ellipse cx="142" cy="157" rx="5" ry="4" fill="#00ccff" opacity="0.9"/>
        <ellipse cx="158" cy="157" rx="5" ry="4" fill="#00ccff" opacity="0.9"/>
        <!-- Legs armored -->
        <rect x="132" y="269" width="16" height="68" rx="5" fill="#000e2a"/>
        <rect x="152" y="269" width="16" height="68" rx="5" fill="#000e2a"/>
        <!-- Knee joint light -->
        <circle cx="140" cy="310" r="4" fill="#0066cc" opacity="0.6"/>
        <circle cx="160" cy="310" r="4" fill="#0066cc" opacity="0.6"/>
        <!-- Stars -->
        <circle cx="30" cy="40" r="1.5" fill="white" opacity="0.8"/>
        <circle cx="80" cy="20" r="1" fill="white" opacity="0.6"/>
        <circle cx="200" cy="30" r="2" fill="white" opacity="0.7"/>
        <circle cx="260" cy="50" r="1.5" fill="white" opacity="0.5"/>
        <circle cx="290" cy="15" r="1" fill="white" opacity="0.8"/>
        <circle cx="15" cy="80" r="1" fill="white" opacity="0.6"/>
        """
    },
    "devara": {
        "title": "DEVARA",
        "subtitle": "PART — 1",
        "year": "2024",
        "rating": "7.8",
        "bg1": "#00080f", "bg2": "#001a2e", "bg3": "#003d66",
        "accent": "#00aaff",
        "art": """
        <defs>
          <radialGradient id="oceanGlow" cx="50%" cy="60%" r="80%">
            <stop offset="0%" stop-color="#005a8c" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#00080f" stop-opacity="0"/>
          </radialGradient>
          <linearGradient id="waveGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0077aa"/>
            <stop offset="100%" stop-color="#003355"/>
          </linearGradient>
        </defs>
        <rect width="300" height="450" fill="#00080f"/>
        <rect width="300" height="450" fill="url(#oceanGlow)"/>
        <!-- Ocean waves -->
        <path d="M0 300 Q40 280 80 300 Q120 320 160 300 Q200 280 240 300 Q280 320 300 300 L300 450 L0 450 Z" fill="#002244" opacity="0.7"/>
        <path d="M0 320 Q50 305 100 320 Q150 335 200 320 Q250 305 300 320 L300 450 L0 450 Z" fill="#003366" opacity="0.5"/>
        <path d="M0 345 Q60 335 120 345 Q180 355 240 345 Q270 340 300 348 L300 450 L0 450 Z" fill="#004477" opacity="0.4"/>
        <!-- Ship mast -->
        <rect x="148" y="60" width="4" height="220" fill="#3a2800"/>
        <!-- Sail -->
        <path d="M152 70 Q200 120 190 200 L152 200 Z" fill="#1a1200" opacity="0.7"/>
        <path d="M148 80 Q100 130 108 210 L148 210 Z" fill="#1a1200" opacity="0.6"/>
        <!-- Flag -->
        <path d="M152 60 L180 72 L152 84 Z" fill="#8b0000"/>
        <!-- Devara figure on bow -->
        <ellipse cx="150" cy="260" rx="22" ry="26" fill="#0a0800"/>
        <!-- Flowing hair/wind -->
        <path d="M128 255 Q115 238 118 225 Q122 215 128 218" fill="#1a0e00"/>
        <path d="M128 262 Q112 250 110 235 Q108 222 118 225" fill="#1a0e00" opacity="0.7"/>
        <!-- Dhoti/dress in wind -->
        <path d="M128 286 Q120 310 128 340 Q135 355 145 360 L152 360 Q148 340 152 310 Q156 286 172 286 Z" fill="#f0e0c0"/>
        <!-- Shawl/angavastram flying -->
        <path d="M128 290 Q100 270 80 250 Q70 240 75 230" fill="#8b4513" stroke="#a0522d" stroke-width="1" opacity="0.8"/>
        <!-- Upper body - commanding pose -->
        <rect x="128" y="284" width="44" height="28" rx="6" fill="#0a0800"/>
        <!-- Arms extended commanding sea -->
        <rect x="68" y="288" width="64" height="13" rx="6" fill="#0a0800"/>
        <rect x="168" y="288" width="64" height="13" rx="6" fill="#0a0800"/>
        <ellipse cx="68" cy="294" rx="12" ry="9" fill="#0a0800"/>
        <ellipse cx="232" cy="294" rx="12" ry="9" fill="#0a0800"/>
        <!-- Moonlight reflection on water -->
        <ellipse cx="150" cy="380" rx="40" ry="8" fill="#00aaff" opacity="0.2"/>
        <!-- Moon -->
        <circle cx="80" cy="55" r="28" fill="#d4c89a" opacity="0.7"/>
        <circle cx="72" cy="48" r="24" fill="#00080f"/>
        <!-- Stars -->
        <circle cx="160" cy="30" r="1.5" fill="white" opacity="0.8"/>
        <circle cx="220" cy="20" r="1" fill="white" opacity="0.7"/>
        <circle cx="260" cy="40" r="2" fill="white" opacity="0.6"/>
        <circle cx="30" cy="45" r="1.5" fill="white" opacity="0.5"/>
        <!-- Sea spray -->
        <ellipse cx="50" cy="300" rx="15" ry="5" fill="white" opacity="0.2"/>
        <ellipse cx="250" cy="305" rx="12" ry="4" fill="white" opacity="0.2"/>
        """
    },
    "salaar": {
        "title": "SALAAR",
        "subtitle": "CEASEFIRE — PART 1",
        "year": "2023",
        "rating": "7.5",
        "bg1": "#0a0000", "bg2": "#1a0000", "bg3": "#4d0000",
        "accent": "#cc0000",
        "art": """
        <defs>
          <radialGradient id="darkGlow" cx="50%" cy="40%" r="60%">
            <stop offset="0%" stop-color="#660000" stop-opacity="0.5"/>
            <stop offset="100%" stop-color="#0a0000" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#0a0000"/>
        <rect width="300" height="450" fill="url(#darkGlow)"/>
        <!-- Dark city rubble -->
        <rect x="0" y="360" width="300" height="90" fill="#0f0000"/>
        <!-- Rubble blocks -->
        <rect x="20" y="350" width="40" height="20" rx="2" fill="#1a0000"/>
        <rect x="70" y="360" width="30" height="15" rx="2" fill="#150000"/>
        <rect x="210" y="355" width="45" height="18" rx="2" fill="#1a0000"/>
        <rect x="260" y="362" width="35" height="12" rx="2" fill="#150000"/>
        <!-- Cracks on ground -->
        <path d="M100 380 L110 400 L90 430" stroke="#330000" stroke-width="2" fill="none"/>
        <path d="M200 375 L195 395 L215 420" stroke="#330000" stroke-width="2" fill="none"/>
        <!-- Salaar - dark warrior silhouette -->
        <!-- Head -->
        <ellipse cx="150" cy="158" rx="26" ry="30" fill="#0f0000"/>
        <!-- Dark hood/hair -->
        <path d="M124 152 Q122 128 150 120 Q178 128 176 152 Z" fill="#0a0000"/>
        <!-- Beard suggestion -->
        <path d="M136 178 Q150 188 164 178 Q158 192 150 194 Q142 192 136 178" fill="#0a0000"/>
        <!-- Eyes — intense -->
        <ellipse cx="141" cy="160" rx="6" ry="5" fill="#cc0000" opacity="0.9"/>
        <ellipse cx="159" cy="160" rx="6" ry="5" fill="#cc0000" opacity="0.9"/>
        <!-- Body - commanding -->
        <rect x="120" y="186" width="60" height="100" rx="8" fill="#0f0000"/>
        <!-- Jacket/coat -->
        <path d="M120 186 L110 240 L120 286 L130 280 L130 240 L120 186" fill="#0a0000"/>
        <path d="M180 186 L190 240 L180 286 L170 280 L170 240 L180 186" fill="#0a0000"/>
        <!-- Arms -->
        <rect x="55" y="192" width="68" height="17" rx="7" fill="#0f0000"/>
        <rect x="177" y="192" width="68" height="17" rx="7" fill="#0f0000"/>
        <ellipse cx="55" cy="200" rx="14" ry="11" fill="#0f0000"/>
        <ellipse cx="245" cy="200" rx="14" ry="11" fill="#0f0000"/>
        <!-- Chains/marks on arms -->
        <rect x="65" y="196" width="20" height="5" rx="2" fill="#330000"/>
        <rect x="215" y="196" width="20" height="5" rx="2" fill="#330000"/>
        <!-- Weapon in right hand -->
        <rect x="246" y="178" width="5" height="45" rx="2" fill="#444"/>
        <rect x="240" y="178" width="17" height="5" rx="2" fill="#444"/>
        <!-- Legs -->
        <rect x="130" y="284" width="18" height="72" rx="5" fill="#0f0000"/>
        <rect x="152" y="284" width="18" height="72" rx="5" fill="#0f0000"/>
        <!-- Blood/red ground marks -->
        <ellipse cx="150" cy="445" rx="180" ry="12" fill="#220000" opacity="0.6"/>
        <path d="M130 410 Q145 415 160 410" stroke="#550000" stroke-width="2" fill="none" opacity="0.5"/>
        <!-- Smoke/ash particles -->
        <circle cx="70" cy="130" r="3" fill="#220000" opacity="0.4"/>
        <circle cx="240" cy="110" r="4" fill="#220000" opacity="0.3"/>
        <circle cx="40" cy="200" r="2" fill="#330000" opacity="0.4"/>
        """
    },
    "hi_nanna": {
        "title": "HI NANNA",
        "subtitle": "A FATHER'S LOVE",
        "year": "2023",
        "rating": "8.2",
        "bg1": "#0a0008", "bg2": "#140014", "bg3": "#3d0030",
        "accent": "#ff69b4",
        "art": """
        <defs>
          <radialGradient id="heartGlow" cx="50%" cy="50%" r="60%">
            <stop offset="0%" stop-color="#c2185b" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#0a0008" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#0a0008"/>
        <rect width="300" height="450" fill="url(#heartGlow)"/>
        <!-- Bokeh lights background -->
        <circle cx="40" cy="60" r="20" fill="#ff69b4" opacity="0.06"/>
        <circle cx="250" cy="80" r="16" fill="#ff69b4" opacity="0.05"/>
        <circle cx="80" cy="200" r="24" fill="#c2185b" opacity="0.04"/>
        <circle cx="230" cy="300" r="18" fill="#ff1493" opacity="0.06"/>
        <circle cx="160" cy="40" r="12" fill="#ff69b4" opacity="0.08"/>
        <!-- Large heart -->
        <path d="M150 200 Q150 175 125 170 Q100 170 100 195 Q100 220 150 250 Q200 220 200 195 Q200 170 175 170 Q150 175 150 200 Z" fill="#8b0050" opacity="0.3"/>
        <!-- Father figure -->
        <ellipse cx="126" cy="198" rx="22" ry="26" fill="#1a0012"/>
        <rect x="104" y="222" width="44" height="80" rx="7" fill="#1a0012"/>
        <rect x="60" y="228" width="48" height="13" rx="6" fill="#1a0012"/>
        <rect x="148" y="232" width="48" height="13" rx="6" fill="#1a0012"/>
        <rect x="112" y="300" width="14" height="55" rx="5" fill="#1a0012"/>
        <rect x="128" y="302" width="14" height="53" rx="5" fill="#1a0012"/>
        <!-- Child figure (held) -->
        <ellipse cx="182" cy="210" rx="18" ry="20" fill="#1e0018"/>
        <rect x="166" y="228" width="32" height="55" rx="6" fill="#1e0018"/>
        <!-- Father's arm around child -->
        <path d="M148 228 Q165 218 180 225" stroke="#1a0012" stroke-width="12" fill="none" stroke-linecap="round"/>
        <!-- Child's arm up -->
        <path d="M166 235 Q155 220 148 230" stroke="#1e0018" stroke-width="10" fill="none" stroke-linecap="round"/>
        <!-- Eyes - emotional -->
        <ellipse cx="120" cy="200" rx="4" ry="3.5" fill="#ff1493" opacity="0.7"/>
        <ellipse cx="132" cy="200" rx="4" ry="3.5" fill="#ff1493" opacity="0.7"/>
        <!-- Floating hearts -->
        <path d="M200 110 Q200 100 192 98 Q184 98 184 108 Q184 118 200 128 Q216 118 216 108 Q216 98 208 98 Q200 100 200 110 Z" fill="#ff69b4" opacity="0.5"/>
        <path d="M70 150 Q70 143 64 141 Q58 141 58 149 Q58 157 70 165 Q82 157 82 149 Q82 141 76 141 Q70 143 70 150 Z" fill="#ff1493" opacity="0.4"/>
        <path d="M240 180 Q240 175 235 173 Q230 173 230 179 Q230 185 240 191 Q250 185 250 179 Q250 173 245 173 Q240 175 240 180 Z" fill="#ff69b4" opacity="0.45"/>
        <!-- Flower petals -->
        <circle cx="50" cy="380" r="6" fill="#ff69b4" opacity="0.3"/>
        <circle cx="90" cy="390" r="5" fill="#c2185b" opacity="0.25"/>
        <circle cx="220" cy="385" r="6" fill="#ff69b4" opacity="0.3"/>
        <circle cx="260" cy="375" r="5" fill="#ff1493" opacity="0.25"/>
        """
    },
    "animal": {
        "title": "ANIMAL",
        "subtitle": "A SON'S RAGE",
        "year": "2023",
        "rating": "7.6",
        "bg1": "#080808", "bg2": "#111", "bg3": "#222",
        "accent": "#cc0000",
        "art": """
        <defs>
          <radialGradient id="smokeGlow" cx="50%" cy="40%" r="70%">
            <stop offset="0%" stop-color="#333" stop-opacity="0.5"/>
            <stop offset="100%" stop-color="#080808" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#080808"/>
        <rect width="300" height="450" fill="url(#smokeGlow)"/>
        <!-- Dark atmospheric smoke -->
        <ellipse cx="80" cy="200" rx="60" ry="80" fill="#1a1a1a" opacity="0.3"/>
        <ellipse cx="220" cy="150" rx="50" ry="70" fill="#1a1a1a" opacity="0.25"/>
        <!-- Suit figure - powerful stance -->
        <!-- Head -->
        <ellipse cx="150" cy="148" rx="26" ry="30" fill="#111"/>
        <!-- Hair slicked back -->
        <path d="M124 142 Q126 118 150 114 Q174 118 176 142 Z" fill="#0a0a0a"/>
        <!-- Clean shaved jawline -->
        <path d="M134 172 Q150 182 166 172 Q160 186 150 188 Q140 186 134 172" fill="#0d0d0d"/>
        <!-- Suit body - expensive -->
        <rect x="118" y="178" width="64" height="108" rx="8" fill="#111"/>
        <!-- Suit lapels -->
        <path d="M118 178 L130 178 L150 200 L170 178 L182 178 L182 286 L118 286 Z" fill="#0d0d0d"/>
        <path d="M130 178 L150 200 L150 286 L118 286 L118 178 Z" fill="#111"/>
        <path d="M170 178 L150 200 L150 286 L182 286 L182 178 Z" fill="#111"/>
        <!-- Tie red -->
        <path d="M147 182 L150 200 L153 182 Z" fill="#cc0000"/>
        <rect x="147" y="182" width="6" height="68" rx="1" fill="#cc0000"/>
        <!-- Arms -->
        <rect x="50" y="184" width="72" height="16" rx="7" fill="#111"/>
        <rect x="178" y="184" width="72" height="16" rx="7" fill="#111"/>
        <!-- Fists/hands -->
        <rect x="44" y="188" width="18" height="16" rx="4" fill="#111"/>
        <rect x="238" y="188" width="18" height="16" rx="4" fill="#111"/>
        <!-- Bullet holes on suit -->
        <circle cx="135" cy="220" r="4" fill="#cc0000" opacity="0.7"/>
        <circle cx="158" cy="235" r="3" fill="#cc0000" opacity="0.5"/>
        <circle cx="165" cy="215" r="3" fill="#cc0000" opacity="0.6"/>
        <!-- Eyes - cold intense -->
        <ellipse cx="142" cy="150" rx="5" ry="4" fill="#222"/>
        <ellipse cx="158" cy="150" rx="5" ry="4" fill="#222"/>
        <ellipse cx="142" cy="150" rx="2" ry="2.5" fill="#cc0000" opacity="0.6"/>
        <ellipse cx="158" cy="150" rx="2" ry="2.5" fill="#cc0000" opacity="0.6"/>
        <!-- Legs dark trousers -->
        <rect x="130" y="284" width="16" height="72" rx="5" fill="#0d0d0d"/>
        <rect x="154" y="284" width="16" height="72" rx="5" fill="#0d0d0d"/>
        <!-- Gun in hand -->
        <rect x="238" y="192" width="28" height="10" rx="3" fill="#333"/>
        <rect x="254" y="200" width="8" height="14" rx="2" fill="#333"/>
        <!-- Blood spatter -->
        <circle cx="60" cy="260" r="2" fill="#cc0000" opacity="0.3"/>
        <circle cx="240" cy="280" r="2" fill="#cc0000" opacity="0.3"/>
        <circle cx="100" cy="300" r="1.5" fill="#cc0000" opacity="0.25"/>
        """
    },
    "fighter": {
        "title": "FIGHTER",
        "subtitle": "INDIA'S TOP GUN",
        "year": "2024",
        "rating": "7.2",
        "bg1": "#000a14", "bg2": "#001428", "bg3": "#002855",
        "accent": "#ff8c00",
        "art": """
        <defs>
          <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#000a14"/>
            <stop offset="50%" stop-color="#001a3d"/>
            <stop offset="100%" stop-color="#003366"/>
          </linearGradient>
          <radialGradient id="sunGlow" cx="50%" cy="30%" r="40%">
            <stop offset="0%" stop-color="#ff8c00" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#000a14" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="url(#skyGrad)"/>
        <rect width="300" height="450" fill="url(#sunGlow)"/>
        <!-- Jet aircraft in background large -->
        <path d="M30 200 L270 200 L280 190 L260 185 L240 200 L200 195 L150 188 L100 195 L60 185 L40 190 Z" fill="#1a2a3a" opacity="0.4"/>
        <!-- Wings -->
        <path d="M60 200 L20 230 L20 240 L60 215 Z" fill="#1a2a3a" opacity="0.4"/>
        <path d="M240 200 L280 230 L280 240 L240 215 Z" fill="#1a2a3a" opacity="0.4"/>
        <!-- Pilot figure large -->
        <ellipse cx="150" cy="195" rx="24" ry="28" fill="#0d1a26"/>
        <!-- Flight helmet -->
        <path d="M126 188 Q126 158 150 152 Q174 158 174 188 Z" fill="#1a2a3a"/>
        <!-- Visor -->
        <path d="M132 178 Q150 172 168 178 Q168 190 150 188 Q132 190 132 178 Z" fill="#ff8c00" opacity="0.7"/>
        <!-- Oxygen mask -->
        <rect x="136" y="196" width="28" height="20" rx="8" fill="#1a2a3a"/>
        <!-- Flight suit body -->
        <rect x="120" y="222" width="60" height="95" rx="8" fill="#0d1a26"/>
        <!-- G-suit details -->
        <rect x="124" y="240" width="52" height="6" rx="2" fill="#1a2a3a"/>
        <rect x="124" y="255" width="52" height="5" rx="2" fill="#1a2a3a"/>
        <rect x="124" y="268" width="52" height="5" rx="2" fill="#1a2a3a"/>
        <!-- Arm with patch -->
        <rect x="55" y="228" width="68" height="15" rx="7" fill="#0d1a26"/>
        <rect x="178" y="228" width="68" height="15" rx="7" fill="#0d1a26"/>
        <!-- India flag patch -->
        <rect x="180" y="231" width="18" height="10" rx="1" fill="#ff8c00" opacity="0.8"/>
        <rect x="180" y="235" width="18" height="3" rx="0" fill="white" opacity="0.6"/>
        <!-- Clouds low -->
        <ellipse cx="50" cy="380" rx="50" ry="15" fill="white" opacity="0.05"/>
        <ellipse cx="250" cy="400" rx="45" ry="12" fill="white" opacity="0.04"/>
        <!-- Afterburner glow from bottom -->
        <ellipse cx="150" cy="445" rx="40" ry="12" fill="#ff4500" opacity="0.25"/>
        <!-- Contrail lines -->
        <line x1="150" y1="60" x2="30" y2="120" stroke="white" stroke-width="1.5" opacity="0.15"/>
        <line x1="150" y1="60" x2="270" y2="120" stroke="white" stroke-width="1.5" opacity="0.15"/>
        <!-- Stars -->
        <circle cx="30" cy="30" r="1.5" fill="white" opacity="0.7"/>
        <circle cx="90" cy="15" r="1" fill="white" opacity="0.6"/>
        <circle cx="210" cy="25" r="1.5" fill="white" opacity="0.5"/>
        <circle cx="280" cy="10" r="1" fill="white" opacity="0.7"/>
        """
    },
    "dunki": {
        "title": "DUNKI",
        "subtitle": "RAJKUMAR HIRANI",
        "year": "2023",
        "rating": "7.4",
        "bg1": "#080b14", "bg2": "#101828", "bg3": "#1a2840",
        "accent": "#4dabf7",
        "art": """
        <defs>
          <radialGradient id="mapGlow" cx="50%" cy="50%" r="70%">
            <stop offset="0%" stop-color="#1a4480" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#080b14" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#080b14"/>
        <rect width="300" height="450" fill="url(#mapGlow)"/>
        <!-- World map faint outline -->
        <path d="M30 200 Q60 180 90 200 Q110 215 130 200 Q160 185 180 200 Q200 215 210 200 Q230 185 260 200" stroke="#1a4480" stroke-width="1.5" fill="none" opacity="0.3"/>
        <ellipse cx="80" cy="200" rx="40" ry="25" fill="none" stroke="#1a4480" stroke-width="1" opacity="0.2"/>
        <ellipse cx="200" cy="195" rx="50" ry="30" fill="none" stroke="#1a4480" stroke-width="1" opacity="0.2"/>
        <!-- Group of 4 people walking -->
        <!-- Person 1 (SRK) - center slightly ahead -->
        <ellipse cx="150" cy="195" rx="20" ry="24" fill="#101828"/>
        <rect x="130" y="218" width="40" height="80" rx="6" fill="#101828"/>
        <rect x="95" y="224" width="38" height="12" rx="5" fill="#101828"/>
        <rect x="172" y="228" width="38" height="12" rx="5" fill="#101828"/>
        <rect x="136" y="296" width="13" height="55" rx="4" fill="#101828"/>
        <rect x="151" y="296" width="13" height="55" rx="4" fill="#101828"/>
        <!-- Jacket -->
        <path d="M130 218 L120 255 L130 298 L140 292 Z" fill="#0d1520"/>
        <path d="M170 218 L180 255 L170 298 L160 292 Z" fill="#0d1520"/>
        <!-- Person 2 (left) -->
        <ellipse cx="95" cy="210" rx="17" ry="20" fill="#0d1a2a"/>
        <rect x="78" y="228" width="34" height="72" rx="6" fill="#0d1a2a"/>
        <rect x="78" y="302" width="12" height="48" rx="4" fill="#0d1a2a"/>
        <rect x="91" y="304" width="12" height="46" rx="4" fill="#0d1a2a"/>
        <!-- Person 3 (right) -->
        <ellipse cx="205" cy="208" rx="17" ry="20" fill="#0d1a2a"/>
        <rect x="188" y="226" width="34" height="72" rx="6" fill="#0d1a2a"/>
        <rect x="191" y="296" width="12" height="50" rx="4" fill="#0d1a2a"/>
        <rect x="204" y="298" width="12" height="48" rx="4" fill="#0d1a2a"/>
        <!-- Suitcases/bags -->
        <rect x="75" y="290" width="22" height="18" rx="3" fill="#0a1220"/>
        <rect x="80" y="286" width="12" height="5" rx="2" fill="#0a1220"/>
        <rect x="205" y="285" width="22" height="18" rx="3" fill="#0a1220"/>
        <rect x="210" y="281" width="12" height="5" rx="2" fill="#0a1220"/>
        <!-- Dotted path/route line on ground -->
        <path d="M0 360 Q75 340 150 360 Q225 380 300 360" stroke="#4dabf7" stroke-width="1.5" stroke-dasharray="5,8" fill="none" opacity="0.5"/>
        <!-- Compass -->
        <circle cx="248" cy="80" r="28" fill="none" stroke="#1a4480" stroke-width="1.5" opacity="0.5"/>
        <line x1="248" y1="55" x2="248" y2="65" stroke="#4dabf7" stroke-width="2" opacity="0.7"/>
        <line x1="248" y1="95" x2="248" y2="105" stroke="#4dabf7" stroke-width="2" opacity="0.5"/>
        <line x1="220" y1="80" x2="230" y2="80" stroke="#4dabf7" stroke-width="2" opacity="0.5"/>
        <line x1="266" y1="80" x2="276" y2="80" stroke="#4dabf7" stroke-width="2" opacity="0.5"/>
        <polygon points="248,58 245,70 248,67 251,70" fill="#4dabf7" opacity="0.8"/>
        <!-- Stars/destination markers -->
        <circle cx="60" cy="100" r="3" fill="#4dabf7" opacity="0.5"/>
        <circle cx="240" cy="120" r="4" fill="#4dabf7" opacity="0.4"/>
        <path d="M60 100 Q150 80 240 120" stroke="#4dabf7" stroke-width="1" stroke-dasharray="4,6" fill="none" opacity="0.3"/>
        """
    },
    "guntur_kaaram": {
        "title": "GUNTUR",
        "subtitle": "KAARAM",
        "year": "2024",
        "rating": "6.8",
        "bg1": "#0a0800", "bg2": "#1a1000", "bg3": "#3a2800",
        "accent": "#ff6b35",
        "art": """
        <defs>
          <radialGradient id="spiceGlow" cx="50%" cy="60%" r="70%">
            <stop offset="0%" stop-color="#c83200" stop-opacity="0.5"/>
            <stop offset="100%" stop-color="#0a0800" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#0a0800"/>
        <rect width="300" height="450" fill="url(#spiceGlow)"/>
        <!-- Red chilli background pattern -->
        <path d="M40 300 Q45 280 55 275 Q65 270 70 280 Q75 295 65 310 Q55 320 40 310 Z" fill="#8b0000" opacity="0.3"/>
        <path d="M240 290 Q245 270 255 265 Q265 260 270 270 Q275 285 265 300 Q255 312 240 302 Z" fill="#8b0000" opacity="0.3"/>
        <!-- Family - father and son split visual -->
        <!-- Dividing line (family conflict) -->
        <line x1="150" y1="80" x2="150" y2="360" stroke="#8b0000" stroke-width="1.5" opacity="0.4" stroke-dasharray="8,6"/>
        <!-- Father (left) - older distinguished -->
        <ellipse cx="100" cy="200" rx="22" ry="26" fill="#1a1000"/>
        <!-- Grey hair/distinguished -->
        <path d="M78 194 Q80 172 100 168 Q120 172 122 194 Z" fill="#333"/>
        <!-- Formal shirt -->
        <rect x="78" y="224" width="44" height="85" rx="6" fill="#1a1000"/>
        <rect x="38" y="230" width="44" height="13" rx="6" fill="#1a1000"/>
        <rect x="122" y="234" width="44" height="13" rx="6" fill="#1a1000"/>
        <rect x="84" y="307" width="14" height="55" rx="5" fill="#1a1000"/>
        <rect x="100" y="308" width="14" height="54" rx="5" fill="#1a1000"/>
        <!-- Dhoti/veshti -->
        <path d="M78 290 Q75 330 85 360 L115 360 Q125 330 122 290 Z" fill="#f0e8d0" opacity="0.5"/>
        <!-- Son (right) - modern younger -->
        <ellipse cx="200" cy="195" rx="22" ry="26" fill="#1a0800"/>
        <path d="M178 188 Q180 165 200 160 Q220 165 222 188 Z" fill="#0d0800"/>
        <!-- Modern jacket -->
        <rect x="178" y="220" width="44" height="88" rx="6" fill="#1a0800"/>
        <path d="M178 220 L168 258 L178 308 L188 302 Z" fill="#150800"/>
        <path d="M222 220 L232 258 L222 308 L212 302 Z" fill="#150800"/>
        <!-- Modern jeans -->
        <rect x="136" y="230" width="44" height="13" rx="6" fill="#1a0800"/>
        <rect x="182" y="234" width="44" height="13" rx="6" fill="#1a0800"/>
        <rect x="184" y="306" width="14" height="56" rx="5" fill="#1a0800"/>
        <rect x="200" y="307" width="14" height="55" rx="5" fill="#1a0800"/>
        <!-- Red chilli pepper between them -->
        <path d="M142 215 Q150 205 158 215 Q162 230 150 240 Q138 230 142 215 Z" fill="#cc0000" opacity="0.8"/>
        <path d="M150 205 Q150 195 155 188" stroke="#2d6e00" stroke-width="2" fill="none"/>
        <!-- Spice particles/dust -->
        <circle cx="70" cy="160" r="2" fill="#ff6b35" opacity="0.5"/>
        <circle cx="230" cy="150" r="2.5" fill="#ff6b35" opacity="0.4"/>
        <circle cx="55" cy="280" r="2" fill="#cc0000" opacity="0.4"/>
        <circle cx="255" cy="270" r="2" fill="#cc0000" opacity="0.4"/>
        <!-- Ground texture -->
        <ellipse cx="150" cy="440" rx="200" ry="18" fill="#2d1800" opacity="0.4"/>
        """
    },
    "merry_christmas": {
        "title": "MERRY",
        "subtitle": "CHRISTMAS",
        "year": "2024",
        "rating": "7.8",
        "bg1": "#00050a", "bg2": "#001a0a", "bg3": "#003314",
        "accent": "#cc0000",
        "art": """
        <defs>
          <radialGradient id="xmasGlow" cx="50%" cy="40%" r="65%">
            <stop offset="0%" stop-color="#003d14" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#00050a" stop-opacity="0"/>
          </radialGradient>
        </defs>
        <rect width="300" height="450" fill="#00050a"/>
        <rect width="300" height="450" fill="url(#xmasGlow)"/>
        <!-- Christmas tree dark -->
        <polygon points="150,60 80,200 220,200" fill="#002810" opacity="0.7"/>
        <polygon points="150,110 90,230 210,230" fill="#003314" opacity="0.7"/>
        <polygon points="150,160 95,270 205,270" fill="#004018" opacity="0.7"/>
        <!-- Tree trunk -->
        <rect x="140" y="270" width="20" height="40" rx="3" fill="#2d1800"/>
        <!-- Ornaments on tree -->
        <circle cx="120" cy="170" r="8" fill="#cc0000" opacity="0.8"/>
        <circle cx="180" cy="160" r="7" fill="#ffd700" opacity="0.7"/>
        <circle cx="140" cy="220" r="7" fill="#cc0000" opacity="0.7"/>
        <circle cx="165" cy="215" r="6" fill="#ffd700" opacity="0.6"/>
        <circle cx="125" cy="240" r="6" fill="#cc0000" opacity="0.7"/>
        <circle cx="175" cy="245" r="7" fill="#cc0000" opacity="0.6"/>
        <!-- Star on top -->
        <polygon points="150,52 153,62 164,62 155,68 158,78 150,72 142,78 145,68 136,62 147,62" fill="#ffd700" opacity="0.8"/>
        <!-- Two figures at tree base -->
        <!-- Figure 1 (Katrina) -->
        <ellipse cx="118" cy="318" rx="18" ry="22" fill="#0d0d14"/>
        <rect x="100" y="338" width="36" height="65" rx="6" fill="#0d0d14"/>
        <!-- Evening gown suggestion -->
        <path d="M100 360 Q95 390 100 402 Q112 415 118 415 Q124 415 136 402 Q141 390 136 360 Z" fill="#0d0d14"/>
        <!-- Figure 2 (Vijay) -->
        <ellipse cx="182" cy="315" rx="18" ry="22" fill="#080810"/>
        <rect x="164" y="335" width="36" height="65" rx="6" fill="#080810"/>
        <!-- Suit jacket -->
        <path d="M164 335 L156 368 L164 400 L174 394 Z" fill="#060610"/>
        <path d="M200 335 L208 368 L200 400 L190 394 Z" fill="#060610"/>
        <!-- Hands touching/reaching -->
        <path d="M136 360 Q150 348 164 355" stroke="#0d0d14" stroke-width="10" fill="none" stroke-linecap="round"/>
        <!-- Christmas lights on tree -->
        <circle cx="110" cy="180" r="3" fill="#ffd700" opacity="0.9"/>
        <circle cx="155" cy="175" r="3" fill="#cc0000" opacity="0.9"/>
        <circle cx="190" cy="185" r="3" fill="#00aa44" opacity="0.9"/>
        <circle cx="130" cy="210" r="3" fill="#ffd700" opacity="0.8"/>
        <circle cx="170" cy="205" r="3" fill="#cc0000" opacity="0.8"/>
        <!-- Snow/bokeh -->
        <circle cx="40" cy="80" r="2" fill="white" opacity="0.4"/>
        <circle cx="260" cy="60" r="1.5" fill="white" opacity="0.5"/>
        <circle cx="30" cy="180" r="2.5" fill="white" opacity="0.3"/>
        <circle cx="280" cy="200" r="2" fill="white" opacity="0.4"/>
        <circle cx="70" cy="350" r="2" fill="white" opacity="0.3"/>
        <circle cx="240" cy="340" r="1.5" fill="white" opacity="0.4"/>
        """
    },
}

def make_svg(key, data):
    title = data["title"]
    subtitle = data["subtitle"]
    year = data["year"]
    rating = data["rating"]
    bg1 = data["bg1"]
    bg2 = data["bg2"]
    accent = data["accent"]
    art = data["art"]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="300" height="450" viewBox="0 0 300 450">
  <!-- Background -->
  <rect width="300" height="450" fill="{bg1}" rx="0"/>
  
  <!-- Art layer -->
  {art}
  
  <!-- Bottom gradient overlay for text -->
  <defs>
    <linearGradient id="textFade_{key}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{bg1}" stop-opacity="0"/>
      <stop offset="55%" stop-color="{bg1}" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="{bg1}" stop-opacity="0.97"/>
    </linearGradient>
    <linearGradient id="topFade_{key}" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="{bg1}" stop-opacity="0.5"/>
      <stop offset="30%" stop-color="{bg1}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <rect width="300" height="450" fill="url(#textFade_{key})"/>
  <rect width="300" height="150" fill="url(#topFade_{key})"/>
  
  <!-- Rating badge -->
  <rect x="12" y="12" width="54" height="24" rx="12" fill="rgba(0,0,0,0.65)"/>
  <rect x="12" y="12" width="54" height="24" rx="12" fill="none" stroke="{accent}" stroke-width="1" opacity="0.6"/>
  <text x="39" y="28" text-anchor="middle" fill="{accent}" font-family="Arial,sans-serif" font-size="11" font-weight="700">⭐ {rating}</text>
  
  <!-- Title text -->
  <text x="16" y="400" fill="white" font-family="Georgia,serif" font-size="26" font-weight="900" letter-spacing="1">{title}</text>
  <text x="16" y="422" fill="{accent}" font-family="Arial,sans-serif" font-size="11" font-weight="600" letter-spacing="1.5">{subtitle}</text>
  <text x="16" y="440" fill="rgba(255,255,255,0.4)" font-family="Arial,sans-serif" font-size="10">{year}</text>
  
  <!-- Decorative accent line -->
  <rect x="16" y="388" width="40" height="3" rx="2" fill="{accent}"/>
</svg>'''
    return svg

for key, data in POSTERS.items():
    svg_content = make_svg(key, data)
    path = os.path.join(OUT, f"{key}.svg")
    with open(path, "w") as f:
        f.write(svg_content)
    print(f"Generated: {key}.svg")

print(f"\n✅ {len(POSTERS)} poster SVGs created in {OUT}")
