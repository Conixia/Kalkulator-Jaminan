import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kalkulator Jaminan",
    page_icon="🏦",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Fraunces:wght@600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0D1B2A;
}

/* Title block */
.hero-title {
    font-family: 'Fraunces', serif;
    font-size: 38px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.1;
    margin-bottom: 6px;
}
.hero-title span { color: #E8B84B; }
.hero-sub {
    color: #8A9BB0;
    font-size: 13px;
    margin-bottom: 32px;
}
.badge {
    display: inline-block;
    background: rgba(74,144,217,0.12);
    border: 1px solid rgba(74,144,217,0.3);
    color: #4A90D9;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .1em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 99px;
    margin-bottom: 14px;
}

/* Tarif cards */
.tarif-row { display: flex; gap: 10px; margin-bottom: 28px; flex-wrap: wrap; }
.tarif-card {
    flex: 1; min-width: 120px;
    background: rgba(255,255,255,0.04);
    border: 1.5px solid rgba(255,255,255,0.09);
    border-radius: 12px;
    padding: 14px 16px;
    text-align: center;
}
.tarif-card-name {
    font-family: 'Fraunces', serif;
    font-size: 14px;
    font-weight: 600;
    color: #FFFFFF;
    margin-bottom: 4px;
}
.tarif-card-pct {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #E8B84B;
}

/* Result box */
.result-box {
    background: linear-gradient(135deg, #1a3a5c 0%, #0d2240 100%);
    border: 1.5px solid #4A90D9;
    border-radius: 18px;
    padding: 28px 32px;
    text-align: center;
    margin: 20px 0;
}
.result-box.minimum {
    background: linear-gradient(135deg, #3a2800 0%, #1a1200 100%);
    border-color: #E8B84B;
}
.result-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .12em;
    text-transform: uppercase;
    color: #8A9BB0;
    margin-bottom: 10px;
}
.result-amount {
    font-family: 'Fraunces', serif;
    font-size: 46px;
    font-weight: 700;
    color: #3ECFB2;
    line-height: 1;
    margin-bottom: 14px;
}
.result-amount.minimum { color: #E8B84B; }
.meta-row { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.pill {
    background: rgba(255,255,255,0.08);
    border-radius: 99px;
    padding: 4px 12px;
    font-size: 12px;
    color: #8A9BB0;
    font-family: 'DM Mono', monospace;
}
.pill-blue { background: rgba(74,144,217,0.15); color: #4A90D9; }
.pill-gold { background: rgba(232,184,75,0.15);  color: #E8B84B; }

/* Formula breakdown */
.formula-box {
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 16px 20px;
    margin-top: 16px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #8A9BB0;
    line-height: 1.9;
    text-align: left;
}
.formula-box .val { color: #FFFFFF; }
.formula-box .eq  { color: #3ECFB2; font-weight: 500; }
.formula-box .warn { color: #E8B84B; }

/* History */
.hist-item {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 14px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}
.hist-name { font-size: 13px; font-weight: 500; color: #FFFFFF; margin-bottom: 3px; }
.hist-detail { font-size: 11px; color: #8A9BB0; font-family: 'DM Mono', monospace; }
.hist-result { font-family: 'Fraunces', serif; font-size: 18px; font-weight: 600; color: #3ECFB2; }
.hist-result.gold { color: #E8B84B; }

/* Section title */
.section-title {
    font-size: 11px; font-weight: 600;
    letter-spacing: .12em; text-transform: uppercase;
    color: #8A9BB0; margin: 28px 0 14px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    padding-bottom: 8px;
}

/* Override streamlit elements */
div[data-baseweb="select"] > div { background: rgba(255,255,255,0.06) !important; border-color: rgba(255,255,255,0.1) !important; color: white !important; }
.stSelectbox label, .stNumberInput label { color: #8A9BB0 !important; font-size: 11px !important; font-weight: 600 !important; letter-spacing: .1em !important; text-transform: uppercase !important; }
input[type="number"] { background: rgba(255,255,255,0.06) !important; color: white !important; border-color: rgba(255,255,255,0.1) !important; font-family: 'DM Mono', monospace !important; }
.stButton > button {
    background: linear-gradient(135deg, #4A90D9, #2563a8) !important;
    color: white !important; border: none !important;
    border-radius: 10px !important; font-weight: 600 !important;
    font-size: 15px !important; width: 100% !important;
    padding: 14px !important;
}
.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(74,144,217,.35) !important; }
</style>
""", unsafe_allow_html=True)

# ── Data ───────────────────────────────────────────────────────────────────────
TARIF = {
    "Penawaran":    0.00132,
    "Pelaksanaan":  0.00212,
    "Uang Muka":    0.00266,
    "Pemeliharaan": 0.00212,
}
TARIF_PCT = {
    "Penawaran":   "0,132%",
    "Pelaksanaan": "0,212%",
    "Uang Muka":   "0,266%",
    "Pemeliharaan":"0,212%",
}
MINIMUM = 75_000

def fmt_rp(n):
    return "Rp {:,.0f}".format(n).replace(",", ".")

def fmt_short(n):
    if n >= 1_000_000_000: return "Rp {:.2f} M".format(n/1_000_000_000).replace(".",",")
    if n >= 1_000_000:     return "Rp {:.2f} Jt".format(n/1_000_000).replace(".",",")
    return fmt_rp(n)

# ── Session State ──────────────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="badge">🏦 Alat Perhitungan</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Kalkulator <span>Jaminan</span></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Penawaran · Pelaksanaan · Uang Muka · Pemeliharaan — Minimum Rp 75.000</div>', unsafe_allow_html=True)

# ── Tarif Reference Cards ──────────────────────────────────────────────────────
cards_html = '<div class="tarif-row">'
for nama, pct in TARIF_PCT.items():
    cards_html += f"""
    <div class="tarif-card">
        <div class="tarif-card-name">{nama}</div>
        <div class="tarif-card-pct">{pct}</div>
    </div>"""
cards_html += "</div>"
st.markdown(cards_html, unsafe_allow_html=True)

# ── Input Form ─────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    jenis = st.selectbox("Jenis Jaminan", list(TARIF.keys()), index=None, placeholder="Pilih jenis jaminan...")
with col2:
    nilai = st.number_input("Nilai Jaminan (Rp)", min_value=0, value=None, step=1_000_000, placeholder="Contoh: 500000000", format="%d")

col3, col4 = st.columns(2)
with col3:
    jw = st.number_input("Jangka Waktu (Hari)", min_value=1, value=None, step=1, placeholder="Contoh: 90", format="%d")
    if jw:
        if jw <= 90:
            st.caption("✓ ≤ 90 hari → rumus normal")
        else:
            st.caption(f"↻ > 90 hari → rumus proporsional (×{90/jw:.4f})")
with col4:
    if nilai and nilai > 0:
        st.caption(f"= {fmt_rp(nilai)}")
    st.markdown("<br>", unsafe_allow_html=True)
    hitung_btn = st.button("Hitung Sekarang →", use_container_width=True)

# ── Calculation ────────────────────────────────────────────────────────────────
if hitung_btn:
    if not jenis:
        st.error("⚠ Pilih jenis jaminan terlebih dahulu!")
    elif not nilai or nilai <= 0:
        st.error("⚠ Masukkan nilai jaminan yang valid!")
    elif not jw or jw <= 0:
        st.error("⚠ Masukkan jangka waktu yang valid!")
    else:
        tarif      = TARIF[jenis]
        is_normal  = jw <= 90
        raw_result = nilai * tarif if is_normal else nilai * (90 / jw) * tarif
        is_min     = raw_result < MINIMUM
        result     = MINIMUM if is_min else raw_result

        # Store to history
        st.session_state.history.insert(0, {
            "jenis": jenis, "nilai": nilai, "jw": jw,
            "tarif": tarif, "result": result, "is_min": is_min,
            "raw_result": raw_result,
        })
        if len(st.session_state.history) > 10:
            st.session_state.history.pop()

        # Result box (tanpa formula-box di dalam)
        box_class   = "result-box minimum" if is_min else "result-box"
        amt_class   = "result-amount minimum" if is_min else "result-amount"
        pill_result = '<span class="pill pill-gold">&#9888; Nilai minimum</span>' if is_min else ""

        st.markdown(f"""
        <div class="{box_class}">
            <div class="result-label">Hasil Perhitungan</div>
            <div class="{amt_class}">{fmt_rp(result)}</div>
            <div class="meta-row">
                <span class="pill pill-blue">{jenis}</span>
                <span class="pill">{fmt_short(nilai)}</span>
                <span class="pill">{jw} hari</span>
                <span class="pill">{tarif*100:.3f}%</span>
                {pill_result}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Formula breakdown — pakai st.code agar tidak ada masalah render HTML
        if is_normal:
            rumus_line1 = f"{fmt_rp(nilai)} x {tarif*100:.3f}%"
            rumus_line2 = f"= {fmt_rp(raw_result)}"
            rumus_line3 = f"= {fmt_rp(result)}"
            formula_text = f"Rumus  : Nilai Jaminan x Tarif  (JW <= 90 hari)\n{'─'*45}\n{rumus_line1}\n{rumus_line2}\n{rumus_line3}"
        else:
            rumus_line1 = f"{fmt_rp(nilai)} x (90 / {jw}) x {tarif*100:.3f}%"
            rumus_line2 = f"= {fmt_rp(nilai)} x {90/jw:.6f} x {tarif*100:.3f}%"
            rumus_line3 = f"= {fmt_rp(raw_result)}"
            formula_text = f"Rumus  : Nilai Jaminan x (90 / JW) x Tarif  (JW > 90 hari)\n{'─'*45}\n{rumus_line1}\n{rumus_line2}\n{rumus_line3}"

        if is_min:
            formula_text += f"\n{'─'*45}\nHasil hitung : {fmt_rp(raw_result)}\nMinimum      : {fmt_rp(MINIMUM)}  ← yang dipakai"

        st.code(formula_text, language=None)

        if is_min:
            st.warning(f"⚠ Hasil hitungan ({fmt_rp(raw_result)}) di bawah minimum — ditampilkan sebagai **Rp 75.000**")

# ── History ────────────────────────────────────────────────────────────────────
if st.session_state.history:
    col_h1, col_h2 = st.columns([3, 1])
    with col_h1:
        st.markdown('<div class="section-title">Riwayat Perhitungan</div>', unsafe_allow_html=True)
    with col_h2:
        if st.button("🗑 Hapus Semua", key="clear"):
            st.session_state.history = []
            st.rerun()

    for h in st.session_state.history:
        res_class = "hist-result gold" if h["is_min"] else "hist-result"
        st.markdown(f"""
        <div class="hist-item">
            <div>
                <div class="hist-name">{h['jenis']}</div>
                <div class="hist-detail">{fmt_rp(h['nilai'])} · {h['jw']} hari · {h['tarif']*100:.3f}%</div>
            </div>
            <div class="{res_class}">{fmt_rp(h['result'])}</div>
        </div>
        """, unsafe_allow_html=True)
