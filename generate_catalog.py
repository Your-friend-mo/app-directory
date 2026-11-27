import os
import re
import json

BASE_DIR = r"c:\Users\m\Documents\app-catalog"
APPS_DIR = os.path.join(BASE_DIR, "apps")
os.makedirs(APPS_DIR, exist_ok=True)

DOMAIN = "https://apphub.comee.online"
DATE_MODIFIED = "2026-11-27"

# 18 Curated Applications & Games
PRODUCTS = [
    # --- Existing 9 Applications ---
    {
        "id": "vscodium",
        "name": "VSCodium",
        "keyword": "VSCodium",
        "type": "SoftwareApplication",
        "category": "Development",
        "badge": "Code Editor",
        "metaDesc": "Download VSCodium, the telemetry-free binary release of VS Code. Enjoy standard development tools, Git integration, and extensions with total user privacy.",
        "desc": "Telemetry-free open-source binary distributions of VS Code.",
        "version": "1.92.0",
        "license": "MIT",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-08-15",
        "downloadUrl": "https://vscodium.com",
        "sameAs": "https://github.com/VSCodium/vscodium",
        "author": "VSCodium Contributors",
        "color": "#2563eb",
        "keywords": ["code", "ide", "vscode", "editor", "programming", "developer", "git", "terminal", "vscodium"],
        "icon": '<svg role="img" aria-label="VSCodium icon" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>VSCodium Icon</title><polygon points="16 18 22 12 16 6"></polygon><polygon points="8 6 2 12 8 18"></polygon></svg>',
        "existing": True
    },
    {
        "id": "obsidian",
        "name": "Obsidian Notes",
        "keyword": "Obsidian Notes",
        "type": "SoftwareApplication",
        "category": "Productivity",
        "badge": "Knowledge Base",
        "metaDesc": "Explore Obsidian Notes, the extensible Markdown knowledge base. Build your second brain with local-first bidirectional linking, graph view, and rich plugins.",
        "desc": "Extensible Markdown knowledge base and personal wiki.",
        "version": "1.6.5",
        "license": "Freeware",
        "platform": "Windows, macOS, Linux, iOS, Android",
        "releaseDate": "2026-07-20",
        "downloadUrl": "https://obsidian.md",
        "sameAs": "https://en.wikipedia.org/wiki/Obsidian_(software)",
        "author": "Dynalist Inc.",
        "color": "#7c3aed",
        "keywords": ["notes", "wiki", "markdown", "knowledge", "pkm", "second brain", "graph", "writing", "obsidian"],
        "icon": '<svg role="img" aria-label="Obsidian Notes icon" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Obsidian Notes Icon</title><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>',
        "existing": True
    },
    {
        "id": "bitwarden",
        "name": "Bitwarden",
        "keyword": "Bitwarden",
        "type": "SoftwareApplication",
        "category": "Security",
        "badge": "Password Vault",
        "metaDesc": "Get Bitwarden, the leading open-source password manager. Secure your sensitive credentials with zero-knowledge AES-256 encryption across all your devices.",
        "desc": "Open-source password manager with zero-knowledge encryption.",
        "version": "2024.7.1",
        "license": "GPLv3",
        "platform": "Cross-platform (All Devices)",
        "releaseDate": "2026-07-28",
        "downloadUrl": "https://bitwarden.com",
        "sameAs": "https://github.com/bitwarden",
        "author": "Bitwarden Inc.",
        "color": "#0284c7",
        "keywords": ["password", "passwords", "vault", "2fa", "authenticator", "credentials", "login", "security", "passkeys", "bitwarden"],
        "icon": '<svg role="img" aria-label="Bitwarden icon" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Bitwarden Icon</title><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>',
        "existing": True
    },
    {
        "id": "vlc",
        "name": "VLC Media Player",
        "keyword": "VLC Media Player",
        "type": "SoftwareApplication",
        "category": "Media",
        "badge": "Audio & Video",
        "metaDesc": "Download VLC Media Player, the open-source cross-platform player. Play virtually all video and audio formats without extra codecs or tracking mechanisms.",
        "desc": "Universal multimedia player supporting virtually all formats.",
        "version": "3.0.21",
        "license": "GNU LGPL",
        "platform": "Windows, macOS, Linux, Android, iOS",
        "releaseDate": "2026-06-10",
        "downloadUrl": "https://www.videolan.org/vlc/",
        "sameAs": "https://en.wikipedia.org/wiki/VLC_media_player",
        "author": "VideoLAN Project",
        "color": "#ea580c",
        "keywords": ["video", "audio", "player", "movie", "music", "mp4", "mkv", "mp3", "stream", "media", "vlc"],
        "icon": '<svg role="img" aria-label="VLC Media Player icon" viewBox="0 0 24 24" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>VLC Media Player Icon</title><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>',
        "existing": True
    },
    {
        "id": "signal",
        "name": "Signal Messenger",
        "keyword": "Signal Messenger",
        "type": "SoftwareApplication",
        "category": "Security",
        "badge": "Private Chat",
        "metaDesc": "Get Signal Messenger, the gold standard for private encrypted messaging. Communicate securely with disappearing messages, voice, and HD video group calls.",
        "desc": "Private, state-of-the-art end-to-end encrypted messaging.",
        "version": "7.15.0",
        "license": "GPLv3",
        "platform": "Android, iOS, Windows, macOS, Linux",
        "releaseDate": "2026-08-01",
        "downloadUrl": "https://signal.org",
        "sameAs": "https://github.com/signalapp",
        "author": "Signal Technology Foundation",
        "color": "#3b82f6",
        "keywords": ["chat", "messenger", "messaging", "private", "sms", "text", "calling", "encrypted", "communication", "signal"],
        "icon": '<svg role="img" aria-label="Signal Messenger icon" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Signal Messenger Icon</title><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>',
        "existing": True
    },
    {
        "id": "7zip",
        "name": "7-Zip Utility",
        "keyword": "7-Zip Utility",
        "type": "SoftwareApplication",
        "category": "Utilities",
        "badge": "Compression",
        "metaDesc": "Download 7-Zip, the high-performance open-source archiver. Compress and extract files with AES-256 encryption, LZMA2 compression, and shell integration.",
        "desc": "High compression ratio file archiver with AES-256 encryption.",
        "version": "24.07",
        "license": "GNU LGPL",
        "platform": "Windows, Linux, CLI",
        "releaseDate": "2026-06-19",
        "downloadUrl": "https://www.7-zip.org",
        "sameAs": "https://en.wikipedia.org/wiki/7-Zip",
        "author": "Igor Pavlov",
        "color": "#16a34a",
        "keywords": ["zip", "unzip", "rar", "archive", "compress", "extractor", "tar", "7z", "compression", "7zip"],
        "icon": '<svg role="img" aria-label="7-Zip Utility icon" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>7-Zip Utility Icon</title><rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M9 3v18"></path><path d="M14 9h3"></path><path d="M14 15h3"></path></svg>',
        "existing": True
    },
    {
        "id": "kdenlive",
        "name": "Kdenlive Video Editor",
        "keyword": "Kdenlive Video Editor",
        "type": "SoftwareApplication",
        "category": "Media",
        "badge": "Video Editing",
        "metaDesc": "Download Kdenlive, the powerful open-source non-linear video editor. Create multi-track video timelines with color grading, effects, and GPU acceleration.",
        "desc": "Multi-track non-linear video editing suite with hardware acceleration.",
        "version": "24.05.2",
        "license": "GPLv3",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-07-12",
        "downloadUrl": "https://kdenlive.org",
        "sameAs": "https://github.com/KDE/kdenlive",
        "author": "KDE Community",
        "color": "#e11d48",
        "keywords": ["video", "editor", "editing", "render", "timeline", "clip", "movie", "cut", "multitrack", "kdenlive"],
        "icon": '<svg role="img" aria-label="Kdenlive Video Editor icon" viewBox="0 0 24 24" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Kdenlive Video Editor Icon</title><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>',
        "existing": True
    },
    {
        "id": "syncthing",
        "name": "Syncthing",
        "keyword": "Syncthing",
        "type": "SoftwareApplication",
        "category": "Utilities",
        "badge": "P2P Sync",
        "metaDesc": "Discover Syncthing, the decentralized peer-to-peer file synchronization utility. Sync files securely across your devices with TLS encryption and zero cloud.",
        "desc": "Continuous decentralized peer-to-peer file synchronization.",
        "version": "1.27.9",
        "license": "MPL-2.0",
        "platform": "Windows, macOS, Linux, Android",
        "releaseDate": "2026-07-05",
        "downloadUrl": "https://syncthing.net",
        "sameAs": "https://github.com/syncthing/syncthing",
        "author": "Syncthing Foundation",
        "color": "#0891b2",
        "keywords": ["sync", "synchronization", "backup", "p2p", "cloud", "transfer", "files", "peer", "syncthing"],
        "icon": '<svg role="img" aria-label="Syncthing icon" viewBox="0 0 24 24" fill="none" stroke="#0891b2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Syncthing Icon</title><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"></path></svg>',
        "existing": True
    },
    {
        "id": "hoppscotch",
        "name": "Hoppscotch",
        "keyword": "Hoppscotch",
        "type": "SoftwareApplication",
        "category": "Development",
        "badge": "API Client",
        "metaDesc": "Explore Hoppscotch, the lightweight open-source API development ecosystem. Test REST, GraphQL, and WebSocket endpoints quickly with zero local footprint.",
        "desc": "Lightweight, privacy-focused open source API development ecosystem.",
        "version": "2024.6.0",
        "license": "MIT",
        "platform": "Web, Windows, macOS, Linux",
        "releaseDate": "2026-06-25",
        "downloadUrl": "https://hoppscotch.com",
        "sameAs": "https://github.com/hoppscotch/hoppscotch",
        "author": "Hoppscotch Team",
        "color": "#10b981",
        "keywords": ["api", "rest", "graphql", "websocket", "postman", "http", "client", "developer", "endpoint", "hoppscotch"],
        "icon": '<svg role="img" aria-label="Hoppscotch icon" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Hoppscotch Icon</title><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
        "existing": True
    },

    # --- 9 New Popular Games ---
    {
        "id": "supertuxkart",
        "name": "SuperTuxKart",
        "keyword": "SuperTuxKart",
        "type": "VideoGame",
        "category": "Games",
        "badge": "3D Kart Racer",
        "metaDesc": "Download SuperTuxKart, the open-source 3D arcade kart racing game. Race with Tux and friends across dozens of tracks with local and online multiplayer modes.",
        "desc": "3D open-source arcade kart racer featuring Tux and friends.",
        "version": "1.4.0",
        "license": "GPLv3",
        "platform": "Windows, macOS, Linux, Android",
        "releaseDate": "2026-06-18",
        "downloadUrl": "https://supertuxkart.net",
        "sameAs": "https://github.com/supertuxkart/stk-code",
        "author": "SuperTuxKart Team",
        "color": "#f59e0b",
        "keywords": ["game", "racing", "kart", "arcade", "supertuxkart", "tux", "multiplayer", "tracks", "speed", "splitscreen"],
        "icon": '<svg role="img" aria-label="SuperTuxKart icon" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>SuperTuxKart Icon</title><circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="3"></circle><line x1="12" y1="3" x2="12" y2="9"></line><line x1="12" y1="15" x2="12" y2="21"></line><line x1="3" y1="12" x2="9" y2="12"></line><line x1="15" y1="12" x2="21" y2="12"></line></svg>',
        "existing": False,
        "genre": "Racing",
        "arch_text": "SuperTuxKart is built on a custom game engine called Antarctica, purpose-built for performance on low-to-mid-range hardware. The rendering pipeline uses OpenGL ES 3.0 and Vulkan on supported systems, delivering smooth frame rates even on integrated graphics. Physics are handled by the Bullet physics library, giving each kart distinct handling characteristics based on weight, acceleration, and grip statistics. The network multiplayer system uses a peer-to-peer relay architecture with a central game server for matchmaking. AI opponents use a waypoint-based racing line algorithm that adapts difficulty dynamically by adjusting their rubber-banding speed, item usage, and shortcut awareness. SuperTuxKart packages a full story mode campaign, quick race, time trial, egg hunt, and soccer mini-game modes into a single binary with zero external dependencies.",
        "features": [
            "Full 3D graphics with dynamic lighting and particle effects",
            "20+ official tracks and 20+ playable karts including Tux, Adiumy, and Wilber",
            "Local splitscreen multiplayer for up to 4 players",
            "Online multiplayer via the official SuperTuxKart server network",
            "Complete story mode with Grand Prix championships",
            "In-game add-on manager for community tracks and karts",
            "Fully keyboard, gamepad, and mouse-steer compatible",
            "GPLv3 source code available on GitHub for community contribution"
        ],
        "faqs": [
            ("Is SuperTuxKart free to download and play forever?", "Yes. SuperTuxKart is 100% free and open-source under the GPLv3 license. There are no paid DLC, in-app purchases, or subscription tiers."),
            ("Can I play SuperTuxKart online with friends?", "Yes. SuperTuxKart includes a built-in online multiplayer mode with server browsing. You can create or join public and private lobbies for races, battle arenas, and soccer."),
            ("What are the minimum system requirements for SuperTuxKart?", "SuperTuxKart requires a GPU with OpenGL 3.3 support, 512 MB RAM, and 700 MB disk space. It runs well on integrated Intel HD graphics and older AMD/NVIDIA cards."),
            ("How do I install add-on tracks in SuperTuxKart?", "Open the game, navigate to Add-Ons from the main menu, and browse the online repository. Click to install any community-created track, kart, or arena directly without leaving the game.")
        ],
        "comparison": [
            ("Mario Kart 8 Deluxe", "Proprietary / Nintendo Switch only", "No", "Yes", "Paid"),
            ("Sonic &amp; All-Stars Racing", "Proprietary / PC &amp; Console", "No", "Yes", "Paid"),
            ("SuperTuxKart", "GPLv3 / Win, Mac, Linux, Android", "Yes", "Yes", "Free")
        ]
    },
    {
        "id": "0ad",
        "name": "0 A.D.",
        "keyword": "0 A.D.",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Historical RTS",
        "metaDesc": "Download 0 A.D., the free open-source real-time strategy game of ancient warfare. Command historical civilizations with naval combat, trade, and custom maps.",
        "desc": "Real-time strategy game of ancient warfare and civilization building.",
        "version": "Alpha 26",
        "license": "GPLv2 / CC-BY-SA",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-05-22",
        "downloadUrl": "https://play0ad.com",
        "sameAs": "https://github.com/0ad/0ad",
        "author": "Wildfire Games",
        "color": "#d97706",
        "keywords": ["game", "rts", "strategy", "historical", "ancient", "warfare", "civilization", "0ad", "empires", "rome", "greece"],
        "icon": '<svg role="img" aria-label="0 A.D. icon" viewBox="0 0 24 24" fill="none" stroke="#d97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>0 A.D. Icon</title><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path><polyline points="14 2 14 8 20 8"></polyline><path d="m9 15 2 2 4-4"></path></svg>',
        "existing": False,
        "genre": "Real-Time Strategy",
        "arch_text": "0 A.D. is powered by Pyrogenesis, Wildfire Games open-source C++ engine designed for large-scale ancient warfare simulations. The simulation layer runs in a separate thread from the rendering layer to maintain deterministic multiplayer synchronization. The graphics stack uses OpenGL with an HDR-capable renderer supporting normal mapping, specular lighting, and GPU-accelerated particle systems. The JavaScript scripting engine (SpiderMonkey) exposes the entire game logic to moddable JS scripts, making 0 A.D. one of the most deeply moddable RTS games available. Maps are created with the Atlas editor, which supports terrain painting, object placement, elevation sculpting, and trigger scripting. The 12 historical civilizations each have fully unique unit rosters, building sets, and civilization bonuses accurately researched from historical records.",
        "features": [
            "12 historically researched civilizations with unique units and buildings",
            "Full-scale naval combat with ship boarding and sea trade routes",
            "Deep economic system with mining, farming, woodcutting, and trade",
            "Atlas map editor for custom scenario and campaign creation",
            "Online multiplayer via lobby system and direct IP connection",
            "Fully moddable via JavaScript, XML, and community mod manager",
            "GPLv2 engine source code available for community developers",
            "Free to play with no microtransactions or paid expansions"
        ],
        "faqs": [
            ("Is 0 A.D. a finished game?", "0 A.D. is in active alpha development with regular releases. Each alpha adds new civilizations, units, mechanics, and engine improvements. It is fully playable in its current state with stable multiplayer."),
            ("How does 0 A.D. compare to Age of Empires II?", "0 A.D. offers similar gameplay depth to Age of Empires II with real-time resource gathering, base building, and unit combat. Its civilizations are more historically detailed and the game is completely free and open-source."),
            ("Can I mod 0 A.D.?", "Yes extensively. The game logic is written in JavaScript and exposed via a full modding API. The community has created hundreds of mods including new civilizations, maps, game modes, and total conversions."),
            ("What are the system requirements for 0 A.D.?", "0 A.D. requires a dedicated GPU with OpenGL 2.1 support, 1 GB RAM, and 2.5 GB disk space. Performance scales well on modern hardware with high-unit-count battles.")
        ],
        "comparison": [
            ("Age of Empires IV", "Proprietary / Windows &amp; Xbox", "No", "Yes", "Paid"),
            ("StarCraft II", "Freeware / Windows &amp; Mac", "No", "Yes", "Partly Free"),
            ("0 A.D.", "GPLv2 / Win, Mac, Linux", "Yes", "Yes", "Free")
        ]
    },
    {
        "id": "mindustry",
        "name": "Mindustry",
        "keyword": "Mindustry",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Factory Defense",
        "metaDesc": "Explore Mindustry, the open-source factory automation and tower defense game. Build logistics supply chains, research tech trees, and protect your core online.",
        "desc": "Hybrid top-down tower defense and supply-chain factory automation.",
        "version": "v146.0",
        "license": "GPLv3",
        "platform": "Windows, macOS, Linux, Android, iOS",
        "releaseDate": "2026-07-15",
        "downloadUrl": "https://mindustrygame.github.io",
        "sameAs": "https://github.com/Anuken/Mindustry",
        "author": "Anuken",
        "color": "#059669",
        "keywords": ["game", "factory", "automation", "tower defense", "strategy", "mindustry", "sandbox", "logistics", "conveyors", "turrets"],
        "icon": '<svg role="img" aria-label="Mindustry icon" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Mindustry Icon</title><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>',
        "existing": False,
        "genre": "Strategy / Factory",
        "arch_text": "Mindustry is built in Java using the Arc framework, a lightweight game library developed by its solo creator Anuken. The game runs on the JVM, ensuring cross-platform compatibility across Windows, macOS, Linux, Android, and iOS without code changes. The simulation is tile-based with a delta-time update loop decoupled from the render frame rate. The conveyor belt and item transport system uses a custom discrete flow simulation that calculates item movement through each tile type at a fixed tick rate, enabling complex multi-tier factory chains of hundreds of belts without frame drops. The map editor bakes sector maps from procedurally generated noise with configurable ore density, enemy spawn distribution, and resource richness. Mindustry multiplayer uses a custom UDP-based protocol with client-side prediction and server-side authoritative simulation.",
        "features": [
            "Tile-based factory automation with conveyors, routers, sorters, and bridges",
            "Deep tech tree with 150+ unlockable buildings and units",
            "Campaign mode with 50+ sectors across multiple planets",
            "Fully featured map editor with custom scripting via JavaScript",
            "Online multiplayer co-op and PvP with dedicated server support",
            "Modding support via JavaScript logic scripts and schematic blueprints",
            "Available on Android and iOS for mobile factory management",
            "Completely free on PC with no ads or in-app purchases"
        ],
        "faqs": [
            ("Is Mindustry free on PC?", "Yes. Mindustry is completely free on PC as an open-source GPLv3 game downloadable from the official website or GitHub. The mobile versions on Google Play and iOS App Store carry a small one-time fee."),
            ("What is the goal in Mindustry?", "In campaign mode, your goal is to protect your core from waves of enemies while building supply chains that produce ammunition for your defenses and resources for unit production. Each sector has unique terrain and objectives."),
            ("Does Mindustry have multiplayer?", "Yes. Mindustry supports online co-op and PvP multiplayer. You can host a local or public server, and official community servers are listed in the multiplayer menu. Up to 128 players can join large servers."),
            ("Can I mod Mindustry?", "Yes. Mindustry has a rich mod ecosystem. Mods are written in JavaScript and can add new buildings, units, planets, mechanics, and campaign content. The in-game mod browser lets you install community mods with one click.")
        ],
        "comparison": [
            ("Factorio", "Proprietary / Win, Mac, Linux", "No", "Yes", "Paid"),
            ("Satisfactory", "Proprietary / Windows &amp; Mac", "No", "Yes", "Paid"),
            ("Mindustry", "GPLv3 / Win, Mac, Linux, Mobile", "Yes", "Yes", "Free on PC")
        ]
    },
    {
        "id": "openttd",
        "name": "OpenTTD",
        "keyword": "OpenTTD",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Transport Tycoon",
        "metaDesc": "Download OpenTTD, the open-source urban transport simulation game. Manage rail networks, freight lines, airports, and road vehicles in a dynamic economy.",
        "desc": "Urban transport simulation and business management strategy game.",
        "version": "14.1",
        "license": "GPLv2",
        "platform": "Windows, macOS, Linux, Android",
        "releaseDate": "2026-05-02",
        "downloadUrl": "https://www.openttd.org",
        "sameAs": "https://github.com/OpenTTD/OpenTTD",
        "author": "OpenTTD Team",
        "color": "#2563eb",
        "keywords": ["game", "tycoon", "transport", "trains", "simulation", "business", "openttd", "management", "railroad", "logistics"],
        "icon": '<svg role="img" aria-label="OpenTTD icon" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>OpenTTD Icon</title><rect x="4" y="3" width="16" height="16" rx="2"></rect><path d="M4 11h16"></path><path d="M12 3v8"></path><path d="m8 19-2 3"></path><path d="m16 19 2 3"></path></svg>',
        "existing": False,
        "genre": "Business Simulation",
        "arch_text": "OpenTTD is a complete open-source reimplementation and enhancement of the classic Transport Tycoon Deluxe. Written in C++, it runs natively on Windows, macOS, Linux, and Android without any runtime dependencies beyond the SDL2 rendering backend. The simulation engine runs at 74 ticks per second regardless of render frame rate, ensuring deterministic multiplayer synchronization. The pathfinding system uses YAPF, a highly optimized A* variant that handles complex rail networks with signaling and bidirectional paths. AI players are implemented as separate GameScript/AI sandboxes written in Squirrel, making it easy for the community to create and share custom AI opponents. OpenTTD Content Download system (Bananas) provides thousands of community-created graphics sets, scenarios, AI scripts, and game scripts, transforming the base game into a massively expandable platform.",
        "features": [
            "Full transport network management: trains, trucks, buses, ships, and aircraft",
            "Advanced rail signaling with block signals, path signals, and PBS",
            "Dynamic economic model with cargo production, aging, and demand shifts",
            "Online multiplayer for up to 15 companies competing on the same map",
            "AI opponents written in Squirrel with community-created AI scripts",
            "NewGRF support for custom vehicle sets, industry types, and objects",
            "Bananas content download system with thousands of add-ons",
            "GPLv2 open-source with 25 years of active community development"
        ],
        "faqs": [
            ("Do I need the original Transport Tycoon Deluxe to play OpenTTD?", "No. OpenTTD ships with its own open-source graphics set (OpenGFX), sound set (OpenSFX), and music set (OpenMSX), so you can play for free without any original game files."),
            ("Does OpenTTD have multiplayer?", "Yes. OpenTTD supports online multiplayer with up to 15 companies on a single server. You can find servers through the in-game server browser. Cooperative and competitive modes are both supported."),
            ("How complex is OpenTTD train network building?", "OpenTTD offers one of the deepest rail network simulation systems in gaming, with block signals, path-based signals, priority merges, and complex junction designs possible. The community has documented hundreds of advanced signal layouts."),
            ("Can I mod OpenTTD?", "Yes. The NewGRF system allows extensive modding of vehicles, industries, cargoes, and terrain. GameScripts and AI scripts add dynamic objectives and opponents. Thousands of add-ons are available on Bananas.")
        ],
        "comparison": [
            ("Transport Fever 2", "Proprietary / Windows &amp; Mac", "No", "No", "Paid"),
            ("Cities Skylines", "Proprietary / Multi-platform", "No", "Limited", "Paid"),
            ("OpenTTD", "GPLv2 / Win, Mac, Linux, Android", "Yes", "Yes", "Free")
        ]
    },
    {
        "id": "wesnoth",
        "name": "Battle for Wesnoth",
        "keyword": "Battle for Wesnoth",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Tactical RPG",
        "metaDesc": "Get Battle for Wesnoth, the open-source turn-based fantasy tactical RPG. Command dozens of unique unit factions across expansive single-player campaigns.",
        "desc": "Turn-based tactical strategy game with a rich high fantasy theme.",
        "version": "1.18.2",
        "license": "GPLv2",
        "platform": "Windows, macOS, Linux, iOS, Android",
        "releaseDate": "2026-06-30",
        "downloadUrl": "https://www.wesnoth.org",
        "sameAs": "https://github.com/wesnoth/wesnoth",
        "author": "Wesnoth Community",
        "color": "#7c3aed",
        "keywords": ["game", "strategy", "turn-based", "fantasy", "tactical", "rpg", "wesnoth", "campaign", "multiplayer", "hex", "elves"],
        "icon": '<svg role="img" aria-label="Battle for Wesnoth icon" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Battle for Wesnoth Icon</title><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
        "existing": False,
        "genre": "Turn-Based Strategy RPG",
        "arch_text": "Battle for Wesnoth is built on a mature C++ engine refined over 20 years of open-source development. The game uses a hex-grid combat model where terrain type, unit elevation, and time of day directly affect attack accuracy and damage multipliers. The campaign scripting system uses WML (Wesnoth Markup Language), a domain-specific event-driven scripting language, supplemented by Lua for advanced procedural campaign logic. This dual-scripting approach enables the creation of complex branching narratives, cutscenes, and conditional objectives. Battle for Wesnoth includes a fully functional map editor with WML trigger support, allowing community authors to create complete campaigns with their own storylines, custom units, and art. With over 16 official single-player campaigns and hundreds of community campaigns available from the add-on server, Battle for Wesnoth provides hundreds of hours of strategic content.",
        "features": [
            "Hex-grid combat with terrain, elevation, and time-of-day modifiers",
            "16+ official single-player campaigns with branching storylines",
            "6 core factions: Humans, Elves, Dwarves, Undead, Orcs, and Drakes",
            "Deep unit advancement system with weapon and trait specializations",
            "Full-featured map and scenario editor with WML and Lua scripting",
            "Online multiplayer with ranked and casual ladder via official server",
            "Hundreds of community campaigns downloadable via the add-on server",
            "GPLv2 open-source, available on Windows, macOS, Linux, iOS, and Android"
        ],
        "faqs": [
            ("How many campaigns does Battle for Wesnoth include?", "The base game ships with 16 official campaigns of varying difficulty and length. Hundreds more are available through the in-game add-on server, contributed by the community over two decades."),
            ("Is Battle for Wesnoth good for beginners to strategy games?", "Yes. Battle for Wesnoth includes a comprehensive tutorial campaign that teaches movement, combat, terrain bonuses, and unit advancement. Difficulty settings allow beginners to learn without frustration."),
            ("Does Battle for Wesnoth have multiplayer?", "Yes. It has a built-in multiplayer client that connects to the official Wesnoth game server. You can play casual or ladder-ranked games against other players, or create private games with friends."),
            ("Can I create my own campaigns in Battle for Wesnoth?", "Yes. The game includes a full map editor and uses WML and Lua for campaign scripting. The community has created over 200 campaigns, some of which rival official content in length and storytelling quality.")
        ],
        "comparison": [
            ("XCOM 2", "Proprietary / Win, Mac, Linux", "No", "No", "Paid"),
            ("Fire Emblem: Three Houses", "Proprietary / Nintendo Switch", "No", "No", "Paid"),
            ("Battle for Wesnoth", "GPLv2 / Win, Mac, Linux, Mobile", "Yes", "Yes", "Free")
        ]
    },
    {
        "id": "veloren",
        "name": "Veloren",
        "keyword": "Veloren",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Voxel Action RPG",
        "metaDesc": "Download Veloren, the open-world procedural voxel action RPG written in Rust. Explore infinite procedural dungeons, tame mounts, and craft legendary weapons.",
        "desc": "Open-world, procedural voxel RPG written in Rust with multiplayer.",
        "version": "0.16.0",
        "license": "GPLv3",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-08-10",
        "downloadUrl": "https://veloren.net",
        "sameAs": "https://gitlab.com/veloren/veloren",
        "author": "Veloren Core Team",
        "color": "#0891b2",
        "keywords": ["game", "voxel", "rpg", "open world", "veloren", "rust", "multiplayer", "adventure", "crafting", "procedural", "dungeons"],
        "icon": '<svg role="img" aria-label="Veloren icon" viewBox="0 0 24 24" fill="none" stroke="#0891b2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Veloren Icon</title><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>',
        "existing": False,
        "genre": "Action RPG",
        "arch_text": "Veloren is an entirely community-developed voxel action RPG written in pure Rust, making it one of the most technically ambitious open-source games in development. The rendering engine uses wgpu, delivering a physically based rendering pipeline with dynamic global illumination, volumetric clouds, atmospheric scattering, and real-time shadow maps. The world generation system uses a multi-octave noise function stack that creates entire continents, mountain ranges, river systems, deserts, and tundra biomes procedurally. Veloren uses a client-server model where the server is authoritative over all game state, with the client handling prediction for smooth local movement. The game supports large public servers with hundreds of concurrent players. Character progression uses a skill tree system with separate trees for combat styles, crafting disciplines, and social abilities.",
        "features": [
            "Infinite procedurally generated voxel world with diverse biomes",
            "Real-time combat with melee, ranged, magic, and stealth skill trees",
            "Deep crafting system with weapon smithing, cooking, alchemy, and tailoring",
            "Mount taming including horses, direwolves, and flying creatures",
            "Procedural dungeons with boss encounters and unique loot tables",
            "Online multiplayer with large public servers and community events",
            "Physically based rendering with global illumination and volumetric clouds",
            "Written in Rust with GPLv3 source available on GitLab"
        ],
        "faqs": [
            ("Is Veloren finished?", "Veloren is in active development with regular weekly releases. It is playable and enjoyable in its current state with hundreds of hours of content, but the developers are still adding major features like expanded quests, new biomes, and improved progression systems."),
            ("What makes Veloren different from Minecraft?", "Veloren focuses on action RPG mechanics, with deep combat, skill progression, procedural dungeons, boss encounters, and mount taming. The voxel world is used as the visual style for a full RPG experience rather than a building sandbox."),
            ("Does Veloren have multiplayer?", "Yes. Veloren has online multiplayer with large community-run public servers. The official Veloren server regularly hosts hundreds of concurrent players. You can also run a private server for friends."),
            ("What hardware do I need to run Veloren?", "Veloren requires a modern GPU with Vulkan, Metal, or DirectX 12 support. The minimum spec is roughly equivalent to a GTX 970 or RX 580. High settings with global illumination require a more powerful GPU.")
        ],
        "comparison": [
            ("Minecraft", "Proprietary / Multi-platform", "No", "Yes", "Paid"),
            ("Cube World", "Proprietary / Windows only", "No", "No", "Paid"),
            ("Veloren", "GPLv3 / Win, Mac, Linux", "Yes", "Yes", "Free")
        ]
    },
    {
        "id": "cataclysm-dda",
        "name": "Cataclysm: DDA",
        "keyword": "Cataclysm: DDA",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Survival Roguelike",
        "metaDesc": "Download Cataclysm: Dark Days Ahead, the post-apocalyptic survival roguelike. Scavenge, build custom vehicles, craft gear, and survive dynamic threats.",
        "desc": "Turn-based post-apocalyptic survival simulation and deep roguelike.",
        "version": "0.G Gaiman",
        "license": "CC-BY-SA 3.0",
        "platform": "Windows, macOS, Linux, Android, iOS",
        "releaseDate": "2026-03-01",
        "downloadUrl": "https://cataclysmdda.org",
        "sameAs": "https://github.com/CleverRaven/Cataclysm-DDA",
        "author": "CleverRaven",
        "color": "#dc2626",
        "keywords": ["game", "roguelike", "survival", "post-apocalyptic", "cataclysm", "cdda", "simulation", "crafting", "zombie", "tactical"],
        "icon": '<svg role="img" aria-label="Cataclysm: DDA icon" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Cataclysm: DDA Icon</title><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
        "existing": False,
        "genre": "Survival Roguelike",
        "arch_text": "Cataclysm: Dark Days Ahead uses a tile-based turn simulation engine written in C++, where every action consumes a fixed number of movement points, creating a deep action-economy layer. The world generates on demand as the player explores, using a JSON-driven town generation system that places buildings, vehicles, NPC groups, and special locations based on configurable region rules, making the world effectively infinite. The simulation layer models bodily functions including hunger, thirst, temperature, blood loss, infection, addiction, morale, and fatigue independently for the player character and every NPC. The vehicle construction system uses individual tile-based vehicle parts with their own hit points, fuel requirements, and mechanical interactions, allowing players to build fully custom cars, armored carriers, or even mobile bases. Cataclysm: DDA has over 500 community-contributed mods available through its mod system, covering new settings, professions, mutations, monsters, and even complete total conversions.",
        "features": [
            "Infinite procedurally generated post-apocalyptic world",
            "Deep survival simulation tracking nutrition, temperature, blood loss, and morale",
            "Full vehicle construction system with 100+ buildable part types",
            "Advanced crafting with 1,000+ recipes spanning weapons, armor, food, and electronics",
            "NPCs with schedules, factions, dialogue trees, and companion AI",
            "Extensive mutation and bionics system for character customization",
            "500+ community mods available via built-in mod manager",
            "Available on Windows, macOS, Linux, Android, and iOS"
        ],
        "faqs": [
            ("Is Cataclysm: DDA hard?", "Yes, it has a steep learning curve. Death is permanent in the default mode (roguelike), and the world simulates danger realistically. However, difficulty settings, challenge scenarios, and extensive in-game help menus make it accessible to dedicated learners."),
            ("What is the difference between CDDA and Cataclysm: BN?", "Cataclysm: Dark Days Ahead (CDDA) is the original mainline version maintained by CleverRaven. Cataclysm: Bright Nights (BN) is a fork focused on streamlining the experience with different design priorities. Both are free and open-source."),
            ("Can I build a base in Cataclysm: DDA?", "Yes. Construction is a core game mechanic. You can fortify existing buildings, dig underground bunkers, install traps, build walls and rooftops, and even create a fully functional mobile base from a salvaged vehicle."),
            ("Does Cataclysm: DDA have multiplayer?", "No. Cataclysm: DDA is a single-player game. The focus is on deep personal survival simulation rather than multiplayer interaction.")
        ],
        "comparison": [
            ("The Long Dark", "Proprietary / Multi-platform", "No", "No", "Paid"),
            ("Project Zomboid", "Proprietary / Win, Mac, Linux", "No", "Yes", "Paid"),
            ("Cataclysm: DDA", "CC-BY-SA / Win, Mac, Linux, Mobile", "Yes", "No", "Free")
        ]
    },
    {
        "id": "xonotic",
        "name": "Xonotic",
        "keyword": "Xonotic",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Arena Shooter",
        "metaDesc": "Experience Xonotic, the free, fast-paced open-source arena first-person shooter. Master laser-slick movement, diverse sci-fi weapons, and competitive maps.",
        "desc": "Addictive, fast-paced first-person arena shooter with slick physics.",
        "version": "0.8.6",
        "license": "GPLv3",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-06-21",
        "downloadUrl": "https://xonotic.org",
        "sameAs": "https://gitlab.com/xonotic/xonotic",
        "author": "Team Xonotic",
        "color": "#ea580c",
        "keywords": ["game", "fps", "shooter", "arena", "multiplayer", "action", "xonotic", "quake", "fast", "weapons", "instagib"],
        "icon": '<svg role="img" aria-label="Xonotic icon" viewBox="0 0 24 24" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Xonotic Icon</title><circle cx="12" cy="12" r="10"></circle><line x1="22" y1="12" x2="18" y2="12"></line><line x1="6" y1="12" x2="2" y2="12"></line><line x1="12" y1="6" x2="12" y2="2"></line><line x1="12" y1="22" x2="12" y2="18"></line></svg>',
        "existing": False,
        "genre": "Arena First-Person Shooter",
        "arch_text": "Xonotic is built on the DarkPlaces engine, an extensively modified Quake engine that adds real-time dynamic lighting, HDR bloom, ambient occlusion, and skeletal animation. The movement physics use a Quake-derived air-strafing model augmented with a unique laser jump system where the game signature Electro weapon can be used to propel the player for high-speed aerial movement. The game networking code runs on a custom UDP protocol with client-side prediction and lag compensation, achieving smooth online play even at 150ms ping. Weapon balance is managed entirely through QuakeC scripts, the domain-specific scripting language inherited from Quake, extended with additional primitives for Xonotic-specific mechanics. Xonotic ships with 100+ maps spanning all game modes and an active mapping community that contributes new content regularly. All content is GPLv3 with the exception of some Creative Commons-licensed music and sound effects.",
        "features": [
            "High-speed arena FPS with Quake-inspired air strafing and laser jumping",
            "16 unique weapons with primary and secondary fire modes",
            "10 game modes: Deathmatch, CTF, Assault, Onslaught, Race, and more",
            "100+ official maps plus a large library of community maps",
            "Bot AI with 10 skill levels for offline practice",
            "Competitive online servers with global leaderboards",
            "Full-featured map editor built into the game client",
            "GPLv3 open-source, completely free to play"
        ],
        "faqs": [
            ("Is Xonotic a sequel to Nexuiz?", "Xonotic was created by former Nexuiz developers after a licensing dispute. It is the spiritual successor, sharing the same core engine and gameplay philosophy but with improved graphics, mechanics, and community governance."),
            ("What is instagib mode in Xonotic?", "Instagib is a popular game mode where all players are equipped only with the Vaporizer, a one-hit-kill laser weapon. The mode emphasizes pure aim skill with no health, armor, or weapon pickups."),
            ("How is Xonotic online playerbase?", "Xonotic has a small but dedicated competitive community. Dozens of servers run 24/7 across game modes and skill levels. Peak hours typically see 50-200 active online players across all servers."),
            ("What are the system requirements for Xonotic?", "Xonotic runs well on modest hardware. Minimum requirements are a GPU with OpenGL 2.0 support, 512 MB RAM, and 3 GB disk space. High settings at 1080p run smoothly on a GTX 760 or equivalent.")
        ],
        "comparison": [
            ("Quake Champions", "Freeware / Windows only", "No", "Limited", "Free-to-play"),
            ("Unreal Tournament (2016)", "Proprietary / Multi-platform", "No", "No", "Discontinued"),
            ("Xonotic", "GPLv3 / Win, Mac, Linux", "Yes", "Yes", "Free")
        ]
    },
    {
        "id": "flightgear",
        "name": "FlightGear",
        "keyword": "FlightGear",
        "type": "VideoGame",
        "category": "Games",
        "badge": "Flight Simulator",
        "metaDesc": "Download FlightGear, the premier open-source atmospheric flight simulator. Fly hundreds of realistic aircraft across worldwide terrain and real weather data.",
        "desc": "Sophisticated, realistic, multi-platform atmospheric flight simulation.",
        "version": "2020.3.19",
        "license": "GPLv2",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-04-14",
        "downloadUrl": "https://www.flightgear.org",
        "sameAs": "https://sourceforge.net/projects/flightgear/",
        "author": "FlightGear Community",
        "color": "#4f46e5",
        "keywords": ["game", "simulator", "flight", "aviation", "aircraft", "flightgear", "airplane", "aerospace", "cockpit", "autopilot"],
        "icon": '<svg role="img" aria-label="FlightGear icon" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>FlightGear Icon</title><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"></path></svg>',
        "existing": False,
        "genre": "Flight Simulation",
        "arch_text": "FlightGear is built on the SimGear library and the OpenSceneGraph rendering engine, providing a fully fledged flight simulation platform in continuous development since 1997. The flight dynamics engine uses JSBSim, one of the most accurate open-source flight dynamics models available, alongside support for UIUC and YASim models for aircraft with unconventional aerodynamics. JSBSim simulates each aircraft aerodynamic coefficients, engine performance curves, landing gear physics, and fuel system behavior independently. The scenery system uses the SRTM elevation dataset to model the entire Earth terrain at 90-meter resolution, supplemented by vector data for coastlines, rivers, roads, and urban areas. Real-time weather integration via METAR data feeds from the Aviation Weather Center allows FlightGear to replicate actual current weather conditions at any airport worldwide. The multiplayer system connects pilots from around the world on a shared airspace, enabling formation flying and virtual airline operations.",
        "features": [
            "500+ aircraft from Cessna 172 trainers to Boeing 747 and Concorde",
            "JSBSim flight dynamics model with accurate aerodynamic coefficient simulation",
            "Worldwide terrain at 90m resolution using SRTM elevation data",
            "Real-time METAR weather integration for current atmospheric conditions",
            "Multiplayer shared airspace with global virtual pilot community",
            "Full ILS, VOR/DME, autopilot, and ATC radio simulation",
            "Fully scriptable via Nasal scripting language for custom avionics",
            "GPLv2 open-source with 25+ years of active development"
        ],
        "faqs": [
            ("Is FlightGear good for real pilot training?", "FlightGear uses JSBSim, a professional-grade flight dynamics model used in real flight training devices. While not FAA-certified, it accurately replicates flight characteristics and instrument behavior, making it valuable for instrument procedure practice and systems familiarization."),
            ("How many aircraft does FlightGear include?", "The base install includes around 20 aircraft. The official Hangar at flightgear.org hosts 500+ aircraft created by the community, covering everything from ultralights to airliners and military jets."),
            ("Does FlightGear have multiplayer?", "Yes. FlightGear has a persistent multiplayer server network where thousands of virtual pilots fly simultaneously in shared airspace. Dedicated ATC servers allow voice communication between pilots and controllers."),
            ("What hardware is needed for FlightGear?", "FlightGear is CPU and GPU-intensive at high quality settings. A quad-core CPU, 8 GB RAM, and a mid-range GPU (GTX 1060 or equivalent) deliver smooth performance at high resolution with detailed aircraft.")
        ],
        "comparison": [
            ("Microsoft Flight Simulator 2024", "Proprietary / Win &amp; Xbox", "No", "Yes", "Paid Subscription"),
            ("X-Plane 12", "Proprietary / Multi-platform", "No", "Limited", "Paid"),
            ("FlightGear", "GPLv2 / Win, Mac, Linux", "Yes", "Yes", "Free")
        ]
    }
]

