# "Çalıştığımız alanlar" bölümü için mini hareketli çizimler (her biri 120x80).
L = "#033246"; B = "#7A3848"; S = "#F2A900"; G = "#9AA4A0"; A = "#E3E6E2"; W = "#FFFFFF"
SU = "#5DADE2"; YE = "#2FA35A"; KI = "#C0392B"; KO = "#5D6A72"

def sv(body, ad):
    return (f'<svg viewBox="0 0 120 80" role="img" aria-label="{ad}" xmlns="http://www.w3.org/2000/svg">'
            f'<line x1="4" y1="73" x2="116" y2="73" stroke="{G}" stroke-width="2"/>{body}</svg>')

def rot(cx, cy):  # belirli bir nokta etrafında döndürme
    return f'transform-box:view-box;transform-origin:{cx}px {cy}px'

def d(s):  # animation-delay
    return f'animation-delay:{s}s'

# ---------------- MAKİNELER ----------------
def geri_donusum():
    b = (f'<path d="M40 22 H80 L70 40 H50 Z" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="46" y="40" width="28" height="22" fill="{KO}" stroke="{L}" stroke-width="2"/>'
         f'<g class="al-spin" style="{rot(60, 51)}"><path d="M52 51 H68 M60 43 V59" stroke="{S}" stroke-width="2.5"/></g>'
         f'<rect x="56" y="62" width="8" height="10" fill="{KO}" stroke="{L}" stroke-width="1.5"/>')
    for i, x in enumerate([54, 62, 58]):
        b += f'<rect class="al-fall" x="{x}" y="4" width="6" height="12" rx="2" fill="#7FB3D5" stroke="{L}" stroke-width="1" style="{d(i*0.55)}"/>'
    for i in range(3):
        b += f'<circle class="al-drop" cx="{57+i*3}" cy="66" r="1.8" fill="#7FB069" style="{d(i*0.4)}"/>'
    b += (f'<g class="al-spin" style="{rot(98, 30)};animation-duration:6s"><path d="M98 20 A10 10 0 0 1 107 34" fill="none" stroke="{YE}" stroke-width="3"/>'
          f'<path d="M89 34 A10 10 0 0 1 93 21" fill="none" stroke="{YE}" stroke-width="3"/><path d="M105 38 L108 33 L103 32 Z" fill="{YE}"/></g>')
    return sv(b, "Plastik geri dönüşüm makinesi: şişeler kırıcıya düşüyor, granül çıkıyor")

def enjeksiyon():
    b = (f'<rect x="8" y="34" width="60" height="16" rx="3" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<path d="M24 34 L18 18 H38 L32 34 Z" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<g class="al-push"><rect x="12" y="38" width="44" height="8" fill="{G}"/><path d="M14 38 l4 8 M22 38 l4 8 M30 38 l4 8 M38 38 l4 8 M46 38 l4 8" stroke="{L}" stroke-width="1.2"/></g>'
         f'<rect x="68" y="30" width="16" height="24" fill="{KO}" stroke="{L}" stroke-width="2"/>'
         f'<rect class="al-mold" x="84" y="30" width="16" height="24" fill="{KO}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="10" y="50" width="96" height="22" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<rect class="al-part" x="86" y="58" width="10" height="8" rx="2" fill="{S}" stroke="{L}"/>')
    for i in range(4): b += f'<rect class="al-heat" x="{40+i*7}" y="31" width="5" height="3" fill="{KI}" style="{d(i*0.2)}"/>'
    return sv(b, "Plastik enjeksiyon makinesi: vida ileri gidiyor, kalıp açılıp parça düşüyor")

def kirma():
    b = (f'<path d="M34 6 H86 L78 24 H42 Z" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="38" y="24" width="44" height="30" fill="{KO}" stroke="{L}" stroke-width="2"/>')
    for cx in (52, 68):
        b += (f'<g class="al-spin" style="{rot(cx, 39)};animation-duration:.9s"><circle cx="{cx}" cy="39" r="9" fill="#3E4A54"/>'
              f'<path d="M{cx} 30 L{cx+3} 36 L{cx} 39 Z M{cx+9} 39 L{cx+3} 42 L{cx} 39 Z M{cx} 48 L{cx-3} 42 L{cx} 39 Z M{cx-9} 39 L{cx-3} 36 L{cx} 39 Z" fill="{S}"/></g>')
    b += f'<path d="M44 54 L50 66 H70 L76 54" fill="{A}" stroke="{L}" stroke-width="2"/>'
    for i in range(3):
        b += f'<rect class="al-fall" x="{50+i*8}" y="8" width="8" height="6" fill="#B0A08A" stroke="{L}" stroke-width=".8" style="{d(i*0.5)}"/>'
    for i in range(4):
        b += f'<circle class="al-drop" cx="{54+i*4}" cy="58" r="1.5" fill="#B0A08A" style="{d(i*0.3)}"/>'
    b += f'<rect x="84" y="36" width="20" height="16" rx="3" fill="#5D7186" stroke="{L}" stroke-width="1.5"/><line x1="82" y1="39" x2="84" y2="39" stroke="{L}" stroke-width="2"/>'
    return sv(b, "Plastik kırma makinesi: bıçaklar dönüyor, parçalar kırılıp aşağı düşüyor")

