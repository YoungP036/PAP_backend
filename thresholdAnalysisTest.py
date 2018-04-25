
from model.ModelManager import mManager
import sys

def main():

	if len(sys.argv)!=3:
		print("Enter params 1. output path for threshold data, 2. output path for raw probabilities")
		return -1
	
	THRESHOLD_OUTPUT_PATH=sys.argv[1]
	PROB_OUTPUT_PATH=sys.argv[2]
	all_images=[
		#typical non dog pictures	
		('https://qph.fs.quoracdn.net/main-qimg-fe6f92538c555d9e9f9f6292db4b9c25-c','Model cannot identify the breed'),#0 cup
		('https://www.pets4homes.co.uk/images/articles/771/large/cat-lifespan-the-life-expectancy-of-cats-568e40723c336.jpg','Model cannot identify the breed'),#1 cat
		('https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Cat-eating-prey.jpg/220px-Cat-eating-prey.jpg','Model cannot identify the breed'),#2 cat
		('https://timedotcom.files.wordpress.com/2017/12/terry-crews-person-of-year-2017-time-magazine-facebook-1.jpg?quality=85','Model cannot identify the breed'),#3 terry crews
		('https://citydiscovery2.imgix.net/new_york.jpg?w=2100&h=1100&bri=-12&q=30&auto=format&crop=entropy&fit=crop','Model cannot identify the breed'),#4 city
		('https://cdn.cnn.com/cnnnext/dam/assets/170727113446-central-park-bench-full-169.jpg','Model cannot identify the breed'),#5 park
		('https://ae01.alicdn.com/kf/HTB1y6u8HVXXXXbVXFXXq6xXFXXX0/simulation-animal-furry-fox-model-toy-polyethylene-furs-handicraft-props-decoration-gift-baby-toy-d404.jpg_640x640.jpg','Model cannot identify the breed'),#6 ??
		('https://vignette.wikia.nocookie.net/meerkats/images/3/33/Super_Furry_Animal%28Ella%29.jpg/revision/latest?cb=20101031064222','Model cannot identify the breed'),#7 marmot
		('https://www.telegraph.co.uk/content/dam/news/2016/08/23/106598324PandawaveNEWS_trans_NvBQzQNjv4Bqeo_i_u9APj8RuoebjoAHt0k9u7HhRJvuo-ZLenGRumA.jpg?imwidth=450','Model cannot identify the breed'),#8 panda
		('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8bsavvEb9CsdG2AEh386Ta5i7UwxRI0kPSZrHyyWATEOt66RpCA','Model cannot identify the breed'),#9 smoking monkey
		#typical good pictures
		('http://www.yourpurebredpuppy.com/dogbreeds/photos-IJKL/labradorretrievers2.jpg','labrador_retriever'),#10
		('https://static.seattletimes.com/wp-content/uploads/2017/03/03212017_Labrador_074401-780x521.jpg','labrador_retriever'),#11
		('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Owczarek_niemiecki_u%C5%BCytkowy_kr%C3%B3tkow%C5%82osy_suka.jpg/1200px-Owczarek_niemiecki_u%C5%BCytkowy_kr%C3%B3tkow%C5%82osy_suka.jpg','german_shepherd'),#12
		('http://www.insidedogsworld.com/wp-content/uploads/2017/07/German-Shepherd-Standard-Coat-GSC-1000x575-1-1-1-1.jpg','german_shepherd'),#13
		('http://www.yourpurebredpuppy.com/dogbreeds/photos-EFGH/goldenretrievers3.jpg','golden_retriever'),#14
		('https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Golden_Retriever_Carlos_%2810581910556%29.jpg/1200px-Golden_Retriever_Carlos_%2810581910556%29.jpg','golden_retriever'),#15
		('http://www.easypetmd.com/sites/default/files/Entlebucher%20Mountain%20Dog%20(1).jpg','entlebucher'),#16
		('https://i.pinimg.com/originals/da/d6/67/dad667b7b5975e95472226872cd4e6d6.jpg','entlebucher'),#17
		('https://steemit-production-imageproxy-upload.s3.amazonaws.com/DQmYW7bBsPPNaGjqCRugWXQWquTtk8bogiYsnbQV9dhhTEQ','rhodesian_ridgeback'),#18
		('http://static.pedigreedatabase.com/dogbreeds/rhodesian_ridgeback.jpg','rhodesian_ridgeback'),#19
		#bad pictures(bad weather, bad angles, obscured subject, etc.)
		('https://i.ytimg.com/vi/CuKYRQMQPTQ/hqdefault.jpg','samoyed'), #samoyed covered in snow
		('https://static1.squarespace.com/static/524727b8e4b016b87cc345e6/t/56a6b2f6df40f31ebb4d4145/1453765367654/','samoyed'), #samoyed during snow
		('https://thumb7.shutterstock.com/display_pic_with_logo/194452/541155871/stock-photo-labrador-in-the-fog-541155871.jpg','labrador_retriever'), #lab, fog, has watermark
		('https://media.gettyimages.com/photos/capelin-fishing-in-the-fog-at-forteau-labrador-newfoundland-and-picture-id79382677','Model cannot identify the breed'), #foggy weather, no dog
		('https://cmkt-image-prd.global.ssl.fastly.net/0.1.0/ps/2468688/910/683/m1/fpnw/wm0/cmindia-2210032ewfrm-.jpg?1490735381&s=b562308681ab9079bc2b7630eafaba44','german_shepherd'), #black and white
		('http://ak5.picdn.net/shutterstock/videos/10279655/thumb/1.jpg','labrador_retriever'),#person and dog far away
		('https://st.depositphotos.com/1489511/3387/i/950/depositphotos_33874329-stock-photo-labrador-retriever-in-the-rain.jpg','labrador_retriever'), #raining, dog soaking wet
		('https://i.pinimg.com/originals/06/8f/8f/068f8f9d699cc25cc930b5bbe046e8b0.jpg','labrador_retriever'), #raining, less wet dog
		('https://ak5.picdn.net/shutterstock/videos/1006910185/thumb/4.jpg?i10c=img.resize(height:160)','labrador_retriever'), #low light, wierd face
		('https://ak3.picdn.net/shutterstock/videos/1006910173/thumb/1.jpg?i10c=img.resize(height:160)','labrador_retriever'), #night time, face is lit
		('https://ak9.picdn.net/shutterstock/videos/1006910179/thumb/1.jpg?i10c=img.resize(height:160)','labrador_retriever') #night time, angled face is lit
	]

	all_thresholds=[0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.65, 0.7, 0.75, 0.8]
	
	model=mManager()
	query_probabilities=[]
	threshold_performance=[]

	print("\n\nBeginning optimal threshold search...")
	
	#get raw probability from model and save along with the expected label
	with open(PROB_OUTPUT_PATH,'w') as fp_out:
		for i,image in enumerate(all_images):
			print("Gathering data on image #" + str(i))
			try:
				url=image[0]
				expected_label=image[1]
				# print('URL: '+url)
				# print('label: ' +expected_label)
				actual_label,prob=model.queryModel(url)
				# print('actual: ' +actual_label)
				query_probabilities.append((prob,actual_label,expected_label))
				fp_out.write(str(prob)+', '+actual_label+', '+expected_label+'\n')
			except Exception as e:
				print("DBG exception " + str(e))
				return -1
	with open(THRESHOLD_OUTPUT_PATH,'w') as fp_out:
		#use each threshold to classify the raw probabilities, track performance in TP/TN/FP/FN
		for threshold in all_thresholds:
			#true pos, true neg, false pos, false neg
			TP=0
			TN=0
			FP=0
			FN=0
			for query_data in query_probabilities:
				prob=query_data[0]
				actual_label=query_data[1]
				expected_label=query_data[2]
				#logic for cases when we want the label to be cannot identify
				if expected_label is 'Model cannot identify the breed':
					if prob<=threshold:
						TN+=1
					else:
						FP+=1
				#logic for cases when we want the breed label
				else:
					if prob<=threshold:
						FN+=1
					else:
						if actual_label==expected_label:
							TP+=1

			fp_out.write(str(threshold)+', '+str(TP)+', '+str(TN)+', '+str(FP)+', '+str(FN)+'\n')
	print("\nExiting gracefully...")
if __name__ == "__main__":
	main()