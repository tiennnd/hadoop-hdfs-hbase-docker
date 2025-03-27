import happybase

# Kết nối đến HBase
connection = happybase.Connection('localhost', port=9090)
connection.open()

# Tạo bảng (nếu chưa tồn tại)
try:
    connection.create_table(
        'employees1',
        {
            'personal_data': dict(max_versions=3),
            'job_data': dict()
        }
    )
except:
    print("Table already exists")

# Chọn bảng
table = connection.table('employees1')

# Ghi dữ liệu bằng batch
with table.batch() as batch:
    batch.put('row1', {
        'personal_data:name': 'John Doe',
        'personal_data:age': '30',
        'job_data:position': 'Engineer'
    })
    batch.put('row2', {
        'personal_data:name': 'Jane Smith',
        'personal_data:age': '28',
        'job_data:position': 'Manager'
    })

# Kiểm tra dữ liệu
print("Dữ liệu trong bảng employees1:")
for key, data in table.scan():
    print(key, data)

# Đóng kết nối
connection.close()