def ekstruder():
    b = (f'<path d="M14 18 L10 4 H28 L24 18 Z" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="8" y="18" width="62" height="14" rx="3" fill="{A}" stroke="{L}" stroke-width="2"/>')
    for i in range(5): b += f'<rect class="al-heat" x="{30+i*8}" y="15" width="6" height="3" fill="{KI}" style="{d(i*0.15)}"/>'
    b += (f'<rect x="70" y="20" width="6" height="10" fill="{KO}" stroke="{L}"/>'
          f'<path class="al-flow" d="M76 25 H100" stroke="#7FB069" stroke-width="3" stroke-dasharray="6 3"/>'
          f'<rect x="98" y="16" width="14" height="18" fill="{KO}" stroke="{L}" stroke-width="1.5"/>'
          f'<g class="al-spin" style="{rot(105, 25)};animation-duration:.5s"><path d="M105 19 V31" stroke="{S}" stroke-width="2"/></g>'
          f'<path d="M94 54 H116 L112 70 H98 Z" fill="{A}" stroke="{L}" stroke-width="2"/>'
          f'<rect x="8" y="32" width="62" height="40" fill="none"/><rect x="14" y="32" width="8" height="40" fill="{G}"/><rect x="56" y="32" width="8" height="40" fill="{G}"/>')
    for i in range(4): b += f'<circle class="al-drop" cx="{101+i*3}" cy="40" r="2" fill="#7FB069" style="{d(i*0.3)}"/>'
    return sv(b, "Ekstrüder ve granül hattı: eriyik çubuk çıkıyor, kesiciyle granül olup düşüyor")

def paketleme():
    b = (f'<rect x="4" y="58" width="112" height="6" rx="3" fill="{G}" stroke="{L}" stroke-width="1.2"/>'
         f'<rect x="48" y="10" width="26" height="10" fill="{KO}" stroke="{L}" stroke-width="1.5"/>'
         f'<g class="al-press" style="animation-duration:2.4s"><rect x="58" y="20" width="6" height="16" fill="{G}"/><rect x="50" y="36" width="22" height="5" fill="{B}"/></g>')
    for i in range(3):
        b += (f'<g class="al-box" style="{d(-i*0.8)}"><rect x="2" y="40" width="22" height="18" fill="#D9B27A" stroke="#8A6A3A" stroke-width="1.2"/>'
              f'<rect x="10" y="40" width="6" height="18" fill="#C9A06A"/></g>')
    return sv(b, "Paketleme makinesi: kutular bantta ilerliyor, bant yapıştırıcı iniyor")

def dolum():
    b = f'<rect x="10" y="8" width="100" height="12" rx="2" fill="{A}" stroke="{L}" stroke-width="2"/>'
    for i, x in enumerate([26, 60, 94]):
        b += (f'<path d="M{x-3} 20 H{x+3} L{x+1} 27 H{x-1} Z" fill="{KO}"/>'
              f'<line class="al-stream" x1="{x}" y1="27" x2="{x}" y2="44" stroke="{SU}" stroke-width="2" style="{d(i*0.3)}"/>'
              f'<path d="M{x-9} 44 H{x+9} V70 H{x-9} Z" fill="{W}" stroke="{L}" stroke-width="1.6"/>'
              f'<rect class="al-fill" x="{x-8}" y="46" width="16" height="23" fill="{SU}" opacity=".75" style="{d(i*0.3)}"/>')
    return sv(b, "Dolum ve dozaj makinesi: memelerden şişelere sıvı doluyor")

