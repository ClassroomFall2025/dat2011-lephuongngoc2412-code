def menu():
    while True:
        print("\n======================== MENU =============================")
        print("1. Nhập danh sách nhân viên từ bàn phím")
        print("2. Đọc thông tin nhân viên và xuất danh sách nhân viên ra màn hình")
        print("3. Tìm và hiển thị nhân viên theo mã")
        print("4. Xóa nhân viên theo mã nhập từ bàn phím và cập nhật dữ liệu")
        print("5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file")
        print("6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím")
        print("7. Sắp xếp danh sách nhân viên theo họ và tên")
        print("8. Sắp xếp danh sách nhân viên theo thu nhập")
        print("9. Xuất 5 nhân viên có thu nhập cao nhất công ty")
        print("0. Thoát chương trình")
        print("============================================================")

        chon = int(input("Nhập lựa chọn của bạn: "))
        match chon:
            case 1:
                print(" Thực hiện nhập danh sách nhân viên và lưu vào file...")
            case 2:
                print(" Đọc thông tin nhân viên từ file và hiển thị...")
            case 3:
                print(" Tìm nhân viên theo mã...")
            case 4:
                print(" Xóa nhân viên theo mã...")
            case 5:
                print(" Cập nhật thông tin nhân viên...")
            case 6:
                print(" Tìm nhân viên theo khoảng lương...")
            case 7:
                print(" Sắp xếp nhân viên theo họ tên...")
            case 8:
                print(" Sắp xếp nhân viên theo thu nhập...")
            case 9:
                print(" Xuất 5 nhân viên có thu nhập cao nhất...")
            case 0:
                print("Đã thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại!")
menu()
