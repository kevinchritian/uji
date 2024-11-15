import streamlit as st
import requests
import streamlit as st
from PIL import Image
import base64
import io


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Fungsi untuk mengonversi gambar ke format Base64
def convert_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()



# Fungsi untuk mengonversi gambar menjadi base64
def convert_image_to_base64(image):
    # Membuka gambar dan mengubahnya ke dalam base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str




# Memuat gambar dengan PIL
image = Image.open('images/anorganik.png')
image_base64 = convert_image_to_base64(image)

images_banner = Image.open('images/sampah.jpg')
image_base65 = convert_image_to_base64(images_banner)


images_organik = Image.open('images/organik.jpg')
image_base66 = convert_image_to_base64(images_organik)

images_AI = Image.open('images/phone.jpg')
image_base67 = convert_image_to_base64(images_AI)

images_sampah = Image.open('images/sampah1.jpg')
image_base68 = convert_image_to_base64(images_sampah)


# Menyisipkan link Bootstrap 5 ke dalam aplikasi Streamlit
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Membaca file CSS dari file terpisah
with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


# Banner

# Membaca gambar dan mengonversinya ke Base64
with open("images/logo.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()




# Menyisipkan gambar Base64 ke dalam tag <img>
st.markdown(f"""
<div class="container-fluid banner try">
    <div class="container banner-content">
            <div>
                <div class="gambar d-none d-md-block text-center">
                    <img src="data:image/jpeg;base64,{encoded_string}" alt="AI Image">
                </div>
                <div>
                    <h1 class="text-center tulisan-banner fw-bold">
                        Pemilahan Sampah Pintar<br> 
                        <span class="txt-bld">Bersama NatureAIClassify</span>
                    </h1>
                </div>
            </div>
    </div>
</div>
""", unsafe_allow_html=True)

# About
# st.markdown("<h1 style='text-align: center;'>Tentang Kami</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class="container-fluid">
        <h2 class="pt-5 mb-5" style='text-align: center;'>Tentang Kami</h2>
        <div class="container pb-5">
            <div>
                <p class="mb-4 about-txt">
                    NatureAIClassify adalah aplikasi berbasis kecerdasan buatan yang membantu masyarakat dalam 
                    mengelola sampah secara lebih tepat dan berkelanjutan. Dengan menggunakan model AI berbasis 
                    klasifikasi gambar, aplikasi ini memungkinkan pengguna untuk mengidentifikasi sampah organik 
                    dan anorganik hanya dengan mengambil foto, tanpa memerlukan pengetahuan khusus. NatureAIClassify 
                    dapat membedakan jenis sampah dan memberikan saran pengelolaan yang sesuai, seperti pengolahan 
                    sampah organik menjadi kompos atau proses daur ulang untuk sampah anorganik. Selain sebagai alat 
                    teknis, aplikasi ini juga berfungsi sebagai alat edukasi untuk meningkatkan kesadaran tentang 
                    pentingnya pemilahan sampah, membantu masyarakat menjaga kebersihan lingkungan, mengurangi polusi, 
                    dan melindungi ekosistem.
                <p>
            </div>
            <div class="text-center">
                <a href="/about" target="_self"><button class="tombol1 text-light">Baca Selengkapnya</button></a>
            </div>
        </div>
    </div>    
""", unsafe_allow_html=True)


# Project
st.markdown(f"""
    <div class="container-fluid konten">
        <h2 class="text-center project pt-5 mb-5">Project</h2>
        <div class="container pb-5">
            <div class="row">
                <div class="col-lg-6 col-md-6 mb-4 col-sm-6">
                    <div class="card shadow">
                        <img src="data:image/jpeg;base64,{image_base68}" class="card-img-top">
                        <div class="card-body">
                            <h5 class="card-title fw-bold">Sampah</h5>
                            <p class="card-text">Pengertian sampah, jenis jenis sampah, dan dampak sampah</p>
                            <button class="button-card float-end">Lihat >></button>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 col-md-6 mb-4 col-sm-6">
                    <div class="card shadow">
                        <img src="data:image/jpeg;base64,{image_base67}" class="card-img-top" alt="Deskripsi gambar AI">
                        <div class="card-body">
                            <h5 class="card-title fw-bold">Artificial Intelligence</h5>
                            <p class="card-text">Klasifikasi gambar sampah organik atau anorganik</p>
                            <button class="button-card float-end">Lihat >></button>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 mb-4">
                    <div class="card shadow">
                        <img src="data:image/jpeg;base64,{image_base66}" class="card-img-top" alt="Deskripsi gambar AI">
                        <div class="card-body">
                            <h5 class="card-title fw-bold">Sampah Organik</h5>
                            <p class="card-text">Pengertian sampah organik dan langkah mengolahnya</p>
                            <button class="button-card float-end">Lihat >></button>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6 col-md-6 mb-4 col-sm-6">
                    <div class="card shadow">
                        <img src="data:image/jpeg;base64,{image_base64}" class="card-img-top" alt="Deskripsi gambar AI">
                        <div class="card-body">
                            <h5 class="card-title fw-bold">Sampah Anorganik</h5>
                            <p class="card-text">Pengertian sampah anorganik dan langkah mengolahnya</p>
                            <button class="button-card float-end">Lihat >></button>
                        </div>
                    </div>
                </div>
            </div>
        </div> 
    </div> 
""", unsafe_allow_html=True)



# masukan dan Saran
st.markdown("""
    <div class="container-fluid ">
        <h2 class="text-center pt-5 mb-5">Saran dan Masukan</h2>
        <div class='container message pb-5'>
                    <form action="https://formsubmit.co/kevinsepoetro@gmail.com" method="POST" class="col-lg-10 offset-lg-1">
                        <input type="hidden" name="_captcha" value="false">
                        <div class="mb-3">            
                            <label class="form-label">Nama</label>
                            <input type="text" name="name" placeholder="Nama Anda" required class="form-control">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Email</label>
                            <input type="email" name="email" placeholder="Email" required class="form-control">
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Masukan</label>
                            <textarea name="message" placeholder="Masukan pesan disini" required class="form-control"></textarea>
                        </div>
                        <div class="mb-3">
                            <button class="submit-form w-100" type="submit">Kirim</button>
                        </div>
                    </form>
        </div>
    </div>
""",unsafe_allow_html=True)