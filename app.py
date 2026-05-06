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

        # ── Siapkan semua nilai sebagai variabel Python dulu ──
        box_border = "#E8B84B" if is_min else "#4A90D9"
        box_bg     = "linear-gradient(135deg,#3a2800,#1a1200)" if is_min else "linear-gradient(135deg,#1a3a5c,#0d2240)"
        amt_color  = "#E8B84B" if is_min else "#3ECFB2"
        result_str = fmt_rp(result)
        nilai_str  = fmt_rp(nilai)
        jw_str     = f"{jw} hari"
        tarif_str  = f"{tarif*100:.3f}%"
        mode_str   = "Normal (JW <= 90 hari)" if is_normal else "Proporsional (JW > 90 hari)"

        if is_normal:
            rb1 = f"{nilai_str} x {tarif_str}"
            rb2 = f"= {fmt_rp(raw_result)}"
            rb3 = ""
        else:
            faktor = round(90 / jw, 6)
            rb1 = f"{nilai_str} x (90 / {jw}) x {tarif_str}"
            rb2 = f"{nilai_str} x {faktor} x {tarif_str}"
            rb3 = f"= {fmt_rp(raw_result)}"

        rb3_row = f"<tr><td colspan='2'></td><td style='text-align:right;color:#fff;padding:2px 0;'>{rb3}</td></tr>" if rb3 else ""

        if is_min:
            min_badge = f'<p style="text-align:center;margin:0 0 18px;"><span style="background:rgba(232,184,75,.2);color:#E8B84B;border-radius:99px;padding:4px 14px;font-size:12px;font-weight:600;">Nilai Minimum Berlaku</span></p>'
            min_rows  = (
                f"<tr><td colspan='2' style='color:#8A9BB0;font-size:12px;border-top:1px solid rgba(255,255,255,.1);padding-top:10px;'>Hasil hitung</td>"
                f"<td style='text-align:right;color:#8A9BB0;font-size:12px;border-top:1px solid rgba(255,255,255,.1);padding-top:10px;'>{fmt_rp(raw_result)}</td></tr>"
                f"<tr><td colspan='2' style='color:#E8B84B;font-weight:600;padding-top:6px;'>Minimum berlaku</td>"
                f"<td style='text-align:right;color:#E8B84B;font-weight:600;padding-top:6px;'>{fmt_rp(MINIMUM)}</td></tr>"
            )
        else:
            min_badge = ""
            min_rows  = ""

        html = f"""
        <div style="background:{box_bg};border:1.5px solid {box_border};border-radius:18px;padding:32px 28px 24px;margin:20px 0;">
            <p style="text-align:center;font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#8A9BB0;margin:0 0 10px;">Hasil Perhitungan</p>
            <p style="text-align:center;font-family:'Fraunces',serif;font-size:52px;font-weight:700;color:{amt_color};line-height:1;margin:0 0 20px;">{result_str}</p>
            {min_badge}
            <table style="width:100%;border-collapse:separate;border-spacing:4px;margin-bottom:20px;">
                <tr>
                    <td style="width:25%;background:rgba(255,255,255,.06);border-radius:10px;padding:12px;text-align:center;">
                        <div style="font-size:10px;color:#8A9BB0;text-transform:uppercase;letter-spacing:.08em;margin-bottom:5px;">Jenis</div>
                        <div style="font-size:14px;font-weight:600;color:#4A90D9;">{jenis}</div>
                    </td>
                    <td style="width:25%;background:rgba(255,255,255,.06);border-radius:10px;padding:12px;text-align:center;">
                        <div style="font-size:10px;color:#8A9BB0;text-transform:uppercase;letter-spacing:.08em;margin-bottom:5px;">Nilai Jaminan</div>
                        <div style="font-size:13px;font-weight:600;color:#fff;font-family:monospace;">{nilai_str}</div>
                    </td>
                    <td style="width:25%;background:rgba(255,255,255,.06);border-radius:10px;padding:12px;text-align:center;">
                        <div style="font-size:10px;color:#8A9BB0;text-transform:uppercase;letter-spacing:.08em;margin-bottom:5px;">Jangka Waktu</div>
                        <div style="font-size:14px;font-weight:600;color:#fff;">{jw_str}</div>
                    </td>
                    <td style="width:25%;background:rgba(255,255,255,.06);border-radius:10px;padding:12px;text-align:center;">
                        <div style="font-size:10px;color:#8A9BB0;text-transform:uppercase;letter-spacing:.08em;margin-bottom:5px;">Tarif</div>
                        <div style="font-size:14px;font-weight:600;color:#E8B84B;font-family:monospace;">{tarif_str}</div>
                    </td>
                </tr>
            </table>
            <div style="background:rgba(0,0,0,.3);border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:16px 20px;">
                <p style="font-size:10px;color:#8A9BB0;text-transform:uppercase;letter-spacing:.1em;margin:0 0 12px;">Rincian Rumus — {mode_str}</p>
                <table style="width:100%;border-collapse:collapse;font-family:monospace;font-size:13px;">
                    <tr><td colspan="2" style="color:#8A9BB0;padding:2px 0;">Perhitungan</td><td style="text-align:right;color:#fff;padding:2px 0;">{rb1}</td></tr>
                    <tr><td colspan="2" style="color:#8A9BB0;padding:2px 0;"></td><td style="text-align:right;color:#fff;padding:2px 0;">{rb2}</td></tr>
                    {rb3_row}
                    <tr>
                        <td colspan="2" style="border-top:1px solid rgba(255,255,255,.1);padding-top:10px;color:#8A9BB0;">Hasil</td>
                        <td style="border-top:1px solid rgba(255,255,255,.1);padding-top:10px;text-align:right;color:{amt_color};font-weight:600;font-size:15px;">{result_str}</td>
                    </tr>
                    {min_rows}
                </table>
            </div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

        if is_min:
            st.warning(f"Hasil hitungan ({fmt_rp(raw_result)}) di bawah minimum — ditampilkan sebagai **Rp 75.000**")

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
