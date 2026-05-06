import streamlit as st

st.set_page_config(page_title="Kalkulator Jaminan", page_icon="🏦", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #0D1B2A; }
.kj-badge { display:inline-block;background:rgba(74,144,217,0.12);border:1px solid rgba(74,144,217,0.3);color:#4A90D9;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;padding:5px 14px;border-radius:99px;margin-bottom:12px; }
.kj-title { font-family:'Fraunces',serif;font-size:38px;font-weight:700;color:#FFFFFF;line-height:1.1;margin-bottom:6px; }
.kj-title span { color:#E8B84B; }
.kj-sub { color:#8A9BB0;font-size:13px;margin-bottom:28px; }
.kj-tarif-row { display:flex;gap:10px;margin-bottom:28px;flex-wrap:wrap; }
.kj-tarif-card { flex:1;min-width:120px;background:rgba(255,255,255,0.04);border:1.5px solid rgba(255,255,255,0.09);border-radius:12px;padding:14px 16px;text-align:center; }
.kj-tarif-name { font-family:'Fraunces',serif;font-size:14px;font-weight:600;color:#FFFFFF;margin-bottom:4px; }
.kj-tarif-pct  { font-family:'DM Mono',monospace;font-size:13px;color:#E8B84B; }
.kj-result-wrap { border-radius:18px;padding:28px 24px 20px;text-align:center;margin:4px 0 0; }
.kj-result-label { font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#8A9BB0;margin:0 0 10px; }
.kj-result-amount { font-family:'Fraunces',serif;font-size:52px;font-weight:700;line-height:1;margin:0; }
.kj-info-box { background:rgba(255,255,255,0.06);border-radius:12px;padding:14px 12px;text-align:center; }
.kj-info-label { font-size:10px;color:#8A9BB0;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px; }
.kj-info-value { font-size:14px;font-weight:600; }
.kj-divider { border:none;border-top:1px solid rgba(255,255,255,0.07);margin:20px 0; }
.kj-section-title { font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#8A9BB0;margin-bottom:12px; }
.kj-hist-wrap { background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:14px 18px;margin-bottom:8px; }
.kj-hist-name { font-size:13px;font-weight:600;color:#FFFFFF; }
.kj-hist-detail { font-size:11px;color:#8A9BB0;font-family:'DM Mono',monospace;margin-top:2px; }
.kj-hist-result { font-family:'Fraunces',serif;font-size:18px;font-weight:700;text-align:right; }
div[data-baseweb="select"] > div { background:rgba(255,255,255,0.06) !important;border-color:rgba(255,255,255,0.12) !important;color:white !important; }
.stSelectbox label, .stNumberInput label { color:#8A9BB0 !important;font-size:11px !important;font-weight:600 !important;letter-spacing:.1em !important;text-transform:uppercase !important; }
input[type="number"] { background:rgba(255,255,255,0.06) !important;color:white !important;border-color:rgba(255,255,255,0.12) !important; }
.stButton > button { background:linear-gradient(135deg,#4A90D9,#2563a8) !important;color:white !important;border:none !important;border-radius:10px !important;font-weight:600 !important;padding:12px !important;width:100% !important; }
.stButton > button:hover { box-shadow:0 8px 24px rgba(74,144,217,.4) !important; }
</style>
""", unsafe_allow_html=True)

TARIF = {"Penawaran":0.00132,"Pelaksanaan":0.00212,"Uang Muka":0.00266,"Pemeliharaan":0.00212}
MINIMUM = 75_000

def fmt_rp(n):
    return "Rp {:,.0f}".format(n).replace(",",".")

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown('<div class="kj-badge">🏦 Alat Perhitungan</div>', unsafe_allow_html=True)
st.markdown('<div class="kj-title">Kalkulator <span>Jaminan</span></div>', unsafe_allow_html=True)
st.markdown('<div class="kj-sub">Penawaran &middot; Pelaksanaan &middot; Uang Muka &middot; Pemeliharaan &mdash; Minimum Rp 75.000</div>', unsafe_allow_html=True)

st.markdown("""
<div class="kj-tarif-row">
<div class="kj-tarif-card"><div class="kj-tarif-name">Penawaran</div><div class="kj-tarif-pct">0,132%</div></div>
<div class="kj-tarif-card"><div class="kj-tarif-name">Pelaksanaan</div><div class="kj-tarif-pct">0,212%</div></div>
<div class="kj-tarif-card"><div class="kj-tarif-name">Uang Muka</div><div class="kj-tarif-pct">0,266%</div></div>
<div class="kj-tarif-card"><div class="kj-tarif-name">Pemeliharaan</div><div class="kj-tarif-pct">0,212%</div></div>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    jenis = st.selectbox("Jenis Jaminan", list(TARIF.keys()), index=None, placeholder="Pilih jenis jaminan...")
with c2:
    nilai = st.number_input("Nilai Jaminan (Rp)", min_value=0, value=None, step=1_000_000, placeholder="Contoh: 500000000", format="%d")
    if nilai and nilai > 0:
        st.caption("= " + fmt_rp(nilai))

c3, c4 = st.columns(2)
with c3:
    jw = st.number_input("Jangka Waktu (Hari)", min_value=1, value=None, step=1, placeholder="Contoh: 90", format="%d")
    if jw:
        st.caption("Rumus normal (JW <= 90 hari)" if jw <= 90 else "Rumus proporsional x " + str(round(90/jw,4)))
with c4:
    st.markdown("<br>", unsafe_allow_html=True)
    hitung = st.button("Hitung Sekarang", use_container_width=True)

if hitung:
    if not jenis:
        st.error("Pilih jenis jaminan terlebih dahulu!")
    elif not nilai or nilai <= 0:
        st.error("Masukkan nilai jaminan yang valid!")
    elif not jw or jw <= 0:
        st.error("Masukkan jangka waktu yang valid!")
    else:
        tarif      = TARIF[jenis]
        is_normal  = jw <= 90
        raw_result = nilai * tarif if is_normal else nilai * (90 / jw) * tarif
        is_min     = raw_result < MINIMUM
        result     = MINIMUM if is_min else raw_result

        st.session_state.history.insert(0, {
            "jenis":jenis,"nilai":nilai,"jw":jw,
            "tarif":tarif,"result":result,"is_min":is_min,"raw":raw_result,
        })
        if len(st.session_state.history) > 10:
            st.session_state.history.pop()

        bg    = "linear-gradient(135deg,#3a2800,#1a1200)" if is_min else "linear-gradient(135deg,#1a3a5c,#0d2240)"
        bdr   = "#E8B84B" if is_min else "#4A90D9"
        color = "#E8B84B" if is_min else "#3ECFB2"

        # Hasil angka besar - HTML sesederhana mungkin
        st.markdown(
            '<div class="kj-result-wrap" style="background:' + bg + ';border:1.5px solid ' + bdr + ';">'
            '<p class="kj-result-label">Hasil Perhitungan</p>'
            '<p class="kj-result-amount" style="color:' + color + ';">' + fmt_rp(result) + '</p>'
            '</div>',
            unsafe_allow_html=True
        )

        if is_min:
            st.warning("Hasil hitung asli **" + fmt_rp(raw_result) + "** di bawah minimum — ditampilkan sebagai **Rp 75.000**")

        # Info 4 kotak - pakai st.columns + HTML sederhana (tidak ada f-string bercabang)
        st.markdown("<br>", unsafe_allow_html=True)
        ic1, ic2, ic3, ic4 = st.columns(4)

        jenis_html  = '<div class="kj-info-box"><div class="kj-info-label">Jenis</div><div class="kj-info-value" style="color:#4A90D9;">' + jenis + '</div></div>'
        nilai_html  = '<div class="kj-info-box"><div class="kj-info-label">Nilai Jaminan</div><div class="kj-info-value" style="color:#fff;font-size:12px;">' + fmt_rp(nilai) + '</div></div>'
        jw_html     = '<div class="kj-info-box"><div class="kj-info-label">Jangka Waktu</div><div class="kj-info-value" style="color:#fff;">' + str(jw) + ' hari</div></div>'
        tarif_html  = '<div class="kj-info-box"><div class="kj-info-label">Tarif</div><div class="kj-info-value" style="color:#E8B84B;">' + str(round(tarif*100,3)) + '%</div></div>'

        ic1.markdown(jenis_html,  unsafe_allow_html=True)
        ic2.markdown(nilai_html,  unsafe_allow_html=True)
        ic3.markdown(jw_html,     unsafe_allow_html=True)
        ic4.markdown(tarif_html,  unsafe_allow_html=True)

        # Rumus - st.code 100% aman
        st.markdown("<br>", unsafe_allow_html=True)
        tarif_pct = str(round(tarif*100, 3)) + "%"
        sep = "  " + "-"*42
        if is_normal:
            formula = (
                "  Rumus  : Nilai Jaminan x Tarif\n" + sep + "\n"
                "  " + fmt_rp(nilai) + " x " + tarif_pct + "\n"
                "  = " + fmt_rp(raw_result) + "\n" + sep + "\n"
                "  Hasil  : " + fmt_rp(result)
            )
        else:
            faktor = round(90 / jw, 6)
            formula = (
                "  Rumus  : Nilai Jaminan x (90 / JW) x Tarif\n" + sep + "\n"
                "  " + fmt_rp(nilai) + " x (90 / " + str(jw) + ") x " + tarif_pct + "\n"
                "  " + fmt_rp(nilai) + " x " + str(faktor) + " x " + tarif_pct + "\n"
                "  = " + fmt_rp(raw_result) + "\n" + sep + "\n"
                "  Hasil  : " + fmt_rp(result)
            )
            if is_min:
                formula += "\n  (Min)  : " + fmt_rp(MINIMUM) + "  <-- yang berlaku"
        st.code(formula, language=None)

# Riwayat
if st.session_state.history:
    st.markdown("<hr class='kj-divider'>", unsafe_allow_html=True)
    hc1, hc2 = st.columns([4, 1])
    with hc1:
        st.markdown('<p class="kj-section-title">Riwayat Perhitungan</p>', unsafe_allow_html=True)
    with hc2:
        if st.button("Hapus", key="clear"):
            st.session_state.history = []
            st.rerun()

    for h in st.session_state.history:
        rc = "#E8B84B" if h["is_min"] else "#3ECFB2"
        row = (
            '<div class="kj-hist-wrap">'
            '<div style="display:flex;justify-content:space-between;align-items:center;">'
            '<div><div class="kj-hist-name">' + h["jenis"] + '</div>'
            '<div class="kj-hist-detail">' + fmt_rp(h["nilai"]) + ' &bull; ' + str(h["jw"]) + ' hari &bull; ' + str(round(h["tarif"]*100,3)) + '%</div></div>'
            '<div class="kj-hist-result" style="color:' + rc + ';">' + fmt_rp(h["result"]) + '</div>'
            '</div></div>'
        )
        st.markdown(row, unsafe_allow_html=True)
