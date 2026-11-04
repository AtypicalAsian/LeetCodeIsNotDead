package main

import (
	"container/heap"
	"math"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type MaxHeap struct{ IntHeap }
func (h MaxHeap) Less(i, j int) bool { return h.IntHeap[i] > h.IntHeap[j] }

func minOperations(nums []int, x int, k int) int64 {
	n := len(nums)
	vals := make([]int64, n)

	lower := &MaxHeap{}
	upper := &IntHeap{}
	lowerDel := make(map[int]int, k)
	upperDel := make(map[int]int, k)
	lowerSize, upperSize := 0, 0
	var sumLower, sumUpper int64

	pruneUpper := func() {
		for upper.Len() > 0 {
			top := (*upper)[0]
			if cnt := upperDel[top]; cnt > 0 {
				if cnt == 1 {
					delete(upperDel, top)
				} else {
					upperDel[top] = cnt - 1
				}
				heap.Pop(upper)
			} else {
				break
			}
		}
	}

	pruneLower := func() {
		for lower.Len() > 0 {
			top := lower.IntHeap[0]
			if cnt := lowerDel[top]; cnt > 0 {
				if cnt == 1 {
					delete(lowerDel, top)
				} else {
					lowerDel[top] = cnt - 1
				}
				heap.Pop(lower)
			} else {
				break
			}
		}
	}

	rebalance := func() {
		pruneUpper()
		pruneLower()

		for upperSize > lowerSize+1 {
			pruneUpper()
			v := heap.Pop(upper).(int)
			upperSize--
			sumUpper -= int64(v)

			heap.Push(lower, v)
			lowerSize++
			sumLower += int64(v)

			pruneUpper()
			pruneLower()
		}

		for upperSize < lowerSize {
			pruneLower()
			v := heap.Pop(lower).(int)
			lowerSize--
			sumLower -= int64(v)

			heap.Push(upper, v)
			upperSize++
			sumUpper += int64(v)

			pruneUpper()
			pruneLower()
		}
	}

	add := func(v int) {
		pruneUpper()
		if upperSize == 0 || v >= (*upper)[0] {
			heap.Push(upper, v)
			upperSize++
			sumUpper += int64(v)
		} else {
			heap.Push(lower, v)
			lowerSize++
			sumLower += int64(v)
		}
		rebalance()
	}

	remove := func(v int) {
		pruneUpper()
		if upperSize > 0 && v >= (*upper)[0] {
			upperDel[v]++
			upperSize--
			sumUpper -= int64(v)
		} else {
			lowerDel[v]++
			lowerSize--
			sumLower -= int64(v)
		}
		rebalance()
	}

	getMinCost := func() int64 {
		pruneUpper()
		median := int64((*upper)[0])
		return sumUpper - sumLower - median*int64(upperSize-lowerSize)
	}

	for i, v := range nums {
		add(v)
		if i >= x {
			remove(nums[i-x])
		}
		if i >= x-1 {
			vals[i-x+1] = getMinCost()
		}
	}

	const inf int64 = math.MaxInt64 / 2
	dp := make([][]int64, n+1)
	for i := range dp {
		dp[i] = make([]int64, k+1)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}

	for i := n; i >= 0; i-- {
		dp[i][0] = 0
		for j := 1; j <= k; j++ {
			if n-i >= j*x {
				val := dp[i+1][j]
				if i < n && vals[i]+dp[i+x][j-1] < val {
					val = vals[i] + dp[i+x][j-1]
				}
				dp[i][j] = val
			}
		}
	}

	if dp[0][k] >= inf {
		return -1
	}
	return dp[0][k]
}