def konveyor():
    b = f'<rect x="6" y="50" width="108" height="10" rx="5" fill="{G}" stroke="{L}" stroke-width="1.5"/>'
    for x in (12, 36, 60, 84, 108):
        b += f'<g class="al-spin" style="{rot(x, 55)};animation-duration:1s"><circle cx="{x}" cy="55" r="4" fill="{A}" stroke="{L}"/><line x1="{x-3}" y1="55" x2="{x+3}" y2="55" stroke="{L}"/></g>'
    b += f'<line x1="20" y1="60" x2="20" y2="72" stroke="{L}" stroke-width="2"/><line x1="100" y1="60" x2="100" y2="72" stroke="{L}" stroke-width="2"/>'
    for i in range(3):
        b += f'<rect class="al-box" x="2" y="34" width="18" height="16" fill="#D9B27A" stroke="#8A6A3A" stroke-width="1.2" style="{d(-i*1)}"/>'
    return sv(b, "Konveyör: makaralar dönüyor, kutular bant üzerinde taşınıyor")

def pres():
    b = (f'<rect x="20" y="6" width="80" height="12" fill="{KO}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="24" y="18" width="6" height="54" fill="{G}" stroke="{L}"/><rect x="90" y="18" width="6" height="54" fill="{G}" stroke="{L}"/>'
         f'<rect x="54" y="18" width="12" height="10" fill="{A}" stroke="{L}"/>'
         f'<g class="al-press"><rect x="57" y="28" width="6" height="10" fill="{G}"/><rect x="40" y="38" width="40" height="8" fill="{L}"/></g>'
         f'<rect x="38" y="56" width="44" height="6" fill="#B7C3BF" stroke="{L}"/><rect x="34" y="62" width="52" height="10" fill="{KO}" stroke="{L}" stroke-width="2"/>')
    b += f'<rect class="al-blink" x="74" y="9" width="4" height="4" fill="{YE}"/>'
    return sv(b, "Hidrolik pres: piston aşağı inip parçayı presliyor")

def test_standi():
    b = (f'<rect x="8" y="44" width="36" height="28" rx="3" fill="#5D7186" stroke="{L}" stroke-width="2"/>'
         f'<g class="al-spin" style="{rot(26, 58)};animation-duration:.8s"><path d="M26 50 V66 M18 58 H34" stroke="{S}" stroke-width="2"/></g>'
         f'<path d="M44 58 H66 V36 H76" fill="none" stroke="{G}" stroke-width="5"/>'
         f'<path class="al-flow" d="M44 58 H66 V36 H76" fill="none" stroke="{S}" stroke-width="2" stroke-dasharray="4 4"/>'
         f'<circle cx="90" cy="36" r="20" fill="{W}" stroke="{L}" stroke-width="2.4"/>'
         f'<path d="M76 44 A16 16 0 0 1 104 44" fill="none" stroke="{YE}" stroke-width="3"/><path d="M100 50 A16 16 0 0 0 104 44" fill="none" stroke="{KI}" stroke-width="3"/>'
         f'<line class="al-needle" x1="90" y1="36" x2="90" y2="22" stroke="{B}" stroke-width="2.5" stroke-linecap="round" style="{rot(90, 36)}"/>'
         f'<circle cx="90" cy="36" r="2.5" fill="{L}"/><text x="90" y="52" text-anchor="middle" font-family="Barlow,Arial" font-size="7" fill="{L}">bar</text>')
    return sv(b, "Hidrolik test standı: pompa çalışıyor, manometre basıncı gösteriyor")

def mikser():
    b = (f'<rect x="50" y="4" width="20" height="12" rx="2" fill="#5D7186" stroke="{L}" stroke-width="1.5"/>'
         f'<line x1="60" y1="16" x2="60" y2="58" stroke="{L}" stroke-width="2.5"/>'
         f'<path d="M30 20 H90 V64 Q60 76 30 64 Z" fill="{W}" stroke="{L}" stroke-width="2.2"/>'
         f'<path d="M32 40 H88 V64 Q60 74 32 64 Z" fill="#E8D3A0" opacity=".9"/>'
         f'<g class="al-mix" style="{rot(60, 54)}"><path d="M48 50 L60 54 L48 58 Z M72 50 L60 54 L72 58 Z" fill="{B}"/></g>'
         f'<path class="al-wave" d="M34 40 Q46 36 58 40 T86 40" fill="none" stroke="#C9A85E" stroke-width="2"/>')
    return sv(b, "Mikser: motor karıştırıcıyı döndürüyor, tanktaki ürün karışıyor")

