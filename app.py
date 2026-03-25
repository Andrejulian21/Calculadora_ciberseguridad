import streamlit as st
import math

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="CryptoCalc — Calculadora Criptográfica",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# GLOBAL STYLES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

/* Main background */
.stApp {
    background: #0a0e1a;
    color: #e2e8f0;
}

/* Top nav bar custom */
.top-nav {
    display: flex;
    gap: 6px;
    padding: 14px 20px;
    background: #0f1629;
    border-bottom: 1px solid #1e2d4a;
    margin-bottom: 30px;
    flex-wrap: wrap;
    border-radius: 0 0 16px 16px;
}
.nav-btn {
    padding: 8px 18px;
    border-radius: 8px;
    font-family: 'Syne', sans-serif;
    font-weight: 600;
    font-size: 13px;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.2s;
    text-decoration: none;
    white-space: nowrap;
}
.nav-btn.active {
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    color: white;
    box-shadow: 0 0 20px rgba(99,102,241,0.4);
}
.nav-btn.inactive {
    background: #1a2340;
    color: #94a3b8;
    border-color: #1e2d4a;
}

/* Title */
.page-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2rem;
    background: linear-gradient(135deg, #60a5fa, #a78bfa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 4px;
}
.page-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 28px;
    font-family: 'JetBrains Mono', monospace;
}

/* Cards */
.calc-card {
    background: #0f1629;
    border: 1px solid #1e2d4a;
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 20px;
}

/* Process box */
.process-box {
    background: #070b14;
    border: 1px solid #1e3a5f;
    border-left: 3px solid #3b82f6;
    border-radius: 8px;
    padding: 20px 24px;
    margin-top: 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 1.9;
    color: #cbd5e1;
}
.process-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 15px;
    color: #60a5fa;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.result-highlight {
    background: linear-gradient(135deg, rgba(59,130,246,0.15), rgba(99,102,241,0.15));
    border: 1px solid #3b82f6;
    border-radius: 10px;
    padding: 14px 20px;
    margin-top: 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    font-weight: 700;
    color: #93c5fd;
    text-align: center;
}
.result-ok {
    border-color: #10b981;
    color: #6ee7b7;
    background: rgba(16,185,129,0.1);
}
.result-error {
    border-color: #ef4444;
    color: #fca5a5;
    background: rgba(239,68,68,0.1);
}
.step-num {
    display: inline-block;
    background: #1e3a5f;
    color: #60a5fa;
    border-radius: 50%;
    width: 22px;
    height: 22px;
    text-align: center;
    line-height: 22px;
    font-size: 11px;
    font-weight: 700;
    margin-right: 6px;
}

/* Table styles */
table.aee-table {
    border-collapse: collapse;
    width: 100%;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    margin-top: 12px;
}
table.aee-table th {
    background: #1e3a5f;
    color: #93c5fd;
    padding: 10px 16px;
    text-align: center;
    border: 1px solid #1e2d4a;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
}
table.aee-table td {
    padding: 9px 16px;
    border: 1px solid #1e2d4a;
    text-align: center;
    color: #cbd5e1;
}
table.aee-table tr:nth-child(even) td {
    background: #0f1629;
}
table.aee-table tr:last-child td {
    background: rgba(59,130,246,0.12);
    color: #93c5fd;
    font-weight: 700;
}

/* Submenu tabs */
div[data-testid="stHorizontalBlock"] { gap: 10px; }

