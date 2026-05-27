express_orders = [
    "GE101",
    "GE102-WRONG",
    "GE103-CANCEL"
]

# Thêm đơn mới
express_orders.append("GE104")

# Chèn đơn hỏa tốc
express_orders.insert(0, "GE100-FAST")

# Sửa đơn nhập sai
express_orders[2] = "GE102-UPDATED"

# Xóa đơn hủy
express_orders.remove("GE103-CANCEL")

# Lấy đơn đầu tiên ra giao
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)