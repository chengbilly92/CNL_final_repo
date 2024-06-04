import streamlit as st
import st_pages
from st_pages import Page
from googletrans import Translator
def translate_string_with_country(string, country):
    country_to_lang = {"Taiwan": "zh-tw",
                       "China": "zh-cn",
                       "France": "fr",
                       "Italy": "it",
                       "South Korea": "ko",
                       "Spain": "es",
                       "Japan": "ja",
                       "Russia": "ru"}
    translator = Translator()
    lang = country_to_lang.get(country, "en")
    after = translator.translate(string, dest = lang).text
    return after

'''usage
f = open("text.txt", "r")
before = f.read()
print(translate_string_with_country(before, "China"))
'''

Home = {"unknown" : "Home", "Taiwan" : "首頁", "China" : "首页", "France" : "Accueil", "Italy" : "Casa", "South Korea" : "홀", "Spain" : "Casa", "Japan" : "ホーム", "Russia" : "Главная"}
Chat = {"unknown" : "Chat", "Taiwan" : "聊天室", "China" : "聊天室", "France" : "Chat", "Italy" : "Chat", "South Korea" : "Chat", "Spain" : "Chat", "Japan" : "チャット", "Russia" : "Чат"}
SignUp = {"unknown" : "Sign up", "Taiwan" : "註冊", "China" : "注册", "France" : "s'inscrire", "Italy" : "Registrati", "South Korea" : "가입", "Spain" : "Registrarse", "Japan" : "サインアップ", "Russia" : "Регистрация"}
LogIn = {"unknown" : "Log in", "Taiwan" : "登入", "China" : "登录", "France" : "Se connecter", "Italy" : "Accedi", "South Korea" : "로그인", "Spain" : "Iniciar sesión", "Japan" : "ログイン", "Russia" : "Вход"}
LogOut = {"unknown" : "Log out", "Taiwan" : "登出", "China" : "注销", "France" : "Deconnexion", "Italy" : "Disconnessione", "South Korea" : "로그인", "Spain" : "Desconectar", "Japan" : "ログアウト", "Russia" : "Выход"}
ChangePassword = {"unknown" : "Change Password", "Taiwan" : "變更密碼", "China" : "更改密码", "France" : "changer le mot de passe", "Italy" : "Cambia la password", "South Korea" : "접기", "Spain" : "Cambia la password", "Japan" : "パスワードを変更", "Russia" : "Сменить пароль"}
Upload = {"unknown" : "Upload Picture", "Taiwan" : "上傳圖片", "China" : "上载图像", "France" : "Uploader l'image", "Italy" : "Carica immagine", "South Korea" : "이메일", "Spain" : "Cargar imagen", "Japan" : "写真をアップロード", "Russia" : "Загрузить фото"}


def set_sidebar()-> None:
    if 'country' not in st.session_state:
        st.session_state['country'] = 'unknown'
    if 'login' in st.session_state: 
        st_pages.show_pages([
            Page('index.py', Home[st.session_state.country]),
            Page('pages/chat.py', Chat[st.session_state.country]),
            Page('pages/logout.py', LogOut[st.session_state.country]),
            Page('pages/changePassword.py', ChangePassword[st.session_state.country]),
            Page('pages/upload.py', Upload[st.session_state.country]),
        ])
        st_pages.hide_pages(["Another page"])
    else:
        st_pages.show_pages([
            Page('index.py', Home[st.session_state.country]),
            Page('pages/register.py', SignUp[st.session_state.country]),
            Page('pages/login.py', LogIn[st.session_state.country]),
        ])
        st_pages.hide_pages(["Another page"])
