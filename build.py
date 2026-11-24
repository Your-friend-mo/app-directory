import os
import json

BASE_DIR = r"c:\Users\m\Documents\app-catalog"
APPS_DIR = os.path.join(BASE_DIR, "apps")
os.makedirs(APPS_DIR, exist_ok=True)

DOMAIN = "https://example.com"
DATE_MODIFIED = "2026-11-23"

APPS = [
    {
        "id": "vscodium",
        "name": "VSCodium",
        "category": "Development",
        "badge": "Code Editor",
        "metaDesc": "Download VSCodium, the telemetry-free binary release of VS Code. Enjoy standard development tools, Git integration, and extensions with total user privacy.",
        "desc": "Telemetry-free open-source binary distributions of VS Code.",
        "fullDesc": "VSCodium is an open-source, community-driven default distribution of Microsoft's editor VS Code with telemetry, tracking, and proprietary code completely disabled. It provides full compatibility with standard development extensions, a built-in terminal, and extensive customization options without sending telemetry data back to corporate servers.",
        "version": "1.92.0",
        "license": "MIT",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-08-15",
        "downloadUrl": "https://vscodium.com",
        "sameAs": "https://github.com/VSCodium/vscodium",
        "author": "VSCodium Contributors",
        "keywords": ["code", "ide", "vscode", "editor", "programming", "developer", "git", "terminal"],
        "features": [
            "100% Free & Open Source under MIT license",
            "Zero tracking, telemetry, or Microsoft proprietary branding",
            "Full compatibility with VS Code extension ecosystem via Open VSX",
            "Integrated Git version control & interactive debugger",
            "Rich multi-language syntax highlighting and IntelliSense"
        ],
        "faq": [
            {"q": "Is VSCodium identical to Microsoft VS Code in features?", "a": "Yes, VSCodium compiles the exact same open-source repository (Code - OSS) with tracking flags disabled and proprietary branding removed."},
            {"q": "Can I install extensions in VSCodium?", "a": "Yes, VSCodium accesses the Open VSX Registry, providing thousands of community-maintained development extensions."}
        ],
        "color": "#2563eb",
        "icon": '<svg role="img" aria-label="VSCodium application icon" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>VSCodium Icon</title><polygon points="16 18 22 12 16 6"></polygon><polygon points="8 6 2 12 8 18"></polygon></svg>'
    },
    {
        "id": "obsidian",
        "name": "Obsidian Notes",
        "category": "Productivity",
        "badge": "Knowledge Base",
        "metaDesc": "Explore Obsidian Notes, the extensible Markdown knowledge base. Build your second brain with local-first bidirectional linking, graph view, and rich plugins.",
        "desc": "Extensible Markdown knowledge base and personal wiki.",
        "fullDesc": "Obsidian is a powerful knowledge base that works on a local folder of plain text Markdown files. It makes note-taking seamless with bi-directional linking, a visual interactive knowledge graph, customizable templates, and hundreds of community plugins for personal knowledge management.",
        "version": "1.6.5",
        "license": "Freeware",
        "platform": "Windows, macOS, Linux, iOS, Android",
        "releaseDate": "2026-07-20",
        "downloadUrl": "https://obsidian.md",
        "sameAs": "https://en.wikipedia.org/wiki/Obsidian_(software)",
        "author": "Dynalist Inc.",
        "keywords": ["notes", "wiki", "markdown", "knowledge", "pkm", "second brain", "graph", "writing"],
        "features": [
            "Local-first storage on your device with zero cloud lock-in",
            "Bi-directional wikilinks and dynamic interactive graph view",
            "Extensible via community themes and community plugins",
            "Canvas workspace for infinite visual brainstorming",
            "Full offline capability with instant indexed text search"
        ],
        "faq": [
            {"q": "Does Obsidian require an account or internet connection?", "a": "No, Obsidian is local-first. Your files are stored as plain Markdown on your local hard drive and work completely offline."},
            {"q": "Can I sync notes across multiple devices?", "a": "You can sync using Obsidian Sync or any free file synchronizer such as Syncthing, Git, or local network folders."}
        ],
        "color": "#7c3aed",
        "icon": '<svg role="img" aria-label="Obsidian Notes application icon" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Obsidian Notes Icon</title><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>'
    },
    {
        "id": "bitwarden",
        "name": "Bitwarden",
        "category": "Security",
        "badge": "Password Vault",
        "metaDesc": "Get Bitwarden, the leading open-source password manager. Secure your sensitive credentials with zero-knowledge AES-256 encryption across all your devices.",
        "desc": "Open-source password manager with zero-knowledge encryption.",
        "fullDesc": "Bitwarden is an open-source password management service that stores sensitive information such as website credentials in an encrypted vault. The platform offers a variety of client applications including a web interface, desktop applications, browser extensions, mobile apps, and a CLI.",
        "version": "2024.7.1",
        "license": "GPLv3",
        "platform": "Cross-platform (All Devices)",
        "releaseDate": "2026-07-28",
        "downloadUrl": "https://bitwarden.com",
        "sameAs": "https://github.com/bitwarden",
        "author": "Bitwarden Inc.",
        "keywords": ["password", "passwords", "vault", "2fa", "authenticator", "credentials", "login", "security", "passkeys"],
        "features": [
            "End-to-end AES-256 bit encryption and zero-knowledge architecture",
            "Secure cross-device syncing across mobile, desktop, and browsers",
            "Built-in two-factor authentication (2FA) authenticator tool",
            "Secure password and passkey generator",
            "Self-hostable backend support for private enterprise servers"
        ],
        "faq": [
            {"q": "Can Bitwarden read my stored passwords?", "a": "No, Bitwarden uses end-to-end zero-knowledge encryption. Only your master password can decrypt your vault."},
            {"q": "Can I host Bitwarden on my own server?", "a": "Yes, Bitwarden provides Docker containers allowing complete self-hosting on your private infrastructure."}
        ],
        "color": "#0284c7",
        "icon": '<svg role="img" aria-label="Bitwarden application icon" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Bitwarden Icon</title><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>'
    },
    {
        "id": "vlc",
        "name": "VLC Media Player",
        "category": "Media",
        "badge": "Audio & Video",
        "metaDesc": "Download VLC Media Player, the open-source cross-platform player. Play virtually all video and audio formats without extra codecs or tracking mechanisms.",
        "desc": "Universal multimedia player supporting virtually all formats.",
        "fullDesc": "VLC is a free and open-source, portable, cross-platform media player software and streaming media server developed by the VideoLAN project. It supports almost all audio and video file formats without needing external codec packs or proprietary software licenses.",
        "version": "3.0.21",
        "license": "GNU LGPL",
        "platform": "Windows, macOS, Linux, Android, iOS",
        "releaseDate": "2026-06-10",
        "downloadUrl": "https://www.videolan.org/vlc/",
        "sameAs": "https://en.wikipedia.org/wiki/VLC_media_player",
        "author": "VideoLAN Project",
        "keywords": ["video", "audio", "player", "movie", "music", "mp4", "mkv", "mp3", "stream", "media"],
        "features": [
            "Plays all formats: Files, Discs, Webcams, Devices, and Streams",
            "Plays most codecs with no codec packs needed: MPEG-2, MPEG-4, H.264, MKV, WebM, MP3",
            "Hardware decoding on all platforms for efficient battery consumption",
            "Advanced subtitle synchronization and video filter controls",
            "Completely free, no spyware, no ads, and no user tracking"
        ],
        "faq": [
            {"q": "Does VLC collect any user data or playback history?", "a": "No, VLC is strictly non-commercial open-source software and does not track playback or collect user data."},
            {"q": "Can VLC play 4K and 8K HDR video files?", "a": "Yes, VLC supports hardware acceleration and modern video codecs including HEVC and AV1."}
        ],
        "color": "#ea580c",
        "icon": '<svg role="img" aria-label="VLC Media Player application icon" viewBox="0 0 24 24" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>VLC Media Player Icon</title><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>'
    },
    {
        "id": "signal",
        "name": "Signal Messenger",
        "category": "Security",
        "badge": "Private Chat",
        "metaDesc": "Get Signal Messenger, the gold standard for private encrypted messaging. Communicate securely with disappearing messages, voice, and HD video group calls.",
        "desc": "Private, state-of-the-art end-to-end encrypted messaging.",
        "fullDesc": "Signal is a cross-platform encrypted messaging service developed by the non-profit Signal Technology Foundation and Signal Messenger LLC. It uses the Internet to send one-to-one and group messages, which can include files, voice notes, images and videos with cryptographic forward secrecy.",
        "version": "7.15.0",
        "license": "GPLv3",
        "platform": "Android, iOS, Windows, macOS, Linux",
        "releaseDate": "2026-08-01",
        "downloadUrl": "https://signal.org",
        "sameAs": "https://github.com/signalapp",
        "author": "Signal Technology Foundation",
        "keywords": ["chat", "messenger", "messaging", "private", "sms", "text", "calling", "encrypted", "communication"],
        "features": [
            "State-of-the-art end-to-end Signal Protocol encryption",
            "No advertising, no affiliate marketers, and zero tracking",
            "Encrypted voice and HD video group calls",
            "Disappearing messages with customizable timers",
            "Screen security protection against unauthorized captures"
        ],
        "faq": [
            {"q": "Who owns Signal?", "a": "Signal is operated by the Signal Foundation, a 501(c)(3) non-profit organization dedicated to privacy and freedom of expression."},
            {"q": "Does Signal store metadata about who I message?", "a": "No, Signal uses Sealed Sender technology so the servers cannot see who is messaging whom."}
        ],
        "color": "#3b82f6",
        "icon": '<svg role="img" aria-label="Signal Messenger application icon" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Signal Messenger Icon</title><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>'
    },
    {
        "id": "7zip",
        "name": "7-Zip Utility",
        "category": "Utilities",
        "badge": "Compression",
        "metaDesc": "Download 7-Zip, the high-performance open-source archiver. Compress and extract files with AES-256 encryption, LZMA2 compression, and shell integration.",
        "desc": "High compression ratio file archiver with AES-256 encryption.",
        "fullDesc": "7-Zip is a free and open-source file archiver, a utility used to place groups of files within compressed containers known as archives. It boasts high compression ratios using the LZMA and LZMA2 compression algorithms with full support for Windows Shell integration.",
        "version": "24.07",
        "license": "GNU LGPL",
        "platform": "Windows, Linux, CLI",
        "releaseDate": "2026-06-19",
        "downloadUrl": "https://www.7-zip.org",
        "sameAs": "https://en.wikipedia.org/wiki/7-Zip",
        "author": "Igor Pavlov",
        "keywords": ["zip", "unzip", "rar", "archive", "compress", "extractor", "tar", "7z", "compression"],
        "features": [
            "High compression ratio in 7z format with LZMA/LZMA2 compression",
            "Supported packing/unpacking: 7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM",
            "Unpacking only: AR, CAB, CHM, CPIO, CramFS, DMG, EXT, FAT, ISO, RAR, RPM, VHD, VMDK",
            "Strong AES-256 encryption in 7z and ZIP formats",
            "Seamless Windows Shell integration and command-line support"
        ],
        "faq": [
            {"q": "Can 7-Zip open RAR files?", "a": "Yes, 7-Zip can unpack and extract files from all modern RAR and RAR5 archives."},
            {"q": "Is 7-Zip free for commercial use?", "a": "Yes, 7-Zip is open-source under GNU LGPL and can be used on commercial computers without licensing fees."}
        ],
        "color": "#16a34a",
        "icon": '<svg role="img" aria-label="7-Zip Utility application icon" viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>7-Zip Utility Icon</title><rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M9 3v18"></path><path d="M14 9h3"></path><path d="M14 15h3"></path></svg>'
    },
    {
        "id": "kdenlive",
        "name": "Kdenlive Video Editor",
        "category": "Media",
        "badge": "Video Editing",
        "metaDesc": "Download Kdenlive, the powerful open-source non-linear video editor. Create multi-track video timelines with color grading, effects, and GPU acceleration.",
        "desc": "Multi-track non-linear video editing suite with hardware acceleration.",
        "fullDesc": "Kdenlive is an acronym for KDE Non-Linear Video Editor. It is a free and open-source video editing software based on the MLT Framework, KDE and Qt. Kdenlive supports all of the formats supported by FFmpeg and provides multi-track editing with unlimited video and audio tracks.",
        "version": "24.05.2",
        "license": "GPLv3",
        "platform": "Windows, macOS, Linux",
        "releaseDate": "2026-07-12",
        "downloadUrl": "https://kdenlive.org",
        "sameAs": "https://github.com/KDE/kdenlive",
        "author": "KDE Community",
        "keywords": ["video", "editor", "editing", "render", "timeline", "clip", "movie", "cut", "multitrack"],
        "features": [
            "Multi-track video and audio timeline editing",
            "Automatic backup and proxy editing for smooth playback of 4K content",
            "Comprehensive audio mixing, keyframing, and spectral analysis",
            "Dozens of effects, color grading wheels, and transition presets",
            "Hardware-accelerated rendering with AV1 and HEVC support"
        ],
        "faq": [
            {"q": "Does Kdenlive add a watermark to exported videos?", "a": "No, Kdenlive is 100% free open-source software and never adds watermarks or limits export resolution."},
            {"q": "Can Kdenlive edit 4K 60FPS video smoothly?", "a": "Yes, using automatic proxy clip generation, Kdenlive allows buttery-smooth playback even on modest hardware."}
        ],
        "color": "#e11d48",
        "icon": '<svg role="img" aria-label="Kdenlive Video Editor application icon" viewBox="0 0 24 24" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Kdenlive Video Editor Icon</title><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>'
    },
    {
        "id": "syncthing",
        "name": "Syncthing",
        "category": "Utilities",
        "badge": "P2P Sync",
        "metaDesc": "Discover Syncthing, the decentralized peer-to-peer file synchronization utility. Sync files securely across your devices with TLS encryption and zero cloud.",
        "desc": "Continuous decentralized peer-to-peer file synchronization.",
        "fullDesc": "Syncthing replaces proprietary sync and cloud services with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.",
        "version": "1.27.9",
        "license": "MPL-2.0",
        "platform": "Windows, macOS, Linux, Android",
        "releaseDate": "2026-07-05",
        "downloadUrl": "https://syncthing.net",
        "sameAs": "https://github.com/syncthing/syncthing",
        "author": "Syncthing Foundation",
        "keywords": ["sync", "synchronization", "backup", "p2p", "cloud", "transfer", "files", "peer"],
        "features": [
            "Decentralized peer-to-peer direct sync between authorized devices",
            "TLS encryption with cryptographic forward secrecy for all communications",
            "No central server or third-party storage holding your data",
            "Automatic conflict detection and file versioning options",
            "Web-based dashboard with bandwidth limiting and detailed status"
        ],
        "faq": [
            {"q": "Where does Syncthing store my synced files?", "a": "Directly in the local folders on your authorized computers and mobile devices. No central cloud server ever touches your data."},
            {"q": "Is the connection between devices encrypted?", "a": "Yes, all communication is secured using TLS with perfect forward secrecy and cryptographic device IDs."}
        ],
        "color": "#0891b2",
        "icon": '<svg role="img" aria-label="Syncthing application icon" viewBox="0 0 24 24" fill="none" stroke="#0891b2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Syncthing Icon</title><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"></path></svg>'
    },
    {
        "id": "hoppscotch",
        "name": "Hoppscotch",
        "category": "Development",
        "badge": "API Client",
        "metaDesc": "Explore Hoppscotch, the lightweight open-source API development ecosystem. Test REST, GraphQL, and WebSocket endpoints quickly with zero local footprint.",
        "desc": "Lightweight, privacy-focused open source API development ecosystem.",
        "fullDesc": "Hoppscotch is a lightweight, web-based API development suite built with speed and simplicity in mind. It allows developers to test REST, GraphQL, WebSocket, Socket.IO, MQTT, and SSE endpoints quickly without resource-heavy desktop clients.",
        "version": "2024.6.0",
        "license": "MIT",
        "platform": "Web, Windows, macOS, Linux",
        "releaseDate": "2026-06-25",
        "downloadUrl": "https://hoppscotch.com",
        "sameAs": "https://github.com/hoppscotch/hoppscotch",
        "author": "Hoppscotch Team",
        "keywords": ["api", "rest", "graphql", "websocket", "postman", "http", "client", "developer", "endpoint"],
        "features": [
            "Instant testing for REST, GraphQL, WebSocket, and SSE endpoints",
            "Lightweight memory footprint and instant startup times",
            "Environments and variable interpolation support",
            "Collections and folder organization for API documentation",
            "Offline-first PWA architecture with local storage support"
        ],
        "faq": [
            {"q": "Can Hoppscotch be used offline?", "a": "Yes, Hoppscotch works as a Progressive Web App (PWA) with complete offline storage for request collections."},
            {"q": "Does Hoppscotch send request data to external analytics?", "a": "No, Hoppscotch is privacy-first and open-source, ensuring sensitive API payloads remain private to your local machine."}
        ],
        "color": "#10b981",
        "icon": '<svg role="img" aria-label="Hoppscotch application icon" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><title>Hoppscotch Icon</title><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>'
    }
]

