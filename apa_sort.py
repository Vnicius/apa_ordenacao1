import sys

class SelectionSort:
	def sort(self,array):
		n = len(array)

		for i in range(0,n-1):
			min = i

			for j in range(i+1,n):
				if array[j] < array[min]:
					min = j

			x = array[min]
			array[min] =  array[i]
			array[i] = x


#########################
class QuickSort(object):
	def partition(self,array,ini,fim):
		pivo = array[ini]
		topo = ini

		for i in range(ini,fim+1):
			if array[i] < pivo:
				array[topo] = array[i]
				array[i] = array[topo+1]
				topo+=1	

		array[topo] = pivo
		return topo
	
	def quickSort(self,array,ini,fim):
		if ini<fim:
			meio = self.partition(array,ini,fim)

			self.quickSort(array,ini,meio)
			self.quickSort(array,meio+1,fim)

	def sort(self, array):
		self.quickSort(array,0,len(array)-1);

#########################
class HeapSort(object):
	def swap(self,array,i,j):
		aux = array[i]
		array[i] = array[j]
		array[j] = aux

	def maxHeap(self,array,i,tam):
		left = 2*i
		right = 2*i + 1
		maior = i
		
		if left <= tam and array[left] > array[i]:
			maior = left

		if right <= tam and array[right] > array[maior]:
			maior = right

		if maior != i:
			self.swap(array,i,maior)  
			self.maxHeap(array,maior,tam)

	def buildHeap(self, array):
		n = len(array) - 1

		for x in range(n//2,0,-1):
			self.maxHeap(array,x,n)

	def sort(self,array):
		self.buildHeap(array)

		n = len(array) - 1

		for x in range(n,0,-1):
			self.swap(array,0,x)
			n-=1
			self.maxHeap(array,0,n)

######################################

class MergeSort:
	
	def merge(self,array,ini,meio,fim):
		b=[]
		for x in array:
			b = b+[x]

		i = ini
		j = meio + 1
		k = ini

		while i <= meio and j<= fim:
			if b[i] <= b[j]:
				array[k] = b[i]
				i+=1
			else:
				array[k] = b[j]
				j+=1
			k+=1

		while i<=meio:
			array[k] = b[i]
			i+=1
			k+=1

		while j<=fim:
			array[k] = b[j]
			j+=1
			k+=1

	def mergeSort(self,array,ini,fim):
		if ini < fim:
			meio = ini + (fim - ini)//2

			self.mergeSort(array,ini,meio)
			self.mergeSort(array,meio+1,fim)

			self.merge(array,ini,meio,fim)


	def sort(self,array):
		self.mergeSort(array,0,len(array)-1)

###################

class InsertionSort(object):
	def sort(self,array):

		for i in range(1, len(array)):
			chave = array[i]
			k = i
			while k > 0 and chave < array[k-1]:
				array[k] = array[k-1]
				k -= 1
			array[k] = chave

########################

if __name__ == '__main__':
	op = sys.argv[1]
	vetor = sys.argv[2]
	print(op)
	if int(op) == 0:
		sort = SelectionSort()
		sort.sort(vetor)
		print(vetor)

	print(vetor+"1")
