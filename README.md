- Web tugas bisa diakses melalui: https://ghozam-muliawan-sepakbolashop.pbp.cs.ui.ac.id/

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
- XML:  
![showxml](https://drive.google.com/uc?export=view&id=1nO0jPqjrvKsF1QFex9YztDKFGFmwAFJg)

- JSON:  
![showjson](https://drive.google.com/uc?export=view&id=1ONyHHAfuBocc689jjjilooe7v2j9QuQW)

- XMLByID:  
![showxmlById](https://drive.google.com/uc?export=view&id=1tYWPmenJZaxUBsa_4jG5kdFo_ONxxbwb)

- JSONByID:  
![showjsonById](https://drive.google.com/uc?export=view&id=1j3QGGluPukBRkFE1kNi4CSUL92B9VosY)



# TUGAS 4
## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
- Django AuthencticationForm adalah fungsi bawaan django yang berfungsi untuk proses "login" yang dilakukan oleh user, lalu akan diberikan form yang memiliki field username dan password. Setelah selesai, fungsi tersebut akan mengembalikan objek "user" dari user. 
- Kelebihan dari Django AuthenticationForm adalah developer tidak perlu membuat form login baru, mudah dipakai, serta langsung terintegrasi dengan sistem django.
- Namun, fungsi ini mempunyai kekurangan sangat sederhana dalam segi UI maupun UX. Hanya memperlihatkan field username dan password yang harus diisi yang terkesan barebone.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
- Autentikasi adalah proses memverifikasi identitas suatu orang.
- Sedangkan otorisasi adalah proses menentukan hak akses terhadap sesuatu setelah identitas orang tersebut diketahui.
- Django mengimplementasikan autentikasi dengan fungsi-fungsi bawaan pada library `django.contrib.auth` yang berisi segala sesuatu tentang autentikasi, seperti login, logout, dan authenticate.
- Sedangkan untuk otorisasi, django memiliki fungsi yang melihat apakah suatu user memiliki izin untuk suatu fungsi, seperti user.has.perm(). Ada pula decorators seperti @login_required, yang hanya mengizinkan user yang sudah tersimpan untuk mengakses suatu fungsi.

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
- Kelebihannya session dan cookies adalah user tidak perlu login berkali-kali jika semisal user berpindah dari satu web ke lainnya. Cookies lebih mudah digunakan, session lebih aman karena disimpan di server. 
- Kekurangannya cookies adalah, tidak aman, ukuran terbatas, dan data tersebut dicuri oleh penyerang, yang membuat penyerang tersebut bisa memiliki terhadap akun jika cookie tidak direset. 
- Kekurangan session adalah, jika cookies di curi oleh penyerang, penyerang bisa mengambil akses session yang sedang berlangsung. Session juga hanya bertahan sampai user logout atau tutup web, berbeda dengan cookies yang disimpan secara local.

##  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
- Cookies tidak selalu aman, karena sifat cookies yang disimpan secara lokal, jadi semisal developer menyimpan username atau password ataupun informasi penting lainnya, cookie tersebut bisa diambil melalui malware cookie stealer, XSS, dan CSRF. 
- Django menangani hal ini dengan membuat server-side session. Jadi informasi penting yang sebelumnya disimpan pada cookie, sekarang disimpan pada server dan cookie hanya menyimpan SessionID. Jadi semisal cookie yang ada di client dicuri, cookie tersebut hanya valid sampe session itu berakhir saja. 

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
###  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
- Pertama, import dulu libary-libary yang dibutuhkan, yaitu library `django.contrib.auth` yang menyimpan fungsi2 login, serta decoratornya. 
- Lalu buat fungsi register yang isinya seperti ini: 
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
- Fungsi ini akan membuat form untuk register menggunakan `UserCreationForm` yang merupakan form bawaan django untuk penambahan user. For ini memiliki field Username dan Password. Fungsi ini akan dipanggil melalui /register.html
- Sebelum fungsi bisa dipanggil lewat html tersebut, buat dulu routing pada urls.py yang mengarah ke register.html. Html tersebut singkatnya hanya berfungsi untuk menampilkan `UserCreationForm` dengan method `POST`.
- Lalu buat fungsi login yang isinya seperti ini:
```
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
- Fungsi ini dipanggil melalui /login, jadi buat routingnya terlebih dahulu. Fungsi ini membuat form login dari `AuthenticationForm`, lalu fungsi akan mengambil user dan diteruskan ke fungsi login django `login(request, user)`. Setelah itu user bisa masuk ke website.
- Lalu buat web login dengan membuat login.html. Di page ini user bisa login dengan memasukkan kredensialnya, atau tersedia button yang memanggil fungsi register. 
- Tidak lupa tambahkan decorator `@login_required(login_url='/login')` pada fungsi `show_main` dan `show_product` agar hanya user terdaftar yang bisa mengakses 2 fungsi tersebut, jika user belum terdaftar atau belum login, redirect ke page login.
- Lalu buat fungsi logout yang isinya seperti ini:
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
- Fungsi ini dipanggil melalui /logout, jadi tambahkan routing pada urls.py dulu. Fungsi digunakan jika user ingin logout dengan cara memanggil logout(request) yang menghapus data session di server, lalu redirect ke halaman login. 
- Fungsi ini bisa dipanggil lewat main.html. Jadi ketika user ingin logout, tinggal pencet button yang ada di page main. Potongan kode buttonnya seperti ini:
```
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
###  Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
- Buat akun baru, lalu tambahkan product dengan isi field-field yang tersedia, ulangi 3x.
- Lalu lakukan lagi untuk akun selanjutnya.

###  Menghubungkan model Product dengan User.
- Pertama, buat dulu field user pada models. Lalu tambahkan bagian kode pada views.py, spesifiknya pada create_product:
```        
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
```
- Pada bagian ini, field user akan diisi dengan user yang sedang terlogin pada saat ini, jadi membuat hubungan one to many antara user dengan product.

###  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
- Pada main.html, ditambahkan kode ini:
```
<h5>Logged in as: {{ logged }}</h5>
<h5>Sesi terakhir login: {{ last_login }}</h5>
<hr>
```
- Potongan kode ini akan mengambil pengguna yang sedang logged dan waktu last_login yang diambil dari context showmain pada views.py yang berisi seperti ini:
```
    context = {
        'npm' : '2406495565',
        'name' : 'Ghozam Muliawan Sholihin',
        'logged': request.user.username,
        'class': 'PBP C',
        'Aplikasi' : 'SlopShop',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
```
- Pada potongan kode tersebut, variabel logged diambil dari user yang sedang terlogin pada saat itu dan diambil usernamenya.
- Sedangkan last_login adalah variabel yang mengambil waktu last_login dari cookies, ketika variabel tersebut ada isinya, maka ambil isi tersebut. Jika tidak ada isi, maka tampilkan 'Never"


# TUGAS 5
## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
- CSS selector memiliki hierarki pengambilan seperti ini:
- 1. Kode dengan inline style `<p style="color: red;">Teks ini pasti merah</p>`
- 2. ID Selector `(#title)`
- 3. Class, pseudo-class, dan attribute `(.class, :hover, [type="text"])`
- 4. Tag/Type selector `(p, h1, div)` dan Universal selector `(*)`
- Lalu ketika ada 2 selector dengan tingkat hierarki yang sama, maka selector yang paling bawah/terakhir lah yang dipakai oleh CSS.

## Mengapa responsive design menjadi konsep yang penting da lam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
-  Karena responsive design membuat sebuah web menjadi lebih ramah untuk semua gadget, mau itu handphone, tablet, maupun desktop. Sehingga tidak hanya user desktop saja yang bisa melihat web cantik, namun semua user pun bisa, yang mengakibatkan UX dari gadget lain menjadi lebih baik.
- Contoh Web yang sudah menerapkan responsive design adalah `https://scele.cs.ui.ac.id/`, web scele kita. Karena ketika disimulate, web tersebut responsif, dimana ukuran2 objeknya berubah untuk menyesuaikan layar hp. 
![SceleDesktop](https://drive.google.com/uc?export=view&id=1Gs-ExRU0-nifgXKCmDgHNa7B9lHjIRBP)
![SceleMobile](https://drive.google.com/uc?export=view&id=1Ib9xx4P3QXzN8xXluNaSVUQOka3oX7-k)
- Contoh Web yang belum menerapkan responsive design adalah `https://www.tokopedia.com/`. Karena tidak ada perubahan ketika disimulasikan melalui hp, Tokopedia sepertinya sudah fokus pada dedicated appnya untuk platform mobile, jadi platform webnya ditinggalkan. 
![TokopediaDesktop](https://drive.google.com/uc?export=view&id=1cSBYWkpiO9ZFfmUNxqt9Bi-efdlldFbL)
![TokopediaMobile](https://drive.google.com/uc?export=view&id=1K_Teo42DjwFeEdfgG2j0OBV0qzt61ehu)

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin adalah ruang tidak berwarna diluar border yang memisahkan objek dari objek lain.
- Border adalah adalah garis bingkai elemen yang berada diantara padding dan margin.
- Padding adalah ruang kosong diantara konten dan border.
- Implementasinya di CSS:
```
* {
    margin : 67px; <- Margin
    padding : 69px: <- Padding
    border : 4x dashed black; <- Border
}
```
![MarginBorderPadding](https://pbp-fasilkom-ui.github.io/ganjil-2026/assets/images/t4-1-833b8ee0d0dd53959be9b66d452cd1d6.png)
- Sumber: Tutorial PBP Fasilkom UI

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox adalah konsep layout 1 dimensi, dimana objek hanya bisa ditambahkan keatas maupun kesamping, namun tidak 2-2nya. 
- Kalau grid, dia adalah konsep layout 2 dimensi, dimana objek bisa ditambahkan keatas maupun kesamping. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
### Implementasikan fungsi untuk menghapus dan mengedit product.
- untuk mengimplementasikan fungsi edit, pada views.py, tambahkan kode seperti ini:
```
@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)
```
- Fungsi ini mengambil produk yang sudah ada, lalu membuat dan mengisi form dengan produk yang diambil tadi. Sehingga pengguna bisa mengedit produk yang sudah ada di database. 
- Tambahkan edit_product.html yang menampung form tersebut. 
- Lalu untuk fungsi delete, tambahkan kode seperti ini: 
```
@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
- Fungsi tersebut mengambil produk berdasarkan id, lalu mendeletenya dengan `.delete()`.
- Jangan lupa tambahkan routing pada urls.py
```
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
```

### Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
#### Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
- Hampir sama seperti tutorial, tapi saya tambah-tambahkan shadow effect (shadow-lg) pada box, lalu hover effects pada button-buttonnya. 

#### Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
##### Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
- Pada main.html, tambahkan seksi
```
{% if not news_list %}

        ...
        <div class="w-32 h-32 mx-auto mb-4">
          <img src="{% static 'image/no-product.png' %}" alt="No product available" class="w-full h-full object-contain">
        </div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">gak ada produk/h3>
        <p class="text-gray-500 mb-6">produk masih kosong.</p>
        ...

{% else %}
        ...
{% endif %}
```
- Di bagian kode itu, jika tidak ada produk, maka page akan menampilkan image dan pesan kalau tidak ada produk yang terdaftar.
![NoProduct](https://drive.google.com/uc?export=view&id=1XPmz6LAbrO3WuZ7NF9RqfJAcdFveI1qm)
#### Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
- Punya saya tidak jauh berbeda dengan yang di tutorial, namun saya modif sedikit banner-bannernya yang akan menunjukkan harga, banner miring untuk category, dan hover effects agar lebih menarik. 

#### Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
- Tambahkan ini pada file html:
```
          <a href="{% url 'main:edit_product' product.id %}" class="text-gray-700 text-sm">Edit</a>
          <a href="{% url 'main:delete_product' product.id %}" class="text-red-700 text-sm">Delete</a>
```
- Bagian kode ini akan menampilkan text yang akan memangil fungsi edit dan delete pada views.py yang sudah ter-route dengan benar.


#### Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
- Tambahkan 2 bagian kode yang berbeda untuk mobile dan desktop.
- Jadi untuk bagian desktop tambahkan bagian kode ini:
```
        <div class="hidden md:flex items-center space-x-8">
``` 
- jadi ketika layar "md" atau medium dan lebih besar, maka akan flex atau menunjukkan menunya, dan hidden secara default untuk lainnya
- Lalu untuk bagian mobile tambahkan kode ini:
```
        <div class="md:hidden flex items-center">
```
- Yang dimana menu hamburger akan hide kalau screen adalah md atau lebih besar, dan show untuk layar yang lebih kecil daripada itu.


