function detailBuku() {
    $.ajax({
      method: 'GET',
      url: "http://localhost:3000/dataBuku",
      beforeSend: function (req) {
        req.setRequestHeader('Content-Type', 'application/json')
      },
      success: function (res) {
        JSON.parse(res).forEach(function (data) {
          // console.log(data)
          document.getElementById('table-buku').insertAdjacentHTML("afterend", `
          <tr>
              <td class="text-center"  scope="row">${data.no_buku}</th>
              <td class="text-center" >${data.judul}</td>
              <td class="text-center" >${data.tahun_terbit}</td>
              <td class="text-center" >${data.pengarang}</td>
              <td class="text-center"><img id="gambarBuku" src='${data.gambar}'></td>
          </tr>
          `)
        })
        },
      error: function (err) {
        console.log(err)
      }
    })
}

function tambahBuku(){
    $.ajax({
        method: 'POST',
        url: "http://localhost:3000/tambahBuku",
        beforeSend: function (req) {
            req.setRequestHeader('Content-Type', 'application/json')
        },
        data: JSON.stringify({
            "judul": document.getElementById('judul').value,
            "tahun_terbit": document.getElementById('tahun_terbit').value,
            "pengarang": document.getElementById('pengarang').value,
            "gambar": document.getElementById('gambar').value
            }),
            success: function (res) {
            alert(res)
            window.location = "/html/detail.html"
            },
            error: function (err) {
            alert("")
            console.log(err)
            }
        })
}

function peminjam(){
    $.ajax({
        method: 'POST',
        url: "http://localhost:3000/dataPeminjam",
        beforeSend: function (req) {
            req.setRequestHeader('Content-Type', 'application/json')
        },
        data: JSON.stringify({
            "judul": document.getElementById('judul').value,
            "nama_peminjam": document.getElementById('nama_peminjam').value,
            "tanggal_peminjaman": document.getElementById('tanggal_peminjaman').value,
            "tanggal_pengembalian": document.getElementById('tanggal_pengembalian').value
            }),
            success: function (res) {
            alert(res)
            window.location = "/html/detail.html"
            },
            error: function (err) {
            alert("")
            console.log(err)
            }
        })
}
