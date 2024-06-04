import streamlit as st
import st_pages
from st_pages import Page

def country_to_language(country):
    country_to_lang = {"Taiwan": "zh-tw",
                       "China": "zh-cn",
                       "France": "fr",
                       "Italy": "it",
                       "South Korea": "ko",
                       "Spain": "es",
                       "Japan": "ja",
                       "Russia": "ru"}
    lang = country_to_lang.get(country, "en")
    return lang

'''usage
f = open("text.txt", "r")
before = f.read()
print(translate_string_with_country(before, "China"))
'''

support_country = ["Taiwan", "South Korea", "Spain", "Russia", "Japan", "Italy", "France", "China"]

IPfrom = {'unknown': 'connecting from ', 'Taiwan': '連線位址: ', 'China': '链接来自: ', 'France': 'Connexion de ', 'Italy': 'Connessione da: ', 'South Korea': '연결:', 'Spain': 'Conectando de ', 'Japan': '接続: ', 'Russia': 'Подключение: '}
Password = {'unknown': 'password', 'Taiwan' : '密碼', 'China' : '密码', 'France' : 'Mot de passe', 'Italy' : 'Password', 'South Korea' : '비밀', 'Spain' : 'Contrasenya', 'Japan' : 'パスワード', 'Russia' : 'Пароль'}
Username = {'unknown': 'username', 'Taiwan' : '使用者名稱', 'China' : '用户名', 'France' : 'Nom d\'utilisateur', 'Italy' : 'Nome utente', 'South Korea' : '사용자 이름', 'Spain' : 'Usuario', 'Japan' : 'ユーザー名', 'Russia' : 'Имя пользователя'}
Hello = {'unknown': 'Hello', 'Taiwan': '你好', 'China': '你好', 'France': 'Bonjour', 'Italy': 'Ciao', 'South Korea': '보안', 'Spain': 'Hola', 'Japan': 'こんにちは', 'Russia': 'Привет'}
ChangeLanguage = {"unknown" : "Change Language", "Taiwan" : "改變語言", "China" : "更改语言设置", "France" : "Changer la langue", "Italy" : "Cambia lingua", "South Korea" : "예로", "Spain" : "Cambia idioma", "Japan" : "言語を変更", "Russia" : "Сменить язык"}
Home = {"unknown" : "Home", "Taiwan" : "首頁", "China" : "首页", "France" : "Accueil", "Italy" : "Casa", "South Korea" : "홀", "Spain" : "Casa", "Japan" : "ホーム", "Russia" : "Главная"}
Chat = {"unknown" : "Chat", "Taiwan" : "聊天室", "China" : "聊天室", "France" : "Chat", "Italy" : "Chat", "South Korea" : "Chat", "Spain" : "Chat", "Japan" : "チャット", "Russia" : "Чат"}
SignUp = {"unknown" : "Sign up", "Taiwan" : "註冊", "China" : "注册", "France" : "s'inscrire", "Italy" : "Registrati", "South Korea" : "가입", "Spain" : "Registrarse", "Japan" : "サインアップ", "Russia" : "Регистрация"}
LogIn = {"unknown" : "Log in", "Taiwan" : "登入", "China" : "登录", "France" : "Se connecter", "Italy" : "Accedi", "South Korea" : "로그인", "Spain" : "Iniciar sesión", "Japan" : "ログイン", "Russia" : "Вход"}
LogOut = {"unknown" : "Log out", "Taiwan" : "登出", "China" : "注销", "France" : "Deconnexion", "Italy" : "Disconnessione", "South Korea" : "로그인", "Spain" : "Desconectar", "Japan" : "ログアウト", "Russia" : "Выход"}
ChangePassword = {"unknown" : "Change Password", "Taiwan" : "變更密碼", "China" : "更改密码", "France" : "changer le mot de passe", "Italy" : "Cambia la password", "South Korea" : "접기", "Spain" : "Cambia la password", "Japan" : "パスワードを変更", "Russia" : "Сменить пароль"}
Upload = {"unknown" : "Upload Picture", "Taiwan" : "上傳圖片", "China" : "上载图像", "France" : "Uploader l'image", "Italy" : "Carica immagine", "South Korea" : "이메일", "Spain" : "Cargar imagen", "Japan" : "写真をアップロード", "Russia" : "Загрузить фото"}
CurrentLogin = {'unknown' : 'You\'ve now logged in as ', 'Taiwan' : '目前登入者: ', 'China' : '当前已连接用户 ', 'France' : 'Vous êtes maintenant connecté en tant que ', 'Italy' : 'Sei ora connesso come ', 'South Korea' : '접는:', 'Spain' : 'Ya se ha conectado como ', 'Japan' : '現在は ', 'Russia' : 'Вы вошли как '}
Share = {'unknown' : 'Share your country with people!', 'Taiwan' : '向世界分享你的家鄉!', 'China' : '向世界分享你的家！', 'France' : 'Partagez votre pays avec les gens!', 'Italy' : 'Condividi il tuo paese con le persone!', 'South Korea' : '바토스레 구역!', 'Spain' : 'Comparte tu pais con las personas!', 'Japan' : '世界を共有しましょう！', 'Russia' : 'Сделайте свой город с людьми!'}


def set_sidebar(country: str = None)-> None:
    if 'country' not in st.session_state:
        st.session_state['country'] = 'unknown'
    if not country:
        country = st.session_state['country']
    if 'login' in st.session_state: 
        st_pages.show_pages([
            Page('index.py', Home[country]),
            Page('pages/chat.py', Chat[country]),
            Page('pages/logout.py', LogOut[country]),
            Page('pages/changePassword.py', ChangePassword[country]),
            Page('pages/upload.py', Upload[country]),
            Page('pages/changeLanguage.py', ChangeLanguage[country])
        ])
        st_pages.hide_pages(["Another page"])
    else:
        st_pages.show_pages([
            Page('index.py', Home[country]),
            Page('pages/register.py', SignUp[country]),
            Page('pages/login.py', LogIn[country]),
            Page('pages/changeLanguage.py', ChangeLanguage[country])
        ])
        st_pages.hide_pages(["Another page"])
    