/* Streamlit widget overrides */
.stSelectbox > div > div {
    background: #0f1629 !important;
    border-color: #1e2d4a !important;
    color: #e2e8f0 !important;
}
.stNumberInput > div > div > input {
    background: #0f1629 !important;
    border-color: #1e2d4a !important;
    color: #e2e8f0 !important;
}
.stTextInput > div > div > input {
    background: #0f1629 !important;
    border-color: #1e2d4a !important;
    color: #e2e8f0 !important;
}
label { color: #94a3b8 !important; font-family: 'Syne', sans-serif !important; }
.stButton > button {
    background: linear-gradient(135deg, #3b82f6, #6366f1) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    padding: 10px 28px !important;
    font-size: 14px !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 15px rgba(99,102,241,0.3) !important;
}
.stButton > button:hover {
    box-shadow: 0 6px 20px rgba(99,102,241,0.5) !important;
    transform: translateY(-1px) !important;
}
h3 { color: #93c5fd !important; font-family: 'Syne', sans-serif !important; }
.stDivider { border-color: #1e2d4a !important; }

/* Logo header */
.logo-area {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 18px 24px 10px 24px;
}
.logo-icon {
    width: 42px; height: 42px;
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
}
.logo-text { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 1.3rem; color: #e2e8f0; }
.logo-version { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #475569; }

/* Info badge */
.info-badge {
    display: inline-block;
    background: rgba(59,130,246,0.12);
    border: 1px solid #1e3a5f;
    border-radius: 6px;
    padding: 3px 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #60a5fa;
    margin-left: 8px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HEADER + TOP NAV
# ─────────────────────────────────────────────
st.markdown("""
<div class="logo-area">
  <div class="logo-icon">🔐</div>
  <div>
    <div class="logo-text">CryptoCalc</div>
    <div class="logo-version">v1.0 · Calculadora Criptográfica</div>
  </div>
</div>
""", unsafe_allow_html=True)

MODULOS = [
    ("1", "⊕ Mat. Modular"),
    ("2", "🔤 Criptografía Clásica"),
    ("3", "🛡️ Criptografía Moderna"),
    ("4", "# Algoritmos Hash"),
    ("5", "⟨⟩ Codificación"),
    ("6", "🧂 Uso de SALT"),
]

if "modulo_activo" not in st.session_state:
    st.session_state.modulo_activo = "1"

cols_nav = st.columns(len(MODULOS))
for col, (key, label) in zip(cols_nav, MODULOS):
    with col:
        activo = st.session_state.modulo_activo == key
        css_class = "active" if activo else "inactive"
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.modulo_activo = key
            st.rerun()

st.markdown("<hr style='border-color:#1e2d4a; margin:0 0 28px 0'>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# MÓDULO 1: OPERACIONES MATEMÁTICAS MODULARES
# ─────────────────────────────────────────────────────────
if st.session_state.modulo_activo == "1":

    st.markdown('<div class="page-title">Operaciones Matemáticas Modulares</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">// Módulo 1 · Aritmética modular paso a paso</div>', unsafe_allow_html=True)

    submenu_labels = [
        "1.1 · a mod n = b",
        "1.2 · Inverso Aditivo",
        "1.3 · Inverso XOR",
        "1.4 · MCD e Inverso Multiplicativo",
        "1.5 · Inverso Multiplicativo (Tradicional)",
        "1.6 · Algoritmo Extendido de Euclides (AEE)",
    ]
    opcion = st.selectbox("**Selecciona la operación:**", submenu_labels, label_visibility="visible")

    st.markdown("---")

    # ── 1.1 Módulo de dos números ──────────────────────────
    if opcion == submenu_labels[0]:
        st.markdown("### 1.1 · Calcular el módulo de dos números")
        st.markdown('<span class="info-badge">a mod n = b</span>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Valor de **a** (dividendo)", value=17, step=1, key="mod_a")
        with col2:
            n = st.number_input("Valor de **n** (módulo)", value=5, min_value=1, step=1, key="mod_n")

        if st.button("Calcular módulo", key="btn_mod"):
            if n == 0:
                st.error("El módulo n no puede ser 0.")
            else:
                a = int(a); n = int(n)
                cociente = a // n
                resto = a % n
                verificacion = cociente * n + resto

                pasos = f"""
<div class="process-box">
  <div class="process-title">📋 Proceso de cálculo — a mod n</div>
  <span class="step-num">1</span> Datos de entrada: a = {a}, n = {n}<br>
  <span class="step-num">2</span> Fórmula: a = n · q + r, donde q es el cociente y r el residuo<br>
  <span class="step-num">3</span> Calcular cociente (división entera): q = ⌊{a} ÷ {n}⌋ = {cociente}<br>
  <span class="step-num">4</span> Calcular residuo: r = {a} − ({n} × {cociente}) = {a} − {n*cociente} = <strong style="color:#93c5fd">{resto}</strong><br>
  <span class="step-num">5</span> Verificación: {n} × {cociente} + {resto} = {verificacion} ✓<br>
  <span class="step-num">6</span> El residuo siempre cumple 0 ≤ r < n → 0 ≤ {resto} < {n} ✓
</div>
<div class="result-highlight result-ok">
  ✅ &nbsp; {a} mod {n} = <strong>{resto}</strong>
</div>
"""
                st.markdown(pasos, unsafe_allow_html=True)

    # ── 1.2 Inverso Aditivo ───────────────────────────────
    elif opcion == submenu_labels[1]:
        st.markdown("### 1.2 · Calcular el Inverso Aditivo")
        st.markdown('<span class="info-badge">-a mod n</span>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Valor de **a**", value=3, step=1, key="ia_a")
        with col2:
            n = st.number_input("Módulo **n**", value=7, min_value=1, step=1, key="ia_n")

        if st.button("Calcular inverso aditivo", key="btn_ia"):
            a = int(a); n = int(n)
            inv_ad = (-a) % n
            verificacion = (a + inv_ad) % n

            pasos = f"""
<div class="process-box">
  <div class="process-title">📋 Proceso — Inverso Aditivo</div>
  <span class="step-num">1</span> Definición: el inverso aditivo de <em>a</em> módulo <em>n</em> es el número <em>b</em> tal que:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a + b ≡ 0 (mod n)<br><br>
  <span class="step-num">2</span> Datos: a = {a}, n = {n}<br>
  <span class="step-num">3</span> Fórmula directa: b = (-a) mod n = (-{a}) mod {n}<br>
  <span class="step-num">4</span> Calcular: -a = -{a}<br>
  <span class="step-num">5</span> Reducir al rango positivo: (-{a}) mod {n} = {inv_ad}<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (Se suma {n} tantas veces como sea necesario para obtener valor positivo)<br>
  <span class="step-num">6</span> Verificación: ({a} + {inv_ad}) mod {n} = {a + inv_ad} mod {n} = {verificacion}<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; → El resultado debe ser 0: {'✓ Correcto' if verificacion == 0 else '✗ Error'}
</div>
<div class="result-highlight result-ok">
  ✅ &nbsp; El inverso aditivo de {a} (mod {n}) es <strong>{inv_ad}</strong><br>
  <small style="opacity:0.7">{a} + {inv_ad} ≡ 0 (mod {n})</small>
</div>
"""
            st.markdown(pasos, unsafe_allow_html=True)

    # ── 1.3 Inverso XOR ───────────────────────────────────
    elif opcion == submenu_labels[2]:
        st.markdown("### 1.3 · Calcular el Inverso XOR")
        st.markdown('<span class="info-badge">a ⊕ b = 0  →  b = a</span>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Valor de **a** (entero)", value=45, min_value=0, step=1, key="xor_a")
        with col2:
            bits = st.selectbox("Cantidad de bits", [4, 8, 16, 32], index=1, key="xor_bits")

        if st.button("Calcular inverso XOR", key="btn_xor"):
            a = int(a); bits = int(bits)
            max_val = (1 << bits) - 1
            if a > max_val:
                st.error(f"El valor {a} supera el máximo permitido con {bits} bits ({max_val}).")
            else:
                inv_xor = a ^ max_val   # XOR con todos 1s = complemento a 1 = inverso XOR
                verificacion = a ^ inv_xor
                a_bin = format(a, f'0{bits}b')
                inv_bin = format(inv_xor, f'0{bits}b')
                mask_bin = format(max_val, f'0{bits}b')
                ver_bin = format(verificacion, f'0{bits}b')

                pasos = f"""
<div class="process-box">
  <div class="process-title">📋 Proceso — Inverso XOR</div>
  <span class="step-num">1</span> El inverso XOR de <em>a</em> es el valor <em>b</em> tal que: a ⊕ b = 0<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; En XOR, un número es su propio inverso: a ⊕ a = 0<br><br>
  <span class="step-num">2</span> Datos: a = {a} (decimal), bits = {bits}<br>
  <span class="step-num">3</span> Representación binaria de a:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a = {a_bin} ({bits} bits)<br>
  <span class="step-num">4</span> El inverso XOR es el propio valor a:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b = a = {a_bin}<br>
  <span class="step-num">5</span> Verificación: a ⊕ b = {a_bin} ⊕ {inv_bin} = {ver_bin} = {verificacion}<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; → El resultado debe ser 0: {'✓ Correcto' if verificacion == 0 else '⚠'}<br><br>
  <span class="step-num">6</span> Nota adicional — Complemento XOR con máscara {bits} bits ({mask_bin}):<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a ⊕ {mask_bin} = {inv_bin} = {inv_xor} (complemento a 1)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Verificación complemento: {a_bin} ⊕ {inv_bin} = {format(a ^ inv_xor, f'0{bits}b')} = {a ^ inv_xor}
</div>
<div class="result-highlight result-ok">
  ✅ &nbsp; Inverso XOR de {a}: <strong>b = {a}</strong> (a ⊕ a = 0)<br>
  <small style="opacity:0.7">Complemento a 1 con máscara {bits}-bits: {inv_xor} ({inv_bin})</small>
</div>
"""
                st.markdown(pasos, unsafe_allow_html=True)

    # ── 1.4 MCD e Inverso Multiplicativo ─────────────────
    elif opcion == submenu_labels[3]:
        st.markdown("### 1.4 · MCD e Inverso Multiplicativo")
        st.markdown('<span class="info-badge">mcd(a, n) → ¿existe a⁻¹ mod n?</span>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Valor de **a**", value=3, min_value=1, step=1, key="mcd_a")
        with col2:
            n = st.number_input("Módulo **n**", value=7, min_value=2, step=1, key="mcd_n")

        if st.button("Calcular MCD", key="btn_mcd"):
            a = int(a); n = int(n)

            # Proceso de Euclides paso a paso
            pasos_euclides = []
            x, y = max(a, n), min(a, n)
            while y != 0:
                q = x // y
                r = x % y
                pasos_euclides.append((x, y, q, r))
                x, y = y, r
            mcd = x
            existe = mcd == 1

            tabla_filas = ""
            for i, (xi, yi, qi, ri) in enumerate(pasos_euclides):
                tabla_filas += f"<tr><td>{i+1}</td><td>{xi}</td><td>{yi}</td><td>{qi}</td><td>{'<strong style=color:#6ee7b7>' if ri==0 else ''}{ri}{'</strong>' if ri==0 else ''}</td></tr>"

            color_res = "result-ok" if existe else "result-error"
            msg_inv = f"✅ Existe el inverso multiplicativo de {a} mod {n} (MCD = 1)" if existe else f"❌ NO existe el inverso multiplicativo (MCD = {mcd} ≠ 1)"

            pasos_html = f"""
<div class="process-box">
  <div class="process-title">📋 Proceso — Algoritmo de Euclides para MCD({a}, {n})</div>
  <span class="step-num">1</span> Para calcular MCD({a}, {n}) aplicamos el algoritmo de Euclides:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Repetir: MCD(a, b) = MCD(b, a mod b) hasta que b = 0<br><br>
  <span class="step-num">2</span> Tabla de iteraciones:<br>
  <table class="aee-table" style="margin-top:10px">
    <tr><th>Paso</th><th>a</th><th>b</th><th>q = ⌊a/b⌋</th><th>r = a mod b</th></tr>
    {tabla_filas}
  </table>
  <br>
  <span class="step-num">3</span> Cuando el residuo = 0, el MCD es el último divisor no nulo.<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MCD({a}, {n}) = <strong style="color:#93c5fd">{mcd}</strong><br><br>
  <span class="step-num">4</span> Condición para inverso multiplicativo: MCD(a, n) = 1 (números coprimos)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; MCD({a}, {n}) = {mcd} → {'Son coprimos ✓' if existe else 'NO son coprimos ✗'}
</div>
<div class="result-highlight {color_res}">
  {msg_inv}
</div>
"""
            st.markdown(pasos_html, unsafe_allow_html=True)

    # ── 1.5 Inverso Multiplicativo Tradicional ────────────
    elif opcion == submenu_labels[4]:
        st.markdown("### 1.5 · Inverso Multiplicativo — Método Tradicional")
        st.markdown('<span class="info-badge">a · x ≡ 1 (mod n) → buscar x por fuerza bruta</span>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Valor de **a**", value=3, min_value=1, step=1, key="mt_a")
        with col2:
            n = st.number_input("Módulo **n**", value=7, min_value=2, step=1, key="mt_n")

        if st.button("Calcular por método tradicional", key="btn_mt"):
            a = int(a); n = int(n)
            mcd = math.gcd(a, n)

            if mcd != 1:
                st.markdown(f"""
<div class="result-highlight result-error">
  ❌ No existe el inverso multiplicativo de {a} mod {n}<br>
  MCD({a}, {n}) = {mcd} ≠ 1 → Los números no son coprimos
</div>
""", unsafe_allow_html=True)
            else:
                # Buscar por fuerza bruta
                filas = ""
                inv = None
                for x in range(1, n):
                    prod = (a * x) % n
                    es_inv = prod == 1
                    if es_inv:
                        inv = x
                    color = "color:#6ee7b7; font-weight:700;" if es_inv else ""
                    check = " ← ✅ INVERSO" if es_inv else ""
                    filas += f"<tr><td>x = {x}</td><td>{a} × {x} = {a*x}</td><td>{a*x} mod {n} = <span style='{color}'>{prod}</span>{check}</td></tr>"

                pasos_html = f"""
<div class="process-box">
  <div class="process-title">📋 Proceso — Método Tradicional (Búsqueda directa)</div>
  <span class="step-num">1</span> Objetivo: encontrar x tal que  a · x ≡ 1 (mod n)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Es decir: {a} · x mod {n} = 1<br><br>
  <span class="step-num">2</span> Verificar existencia: MCD({a}, {n}) = {mcd} = 1 → Existe ✓<br><br>
  <span class="step-num">3</span> Probar todos los valores x ∈ {{1, 2, ..., {n-1}}}:<br>
  <table class="aee-table" style="margin-top:10px">
    <tr><th>x</th><th>Producto</th><th>Resultado mod {n}</th></tr>
    {filas}
  </table>
  <br>
  <span class="step-num">4</span> Se encontró que x = {inv} cumple: {a} × {inv} = {a*inv}, y {a*inv} mod {n} = {(a*inv)%n} ✓
</div>
<div class="result-highlight result-ok">
  ✅ &nbsp; El inverso multiplicativo de {a} (mod {n}) es <strong>{inv}</strong><br>
  <small style="opacity:0.7">{a} × {inv} ≡ 1 (mod {n})</small>
</div>
"""
                st.markdown(pasos_html, unsafe_allow_html=True)

    # ── 1.6 AEE — Algoritmo Extendido de Euclides ─────────
    elif opcion == submenu_labels[5]:
        st.markdown("### 1.6 · Algoritmo Extendido de Euclides (AEE)")
        st.markdown('<span class="info-badge">Inverso multiplicativo con tabla completa</span>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Valor de **a**", value=3, min_value=1, step=1, key="aee_a")
        with col2:
            n = st.number_input("Módulo **n**", value=7, min_value=2, step=1, key="aee_n")

        if st.button("Calcular con AEE", key="btn_aee"):
            a = int(a); n = int(n)
            mcd = math.gcd(a, n)

            if mcd != 1:
                st.markdown(f"""
<div class="result-highlight result-error">
  ❌ No existe el inverso multiplicativo de {a} mod {n}<br>
  MCD({a}, {n}) = {mcd} ≠ 1 → No se puede aplicar AEE para obtener inverso
</div>
""", unsafe_allow_html=True)
            else:
                # Algoritmo Extendido de Euclides
                # Tabla: ronda, ri, qi, si, ti
                tabla = []
                r0, r1 = n, a
                s0, s1 = 1, 0
                t0, t1 = 0, 1
                ronda = 0
                tabla.append((ronda, r0, "-", s0, t0))
                ronda = 1
                tabla.append((ronda, r1, "-", s1, t1))

                ronda = 2
                while r1 != 0:
                    q = r0 // r1
                    r2 = r0 - q * r1
                    s2 = s0 - q * s1
                    t2 = t0 - q * t1
                    tabla.append((ronda, r2, q, s2, t2))
                    r0, s0, t0 = r1, s1, t1
                    r1, s1, t1 = r2, s2, t2
                    ronda += 1
                    if r1 == 0:
                        break

                total_rondas = ronda - 2  # rondas de cálculo reales
                # El inverso es t donde r = 1 (antes del 0 final)
                inv_t = None
                for row in tabla:
                    if row[1] == 1:
                        inv_t = row[4]
                        break
                inv_final = inv_t % n if inv_t is not None else None

                # Construir tabla HTML
                filas_html = ""
                for row in tabla:
                    rnd, ri, qi, si, ti = row
                    qi_str = str(qi) if qi != "-" else "-"
                    highlight = "background:rgba(59,130,246,0.15); font-weight:700; color:#93c5fd;" if ri == 1 else ""
                    filas_html += f"<tr style='{highlight}'><td>{rnd}</td><td>{ri}</td><td>{qi_str}</td><td>{si}</td><td>{ti}</td></tr>"

                pasos_html = f"""
<div class="process-box">
  <div class="process-title">📋 Proceso — Algoritmo Extendido de Euclides</div>
  <span class="step-num">1</span> Objetivo: encontrar x tal que  a·x ≡ 1 (mod n)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Usando: a = {a},  n = {n}<br><br>
  <span class="step-num">2</span> El AEE resuelve la identidad de Bézout: n·s + a·t = MCD(n, a)<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Cuando MCD = 1: n·s + a·t = 1 → a·t ≡ 1 (mod n) → t es el inverso<br><br>
  <span class="step-num">3</span> Inicialización de la tabla:<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fila 0: r = n = {n}, s = 1, t = 0<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fila 1: r = a = {a}, s = 0, t = 1<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Fórmulas: r(i) = r(i-2) - q(i)·r(i-1), &nbsp; s(i) = s(i-2) - q(i)·s(i-1), &nbsp; t(i) = t(i-2) - q(i)·t(i-1)<br><br>
  <span class="step-num">4</span> Tabla del Algoritmo Extendido de Euclides ({total_rondas} ronda(s) de cálculo):<br>
  <table class="aee-table" style="margin-top:10px">
    <tr><th>Ronda</th><th>r</th><th>q = ⌊r(prev)/r⌋</th><th>s</th><th>t</th></tr>
    {filas_html}
  </table>
  <br>
  <span class="step-num">5</span> Se detiene cuando r = 0. El MCD es el último r ≠ 0 = 1 ✓<br>
  <span class="step-num">6</span> El inverso multiplicativo es el valor <strong>t</strong> en la fila donde r = 1: t = {inv_t}<br>
  <span class="step-num">7</span> Ajustar al rango positivo: {inv_t} mod {n} = <strong style="color:#6ee7b7">{inv_final}</strong><br>
  <span class="step-num">8</span> Verificación: {a} × {inv_final} = {a * inv_final},  {a * inv_final} mod {n} = {(a * inv_final) % n} {'✓' if (a * inv_final) % n == 1 else '✗'}
</div>
<div class="result-highlight result-ok">
  ✅ &nbsp; Inverso multiplicativo de {a} (mod {n}) = <strong>{inv_final}</strong><br>
  <small style="opacity:0.7">Calculado en {total_rondas} ronda(s) · {a} × {inv_final} ≡ 1 (mod {n})</small>
</div>
"""
                st.markdown(pasos_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# MÓDULOS 2–6: PRÓXIMAMENTE
# ─────────────────────────────────────────────────────────
else:
    nombres = {
        "2": ("🔤 Criptografía Clásica", "Cifrados históricos: César, Vernam, ATBASH, Afín y más"),
        "3": ("🛡️ Criptografía Moderna", "Diffie-Hellman, RSA, Exponenciación rápida"),
        "4": ("# Algoritmos Hash", "MD5, SHA-256, SHA-512 con proceso detallado"),
        "5": ("⟨⟩ Codificación", "ASCII, Hexadecimal, Binario, Base64"),
        "6": ("🧂 Uso de SALT", "Hash de claves con sal: MD5, SHA-256, SHA-512"),
    }
    nombre, desc = nombres.get(st.session_state.modulo_activo, ("Módulo", ""))
    st.markdown(f'<div class="page-title">{nombre}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">// {desc}</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="calc-card" style="text-align:center; padding: 60px 30px;">
  <div style="font-size:3rem; margin-bottom:16px">🚧</div>
  <div style="font-family:'Syne',sans-serif; font-size:1.3rem; color:#60a5fa; font-weight:700; margin-bottom:8px">Módulo en construcción</div>
  <div style="color:#64748b; font-family:'JetBrains Mono',monospace; font-size:13px">Este módulo estará disponible en la próxima versión</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#334155; font-family:'JetBrains Mono',monospace; font-size:11px; padding:10px 0">
  CryptoCalc v1.0 · Calculadora Criptográfica · Módulo 1 activo
</div>
""", unsafe_allow_html=True)