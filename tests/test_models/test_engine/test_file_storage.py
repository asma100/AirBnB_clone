#!/usr/bin/python3
"""
Unittest Module for FileStorage
"""
import unittest
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ Unittest for FileStorage """

    def test_Instantiation(self):
        """ instance is of BaseModel """
        self.FileStorage = FileStorage()
        self.assertIsInstance(self.FileStorage, FileStorage)

    def test_Access(self):
        """  read-write access permissions """
        rd = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(rd)
        wr = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(wr)
        ex = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(ex)

    

    def test_reload(self):
        """
        Tests method: reload (reloads oects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
    def test_new(self):
        """
        new 
        """
        m_stor = FileStorage()
        instances_dic = m_stor.all()
        Aman = User()
        Aman.id = 999999
        Aman.name = "Aman"
        m_stor.new(Aman)
        k = Aman.__class__.__name__ + "." + str(Aman.id)
        self.assertIsNotNone(instances_dic[k])
    def test_funcdocs(self):
        """ docstring """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_save(self):
        """ save method"""
        o = FileStorage()
        new_o = BaseModel()
        o.new(new_o)
        dict1 = o.all()
        o.save()
        o.reload()
        dict2 = o.all()
        for k in dict1:
            k1 = k
        for k in dict2:
            k2 = k
        self.assertEqual(dict1[k1].to_dict(), dict2[k2].to_dict())


if __name__ == '__main__':
    unittest.main()
