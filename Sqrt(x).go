import "math"

func mySqrt(x int) int{
    var i float64 = float64(x)
    var c float64 = math.Sqrt(i)
    var z float64 = math.Floor(c)
    var y int = int(z)
    
    //y float64 := float64(math.Sqrt(x))
    return y
}
