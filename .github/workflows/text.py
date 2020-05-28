import time

# Khai Báo Thông Tin Nhân Vật Chính Tadashi Ringo
nvc = "- Nhân vật chính tên: 【Tadashi Ringo】"
nvc_tuoi = "- Số Tuổi: 17"
nvc_chung_toc = "- Chủng Tộc: Nhân Loại(Đã Từng), Tinh Linh(Hiện Tại)"
nvc_nang_luc = "- Năng Lực:《Vô Hạn Võ Đạo》, 《Gate Of Babylon》, 《Thiên Lý Nhãn》, 《Imagine Breaker》, 《Đệ Tam Vĩnh Cửu Động Cơ》, 《Đệ Tam Pháp》"
nvc_bao_cu = []
nvc_bao_cu.append("- Bảo Cụ:")
nvc_bao_cu.append("《Gate Of Babylon》")
nvc_bao_cu.append("《Ngôn Linh Đao》")
nvc_kabbalah = "- Kabbalah: Viêm Ma, Phá Quân Ca Cơ..."

nvc_list_hau_cung = ["Scathach", "Zenjou Aoi", "Matou Sakura", 
                     "Tohsaka Rin", "Irisviel", "Altria Alter", 
                     "Yoshino", "Itsuka Kotori", "Katou Aki"
                     ]


i = 0
x = 1
z = i
dung = 10
while i <= 10:
  print (nvc_list_hau_cung[i]+"/"+ nvc_list_hau_cung[x])
  i += 2
  z = i
  x = z + 1
  



# Bảo Cụ
bao_cu = "Bảo Cụ là một loại vũ khí của Anh Linh, chúng được hình thành từ tín ngưỡng hay các truyền thuyết của nhân loại kết tinh ý chí sáng tạo đi ra"
list_bao_cu = ["《Gate Of Babylon》","《Thiên Lý Nhãn》"]

#Thời Gian Hôm Nay
seconds = time.time()
print ("Bây Giờ Là:")
local_time = time.ctime(seconds)
year_new = time.localtime()
print ("Năm:", year_new.tm_year)
print ("Ngày:", year_new.tm_mday)
print ("#########")


#Hệ Thống
print ("————")
print ("Mời Bạn Nhập Câu Lệnh")
print ("————")
nhap_player = input()

#Cú Pháp Hỗ Trợ
if nhap_player == "/help":
  print ("THÔNG TIN CÁC CÚ PHÁP")
  print ("/help: Cú pháp hiển thị thông tin trợ giúp")
  print ("/nvc: Cú pháp hiển thị thông tin nhân vật chính Tadashi Ringo")
  print ("/baocu: Cú pháp truy cập thông tin bảo cụ")

#Cú Pháp Nhân Vật Chính
if nhap_player == "/nvc":
    print (nvc)
    print (nvc_tuoi)
    print (nvc_chung_toc)
    print (nvc_nang_luc)
    print (nvc_kabbalah)
    i = 0
    while i <= 10:
      print (nvc_bao_cu[i])
      i += 1 

#Cú Pháp Bảo Cụ

elif nhap_player == "/baocu":
      print (bao_cu)
      print (" ")
      print ("———Nhập Tên Hoặc Số Thứ Tự Bảo Cụ———")
      nhap_bao_cu = input()
      xprint ("Bảo Cụ là:" + nhap_bao_cu)
      