def firin():
    b = (f'<rect x="14" y="14" width="70" height="58" rx="4" fill="{KO}" stroke="{L}" stroke-width="2.2"/>'
         f'<rect x="22" y="24" width="54" height="36" fill="#3B1F1A"/>'
         f'<rect class="al-glow" x="22" y="24" width="54" height="36" fill="#E67E22"/>'
         f'<rect x="28" y="44" width="42" height="8" fill="#9C9C9C" stroke="#4A4A4A"/>'
         f'<rect x="90" y="14" width="14" height="52" rx="7" fill="{W}" stroke="{L}" stroke-width="1.6"/>'
         f'<rect class="al-fill" x="94" y="22" width="6" height="40" rx="3" fill="{KI}"/>')
    for i in range(3):
        b += f'<path class="al-rise" d="M{34+i*14} 12 q3 -4 0 -8 q-3 -4 0 -8" fill="none" stroke="#E67E22" stroke-width="2" style="{d(i*0.5)}"/>'
    return sv(b, "Fırın ve ısıl işlem: fırın kızarıyor, sıcaklık yükseliyor")

def kesim():
    b = (f'<rect x="8" y="50" width="104" height="8" fill="{KO}" stroke="{L}" stroke-width="1.5"/>'
         f'<rect x="10" y="40" width="74" height="10" fill="#B7C3BF" stroke="{L}" stroke-width="1.5"/>'
         f'<rect x="76" y="6" width="34" height="14" fill="#5D7186" stroke="{L}" stroke-width="1.5"/>'
         f'<line x1="92" y1="20" x2="92" y2="26" stroke="{L}" stroke-width="3"/>'
         f'<g class="al-spin" style="{rot(92, 34)};animation-duration:.6s"><circle cx="92" cy="34" r="12" fill="#D5DBDF" stroke="{L}" stroke-width="1.5"/>'
         + "".join(f'<path d="M92 22 l2 -3 l2 3 Z" fill="{L}" transform="rotate({k*45} 92 34)"/>' for k in range(8)) + '</g>')
    for i in range(4):
        b += f'<circle class="al-spark" cx="{80-i*4}" cy="{42-i*3}" r="1.6" fill="{S}" style="{d(i*0.15)}"/>'
    return sv(b, "Kesim ve işleme makinesi: testere dönüyor, malzeme kesiliyor")

# ---------------- TESİSLER ----------------
def aritma():
    b = (f'<rect x="6" y="30" width="62" height="42" fill="#8FB9C9" stroke="{L}" stroke-width="2"/>'
         f'<path d="M6 30 H68" stroke="{L}" stroke-width="2"/>'
         f'<line x1="10" y1="66" x2="64" y2="66" stroke="{G}" stroke-width="2"/>'
         f'<ellipse cx="94" cy="56" rx="20" ry="6" fill="#A9CFDD" stroke="{L}" stroke-width="2"/>'
         f'<path d="M74 56 V68 Q94 76 114 68 V56" fill="#A9CFDD" stroke="{L}" stroke-width="2"/>'
         f'<g class="al-spin" style="{rot(94, 56)};animation-duration:8s"><line x1="76" y1="56" x2="112" y2="56" stroke="{L}" stroke-width="1.6"/></g>'
         f'<path class="al-flow" d="M68 50 H76" stroke="{SU}" stroke-width="3" stroke-dasharray="3 3"/>'
         f'<rect x="20" y="8" width="18" height="14" fill="#5D7186" stroke="{L}" stroke-width="1.5"/><path d="M29 22 V30" stroke="{L}" stroke-width="2"/>')
    for i in range(7):
        b += f'<circle class="al-bubble" cx="{14+i*8}" cy="64" r="{1.8+(i%2)}" fill="{W}" opacity=".9" style="{d(i*0.25)}"/>'
    return sv(b, "Atık su arıtma tesisi: havalandırma havuzunda kabarcıklar yükseliyor, çöktürme havuzu dönüyor")

