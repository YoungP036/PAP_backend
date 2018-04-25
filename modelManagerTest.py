from model.ModelManager import mManager

#The purpose of this test is to check that modelManager is properly providing an interface with the model
#It is not to assess the accuracy or usefullness of the model itself
def main():
	test_set=[
		('https://st.depositphotos.com/1489511/3387/i/950/depositphotos_33874329-stock-photo-labrador-retriever-in-the-rain.jpg','golden_retriever'),	
		('https://static1.squarespace.com/static/524727b8e4b016b87cc345e6/t/56a6b2f6df40f31ebb4d4145/1453765367654/','samoyed'),
		('','download_error')
		]

	model=mManager()
	res1=model.queryModel(test_set[0][0])
	print("\n\nBeginning modelManager unit test...\n")
	printResult(assertExpectedActual(test_set[0][1], res1[0]), 'test 1',res1[0])
	
	res2=model.queryModel(test_set[1][0])
	printResult(assertExpectedActual(test_set[1][1], res2[0]), 'test 2',res2[0])

	res3=model.queryModel(test_set[2][0])
	printResult(assertExpectedActual(test_set[2][1], res3[0]), 'test 3',res3[0])

	print("\nExiting gracefully...\n")

def assertExpectedActual(expected,actual):
	if expected.lower()!=actual.lower():
		return False
	else:
		return True
def printResult(pass_flag, target, returned_label):
	if pass_flag:
		print(target +" **PASSED** with label " +returned_label)
	else:
		print(target +" **FAILED** with label " +returned_label)
if __name__=="__main__":
	main()