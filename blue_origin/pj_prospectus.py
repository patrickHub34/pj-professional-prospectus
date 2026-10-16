import plotly.graph_objects as go
import plotly.io as pio

# -------------------------------------------------------------------------
# 1. CHART 1: MASTER ENGINEERING COMPETENCY & VERIFICATION MATRIX
#    Tailored for: Blue Origin — PAA/DBF DSP Simulation & Verification Engineer
# -------------------------------------------------------------------------
master_data = [
    # Pillar 1: High-Performance Computing & Code Optimization
    {
        "metric": "MATLAB & Python<br>Scientific<br>Computing",
        "pillar": "High-Performance Computing & Code Optimization",
        "verified": 3.2, "upskill": 0.3, "baseline": 3.5, "color": "#38bdf8",
        "evidence": "University simulation coursework, non-linear dynamic modeling, vectorized array operations in NumPy/JAX & MATLAB.",
        "tools": "MATLAB/Simulink, Python, NumPy, SciPy, JAX",
        "jd_req": "Optimize MATLAB & Python simulation models; familiarity with numerical methods & scientific computing"
    },
    {
        "metric": "Code Profiling,<br>Vectorization &<br>Refactoring",
        "pillar": "High-Performance Computing & Code Optimization",
        "verified": 3.0, "upskill": 0.4, "baseline": 3.5, "color": "#38bdf8",
        "evidence": "Refactored monolithic scripts into modular monorepo packages; eliminated Python loops via JAX JIT compilation & array vectorization.",
        "tools": "JAX JIT/vmap, Python Profilers, MATLAB Profiler, Modular Architecture",
        "jd_req": "Profile/benchmark code for bottlenecks; refactor legacy scripts into modular, maintainable codebases"
    },
    {
        "metric": "C/C++ Algorithms<br>& Memory<br>Management",
        "pillar": "High-Performance Computing & Code Optimization",
        "verified": 2.4, "upskill": 0.6, "baseline": 3.5, "color": "#38bdf8",
        "evidence": "Embedded & algorithmic C/C++ programming, data structure selection, static typing, and memory-constrained execution.",
        "tools": "C/C++, GCC/Clang, Data Structures, Memory Allocation, MEX (Active Upskilling)",
        "jd_req": "Implement high-performance C++ algorithms; memory management, data structures & MEX integration"
    },
    {
        "metric": "Parallel Computing<br>& Hardware<br>Acceleration",
        "pillar": "High-Performance Computing & Code Optimization",
        "verified": 2.6, "upskill": 0.6, "baseline": 3.0, "color": "#38bdf8",
        "evidence": "Parallelized batch trajectory simulations and matrix solvers using XLA/JAX vectorization; active study in OpenMP & MATLAB PCT.",
        "tools": "JAX (vmap/pmap), XLA, Multiprocessing, MATLAB Parallel Toolbox (Upskilling)",
        "jd_req": "Explore and integrate parallel computing techniques (MATLAB PCT, OpenMP, MPI)"
    },

    # Pillar 2: Simulation V&V & Software Infrastructure
    {
        "metric": "Unit / Integration<br>Testing & Fidelity<br>Verification",
        "pillar": "Simulation V&V & Software Infrastructure",
        "verified": 3.1, "upskill": 0.3, "baseline": 3.2, "color": "#34d399",
        "evidence": "Automated unit/integration test suites verifying mathematical solver invariants and physical model fidelity pre/post-optimization.",
        "tools": "Pytest, Bazel Test, Regression Benchmarking, FAT/SAT Verification",
        "jd_req": "Develop unit/integration tests to validate model accuracy before and after optimization"
    },
    {
        "metric": "CI/CD Pipelines,<br>Git & Container<br>Environments",
        "pillar": "Simulation V&V & Software Infrastructure",
        "verified": 3.2, "upskill": 0.2, "baseline": 3.0, "color": "#34d399",
        "evidence": "Hermetic monorepo build orchestration, containerized simulation runners, automated GitHub Actions validation workflows.",
        "tools": "Git, GitHub Actions, Docker, Bazel, Linux CLI",
        "jd_req": "Experience with version control (Git) & supporting continuous integration pipelines for model validation"
    },
    {
        "metric": "Technical Docs &<br>Cross-Disciplinary<br>Collaboration",
        "pillar": "Simulation V&V & Software Infrastructure",
        "verified": 3.2, "upskill": 0.2, "baseline": 3.0, "color": "#34d399",
        "evidence": "Authored formal engineering verification reports, benchmarking logs, and interface registers across multi-disciplinary teams.",
        "tools": "Weights & Biases, LaTeX, Markdown, Technical Review Matrices",
        "jd_req": "Collaborate with hardware/RF engineers on physical models; document optimization methodologies & results"
    },

    # Pillar 3: Signal Processing, RF & Physical Modeling
    {
        "metric": "DSP, Spectral<br>Analysis & Comms<br>Modeling",
        "pillar": "Signal Processing, RF & Physical Modeling",
        "verified": 2.3, "upskill": 0.6, "baseline": 3.0, "color": "#fbbf24",
        "evidence": "University EEE coursework in digital signal processing, FFT spectral analysis, filter design, and OFDM link simulation in MATLAB.",
        "tools": "MATLAB DSP & Comms Toolboxes, FFT, Filter Design, Complex Baseband",
        "jd_req": "Background in signal processing; collaborate with DSP engineers on simulation models"
    },
    {
        "metric": "Phased Array (PAA),<br>Beamforming & RF<br>Physics Modeling",
        "pillar": "Signal Processing, RF & Physical Modeling",
        "verified": 1.8, "upskill": 0.8, "baseline": 3.0, "color": "#fbbf24",
        "evidence": "Undergraduate electromagnetics & wave propagation foundation; active self-directed study in array factor math & digital beamforming (DBF).",
        "tools": "MATLAB Phased Array System Toolbox, EM Wave Theory, Steering Vector Math",
        "jd_req": "Optimize models for phased array antenna (PAA) systems, digital beamforming (DBF) & silicon RF components"
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
            "<b>Verified Competence Level:</b> Level %{y:.1f} / 4.0<br>"
            "<b>Active Growth Target (Grad 2026/27):</b> Level %{customdata[4]:.1f} / 4.0<br>"
            "<b>Key Evidence:</b> %{customdata[1]}<br>"
            "<b>Tools:</b> <span style='font-family:JetBrains Mono,monospace;color:#38bdf8'>%{customdata[2]}</span><br>"
            "<b>Blue Origin JD Mapping:</b> <i>%{customdata[3]}</i><extra></extra>"
        ),
    )
)

