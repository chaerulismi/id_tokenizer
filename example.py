import pickle

from pprint import pprint

text = """Dua warga Perum Banjararum, Singosari, Kabupaten Malang diamankan Tim Densus 88 Anti Teror. Mereka adalah pasangan suami istri. Mereka adalah Syamsul Arif alias Abu Umar Ph.D (37) dan istrinya Wahyu Mega Wijayanti (40), keduanya tinggal di Perum Banjararum Blok BB, Singosari, Kabupaten Malang. Diketahui, mereka mengontrak di rumah tersebut beberapa bulan ini. Wahyu juga tercatat sebagai warga Jalan Ir. Rais, Klojen, Kota Malang. "Benar ada kegiatan (penggerebekkan TKP Banjararum, Singosari) dua orang terduga diamankan dan kini berada di Brimob. Tengah dilakukan pengembangan," kata Barung saat dihubungi detikcom, Selasa (15/5/2018). Namun warga tak banyak tahu tentang pasutri tersebut. "Kami tak begitu mengenal, mereka kontrak di rumah itu, sekitar dua bulan ini," ujar Fatmawati (64), warga yang tinggal di depan kontrakan Syamsul dan Wahyu ditemui wartawan di lokasi. """

tokenizer_path = 'id_tokenizer'
with open(tokenizer_path) as f:
    tokenizer = pickle.load(f)

pprint(tokenizer.tokenize(text))