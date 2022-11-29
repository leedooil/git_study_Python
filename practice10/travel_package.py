# import travel.thailand
# # import travel.thailand.ThailandPackage # 클래스 명은 import 못함
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from import 구문에선 클래스명 import가능
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# # from random import *
# # from travel import thailand
from travel import * # 이렇게 쓰려면 __init__파일에서 직접 import범위 정해줘야함
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

