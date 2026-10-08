import plotly.graph_objects as go
import plotly.io as pio

# -------------------------------------------------------------------------
# 1. CHART 1: MASTER ENGINEERING COMPETENCY & VERIFICATION MATRIX
# -------------------------------------------------------------------------
master_data = [
    # Pillar 1: Software & Linux Infrastructure
    {
        "metric": "Docker Container<br> Operations &<br>Execution",
        "pillar": "Software & Linux Infrastructure",
        "verified": 3.0, "upskill": 0.2, "baseline": 3.0, "color": "#38bdf8",
        "evidence": "Containerised simulation environments, runtime diagnostics, reproducible CI/CD pipelines.",
        "tools": "Docker, Bash, Bazel, GitHub Actions",
        "jd_req": "Start/stop containers, diagnostics, rebuild images, stable execution"
    },
    {
        "metric": "Linux CLI &<br>Remote Server<br>Operations",
        "pillar": "Software & Linux Infrastructure",
        "verified": 3, "upskill": 0.2, "baseline": 3.0, "color": "#38bdf8",
        "evidence": "Simulation execution through SSH, automated log filtering, SFTP data retrieval, permission management.",
        "tools": "Linux CLI, SSH, Bash",
        "jd_req": "Connect to remote servers via SSH, and transfer files FTP/SFTP/FTPS"
    },
    {
        "metric": "Python & C/C++<br>Programming",
        "pillar": "Software & Linux Infrastructure",
        "verified": 3.0, "upskill": 0.2, "baseline": 3.0, "color": "#38bdf8",
        "evidence": "High-performance numerical computing, build system integration, telemetry logging.",
        "tools": "VSCode, Python and C/C++ libraries, Bazel, MATLAB/Simulink, Arduino IDE",
        "jd_req": "Follow code structure, interpret build/runtime errors, adjust parameters"
    },
    # Pillar 2: Systems Engineering & V&V
    {
        "metric": "E2E Simulatiors<br>Operations &<br> Validations",
        "pillar": "Systems Engineering & Validation Processes",
        "verified": 3.0, "upskill": 0.3, "baseline": 3.5, "color": "#34d399",
        "evidence": "Software-in-the-loop (SIL) predictive control, sensitivity analysis, non-compliance impact matrix evaluation.",
        "tools": "Waymax SIL, Python, MATLAB/Simulink, W&B",
        "jd_req": "Operate E2E simulators & assess non-compliance on mission performance"
    },
    {
        "metric": "Test Dataset<br>Production &<br> Verification",
        "pillar": "Systems Engineering & Validation Processes",
        "verified": 3.0, "upskill": 0.2, "baseline": 3.0, "color": "#34d399",
        "evidence": "Extraction, synthesis, and validation of large-scale autonomous vehicle scenario trajectory and telemetry datasets.",
        "tools": "Python, NumPy/SciPy, Automated Pipelines, Waymax Simulator",
        "jd_req": "Production and verification of test data sets for performance simulators"
    },
    {
        "metric": "Calibration,<br>Hardware<br>Integration &<br> Anomaly Analysis &<br> Reporting",
        "pillar": "Systems Engineering & Validation Processes",
        "verified": 3.4, "upskill": 0.4, "baseline": 3.0, "color": "#34d399",
        "evidence": "Time-series telemetry anomaly detection, ramp and step-response characterisations",
        "tools": "Python, MATLAB, Weights & Biases",
        "jd_req": "Analyse calibration and characterization campaign data & Identify software anomalies and report "
    },
    {
        "metric": "Requirements &<br>VCB Compliance",
        "pillar": "Systems Engineering & Validation Processes",
        "verified": 2.0, "upskill": 0.5, "baseline": 3.0, "color": "#34d399",
        "evidence": "System verification matrices, SAT and FAT Testing Procedures, formal multi-stakeholder technical reviews.",
        "tools": "Verification Matrices, Git",
        "jd_req": "Support Verification Control Boards (VCB) & compliance tracking"
    },
    # Pillar 3: Payload & Signal Processing
    {
        "metric": "Optical Imager<br>Simulation &<br>Processing",
        "pillar": "Hardware Operations & Signal Processing",
        "verified": 1.5, "upskill": 1.0, "baseline": 3.5, "color": "#fbbf24",
        "evidence": "Proven expertise with optical instruments (Imagers).",
        "tools": "Python, MATLAB/Simulink Image Processing",
        "jd_req": "Expertise with optical instruments (imagers) for simulation & processing"
    },
    {
        "metric": "SAR Signal<br>Processing",
        "pillar": "Hardware Operations & Signal Processing",
        "verified": 2.0, "upskill": 0.5, "baseline": 3.0, "color": "#fbbf24",
        "evidence": "Digital communications link modeling, OFDM signal processing, phase/FFT analysis.",
        "tools": "MATLAB Wireless Comms, FFT",
        "jd_req": "Expertise in the field of Synthetic Aperture Radar (SAR) processing"
    },
]