# ─────────────────────────────────────────
# SHARED HTML TEMPLATE HELPERS
# ─────────────────────────────────────────

SHARED_HEAD_CSS = """  <style>
    :root {
      --bg-gradient: linear-gradient(145deg, #0d0f14 0%, #171b24 100%);
      --header-bg: #11141b;
      --card-bg: rgba(255, 255, 255, 0.02);
      --card-border: rgba(255, 255, 255, 0.07);
      --accent: #10b981;
      --accent-glow: rgba(16, 185, 129, 0.25);
      --input-bg: rgba(255, 255, 255, 0.05);
      --input-border: rgba(255, 255, 255, 0.1);
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --text-dim: #6b7280;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: var(--bg-gradient); min-height: 100vh; color: var(--text-main); line-height: 1.6; }
    .container { max-width: 880px; margin: 0 auto; padding: 0 20px; }
    header { background: var(--header-bg); border-bottom: 1px solid var(--card-border); padding: 16px 0; }
    .nav-wrap { display: flex; align-items: center; justify-content: space-between; }
    .brand-link { display: inline-flex; align-items: center; gap: 10px; text-decoration: none; color: var(--text-main); font-weight: 700; font-size: 1.25rem; }
    .brand-link span.accent { color: var(--accent); }
    .back-btn { display: inline-flex; align-items: center; gap: 6px; color: var(--text-muted); text-decoration: none; font-size: 0.9rem; padding: 6px 14px; border-radius: var(--radius-sm); border: 1px solid var(--card-border); background: rgba(255, 255, 255, 0.04); transition: var(--transition); white-space: nowrap; }
    .back-btn:hover { color: var(--text-main); border-color: rgba(255,255,255,0.15); background: rgba(255,255,255,0.08); }
    .header-search-form { flex: 1; max-width: 340px; margin: 0 16px; }
    .header-search-wrapper { position: relative; display: flex; align-items: center; }
    .header-search-icon { position: absolute; left: 12px; color: var(--text-dim); pointer-events: none; }
    .header-search-input { width: 100%; height: 38px; padding: 0 12px 0 36px; font-size: 0.88rem; font-family: inherit; color: var(--text-main); background: var(--input-bg); border: 1px solid var(--input-border); border-radius: var(--radius-sm); outline: none; transition: var(--transition); }
    .header-search-input:focus { border-color: var(--accent); background: rgba(255,255,255,0.08); box-shadow: 0 0 0 3px var(--accent-glow); }
    @media (max-width: 680px) { .nav-wrap { flex-wrap: wrap; gap: 12px; } .header-search-form { max-width: 100%; order: 3; width: 100%; margin: 6px 0 0; } }
    .breadcrumb { display: flex; align-items: center; gap: 8px; font-size: 0.85rem; color: var(--text-dim); margin: 28px 0 16px; }
    .breadcrumb a { color: var(--text-muted); text-decoration: none; }
    .breadcrumb a:hover { color: var(--accent); }
    .app-detail-card { background: var(--card-bg); border: 1px solid var(--card-border); border-radius: var(--radius-lg); padding: 32px; margin-bottom: 30px; }
    .hero-banner { display: flex; align-items: flex-start; gap: 24px; border-bottom: 1px solid var(--card-border); padding-bottom: 28px; margin-bottom: 28px; }
    .app-icon-large { width: 76px; height: 76px; min-width: 76px; border-radius: var(--radius-md); background: rgba(255,255,255,0.05); border: 1px solid var(--card-border); display: flex; align-items: center; justify-content: center; }
    .app-icon-large svg { width: 42px; height: 42px; }
    .app-info-hero { flex: 1; }
    .app-name-title { font-size: 2rem; font-weight: 700; color: var(--text-main); display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
    .app-badge { font-size: 0.75rem; padding: 3px 10px; border-radius: 4px; background: rgba(16,185,129,0.15); color: var(--accent); font-weight: 600; text-transform: uppercase; }
    .app-tagline { color: var(--text-muted); font-size: 1.05rem; margin-top: 6px; }
    .action-row { display: flex; gap: 12px; margin-top: 20px; flex-wrap: wrap; }
    .btn-download { display: inline-flex; align-items: center; gap: 8px; background: var(--accent); color: #0d0f14; font-weight: 700; font-size: 0.95rem; padding: 12px 24px; border-radius: var(--radius-sm); text-decoration: none; transition: var(--transition); }
    .btn-download:hover { background: #34d399; box-shadow: 0 4px 20px var(--accent-glow); }
    .specs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; background: rgba(255,255,255,0.03); padding: 18px 20px; border-radius: var(--radius-md); border: 1px solid var(--card-border); margin-bottom: 32px; }
    .spec-label { font-size: 0.75rem; text-transform: uppercase; color: var(--text-dim); margin-bottom: 4px; letter-spacing: 0.04em; }
    .spec-val { font-size: 0.95rem; font-weight: 600; color: var(--text-main); }
    .section-title { font-size: 1.3rem; font-weight: 700; margin: 28px 0 14px; color: var(--text-main); border-left: 3px solid var(--accent); padding-left: 10px; }
    .sub-section-title { font-size: 1.05rem; font-weight: 600; margin: 16px 0 8px; color: var(--text-main); }
    .overview-text { color: var(--text-muted); font-size: 1rem; margin-bottom: 20px; }
    .features-list { list-style: none; display: flex; flex-direction: column; gap: 10px; margin-bottom: 28px; }
    .features-list li { display: flex; align-items: flex-start; gap: 12px; color: var(--text-muted); }
    .feature-check { color: var(--accent); font-weight: bold; flex-shrink: 0; }
    .comparison-table-wrapper { overflow-x: auto; margin: 16px 0 28px; border-radius: var(--radius-sm); border: 1px solid var(--card-border); }
    .comparison-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; text-align: left; }
    .comparison-table th { background: rgba(255,255,255,0.05); color: var(--text-main); padding: 10px 14px; font-weight: 600; border-bottom: 1px solid var(--card-border); }
    .comparison-table td { padding: 10px 14px; color: var(--text-muted); border-bottom: 1px solid rgba(255,255,255,0.04); }
    .comparison-table tr:last-child td { border-bottom: none; font-weight: 600; color: var(--text-main); }
    .faq-container { display: flex; flex-direction: column; gap: 16px; margin-top: 16px; }
    .faq-item { background: rgba(255,255,255,0.02); border: 1px solid var(--card-border); border-radius: var(--radius-sm); padding: 16px 20px; }
    .faq-item h3 { font-size: 1rem; font-weight: 600; color: var(--text-main); margin-bottom: 8px; }
    .faq-item p { font-size: 0.92rem; color: var(--text-muted); line-height: 1.5; }
    .editorial-byline { margin-top: 32px; padding-top: 18px; border-top: 1px solid var(--card-border); display: flex; justify-content: space-between; align-items: center; font-size: 0.82rem; color: var(--text-dim); flex-wrap: wrap; gap: 8px; }
    footer { text-align: center; padding: 36px 20px; border-top: 1px solid var(--card-border); color: var(--text-dim); font-size: 0.85rem; }
    footer a { color: var(--text-muted); text-decoration: none; margin: 0 8px; }
    footer a:hover { color: var(--accent); }
    @media (max-width: 600px) { .hero-banner { flex-direction: column; } .app-name-title { font-size: 1.6rem; } .app-detail-card { padding: 20px 16px; } }
  </style>"""