def fumigasyon():
    b = (f'<rect x="10" y="20" width="76" height="52" fill="#9FAEA9" stroke="{L}" stroke-width="2.2"/>'
         + "".join(f'<line x1="{18+i*10}" y1="24" x2="{18+i*10}" y2="68" stroke="#8A9893" stroke-width="2"/>' for i in range(7)) +
         f'<rect x="76" y="24" width="10" height="44" fill="#8A9893" stroke="{L}"/>'
         f'<path d="M94 30 L106 52 H82 Z" fill="{S}" stroke="#C98A00" stroke-width="1.5"/><text x="94" y="49" text-anchor="middle" font-family="Barlow,Arial" font-size="12" font-weight="700" fill="{L}">!</text>'
         f'<rect x="98" y="56" width="16" height="16" rx="2" fill="#5D7186" stroke="{L}"/><path d="M98 62 H86" stroke="{L}" stroke-width="2"/>')
    for i in range(4):
        b += f'<circle class="al-gas" cx="{28+i*14}" cy="{48-(i%2)*8}" r="7" fill="#B8E0B0" opacity=".7" style="{d(i*0.6)}"/>'
    return sv(b, "Fümigasyon sistemi: kapalı konteynerde gaz dolaşıyor, uyarı levhası")

def soguk_kurutma():
    b = (f'<rect x="10" y="10" width="84" height="62" rx="3" fill="#DCEAF2" stroke="{L}" stroke-width="2.2"/>'
         + "".join(f'<rect x="18" y="{24+i*14}" width="44" height="4" fill="{G}"/><rect x="{22+i*6}" y="{18+i*14}" width="10" height="6" rx="2" fill="#E3A35A"/>' for i in range(3)) +
         f'<circle cx="78" cy="40" r="12" fill="{W}" stroke="{L}" stroke-width="1.6"/>'
         f'<g class="al-spin" style="{rot(78, 40)};animation-duration:1s"><path d="M78 30 Q82 36 78 40 Q74 44 78 50 M68 40 Q74 44 78 40 Q82 36 88 40" fill="none" stroke="{SU}" stroke-width="2.5"/></g>'
         f'<g class="al-spin" style="{rot(106, 18)};animation-duration:7s"><path d="M106 8 V28 M97 13 L115 23 M115 13 L97 23" stroke="{SU}" stroke-width="2"/></g>')
    return sv(b, "Soğuk kurutma: soğuk odada fan dönüyor, raflardaki ürünler kuruyor")

def yem_gida():
    b = (f'<rect x="10" y="10" width="26" height="50" rx="2" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<path d="M10 10 L23 2 L36 10" fill="{A}" stroke="{L}" stroke-width="2"/><path d="M14 60 L23 70 L32 60" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="40" y="10" width="26" height="50" rx="2" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<path d="M40 10 L53 2 L66 10" fill="{A}" stroke="{L}" stroke-width="2"/><path d="M44 60 L53 70 L62 60" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<path d="M80 40 H112 L104 54 H88 Z" fill="{KO}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="88" y="54" width="16" height="18" fill="#5D7186" stroke="{L}" stroke-width="1.5"/>'
         f'<path d="M66 20 H96 V40" fill="none" stroke="{G}" stroke-width="5"/>')
    for i in range(4):
        b += f'<circle class="al-grain" cx="96" cy="30" r="1.8" fill="#D4A04A" style="{d(i*0.35)}"/>'
    return sv(b, "Yem ve gıda üretimi: silolardan hammadde değirmene akıyor")

def tekstil():
    b = (f'<rect x="8" y="16" width="104" height="8" fill="{KO}" stroke="{L}" stroke-width="1.5"/>'
         f'<line x1="14" y1="24" x2="14" y2="72" stroke="{L}" stroke-width="3"/><line x1="106" y1="24" x2="106" y2="72" stroke="{L}" stroke-width="3"/>')
    cols = ["#C0392B", "#2E86C1", "#F2A900", "#7FB069"]
    for i, x in enumerate([32, 52, 72, 92]):
        b += (f'<line class="al-flow" x1="{x}" y1="24" x2="{x}" y2="48" stroke="{cols[i]}" stroke-width="1.5" stroke-dasharray="3 2"/>'
              f'<g class="al-spin" style="{rot(x, 56)};animation-duration:.9s"><ellipse cx="{x}" cy="56" rx="7" ry="9" fill="{cols[i]}" stroke="{L}"/>'
              f'<path d="M{x-6} 53 H{x+6} M{x-6} 59 H{x+6}" stroke="{W}" stroke-width="1" opacity=".7"/></g>'
              f'<rect x="{x-3}" y="65" width="6" height="7" fill="{G}"/>')
    return sv(b, "Tekstil fabrikası: bobinler dönüyor, iplikler sarılıyor")

