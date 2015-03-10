
import java.io._

class Point(val xc: Int, val yc: Int) {
   var x: Int = xc
   var y: Int = yc
   println("Fuck yeah"+X)
   if (x>0)
      {
         x=x+600;
      }
  
   def move(dx: Int, dy: Int) {
      x = x + dx
      y = y + dy
      println ("Point x location : " + x);
      println ("Point y location : " + y);
   }
}


object Test123 {
 def main(args: Array[String]) : Unit =  {
      val loc = new Location(10, 20, 15);
val z=1
        if (z < 21)
   {
      class Point123() 
      {
     
        println ("Point y location : ");
        println ("Point z location : ");

      }
   }

      // Move to a new location
      loc.move(10, 10, 5);
      println( "Returned Valuefjvnfkldv : " + addInt(5,7) );
   }

def addInt(a:Int,b:Int ) : Int = {
      var sum:Int = 0
      sum = a + b

      return sum
   }


   object Test345 {
       def main(args: Array[String]) {
      val loc = new Location(10, 20, 15);

      // Move to a new location
      loc.move(10, 10, 5);
      println( "Returned Valuefjvnfkldv : " + addInt(5,7) );
   }

 

def addInt(a:Int,b:Int ) : Int = {
      var sum:Int = 0
      sum = a + b

      return sum
   }


}




}



// object Test345 {
 

// def addInt(a:Int,b:Int ) : Int = {
//       var sum:Int = 0
//       sum = a + b

//       return sum
//    }


// }




class Location(override val xc: Int, override val yc: Int,
   val zc :Int) extends Point(xc, yc){
   var z: Int = zc


   def move(dx: Int, dy: Int, dz: Int) {
      x = x + dx
      y = y + dy
      z = z + dz
      println ("Point x location : " + x);
      println ("Point y location : " + y);
      println ("Point z location : " + z);
      val loc=new Point123() 

   }

   private class Point123() 
   {
  
     println ("Point y location : ");
     println ("Point z location : ");

   }



}