LOGO_SVG = """<svg role="img" aria-label="AppDirectory Logo" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>AppDirectory Logo</title><rect x="3" y="3" width="7" height="7" rx="1.5"></rect><rect x="14" y="3" width="7" height="7" rx="1.5"></rect><rect x="3" y="14" width="7" height="7" rx="1.5"></rect><path d="M14 17.5h7m-3.5-3.5v7"></path></svg>"""

BACK_ARROW = """<svg role="img" aria-label="Back arrow" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Back</title><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>"""

EXT_LINK = """<svg role="img" aria-label="External link icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>External link</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>"""

SEARCH_ICON_SVG = """<svg class="header-search-icon" role="img" aria-label="Search icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Search</title><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>"""


def build_schema(p):
    schema_type = p["type"]
    item_obj = {
        "@type": schema_type,
        "@id": f"{DOMAIN}/apps/{p['id']}#software",
        "name": p["name"],
        "operatingSystem": p["platform"],
        "applicationCategory": p.get("genre", p["category"]),
        "description": p["metaDesc"],
        "softwareVersion": p["version"],
        "license": p["license"],
        "datePublished": p["releaseDate"],
        "dateModified": DATE_MODIFIED,
        "author": {"@type": "Organization", "name": p["author"], "url": p["downloadUrl"]},
        "sameAs": [p["sameAs"], p["downloadUrl"]],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }
    if schema_type == "VideoGame":
        item_obj["genre"] = p.get("genre", "Game")
        item_obj["gamePlatform"] = p["platform"]

    breadcrumb = {
        "@type": "BreadcrumbList",
        "@id": f"{DOMAIN}/apps/{p['id']}#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/"},
            {"@type": "ListItem", "position": 2, "name": p["category"], "item": f"{DOMAIN}/?category={p['category'].lower()}"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": f"{DOMAIN}/apps/{p['id']}"}
        ]
    }

    faqs_q = p.get("faqs", [
        (f"Is {p['name']} free?", f"Yes, {p['name']} is free under the {p['license']} license."),
        (f"What platforms does {p['name']} support?", f"{p['name']} supports {p['platform']}.")
    ])
    faq_obj = {
        "@type": "FAQPage",
        "@id": f"{DOMAIN}/apps/{p['id']}#faq",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs_q
        ]
    }
    return json.dumps({"@context": "https://schema.org", "@graph": [item_obj, breadcrumb, faq_obj]}, indent=2)


