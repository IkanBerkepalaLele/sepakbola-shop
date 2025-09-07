
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
### Membuat Projek Django Baru
- Membuat proyek Django baru dengan cara menginstall dependencies yang tercantum pada tutorial 0 dan membuat proyek bernama sepakbola_shop dengan menjalankan perintah `django-admin startproject sepakbola_shop .`
- Membuat dan mengkonfigurasi env dengan perintah ` python -m venv env`.
- mengkonfigurasi settings.py dengan memasukkan .kredensial yang sudah diberikan oleh PBP.
- membuat .gitignore.
- Membuat repo baru di github.
- upload repo lokal ke repo github dengan git remote. 


### Membuat Aplikasi Baru Dengan Nama `Main`.
- Menjalankan perintah `python manage.py startapp main` dengan mengaktifkan virtual environemnt terlebih dulu.


### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Tambahkan `path('', include('main.urls')),` pada urlpatterns di file `urls.py` di direktori proyek.


### Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
- buat class baru yang bernama Product.
- Saya buat classnya seperti ini:

```
class Product(models.Model):
    CATEGORY_CHOICES = [('shoe', 'Shoe'), ('jersey', 'Jersey'), ('accessory', 'Accessory'), ('shorts', 'Shorts')]
    
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
```
- saya buat kategorinya hanya bisa dipilih dari pilihan yang sudah dibuat.


###  Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- Mengimport render pada `views.py`
- membuat fungsi yang merender html di `views.py` (return render(request, "main.html"))
- Untuk membuat template html yang bisa menampilkan nama aplikasi, nama, dan kelas, maka bisa langsung diedit di htmlnya, atau bisa membuat html menampilkan variabel yang telah ditulis pada `views.py`. contoh htmlnya seperti ini:
```
<h1>Nama Aplikasi: </h1>
<h1>{{ Aplikasi }}</h1>

<h5>NPM: </h5>
<p>{{ npm }}</p>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}</p>
```


###  Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
- Setelah mmengedit `views.py`, buat `urls.py` pada `main` yang berisi:
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
] 
```


###  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Setelah melakukan perubahan yang dibutuhkan, migrate program dengan menjalankan perintah:
```
python manage.py makemigrations

python manage.py migrate

```
- buat proyek baru pada PWS, lalu tambahkan deployment url ke `ALLOWED_HOST` pada `settings.py`.
- lakukan git remote dengan server pws, lalu jalankan `git push pws master`.


# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
- ![bagan](https://drive.google.com/uc?export=view&id=1LQExL_O0giAiTYe3t-gp3JdzbagXQGlg)
- Pertama-tama, `urls.py` menerima url request dari server, jika cocok maka diteruskan ke `views.py`, dimana `models.py` akan digunakan jika perlu, lalu `views.py` akan meneruskan data ke template atau file `html` yang telah dibuat. 


# Jelaskan peran `settings.py` dalam proyek Django!
- File tersebut berisi semua konfigurasi pada proyek Django. Contohnya konfigurasi aplikasi yang ingin dipakai pada proyek, jenis database yang ingin dipakai, dan pengaturan keamanan. 

# Bagaimana cara kerja migrasi database di Django?
- Ketika melakukan migration di django, kita perlu melakukan 2 perintah, yakni: 
```
python manage.py makemigrations

python manage.py migrate

```
- Perintah pertama memberi tahu perubahan yang dilakukan pada database, seperti menambah kolom pada tabel database. Django membuat file migration untuk menyimpan perubahan ini. 
- Perintah kedua, django menjalankan perubahan yang ada di file migration yang dibuat pada saat menjalankan perintah pertama. 


# Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Karena django menggunakan python, dimana sudah saya pelajari di mata kuliah DDP-1
- Karena lebih noob friendly dibanding framework lain?
- Source pembelajaran sudah banyak, dari stackoverflow maupun dokumentasi django.

# Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
- Asdos sudah sangat membantu saya dengan cara standby jika ada pertanyaan atau ada error pada program