def hidrofor():
    b = (f'<rect x="72" y="12" width="26" height="54" rx="12" fill="#C0392B" stroke="{L}" stroke-width="2"/>'
         f'<rect x="80" y="66" width="10" height="6" fill="{G}"/>'
         f'<rect x="10" y="48" width="32" height="24" rx="3" fill="#2E86C1" stroke="{L}" stroke-width="2"/>'
         f'<g class="al-spin" style="{rot(26, 60)};animation-duration:.7s"><path d="M26 52 V68 M18 60 H34" stroke="{W}" stroke-width="2"/></g>'
         f'<path d="M42 56 H60 V40 H72" fill="none" stroke="{G}" stroke-width="6"/>'
         f'<path class="al-flow" d="M42 56 H60 V40 H72" fill="none" stroke="{SU}" stroke-width="3" stroke-dasharray="5 4"/>'
         f'<path d="M98 30 H114 V4" fill="none" stroke="{G}" stroke-width="6"/>'
         f'<path class="al-flow" d="M98 30 H114 V4" fill="none" stroke="{SU}" stroke-width="3" stroke-dasharray="5 4"/>'
         f'<circle cx="54" cy="22" r="10" fill="{W}" stroke="{L}" stroke-width="1.8"/>'
         f'<line class="al-needle" x1="54" y1="22" x2="54" y2="14" stroke="{B}" stroke-width="2" style="{rot(54, 22)}"/><path d="M54 32 V40" stroke="{L}" stroke-width="2"/>')
    return sv(b, "Pompa ve hidrofor istasyonu: pompa suyu basınçlı tanka ve tesisata basıyor")

def fabrika():
    b = (f'<rect x="10" y="32" width="84" height="40" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<path d="M10 32 L31 18 V32 L52 18 V32 L73 18 V32 L94 18 V32" fill="#CBD1CE" stroke="{L}" stroke-width="2"/>'
         f'<rect x="80" y="8" width="8" height="16" fill="{G}" stroke="{L}"/>')
    for i in range(4):
        b += f'<rect class="al-win" x="{18+i*18}" y="42" width="10" height="10" fill="{S}" stroke="{L}" style="{d(i*0.5)}"/>'
    b += f'<rect x="44" y="58" width="16" height="14" fill="#5D7186" stroke="{L}"/>'
    b += (f'<g class="al-spin" style="{rot(106, 50)};animation-duration:3s"><circle cx="106" cy="50" r="8" fill="none" stroke="{B}" stroke-width="4" stroke-dasharray="3 2.3"/><circle cx="106" cy="50" r="3" fill="{B}"/></g>')
    for i in range(3):
        b += f'<circle class="al-rise" cx="84" cy="6" r="{3+i}" fill="{G}" opacity=".6" style="{d(i*0.7)}"/>'
    return sv(b, "Fabrika ve atölye: üretim çalışıyor, dişli dönüyor")

def apartman():
    b = (f'<rect x="20" y="6" width="50" height="66" fill="{A}" stroke="{L}" stroke-width="2"/>'
         f'<rect x="76" y="26" width="34" height="46" fill="{A}" stroke="{L}" stroke-width="2"/>')
    k = 0
    for r in range(5):
        for c in range(3):
            b += f'<rect class="al-win" x="{26+c*14}" y="{12+r*11}" width="8" height="7" fill="{S}" stroke="{L}" stroke-width=".8" style="{d(((r*3+c)*0.37)%3)}"/>'
    for r in range(3):
        for c in range(2):
            b += f'<rect class="al-win" x="{82+c*14}" y="{32+r*12}" width="8" height="7" fill="{S}" stroke="{L}" stroke-width=".8" style="{d(((r*2+c)*0.53)%3)}"/>'
    b += f'<rect x="4" y="50" width="12" height="22" rx="1" fill="#ECEEED" stroke="{L}" stroke-width="1.4"/><rect class="al-blink" x="7" y="54" width="6" height="3" fill="{YE}"/>'
    return sv(b, "Apartman ve siteler: dairelerde ışıklar yanıyor, sayaç panosu çalışıyor")

def magaza():
    b = (f'<rect x="14" y="28" width="92" height="44" fill="{W}" stroke="{L}" stroke-width="2"/>'
         + "".join(f'<path d="M{14+i*18.4} 18 H{32.4+i*18.4} V28 Q{23.2+i*18.4} 34 {14+i*18.4} 28 Z" fill="{B if i%2==0 else W}" stroke="{L}" stroke-width="1.2"/>' for i in range(5)) +
         f'<rect x="22" y="38" width="40" height="26" fill="#CFE0EA" stroke="{L}" stroke-width="1.5"/>'
         f'<rect x="70" y="38" width="26" height="34" fill="#5D7186" stroke="{L}" stroke-width="1.5"/>'
         f'<rect class="al-blink" x="28" y="44" width="28" height="11" rx="2" fill="{YE}"/>'
         f'<text x="42" y="52.5" text-anchor="middle" font-family="Barlow,Arial" font-size="7.5" font-weight="700" fill="#fff">AÇIK</text>')
    for i in range(3):
        b += f'<circle class="al-win" cx="{36+i*24}" cy="9" r="3" fill="{S}" style="{d(i*0.4)}"/><line x1="{36+i*24}" y1="0" x2="{36+i*24}" y2="6" stroke="{L}"/>'
    return sv(b, "İşletmeler ve mağazalar: aydınlatma ve tabela çalışıyor")