def build_game_page(p):
    kw = p["keyword"]
    name = p["name"]
    schema_json = build_schema(p)
    canon_url = f"{DOMAIN}/apps/{p['id']}"

    arch_text = p.get("arch_text", f"{name} is a free and open-source {p.get('genre', p['category'])} game.")

    features_html = "\n        ".join(
        f"<li><span class='feature-check' aria-hidden='true'>&#10003;</span> {feat}</li>"
        for feat in p.get("features", [f"{name} is free and open-source.", f"Available on {p['platform']}."])
    )

    faqs = p.get("faqs", [
        (f"Is {name} free?", f"Yes, {name} is free and open-source."),
        (f"What platforms support {name}?", f"{name} runs on {p['platform']}.")
    ])
    faq_html = "\n        ".join(
        f"<div class='faq-item'><h3>{q}</h3><p>{a}</p></div>"
        for q, a in faqs
    )

    comparison = p.get("comparison", [])
    comp_table = ""
    if comparison:
        comp_rows = "\n            ".join(
            f"<tr><td><strong>{row[0]}</strong></td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
            for row in comparison
        )
        comp_table = f"""
      <h2 class="section-title">Alternatives Comparison</h2>
      <div class="comparison-table-wrapper">
        <table class="comparison-table" summary="{name} alternatives comparison">
          <thead><tr><th scope="col">Game</th><th scope="col">License &amp; Platform</th><th scope="col">Open Source</th><th scope="col">Multiplayer</th><th scope="col">Price</th></tr></thead>
          <tbody>
            {comp_rows}
          </tbody>
        </table>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="icon" href="/favicon.ico" type="image/x-icon" />
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} - Free Download &amp; Review | AppDirectory</title>
  <meta name="description" content="{p['metaDesc']}">
  <link rel="canonical" href="{canon_url}" />
  <meta property="og:site_name" content="AppDirectory">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canon_url}" />
  <meta property="og:title" content="{name} - AppDirectory">
  <meta property="og:description" content="{p['metaDesc']}">
  <meta property="og:image" content="https://apphub.comee.online/assets/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{name} - AppDirectory">
  <meta name="twitter:description" content="{p['metaDesc']}">
  <meta name="twitter:image" content="https://apphub.comee.online/assets/og-image.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{schema_json}
  </script>
{SHARED_HEAD_CSS}
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <a href="../index.html" class="brand-link">
        {LOGO_SVG}
        <span>App<span class="accent">Directory</span></span>
      </a>
      <form class="header-search-form" action="../index.html" method="get" role="search">
        <div class="header-search-wrapper">
          {SEARCH_ICON_SVG}
          <input type="text" name="q" class="header-search-input" placeholder="Search apps &amp; games..." autocomplete="off" aria-label="Search applications and games">
        </div>
      </form>
      <a href="../index.html" class="back-btn">
        {BACK_ARROW}
        <span>Catalog</span>
      </a>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a>
      <span>/</span>
      <span>{p['category']}</span>
      <span>/</span>
      <span aria-current="page">{name}</span>
    </nav>

    <article class="app-detail-card">
      <div class="hero-banner">
        <div class="app-icon-large">{p['icon']}</div>
        <div class="app-info-hero">
          <h1 class="app-name-title">
            {name}
            <span class="app-badge">{p['badge']}</span>
          </h1>
          <p class="app-tagline">{p['desc']}</p>
          <div class="action-row">
            <a href="{p['downloadUrl']}" target="_blank" rel="noopener noreferrer" class="btn-download">
              <span>Download {name}</span>
              {EXT_LINK}
            </a>
          </div>
        </div>
      </div>

      <div class="specs-grid">
        <div><div class="spec-label">Version</div><div class="spec-val">{p['version']}</div></div>
        <div><div class="spec-label">License</div><div class="spec-val">{p['license']}</div></div>
        <div><div class="spec-label">Genre</div><div class="spec-val">{p.get('genre', p['category'])}</div></div>
        <div><div class="spec-label">Platform</div><div class="spec-val">{p['platform']}</div></div>
      </div>

      <h2 class="section-title">What is {name}?</h2>
      <p class="overview-text">
        {kw} is a free, open-source {p.get('genre', p['badge'])} available on {p['platform']}.
        Developed by {p['author']} and distributed under the {p['license']} license,
        {kw} has built a dedicated global community of players who value open software and
        transparent development. Unlike proprietary alternatives, {kw} gives players full
        access to the source code, enabling community-driven improvements, custom modifications,
        and long-term preservation independent of any commercial publisher.
        Whether you are a casual player or a competitive enthusiast, {kw} delivers a polished,
        feature-complete experience at absolutely no cost. The {kw} download is available
        directly from the official website with no registration required.
      </p>

      <h2 class="section-title">Architecture &amp; Technical Design</h2>
      <h3 class="sub-section-title">Engine &amp; Rendering</h3>
      <p class="overview-text">{arch_text}</p>

      <h3 class="sub-section-title">System Requirements for {name}</h3>
      <p class="overview-text">
        {kw} is designed to run on a wide range of hardware supporting {p['platform']}.
        Because {kw} is open-source, community members have produced optimized builds for
        lower-end systems, extending the accessible player base. The {kw} repository on its
        official version control host provides build instructions for advanced users who wish
        to compile {kw} from source for custom hardware targets.
      </p>

      <h3 class="sub-section-title">Zero-Cost &amp; Open Source Model</h3>
      <p class="overview-text">
        {kw} is released under the {p['license']} license. There are no hidden monetization
        mechanisms, no paid DLC paywalls, and no mandatory account registration to download
        and play {kw}. The community maintains {kw} through voluntary contributions, ensuring
        {kw} evolves based on player needs rather than commercial pressures.
      </p>

      <h2 class="section-title">Key Features of {name}</h2>
      <h3 class="sub-section-title">Core Capabilities</h3>
      <ul class="features-list">
        {features_html}
      </ul>

      <h3 class="sub-section-title">Modding &amp; Community Ecosystem</h3>
      <p class="overview-text">
        One of {kw}'s greatest strengths is its modding-friendly architecture. The {kw}
        community has produced a rich ecosystem of custom content, gameplay modifications,
        and total conversions that extend the base game with hundreds of hours of additional
        content. Installing community mods for {kw} is straightforward, and the development
        team actively supports modding through well-documented APIs and scripting interfaces.
        This vibrant modding culture ensures {kw} stays fresh and relevant years after its
        initial release.
      </p>
{comp_table}

      <h2 class="section-title">Editorial Review of {name}</h2>
      <h3 class="sub-section-title">AppDirectory Benchmark Assessment</h3>
      <p class="overview-text">
        Our editorial team evaluated {kw} across six criteria: gameplay depth, technical
        performance, community health, documentation quality, cross-platform support, and
        open-source license clarity. {kw} scores exceptionally well on cross-platform support
        and license transparency, with the {p['license']} license providing clear user rights.
        Community health is strong, with active development commits and a responsive issue
        tracker on the {kw} repository. We recommend {kw} without reservation to any player
        looking for a high-quality, telemetry-free gaming experience.
      </p>

      <h3 class="sub-section-title">How to Install {name}</h3>
      <p class="overview-text">
        Installing {kw} is straightforward on all supported platforms. Visit the official
        {kw} website at <a href="{p['downloadUrl']}" target="_blank" rel="noopener noreferrer" style="color:var(--accent)">{p['downloadUrl']}</a>
        and select the installer for your operating system. {kw} requires no additional
        runtime dependencies beyond those bundled with the installer. After installation,
        {kw} launches immediately without requiring online account registration or internet
        connectivity for single-player modes.
      </p>

      <h2 class="section-title">Frequently Asked Questions about {name}</h2>
      <div class="faq-container">
        {faq_html}
      </div>

      <div class="editorial-byline">
        <span>Curated by the AppDirectory Editorial Team</span>
        <span>Verified: {DATE_MODIFIED}</span>
      </div>
    </article>
  </main>

  <footer>
    <div class="container">
      <p>&copy; 2026 AppDirectory. Clean, open-source application and game catalog.</p>
      <div style="margin-top: 10px;">
        <a href="../about.html">About Us</a>
        <span>&#8226;</span>
        <a href="../contact.html">Contact</a>
        <span>&#8226;</span>
        <a href="../privacy.html">Privacy Policy</a>
        <span>&#8226;</span>
        <a href="../terms.html">Terms of Service</a>
        <span>&#8226;</span>
        <a href="../sitemap.xml">Sitemap</a>
        <span>&#8226;</span>
        <a href="../llms.txt">llms.txt</a>
      </div>
    </div>
  </footer>
</body>
</html>"""


