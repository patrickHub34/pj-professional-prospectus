import plotly.graph_objects as go

# -------------------------------------------------------------------------
# 1. DEFINE COMPETENCY DATASET (Tailored to EO Mission Performance JD)
# -------------------------------------------------------------------------
data = [
    # Pillar 1: Software Infrastructure & Remote Operations
    {
        "metric": "Docker & Hermetic<br>Execution",
        "pillar": "Software & Linux Infrastructure",
        "verified": 3.8,
        "upskill": 0.2,  # Stacked on top of verified to show active trajectory
        "baseline": 3.0,
        "color": "#38bdf8",
        "evidence": "Containerized simulation pipelines, multi-stage builds, runtime diagnostics, CI integration",
        "tools": "Docker, Bash, Bazel, GitHub Actions",
        "jd_req": "Start/stop containers, diagnostics, rebuild images, maintain stable environment"
    },
    {
        "metric": "Linux CLI &<br>Remote Server Ops",
        "pillar": "Software & Linux Infrastructure",
        "verified": 3.5,
        "upskill": 0.3,
        "baseline": 3.0,
        "color": "#38bdf8",
        "evidence": "Headless simulation execution via SSH, automated log parsing, SFTP/FTPS transfers",
        "tools": "Linux CLI, SSH, SFTP, grep/awk/sed, systemd",
        "jd_req": "Work in CLI, run scripts, filter logs, manage permissions, remote SSH/SFTP"
    },
    {
        "metric": "Python & C/C++<br>Simulation Code",
        "pillar": "Software & Linux Infrastructure",
        "verified": 3.6,
        "upskill": 0.3,
        "baseline": 3.0,
        "color": "#38bdf8",
        "evidence": "High-performance numerical computing, build system navigation, parameter steering",
        "tools": "Python (JAX/NumPy), C/C++, Bazel/CMake, Git",
        "jd_req": "Follow code structure, interpret build/runtime errors, adjust parameters"
    },
    # Pillar 2: Systems Engineering, V&V & E2E Simulation
    {
        "metric": "E2E Simulator<br>Operation & V&V",
        "pillar": "Systems Engineering & V&V",
        "verified": 3.7,
        "upskill": 0.3,
        "baseline": 3.5,
        "color": "#34d399",
        "evidence": "Software-in-the-loop (SIL) predictive control, sensitivity & non-compliance trade studies",
        "tools": "SIL Simulators, Python, MATLAB/Simulink, W&B",
        "jd_req": "Operate E2E simulators & evaluate non-compliance effects on mission performance"
    },
    {
        "metric": "Test Dataset<br>Production",
        "pillar": "Systems Engineering & V&V",
        "verified": 3.6,
        "upskill": 0.3,
        "baseline": 3.0,
        "color": "#34d399",
        "evidence": "Extraction, synthesis, and validation of multi-agent trajectory & telemetry datasets",
        "tools": "Python, NumPy, SciPy, Automated Data Pipelines",
        "jd_req": "Production and verification of test data sets for performance simulators"
    },
    {
        "metric": "Calibration &<br>Anomaly Analysis",
        "pillar": "Systems Engineering & V&V",
        "verified": 3.4,
        "upskill": 0.4,
        "baseline": 3.0,
        "color": "#34d399",
        "evidence": "Telemetry anomaly logging, step-response characterization, structured bug reporting",
        "tools": "MATLAB, Python, Weights & Biases, Telemetry Suites",
        "jd_req": "Analyze calibration campaign data & report software anomalies to developers"
    },
    {
        "metric": "Requirements &<br>VCB Compliance",
        "pillar": "Systems Engineering & V&V",
        "verified": 3.2,
        "upskill": 0.5,
        "baseline": 3.0,
        "color": "#34d399",
        "evidence": "System verification matrices, protection/control grading, formal technical reviews",
        "tools": "Verification Matrices, Technical Documentation, LaTeX",
        "jd_req": "Support requirements verification & Verification Control Board (VCB) tracking"
    },
    # Pillar 3: Payload Modeling & Signal Processing
    {
        "metric": "Optical Imager<br>Simulation",
        "pillar": "Payload & Signal Processing",
        "verified": 2.6,
        "upskill": 0.9,
        "baseline": 3.0,
        "color": "#fbbf24",
        "evidence": "2D spatial array processing, sensor noise modeling, PSF/MTF physical foundations",
        "tools": "Python, MATLAB Image Processing, Numerical Optics",
        "jd_req": "Expertise with optical instruments (imagers) for simulation and processing"
    },
    {
        "metric": "SAR Signal<br>Processing",
        "pillar": "Payload & Signal Processing",
        "verified": 2.4,
        "upskill": 1.0,
        "baseline": 2.5,
        "color": "#fbbf24",
        "evidence": "Multipath channel modeling, OFDM/RF signal processing, FFT/phase-history foundations",
        "tools": "MATLAB Wireless Comms, Python SciPy.signal, FFT",
        "jd_req": "Expertise in Synthetic Aperture Radar (SAR) processing (desirable)"
    },
]

