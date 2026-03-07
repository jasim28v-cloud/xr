import requests
import re
from datetime import datetime

def run():
    url = "https://t.me/s/kg33d"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        links = re.findall(r'(?:vless|vmess|trojan|ss)://[^\s<"\'\s]+', response.text)
        
        clean_links = []
        for l in links:
            c = l.replace('&amp;', '&').split('<')[0].split('"')[0].strip()
            if c not in clean_links: clean_links.append(c)
        
        now = datetime.now().strftime("%Y-%m-%d | %I:%M %p")
        cards = ""
        for i, link in enumerate(clean_links):
            proto = link.split('://')[0].upper()
            cards += f'''
            <div class="card">
                <div class="card-header">
                    <span class="badge">{proto}</span>
                    <button class="btn-copy" onclick="copy('{link}')">نسخ 📋</button>
                </div>
                <div class="link-box">{link}</div>
                <button class="btn-qr" onclick="qr('q{i}','{link}')">إظهار الباركود 🔳</button>
                <div id="q{i}" class="qr-area"></div>
            </div>'''

        html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>V2Ray Elite Hub</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --p: #00f2fe; --bg: #0f172a; --c: #1e293b; }}
        body {{ background: var(--bg); color: white; font-family: 'Tajawal', sans-serif; padding: 20px; display: flex; flex-direction: column; align-items: center; margin: 0; }}
        .header {{ text-align: center; margin-bottom: 30px; margin-top: 20px; }}
        h1 {{ color: var(--p); margin: 0; font-size: 26px; text-shadow: 0 0 10px rgba(0,242,254,0.3); }}
        .status-bar {{ font-size: 11px; color: #94a3b8; background: rgba(255,255,255,0.05); padding: 5px 15px; border-radius: 50px; margin-top: 10px; border: 1px solid #334155; }}
        .info-box {{ background: var(--c); border-radius: 15px; padding: 15px; width: 100%; max-width: 450px; margin-bottom: 25px; border-right: 5px solid var(--p); box-shadow: 0 4px 15px rgba(0,0,0,0.2); }}
        .card {{ background: var(--c); border-radius: 15px; padding: 15px; margin-bottom: 20px; width: 100%; max-width: 450px; border: 1px solid #334155; transition: 0.3s; }}
        .card:hover {{ border-color: var(--p); transform: translateY(-3px); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
        .badge {{ background: linear-gradient(135deg, var(--p), #4facfe); color: #0f172a; padding: 3px 12px; border-radius: 8px; font-weight: bold; font-size: 12px; }}
        .btn-copy {{ background: #f1f5f9; border: none; padding: 6px 15px; border-radius: 8px; cursor: pointer; font-family: 'Tajawal'; font-weight: bold; font-size: 12px; }}
        .link-box {{ background: rgba(0,0,0,0.2); padding: 10px; border-radius: 10px; font-size: 10px; color: #94a3b8; word-break: break-all; direction: ltr; margin-bottom: 12px; border: 1px inset #1e293b; }}
        .btn-qr {{ width: 100%; background: #38bdf8; border: none; color: white; padding: 10px; border-radius: 10px; font-weight: bold; cursor: pointer; transition: 0.2s; }}
        .btn-qr:hover {{ background: #0ea5e9; }}
        .qr-area {{ display: none; background: white; padding: 15px; margin-top: 15px; border-radius: 12px; text-align: center; }}
        .qr-area img {{ margin: 0 auto; }}
        footer {{ margin: 40px 0; color: #4b5563; font-size: 11px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>V2Ray Elite Hub 🚀</h1>
        <div class="status-bar">تحديث: {now} | السيرفرات: {len(clean_links)}</div>
    </div>

    <div class="info-box">
        <h4 style="margin:0 0 10px 0; color:var(--p);">📖 دليل الاستخدام السريع:</h4>
        <p style="font-size: 13px; margin: 5px 0;">• <b>للنسخ:</b> اضغط "نسخ" ثم Import في تطبيق VPN.</p>
        <p style="font-size: 13px; margin: 5px 0;">• <b>للباركود:</b> اضغط الزر الأزرق للمسح بالكاميرا.</p>
    </div>

    <div style="width:100%; max-width:450px;">{cards if clean_links else '<div class="card" style="text-align:center">جاري سحب السيرفرات...</div>'}</div>

    <footer>صُنع بواسطة المساعد الذكي جيميني | 2026</footer>

    <script>
        function copy(t) {{ navigator.clipboard.writeText(t).then(() => alert("تم النسخ بنجاح ✅")); }}
        function qr(id, l) {{
            var el = document.getElementById(id);
            if(!el.innerHTML) new QRCode(el, {{text:l, width:180, height:180}});
            el.style.display = (el.style.display == 'block') ? 'none' : 'block';
        }}
    </script>
</body>
</html>'''
        with open("index.html", "w", encoding="utf-8") as f: f.write(html)
    except Exception as e: print(f"Error: {e}")

if __name__ == "__main__": run()
