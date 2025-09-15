# TUGAS 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
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


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
- ![bagan](https://drive.google.com/uc?export=view&id=1LQExL_O0giAiTYe3t-gp3JdzbagXQGlg)
- Pertama-tama, `urls.py` menerima url request dari server, jika cocok maka diteruskan ke `views.py`, dimana `models.py` akan digunakan jika perlu, lalu `views.py` akan meneruskan data ke template atau file `html` yang telah dibuat. 


## Jelaskan peran `settings.py` dalam proyek Django!
- File tersebut berisi semua konfigurasi pada proyek Django. Contohnya konfigurasi aplikasi yang ingin dipakai pada proyek, jenis database yang ingin dipakai, dan pengaturan keamanan. 

## Bagaimana cara kerja migrasi database di Django?
- Ketika melakukan migration di django, kita perlu melakukan 2 perintah, yakni: 
```
python manage.py makemigrations

python manage.py migrate

```
- Perintah pertama memberi tahu perubahan yang dilakukan pada database, seperti menambah kolom pada tabel database. Django membuat file migration untuk menyimpan perubahan ini. 
- Perintah kedua, django menjalankan perubahan yang ada di file migration yang dibuat pada saat menjalankan perintah pertama. 


## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Karena django menggunakan python, dimana sudah saya pelajari di mata kuliah DDP-1
- Karena lebih noob friendly dibanding framework lain?
- Source pembelajaran sudah banyak, dari stackoverflow maupun dokumentasi django.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
- Asdos sudah sangat membantu saya dengan cara standby jika ada pertanyaan atau ada error pada program




# TUGAS 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Agar data dapat diakses di berbagai tempat (Client <-> Server), sehingga memungkinkan data tersebut bisa dikirim dari client ke server atau sebaliknya, lalu disimpan ke dalam database. Kegunaan lainnya termasuk dapat memperlihatkan data tersebut pada platform yang client gunakan.


## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- Karena JSON lebih mudah dibaca oleh orang awam.
- JSON lebih ringan, sehingga read/write lebih cepat.
- Karena JSON bawaan JavaScript, jadi setiap pengguna yang memakai JavaScript, kemungkinan besar menggunakan JSON juga. Alasan tersebut dan 2 kelebihan JSON yang saya sebutkan itu yang menurut saya adalah alasan mengapa JSON lebih populer.


## Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
- `is_valid` berguna untuk memvalidasi apakah input form sudah sesuai dengan aturan field pada models maupun aturan django tentang isi form tersebut.
- Jika `is_valid()` tidak digunakan, maka ketika user menginput form tersebut dan masuk ke database, maka ketika database ingin menggunakan data tersebut dapat menyebabkan crash.


## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- CSRF atau "Cross-Site Request Forgery" adalah jenis serangan pada web dimana penyerang mengirim request ke server saat loading sebuah form (semisal form login) sehingga penyerang dapat mengirim request atas nama pengguna.
- csrf_token dibuat agar serangan crsf tidak terjadi, dengan cara server mengirim kode csrf kepada client, dan ketika melakukan request, client harus mengembalikkan kode tersebut ke server. 
- Ketika form tidak menggunakan csrf_token, maka penyerang dapat melakukan request kepada server tanpa verifikasi dengan form tersebut.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- untuk menunjukkan objek dalam fungsi XML, saya memakai fungsi:
```def show_xml(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")
```
- disini fungsi mengambil semua object, lalu dengan menggunakan library serializer, library tersebut mengubah semua format object menjadi xml. lalu fungsi mengembalikan response berupa page dengan semua xml.
- Untuk menunjukkan object dalam id, saya memakai fungsi: 
``` def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
```
- disini fungsi mengambil object dengan id yang sama dengan request dengan cara filter. Lalu diserialize ke xml dan mengembalikan respons page berupa xml dengan id yang sama. Jika object dengan id request tidak ada, mengembalikan response page 404.
- untuk JSON sama saja, hanya semua "xml" diubah ke json di 2 fungsi tersebut.
   

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
- Pada file urls.py, saya mengimport semua fungsi yang ada di views.py agar bisa di rout. 
- Untuk file XML, saya buat fungsi ini: 
```path('xml/', show_xml, name='show_xml') ```
- disitu untuk melihat file xml, pengguna harus memasukkan URL/xml untuk melihatnya.
- Saya buat fungsi yang sama untuk ketiga fungsi lainnya.

###  Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
- Ini saya buat di main.html, tinggal buat 2 button dengan tag button yang punya anchor (href) ke create_product.html untuk menambahkan objek dan tag button lagi yang href ke product_detail untuk lihat detail objek
- untuk menampilkan data objek, jika sudah ada objek, tinggal for-loop saja semua objek produk yang ada di database dan ambil semua field objeknya.

###  Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
- Pertama-tama saya buat dulu forms.py yang berisi field pada model apa saja yang ingin diisi.
- Lalu buat fungsi pada views.py yang bernama create_product yang mengimport forms.py lalu diroute ke /create-product di urls.py
- halaman form saya buat pada create_product yang inti isinya adalah form dari forms.py, disitu juga ada csrf_token untuk mencegah peretasan. Lalu ada input submit yang akan mengirim data form ke database lewat views.py dan redirect ke main.html.

### Membuat halaman yang menampilkan detail dari setiap data objek model.
- Pertama-tama dibuat dulu fungsi yang bernama show_product detail. Fungsi ini bisa mengambil objek dan routing ke product_detail.html di views.py. Lalu saya atur juga routing fungsi tersebut di urls.py. 
- Lalu pada product_detail.html, saya tambahakan header untuk semua field yang ada di objek tersebut. Untuk thumbnail, jika tidak ada, maka hanya menampilkan alt text saja.
- Ditambahkan juga button untuk kembali ke halaman utama dengan href main.html

### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
- Asdos siap membantu walaupun pertanyaannya terkesan basic atau tidak terlalu penting.

### Screenshot 4 URL di Postman
- ![showxml](https://drive.google.com/uc?export=view&id=1LQExL_O0giAiTYe3t-gp3JdzbagXQGlg)
- ![showjson](https://drive.google.com/uc?export=view&id=1LQExL_O0giAiTYe3t-gp3JdzbagXQGlg)
- ![showxmlById](https://drive.google.com/uc?export=view&id=1LQExL_O0giAiTYe3t-gp3JdzbagXQGlg)
- ![showjsonById](https://drive.google.com/uc?export=view&id=1LQExL_O0giAiTYe3t-gp3JdzbagXQGlg)