def mergeSort(array, start=0, end=None):
    if end is None:
        end = len(array)

    # Base da recursão: se o intervalo contém 1 ou 0 elementos
    if end - start > 1:
        center = (end + start) // 2
        mergeSort(array, start, center)  # LADO ESQUERDO
        mergeSort(array, center, end)   # LADO DIREITO
        merge(array, start, center, end)

def merge(array, start, center, end):
    leftArray = array[start:center]
    rightArray = array[center:end]

    leftTop, rightTop = 0, 0

    for i in range(start, end):
        if leftTop >= len(leftArray):
            array[i] = rightArray[rightTop]
            rightTop += 1
        elif rightTop >= len(rightArray):
            array[i] = leftArray[leftTop]
            leftTop += 1
        elif leftArray[leftTop] < rightArray[rightTop]:
            array[i] = leftArray[leftTop]
            leftTop += 1
        else:
            array[i] = rightArray[rightTop]
            rightTop += 1

def insertionSort(array):
    lenght = len(array)
    for i in range(1, lenght):
        key = array[i]
        condListaOrdenada = i - 1
        while condListaOrdenada >= 0 and array[condListaOrdenada] > key:
            array[condListaOrdenada+1] = array[condListaOrdenada]
            condListaOrdenada-=1
        array[condListaOrdenada+1] = key

def bubbleSort(array):
    length = len(array)
    for iteration in range(length - 1):
        for currentIndex in range(length - 1 - iteration):
            if array[currentIndex] > array[currentIndex + 1]:
                # Troca os elementos de posição
                array[currentIndex], array[currentIndex + 1] = array[currentIndex + 1], array[currentIndex]


# Teste do algoritmo
mergeArray = [2, 3, 4, 1, 5, 7, 1, 1]
mergeSort(mergeArray)
print("Array ordenado (MergeSort):", mergeArray)
inserArray = [2, 3, 4, 1, 5, 7, 1, 1]
insertionSort(inserArray)
print("Array ordenado (InsertionSort):", inserArray)
bubbleArray = [2, 3, 4, 1, 5, 7, 1, 1]
bubbleSort(bubbleArray)
print("Array ordenado (BubbleSort):", bubbleArray)





def search(array, searched):
    for i in range(len(array)):
        if array[i] == searched:
            return i 
    return None  

searchArray = [2, "3", 4, 1, "nao", 7, 1, 1] 
element = 3
indx = search(searchArray, element)

if indx is not None:
    print("Indicie: {} do elemento {}".format(indx, element))
else:
    print("Elemento {} não encontrado".format(  element))


def binarySearch(array, searched):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == searched:
            return mid
        elif array[mid] < searched:
            left = mid + 1
        else:
            right = mid - 1
    return None

binaryArray = [1, 1, 2, 3, 4, 5, 7]
searched = 4
index = binarySearch(binaryArray, searched)

if index is not None:
    print("Índice: {} do elemento {}".format(index, searched))
else:
    print("Elemento {} não encontrado".format(searched))
