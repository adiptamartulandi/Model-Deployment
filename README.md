# 🎈 🎉 Model Deployment 🎊 🎈 📚 

- Pada Repository ini, terdiri dari code dan dataset untuk melakukan Model Deployment di Python Anywhere dan Tes di Postman.
- Deployment kali ini menggunakan web framework Flask.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖  

# Contents
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖  

- Code dan Dataset
- Membuat model dy sublime text
- Membuat Pickle file di anaconda prompt 
- Deployment Model di PythonAnywhere
- Testing di Postman
- Interpretasi

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

# Code dan Dataset
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

- Data terdiri dari training dan testing untuk membuat model dan input_data.txt .
- Model yang paling optimal yang saya gunakan adalah random forest
- Code terdiri dari model.py, request.py, dan server.py

# Membuat model di sublime text
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

- Langkah pertama adalah membuat model python menggunakan text editor, pada tutorial kali ini saya menggunakan Sublime Text.
- Untuk detail codenya bisa dilihat pada file model.py

# Membuat pickle file
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

- Lalu setelah itu model.py bisa dijalankan di anaconda prompt dengan cara berikut ini:
  1. g: --> karena file model.py ada di drive G
  2. cd G:\Bootcamp\Materi\21. Deployment\credit-scoring\code
  3. lalu ketik python model.py
  4. file .pkl akan terbentuk di folder yang sama
  
# Deployment Model di PythonAnywhere
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

- Langkah selanjutnya membuat server di pythonanywhere.
- Jika belum punya akun maka sign up terlebih dahulu.
- Di tab web, klik add new web app.
- Di bagian console, klik yang bash lalu install beberapa packages yang akan digunakan. Contohnya adalah pip install --user flask_cors numpy pandas
- Lalu klik di bagian files dan klik mysite dan upload file .pkl.
- Setelah itu edit file flask_app.py dan ganti sesuai dengan yang ada di file server.py.
Lalu kembali ke bagian tab web dan reload.
- Lalu endpoints API kita sudah ada yaitu username.pythonanywhere.com/api

# Testing Model di Postman
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

- Buka software postman.
- Pada kiri pojok atas klik New untuk membuat request baru dan pilih POST.
- Di bagian header, pada bagian key pilih Content-type dan pada bagian value pilih application/json.
- Pada bagian request url masukan url endpoints API kita yaitu pada case ini adalah adiptamartulandi.pythonanywhere.com/api
- Lalu untuk memasukan data pilih tab Body, pilih raw dan pilih jenis datanya adalah JSON.
- Masukan data sesuai yang ada di input_data.txt di folder data.
- Lalu klik Send!

# Interpretasi Hasil
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

- Ketika hasil menunjukan 'Tidak Lolos Scoring' Maka orang tersebut memiliki kecendurungan untuk tidak bisa membayar kredit jadi tidak diberi kredit oleh kreditur.
- Ketika hasil menunjukan 'Lolos Credit Scoring' Maka orang tersebut mampu membayar credit sehingga bisa diberi kredit oleh kreditur.