fig_master = go.Figure()

fig_master.add_trace(
    go.Bar(
        name="Verified Capability",
        x=[d["metric"] for d in master_data],
        y=[d["verified"] for d in master_data],
        marker=dict(
            color=[d["color"] for d in master_data],
            line=dict(color="#111827", width=1.5),
            opacity=0.92,
        ),
        customdata=[
            [d["pillar"], d["evidence"], d["tools"], d["jd_req"], d["verified"] + d["upskill"]]
            for d in master_data
        ],
        hovertemplate=(
            "<b>%{x}</b><br>"
            "<span style='color:#94a3b8'>%{customdata[0]}</span><br><br>"
            "<b>Verified Competance Level:</b> Level %{y:.1f} / 4.0<br>"
            "<b>Active Growth Target (02/27):</b> Level %{customdata[4]:.1f} / 4.0<br>"
            "<b>Key Evidence:</b> %{customdata[1]}<br>"
            "<b>Tools:</b> <span style='font-family:JetBrains Mono,monospace;color:#38bdf8'>%{customdata[2]}</span><br>"
            "<b>JD Requirment/s:</b> <i>%{customdata[3]}</i><extra></extra>"
        ),
    )
)

fig_master.add_trace(
    go.Bar(
        name="Active Upskilling and Research",
        x=[d["metric"] for d in master_data],
        y=[d["upskill"] for d in master_data],
        marker=dict(
            color=[d["color"] for d in master_data],
            opacity=0.25,
            pattern=dict(shape="/", solidity=0.3),
            line=dict(color=[d["color"] for d in master_data], width=1.2),
        ),
        hoverinfo="skip",
    )
)

fig_master.add_trace(
    go.Scatter(
        name="Role Expectation",
        x=[d["metric"] for d in master_data],
        y=[d["baseline"] for d in master_data],
        mode="markers+lines",
        line=dict(color="#f43f5e", width=2, dash="dot"),
        marker=dict(symbol="diamond", size=9, color="#f43f5e", line=dict(color="#ffffff", width=1.2)),
        hovertemplate="<b>%{x}</b><br>JD Target Baseline: Level %{y:.1f}<extra></extra>",
    )
)

fig_master.update_layout(
    barmode="stack",
    bargap=0.34,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#cbd5e1", size=12),
    yaxis=dict(
        title="",
        range=[0, 4.35],
        tickvals=[1, 2, 3, 4],
        ticktext=[
            "<b>L1: Theoretical Knowledge</b><br><span style='font-size:10px;color:#64748b'>Academic grounding, conceptual understanding & observation</span>",
            "<b>L2: Practical Foundation</b><br><span style='font-size:10px;color:#64748b'>Guided execution, basic scripting & procedural operations</span>",
            "<b>L3: Proficient Execution</b><br><span style='font-size:10px;color:#64748b'>Operational competence, system diagnostics & troubleshooting</span>",
            "<b>L4: Advanced Applications</b><br><span style='font-size:10px;color:#64748b'>Full integrations, validation & architectural synthesis</span>",
        ],
        gridcolor="#1e293b",
        zerolinecolor="#334155",
    ),
    xaxis=dict(
        title="",
        tickangle=0,
        tickfont=dict(size=11, color="#e2e8f0"),
        gridcolor="rgba(30, 41, 59, 0.4)",
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom", y=1.04,
        xanchor="right", x=1,
        bgcolor="rgba(17, 24, 39, 0.85)",
        bordercolor="#334155", borderwidth=1,
        font=dict(size=11),
    ),
    hoverlabel=dict(
        bgcolor="#0f172a", bordercolor="#38bdf8",
        font=dict(family="Inter, sans-serif", size=12, color="#f8fafc"),
        align="left",
    ),
    margin=dict(l=175, r=25, t=60, b=65),
    height=520,
)

