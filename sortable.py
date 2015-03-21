#   A Solution to the Coding Challenge @Sortable
#	By Hung-Liang (Leon) Lai
#   March 20, 2015
#
import json

def extract(filename,key,JsonObjects,KeySets):
#  Given a file and its target key
#     extract the arrays of JSON objects and the corresponding key sets
#


# open the file in filename
# loop over each line of the file
#    load the line in JSON object
#    append it to JsonObjects
#    convert the key in the object with every letter into lower case and
#       replace '-' and '_' by simply space for easy split of the key values
#    append the converted key into KeySets
# close the file
	f=open(filename)
	for line in f:
		x=json.loads(line)
		JsonObjects.append(x)
		xx=x[key].lower().replace('-',' ').replace('_',' ').split()
		KeySets.append(set(xx))
	f.close()

def sortable():
# main function sortable

# read through file 'products.txt' with the key of 'product_name'
# extract the JSON objects and the corresponding key sets
	ProductObjects=[]
	ProductKeySets=[]
	extract('products.txt','product_name',ProductObjects,ProductKeySets)
	NumberProducts=len(ProductObjects)

# similarly for file 'listings.txt' with the key of 'title'
	ListingObjects=[]
	ListingKeySets=[]
	extract('listings.txt','title',ListingObjects,ListingKeySets)
	NumberListings=len(ListingObjects)

# open a file "results.txt" for the output results
# loop over the total number of products and then 
#    loop over the total number of listings
#       compare if key set of the product is fully contained in key set of the listing
#          if yes, append the listing to the result.listings
#    write out the resultant JSON object in the required form
# close the file
	ff=open("results.txt","w")
	for np in range(NumberProducts):
		listings=[]
		for nl in range(NumberListings):
			if (ProductKeySets[np] == ListingKeySets[nl] & ProductKeySets[np]):
				listings.append(ListingObjects[nl])
		result={'product_name':ProductObjects[np]['product_name'], 'listings':listings}
		json.dump(result,ff)
		ff.write("\n")

	ff.close()
	
if __name__ == "__main__":
	sortable()

