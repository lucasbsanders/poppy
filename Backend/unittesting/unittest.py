import unittest
import modules.text_processor
import modules.image_processor
import modules.create_event
from img_set import imgset
from instruction_set import instructionset
from log_file_set import logfileset
from instruction_set import whitespacecorrectedset
from instruction_set import correctedinstructionset


class TestBackendMethods(unittest.TestCase):

    def test_create_event(self):
        self.assertEqual(create_event.times_per_day(instructionset.instruction1), 'numPlaceHolder1')
        self.assertEqual(create_event.times_per_day(instructionset.instruction2), 'numPlaceHolder2')
        self.assertEqual(create_event.times_per_day(instructionset.instruction3), 'numPlaceHolder3')
        #input the correct numbers to be expected before running

        self.assertNotEqual(create_event.create_log_file(instructionset.instruction1), logfileset.log1)
        self.assertNotEqual(create_event.create_log_file(instructionset.instruction2), logfileset.log2)
        self.assertNotEqual(create_event.create_log_file(instructionset.instruction3), logfileset.log3)
        #check if created file by the event creator is equivalent to the preselected log file, as this
        #function does not produce a returned log

    def test_image_processor(self):
        self.assertEqual(image_processor.resize(imgset.incimg1), imgset.img1)
        self.assertEqual(image_processor.resize(imgset.incimg2), imgset.img2)
        self.assertEqual(image_processor.resize(imgset.incimg3), imgset.img3)
        #place unsized and expected size images in imgset file

        self.assertEqual(image_processor.get_text("test"), "testing testing")

    def test_text_processor(self):
       self.assertEqual(text_processor.removes_whitespace(instructionset.instruction1), whitespacecorrectedset.whitespace_cleaned_instruction1)
       self.assertEqual(text_processor.removes_whitespace(instructionset.instruction2), whitespacecorrectedset.whitespace_cleaned_instruction2)
       self.assertEqual(text_processor.removes_whitespace(instructionset.instruction2), whitespacecorrectedset.whitespace_cleaned_instruction3)
        #place expected cleaning of instruction in whitespacecorrectedset file

       self.assertEqual(text_processor.correct_instruction(instructionset.instruction1), correctedinstructionset.corrected_Instruction1)
       self.assertEqual(text_processor.correct_instruction(instructionset.instruction2), correctedinstructionset.corrected_Instruction2)
       self.assertEqual(text_processor.correct_instruction(instructionset.instruction3), correctedinstructionset.corrected_Instruction3)
       

if __name__ == '__main__':
    unittest.main()
    TestBackendMethods.test_image_processor()