MAKINELER = [("Plastik geri dönüşüm makineleri", geri_donusum), ("Plastik enjeksiyon makineleri", enjeksiyon),
             ("Plastik kırma makineleri", kirma), ("Ekstrüder ve granül hatları", ekstruder),
             ("Paketleme makineleri", paketleme), ("Dolum ve dozaj makineleri", dolum),
             ("Konveyör ve taşıma sistemleri", konveyor), ("Pres ve hidrolik makineler", pres),
             ("Hidrolik test standları", test_standi), ("Mikser ve karıştırıcılar", mikser),
             ("Fırın ve ısıl işlem sistemleri", firin), ("Kesim ve işleme makineleri", kesim)]
TESISLER = [("Atık su arıtma tesisleri", aritma), ("Fümigasyon sistemleri", fumigasyon),
            ("Soğuk kurutma", soguk_kurutma), ("Yem ve gıda üretimi", yem_gida),
            ("Tekstil fabrikaları", tekstil), ("Pompa ve hidrofor istasyonları", hidrofor),
            ("Fabrika ve atölyeler", fabrika), ("Apartman ve siteler", apartman),
            ("İşletmeler ve mağazalar", magaza)]

def grup(baslik, liste, i):
    kartlar = "".join(f'<li class="alan">{f()}<span>{ad}</span></li>' for ad, f in liste)
    return (f'<div class="sek-grup" data-reveal style="--i:{i}">\n        <h3>{baslik}</h3>\n'
            f'        <ul class="alan-izgara">{kartlar}</ul>\n      </div>')

