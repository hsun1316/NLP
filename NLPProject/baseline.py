# Helen Sun hs667
# Juliana Hong jhh274
# Anna Tedijanto ajt232
import numpy as np
import json

class Baseline:
	def __init__(self, test_filepath):
		#self.processFiles(test_filepath)
		self.loadTestingData("testing.json")
		self.predictAnswer()

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
		question_id_list = []

		for section in testing_data:
			title = section["title"]
			paragraphs = section["paragraphs"]

			for paragraph in paragraphs:
				questions_in_paragraph = []
				ids_in_paragraph = []
				sentences = paragraph["context"].split(".")
				paragraphs_list.append(sentences)

				qas = paragraph["qas"]
				for question in qas:
					questions_in_paragraph.append(question["question"])
					ids_in_paragraph.append(question["id"])
				questions_list.append(questions_in_paragraph)
				question_id_list.append(ids_in_paragraph)
		self.paragraphs = paragraphs_list
		self.questions = questions_list
		self.ids = question_id_list

	def randAnswer(self, questionIndex, paragraphIndex):


	def predictAnswer(self):
		predictions = {}
		for outerInd in range(len(self.questions)):
			for innerInd in range(len(self.questions[outerInd])):
				randomAnswer = self.randAnswer(innerInd, outerInd)
				predictions[self.ids[outerInd][innerInd]] = randomAnswer

		f = open('predictions.json', 'w')
		f.write(json.dumps(predictions))
		f.close()


baseline = Baseline("training.json")