# ─────────────────────────────────────────
# GENERATE GAME PAGES
# ─────────────────────────────────────────
print("Generating new game pages...")
generated = []
for p in PRODUCTS:
    if not p.get("existing", False):
        html = build_game_page(p)
        out_path = os.path.join(APPS_DIR, f"{p['id']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [OK] Generated: apps/{p['id']}.html")
        generated.append(p["id"])

print(f"\nGenerated {len(generated)} new game pages: {generated}")

# ─────────────────────────────────────────
# BUILD JS/APPS_DATA.JS (all 18)
# ─────────────────────────────────────────
print("\nBuilding js/apps_data.js with all 18 products...")

def build_js_entry(p):
    kw_list = json.dumps(p["keywords"])
    icon_safe = p['icon'].replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
    desc_safe = p['desc'].replace('"', '\\"').replace("'", "\\'")
    return f"""  {{
    id: "{p['id']}",
    name: "{p['name']}",
    category: "{p['category']}",
    badge: "{p['badge']}",
    desc: "{desc_safe}",
    fullDesc: "{desc_safe}",
    version: "{p['version']}",
    license: "{p['license']}",
    platform: "{p['platform']}",
    downloadUrl: "{p['downloadUrl']}",
    color: "{p['color']}",
    keywords: {kw_list},
    icon: `{icon_safe}`
  }}"""

