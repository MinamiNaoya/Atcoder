package main

import "fmt"

func main() {
	var N int
	fmt.Scanf("%d", &N)
	var can_do bool
	A := make([]int, N)
	can_do = true

	for i := 0; i < N+1; i++ {
		if A[i]%2 == 1 {
			can_do = false
		}
		if can_do == false {
			break
		} else {
			for x := 0; x < N; x++ {
				A[x] /= 2
			}
		}

	}
}
