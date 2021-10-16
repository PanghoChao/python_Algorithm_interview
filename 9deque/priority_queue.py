# make heap function


## 힙 더하기
def heapinsert(heap, item):
    heap.append(item)
    percolate_down(heap, 0, len(heap)-1)    

def percolate_down(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem




##힙 추출하기
def heapextract(heap):
    
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0] 
        heap[0] = lastelt
        percolate_up(heap, 0)
        return returnitem
    return lastelt


def percolate_up(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    percolate_down(heap, startpos, pos)

test = [3,6,2,1,10,0]
prt =[]
for i in test:
    heapinsert(prt, i)
print(prt)

print(heapextract(prt))
print(prt)

print(heapextract(prt))
print(prt)

#이진트리를 처음 접해서 생각보다 이해하는데 오래 걸렸다.