def generate_header_search(action_path="../index.html"):
    return f"""      <form class="header-search-form" action="{action_path}" method="get" role="search">
        <div class="header-search-wrapper">
          <svg class="header-search-icon" role="img" aria-label="Search icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <title>Search</title>
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input type="text" name="q" class="header-search-input" placeholder="Search applications..." autocomplete="off" aria-label="Search applications">
        </div>
      </form>"""

def get_header_search_css():
    return """
    .header-search-form {
      flex: 1;
      max-width: 340px;
      margin: 0 16px;
    }
    .header-search-wrapper {
      position: relative;
      display: flex;
      align-items: center;
    }
    .header-search-icon {
      position: absolute;
      left: 12px;
      color: var(--text-dim);
      pointer-events: none;
    }
    .header-search-input {
      width: 100%;
      height: 38px;
      padding: 0 12px 0 36px;
      font-size: 0.88rem;
      font-family: inherit;
      color: var(--text-main);
      background: var(--input-bg, rgba(255, 255, 255, 0.05));
      border: 1px solid var(--input-border, rgba(255, 255, 255, 0.1));
      border-radius: var(--radius-sm, 8px);
      outline: none;
      transition: var(--transition, all 0.2s ease);
    }
    .header-search-input:focus {
      border-color: var(--accent, #10b981);
      background: rgba(255, 255, 255, 0.08);
      box-shadow: 0 0 0 3px var(--accent-glow, rgba(16, 185, 129, 0.25));
    }
    @media (max-width: 680px) {
      .nav-wrap { flex-wrap: wrap; gap: 12px; }
      .header-search-form { max-width: 100%; order: 3; width: 100%; margin: 6px 0 0; }
    }
"""