metrics = [d["metric"] for d in data]
verified = [d["verified"] for d in data]
upskill = [d["upskill"] for d in data]
baselines = [d["baseline"] for d in data]

# -------------------------------------------------------------------------
# 2. BUILD FIGURE WITH STACKED COMPETENCY + TARGET TRAJECTORY
# -------------------------------------------------------------------------
fig = go.Figure()

# Trace 1: Verified Competency (Solid Bars)
fig.add_trace(
    go.Bar(
        name="Verified Operational Capability",
        x=metrics,
        y=verified,
        marker=dict(
            color=[d["color"] for d in data],
            line=dict(color="#0f172a", width=1.5),
            opacity=0.92,
        ),
        customdata=[
            [d["pillar"], d["evidence"], d["tools"], d["jd_req"], d["verified"] + d["upskill"]]
            for d in data
        ],
        hovertemplate=(
            "<b>%{x}</b><br>"
            "<span style='color:#94a3b8'>Pillar: %{customdata[0]}</span><br><br>"
            "<b>Verified Tier:</b> Level %{y:.1f} / 4.0<br>"
            "<b>Active Growth Target:</b> Level %{customdata[4]:.1f} / 4.0<br>"
            "<b>Demonstrated Evidence:</b> %{customdata[1]}<br>"
            "<b>Tool Stack:</b> <span style='font-family:monospace'>%{customdata[2]}</span><br>"
            "<b>JD Alignment:</b> <i>%{customdata[3]}</i>"
            "<extra></extra>"
        ),
    )
)

# Trace 2: Active Upskilling / Commissioning Readiness Margin (Translucent Top Bar)
fig.add_trace(
    go.Bar(
        name="Active Upskilling / Domain Ramp-Up",
        x=metrics,
        y=upskill,
        marker=dict(
            color=[d["color"] for d in data],
            opacity=0.28,
            pattern=dict(shape="/", solidity=0.3),
            line=dict(color=[d["color"] for d in data], width=1.5),
        ),
        hoverinfo="skip",
    )
)

# Trace 3: Role Baseline Requirement Marker
fig.add_trace(
    go.Scatter(
        name="Role Target Baseline (JD Expectation)",
        x=metrics,
        y=baselines,
        mode="markers+lines",
        line=dict(color="#f43f5e", width=2, dash="dot"),
        marker=dict(symbol="diamond", size=10, color="#f43f5e", line=dict(color="#ffffff", width=1)),
        hovertemplate="<b>%{x}</b><br>JD Target Baseline: Level %{y:.1f}<extra></extra>",
    )
)

# -------------------------------------------------------------------------
# 3. CONFIGURE TELEMETRY-GRADE LAYOUT & Y-AXIS V&V TIERS
# -------------------------------------------------------------------------
fig.update_layout(
    barmode="stack",
    title=dict(
        text=(
            "<b>ENGINEERING COMPETENCY & VERIFICATION MATRIX</b><br>"
            "<span style='font-size:13px;color:#94a3b8'>"
            "End-to-End (E2E) Mission Performance & Simulation Engineer Prospectus — Hover bars for V&V evidence"
            "</span>"
        ),
        font=dict(family="Inter, Segoe UI, sans-serif", size=20, color="#f8fafc"),
        x=0.03,
        y=0.95,
    ),
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(family="Inter, Segoe UI, sans-serif", color="#cbd5e1", size=12),
    yaxis=dict(
        title="<b>Verification & Operational Readiness Tier</b>",
        range=[0, 4.3],
        tickvals=[1, 2, 3, 4],
        ticktext=[
            "<b>L1: Theoretical / Review</b><br><span style='font-size:10px;color:#64748b'>Code structure & math foundations</span>",
            "<b>L2: Scripting & Execution</b><br><span style='font-size:10px;color:#64748b'>CLI operation, param tuning, test data</span>",
            "<b>L3: Diagnostics & Anomaly ID</b><br><span style='font-size:10px;color:#64748b'>Log filtering, debugging, compliance</span>",
            "<b>L4: Full E2E Integration & V&V</b><br><span style='font-size:10px;color:#64748b'>Hermetic pipelines, SIL & VCB closure</span>",
        ],
        gridcolor="#1e293b",
        zerolinecolor="#334155",
    ),
    xaxis=dict(
        title="",
        tickangle=0,
        gridcolor="#1e293b",
    ),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        bgcolor="rgba(15, 23, 42, 0.8)",
        bordercolor="#334155",
        borderwidth=1,
    ),
    hoverlabel=dict(
        bgcolor="#1e293b",
        bordercolor="#475569",
        font=dict(family="Inter, sans-serif", size=12, color="#f8fafc"),
        align="left",
    ),
    margin=dict(l=210, r=40, t=110, b=80),
    height=650,
)

# Replace the final lines of generate_prospectus.py with this:
fig.write_html(
    "index.html",
    include_plotlyjs="cdn",
    full_html=True,
    config={"displayModeBar": True, "displaylogo": False},
)
print("Successfully generated: index.html")