# test_app.py
from app import add, subtract

def test_add():
    # نتحقق هل 5 + 5 تساوي 10 فعلاً؟
    assert add(5, 5) == 10
    # نتحقق من الأرقام السالبة
    assert add(-1, 1) == 0

def test_subtract():
    # نتحقق هل 10 - 7 تساوي 3 فعلاً؟
    assert subtract(10, 7) == 3

def test_add_wrong_value():
    # هذا الاختبار سيفشل إذا كانت النتيجة غير 5
    # نستخدمه للتأكد أن الـ CI سيعطي علامة حمراء عند الخطأ
    assert add(2, 2) == 4
