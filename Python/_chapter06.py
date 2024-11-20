{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOzNMwQYizjXAwhZqGEkMgf"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["변수 : 하나의 값을 저장할 수 있는 공간을 생성하는 것\n","\n","변수명을 만들때 컨벤션  \n","변수를 표현하는 방법 : 스네이크 카멜  \n","변수를 활용해서 다양한 문제  \n","\n"],"metadata":{"id":"VvPdHk-hr3d_"}},{"cell_type":"code","execution_count":null,"metadata":{"id":"vOx_geMRrot3"},"outputs":[],"source":["# 1. int(integer) : 정수\n","# 2. float(float) : 실수\n","# 3. str(String)  : 문자\n","# 4. bool(bool,boolean) : 참 또는 거짓, true 또는 false, 1 또는 0\n","# 5. list\n","# 6. tuple\n","# 7. dict\n","# 8. set"]},{"cell_type":"code","source":["1.1 + 2\n","\n","4 / 2"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"ITaW83i8tIs2","executionInfo":{"status":"ok","timestamp":1731990985941,"user_tz":-540,"elapsed":525,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"a5f9bd65-c56f-4f69-ba17-c6987d515f2a"},"execution_count":1,"outputs":[{"output_type":"execute_result","data":{"text/plain":["2.0"]},"metadata":{},"execution_count":1}]},{"cell_type":"code","source":["# 정수 : 1,2,3,4, -1,-4\n","# 실수 : 1.2,4.0\n","\n","9.0 + 2"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"fS8QBPiAtQWB","executionInfo":{"status":"ok","timestamp":1731991063532,"user_tz":-540,"elapsed":526,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"9fbaf615-a35f-48c4-edbc-1dbb190b2572"},"execution_count":2,"outputs":[{"output_type":"execute_result","data":{"text/plain":["11.0"]},"metadata":{},"execution_count":2}]},{"cell_type":"code","source":["#box_num 에 숫자만 넣자는 약속을 함. 근데 누가 한글표기법으로 숫자를 넣음\n","\n","box_num = \"하나\"\n","box_num += 1 컴은 허용 되지 않음, 타입을 미리 저장하지 않고 결과 나올때 정해져서 오류가 나는 것\n","print(box_num)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"_BaaZgZ0t0F-","executionInfo":{"status":"ok","timestamp":1731991926076,"user_tz":-540,"elapsed":525,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"2a667f1e-62bb-4004-93bd-5b5a52bcfb56"},"execution_count":6,"outputs":[{"output_type":"stream","name":"stdout","text":["하나\n"]}]},{"cell_type":"code","source":["type(box_num)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"KabE_wzhwHQm","executionInfo":{"status":"ok","timestamp":1731991930275,"user_tz":-540,"elapsed":530,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"6b557e3b-6f52-4479-8890-bca5dcfcc097"},"execution_count":7,"outputs":[{"output_type":"execute_result","data":{"text/plain":["str"]},"metadata":{},"execution_count":7}]},{"cell_type":"code","source":["type(1)\n","type(1.2)"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"tffGyitbxB-i","executionInfo":{"status":"ok","timestamp":1731992009964,"user_tz":-540,"elapsed":511,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"d6b5d05e-6b4a-47bf-e3dd-191655f9405f"},"execution_count":9,"outputs":[{"output_type":"execute_result","data":{"text/plain":["float"]},"metadata":{},"execution_count":9}]},{"cell_type":"code","source":["#가져야할 값이 2여야하는 데 파이썬은 실수영역이 더 커서 실수값이 결과값에 출력되는 것임.\n","#형변환\n","\n","4/2"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"OaNPnIMdxOPY","executionInfo":{"status":"ok","timestamp":1731992026745,"user_tz":-540,"elapsed":517,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"d1626892-7736-4f79-c806-48f457e41565"},"execution_count":10,"outputs":[{"output_type":"execute_result","data":{"text/plain":["2.0"]},"metadata":{},"execution_count":10}]},{"cell_type":"markdown","source":["### 말 그대로 형태를 변형한다. : 형변환\n","\n","int, float  int -> float\n","ex)5 ->5.0 float(5)"],"metadata":{"id":"-_9dcq00xn-9"}},{"cell_type":"code","source":["print(float(5))\n","print(int(5.0))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"lcc8nFb0xlPA","executionInfo":{"status":"ok","timestamp":1731992257431,"user_tz":-540,"elapsed":528,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"dbe6931e-ad12-42d7-9b0f-7fc8035dec25"},"execution_count":11,"outputs":[{"output_type":"stream","name":"stdout","text":["5.0\n","5\n"]}]},{"cell_type":"code","source":["나이=10\n","type(나이)\n","print(dir(나이))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"9MVAzBSoyOlJ","executionInfo":{"status":"ok","timestamp":1731992319871,"user_tz":-540,"elapsed":1008,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"f079a207-a05a-4f94-ab21-2286ed18aa9f"},"execution_count":12,"outputs":[{"output_type":"stream","name":"stdout","text":["['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']\n"]}]},{"cell_type":"code","source":["print(나이.bit_length()) #숫자 10을 비트로 변환해 길이를 알려주는 것\n","print(bin(나이))"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"18-xgR7cygYG","executionInfo":{"status":"ok","timestamp":1731992393219,"user_tz":-540,"elapsed":527,"user":{"displayName":"최혜민","userId":"04567162278317362637"}},"outputId":"2913fe72-7a37-45b3-ba78-90524cd86b5b"},"execution_count":14,"outputs":[{"output_type":"stream","name":"stdout","text":["4\n","0b1010\n"]}]},{"cell_type":"markdown","source":["###메소드/내장함수/함수\n","설명할 수 있어야 좋음."],"metadata":{"id":"KKElNc16y_Vs"}}]}