import wikipedia

info = wikipedia.summary("American Staffordshire Terrier", sentences = 5)  
	  
data = "The American Staffordshire Terrier, also known as Amstaff (in the United States), is a medium-sized, short-coated American dog breed. It is one of several breeds in the pit bull group. In the early part of the twentieth century the breed gained social stature and was accepted by the American Kennel Club in 1936 and should not be confused with the Staffordshire Bull Terrier of the United Kingdom.\n\n\n== History ==\n\nThe Staffordshire Terrier's ancestor, the bull and terrier was first bred in the nineteenth century in Birmingham. The early ancestors of this breed came from England where, until the first part of the 19th century, the Bulldog was bred."  
	  
if info == data:  
	print ("success")  
else:  
  print("Fails")  