fig_master.add_trace(
    go.Bar(
        name="Active Upskilling & Research",
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
        name="Role Expectation (Baseline)",
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
            "<b>L2: Practical Foundation</b><br><span style='font-size:10px;color:#64748b'>Guided execution, coursework scripting & procedural operations</span>",
            "<b>L3: Proficient Execution</b><br><span style='font-size:10px;color:#64748b'>Applied project competence, profiling & modular development</span>",
            "<b>L4: Advanced Applications</b><br><span style='font-size:10px;color:#64748b'>Production architecture, deep optimization & multi-system synthesis</span>",
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
    "High-Performance Numerical Simulation<br>(Python / JAX Acceleration)",
    "Predictive Control Design<br>(Hierarchical MPC)",
    "Cloud Telemetry & Anomaly Log<br>(Weights & Biases)",
]
proj1_scores = [3.0, 3.0, 3.6, 3.0]
proj1_details = [
    "Reproducible monorepo builds in Linux containers with automated CI testing.",
    "Native JAX compiled vectorised simulation loops.",
    "Coupled energy and battery thermal management under dynamic constraints.",
    "Real-time experiment tracking and run comparison.",
]

fig_proj1 = go.Figure(
    go.Bar(
        y=proj1_metrics,
        x=proj1_scores,
        orientation="h",
        marker=dict(
            color=["#38bdf8", "#38bdf8", "#34d399", "#818cf8"],
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
# 3. PROJECT 2 BREAKDOWN CHART: POWER, CONTROL & RF SIGNAL PROCESSING
# -------------------------------------------------------------------------
proj2_metrics = [
    "Systems Verification & Validation<br>(FAT/SAT Compliance)",
    "Control Logic & PLC Integration<br>(Schneider / SCADA)",
    "Hardware to Software Interfacing and Integration<br>(Conveyor Systems)",
    "Architecture & Network Documentation",
    "Interdisciplinary Engineering Team Coordination",
]
proj2_scores = [2.8, 3.2, 2.6, 3.0, 3.0]
proj2_details = [
    "Assisted in FAT and SAT documentation and procedures to verify control system<br>compliance with client and design expectations.",
    "Assisted in development of system control logic and HMI systems using Schneider<br>Control Expert and AVEVA Plant SCADA.",
    "Works involved integrating modernised conveyor systems into legacy<br>mechanical infrastructure.",
    "Developed plant network systems diagrams and management of<br>system documentation.",
    "Collaborated across project teams in the design and<br>performance validation processes."
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
    "Translated life support requirements into verifiable engineering metrics.",
    "Managed core design constraints of power usage and thermal efficiency.",
    "Modeled regenerative heat exchange fluid loops and advanced aerogels.",
    "Evaluated and proposed complete closed-loop thermal system.",
    "Validated systems feasibility for conceptual surface habitats.",
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
            max-width: 900px;
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
            max-width: 520px;
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
                <!-- <img src="profile.jpg" alt="Patrick Johnston"> -->
                PJ
            </div>
            <div>
                <div class="hero-meta">
                    <span class="badge">B.Eng (Hons) Electrical & Electronic Engineering (Final Semester)</span>
                    <span class="badge green">MATLAB / Python / C++ / JAX</span>
                    <span class="badge amber">Simulation Optimization & V&V</span>
                </div>
                <h1 class="hero-title">Patrick Johnston — Engineering Prospectus</h1>
                <p class="hero-subtitle">
                    Final-semester Electrical & Electronic Engineering (Honours) undergraduate with 1 year of industry and research experience in <b>high-performance numerical simulation, control systems, and verification</b>. Proven capability in refactoring and accelerating mathematical models in <b>MATLAB, Python (JAX/NumPy), and C/C++</b>, alongside building reproducible, containerized Software-in-the-Loop (SIL) CI/CD validation pipelines.
                </p>
            </div>
        </header>

        <!-- 2. MASTER COMPETENCY & VERIFICATION MATRIX -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">01 // Target Role Alignment: PAA/DBF DSP Simulation & Verification Engineer</div>
                    <h2 class="section-title">Engineering Competency & Operational Readiness Matrix</h2>
                </div>
                <div class="section-desc">
                    Transparently maps verified undergraduate & industry capabilities against Blue Origin's role expectations. Hover over any metric bar to inspect supporting evidence, toolchains, and direct Job Description (JD) alignment.
                </div>
            </div>
            <div class="pillar-legend">
                <div class="pillar-item"><span class="dot" style="background:#38bdf8;"></span> <b>Pillar 1:</b> High-Performance Computing & Code Optimization</div>
                <div class="pillar-item"><span class="dot" style="background:#34d399;"></span> <b>Pillar 2:</b> Simulation V&V & Software Infrastructure</div>
                <div class="pillar-item"><span class="dot" style="background:#fbbf24;"></span> <b>Pillar 3:</b> Signal Processing, RF & Physical Modeling</div>
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
                    Honours Engineering Thesis | Linux/Docker Containerised CI/CD Simulation Pipeline
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Architecture & Project Scope</h4>
                    <p>
                        Designed and executed a Software-in-the-Loop (SIL) simulation framework evaluating predictive energy and thermal control strategies across multi-agent autonomous driving scenarios/trajectories, utilizing vectorized numerical solvers and automated regression testing.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">EXECUTION ENV</span> <span>Docker + Bazel Monorepo</span></li>
                        <li><span class="spec-label">SIMULATION ENGINE</span> <span>MATLAB + Python / JAX + Waymax Simulator</span></li>
                        <li><span class="spec-label">TEST DATASETS</span> <span>Waymo Open Motion Dataset</span></li>
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
                    <div class="section-kicker">03 // Key Project Breakdown — Control Systems Development, Testing and Integration</div>
                    <h2 class="section-title">Esperance Grain Terminal Control System Upgrade Project</h2>
                </div>
                <div class="section-desc">
                    Spark Engineering | Undergraduate Control Systems Engineer
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Project Scope and My Role</h4>
                    <p>
                        Facilitated the integration of modernised conveyor systems into legacy mechanical infrastructure through control system design, PLC programming, and SCADA development. Additionally, assisted with Factory and Site Acceptance Testing (FAT/SAT) to verify compliance with client expectations, and designed system performance metrics.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">CONTROL LOGIC</span> <span>Schneider Control Expert (Control & Automation)</span></li>
                        <li><span class="spec-label">HMI & SCADA</span> <span>AVEVA Plant SCADA</span></li>
                        <li><span class="spec-label">SYSTEMS V&V</span> <span>FAT & SAT Protocols & Execution</span></li>
                        <li><span class="spec-label">PLANT DOCUMENTATION</span> <span>Plant Network Systems Auditing and Diagrams</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj2_html}
                </div>
            </div>
        </section>

        <!-- 5. PROJECT BREAKDOWN 03: MARS HVAC & POWER -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">04 // Key Project Breakdown — Thermal Dynamics, Systems & Resource Planning</div>
                    <h2 class="section-title">Mars HVAC and Power System Design Project</h2>
                </div>
                <div class="section-desc">
                    Selective University Engineering Project | Conceptual Modular Mars Surface Habitat
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Project Scope and My Role</h4>
                    <p>
                        Investigated and evaluated potential closed-loop HVAC solutions for a conceptual modular Mars surface habitat, establishing power requirements and thermal mapping alongside Quality Function Deployment (QFD) matrices.
                    </p>
                    <ul class="spec-list">
                        <li><span class="spec-label">THERMAL DYNAMICS</span> <span>Regenerative Heat Exchange Fluid Loop & Aerogels</span></li>
                        <li><span class="spec-label">SYSTEMS ENGINEERING</span> <span>QFD & Requirements Definition and Traceability</span></li>
                        <li><span class="spec-label">CONTROL SYSTEMS</span> <span>Environmental Sensored Feedback Controlled System</span></li>
                        <li><span class="spec-label">CORE DESIGN CONSTRAINTS</span> <span>Power Usage and Management Constraints</span></li>
                    </ul>
                </div>
                <div>
                    {chart_proj3_html}
                </div>
            </div>
        </section>

        <!-- 6. PROJECT BREAKDOWN 04: SALVAGE OPERATION -->
        <section class="section-card">
            <div class="section-header">
                <div>
                    <div class="section-kicker">05 // Key Project Breakdown — Complex Marine Salvage Operations & Risk Mitigation</div>
                    <h2 class="section-title">HMAS OTAMA Submarine Salvage Project</h2>
                </div>
                <div class="section-desc">
                    Aegir Divers | Extensive Multi-Disciplinary Submarine Recovery Project
                </div>
            </div>
            <div class="project-grid">
                <div class="project-info">
                    <h4>Project Scope and My Role</h4>
                    <p>
                        Supported multi-disciplinary dive and engineering teams in executing the salvage operation of a compromised naval submarine, implementing buoyancy stabilization, wet welding repairs, and towage infrastructure.
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

print("Successfully generated full multi-section prospectus: index.html")