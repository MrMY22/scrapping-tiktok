from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


video_urls = [
    "https://www.tiktok.com/@officialmnctv/video/7391824777964473616",
    "https://www.tiktok.com/@andilempong/video/7390358532555656453",
    "https://www.tiktok.com/@kahfeveryday/video/7389231713181830406",
    "https://www.tiktok.com/@chaerunnisasaputri/video/7391271581835709701",
    "https://www.tiktok.com/@l.elisabeths/video/7390424289637502214",
    "https://www.tiktok.com/@mang_ea2/video/7392074189798198534",
    "https://www.tiktok.com/@mastercorbuzier/video/7389878209623657733",
    "https://www.tiktok.com/@siskavizar/video/7390165920238308613",
    "https://www.tiktok.com/@div_frey/video/7389472207753301254",
    "https://www.tiktok.com/@dwynnawin/video/7392466762224143622",
    "https://www.tiktok.com/@rofie_ash/video/7392260189992258821",
    "https://www.tiktok.com/@attahalilintar/video/7372051143985302790",
    "https://www.tiktok.com/@mastercorbuzier/video/7380717086177283333",
    "https://www.tiktok.com/@glencachysaraofficial/video/7391766200222534918",
    "https://www.tiktok.com/@rctiplusofficial/video/7390042996206570758",
    "https://www.tiktok.com/@vitosinagaprank/video/7389620922514263301",
    "https://www.tiktok.com/@tya_ariestya/video/7392861622596898054",
    "https://www.tiktok.com/@ndhiraa07/video/7389234139972521222"
    # Tambahkan URL video lainnya di sini
]

data = []

# Fungsi untuk mengambil data dari satu video TikTok
def get_video_data(url):
    driver.get(url)
    time.sleep(8)  # Tunggu beberapa detik untuk memastikan halaman dimuat dengan benar

    # Mengambil nama Author
    try:
        author = driver.find_element(By.XPATH, '//span[@data-e2e="browse-username"]').text
    except:
        author = "N/A"
    
    # Mengambil Deskripsi
    try:
        desc = driver.find_element(By.XPATH, '//h1[@data-e2e="browse-video-desc"]').text
    except:
        desc = "N/A"
    
    # Mengambil jumlah likes
    try:
        likes = driver.find_element(By.XPATH, '//strong[@data-e2e="like-count"]').text
    except:
        likes = "N/A"

    # Mengambil jumlah comments
    try:
        comments = driver.find_element(By.XPATH, '//strong[@data-e2e="comment-count"]').text
    except:
        comments = "N/A"

    # Mengambil jumlah Save
    try:
        save = driver.find_element(By.XPATH, '//strong[@data-e2e="undefined-count"]').text
    except:
        save = "N/A"
    
    # Mengambil jumlah Share
    try:
        share = driver.find_element(By.XPATH, '//strong[@data-e2e="share-count"]').text
    except:
        share = "N/A"

    data.append({
        "url": url,
        "author": author,
        "desc": desc,
        "likes": likes,
        "comments": comments,
        "save": save,
        "share": share
    })
    
    return {
        "url": url,
        "author": author,
        "desc": desc,
        "likes": likes,
        "comments": comments,
        "save": save,
        "share": share
    }

# Mengambil data dari semua video
video_data_list = []

for url in video_urls:
    video_data = get_video_data(url)
    video_data_list.append(video_data)

# Tutup browser
driver.quit()

# Menampilkan data yang diambil
for video_data in video_data_list:
    print(f"URL: {video_data['url']}")
    print(f"Author: {video_data['author']}, Desc: {video_data['desc']}, Likes: {video_data['likes']}, Comments: {video_data['comments']}, Save: {video_data['save']}, Share: {video_data['share']}")
    print("-" * 50)
    
# Membuat Dataframe dan menyimpa ke CSV
df = pd.DataFrame(data)
df.to_csv("tiktok_data_noviral9.csv", index=False)

print("Data telah disimpan ke tiktok_data_noviral9.csv")