def generate_app_page(app):
    features_html = "".join([f"<li><span class='feature-check' aria-hidden='true'>✓</span> {feat}</li>" for feat in app["features"]])
    faq_html = "".join([f"<div class='faq-item'><h3>{item['q']}</h3><p>{item['a']}</p></div>" for item in app["faq"]])
    
    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "@id": f"{DOMAIN}/apps/{app['id']}.html#software",
                "name": app["name"],
                "operatingSystem": app["platform"],
                "applicationCategory": app["category"],
                "description": app["metaDesc"],
                "softwareVersion": app["version"],
                "license": app["license"],
                "datePublished": app["releaseDate"],
                "dateModified": DATE_MODIFIED,
                "author": {
                    "@type": "Organization",
                    "name": app["author"],
                    "url": app["downloadUrl"]
                },
                "sameAs": [app["sameAs"], app["downloadUrl"]],
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                }
            },
            {
                "@type": "BreadcrumbList",
                "@id": f"{DOMAIN}/apps/{app['id']}.html#breadcrumb",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": f"{DOMAIN}/index.html"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": app["category"],
                        "item": f"{DOMAIN}/index.html?category={app['category'].lower()}"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": app["name"],
                        "item": f"{DOMAIN}/apps/{app['id']}.html"
                    }
                ]
            },
            {
                "@type": "FAQPage",
                "@id": f"{DOMAIN}/apps/{app['id']}.html#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item["q"],
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": item["a"]
                        }
                    } for item in app["faq"]
                ]
            }
        ]
    }, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{app['name']} - App Overview & Download | AppDirectory</title>
  <meta name="description" content="{app['metaDesc']}">
  <link rel="canonical" href="{DOMAIN}/apps/{app['id']}.html">
  
  <!-- Open Graph / Facebook -->
  <meta property="og:site_name" content="AppDirectory">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{DOMAIN}/apps/{app['id']}.html">
  <meta property="og:title" content="{app['name']} - AppDirectory">
  <meta property="og:description" content="{app['metaDesc']}">
  <meta property="og:image" content="{DOMAIN}/assets/og-image.png">
  
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{app['name']} - AppDirectory">
  <meta name="twitter:description" content="{app['metaDesc']}">
  <meta name="twitter:image" content="{DOMAIN}/assets/og-image.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{schema_json}
  </script>
  <style>
    :root {{
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
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg-gradient);
      min-height: 100vh;
      color: var(--text-main);
      line-height: 1.6;
    }}

    .container {{
      max-width: 880px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    header {{
      background: var(--header-bg);
      border-bottom: 1px solid var(--card-border);
      padding: 16px 0;
    }}
    .nav-wrap {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .brand-link {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: var(--text-main);
      font-weight: 700;
      font-size: 1.25rem;
    }}
    .brand-link span.accent {{ color: var(--accent); }}
    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--card-border);
      background: rgba(255, 255, 255, 0.04);
      transition: var(--transition);
      white-space: nowrap;
    }}
    .back-btn:hover {{
      color: var(--text-main);
      border-color: rgba(255, 255, 255, 0.15);
      background: rgba(255, 255, 255, 0.08);
    }}

