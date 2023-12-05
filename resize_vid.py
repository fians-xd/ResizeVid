from calendar import c
import time
import sys
import os
import datetime
from moviepy.editor import VideoFileClip, AudioFileClip

# Warna
h  = ('\x1b[0;32m') # hijau gelap
ht = ('\x1b[38;5;40m') # hijau terang
b  = ('\x1b[0;36m') # biru gelap
bt = ('\x1b[36;1m') # biru terang
m  = ('\x1b[31;1m') # merah
p  = ('\x1b[37;1m') # putih
h  = ('\x1b[30;1m') # hitam
o  = ('\x1b[33;1m') # oren
k = ('\x1b[1;33m') # kuning terang
c = ('\x1b[38;5;172m') # Coklat terang
b  = ('\x1b[0;34m') # biru tua
u  = ('\x1b[38;5;135m') # ungu
n  = ('\x1b[0;0m') # normal
mc = ('\x1b[38;5;52m') # Merah Coklat
pk = ('\x1b[38;5;207m') # pink
pn = ('\x1b[38;5;86m') # pesan

# Waktu
waktu_sekarang = datetime.datetime.now()
wkt = waktu_sekarang.strftime(f"{bt}%Y{k}-{bt}%m{k}-{bt}%d %H{k}:{bt}%M{n}")

# Logo
___logo___ = (f"""{u} ################################################################
{u} #                         {m},          ,                         {u}#
{u} # {n}"Hai bree.!            {ht}_{m}|\{ht}_       {m}/|      {n}{wkt}   {u}#
{u} #  {n}Alat ini diciptakan  {ht}/___ "\----{m}' |                         {u}#
{u} #  {n}Untuk merubah size  {ht}/=====\ \     `-.      {n}Version{k}: {bt}01{k}.{bt}00   {u}#
{u} #  {n}Pada video"       {ht}// {c}.--.{ht}  \|  |      \                     {u}#
{u} #              {n}\    {ht}/(  {b}[{m}@@{b}]{ht}   )  /       \                    {u}#
{u} #       {c},{ht}       {n}\  {ht}|  \ {c}'--'{ht}  /  /         \------.            {u}#
{u} #       {c}|\_{ht}        |   \___.-'              \----. \           {u}#
{u} #  {c}__,--'' \.{ht}     /|   {c}_____..----) ){ht}       |     \ \          {u}#
{u} # {c}"----____:{ht} \.  / | {c}('          /{ht}      |   |      \ \         {u}#
{u} #           {ht}`. \/ /\  {c}\._     _./{ht}      /    |       \ \        {u}#
{u} #             {ht}\_./  \    {c}'===={ht}        /    /         \ \       {u}#
{u} #                    {ht}\     {c}---{ht}     --'    /           \{c}.{ht}\{c}.     {u}#
{u} #                     {ht}\.              _,-;           {c}/,--.\    {u}#
{u} #      {m}凸{b}({m}•̀{b}_{m}•́{b}){m}凸        {ht}\___________/\/ /            {c}"    "    {u}#
{u} #                                   {ht}\/ /{c}_                      {u}#
{u} #                                   {ht}/`/  {c}|                     {u}#
{u} #                         {c}+"";".{ht}   / /{c}|  /                     {u}#
{u} #  {pn}_   _   ___   ___{b}       {c}\    \.{ht}/ / {c}| /   {n}__Auth{k}:            {u}#
{u} # {pn}\ ( ) / )_ _( \   \{b}       {c}`\ . | {ht}/  {c}+"           {n}Yan-xd__    {u}#
{u} #  {pn})\_/(  _| |_ | ) ({b}         {c}\  |{ht}/                            {u}#
{u} #   {pn}\_/  )_____(/___/{b}          {c}(_)                             {u}#
{u} #    {pn}____   ___    ___    ___   ____   ___     _*_ _ __   ___  {u}#
{u} #   {pn}/  _ \ ) __(  (  _(  )_ _( )___ ( ) __(    | || '_ \ / __( {u}#
{u} #   {pn})  ' / | _)   _) \   _| |_   / /_ | _) _   | || | | | (__  {u}#
{u} #   {pn}|_()_\ )___( )____) )_____( )____()___( ) (___|_| |_|\___( {u}#      
{u} #                                         {pn}|/                   {u}#
{u} ################################################################
{n}""")
              
___pesan___ = (f"{u}\nツ {o}Gari enteni wae lapet rangasi semenit, sulet udute seruput kopine karo mandengi kode meroses videomu{u} ツ {n}{ht}\n\n")              

# Teks Berjalan logo
speed_logo = 0.0009
def berjalan_teks(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed_logo)

def resize_video():
    os.system('clear')
    berjalan_teks(___logo___)
    input_file = input(f"\n{ht}Masukkan path video input Anda{k}:{n} ")
    output_filename = input(f"{ht}Masukkan nama file video hasil resize (tanpa ekstensi){k}:{n} ")
    target_width = int(input(f"\n{ht}Masukkan lebar (width) yang diinginkan{k}:{n} "))
    target_height = int(input(f"{ht}Masukkan tinggi (height) yang diinginkan{k}:{n} "))

    # Cetak pesan dulu
    for charlex in ___pesan___:
        print(charlex, end='', flush=True,)
        time.sleep(0.05)  # Mengatur jeda menjadi 0.2 detik untuk perlahan lebih lambat

    # Pastikan folder "hasil" sudah ada, jika belum, buat folder tersebut
    output_folder = "hasil"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Baca video menggunakan VideoFileClip
    video_clip = VideoFileClip(input_file)

    # Resize video tanpa crop
    resized_clip = video_clip.resize((target_width, target_height))

    # Simpan video hasil resize sementara
    temp_output_file = os.path.join(output_folder, f"{output_filename}_temp.mp4")
    resized_clip.write_videofile(temp_output_file, codec="libx264", audio_codec="aac")

    # Konversi audio dari format mp4 ke mp3
    audio_file = input_file.replace(".mp4", ".mp3")
    video_clip.audio.write_audiofile(audio_file)

    # Baca video hasil resize yang telah disimpan
    video_clip_with_audio = VideoFileClip(temp_output_file)

    # Baca file audio yang telah dikonversi menjadi mp3
    audio_clip = AudioFileClip(audio_file)

    # Gabungkan audio dengan video hasil resize
    final_clip = video_clip_with_audio.set_audio(audio_clip)

    # Simpan video hasil resize dengan audio di dalam folder "hasil"
    output_file = os.path.join(output_folder, f"{output_filename}.mp4")
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # Hapus file video hasil resize sementara dan file audio yang sudah digabungkan
    os.remove(temp_output_file)
    os.remove(audio_file)

if __name__ == "__main__":
    resize_video()
