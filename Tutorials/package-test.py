# 封包測試
# 當主程式與封包資料夾在同一層就可以直接使用模組
import modules.point as point
result = point.distance(3,4)
print("距離",result)

import modules.line as line
result = line.slope(1,1,3,3)
print("斜率",result)

result = line.len(1,1,2,2)
print("長度",result)