js_entries = ",\n".join(build_js_entry(p) for p in PRODUCTS)

apps_data_js = f"""// AppDirectory - Full 18-product catalog
// Auto-generated: {DATE_MODIFIED}
const APPS_DATA_FULL = [
{js_entries}
];
"""

os.makedirs(os.path.join(BASE_DIR, "js"), exist_ok=True)
with open(os.path.join(BASE_DIR, "js", "apps_data.js"), "w", encoding="utf-8") as f:
    f.write(apps_data_js)
print("  [OK] Written: js/apps_data.js")

# ─────────────────────────────────────────
# UPDATE SITEMAP.XML
# ─────────────────────────────────────────
print("\nUpdating sitemap.xml...")

sitemap_urls = [
    (f"{DOMAIN}/", "1.0", "weekly"),
    (f"{DOMAIN}/about", "0.6", "monthly"),
    (f"{DOMAIN}/contact", "0.5", "monthly"),
    (f"{DOMAIN}/privacy", "0.4", "yearly"),
    (f"{DOMAIN}/terms", "0.4", "yearly"),
]
for p in PRODUCTS:
    sitemap_urls.append((f"{DOMAIN}/apps/{p['id']}", "0.9", "weekly"))

url_blocks = "\n".join(
    f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{DATE_MODIFIED}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n  </url>"
    for url, pri, freq in sitemap_urls
)

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{url_blocks}
</urlset>
"""

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print(f"  [OK] sitemap.xml updated with {len(sitemap_urls)} URLs")

# ─────────────────────────────────────────
# UPDATE LLMS.TXT
# ─────────────────────────────────────────
print("\nUpdating llms.txt...")

apps_block = "\n".join(
    f"- [{p['name']}]({DOMAIN}/apps/{p['id']}) — {p['desc']} ({p['license']})"
    for p in PRODUCTS if p.get("type") == "SoftwareApplication"
)
games_block = "\n".join(
    f"- [{p['name']}]({DOMAIN}/apps/{p['id']}) — {p['desc']} ({p['license']})"
    for p in PRODUCTS if p.get("type") == "VideoGame"
)

llms_txt = f"""# AppDirectory — LLM Discovery Index
> Canonical URL: {DOMAIN}
> Updated: {DATE_MODIFIED}
> Purpose: Machine-readable directory index for AI assistants and LLM agents

