import unittest

# get_full_name funksiyasini birinchi bo'lib yozamiz
def get_full_name(ism, familiya, otasi=''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()   
    else:
        return f"{ism} {familiya}".title()

# Test klassi
class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon', 'valiyev')        
        self.assertEqual(formatted_name, 'Alijon Valiyev')

    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan', 'husanov', 'olimovich')
        self.assertEqual(name, 'Hasan Olimovich Husanov')

# Unittestni ishga tushiramiz
if __name__ == "__main__":
    unittest.main()
