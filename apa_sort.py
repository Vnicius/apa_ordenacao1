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

		for x in range(n//2,-1,-1):
			self.maxHeap(array,x,n)

	def sort(self,array):
		self.buildHeap(array)

		n = len(array) - 1

		for x in range(n,-1,-1):
			self.swap(array,0,x)
			n-=1
			self.maxHeap(array,0,n)

######################################

class MergeSort:
	
	def sort(self,lista):

		if len(lista) > 1:
			meio = len(lista)/2

			listaEsq = lista[:meio]
			listaDir = lista[meio:]

			self.sort(listaEsq)
			self.sort(listaDir)

			i = j = k = 0

			while i < len(listaEsq) and j < len(listaDir):
				if listaEsq[i] < listaDir[j]:
					lista[k] = listaEsq[i]
					i += 1
				else:
					lista[k] = listaDir[j]
					j+= 1
				k += 1

			while i < len(listaEsq):
				lista[k] = listaEsq[i]
				i+=1
				k+=1

			while j < len(listaDir):
				lista[k] = listaDir[j]
				j+=1
				k+=1

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
	op = int(sys.argv[1])
	vetor = []
	tam = input()
	cont = 0

	while cont <= tam-1:
		x = input()
		vetor.append(x)
		cont+=1

	if op == 1:
		sort = SelectionSort()
		sort.sort(vetor)
	elif op == 2:
		sort = InsertionSort()
		sort.sort(vetor)
	elif op == 3:
		sort = MergeSort()
		sort.sort(vetor)
	elif op == 4:
		sort = QuickSort()
		sort.sort(vetor)
	elif op == 5:
		sort = HeapSort()
		sort.sort(vetor)	

	for x in range(0,len(vetor)):
		print(vetor[x])
