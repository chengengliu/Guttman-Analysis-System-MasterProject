import unittest
import os
import shutil
import json
import model.storage as st


class StorageTestCase(unittest.TestCase):
    def setUp(self) -> None:
        shutil.copytree('upload/', 'upload_bak/')
        shutil.rmtree('upload/', ignore_errors=True, onerror=None)
        os.makedirs('upload/1/mod/')
        os.mkdir('upload/1/ori/')
        shutil.copyfile('testdata/SampleAssessmentResult.xlsx', 'upload/1/ori/SampleAssessmentResult.xlsx')
        shutil.copyfile('testdata/SampleAssessmentResult.xlsx', 'upload/1/mod/SampleAssessmentResult.xlsx')
        shutil.copyfile('testdata/result.json', 'upload/1/result.json')

    def tearDown(self) -> None:
        shutil.rmtree('upload/', ignore_errors=True, onerror=None)
        shutil.copytree('upload_bak/', 'upload/')
        shutil.rmtree('upload_bak/', ignore_errors=True, onerror=None)

    def test_get_export_path(self):
        file_dir, file = st.get_export_path(1)
        self.assertEquals(file_dir, st.get_base_dir(1) + 'mod/')
        self.assertEquals(file, 'SampleAssessmentResult.xlsx')

    def test_get_base_dir(self):
        self.assertEquals(st.get_base_dir(1), 'upload/1/')

    def test_make_new_path(self):
        fid, ori_path, mod_path = st.make_new_path('MadeInAbyss')
        self.assertEquals(fid, 2)
        self.assertEquals(ori_path, 'upload/2/ori/MadeInAbyss')
        self.assertEquals(mod_path, 'upload/2/mod/MadeInAbyss')
        self.assertTrue(os.path.isdir('upload/2/'))
        self.assertTrue(os.path.isdir('upload/2/ori/'))
        self.assertTrue(os.path.isdir('upload/2/mod/'))
        shutil.rmtree('upload/2/', ignore_errors=True, onerror=None)

    def test_allowed_file(self):
        self.assertTrue(st.allowed_file("WeatheringWithYou.xLSx"))
        self.assertTrue(st.allowed_file("a..place..further..than..the..universe.pnG.XlS"))
        self.assertFalse(st.allowed_file("--> BLACKHOLE <--"))
        self.assertFalse(st.allowed_file("This action will have consequences...butterfly"))

    def test_get_file_list(self):
        result = st.get_result(1)
        self.assertEquals([result], st.get_file_list())

    def test_delete_file(self):
        st.delete_file(1)
        self.assertFalse(os.path.isdir('upload/1/'))

    def test_get_result(self):
        result = st.get_result(1)
        with open('upload/1/result.json', 'r') as json_file:
            self.assertEquals(result, json.load(json_file))

    def test_save_result(self):
        data = {'Orcas Hunt': 'Sperm Whales'}
        st.save_result(data, 1)
        self.assertEquals(data, st.get_result(1))