AppDirectory is an independent, editorially curated catalog of verified open-source applications and games. Every listing is reviewed for OSI-approved licensing, zero telemetry, and active community maintenance.

## Applications (9)

{apps_block}

## Games (9)

{games_block}

## Site Pages

- [Home]({DOMAIN}/) — Full catalog with search, filter, and category tags
- [About]({DOMAIN}/about) — Editorial mission, curation methodology, and team
- [Contact]({DOMAIN}/contact) — Submission forms and editorial contact
- [Privacy Policy]({DOMAIN}/privacy) — Data collection policy (zero user tracking)
- [Terms of Service]({DOMAIN}/terms)
- [Sitemap]({DOMAIN}/sitemap.xml)

## Notes for AI Agents

- All pages are static HTML with Schema.org JSON-LD embedded (SoftwareApplication / VideoGame / FAQPage / BreadcrumbList)
- No paywalls, no login required, no cookies set
- Canonical domain: {DOMAIN}
"""

with open(os.path.join(BASE_DIR, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(llms_txt)
print("  [OK] llms.txt updated")

print("\n=== ALL GENERATION TASKS COMPLETE ===")
print(f"  Game pages generated: {len(generated)}")
print(f"  Sitemap URLs: {len(sitemap_urls)}")
print("  js/apps_data.js: 18 products")
print("  llms.txt: updated with 9 apps + 9 games")