# -------------------------------------------------------------------------
# 2. PROJECT 1 BREAKDOWN CHART: H-MPC & SIL SIMULATION PIPELINE
# -------------------------------------------------------------------------
proj1_metrics = [
    "Hermetic Build & CI<br>(Bazel / Docker / GH Actions)",
    "High-Performance Numerical Sim<br>(Python / JAX Acceleration)",
    "Multi-Agent Scenario Data<br>(WOMD / Waymax Extraction)",
    "Predictive Control & Thermal<br>(Hierarchical MPC Design)",
    "Cloud Telemetry & Anomaly Log<br>(Weights & Biases MLOps)",
]
proj1_scores = [3.9, 3.8, 3.7, 3.8, 3.7]
proj1_details = [
    "Reproducible monorepo builds in Linux containers with automated CI testing.",
    "JIT-compiled vectorised simulation loops & sensitivity trade evaluations.",
    "Automated parsing, filtering, and validation of multi-agent trajectory arrays.",
    "Coupled energy and battery thermal management under dynamic constraints.",
    "Real-time experiment tracking, constraint violation alerts, and run comparison.",
]

fig_proj1 = go.Figure(
    go.Bar(
        y=proj1_metrics,
        x=proj1_scores,
        orientation="h",
        marker=dict(
            color=["#38bdf8", "#38bdf8", "#34d399", "#34d399", "#818cf8"],
            line=dict(color="#111827", width=1),
            opacity=0.9,
        ),
        customdata=proj1_details,
        text=[f"L{s:.1f}" for s in proj1_scores],
        textposition="inside",
        insidetextanchor="end",
        textfont=dict(family="JetBrains Mono, monospace", size=11, color="#0f172a", weight="bold"),
        hovertemplate="<b>%{y}</b><br>Verified Tier: Level %{x:.1f} / 4.0<br>%{customdata}<extra></extra>",
    )
)

fig_proj1.update_layout(
    bargap=0.32,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#cbd5e1", size=11),
    xaxis=dict(
        range=[0, 4.1],
        tickvals=[1, 2, 3, 4],
        ticktext=["L1: Theory", "L2: Execution", "L3: Diagnostics", "L4: E2E V&V"],
        gridcolor="#1e293b",
        zerolinecolor="#334155",
    ),
    yaxis=dict(autorange="reversed", gridcolor="rgba(0,0,0,0)"),
    hoverlabel=dict(bgcolor="#0f172a", bordercolor="#38bdf8", font=dict(color="#f8fafc")),
    margin=dict(l=185, r=20, t=15, b=35),
    height=300,
)

# -------------------------------------------------------------------------
# 3. PROJECT 2 BREAKDOWN CHART: POWER, CONTROL & RF SIGNAL PROCESSING
# -------------------------------------------------------------------------
proj2_metrics = [
    "Control Loop Modeling & PID<br>(MATLAB / Simulink)",
    "Power Load Flow & Faults<br>(DIgSILENT / PSS SINCAL)",
    "Protection Relay Grading<br>(Compliance & Selectivity)",
    "Industrial Automation V&V<br>(Spark Engineering Placement)",
    "RF Comms & OFDM Channels<br>(Multipath / Signal Processing)",
]
proj2_scores = [3.7, 3.6, 3.5, 3.5, 2.9]
proj2_details = [
    "Transfer function derivation, root-locus stability, step-response characterization.",
    "Newton-Raphson load flow studies and three-phase short-circuit fault analysis.",
    "Time-overcurrent relay coordination and system compliance verification.",
    "60-day industrial placement delivering control engineering & automation evaluations.",
    "Digital communication link modeling, multipath fading channels, and OFDM modulation.",
]

fig_proj2 = go.Figure(
    go.Bar(
        y=proj2_metrics,
        x=proj2_scores,
        orientation="h",
        marker=dict(
            color=["#34d399", "#34d399", "#34d399", "#38bdf8", "#fbbf24"],
            line=dict(color="#111827", width=1),
            opacity=0.9,
        ),
        customdata=proj2_details,
        text=[f"L{s:.1f}" for s in proj2_scores],
        textposition="inside",
        insidetextanchor="end",
        textfont=dict(family="JetBrains Mono, monospace", size=11, color="#0f172a", weight="bold"),
        hovertemplate="<b>%{y}</b><br>Verified Tier: Level %{x:.1f} / 4.0<br>%{customdata}<extra></extra>",
    )
)