{get_header_search_css()}

    .breadcrumb {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.85rem;
      color: var(--text-dim);
      margin: 28px 0 16px;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ color: var(--accent); }}

    .app-detail-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-lg);
      padding: 32px;
      margin-bottom: 30px;
    }}

    .hero-banner {{
      display: flex;
      align-items: flex-start;
      gap: 24px;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 28px;
      margin-bottom: 28px;
    }}

    .app-icon-large {{
      width: 76px;
      height: 76px;
      min-width: 76px;
      border-radius: var(--radius-md);
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .app-icon-large svg {{ width: 42px; height: 42px; }}

    .app-info-hero {{ flex: 1; }}
    .app-name-title {{
      font-size: 2rem;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .app-badge {{
      font-size: 0.75rem;
      padding: 3px 10px;
      border-radius: 4px;
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent);
      font-weight: 600;
      text-transform: uppercase;
    }}
    .app-tagline {{
      color: var(--text-muted);
      font-size: 1.05rem;
      margin-top: 6px;
    }}

    .action-row {{
      display: flex;
      gap: 12px;
      margin-top: 20px;
      flex-wrap: wrap;
    }}
    .btn-download {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--accent);
      color: #0d0f14;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 12px 24px;
      border-radius: var(--radius-sm);
      text-decoration: none;
      transition: var(--transition);
    }}
    .btn-download:hover {{
      background: #34d399;
      box-shadow: 0 4px 20px var(--accent-glow);
    }}

    .specs-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      background: rgba(255, 255, 255, 0.03);
      padding: 18px 20px;
      border-radius: var(--radius-md);
      border: 1px solid var(--card-border);
      margin-bottom: 32px;
    }}
    .spec-label {{
      font-size: 0.75rem;
      text-transform: uppercase;
      color: var(--text-dim);
      margin-bottom: 4px;
      letter-spacing: 0.04em;
    }}
    .spec-val {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-main);
    }}

    .section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      margin: 28px 0 14px;
      color: var(--text-main);
      border-left: 3px solid var(--accent);
      padding-left: 10px;
    }}
    .sub-section-title {{
      font-size: 1.05rem;
      font-weight: 600;
      margin: 16px 0 8px;
      color: var(--text-main);
    }}
    .overview-text {{
      color: var(--text-muted);
      font-size: 1rem;
      margin-bottom: 20px;
    }}
    .features-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 28px;
    }}
    .features-list li {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      color: var(--text-muted);
    }}
    .feature-check {{
      color: var(--accent);
      font-weight: bold;
    }}

    .faq-container {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 16px;
    }}
    .faq-item {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--card-border);
      border-radius: var(--radius-sm);
      padding: 16px 20px;
    }}
    .faq-item h3 {{
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 8px;
    }}
    .faq-item p {{
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .editorial-byline {{
      margin-top: 32px;
      padding-top: 18px;
      border-top: 1px solid var(--card-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.82rem;
      color: var(--text-dim);
      flex-wrap: wrap;
      gap: 8px;
    }}

    footer {{
      text-align: center;
      padding: 36px 20px;
      border-top: 1px solid var(--card-border);
      color: var(--text-dim);
      font-size: 0.85rem;
    }}
    footer a {{ color: var(--text-muted); text-decoration: none; margin: 0 8px; }}
    footer a:hover {{ color: var(--accent); }}

    @media (max-width: 600px) {{
      .hero-banner {{ flex-direction: column; }}
      .app-name-title {{ font-size: 1.6rem; }}
      .app-detail-card {{ padding: 20px 16px; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <a href="../index.html" class="brand-link">
        <svg role="img" aria-label="AppDirectory Logo" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <title>AppDirectory Logo</title>
          <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
          <path d="M14 17.5h7m-3.5-3.5v7"></path>
        </svg>
        <span>App<span class="accent">Directory</span></span>
      </a>

{generate_header_search("../index.html")}

      <a href="../index.html" class="back-btn">
        <svg role="img" aria-label="Back arrow" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <title>Back</title>
          <line x1="19" y1="12" x2="5" y2="12"></line>
          <polyline points="12 19 5 12 12 5"></polyline>
        </svg>
        <span>Catalog</span>
      </a>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a>
      <span>/</span>
      <span>{app['category']}</span>
      <span>/</span>
      <span aria-current="page">{app['name']}</span>
    </nav>

    <article class="app-detail-card">
      <div class="hero-banner">
        <div class="app-icon-large">
          {app['icon']}
        </div>
        <div class="app-info-hero">
          <h1 class="app-name-title">
            {app['name']}
            <span class="app-badge">{app['badge']}</span>
          </h1>
          <p class="app-tagline">{app['desc']}</p>
          <div class="action-row">
            <a href="{app['downloadUrl']}" target="_blank" rel="noopener noreferrer" class="btn-download">
              <span>Visit Official Project</span>
              <svg role="img" aria-label="External link icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <title>External link</title>
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                <polyline points="15 3 21 3 21 9"></polyline>
                <line x1="10" y1="14" x2="21" y2="3"></line>
              </svg>
            </a>
          </div>
        </div>
      </div>

      <div class="specs-grid">
        <div>
          <div class="spec-label">Version</div>
          <div class="spec-val">v{app['version']}</div>
        </div>
        <div>
          <div class="spec-label">License</div>
          <div class="spec-val">{app['license']}</div>
        </div>
        <div>
          <div class="spec-label">Category</div>
          <div class="spec-val">{app['category']}</div>
        </div>
        <div>
          <div class="spec-label">Platform</div>
          <div class="spec-val">{app['platform']}</div>
        </div>
      </div>

      <h2 class="section-title">Application Overview & Architecture</h2>
      <p class="overview-text">{app['fullDesc']}</p>

      <h2 class="section-title">Key Capabilities & Features</h2>
      <ul class="features-list">
        {features_html}
      </ul>

      <h2 class="section-title">Frequently Asked Questions</h2>
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
      <p>&copy; 2026 AppDirectory. Clean, open-source application catalog template.</p>
      <div style="margin-top: 10px;">
        <a href="../about.html">About Us</a>
        <span>•</span>
        <a href="../contact.html">Contact</a>
        <span>•</span>
        <a href="../privacy.html">Privacy Policy</a>
        <span>•</span>
        <a href="../terms.html">Terms of Service</a>
        <span>•</span>
        <a href="../sitemap.xml">Sitemap</a>
        <span>•</span>
        <a href="../llms.txt">llms.txt</a>
      </div>
    </div>
  </footer>
</body>
</html>"""

def generate_about_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About AppDirectory - Open Source Editorial Standards</title>
  <meta name="description" content="Learn about AppDirectory, our curation methodology, open-source evaluation standards, and our commitment to telemetry-free software discovery.">
  <link rel="canonical" href="{DOMAIN}/about.html">
  <meta property="og:site_name" content="AppDirectory">
  <meta property="og:title" content="About AppDirectory">
  <meta property="og:description" content="Learn about our curation methodology and commitment to telemetry-free software discovery.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{DOMAIN}/about.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "AboutPage",
    "name": "About AppDirectory",
    "url": "{DOMAIN}/about.html",
    "description": "AppDirectory is a curated independent catalog dedicated to discovering verified open-source applications.",
    "publisher": {{
      "@type": "Organization",
      "name": "AppDirectory",
      "url": "{DOMAIN}"
    }}
  }}
  </script>
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: linear-gradient(145deg, #0d0f14 0%, #171b24 100%);
      color: #f3f4f6;
      line-height: 1.7;
      margin: 0;
      padding: 0 0 40px;
    }}
    .container {{ max-width: 840px; margin: 0 auto; padding: 0 20px; }}
    header {{
      background: #11141b;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      padding: 16px 0;
      margin-bottom: 36px;
    }}
    .nav-wrap {{ display: flex; align-items: center; justify-content: space-between; }}
    .brand-link {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #f3f4f6;
      font-weight: 700;
      font-size: 1.25rem;
    }}
    .brand-link span.accent {{ color: #10b981; }}
    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #9ca3af;
      text-decoration: none;
      font-size: 0.9rem;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.07);
      background: rgba(255, 255, 255, 0.04);
      white-space: nowrap;
    }}
{get_header_search_css()}
    h1 {{ font-size: 2.2rem; margin: 20px 0 10px; color: #10b981; }}
    h2 {{ font-size: 1.35rem; margin-top: 32px; margin-bottom: 12px; color: #f3f4f6; border-left: 3px solid #10b981; padding-left: 10px; }}
    h3 {{ font-size: 1.1rem; margin-top: 20px; margin-bottom: 8px; color: #e5e7eb; }}
    p {{ color: #9ca3af; margin-bottom: 16px; }}
    a {{ color: #10b981; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .stats-box {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 24px 0; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 8px; text-align: center; border: 1px solid rgba(255,255,255,0.08); }}
    .stats-num {{ font-size: 1.8rem; font-weight: 700; color: #10b981; }}
    .stats-lbl {{ font-size: 0.8rem; color: #9ca3af; text-transform: uppercase; }}
  </style>
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <a href="index.html" class="brand-link">
        <svg role="img" aria-label="AppDirectory Logo" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <title>AppDirectory Logo</title>
          <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
          <path d="M14 17.5h7m-3.5-3.5v7"></path>
        </svg>
        <span>App<span class="accent">Directory</span></span>
      </a>
{generate_header_search("index.html")}
      <a href="index.html" class="back-btn">Catalog</a>
    </div>
  </header>
  <div class="container">
    <h1>About AppDirectory</h1>
    <p>AppDirectory is an independent, non-commercial software index providing transparent discovery of verified open-source, privacy-respecting applications for desktop and mobile operating systems.</p>
    
    <div class="stats-box">
      <div>
        <div class="stats-num">100%</div>
        <div class="stats-lbl">Telemetry-Free Curation</div>
      </div>
      <div>
        <div class="stats-num">9</div>
        <div class="stats-lbl">Audited Core Tools</div>
      </div>
      <div>
        <div class="stats-num">0</div>
        <div class="stats-lbl">Affiliate / Gated Locks</div>
      </div>
    </div>

    <h2>Our Mission & Standards</h2>
    <p>Modern software ecosystems are increasingly crowded with proprietary tracking, bundled adware, and opaque data collection policies. AppDirectory was founded to provide developers, privacy advocates, and everyday users with an accessible directory of software where source code is verifiable and user rights are prioritized.</p>

    <h3>Curation Criteria</h3>
    <p>Every tool featured on AppDirectory must satisfy three rigorous baseline criteria: verifiable license status under recognized OSI/Fsf licenses, active development maintenance within the past 12 months, and absence of dark patterns or mandatory telemetry.</p>

    <h2>Editorial Independence</h2>
    <p>We do not accept sponsored placements, paid rankings, or promotional compensation. All project descriptions are authored by our editorial contributors with direct references to official repositories.</p>
  </div>
</body>
</html>"""

def generate_contact_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact & Software Submissions - AppDirectory</title>
  <meta name="description" content="Contact the AppDirectory team, report outdated software listings, or submit your open-source application project for independent editorial evaluation.">
  <link rel="canonical" href="{DOMAIN}/contact.html">
  <meta property="og:site_name" content="AppDirectory">
  <meta property="og:title" content="Contact AppDirectory">
  <meta property="og:description" content="Contact the AppDirectory team, report outdated software listings, or submit your open-source application project for independent editorial evaluation.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{DOMAIN}/contact.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ContactPage",
    "name": "Contact AppDirectory",
    "url": "{DOMAIN}/contact.html",
    "description": "Contact the editorial board or submit software to AppDirectory.",
    "datePublished": "2026-08-15",
    "dateModified": "{DATE_MODIFIED}",
    "publisher": {{
      "@type": "Organization",
      "name": "AppDirectory",
      "url": "{DOMAIN}"
    }}
  }}
  </script>
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: linear-gradient(145deg, #0d0f14 0%, #171b24 100%);
      color: #f3f4f6;
      line-height: 1.7;
      margin: 0;
      padding: 0 0 40px;
    }}
    .container {{ max-width: 840px; margin: 0 auto; padding: 0 20px; }}
    header {{
      background: #11141b;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      padding: 16px 0;
      margin-bottom: 36px;
    }}
    .nav-wrap {{ display: flex; align-items: center; justify-content: space-between; }}
    .brand-link {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #f3f4f6;
      font-weight: 700;
      font-size: 1.25rem;
    }}
    .brand-link span.accent {{ color: #10b981; }}
    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #9ca3af;
      text-decoration: none;
      font-size: 0.9rem;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.07);
      background: rgba(255, 255, 255, 0.04);
      white-space: nowrap;
    }}
{get_header_search_css()}
    h1 {{ font-size: 2.2rem; margin: 20px 0 10px; color: #10b981; }}
    h2 {{ font-size: 1.35rem; margin-top: 32px; margin-bottom: 12px; color: #f3f4f6; border-left: 3px solid #10b981; padding-left: 10px; }}
    h3 {{ font-size: 1.1rem; margin-top: 18px; margin-bottom: 6px; color: #e5e7eb; }}
    p {{ color: #9ca3af; margin-bottom: 16px; }}
    a {{ color: #10b981; text-decoration: none; }}
    .contact-card {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); padding: 24px; border-radius: 8px; margin-top: 20px; }}
  </style>
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <a href="index.html" class="brand-link">
        <svg role="img" aria-label="AppDirectory Logo" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <title>AppDirectory Logo</title>
          <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
          <path d="M14 17.5h7m-3.5-3.5v7"></path>
        </svg>
        <span>App<span class="accent">Directory</span></span>
      </a>
{generate_header_search("index.html")}
      <a href="index.html" class="back-btn">Catalog</a>
    </div>
  </header>
  <div class="container">
    <h1>Contact & Software Submissions</h1>
    <p>Have an open-source tool you would like featured? Found a broken link or outdated version number? Reach out to our editorial team.</p>

    <div class="contact-card">
      <h2>Submission Guidelines & Channels</h2>
      <h3>Software Inquiries & Verification</h3>
      <p>When submitting an application for inclusion, please include:</p>
      <ul style="color: #9ca3af; margin-left: 20px; margin-bottom: 20px;">
        <li>Application Name and Primary Website</li>
        <li>Public Repository Link (GitHub, GitLab, Codeberg, etc.)</li>
        <li>Open-source license type (MIT, GPL, Apache, BSD, etc.)</li>
        <li>Brief summary of core features and platform support</li>
      </ul>
      <h3>Direct Inquiries</h3>
      <p><strong>Editorial Inbox:</strong> <a href="mailto:submissions@example.com">submissions@example.com</a></p>
      <p><strong>General Inquiries:</strong> <a href="mailto:contact@example.com">contact@example.com</a></p>
    </div>
  </div>
</body>
</html>"""

def generate_privacy_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy - AppDirectory</title>
  <meta name="description" content="Review the AppDirectory privacy policy. We adhere to strict zero-tracking principles, collecting no personal data, telemetry, or user analytics.">
  <link rel="canonical" href="{DOMAIN}/privacy.html">
  <meta property="og:site_name" content="AppDirectory">
  <meta property="og:title" content="Privacy Policy - AppDirectory">
  <meta property="og:description" content="Review the AppDirectory privacy policy. We adhere to strict zero-tracking principles, collecting no personal data, telemetry, or user analytics.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{DOMAIN}/privacy.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Privacy Policy",
    "url": "{DOMAIN}/privacy.html",
    "description": "AppDirectory privacy policy adhering to strict zero-tracking principles.",
    "datePublished": "2026-08-15",
    "dateModified": "{DATE_MODIFIED}",
    "publisher": {{
      "@type": "Organization",
      "name": "AppDirectory",
      "url": "{DOMAIN}"
    }}
  }}
  </script>
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: linear-gradient(145deg, #0d0f14 0%, #171b24 100%);
      color: #f3f4f6;
      line-height: 1.7;
      margin: 0;
      padding: 0 0 40px;
    }}
    .container {{ max-width: 840px; margin: 0 auto; padding: 0 20px; }}
    header {{
      background: #11141b;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      padding: 16px 0;
      margin-bottom: 36px;
    }}
    .nav-wrap {{ display: flex; align-items: center; justify-content: space-between; }}
    .brand-link {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #f3f4f6;
      font-weight: 700;
      font-size: 1.25rem;
    }}
    .brand-link span.accent {{ color: #10b981; }}
    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #9ca3af;
      text-decoration: none;
      font-size: 0.9rem;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.07);
      background: rgba(255, 255, 255, 0.04);
      white-space: nowrap;
    }}
{get_header_search_css()}
    h1 {{ font-size: 2rem; margin-bottom: 20px; color: #10b981; }}
    h2 {{ font-size: 1.3rem; margin-top: 24px; margin-bottom: 10px; }}
    h3 {{ font-size: 1.05rem; margin-top: 14px; margin-bottom: 6px; color: #e5e7eb; }}
    p {{ color: #9ca3af; margin-bottom: 16px; }}
    a {{ color: #10b981; text-decoration: none; }}
  </style>
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <a href="index.html" class="brand-link">
        <svg role="img" aria-label="AppDirectory Logo" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <title>AppDirectory Logo</title>
          <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
          <path d="M14 17.5h7m-3.5-3.5v7"></path>
        </svg>
        <span>App<span class="accent">Directory</span></span>
      </a>
{generate_header_search("index.html")}
      <a href="index.html" class="back-btn">Catalog</a>
    </div>
  </header>
  <div class="container">
    <h1>Privacy Policy</h1>
    <p>Last updated: {DATE_MODIFIED}</p>
    <h2>1. General Principles</h2>
    <h3>Zero-Data Architecture</h3>
    <p>AppDirectory operates as a static directory for showcasing open-source applications and utility software. We do not require accounts, cookies, or personal tracking tokens.</p>
    <h2>2. Data Collection Standards</h2>
    <h3>Analytics & Third-Party Trackers</h3>
    <p>This static catalog does not collect personal data, perform tracking, use third-party analytics, or sell visitor information to third parties.</p>
    <h2>3. External Project Links</h2>
    <h3>Upstream Repository Policies</h3>
    <p>The applications listed link directly to their respective official open-source repositories and development projects. We encourage you to review their individual privacy policies.</p>
  </div>
</body>
</html>"""

def generate_terms_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms of Service - AppDirectory</title>
  <meta name="description" content="Read the AppDirectory terms of service: guidelines for browsing our curated open-source application catalog, verifying licenses, and accessing code.">
  <link rel="canonical" href="{DOMAIN}/terms.html">
  <meta property="og:site_name" content="AppDirectory">
  <meta property="og:title" content="Terms of Service - AppDirectory">
  <meta property="og:description" content="Read the AppDirectory terms of service: guidelines for browsing our curated open-source application catalog, verifying licenses, and accessing code.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{DOMAIN}/terms.html">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Terms of Service",
    "url": "{DOMAIN}/terms.html",
    "description": "AppDirectory terms of service and acceptable usage guidelines.",
    "datePublished": "2026-08-15",
    "dateModified": "{DATE_MODIFIED}",
    "publisher": {{
      "@type": "Organization",
      "name": "AppDirectory",
      "url": "{DOMAIN}"
    }}
  }}
  </script>
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: linear-gradient(145deg, #0d0f14 0%, #171b24 100%);
      color: #f3f4f6;
      line-height: 1.7;
      margin: 0;
      padding: 0 0 40px;
    }}
    .container {{ max-width: 840px; margin: 0 auto; padding: 0 20px; }}
    header {{
      background: #11141b;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      padding: 16px 0;
      margin-bottom: 36px;
    }}
    .nav-wrap {{ display: flex; align-items: center; justify-content: space-between; }}
    .brand-link {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: #f3f4f6;
      font-weight: 700;
      font-size: 1.25rem;
    }}
    .brand-link span.accent {{ color: #10b981; }}
    .back-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #9ca3af;
      text-decoration: none;
      font-size: 0.9rem;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.07);
      background: rgba(255, 255, 255, 0.04);
      white-space: nowrap;
    }}
{get_header_search_css()}
    h1 {{ font-size: 2rem; margin-bottom: 20px; color: #10b981; }}
    h2 {{ font-size: 1.3rem; margin-top: 24px; margin-bottom: 10px; }}
    h3 {{ font-size: 1.05rem; margin-top: 14px; margin-bottom: 6px; color: #e5e7eb; }}
    p {{ color: #9ca3af; margin-bottom: 16px; }}
    a {{ color: #10b981; text-decoration: none; }}
  </style>
</head>
<body>
  <header>
    <div class="container nav-wrap">
      <a href="index.html" class="brand-link">
        <svg role="img" aria-label="AppDirectory Logo" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <title>AppDirectory Logo</title>
          <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
          <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
          <path d="M14 17.5h7m-3.5-3.5v7"></path>
        </svg>
        <span>App<span class="accent">Directory</span></span>
      </a>
{generate_header_search("index.html")}
      <a href="index.html" class="back-btn">Catalog</a>
    </div>
  </header>
  <div class="container">
    <h1>Terms of Service</h1>
    <p>Last updated: {DATE_MODIFIED}</p>
    <h2>1. Terms of Use</h2>
    <h3>Acceptable Directory Usage</h3>
    <p>By accessing AppDirectory, you agree to use this catalog for discovering software applications in accordance with their respective open-source licenses.</p>
    <h2>2. Intellectual Property Rights</h2>
    <h3>Trademarks & Project Ownership</h3>
    <p>All trademarks, logos, and software titles belong to their respective project maintainers and developers. We do not claim ownership of listed software.</p>
  </div>
</body>
</html>"""

def generate_sitemap(apps):
    urls = [
        {"loc": f"{DOMAIN}/index.html", "priority": "1.0", "changefreq": "weekly"},
        {"loc": f"{DOMAIN}/about.html", "priority": "0.8", "changefreq": "monthly"},
        {"loc": f"{DOMAIN}/contact.html", "priority": "0.7", "changefreq": "monthly"},
        {"loc": f"{DOMAIN}/privacy.html", "priority": "0.5", "changefreq": "yearly"},
        {"loc": f"{DOMAIN}/terms.html", "priority": "0.5", "changefreq": "yearly"}
    ]
    for app in apps:
        urls.append({
            "loc": f"{DOMAIN}/apps/{app['id']}.html",
            "priority": "0.9",
            "changefreq": "weekly"
        })

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for u in urls:
        xml_lines.append(f"""  <url>
    <loc>{u['loc']}</loc>
    <lastmod>{DATE_MODIFIED}</lastmod>
    <changefreq>{u['changefreq']}</changefreq>
    <priority>{u['priority']}</priority>
  </url>""")
    xml_lines.append('</urlset>')
    return "\n".join(xml_lines)

def generate_robots():
    return f"""User-agent: *
Allow: /

# Dedicated AI Search & Agent Crawlers
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: CCBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-User
Allow: /

User-agent: Perplexity-User
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""

def generate_llms_txt(apps):
    lines = [
        "# AppDirectory",
        "> Curated directory of verified open-source and privacy-respecting software applications.",
        "",
        "## Directory Overview",
        "AppDirectory provides transparent access to telemetry-free desktop and mobile applications.",
        f"- [Home Page]({DOMAIN}/index.html): Full searchable directory of curated tools.",
        f"- [About AppDirectory]({DOMAIN}/about.html): Curation standards and editorial guidelines.",
        f"- [Contact & Submissions]({DOMAIN}/contact.html): Suggest software or contact contributors.",
        f"- [Privacy Policy]({DOMAIN}/privacy.html): Our zero-tracking privacy policy.",
        f"- [Terms of Service]({DOMAIN}/terms.html): Open-source directory terms of use.",
        "",
        "## Curated Applications",
    ]
    for app in apps:
        lines.append(f"- [{app['name']}]({DOMAIN}/apps/{app['id']}.html): {app['desc']} ({app['category']} • {app['license']})")

    lines.append("")
    lines.append("## Optional Context & Full Documentation")
    lines.append(f"- [XML Sitemap]({DOMAIN}/sitemap.xml): Machine-readable index of all pages.")
    return "\n".join(lines)

# Rebuild all pages
for app in APPS:
    app_file_path = os.path.join(APPS_DIR, f"{app['id']}.html")
    with open(app_file_path, "w", encoding="utf-8") as f:
        f.write(generate_app_page(app))
    print(f"Generated {app_file_path}")

with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(generate_about_page())
print("Generated about.html")

with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(generate_contact_page())
print("Generated contact.html")

with open(os.path.join(BASE_DIR, "privacy.html"), "w", encoding="utf-8") as f:
    f.write(generate_privacy_page())
print("Generated privacy.html")

with open(os.path.join(BASE_DIR, "terms.html"), "w", encoding="utf-8") as f:
    f.write(generate_terms_page())
print("Generated terms.html")

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(generate_sitemap(APPS))
print("Generated sitemap.xml")

with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(generate_robots())
print("Generated robots.txt")

with open(os.path.join(BASE_DIR, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(generate_llms_txt(APPS))
print("Generated llms.txt")

print("All build files successfully created with functional search.")
