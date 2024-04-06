---
layout: page
title: Contact Page
permalink: /contact
description: menghubungi kami
comments: false
---

<!-- Teks Profesional -->
<div style="margin-top: 20px; font-family: Arial, sans-serif;">
  <h2>Hubungi Kami</h2>
  <p>Jika Anda ingin menghubungi kami, silakan isi formulir di bawah ini.</p>
  
  <h3>Email:</h3>
  <p>info@budidayatani.com</p>
  <p>Kami berusaha untuk menjawab semua pertanyaan dalam beberapa hari.</p>

  <h2>Kesempatan Kerja</h2>
  <p>Kami senang untuk membahas peluang kerja, freelance, atau kontrak. Email kami dengan deskripsi proyek Anda, dan kita bisa membicarakannya lebih lanjut.</p>
  <p>Kami sangat menghargai masukan atau permintaan fitur terkait proyek-proyek kami. Juga, jangan ragu untuk menghubungi kami untuk melaporkan bug atau permintaan dukungan.</p>

  <h2>Posting Blog atau Video</h2>
  <p>Jika Anda ingin berbicara tentang salah satu posting blog atau video kami, silakan kirimkan email. Jika Anda membutuhkan bantuan dengan sesuatu, email kami, dan kami akan mencoba membantu.</p>
</div>

<!-- Formulir Kontak -->
<div id="formkeep-embed" data-formkeep-url="https://formkeep.com/p/08dca62b3c8203887cd84131491b5c20?embedded=1"></div>

<!-- Sertakan pustaka FormKeep dan Pym.js -->
<script type="text/javascript" src="https://pym.nprapps.org/pym.v1.min.js"></script>
<script type="text/javascript" src="https://formkeep-production-herokuapp-com.global.ssl.fastly.net/formkeep-embed.js"></script>

<!-- JavaScript untuk menangani peristiwa pengiriman formulir -->
<script>
  const formkeepEmbed = document.querySelector('#formkeep-embed');

  formkeepEmbed.addEventListener('formkeep-embed:submitting', _event => {
    console.log('Mengirim formulir...');
    // Anda dapat menambahkan animasi loading atau pesan di sini
  });

  formkeepEmbed.addEventListener('formkeep-embed:submitted', _event => {
    console.log('Formulir terkirim...');
    // Anda dapat menambahkan pesan sukses atau mengarahkan pengguna ke halaman terima kasih di sini
  });
</script>