fig_proj2.update_layout(
    bargap=0.32,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#cbd5e1", size=11),
    xaxis=dict(
        range=[0, 4.1],
        tickvals=[1, 2, 3, 4],
        ticktext=["L1: Theory", "L2: Practical<br>Foundation", "L3: Proficient<br>Execution", "L4: Advanced<br>Application"],
        gridcolor="#1e293b",
        zerolinecolor="#334155",
    ),
    yaxis=dict(autorange="reversed", gridcolor="rgba(0,0,0,0)"),
    hoverlabel=dict(bgcolor="#0f172a", bordercolor="#fbbf24", font=dict(color="#f8fafc")),
    margin=dict(l=185, r=20, t=15, b=35),
    height=300,
)

# Convert figures to embeddable HTML fragments
chart_master_html = pio.to_html(fig_master, full_html=False, include_plotlyjs="cdn", config={"displaylogo": False})
chart_proj1_html = pio.to_html(fig_proj1, full_html=False, include_plotlyjs=False, config={"displayModeBar": False})
chart_proj2_html = pio.to_html(fig_proj2, full_html=False, include_plotlyjs=False, config={"displayModeBar": False})

# -------------------------------------------------------------------------
# 4. ASSEMBLE FULL SLEEK SPACE-GREY WEB PROSPECTUS (index.html)
# -------------------------------------------------------------------------
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patrick Johnston | Engineering Prospectus</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-space: #090d16;
            --bg-card: #111827;
            --bg-card-alt: #161f33;
            --border-subtle: #1f2937;
            --border-accent: #38bdf8;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-blue: #38bdf8;
            --accent-green: #34d399;
            --accent-amber: #fbbf24;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-color: var(--bg-space);
            background-image: radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.06) 0%, transparent 45%),
                              radial-gradient(circle at 85% 80%, rgba(52, 211, 153, 0.05) 0%, transparent 45%);
            color: var(--text-primary);
            font-family: 'Inter', -apple-system, sans-serif;
            line-height: 1.6;
            padding: 2.5rem 1.5rem 4rem;
        }}
        .container {{
            max-width: 1240px;
            margin: 0 auto;
        }}
        /* Header / Profile Banner */
        .hero-card {{
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.95), rgba(15, 23, 42, 0.9));
            border: 1px solid var(--border-subtle);
            border-top: 2px solid var(--accent-blue);
            border-radius: 14px;
            padding: 2.2rem 2.5rem;
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 2rem;
            align-items: center;
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6);
            margin-bottom: 2rem;
        }}
        .avatar-box {{
            width: 115px;
            height: 115px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            border: 2px solid var(--accent-blue);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'JetBrains Mono', monospace;
            font-size: 2rem;
            font-weight: 700;
            color: var(--accent-blue);
            overflow: hidden;
            flex-shrink: 0;
        }}
        .avatar-box img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .hero-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-bottom: 0.6rem;
        }}
        .badge {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            background: rgba(56, 189, 248, 0.1);
            color: var(--accent-blue);
            border: 1px solid rgba(56, 189, 248, 0.25);
        }}
        .badge.green {{
            background: rgba(52, 211, 153, 0.1);
            color: var(--accent-green);
            border-color: rgba(52, 211, 153, 0.25);
        }}
        .hero-title {{
            font-size: 1.85rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 0.4rem;
        }}
        .hero-subtitle {{
            color: var(--text-secondary);
            font-size: 0.98rem;
            max-width: 880px;
            margin-bottom: 1.1rem;
        }}
        .cli-bar {{
            background: #060911;
            border: 1px solid #1e293b;
            border-radius: 8px;
            padding: 0.55rem 1rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            color: #cbd5e1;
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .cli-prompt {{ color: var(--accent-green); font-weight: 600; }}
        /* Section Cards */
        .section-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 1.8rem 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.45);
        }}
        .section-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            border-bottom: 1px solid var(--border-subtle);
            padding-bottom: 1rem;
            margin-bottom: 1.2rem;
            flex-wrap: wrap;
            gap: 1rem;
        }}
        .section-kicker {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--accent-blue);
            margin-bottom: 0.25rem;
        }}
        .section-title {{
            font-size: 1.35rem;
            font-weight: 600;
        }}
        .section-desc {{
            font-size: 0.88rem;
            color: var(--text-secondary);
        }}
        /* Project Grid */
        .project-grid {{
            display: grid;
            grid-template-columns: 1fr 1.25fr;
            gap: 1.75rem;
            align-items: center;
        }}
        .project-info h4 {{
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            color: #f1f5f9;
        }}
        .project-info p {{
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }}
        .spec-list {{
            list-style: none;
            margin-bottom: 1rem;
        }}
        .spec-list li {{
            font-size: 0.85rem;
            color: #cbd5e1;
            padding: 0.35rem 0;
            border-bottom: 1px dashed rgba(51, 65, 85, 0.5);
            display: flex;
            justify-content: space-between;
        }}
        .spec-label {{
            color: var(--text-secondary);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
        }}
        @media (max-width: 920px) {{
            .hero-card {{ grid-template-columns: 1fr; text-align: left; }}
            .project-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- 1. EXECUTIVE INTRODUCTION BANNER -->
        <header class="hero-card">
            <div class="avatar-box">
                <!-- Tip: Place a photo named profile.jpg in your folder and uncomment the img tag below -->
                <!-- <img src="profile.jpg" alt="Patrick Johnston"> -->
                PJ
            </div>
            <div>
                <div class="hero-meta">
                    <span class="badge">B.Eng (Hons) Electrical & Electronics Engineering</span>
                    <span class="badge green">Docker / Linux / Python / C++</span>
                </div>
                <h1 class="hero-title">Patrick Johnston — Engineering Prospectus</h1>
                <p class="hero-subtitle">
                    Final year Electrical & Electronics Engineering undergraduate with experience in <b>Control and Power Systems Engineering</b>. I have notable technical project based experience in building C/C++ and Python programs, containerised Software in the Loop (SIL) simulation pipelines, and systems compliance and factory acceptance testing verification.
.
                </div>
            </div>
        </header>

        <!-- 2. MASTER COMPETENCY & VERIFICATION MATRIX -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">01 // Technical Skills Overview</div>
                    <h2 class="section-title">Engineering Competency & Operational Readiness Matrix</h2>
                </div>
                <div class="section-desc">
                    Hover over any metric bar to inspect concrete project evidence, tool stack, and JD verification mapping.
                </div>
            </div>
            {chart_master_html}
        </section>

        <!-- 3. PROJECT BREAKDOWN 01: SIL & PREDICTIVE CONTROL -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">02 // Key Project Breakdown — Model Development, Simulation & Software Integrations</div>
                    <h2 class="section-title">Data-Driven Hierarchical MPC & SIL Simulation Framework</h2>
                </div>
                <div class="section-desc">
                    Honours Engineering Thesis | Linux/Docker Conterised CI/CD Simulation Pipeline
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Architecture & Project Scope</h4>
                    <p>
                        Designed and executed a Software in the Loop (SIL) simulation framework evaluating predictive energy and thermal control strategies across multi-agent driving autonomous driving scenarios/trajectories.

                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">EXECUTION ENV</span> <span>Docker + Bazel Monorepo</span></li>
                        <li><span class="spec-label">SIMULATION ENGINE</span> <span>Python / JAX + Waymax Simulator</span></li>
                        <li><span class="spec-label">TEST DATASETS</span> <span>Waymo Open Motion Dataset (WOMD)</span></li>
                        <li><span class="spec-label">TELEMETRY & V&V</span> <span>Weights & Biases + GitHub Actions CI</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj1_html}
                </div>
            </div>
        </section>

        <!-- 4. PROJECT BREAKDOWN 02: POWER, CONTROL & RF PROCESSING -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">03 // Key Project Breakdown — Systems Analysis & Signal Foundations</div>
                    <h2 class="section-title">Control Systems Design, Grid Protection Grading & RF Channel Modeling</h2>
                </div>
                <div class="section-desc">
                    Spark Engineering Placement & Advanced Engineering Coursework
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Project Scope and My Role</h4>
                    <p>
                        Combined industrial control systems engineering placement experience with analytical modeling of electrical power networks, protection compliance, and wireless digital communication links.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">INDUSTRY PLACEMENT</span> <span>Spark Engineering (Control & Automation)</span></li>
                        <li><span class="spec-label">CONTROL & DYNAMICS</span> <span>MATLAB & Simulink (PID / Root Locus)</span></li>
                        <li><span class="spec-label">POWER & PROTECTION</span> <span>DIgSILENT PowerFactory & PSS SINCAL</span></li>
                        <li><span class="spec-label">RF / SIGNAL PHYSICS</span> <span>OFDM, Multipath Fading & FFT Analysis</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj2_html}
                </div>
            </div>
        </section>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Successfully generated full multi-section prospectus: index.html")