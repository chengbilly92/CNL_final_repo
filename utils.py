from PIL import Image
import streamlit as st
import os
import random
import st_pages
from st_pages import Page
from googletrans import Translator
import base64

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

ChangeLanguage = {"unknown" : "Change Language", "Taiwan" : "改變語言", "China" : "上载图像", "France" : "Uploader l'image", "Italy" : "Carica immagine", "South Korea" : "이메일", "Spain" : "Cargar imagen", "Japan" : "写真をアップロード", "Russia" : "Загрузить фото"}
Home = {"unknown" : "Home", "Taiwan" : "首頁", "China" : "首页", "France" : "Accueil", "Italy" : "Casa", "South Korea" : "홀", "Spain" : "Casa", "Japan" : "ホーム", "Russia" : "Главная"}
Chat = {"unknown" : "Chat", "Taiwan" : "聊天室", "China" : "聊天室", "France" : "Chat", "Italy" : "Chat", "South Korea" : "Chat", "Spain" : "Chat", "Japan" : "チャット", "Russia" : "Чат"}
SignUp = {"unknown" : "Sign up", "Taiwan" : "註冊", "China" : "注册", "France" : "s'inscrire", "Italy" : "Registrati", "South Korea" : "가입", "Spain" : "Registrarse", "Japan" : "サインアップ", "Russia" : "Регистрация"}
LogIn = {"unknown" : "Log in", "Taiwan" : "登入", "China" : "登录", "France" : "Se connecter", "Italy" : "Accedi", "South Korea" : "로그인", "Spain" : "Iniciar sesión", "Japan" : "ログイン", "Russia" : "Вход"}
LogOut = {"unknown" : "Log out", "Taiwan" : "登出", "China" : "注销", "France" : "Deconnexion", "Italy" : "Disconnessione", "South Korea" : "로그인", "Spain" : "Desconectar", "Japan" : "ログアウト", "Russia" : "Выход"}
ChangePassword = {"unknown" : "Change Password", "Taiwan" : "變更密碼", "China" : "更改密码", "France" : "changer le mot de passe", "Italy" : "Cambia la password", "South Korea" : "접기", "Spain" : "Cambia la password", "Japan" : "パスワードを変更", "Russia" : "Сменить пароль"}
Upload = {"unknown" : "Upload Picture", "Taiwan" : "上傳圖片", "China" : "上载图像", "France" : "Uploader l'image", "Italy" : "Carica immagine", "South Korea" : "이메일", "Spain" : "Cargar imagen", "Japan" : "写真をアップロード", "Russia" : "Загрузить фото"}

import base64
@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    opacity: 0.8;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
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
            Page('pages/changeLanguage.py', ChangeLanguage[st.session_state.country])
        ])
        st_pages.hide_pages(["Another page"])
    else:
        st_pages.show_pages([
            Page('index.py', Home[st.session_state.country]),
            Page('pages/register.py', SignUp[st.session_state.country]),
            Page('pages/login.py', LogIn[st.session_state.country]),
            Page('pages/changeLanguage.py', ChangeLanguage[st.session_state.country])
        ])
        st_pages.hide_pages(["Another page"])
    newPath = "./image/{}".format(st.session_state["country"])
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    filePath = "./image/{}".format(st.session_state['country'])
    files = os.listdir(filePath)
    if len(files) != 0:
        image_file = random.choice(files)
        img = load_image(filePath+"/"+image_file)
        set_background(img)
