# Helen Sun hs667
# Juliana Hong jhh274
# Anna Tedijanto ajt232
import numpy as np
import json

class Baseline:
	def __init__(self, test_filepath):
		#self.processFiles(test_filepath)
		self.loadTestingData("testing.json")

	"""
	Loads paragraphs and questions
	self.paragraphs is array of paragraph texts
	and has structure ["paragraph 1 text", "paragraph 2 text" ...]
									
	self.questions is a 2d array, where each inner array is the list of questions for that paragraph
	and has structure [[q1, q2, ...], [q1, q2, ...] ...]]
	e.g. 
	self.paragraphs = ["Architecturally, the school has...", "As at most ...", ...]
	self.questions = [["To whom did the Virgin ... ?", "What is in front ...?"],
					 [""When did the Scholastic ...?", "How often is ...?"] ...]
	"""
	def loadTestingData(self, test_filepath):
		with open(test_filepath) as file:
			testing_json = json.load(file)
		
		testing_data = testing_json['data']

		paragraphs_list = []
		questions_list = []

		for section in testing_data:
			title = section["title"]
			paragraphs = section["paragraphs"]

			for paragraph in paragraphs:
				questions_in_paragraph = []
				paragraphs_list.append(paragraph["context"])

				qas = paragraph["qas"]
				for question in qas:
					questions_in_paragraph.append(question["question"])
				questions_list.append(questions_in_paragraph)

		self.paragraphs = paragraphs_list
		self.questions = questions_list

		# print(self.questions[0])


baseline = Baseline("training.json")