CSS = r'''
/* Çalıştığımız alanlar: mini animasyonlu kartlar */
.sek-gruplar{grid-template-columns:1.33fr 1fr}
.alan-izgara{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.sek-grup:nth-child(2) .alan-izgara{grid-template-columns:repeat(3,1fr)}
.alan{background:var(--sac);border:1px solid var(--cizgi);border-bottom:3px solid var(--lacivert);display:flex;flex-direction:column;transition:transform .2s var(--yumusak),box-shadow .2s,border-color .2s}
.alan svg{display:block;width:100%;height:auto;background:#fff;border-bottom:1px solid var(--cizgi)}
.alan span{font-size:13.5px;font-weight:500;line-height:1.3;padding:8px 10px 10px;color:var(--murekkep)}
.alan:hover{transform:translateY(-3px);box-shadow:var(--golge);border-bottom-color:var(--sari)}
@media (max-width:1100px){.sek-gruplar{grid-template-columns:1fr}.alan-izgara,.sek-grup:nth-child(2) .alan-izgara{grid-template-columns:repeat(4,1fr)}}
@media (max-width:700px){.alan-izgara,.sek-grup:nth-child(2) .alan-izgara{grid-template-columns:repeat(2,1fr);gap:10px}}
.alan [class*="al-"]{transform-box:fill-box;transform-origin:center}
.gorundu .al-spin{animation:al-spin 2s linear infinite}
.gorundu .al-fall{animation:al-fall 1.6s ease-in infinite}
.gorundu .al-drop{animation:al-drop 1.2s ease-in infinite}
.gorundu .al-push{animation:al-push 2.4s ease-in-out infinite}
.gorundu .al-mold{animation:al-mold 2.4s ease-in-out infinite}
.gorundu .al-part{animation:al-part 2.4s ease-in infinite}
.gorundu .al-heat,.gorundu .al-blink{animation:al-blink 1.2s ease-in-out infinite}
.gorundu .al-press{animation:al-press 1.6s ease-in-out infinite}
.gorundu .al-box{animation:al-box 3s linear infinite}
.gorundu .al-stream{animation:al-stream 2.4s ease-in-out infinite}
.al-fill{transform-origin:center bottom!important}
.gorundu .al-fill{animation:al-fill 2.4s ease-in-out infinite}
.gorundu .al-flow{animation:al-flow .8s linear infinite}
.gorundu .al-needle{animation:al-needle 3s ease-in-out infinite}
.gorundu .al-mix{animation:al-mix .8s ease-in-out infinite}
.gorundu .al-wave{animation:al-wave 1.2s ease-in-out infinite}
.gorundu .al-glow{animation:al-glow 2s ease-in-out infinite}
.gorundu .al-rise{animation:al-rise 1.8s ease-out infinite}
.gorundu .al-spark{animation:al-spark .6s ease-out infinite}
.gorundu .al-bubble{animation:al-bubble 1.8s ease-in infinite}
.gorundu .al-gas{animation:al-gas 2.4s ease-in-out infinite}
.gorundu .al-grain{animation:al-grain 1.4s ease-in infinite}
.gorundu .al-win{animation:al-win 3s steps(1) infinite}
@keyframes al-spin{to{transform:rotate(360deg)}}
@keyframes al-fall{0%{transform:translateY(-6px);opacity:0}20%{opacity:1}80%{opacity:1}100%{transform:translateY(16px);opacity:0}}
@keyframes al-drop{0%{transform:translateY(0);opacity:0}20%{opacity:1}100%{transform:translateY(8px);opacity:0}}
@keyframes al-push{0%,100%{transform:translateX(0)}45%,60%{transform:translateX(10px)}}
@keyframes al-mold{0%,55%{transform:translateX(0)}70%,90%{transform:translateX(8px)}100%{transform:translateX(0)}}
@keyframes al-part{0%,65%{opacity:0;transform:translateY(-14px)}72%{opacity:1;transform:translateY(-14px)}95%{opacity:1;transform:translateY(0)}100%{opacity:0;transform:translateY(0)}}
@keyframes al-blink{50%{opacity:.25}}
@keyframes al-press{0%,100%{transform:translateY(0)}45%,55%{transform:translateY(10px)}}
@keyframes al-box{from{transform:translateX(-20px)}to{transform:translateX(110px)}}
@keyframes al-stream{0%,10%{opacity:0}20%,80%{opacity:1}90%,100%{opacity:0}}
@keyframes al-fill{0%{transform:scaleY(.05)}80%,100%{transform:scaleY(1)}}
@keyframes al-flow{to{stroke-dashoffset:-18}}
@keyframes al-needle{0%,100%{transform:rotate(-70deg)}50%{transform:rotate(55deg)}}
@keyframes al-mix{0%,100%{transform:scaleX(1)}50%{transform:scaleX(-1)}}
@keyframes al-wave{50%{transform:translateX(3px)}}
@keyframes al-glow{0%,100%{opacity:.55}50%{opacity:1}}
@keyframes al-rise{0%{transform:translateY(4px);opacity:0}30%{opacity:.9}100%{transform:translateY(-8px);opacity:0}}
@keyframes al-spark{0%{transform:translate(0,0);opacity:1}100%{transform:translate(-6px,-6px);opacity:0}}
@keyframes al-bubble{0%{transform:translateY(0);opacity:0}15%{opacity:1}100%{transform:translateY(-32px);opacity:0}}
@keyframes al-gas{0%,100%{transform:translate(0,0) scale(.8);opacity:.35}50%{transform:translate(4px,-6px) scale(1.15);opacity:.8}}
@keyframes al-grain{0%{transform:translateY(0);opacity:0}15%{opacity:1}100%{transform:translateY(14px);opacity:0}}
@keyframes al-win{0%,60%{opacity:1}61%,100%{opacity:.3}}
@media (prefers-reduced-motion:reduce){.alan [class*="al-"]{animation:none!important}.alan:hover{transform:none}}
'''

if __name__ == "__main__":
    import json, sys
    html = ('<div class="sek-gruplar">\n      ' + grup("Makineler", MAKINELER, 0) + '\n      '
            + grup("Tesisler", TESISLER, 1) + '\n    </div>\n\n    ')
    json.dump({"html": html, "css": CSS}, open(sys.argv[1], "w"), ensure_ascii=False)
    pv = ("<html><body style='margin:0;padding:8px;display:grid;grid-template-columns:repeat(7,170px);gap:8px;font:12px sans-serif'>"
          + "".join(f"<div class='gorundu'>{f()}<div>{ad}</div></div>" for ad, f in MAKINELER + TESISLER) + "</body></html>")
    open(sys.argv[1].replace('.json', '.html'), 'w').write(pv)
