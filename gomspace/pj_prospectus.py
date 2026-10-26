import plotly.graph_objects as go
import plotly.io as pio

# -------------------------------------------------------------------------
# 1. CHART 1: MASTER ENGINEERING COMPETENCY & OPERATIONAL READINESS MATRIX
#    Tailored for: GomSpace — Early-Career RF & Satellite Comms Engineer
# -------------------------------------------------------------------------

master_data = [
    # Pillar 1: RF Subsystems, Link Budgets & SDR Architecture (Target Growth Zone)
    {
        "metric": "Link-Budget &<br>RF-Chain<br>Modelling",
        "pillar": "RF Subsystems, Link Budgets & SDR Architecture",
        "verified": 2.2, "upskill": 1.1, "baseline": 3.0, "color": "#38bdf8",
        "evidence": "EEE electromagnetics, wave propagation & link simulation coursework; building modular Python S/X-band dynamic orbital link-budget engine.",
        "tools": "Python, MATLAB Communications Toolbox, Free-Space/Atmospheric Loss Models",
        "jd_req": "Perform link-budget analysis and RF-chain modelling across frequency bands & mission constraints"
    },
    {
        "metric": "SDR Platforms,<br>Modulation &<br>Onboard DSP",
        "pillar": "RF Subsystems, Link Budgets & SDR Architecture",
        "verified": 2.4, "upskill": 0.9, "baseline": 3.0, "color": "#38bdf8",
        "evidence": "University DSP, FFT spectral analysis, filter design & OFDM/QPSK link modelling; Completed MathWorks Wireless Communications Onramp.",
        "tools": "MATLAB DSP/Comms, Python, SDR Prototyping (GNU Radio / PlutoSDR / USRP Target)",
        "jd_req": "Work with NanoCom radios & SDR platforms; contribute to onboard signal-processing & data-reduction"
    },
    {
        "metric": "RF Front-End<br>Evaluation<br>(UHF/VHF/S/X)",
        "pillar": "RF Subsystems, Link Budgets & SDR Architecture",
        "verified": 1.9, "upskill": 1.1, "baseline": 2.8, "color": "#38bdf8",
        "evidence": "Undergraduate RF/microwave theory, cascaded noise figure (NF), gain & linearity (IIP3) trade-off analysis; targeted UNSW MSc RF coursework.",
        "tools": "MATLAB RF Toolbox, CST / ADS / HFSS (Active MSc Upskilling), Component Datasheets",
        "jd_req": "Assist with evaluation and selection of RF front-end components across UHF, VHF, S-band and X-band"
    },
    {
        "metric": "RF Lab Bench<br>Testing &<br>Troubleshooting",
        "pillar": "RF Subsystems, Link Budgets & SDR Architecture",
        "verified": 2.1, "upskill": 0.9, "baseline": 2.8, "color": "#38bdf8",
        "evidence": "University electronics laboratory diagnostics (oscilloscopes, signal generators, spectral measurements) & industrial hardware fault-finding.",
        "tools": "Spectrum Analysers, Vector Network Analysers (VNA), Signal Generators, Bench Diagnostics",
        "jd_req": "Prepare and carry out laboratory measurements using RF test equipment; troubleshoot RF performance"
    },

    # Pillar 2: Reusable Engineering Tools, HIL/SIL V&V & Test Automation (Core Strength)
    {
        "metric": "Reusable Python &<br>MATLAB Modelling<br>Frameworks",
        "pillar": "Reusable Tooling, HIL/SIL V&V & Automation",
        "verified": 3.3, "upskill": 0.4, "baseline": 3.0, "color": "#34d399",
        "evidence": "Architected modular, vectorized simulation packages (NumPy/SciPy/JAX & MATLAB) for complex non-linear dynamic and multi-constraint systems.",
        "tools": "Python (NumPy, SciPy, JAX, Plotly), MATLAB/Simulink, Modular OOP/Functional Design",
        "jd_req": "Familiarity with MATLAB, Python or similar; help develop reusable RF models, test methods and engineering tools"
    },
    {
        "metric": "HIL / SIL<br>Integration &<br>Automated V&V",
        "pillar": "Reusable Tooling, HIL/SIL V&V & Automation",
        "verified": 3.0, "upskill": 0.5, "baseline": 3.0, "color": "#34d399",
        "evidence": "Built end-to-end Software-in-the-Loop (SIL) verification pipelines and executed industrial Factory/Site Acceptance Testing (FAT/SAT).",
        "tools": "Pytest, Bazel, Docker, GitHub Actions CI/CD, Automated HIL Test Scripting",
        "jd_req": "Support integration, verification and validation of RF subsystems, including HIL and over-the-air testing"
    },

    # Pillar 3: Satellite Systems Engineering, Interfaces & Documentation (Core Strength)
    {
        "metric": "Subsystem<br>Requirements &<br>ECSS Standards",
        "pillar": "Satellite Systems Engineering & Interfaces",
        "verified": 2.9, "upskill": 0.6, "baseline": 2.8, "color": "#fbbf24",
        "evidence": "QFD requirements traceability matrices, industrial interface definitions, and active study of ECSS-E-ST-50 space communications standards.",
        "tools": "Requirements Traceability Matrices, QFD, Interface Control Documents (ICDs), ECSS Standards",
        "jd_req": "Contribute to definition and documentation of RF subsystem requirements, interfaces & mission proposals"
    },
    {
        "metric": "Power, Thermal &<br>Comms Mission<br>Trade-Offs",
        "pillar": "Satellite Systems Engineering & Interfaces",
        "verified": 3.2, "upskill": 0.4, "baseline": 2.8, "color": "#fbbf24",
        "evidence": "Honours thesis on hierarchical predictive energy & thermal management (MPC); Mars habitat power budgeting; H2 electrolyser control systems.",
        "tools": "Model Predictive Control (MPC), Power/Thermal System Modelling, Trade-Off Matrices",
        "jd_req": "Support RF subsystem analysis and technical trade-offs across performance and mission constraints"
    },
    {
        "metric": "Systematic<br>Documentation &<br>Team Collaboration",
        "pillar": "Satellite Systems Engineering & Interfaces",
        "verified": 3.2, "upskill": 0.3, "baseline": 3.0, "color": "#fbbf24",
        "evidence": "Delivered formal verification reports, network diagrams, and cross-disciplinary briefings across industrial automation and academic teams.",
        "tools": "LaTeX, Weights & Biases, Git, Technical Reports, Multidisciplinary Engineering Reviews",
        "jd_req": "Document analyses & test conclusions systematically; collaborate across RF, Hardware & Systems Engineering"
    },
]

