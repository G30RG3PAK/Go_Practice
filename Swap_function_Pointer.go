package main

import (
	"fmt"
)

func main() {

	
	var a int = 100
	var b int = 200
	swap(&a,&b)

	/* calling a function to swap the values.
   &a indicates pointer to a ie. address of variable a and 
   &b indicates pointer to b ie. address of variable b.
  	 */
	fmt.Println(a)
	fmt.Println(b) 
	

}

/*This function definition to swap the value*/
func swap(x, y *int){
	
	var temp int
	temp = *x //save the value at address x 
	*x = *y //put y into x
	*y = temp  //put temp into y
	
		
}

