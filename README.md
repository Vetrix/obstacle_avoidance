# seleksi_dagozilla_13517138_dzannun
Berikut adalah takehome test Seleksi Dagozilla

## Problem 1, Obstacle avoidance

   Hal yang dapat dilakukan pertama sebelum menentukan gerakan, adalah menentukan lokasi robot dalam lapangan. Lokalisasi robot dapat membantu bagaimana robot dapat bergerak, dan menentukan strategi untuk melewati rintangan. Lokasi yang perlu ditentukan adalah lokasi robot itu sendiri, lokasi bola, lokasi garis lapangan (termasuk gawang dan pojok lapangan), dan rintangan. Dengan menggunakan menggunakan hubungan jarak dari ujung lapangan dan sudutnya terhadap pojok lapangan, dapat ditentukan posisi yang diinginkan (dengan asumsi seluruh lapangan terlihat dalam vision). Contoh cara yang dapat digunakan adalah:(
    
    (x3 − x2)^2 + (y3 − y2)^2 = a^2 + b^2 − 2abcos(θ2) 
    (x2 − x1)^2 + (y2 − y1)^2 = b^2 + c^2 − 2bccos(θ3)
    
   Dengan a, b, c adalah jarak robot ke pojok lapangan, dan (xi , yi) adalah posisi pojok lapangan, sedangan θi adalah besar sudut dari posisi robot terhadapat dua pojok lapangan.

   Lalu gerakan yang dilakukan adalah gerakan dari kombinasi 3 roda omniwheel bersudut (β 1 , β 2 , β 3 ) = (π/3, π, −π/3). Setiap gerakan ke suatu posisi dengan arah tertentu dapat dilakukan dengan efektif dengan menggunakan gerak 3 roda dengan arah dan distribusi motor yang berbeda pada tiap gerakannya. Sedangkan untuk gerakan memutar, dapat digunakan ketiga roda bergerak bersamaan, dengan distribusi sama, ke arah yang sama.
   Dari hasil gambar tangkapan sistem vision, setiap objek yang didapat, disegmentasi menjadi empat warna, hijau untuk lapangan, putih untuk garis lapangan, jingga untuk bola, dan abu-abu untuk lainnya. Lalu dari gambar yang didapat dari omnidirectional camera, diubah menjadi datar. 

   Dari gambar yang kita miliki tersebut kita bisa menggeneralisir bahwa, semua yang hijau adalah lapangan, dan seterusnya. Dari hal tersebut dapat kita ambil, bahwa objective yang kita miliki adalah mengambil bola, melewati obstacle tanpa kehilangan bola, lalu mencetak gol.
   Menurut saya, cara yang dapat digunakan harus diawali dengan analisis kasus. Untuk kasus pertama adalah saat bola sudah terlihat secara jelas dalam vision, maka robot bergerak ke arah depan yang memiliki (dribbler untuk mencengkram dan membawa bola) berada dengan hadapan yang lurus terhadap bola, sehingga bola dapat dengan mudah terambil. Jika terdapat rintangan yang menghalangi bola, maka robot harus bergerak memutari salah satu rintangan, apabila terlihat bola, kembali ke gerak sebelumnya, apabila tidak terlihat, robot harus memutari obstacle lain. Setelah mendapat bola, kita gunakan kasus seperti gambar yang kita miliki yaitu rintangan berada tepat di samping robot, di sebelah timur laut robot, dan bagian barat dari gawang. Dengan asumsi gol berada di utara robot, menurut saya, cara yang efektif untuk membuat gol adalah dengan langsung melancarkan tendangan ke daerah kosong gawang. Namun apabila memang harus dilakukan gerakan, maka lebih baik melakukan gerakan dengan bergerak membelakangi robot obstacle terdekat, dengan harapan robot tidak kehilangan bola dengan cepat, setelah itu langsung melakukan tendangan ke arah gawang.

## Problem 2, Code Comprehesnsion
## Sudoku
   Puzzle sudoku diselesaikan menggunakan algoritma backtracking, yang dapat mengulang balik apa yang dilakukan, hingga mendapat jawaban yang benar. Dari program yang sudah tersedia, program penyelesaian sudoku memiliki tahapan kerja sebagai berikut, yaitu:
    
   1. Saat dijalankan, program akan meminta 3 command line arguments yang berisi program yang akan dijalankan (sudoku.py), file eksternal sudoku yang akan diselesaikan (probX.txt), dan file eksternal untuk menyimpan hasil penyelesaian sudoku (solnX.txt), apabila tidak sesuai, program akan mengeluarkan pesan error
```
./Python sudoku.py probX.txt solnX.txt
```
   2. Program akan membuka file eksternal, dan membacanya, untuk disimpan dalam tabel dengan nama variabel board, dan mengganti setiap char '-' menjadi int 0, dan menuliskan board ke layar
   3. Program lalu mencari bagian sudoku yang belum terisi, dan mengisikannya dengan angka 1-9, dengan syarat tidak boleh ada angka yang sama, dalam satu baris, kolom, maupun kotak 3x3
   4. Apabila ada kesalahan, program akan melakukan backtracking, dan mengisi bagian kosong dengan angka lain, hingga diperoleh hasil yang tepat
   5. Program menuliskan board yang sudah selesai ke layar, lalu menyimpannya di file eksternal solnX.txt, apabila tidak ada penyelesaian, program akan mengembalikan "No solution found"
  
## Minesweeper
   Program minesweeper.cpp secara umum membuat permainan sudoku, dengan ukuran papan yang berupa array dinamik yang ukurannya berubah sesuai dengan input dari user. Meminta pula dari user, berapa banyak bom yang akan ada dalam satu papan minesweeper, lalu melakukan random generate bom pada papan minesweeper. Setelah itu masuk ke mode permainan yang dijalankan seperti halnya permainan minesweeper, dengan user bisa melakukan click on board, dengan memasukkan input berupa baris dan kolom. Kondisi menang adalah saat seluruh papan tanpa bom telah "dijelajahi", sedangkan posisi kalah terjadi saat user melakukan click terhadap bagian bom. Saat dijalankan, program akan berjalan seperti:
   1. Program mnuliskan tulisan untuk menerima input dari pengguna, yaitu ukuran papan, dan jumlah bom
   2. Program melakukan random generate bom, dan menuliskan lokasi bom ke layar
   3. Bagian papan akan diganti dengan angka, sesuai dengan ada tidaknya bom disekitarnya, lalu ditutup dengan char berupa "*"
   4. Masuk ke mode permainan, dengan user dapat melakukan click pada papan dengan memasukkan input berupa "[baris] [kolom]"
   5. Kondisi menang apabila user dapat "menjelajahi" seluruh map tanpa melakukan click pada bom, kondisi kalah terjadi apabila user melakukan click pada bom, selain itu akan kembali pada kondisi permainan.