fig_master = go.Figure()

fig_master.add_trace(
    go.Bar(
        name="Verified and Self Defined Capability (Current)",
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
            "<b>Verified Competence Level:</b> Level %{y:.1f} / 4.0<br>"
            "<b>18-Month Target (UNSW MSc + Projects):</b> Level %{customdata[4]:.1f} / 4.0<br>"
            "<b>Key Evidence:</b> %{customdata[1]}<br>"
            "<b>Tools & Standards:</b> <span style='font-family:JetBrains Mono,monospace;color:#38bdf8'>%{customdata[2]}</span><br>"
            "<b>GomSpace JD Mapping:</b> <i>%{customdata[3]}</i><extra></extra>"
        ),
    )
)

fig_master.add_trace(
    go.Bar(
        name="18-Month MSc & Project Upskilling Projection",
        x=[d["metric"] for d in master_data],
        y=[d["upskill"] for d in master_data],
        marker=dict(
            color=[d["color"] for d in master_data],
            opacity=0.28,
            pattern=dict(shape="/", solidity=0.32),
            line=dict(color=[d["color"] for d in master_data], width=1.2),
        ),
        hoverinfo="skip",
    )
)

fig_master.add_trace(
    go.Scatter(
        name="GomSpace Early-Career Role Interpreted Expectations",
        x=[d["metric"] for d in master_data],
        y=[d["baseline"] for d in master_data],
        mode="markers+lines",
        line=dict(color="#f43f5e", width=2, dash="dot"),
        marker=dict(symbol="diamond", size=9, color="#f43f5e", line=dict(color="#ffffff", width=1.2)),
        hovertemplate="<b>%{x}</b><br>GomSpace JD Target Baseline: Level %{y:.1f}<extra></extra>",
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
        tickvals=[1, 2, 3, 5],
        ticktext=[
            "<b>L1: Theoretical Knowledge</b><br><span style='font-size:10px;color:#64748b'>Academic grounding, conceptual understanding & observation</span>",
            "<b>L2: Practical Foundation</b><br><span style='font-size:10px;color:#64748b'>Guided execution, basic scripting & lab operations</span>",
            "<b>L3: Proficient Execution</b><br><span style='font-size:10px;color:#64748b'>Applied project competence, reusable modelling & V&V</span>",
            "<b>L4: Advanced Applications</b><br><span style='font-size:10px;color:#64748b'>Production-grade architectures & multi-subsystem synthesis</span>",
        ],
        gridcolor="#1e293b",
        zerolinecolor="#334155",
    ),
    xaxis=dict(
        title="",
        tickangle=0,
        tickfont=dict(size=10.5, color="#e2e8f0"),
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
    "Build & CI<br>(Bazel / Docker / Git Actions)",
    "Reusable Numerical Modelling<br>(Python / MATLAB / JAX)",
    "Multi-Constraint Optimisation<br>(Hierarchical MPC)",
    "Automated V&V & Telemetry<br>(Weights & Biases)",
]
proj1_scores = [3.0, 3.2, 3.6, 3.0]
proj1_details = [
    "Reproducible monorepo builds in Linux containers with automated CI regression testing.",
    "Modular, vectorized simulation architectures directly transferable to RF link & channel modelling.",
    "Coupled energy and thermal management under dynamic constraints—applicable to satellite downlink scheduling.",
    "Systematic experiment tracking, diagnostic logging, and automated model verification.",
]

fig_proj1 = go.Figure(
    go.Bar(
        y=proj1_metrics,
        x=proj1_scores,
        orientation="h",
        marker=dict(
            color=["#34d399", "#38bdf8", "#fbbf24", "#818cf8"],
            line=dict(color="#111827", width=1),
            opacity=0.9,
        ),
        customdata=proj1_details,
        text=[f"<b>L{s:.1f}</b>" for s in proj1_scores],
        textposition="inside",
        insidetextanchor="end",
        textfont=dict(family="JetBrains Mono, monospace", size=11, color="#0f172a"),
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
        ticktext=["L1: Theory", "L2: Practical<br>Foundation", "L3: Proficient<br>Execution", "L4: Advanced<br>Application"],
        gridcolor="#1e293b",
        zerolinecolor="#334155",
    ),
    yaxis=dict(autorange="reversed", gridcolor="rgba(0,0,0,0)"),
    hoverlabel=dict(bgcolor="#0f172a", bordercolor="#38bdf8", font=dict(color="#f8fafc")),
    margin=dict(l=185, r=20, t=15, b=35),
    height=300,
)

# -------------------------------------------------------------------------
# 3. PROJECT 2 BREAKDOWN CHART: INDUSTRIAL CONTROL, NETWORKS & V&V
# -------------------------------------------------------------------------
proj2_metrics = [
    "Systems Verification & Validation<br>(FAT/SAT Compliance)",
    "Control Logic & PLC Integration<br>(Schneider / SCADA)",
    "Hardware-to-Software Interfacing<br>(Field Integration)",
    "Architecture & Interface Documentation",
    "Interdisciplinary Engineering Coordination",
]
proj2_scores = [2.8, 3.2, 2.6, 3.0, 3.0]
proj2_details = [
    "Assisted in FAT and SAT documentation and procedures to verify system<br>compliance with client and design expectations.",
    "Assisted in development of system control logic and HMI systems using Schneider<br>Control Expert and AVEVA Plant SCADA.",
    "Integrated modernised control and communication systems into physical<br>infrastructure.",
    "Developed plant network systems diagrams and systematic interface<br>documentation.",
    "Collaborated across hardware, electrical, and software teams in design and<br>performance validation."
]

fig_proj2 = go.Figure(
    go.Bar(
        y=proj2_metrics,
        x=proj2_scores,
        orientation="h",
        marker=dict(
            color=["#34d399", "#34d399", "#38bdf8", "#fbbf24", "#fbbf24"],
            line=dict(color="#111827", width=1),
            opacity=0.9,
        ),
        customdata=proj2_details,
        text=[f"<b>L{s:.1f}</b>" for s in proj2_scores],
        textposition="inside",
        insidetextanchor="end",
        textfont=dict(family="JetBrains Mono, monospace", size=11, color="#0f172a"),
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

# -------------------------------------------------------------------------
# 4. PROJECT 3 BREAKDOWN CHART: MARS HVAC & POWER SYSTEM DESIGN
# -------------------------------------------------------------------------
proj3_metrics = [
    "Requirements Traceability &<br>QFD Matrix Mapping",
    "Power Budgeting &<br>Efficiency Evaluations",
    "Thermal / Environmental<br>System Modeling",
    "Closed-Loop Resource<br>Management",
    "Technical Feasibility &<br>Concept Validation",
]
proj3_scores = [3.2, 3.4, 3.0, 3.0, 3.0]
proj3_details = [
    "Translated mission requirements into verifiable subsystem engineering metrics.",
    "Managed core design trade-offs of power budgets and thermal dissipation.",
    "Modelled regenerative heat exchange fluid loops and advanced thermal insulation.",
    "Evaluated and proposed complete closed-loop environmental control architecture.",
    "Validated systems feasibility and documented technical trade-offs.",
]

fig_proj3 = go.Figure(
    go.Bar(
        y=proj3_metrics,
        x=proj3_scores,
        orientation="h",
        marker=dict(
            color=["#818cf8", "#38bdf8", "#34d399", "#fbbf24", "#fbbf24"],
            line=dict(color="#111827", width=1),
            opacity=0.9,
        ),
        customdata=proj3_details,
        text=[f"<b>L{s:.1f}</b>" for s in proj3_scores],
        textposition="inside",
        insidetextanchor="end",
        textfont=dict(family="JetBrains Mono, monospace", size=11, color="#0f172a"),
        hovertemplate="<b>%{y}</b><br>Verified Tier: Level %{x:.1f} / 4.0<br>%{customdata}<extra></extra>",
    )
)

fig_proj3.update_layout(
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
    hoverlabel=dict(bgcolor="#0f172a", bordercolor="#818cf8", font=dict(color="#f8fafc")),
    margin=dict(l=185, r=20, t=15, b=35),
    height=300,
)

# -------------------------------------------------------------------------
# 5. PROJECT 4 BREAKDOWN CHART: HMAS OTAMA SUBMARINE SALVAGE
# -------------------------------------------------------------------------
proj4_metrics = [
    "Structural Stabilisation &<br>Buoyancy Control",
    "Complex Recovery<br>& Towage Logistics",
    "Operational Plan<br>Revisions & Execution",
    "Field Operations &<br>Inter-team Coordination",
    "Dynamic Risk Assessment &<br>Environmental Mitigation",
]
proj4_scores = [3.2, 3.0, 3.0, 2.8, 2.6]
proj4_details = [
    "Constructed and secured precision buoyancy systems and<br>integrated structural wet welding repairs.",
    "Implemented secure towage infrastructure and assisted in towage operations.",
    "Engaged in dynamic multi-disciplinary salvage plan adaptation and iterations.",
    "Liaised with the engineering team on specifications and expectations.",
    "Safety and environmental compliance in active ocean conditions.",
]

fig_proj4 = go.Figure(
    go.Bar(
        y=proj4_metrics,
        x=proj4_scores,
        orientation="h",
        marker=dict(
            color=["#34d399", "#38bdf8", "#818cf8", "#fbbf24", "#f43f5e"],
            line=dict(color="#111827", width=1),
            opacity=0.9,
        ),
        customdata=proj4_details,
        text=[f"<b>L{s:.1f}</b>" for s in proj4_scores],
        textposition="inside",
        insidetextanchor="end",
        textfont=dict(family="JetBrains Mono, monospace", size=11, color="#0f172a"),
        hovertemplate="<b>%{y}</b><br>Verified Tier: Level %{x:.1f} / 4.0<br>%{customdata}<extra></extra>",
    )
)

fig_proj4.update_layout(
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
    hoverlabel=dict(bgcolor="#0f172a", bordercolor="#34d399", font=dict(color="#f8fafc")),
    margin=dict(l=185, r=20, t=15, b=35),
    height=300,
)

# Convert figures to embeddable HTML fragments
chart_master_html = pio.to_html(fig_master, full_html=False, include_plotlyjs="cdn", config={"displaylogo": False})
chart_proj1_html = pio.to_html(fig_proj1, full_html=False, include_plotlyjs=False, config={"displayModeBar": False})
chart_proj2_html = pio.to_html(fig_proj2, full_html=False, include_plotlyjs=False, config={"displayModeBar": False})
chart_proj3_html = pio.to_html(fig_proj3, full_html=False, include_plotlyjs=False, config={"displayModeBar": False})
chart_proj4_html = pio.to_html(fig_proj4, full_html=False, include_plotlyjs=False, config={"displayModeBar": False})

# -------------------------------------------------------------------------
# 6. ASSEMBLE FULL SLEEK SPACE-GREY WEB PROSPECTUS (index.html)
# -------------------------------------------------------------------------
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patrick Johnston | GomSpace RF & SatCom Engineering Prospectus</title>
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
        .badge.amber {{
            background: rgba(251, 191, 36, 0.1);
            color: var(--accent-amber);
            border-color: rgba(251, 191, 36, 0.25);
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
            max-width: 940px;
            margin-bottom: 0.5rem;
        }}
        /* Pillar Legend Pills */
        .pillar-legend {{
            display: flex;
            flex-wrap: wrap;
            gap: 1.2rem;
            margin-bottom: 0.8rem;
            padding: 0.6rem 1rem;
            background: rgba(15, 23, 42, 0.6);
            border-radius: 8px;
            border: 1px solid var(--border-subtle);
            font-size: 0.8rem;
            color: var(--text-secondary);
        }}
        .pillar-item {{
            display: flex;
            align-items: center;
            gap: 0.45rem;
        }}
        .dot {{
            width: 10px;
            height: 10px;
            border-radius: 2px;
            display: inline-block;
        }}
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
            max-width: 540px;
        }}
        /* Roadmap Cards */
        .roadmap-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.25rem;
            margin-top: 1rem;
        }}
        .roadmap-box {{
            background: rgba(15, 23, 42, 0.75);
            border: 1px solid var(--border-subtle);
            border-top: 2px solid var(--accent-blue);
            border-radius: 10px;
            padding: 1.25rem;
        }}
        .roadmap-box h4 {{
            font-size: 0.98rem;
            color: #f8fafc;
            margin-bottom: 0.4rem;
        }}
        .roadmap-box .tag {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            color: var(--accent-blue);
            display: block;
            margin-bottom: 0.5rem;
        }}
        .roadmap-box p {{
            font-size: 0.84rem;
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
            .roadmap-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- 1. EXECUTIVE INTRODUCTION BANNER -->
        <header class="hero-card">
            <div class="avatar-box">
                PJ
            </div>
            <div>
                <div class="hero-meta">
                    <span class="badge">B.Eng (Hons) Electrical & Electronic Engineering (Completing Jan 2027)</span>
                    <span class="badge green">Upcoming M.Sc Space Engineering (2027)</span>
                </div>
                <h1 class="hero-title">Patrick Johnston — Engineering Prospectus</h1>
                <p class="hero-subtitle">
                    Final semester Electrical & Electronic Engineering (Honours) undergraduate with 1 year of industry and research experience in <b>performance numerical simulation, control systems, and model verification</b>. Proven capability in translating and accelerating mathematical models using <b>MATLAB, Python (JAX/NumPy), and C/C++</b>, alongside building reproducible, containerised Software in Loop (SIL) CI/CD validation pipelines.
                </p>
            </div>
        </header>

        <!-- 2. MASTER COMPETENCY & VERIFICATION MATRIX -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">01 // Target Role Alignment: Early-Career RF Engineer (Satellite Systems Hardware Team)</div>
                    <h2 class="section-title">Engineering Competency & 18 Month Operational Readiness Matrix</h2>
                </div>
                <div class="section-desc">
                    This matrix maps and aligns my self defined and verified engineering capabilities, and projected upskilling projections directly against GomSpace's Early Career RF Engineer requirements. Hover over any metric bar to view supporting project evidence, tools used, and job description (JD) requirement mapping.
                </div>
            </div>
            <div class="pillar-legend">
                <div class="pillar-item"><span class="dot" style="background:#38bdf8;"></span> <b>Pillar 1:</b> RF Subsystems, Link Budgeting & SDR Architectures</div>
                <div class="pillar-item"><span class="dot" style="background:#34d399;"></span> <b>Pillar 2:</b> HIL/SIL V&V & Automation</div>
                <div class="pillar-item"><span class="dot" style="background:#fbbf24;"></span> <b>Pillar 3:</b> Satellite Systems & ECSS Engineering</div>
            </div>
            {chart_master_html}
        </section>

        <!-- 3. TARGETED 18-MONTH GOMSPACE PROJECT ROADMAP -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">02 // Proactive 14–18 Month R&D Horizon — Master of Space Engineering & Lab Builds</div>
                    <h2 class="section-title">Proposed Project Alignment with GomSpace NanoCom & SDR Platforms</h2>
                </div>
                <div class="section-desc">
                    Candidate research and hardware verification projects designed to bridge industrial control/simulation expertise with nanosatellite RF subsystem engineering.
                </div>
            </div>
            <div class="roadmap-grid">
                <div class="roadmap-box">
                    <span class="tag">CONCEPT A // REUSABLE RF TOOLING</span>
                    <h4>Dynamic Orbital Link-Budget & RF-Chain Engine</h4>
                    <p>Modular Python/MATLAB framework evaluating UHF, S-band, and X-band link margins across dynamic LEO pass geometries, rain/atmospheric attenuation, and cascaded RF front-end NF/IIP3 parameters.</p>
                </div>
                <div class="roadmap-box" style="border-top-color: var(--accent-green);">
                    <span class="tag" style="color: var(--accent-green);">CONCEPT B // HIL BENCH VERIFICATION</span>
                    <h4>SDR Hardware-in-the-Loop (HIL) Verification Testbed</h4>
                    <p>Automated bench validation setup using SDR transceivers, VNA, and Spectrum Analyser to inject synthetic LEO Doppler profiles and channel impairments for BER/EVM verification.</p>
                </div>
                <div class="roadmap-box" style="border-top-color: var(--accent-amber);">
                    <span class="tag" style="color: var(--accent-amber);">CONCEPT C // SYSTEMS & DSP OPTIMISATION</span>
                    <h4>Power-Aware Comms & Onboard Data-Reduction Controller</h4>
                    <p>Extending Hierarchical MPC thesis architecture to schedule high-data-rate S/X-band downlinks and onboard DSP data-reduction routines against real-time nanosatellite solar/battery constraints.</p>
                </div>
            </div>
        </section>

        <!-- 4. PROJECT BREAKDOWN 01: SIL & PREDICTIVE CONTROL -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">03 // Key Project Breakdown — Reusable Simulation Tooling & Automated Verification</div>
                    <h2 class="section-title">Data-Driven Hierarchical MPC & SIL Simulation Framework</h2>
                </div>
                <div class="section-desc">
                    Honours Engineering Thesis | Containerised CI/CD Simulation Pipeline
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Architecture & GomSpace Transferability</h4>
                    <p>
                        Designed and executed a Software-in-the-Loop (SIL) simulation framework evaluating predictive energy and thermal control strategies across multi agent autonomous driving scenarios/trajectories, utilizing vectorized numerical solvers and automated regression testing.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">EXECUTION ENV</span> <span>Docker + Bazel Monorepo</span></li>
                        <li><span class="spec-label">SIMULATION ENGINE</span> <span>MATLAB + Python / JAX Vectorized Solvers</span></li>
                        <li><span class="spec-label">SYSTEM OPTIMISATION</span> <span>Coupled Power & Thermal Constraints</span></li>
                        <li><span class="spec-label">TELEMETRY & V&V</span> <span>Weights & Biases + GitHub Actions CI</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj1_html}
                </div>
            </div>
        </section>

        <!-- 5. PROJECT BREAKDOWN 02: INDUSTRIAL CONTROL & V&V -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">04 // Key Project Breakdown — Hardware-Software Integration & Acceptance Testing</div>
                    <h2 class="section-title">Esperance Grain Terminal Control System Upgrade Project</h2>
                </div>
                <div class="section-desc">
                    Spark Engineering | Control Systems & Network Engineering
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Project Scope and My Role</h4>
                    <p>
                        Facilitated the integration of modernised industrial control and communication systems into physical infrastructure. Executed Factory and Site Acceptance Testing (FAT/SAT) protocols, hardware troubleshooting, and systematic interface documentation across multidisciplinary teams.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">CONTROL LOGIC</span> <span>Schneider Control Expert (Control & Automation)</span></li>
                        <li><span class="spec-label">HMI & SCADA</span> <span>AVEVA Plant SCADA</span></li>
                        <li><span class="spec-label">SYSTEMS V&V</span> <span>FAT & SAT Protocols & Hardware Troubleshooting</span></li>
                        <li><span class="spec-label">DOCUMENTATION</span> <span>Network Systems Auditing & Interface Diagrams</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj2_html}
                </div>
            </div>
        </section>

        <!-- 6. PROJECT BREAKDOWN 03: MARS HVAC & POWER -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">05 // Key Project Breakdown — Space Systems Engineering, Power Budgets & Traceability</div>
                    <h2 class="section-title">Mars Habitat Environmental & Power System Design</h2>
                </div>
                <div class="section-desc">
                    Selective University Engineering Project | Conceptual Modular Mars Surface Habitat
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Project Scope and My Role</h4>
                    <p>
                        Evaluated closed-loop environmental and power management solutions for a modular space habitat, establishing strict power budgets, thermal trade-offs, and Quality Function Deployment (QFD) requirements traceability matrices.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">THERMAL DYNAMICS</span> <span>Regenerative Heat Exchange Fluid Loop & Aerogels</span></li>
                        <li><span class="spec-label">SYSTEMS ENGINEERING</span> <span>QFD & Subsystem Requirements Traceability</span></li>
                        <li><span class="spec-label">CONTROL SYSTEMS</span> <span>Sensor-Driven Feedback Control Architecture</span></li>
                        <li><span class="spec-label">CORE DESIGN CONSTRAINTS</span> <span>Strict Mission Power Budgeting & Trade-Offs</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj3_html}
                </div>
            </div>
        </section>

        <!-- 7. PROJECT BREAKDOWN 04: SALVAGE OPERATION -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">06 // Key Project Breakdown — High-Consequence Field Operations & Risk Mitigation</div>
                    <h2 class="section-title">HMAS OTAMA Submarine Salvage Project</h2>
                </div>
                <div class="section-desc">
                    Aegir Divers | Multi-Disciplinary Marine Recovery Project
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Project Scope and My Role</h4>
                    <p>
                        Supported multi-disciplinary dive and engineering teams in executing the salvage operation of a compromised naval submarine, implementing buoyancy stabilization, wet welding repairs, and dynamic operational plan iterations under high-risk field constraints.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">FIELD OPERATIONS</span> <span>Underwater Salvage & Buoyancy Stabilization</span></li>
                        <li><span class="spec-label">STRUCTURAL ENGINEERING</span> <span>Wet Welding & Mooring Infrastructure Design</span></li>
                        <li><span class="spec-label">RISK MANAGEMENT</span> <span>Environmental & Safety Compliance</span></li>
                        <li><span class="spec-label">PROJECT CONTROL</span> <span>Multi-Disciplinary Operational Plan Iterations</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj4_html}
                </div>
            </div>
        </section>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Successfully generated GomSpace-tailored engineering prospectus: index.html")